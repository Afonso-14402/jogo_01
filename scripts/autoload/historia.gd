extends Node
## A história (docs/guiao/; dados/cenas.json): toca as cenas no momento certo e faz avançar as missões H_.
## Quando começa uma cena (o "gatilho" de cada uma, lido do campo "Quando" do guião):
##   andar    — entrar no andar N (com zona: ao chegar perto do sítio do mapa com esse nome)
##   vencer   — vencer um boss ou guardião
##   cidade   — voltar a Ascendia (com uma condição: depois de um boss)
##   falar    — falar com um NPC (com uma condição: ex. a missão H_06 no último passo)
##   interior — entrar num interior (ex. a Estalagem, à noite)
##   manual   — o código chama acontecer("…") com um pedaço do texto do "Quando" (ex. "Grande Portão Anão")
## As cenas já vistas ficam nas flags ("cena_<id>").

const RAIO_ZONA := 14.0

var _fila: Array[String] = []
var _zonas: Array = []            # [{id, p: Vector3, r}] cenas à espera de chegares perto
var _a_tocar: bool = false


func _ready() -> void:
	process_mode = Node.PROCESS_MODE_ALWAYS
	Eventos.andar_entrou.connect(_andar)
	Eventos.monstro_morto.connect(func(mid: String, _n: int): _vencer(mid))
	Eventos.missao_mudou.connect(func(_id): progressao.call_deferred())


func cenas() -> Dictionary:
	return Dados.tabela("cenas")


func vista(id: String) -> bool:
	return Jogo.tem_flag("cena_" + id)


func _pode(c: Dictionary) -> bool:
	return not vista(c.id) and Condicoes.avaliar(String(c.get("cond", "")))


## Pôr uma cena a tocar (ou na fila, se já houver uma conversa aberta).
func tocar(id: String, espera: float = 0.0) -> void:
	if vista(id) or id in _fila or not cenas().has(id):
		return
	Jogo.por_flag("cena_" + id)   # marca já: não se repete mesmo que se saia a meio
	if espera > 0.0:
		await get_tree().create_timer(espera, true).timeout
	_fila.append(id)


func _process(_delta: float) -> void:
	if not _zonas.is_empty() and Engine.get_process_frames() % 10 == 0:
		var j := get_tree().get_first_node_in_group("jogador") as Node3D
		if j and not Jogo.dentro:
			for z in _zonas.duplicate():
				if Vector2(j.global_position.x - z.p.x, j.global_position.z - z.p.z).length() < float(z.r):
					_zonas.erase(z)
					tocar(z.id)
	if _fila.is_empty() or _a_tocar:
		return
	var ui = get_tree().get_first_node_in_group("dialogo_ui")
	if ui == null or ui.ocupado:
		return
	_tocar_ja(_fila.pop_front(), ui)


func _tocar_ja(id: String, ui) -> void:
	_a_tocar = true
	var c: Dictionary = cenas()[id]
	await ui.falar(c.falas)
	_a_tocar = false


## Os efeitos ⚙ que o jogo sabe fazer (chamado pela caixa de diálogo).
func efeito(f: Dictionary) -> void:
	if f.has("missao_aceitar") and Missoes.estado(f.missao_aceitar) == "inativa":
		Missoes.aceitar(f.missao_aceitar)
	if f.has("missao_passo"):
		var id: String = f.missao_passo
		if Missoes.estado(id) == "inativa":
			Missoes.aceitar(id)
		for i in Missoes.dados(id).get("passos", []).size():
			if not Missoes.passo_feito(id, i):
				Missoes.marcar(id, i)
				break
	if f.has("missao_concluir"):
		var id: String = f.missao_concluir
		if Missoes.estado(id) == "inativa":
			Missoes.aceitar(id)
		for i in Missoes.dados(id).get("passos", []).size():
			Missoes.marcar(id, i)
		if Missoes.estado(id) == "pronta":
			Missoes.entregar(id)
	if f.has("amizade") and f.get("npc", "") != "":
		Amizade.mudar(f.npc, int(f.amizade))
	for fl in f.get("flags", []):
		Jogo.por_flag(fl)
	if f.has("titulo"):
		Jogo.por_flag("titulo_" + String(f.titulo).to_snake_case())
		Sistema.mensagem("Título novo: %s" % f.titulo, "nivel")
	for it in f.get("itens", []):
		Jogo.apanhar(it, 1)
	for s in f.get("sistema", []):
		if not String(s).begins_with("Obtiveste"):
			Sistema.mensagem(s, "missao" if "issão" in s else "sistema")
	if f.has("capitulo_pt"):
		Sistema.mensagem(f.capitulo_pt, "andar")


## As missões da história abrem sozinhas pela ordem, capítulo a capítulo (docs/MISSOES.md, H_).
func progressao() -> void:
	var por_cap := {}
	for m in Dados.tabela("missoes").values():
		if m.get("tipo", "") == "historia" and int(m.get("capitulo", 0)) >= 1:
			por_cap.get_or_add(int(m.capitulo), []).append(m.id)
	for cap in por_cap:
		if cap > Jogo.capitulo():
			continue
		var ids: Array = por_cap[cap]
		ids.sort()
		for i in ids.size():
			if Missoes.estado(ids[i]) == "inativa":
				if i == 0 or Missoes.estado(ids[i - 1]) == "concluida":
					Missoes.aceitar(ids[i])
				break
			if Missoes.estado(ids[i]) != "concluida":
				break


# ------------------------------------------------------------------ gatilhos ------------------------------------------------------------------

func _andar(n: int) -> void:
	_zonas.clear()
	progressao()
	await get_tree().process_frame
	var andar := get_tree().current_scene as Andar
	for c in cenas().values():
		var g: Dictionary = c.gatilho
		if g.tipo != "andar" or int(g.andar) != n or not _pode(c):
			continue
		var z := _sitio(andar, String(g.get("zona", "")))
		if z.is_empty():
			tocar(c.id, 1.5)
		else:
			z["id"] = c.id
			_zonas.append(z)


## O sítio do mapa com o nome da zona: {p, r} (as zonas do andar, senão os textos dos pontos); {} se não houver.
func _sitio(andar: Andar, zona: String) -> Dictionary:
	if andar == null or zona == "":
		return {}
	var z := _limpo(zona)
	for zz in andar.dados.get("zonas", []):
		var r: Array = zz.get("rect", [])
		if z in _limpo(String(zz.get("nome", ""))) and r.size() == 4:
			var meio: Vector3 = (andar.centro_celula(int(r[0]), int(r[1])) + andar.centro_celula(int(r[2]), int(r[3]))) / 2.0
			return {"p": meio, "r": maxf(absf(r[2] - r[0]), absf(r[3] - r[1])) * Andar.CEL / 2.0 + 6.0}
	for p in andar.dados.get("pontos", []):
		if z in _limpo(String(p.texto)):
			return {"p": andar.centro_celula(int(p.x), int(p.y)), "r": RAIO_ZONA}
	return {}


func _limpo(t: String) -> String:
	t = t.to_lower()
	for a in [["á", "a"], ["à", "a"], ["ã", "a"], ["â", "a"], ["é", "e"], ["ê", "e"], ["í", "i"], ["ó", "o"], ["õ", "o"], ["ô", "o"], ["ú", "u"], ["ç", "c"]]:
		t = t.replace(a[0], a[1])
	return t


func _vencer(mid: String) -> void:
	for c in cenas().values():
		if c.gatilho.tipo == "vencer" and c.gatilho.monstro == mid and _pode(c):
			tocar(c.id, 2.5)


## Entraste em Ascendia (scripts/mundo/cidade.gd): uma cena de cada vez.
func entrou_cidade() -> void:
	progressao()
	for c in cenas().values():
		if c.gatilho.tipo == "cidade" and _pode(c):
			tocar(c.id, 1.5)
			return


func entrou_interior(tipo: String) -> void:
	for c in cenas().values():
		if c.gatilho.tipo == "interior" and c.gatilho.get("interior", "") == tipo and _pode(c):
			tocar(c.id, 0.8)
			return


## A cena que este NPC tem para ti agora (ou ""): o NPC toca-a em vez da conversa normal.
func cena_npc(npc: String) -> String:
	for c in cenas().values():
		if c.gatilho.tipo == "falar" and c.gatilho.npc == npc and _pode(c):
			return c.id
	return ""


## Falar com um NPC que tem uma cena: toca-a já (devolve true se tocou).
func falar_npc(npc: String, ui) -> bool:
	var id := cena_npc(npc)
	if id == "":
		return false
	Jogo.por_flag("cena_" + id)
	_a_tocar = true
	await ui.falar(cenas()[id].falas, npc)
	_a_tocar = false
	return true


## Gatilhos "manuais": o código diz o que aconteceu ("Grande Portão Anão") e toca a cena cujo "Quando" o diz.
func acontecer(chave: String) -> void:
	var k := _limpo(chave)
	for c in cenas().values():
		if c.gatilho.tipo == "manual" and k in _limpo(String(c.quando_pt)) and _pode(c):
			tocar(c.id, 0.5)
			return
