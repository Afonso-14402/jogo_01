extends Node
## Missões (docs/MISSOES.md; docs/SISTEMAS.md, secção 16): aceitar, contar os passos, entregar e dar as recompensas.
## Estados: inativa → ativa → pronta (entregar a quem a deu) → concluida. Máximo de 10 missões ativas (a história não conta).
## O quadro da Guilda tem as missões fixas do teu rank e 3 missões novas por dia (geradas).
## O estado fica em Jogo.missoes[id] = {"estado", "prog": [n por passo]} e o quadro do dia em Jogo.quadro.


func _ready() -> void:
	Eventos.monstro_morto.connect(_monstro_morto)
	Eventos.item_apanhado.connect(func(_i, _q): _contar_itens())
	Eventos.andar_entrou.connect(_andar)
	Tempo.novo_dia.connect(func(_d): gerar_quadro())


func dados(id: String) -> Dictionary:
	var d := Dados.obter("missoes", id)
	if d.is_empty():
		for g in Jogo.quadro:
			if g.id == id:
				return g
	return d


func estado(id: String) -> String:
	return Jogo.estado_missao(id)


func _reg(id: String) -> Dictionary:
	if not (Jogo.missoes.get(id) is Dictionary):
		Jogo.missoes[id] = {"estado": "inativa", "prog": []}
	return Jogo.missoes[id]


func ativas() -> Array:
	var r := []
	for id in Jogo.missoes:
		if estado(id) in ["ativa", "pronta"]:
			r.append(id)
	return r


func pode_aceitar(id: String) -> String:
	var d := dados(id)
	if d.is_empty():
		return "Esta missão não existe."
	if estado(id) != "inativa":
		return "Já aceitaste esta missão."
	if d.get("tipo", "") != "historia":
		var n := ativas().filter(func(x): return dados(x).get("tipo", "") != "historia").size()
		if n >= int(Dados.c("missoes_max_ativas", 10)):
			return "Já tens 10 missões aceites."
	if d.get("rank", "") != "" and Condicoes.RANKS.find(d.rank) > Condicoes.RANKS.find(Jogo.rank()):
		return "Precisas do rank %s." % d.rank
	return ""


func aceitar(id: String) -> bool:
	if pode_aceitar(id) != "":
		Sistema.mensagem(pode_aceitar(id), "aviso")
		return false
	var d := dados(id)
	var r := _reg(id)
	r.estado = "ativa"
	r.prog = []
	for p in d.get("passos", []):
		r.prog.append(0)
	Sistema.mensagem("Missão aceite: %s%s" % ["⭐ " if d.get("tipo", "") == "historia" else "", d.get("nome_pt", id)], "missao")
	_contar_itens()
	_verificar(id)
	Eventos.missao_mudou.emit(id)
	return true


## Quanto falta de um passo: [feito, preciso]
func progresso(id: String, i: int) -> Array:
	var p: Dictionary = dados(id).get("passos", [])[i]
	var prog: Array = _reg(id).get("prog", [])
	var feito := int(prog[i]) if i < prog.size() else 0
	return [feito, int(p.get("qtd", 1))]


func passo_feito(id: String, i: int) -> bool:
	var pr := progresso(id, i)
	return pr[0] >= pr[1]


## Marca um passo "livre" (ou qualquer outro) como feito — as cenas e eventos da história usam isto.
func marcar(id: String, i: int) -> void:
	if estado(id) != "ativa":
		return
	var r := _reg(id)
	var p: Dictionary = dados(id).passos[i]
	r.prog[i] = int(p.get("qtd", 1))
	_verificar(id)


func _verificar(id: String) -> void:
	if estado(id) != "ativa":
		return
	for i in dados(id).get("passos", []).size():
		if not passo_feito(id, i):
			return
	_reg(id).estado = "pronta"
	var d := dados(id)
	var quem: String = Dados.obter("npcs", d.get("dada_por", "")).get("nome_pt", "")
	Sistema.mensagem("Missão pronta: %s%s" % [d.get("nome_pt", id), (" — fala com %s." % quem) if quem != "" else "."], "missao")
	Eventos.missao_mudou.emit(id)
	if quem == "" and d.get("tipo", "") != "guilda":   # sem ninguém a quem entregar: acaba logo
		entregar(id)


func _monstro_morto(mid: String, _nivel: int) -> void:
	for id in ativas():
		if estado(id) != "ativa":
			continue
		var passos: Array = dados(id).get("passos", [])
		for i in passos.size():
			var p: Dictionary = passos[i]
			if p.tipo in ["matar", "derrotar"] and p.get("monstro", "") == mid and not passo_feito(id, i):
				if p.has("andar") and int(p.andar) != Jogo.andar_atual:
					continue
				if p.get("noite", false) and not Tempo.e_noite():
					continue
				_reg(id).prog[i] = int(_reg(id).prog[i]) + 1
				var pr := progresso(id, i)
				if p.tipo == "matar":
					Sistema.mensagem("%s: %d/%d" % [dados(id).nome_pt, pr[0], pr[1]], "missao")
		_verificar(id)


func _contar_itens() -> void:
	for id in ativas():
		var passos: Array = dados(id).get("passos", [])
		for i in passos.size():
			if passos[i].tipo == "apanhar":
				_reg(id).prog[i] = mini(Jogo.inventario.contar(passos[i].item), int(passos[i].qtd))
		if estado(id) == "pronta":   # deitaste os itens fora: volta a ativa
			for i in passos.size():
				if passos[i].tipo == "apanhar" and not passo_feito(id, i):
					_reg(id).estado = "ativa"
		_verificar(id)


func _andar(n: int) -> void:
	for id in ativas():
		var passos: Array = dados(id).get("passos", [])
		for i in passos.size():
			if passos[i].tipo == "ir_a" and n >= int(passos[i].andar):
				_reg(id).prog[i] = 1
		_verificar(id)


func explorou(andar: int, pct: float) -> void:
	for id in ativas():
		var passos: Array = dados(id).get("passos", [])
		for i in passos.size():
			if passos[i].tipo == "explorar" and int(passos[i].andar) == andar and pct >= float(passos[i].percent):
				_reg(id).prog[i] = 1
		_verificar(id)


## Entregar: tira os itens pedidos e dá as recompensas.
func entregar(id: String) -> bool:
	if estado(id) != "pronta":
		return false
	var d := dados(id)
	for p in d.get("passos", []):
		if p.tipo == "apanhar":
			Jogo.inventario.retirar(p.item, int(p.qtd))
	var r: Dictionary = d.get("recompensas", {})
	var c := Dados.constantes
	var xp := int(r.get("xp", Formulas.xp_monstro(c, maxi(1, Jogo.andar_maximo)) * int(c.get("missao_xp_monstros", 5))))
	Jogo.ganhar_xp(xp)
	if int(r.get("ouro", 0)) > 0:
		Jogo.ganhar_ouro(int(r.ouro))
	for it in r.get("itens", []):
		Jogo.apanhar(it[0], int(it[1]))
	for npc in r.get("amizade", {}):
		Amizade.mudar(npc, int(r.amizade[npc]))
	for rc in r.get("receitas", []):
		Jogo.aprender_receita(rc)
	for f in r.get("flags", []):
		Jogo.por_flag(f)
	if r.has("titulo"):
		Jogo.por_flag("titulo_" + String(r.titulo).to_snake_case())
		Sistema.mensagem("Título novo: %s" % r.titulo, "nivel")
	var pontos := int(r.get("pontos_guilda", 0))
	if pontos > 0:
		var antes := Jogo.rank()
		Jogo.pontos_guilda += pontos
		if Jogo.rank() != antes:
			Sistema.mensagem("Subiste para o rank %s!" % Jogo.rank(), "nivel")
	_reg(id).estado = "concluida"
	Jogo.por_flag("missao_" + id)
	Sistema.mensagem("Missão concluída: %s (+%d XP%s)" % [d.get("nome_pt", id), xp, (", +%d ouro" % int(r.ouro)) if int(r.get("ouro", 0)) > 0 else ""], "missao")
	if d.get("gerada", false):
		Jogo.quadro_feitas_hoje += 1
		if Jogo.quadro_feitas_hoje == int(c.get("quadro_bau_prata", 3)):
			Sistema.mensagem("Fizeste 3 missões do quadro hoje: a Guilda dá-te um baú de prata!", "nivel")
			var cont := Loot.bau(c, "prata", Jogo.andar_maximo, clampi((Jogo.andar_maximo - 1) / 10 + 1, 1, 10), Jogo.a("sor"), RandomNumberGenerator.new())
			for it in cont.itens:
				Jogo.apanhar(it[0], int(it[1]), it[2])
			Jogo.ganhar_ouro(int(cont.ouro))
	Eventos.missao_mudou.emit(id)
	return true


# ------------------------------------------------------------------ quadro da Guilda ------------------------------------------------------------------

## As missões fixas do teu rank (ainda por fazer) e as 3 do dia.
func quadro_disponiveis() -> Array:
	var r := []
	for m in Dados.tabela("missoes").values():
		if m.tipo == "guilda" and estado(m.id) == "inativa" and Condicoes.RANKS.find(m.rank) <= Condicoes.RANKS.find(Jogo.rank()):
			r.append(m)
	for g in Jogo.quadro:
		if estado(g.id) == "inativa":
			r.append(g)
	return r


## 3 missões novas por dia (docs/MISSOES.md, secção 4): caça e recolha, com o que já desbloqueaste.
func gerar_quadro(rng: RandomNumberGenerator = null) -> void:
	if rng == null:
		rng = RandomNumberGenerator.new()
		rng.seed = hash([Tempo.ano, Tempo.estacao, Tempo.dia, "quadro"])
	var c := Dados.constantes
	Jogo.quadro = []
	Jogo.quadro_feitas_hoje = 0
	var rank: String = Jogo.rank()
	var ri := Condicoes.RANKS.find(rank)
	var dia := Amizade.dia_absoluto()
	for n in int(c.get("missoes_quadro_por_dia", 3)):
		var andar := rng.randi_range(maxi(1, Jogo.andar_maximo - 5), Jogo.andar_maximo)
		var dados_andar := Dados.tabela("andares/a%03d" % andar)
		var nivel := int(dados_andar.get("nivel", andar))
		var r_m: String = Condicoes.RANKS[maxi(0, ri - rng.randi_range(0, 1))]
		var g := {"id": "GQ_%d_%d" % [dia, n], "tipo": "guilda", "gerada": true, "rank": r_m, "dada_por": "lyra"}
		var monstros: Array = dados_andar.get("monstros", [])
		if rng.randf() < 0.6 and not monstros.is_empty():
			var mid: String = monstros[rng.randi() % monstros.size()]
			var q := rng.randi_range(6, 14)
			g["nome_pt"] = "Caça: %s" % Dados.monstro(mid).get("nome_pt", mid)
			g["descricao_pt"] = "Matar %d %s no andar %d." % [q, Dados.monstro(mid).get("nome_pt", mid), andar]
			g["passos"] = [{"tipo": "matar", "monstro": mid, "qtd": q, "andar": andar}]
			g["recompensas"] = {"ouro": int(c.missao_ouro_modelo.caca) * nivel, "pontos_guilda": int(c.missao_pontos_rank[r_m])}
		else:
			var recursos: Array = Dados.lista_simples("recursos").filter(func(x): return float(andar) in x.andares and not x.raro)
			if recursos.is_empty():
				continue
			var it: String = recursos[rng.randi() % recursos.size()].item
			var q := rng.randi_range(5, 15)
			var preco := maxi(5, int(Inventario._dados(it).get("preco", 10)))
			g["nome_pt"] = "Recolha: %s" % Inventario._dados(it).get("nome_pt", it)
			g["descricao_pt"] = "Trazer %d %s." % [q, Inventario._dados(it).get("nome_pt", it)]
			g["passos"] = [{"tipo": "apanhar", "item": it, "qtd": q}]
			g["recompensas"] = {"ouro": int(preco * q * float(c.missao_ouro_modelo.recolha)), "pontos_guilda": int(c.missao_pontos_rank[r_m])}
		Jogo.quadro.append(g)
