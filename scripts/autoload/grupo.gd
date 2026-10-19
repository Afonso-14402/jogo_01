extends Node
## O grupo de companheiros (docs/SISTEMAS.md, secção 20; quem são: docs/NPCS.md, secção 4; dados: dados/companheiros.json).
## O estado fica em Jogo (companheiros = a equipa; grupo = conhecidos e o que cada um leva) para se gravar com o resto.
## Aqui está a lógica: contratar, entrar e sair da equipa, valores (nível, HP, ATQ, DEF), dar itens, ensinar skills,
## ordens, as habilidades especiais dos escondidos e pôr os companheiros (e os escondidos) nos andares.

const ORDENS := ["atacar", "defender", "ficar", "seguir"]
const NOMES_ORDENS := {"atacar": "Atacar", "defender": "Defender-me", "ficar": "Ficar", "seguir": "Seguir"}
const MATERIAIS := ["cobre", "ferro", "aco", "prata", "gelo_eterno", "coral_abissal", "obsidiana", "mitril", "oricalco", "estelar"]
const ESPACOS := ["cabeca", "corpo", "maos", "pes"]

var _andar_antes: int = -1
var _regen_t: float = 0.0


func _ready() -> void:
	get_tree().node_added.connect(_no_novo)


# ------------------------------------------------------------------ dados ------------------------------------------------------------------

func c(chave: String, padrao: Variant = null) -> Variant:
	return Dados.c("companheiros", {}).get(chave, padrao)


func dados(id: String) -> Dictionary:
	return Dados.obter("companheiros", id)


func todos() -> Array:
	return Dados.tabela("companheiros").values()


func conhecidos() -> Array:
	return Jogo.grupo.get_or_add("conhecidos", [])


func conhecido(id: String) -> bool:
	return id in conhecidos()


func na_equipa(id: String) -> bool:
	return id in Jogo.companheiros


## Pode ser contratado/convidado agora (a condição do JSON está feita).
func disponivel(id: String) -> bool:
	var d := dados(id)
	return not d.is_empty() and Condicoes.avaliar(String(d.get("condicao", "")))


## O que cada um leva: arma, peças, poções, skill ensinada, ordem.
func estado(id: String) -> Dictionary:
	var por: Dictionary = Jogo.grupo.get_or_add("dados", {})
	var e: Dictionary = por.get_or_add(id, {})
	for k in [["arma", {}], ["pecas", {}], ["pocoes", []], ["ensinada", ""], ["ordem", "atacar"]]:
		if not e.has(k[0]):
			e[k[0]] = k[1].duplicate() if k[1] is Dictionary or k[1] is Array else k[1]
	return e


# ------------------------------------------------------------------ entrar e sair ------------------------------------------------------------------

## Contratar (Guilda), convidar (história) ou recrutar (escondido): paga o preço e entra na equipa se houver lugar.
func recrutar(id: String) -> bool:
	var d := dados(id)
	if d.is_empty() or conhecido(id):
		return false
	if not disponivel(id):
		Sistema.mensagem("%s ainda não quer vir contigo." % d.nome_pt, "aviso")
		return false
	var preco := int(d.get("preco", 0))
	if Jogo.ouro < preco:
		Sistema.mensagem("Precisas de %d de ouro." % preco, "aviso")
		Audio.efeito("sem_dinheiro", 0.0)
		return false
	if preco > 0:
		Jogo.ganhar_ouro(-preco)
	conhecidos().append(id)
	estado(id)
	Sistema.mensagem("%s juntou-se a ti!" % d.nome_pt, "nivel")
	Colecoes.contar("companheiros")
	if Jogo.companheiros.size() < int(c("maximo", 3)):
		juntar(id)
	else:
		Sistema.mensagem("A equipa está cheia: troca na janela Grupo (tecla G).")
	return true


func juntar(id: String) -> bool:
	if not conhecido(id) or na_equipa(id) or Jogo.companheiros.size() >= int(c("maximo", 3)):
		return false
	Jogo.companheiros.append(id)
	_chamar_um(id)
	Eventos.stats_mudaram.emit()
	return true


func sair(id: String) -> void:
	Jogo.companheiros.erase(id)
	for n in get_tree().get_nodes_in_group("companheiros"):
		if n.id == id:
			n.queue_free()
	Eventos.stats_mudaram.emit()


# ------------------------------------------------------------------ valores ------------------------------------------------------------------

func nivel(_id: String = "") -> int:
	return maxi(1, Jogo.nivel - int(c("nivel_menos", 2)))


func atributos(id: String) -> Dictionary:
	var d := dados(id)
	var n := nivel(id)
	var a := {}
	for k in Jogo.ATRIBUTOS:
		a[k] = int(Dados.c("atributo_inicial", 5))
	var cres: Dictionary = d.get("crescimento", {})
	for k in cres:
		a[k] = int(a.get(k, 5)) + int(cres[k]) * (n - 1)
	return a


## Multiplicador do tipo (Guilda ×0,85, escondidos ×1,1, história ×1).
func mult_origem(id: String) -> float:
	match String(dados(id).get("origem", "")):
		"guilda": return float(c("guilda_mult", 0.85))
		"escondido": return float(c("escondido_mult", 1.1))
	return 1.0


func tier(id: String) -> int:
	return clampi(1 + (nivel(id) - 1) / 10, 1, MATERIAIS.size())


## A arma que usa: a que lhe deste ({id, melhoria, raridade...}) ou a própria (tier do nível, gasta).
func arma(id: String) -> Dictionary:
	var dada: Dictionary = estado(id).arma
	if not dada.is_empty() and not Dados.arma(String(dada.get("id", ""))).is_empty():
		return Dados.arma(dada.id)
	var tipo := String(dados(id).get("arma", "espada"))
	var a := Dados.arma("%s_%s" % [tipo, MATERIAIS[tier(id) - 1]])
	return a if not a.is_empty() else Dados.arma(tipo + "_cobre")


func mult_arma(id: String) -> float:
	var dada: Dictionary = estado(id).arma
	if dada.is_empty():
		return float(c("arma_propria_mult", 0.9))
	return Crafting.mult_instancia(Dados.constantes, dada)


func hp_max(id: String) -> float:
	var a := atributos(id)
	return Formulas.hp_maximo(Dados.constantes, int(a.vit), nivel(id)) * mult_origem(id)


func atq(id: String) -> float:
	var a := atributos(id)
	var w := arma(id)
	var k := Dados.constantes
	var v: float
	if w.get("tipo", "") == "cajado":
		v = Formulas.atq_magico(k, float(w.get("atq_magico", 0)), 0, 1.0, int(a["int"]))
	else:
		v = Formulas.atq_fisico(k, float(w.get("atq", 0)), 0, 1.0, int(a["for"]), int(a.des), bool(w.get("distancia", false)))
	return v * mult_arma(id) * mult_origem(id) * (1.0 + bonus("atq"))


## DEF e RES: as peças dadas + a armadura leve própria em cada espaço vazio + VIT.
func defesa(id: String) -> Array:
	var a := atributos(id)
	var pecas: Dictionary = estado(id).pecas
	var df := 0.0
	var rs := 0.0
	var conj := _conjunto_tier(tier(id))
	for esp in ESPACOS:
		var e: Dictionary = pecas.get(esp, {})
		if not e.is_empty():
			var d := Inventario._dados(String(e.get("id", "")))
			var m := Crafting.mult_instancia(Dados.constantes, e)
			df += float(d.get("def", 0)) * m
			rs += float(d.get("res", 0)) * m
		elif conj.has(esp):
			df += float(conj[esp][0]) * float(c("armadura_propria", 0.5))
			rs += float(conj[esp][1]) * float(c("armadura_propria", 0.5))
	var k := Dados.constantes
	var mb := 1.0 + bonus("def")
	return [Formulas.defesa(k, df, int(a.vit)) * mb, Formulas.resistencia(k, rs, int(a.vit), int(a["int"])) * mb]


static var _conjuntos: Dictionary = {}


## As peças "normais" de armadura de um tier (para a armadura própria): espaço -> [def, res].
func _conjunto_tier(t: int) -> Dictionary:
	if _conjuntos.is_empty():
		for it in Dados.tabela("itens").values():
			if it.get("categoria", "") == "armadura" and String(it.get("espaco", "")) in ESPACOS and it.has("tier"):
				var por: Dictionary = _conjuntos.get_or_add(int(it.tier), {})
				if not por.has(it.espaco):
					por[it.espaco] = [float(it.get("def", 0)), float(it.get("res", 0))]
	return _conjuntos.get(t, {})


## A skill ensinada (uma das tuas skills ativas do tipo da arma dele).
func skills_para_ensinar(id: String) -> Array:
	var tipos: Array = dados(id).get("armas", [])
	var r := []
	for s in Jogo.skills_ativas():
		if s.has("arma") and s.arma in tipos and s.get("forma", "") != "buff":
			r.append(s)
	return r


func ensinar(id: String, skill_id: String) -> void:
	estado(id).ensinada = skill_id
	Sistema.mensagem("%s aprendeu %s." % [dados(id).nome_pt, Jogo.skill(skill_id).get("nome_pt", skill_id)], "nivel")


# ------------------------------------------------------------------ dar e tirar itens ------------------------------------------------------------------

func pode_usar_arma(id: String, arma_id: String) -> bool:
	return String(Dados.arma(arma_id).get("tipo", "")) in dados(id).get("armas", [])


## Dá a arma do espaço i da mochila (a que ele tinha volta para a mochila).
func dar_arma(id: String, i: int) -> bool:
	var e = Jogo.inventario.espacos[i]
	if e == null or not pode_usar_arma(id, e.id):
		return false
	Jogo.inventario.espacos[i] = null
	tirar_arma(id)
	estado(id).arma = e
	Jogo.inventario.mudou.emit()
	_atualizar(id)
	return true


func tirar_arma(id: String) -> void:
	var velha: Dictionary = estado(id).arma
	if not velha.is_empty() and Jogo.inventario.adicionar_instancia(velha):
		estado(id).arma = {}
	_atualizar(id)


func dar_peca(id: String, i: int) -> bool:
	var e = Jogo.inventario.espacos[i]
	if e == null:
		return false
	var d := Inventario._dados(e.id)
	if d.get("categoria", "") != "armadura" or not String(d.get("espaco", "")) in ESPACOS:
		return false
	Jogo.inventario.espacos[i] = null
	tirar_peca(id, d.espaco)
	estado(id).pecas[d.espaco] = e
	Jogo.inventario.mudou.emit()
	_atualizar(id)
	return true


func tirar_peca(id: String, esp: String) -> void:
	var velha: Dictionary = estado(id).pecas.get(esp, {})
	if not velha.is_empty() and Jogo.inventario.adicionar_instancia(velha):
		estado(id).pecas.erase(esp)
	_atualizar(id)


## Poções de vida que tens (as que curam HP), da melhor para a pior.
func pocoes_na_mochila() -> Array:
	var r := []
	for it in ["pocao_vida_maxima", "pocao_vida_g", "pocao_vida_m", "pocao_vida_p"]:
		if Jogo.inventario.tem(it):
			r.append(it)
	return r


func dar_pocao(id: String) -> bool:
	var lista: Array = estado(id).pocoes
	var p := pocoes_na_mochila()
	if p.is_empty() or lista.size() >= int(c("pocoes_max", 5)):
		return false
	Jogo.inventario.retirar(p[-1], 1)   # dá primeiro as mais fracas
	lista.append(p[-1])
	return true


func tirar_pocoes(id: String) -> void:
	var lista: Array = estado(id).pocoes
	for it in lista:
		Jogo.inventario.adicionar(it, 1)
	lista.clear()


## Quanto uma poção cura (em fração do HP máximo, ou HP fixo) a um companheiro.
func cura_pocao(item: String, hp_maximo: float) -> float:
	var ef: Dictionary = Inventario._dados(item).get("efeito", {})
	return hp_maximo * float(ef.get("curar_hp_percent", 0.0)) + float(ef.get("curar_hp", 0.0))


# ------------------------------------------------------------------ ordens ------------------------------------------------------------------

func ordem(id: String) -> String:
	return String(estado(id).ordem)


func mudar_ordem(id: String, o: String) -> void:
	estado(id).ordem = o


func rodar_ordens() -> void:
	if Jogo.companheiros.is_empty():
		return
	var atual := ordem(Jogo.companheiros[0])
	var nova: String = ORDENS[(ORDENS.find(atual) + 1) % ORDENS.size()]
	for id in Jogo.companheiros:
		mudar_ordem(id, nova)
	Sistema.mensagem("Ordem ao grupo: %s." % NOMES_ORDENS[nova])
	Audio.efeito("aceitar", 0.0)


func _unhandled_input(e: InputEvent) -> void:
	if e.is_action_pressed("ordem_grupo") and not get_tree().paused:
		rodar_ordens()


# ------------------------------------------------------------------ habilidades especiais ------------------------------------------------------------------

## A habilidade especial ativa no grupo (de um companheiro na equipa que esteja de pé), ou {}.
func especial(nome: String) -> Dictionary:
	for id in Jogo.companheiros:
		var es: Dictionary = dados(id).get("especial", {})
		if es.get("id", "") == nome and _de_pe(id):
			return es
	return {}


func _de_pe(id: String) -> bool:
	for n in get_tree().get_nodes_in_group("companheiros"):
		if n.id == id:
			return n.estado != "morto"
	return true   # fora dos andares (sem boneco) conta como presente


## Bónus ao grupo todo (tu também): "atq", "def" (Bênção Estelar).
func bonus(stat: String) -> float:
	if stat in ["atq", "def"]:
		return float(especial("bencao_estelar").get("valor", 0.0))
	return 0.0


func mult_ouro() -> float:
	return 1.0 + float(especial("maos_leves").get("valor", 0.0))


func raio_iman(base: float) -> float:
	return maxf(base, float(especial("lingua_comprida").get("valor", 0.0)))


## Renascer (Brasa): uma vez por andar, quando cais, levantas-te com 50%.
func tentar_renascer() -> bool:
	var es := especial("renascer")
	if es.is_empty() or Jogo.grupo.get("renascer_andar", -1) == Jogo.andar_atual:
		return false
	Jogo.grupo["renascer_andar"] = Jogo.andar_atual
	Jogo.hp = Jogo.hp_maximo() * float(es.get("valor", 0.5))
	Sistema.mensagem("Renascer! A Brasa levanta-te das cinzas.", "nivel")
	return true


func _process(delta: float) -> void:
	var es := especial("remedio_do_mato")
	if es.is_empty() or get_tree().paused:
		return
	_regen_t += delta
	if _regen_t < float(es.get("intervalo", 5.0)):
		return
	_regen_t = 0.0
	if Jogo.hp > 0.0:
		Jogo.curar(Jogo.hp_maximo() * float(es.valor))
	for n in get_tree().get_nodes_in_group("companheiros"):
		n.curar(n.hp_max * float(es.valor))


# ------------------------------------------------------------------ nos andares ------------------------------------------------------------------

## Quando o herói aparece num andar da torre, os companheiros aparecem ao lado dele (e o escondido do andar, se houver).
func _no_novo(n: Node) -> void:
	if n is Jogador:
		_chamar.call_deferred(n)


func _no_andar(j: Node) -> Andar:
	var p := j.get_parent()
	while p and not p is Andar:
		p = p.get_parent()
	return p as Andar


func _chamar(j: Variant) -> void:   # (Variant: o herói pode já ter sido apagado quando isto corre)
	if not is_instance_valid(j):
		return
	var andar := _no_andar(j)
	if andar == null:
		_andar_antes = -1
		return
	if _andar_antes > 0 and Jogo.andar_atual == _andar_antes + 1:   # subiste um andar com eles: +5 de amizade
		for id in Jogo.companheiros:
			Amizade.mudar(id, int(c("amizade_andar", 5)))
	_andar_antes = Jogo.andar_atual
	for id in Jogo.companheiros:
		_chamar_um(id)
	_por_escondido(andar)


func _chamar_um(id: String) -> void:
	var j := get_tree().get_first_node_in_group("jogador") as Node3D
	if j == null or _no_andar(j) == null:
		return
	for n in get_tree().get_nodes_in_group("companheiros"):
		if n.id == id:
			return
	var comp := Companheiro.new()
	comp.id = id
	var i := Jogo.companheiros.find(id)
	var lado := Vector3(-1.4 + 1.4 * i, 0.3, 1.2)
	j.get_parent().add_child(comp)
	comp.global_position = j.global_position + lado


func _atualizar(id: String) -> void:
	for n in get_tree().get_nodes_in_group("companheiros"):
		if n.id == id:
			n.recalcular()
	Eventos.stats_mudaram.emit()


## O escondido deste andar (se ainda não o recrutaste): num sítio afastado da chegada.
func _por_escondido(andar: Andar) -> void:
	for d in todos():
		if d.get("origem", "") != "escondido" or int(d.get("andar", 0)) != andar.numero or conhecido(d.id):
			continue
		var p := andar.ponto_bicho(andar.ponto_chegada, 30.0)
		if p == Vector3.INF:
			p = andar.ponto_bicho(Vector3.INF, 0.0)
		if p == Vector3.INF:
			return
		var e := Escondido.new()
		e.id = d.id
		andar.add_child(e)
		e.global_position = p + Vector3(0, 0.3, 0)
