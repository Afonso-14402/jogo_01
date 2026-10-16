extends Node
## O estado do jogo: jogador (nível, atributos, HP...), ouro, andares, flags, amizades, missões.
## As fórmulas estão em Formulas (scripts/sistemas/formulas.gd) e os números em dados/constantes.json.

const ATRIBUTOS := ["for", "agi", "des", "int", "vit", "sor"]

var nome: String = "Jogador"
var tratamento: String = "ele"
var nivel: int = 1
var xp: int = 0
var atributos: Dictionary = {}
var pontos_livres: int = 0
var hp: float = 0.0
var mp: float = 0.0
var estamina: float = 0.0
var ouro: int = 0
var arma_equipada: String = "espada_cobre"
var arma_2: String = ""
var inventario := Inventario.new(30)
var azar_baus: int = 0   # baús de prata/ouro sem Épico (proteção contra azar)
var materiais_andar: Dictionary = {}   # materiais apanhados neste andar desde a última Zona Segura
var dificuldade: String = "normal"
var aparencia: Dictionary = {"penteado": "espetado", "pele": "clara", "cabelo": "castanho_avermelhado", "olhos": "preto", "roupa": "aventureiro"}

var andar_maximo: int = 1
var andar_atual: int = 1
var flags: Array[String] = []
var amizade: Dictionary = {}
var missoes: Dictionary = {}
var tempo_jogado: float = 0.0

# bónus vindos do equipamento (o inventário preenche isto)
var origem: String = ""          # docs/PROGRESSAO.md, 1.1 (atrasado, jogador, ajudante, dormir)
var skill_unica: String = ""      # sorteada pelo Cristal de Avaliação
var classe: String = ""           # "" = Aventureiro (até ao nível 10)
var skills_arma: Dictionary = {}  # tipo de arma -> pontos
var skills_vida: Dictionary = {}  # mineracao, pesca... -> ações
var skills_barra: Array = ["", "", "", "", "", ""]   # ids de skills nas teclas 1–6
var pontos_guilda: int = 0
var segunda_vida_usada: bool = false
var estados: Node = null   # os estados do herói (Estados), quando está no mundo
var buffs: Dictionary = {}   # stat -> [valor, segundos que faltam] (poções de força, defesa, velocidade, regeneração)
var bonus := {"hp": 0, "def": 0.0, "res": 0.0, "critico": 0.0}


func _ready() -> void:
	novo_jogo()


## Bónus temporário (1.0 = nada; 1.2 = +20%).
func buff(stat: String) -> float:
	return 1.0 + float(buffs.get(stat, [0.0, 0.0])[0])


func _tratar_buffs(delta: float) -> void:
	for k in buffs.keys():
		buffs[k][1] -= delta
		if k == "regenerar" and hp > 0.0:
			hp = min(float(hp_maximo()), hp + hp_maximo() * float(buffs[k][0]) * delta)
		if buffs[k][1] <= 0.0:
			buffs.erase(k)
			Eventos.stats_mudaram.emit()


func _process(delta: float) -> void:
	_tratar_buffs(delta)
	tempo_jogado += delta


func novo_jogo(nome_jogador: String = "Jogador") -> void:
	nome = nome_jogador
	buffs.clear()
	origem = ""
	skill_unica = ""
	classe = ""
	skills_arma.clear()
	skills_vida.clear()
	skills_barra = ["", "", "", "", "", ""]
	pontos_guilda = 0
	nivel = 1
	xp = 0
	pontos_livres = 0
	ouro = 0
	andar_maximo = 1
	flags.clear()
	amizade.clear()
	missoes.clear()
	for a in ATRIBUTOS:
		atributos[a] = int(Dados.c("atributo_inicial", 5))
	inventario = Inventario.new(int(Dados.c("mochila", 30)))
	inventario.adicionar("espada_cobre")
	inventario.adicionar("pocao_vida_p", 3)
	inventario.barra_rapida[0] = "pocao_vida_p"
	arma_equipada = "espada_cobre"
	arma_2 = ""
	azar_baus = 0
	materiais_andar.clear()
	encher()


func a(nome_atributo: String) -> int:
	return int(atributos.get(nome_atributo, 0))


# ---------------- valores derivados ----------------

func hp_maximo() -> int:
	return int(Formulas.hp_maximo(Dados.constantes, a("vit"), nivel, bonus.hp) * (1.0 + passivo("hp")))


func mp_maximo() -> int:
	return int(Formulas.mp_maximo(Dados.constantes, a("int"), nivel) * (1.0 + passivo("mp")))


func estamina_maxima() -> int:
	return int(Formulas.estamina_maxima(Dados.constantes, a("agi")) * (1.0 + passivo("estamina")))


func velocidade() -> float:
	return Formulas.velocidade(Dados.constantes, a("agi")) * buff("velocidade") * (1.0 + passivo("velocidade"))


func critico(bonus_arma: float = 0.0) -> float:
	return Formulas.critico(Dados.constantes, a("des"), a("sor"), bonus_arma + bonus.critico + passivo("critico"))


func defesa() -> float:
	return Formulas.defesa(Dados.constantes, bonus["def"], a("vit")) * buff("def") * (1.0 + passivo("def"))


# ---------------- Sistema isekai: origem, classe, skills (docs/PROGRESSAO.md) ----------------

## Soma dos bónus passivos de um stat: origem + classe base + skills passivas já desbloqueadas.
func passivo(stat: String) -> float:
	var t := 0.0
	for b in Dados.obter("origens", origem).get("bonus", []):
		if b.stat == stat:
			t += float(b.valor)
	var linha := Progressao.linha_classes(classe)
	if not linha.is_empty() and stat != "atq":   # o bónus de ATQ da classe só conta com as armas preferidas
		for b in linha[0].get("bonus", []):
			if b.stat == stat:
				t += float(b.valor)
	for s in Progressao.skills_classe(classe, nivel):
		for b in s.get("bonus", []):
			if b.stat == stat:
				t += float(b.valor)
	return t


func tem_unica(id: String) -> bool:
	return skill_unica == id


func nivel_arma(tipo: String) -> int:
	return Progressao.nivel_arma(Dados.constantes, float(skills_arma.get(tipo, 0)))[0]


func nivel_vida(id: String) -> int:
	return Progressao.nivel_vida(Dados.constantes, float(skills_vida.get(id, 0)))[0]


## Multiplicador de dano com um tipo de arma: +2% por nível de Manejo e +10% (bónus da classe) se for preferida.
func mult_arma(tipo: String) -> float:
	var m := 1.0 + float(Dados.c("skill_arma_dano")) * nivel_arma(tipo) + passivo("dano")
	var linha := Progressao.linha_classes(classe)
	if not linha.is_empty() and tipo in linha[0].get("armas_preferidas", []):
		for b in linha[0].get("bonus", []):
			if b.stat == "atq":
				m += float(b.valor)
	return m


func _mult_treino() -> float:
	var m := 1.0
	if tem_unica("aprendiz_rapido"):
		m *= float(Dados.c("unica_aprendiz_skills"))
	if origem == "jogador":
		m *= float(Dados.c("origem_jogador_skills"))
	return m


## Cada golpe que acerta dá 1 ponto ao Manejo dessa arma. Nos níveis 3, 6 e 10 aprende-se um ataque especial.
func treinar_arma(tipo: String, pontos: float = 1.0) -> void:
	var antes := nivel_arma(tipo)
	skills_arma[tipo] = float(skills_arma.get(tipo, 0)) + pontos * _mult_treino()
	var depois := nivel_arma(tipo)
	if depois > antes:
		var nome_arma: String = tipo.replace("_", " ").capitalize()
		Sistema.mensagem("Manejo de %s subiu para o nível %d!" % [nome_arma, depois], "nivel")
		for s in Progressao.especiais_arma(tipo, depois):
			if int(s.nivel) > antes:
				Sistema.mensagem("Aprendeste uma skill nova: %s." % s.nome_pt, "nivel")
				por_na_barra(s.id)
		Eventos.stats_mudaram.emit()


func treinar_vida(id: String, acoes: float = 1.0) -> void:
	var antes := nivel_vida(id)
	skills_vida[id] = float(skills_vida.get(id, 0)) + acoes * _mult_treino()
	var depois := nivel_vida(id)
	if depois > antes:
		Sistema.mensagem("%s subiu para o nível %d!" % [Dados.obter("skills_vida", id).get("nome_pt", id), depois], "nivel")


func por_na_barra(id: String) -> void:
	if id in skills_barra:
		return
	var i := skills_barra.find("")
	if i >= 0:
		skills_barra[i] = id
		Eventos.stats_mudaram.emit()


## Todas as skills ativas que já podes usar (especiais de armas + classe).
func skills_ativas() -> Array:
	var r := []
	for tipo in skills_arma:
		r.append_array(Progressao.especiais_arma(tipo, nivel_arma(tipo)))
	for s in Progressao.skills_classe(classe, nivel):
		if s.tipo == "ativa":
			r.append(s)
	return r


func skill(id: String) -> Dictionary:
	var s := Dados.obter("skills_armas", id)
	if not s.is_empty():
		return s
	for c in Dados.tabela("classes").values():
		for k in c.skills:
			if k.id == id:
				return k
	return {}


func escolher_classe(id: String) -> bool:
	var d := Dados.obter("classes", id)
	if d.is_empty() or nivel < int(d.nivel_minimo) or (d.get("anterior") if d.get("anterior") else "") != classe:
		return false
	classe = id
	Sistema.mensagem("Classe: %s." % d.nome_pt, "nivel")
	for s in d.skills:
		if int(s.nivel) <= nivel and s.tipo == "ativa":
			por_na_barra(s.id)
	encher()
	return true


func rank() -> String:
	return Progressao.rank(Dados.constantes, pontos_guilda, andar_maximo)


func peso_maximo() -> float:
	if tem_unica("bolsa_infinita"):
		return INF
	return float(Dados.c("carga_base")) + a("for") * float(Dados.c("carga_por_for"))


func resistencia() -> float:
	return Formulas.resistencia(Dados.constantes, bonus.res, a("vit"), a("int"))


func encher() -> void:
	hp = hp_maximo()
	mp = mp_maximo()
	estamina = estamina_maxima()
	Eventos.stats_mudaram.emit()


# ---------------- ações ----------------

func gastar_estamina(valor: float) -> bool:
	if estamina < valor:
		return false
	estamina -= valor
	Eventos.stats_mudaram.emit()
	return true


func receber_dano(valor: int) -> void:
	hp = max(0.0, hp - valor)
	Eventos.jogador_dano.emit(valor)
	Eventos.stats_mudaram.emit()
	if hp <= 0.0:
		Eventos.jogador_morreu.emit()


func curar(valor: float) -> void:
	if estados and is_instance_valid(estados):
		valor *= estados.mult("cura_mult")   # Maldição: cura −50%
	hp = min(float(hp_maximo()), hp + valor)
	Eventos.stats_mudaram.emit()


## achado = ouro de monstros e baús (conta a SOR, +0,5% por ponto, e a Mão de Midas).
func ganhar_ouro(valor: int, achado: bool = false) -> void:
	if achado and valor > 0:
		if tem_unica("mao_de_midas"):
			valor = int(valor * float(Dados.c("unica_midas_ouro")))
		valor = int(valor * (1.0 + a("sor") * float(Dados.c("ouro_por_sor", 0.005))))
	ouro += valor
	Eventos.ouro_mudou.emit(ouro)


func ganhar_xp(valor: int) -> void:
	if nivel >= int(Dados.c("nivel_maximo", 100)):
		return
	if tem_unica("aprendiz_rapido"):
		valor = int(valor * float(Dados.c("unica_aprendiz_xp")))
	xp += valor
	Eventos.xp_ganha.emit(valor)
	while nivel < int(Dados.c("nivel_maximo", 100)) and xp >= xp_para_subir():
		xp -= xp_para_subir()
		nivel += 1
		pontos_livres += int(Dados.c("pontos_por_nivel", 5))
		encher()
		Sistema.mensagem("Subiste para o nível %d!" % nivel, "nivel")
		if nivel in Dados.c("classe_nivel", []):
			Sistema.mensagem("Podes escolher uma classe nova: fala com o Mestre Gorvan, na Guilda.", "nivel")
		for s in Progressao.skills_classe(classe, nivel):
			if int(s.nivel) == nivel:
				Sistema.mensagem("Skill de classe nova: %s." % s.nome_pt, "nivel")
				if s.tipo == "ativa":
					por_na_barra(s.id)
		Eventos.jogador_subiu_nivel.emit(nivel)
	Eventos.stats_mudaram.emit()


func xp_para_subir() -> int:
	return Formulas.xp_para_subir(Dados.constantes, nivel)


func gastar_ponto(nome_atributo: String) -> bool:
	if pontos_livres <= 0 or a(nome_atributo) >= int(Dados.c("atributo_maximo", 300)):
		return false
	atributos[nome_atributo] = a(nome_atributo) + 1
	pontos_livres -= 1
	Eventos.stats_mudaram.emit()
	return true


## Apanhar um item (do chão, de um baú, de uma recompensa).
func apanhar(id: String, qtd: int = 1, extra: Dictionary = {}) -> bool:
	var falta := inventario.adicionar(id, qtd, extra)
	var ficou := qtd - falta
	if ficou > 0:
		var d := Inventario._dados(id)
		if d.get("categoria", "") == "material":
			materiais_andar[id] = int(materiais_andar.get(id, 0)) + ficou
		var nome: String = d.get("nome_pt", id)
		var r: String = extra.get("raridade", "")
		Sistema.mensagem("Obtiveste: %s ×%d%s" % [nome, ficou, " (%s)" % r.capitalize() if r != "" and r != "comum" else ""])
		Eventos.item_apanhado.emit(id, ficou)
	if falta > 0:
		Sistema.mensagem("A mochila está cheia.", "aviso")
	return falta == 0


## Morrer (docs/SISTEMAS.md, secção 8): perdes 30% dos materiais apanhados neste andar desde a última Zona Segura.
func perder_materiais_do_andar(rng: RandomNumberGenerator) -> Array:
	var perdidos := []
	for id in materiais_andar:
		var n := int(round(int(materiais_andar[id]) * float(Dados.c("perda_materiais_morte", 0.3))))
		if n > 0:
			perdidos.append([id, inventario.retirar(id, n)])
	materiais_andar.clear()
	return perdidos


func usar_consumivel(id: String) -> bool:
	if not inventario.tem(id):
		return false
	var ef: Dictionary = Inventario._dados(id).get("efeito", {})
	if ef.is_empty():
		return false
	if ef.has("curar_hp_percent"):
		curar(hp_maximo() * float(ef.curar_hp_percent))
	if ef.has("curar_hp"):
		curar(float(ef.curar_hp))
	if ef.has("curar_mp_percent"):
		mp = min(float(mp_maximo()), mp + mp_maximo() * float(ef.curar_mp_percent))
	if ef.has("curar_estamina_percent"):
		estamina = min(float(estamina_maxima()), estamina + estamina_maxima() * float(ef.curar_estamina_percent))
	if ef.has("bonus"):
		buffs[String(ef.bonus.stat)] = [float(ef.bonus.valor), float(ef.bonus.minutos) * 60.0]
	if ef.has("regenerar"):
		buffs["regenerar"] = [float(ef.regenerar.percent), float(ef.regenerar.dura)]
	if estados and is_instance_valid(estados):
		if ef.has("tira_estados"):
			estados.tirar(ef.tira_estados)
		for est in ef.get("imune", []):
			estados.dar_imunidade(est, float(Dados.c("pocao_imune_s", 300)))
	inventario.retirar(id, 1)
	Eventos.stats_mudaram.emit()
	return true


## Equipar a arma que está no espaço i da mochila (a antiga vai para o lugar dela).
func equipar_do_espaco(i: int, segunda: bool = false) -> bool:
	var e = inventario.espacos[i]
	if e == null or Inventario._dados(e.id).get("categoria", "") != "arma":
		return false
	var antiga := arma_2 if segunda else arma_equipada
	inventario.espacos[i] = null
	if antiga != "":
		inventario.adicionar(antiga)
	if segunda:
		arma_2 = e.id
	else:
		arma_equipada = e.id
	inventario.mudou.emit()
	Eventos.equipamento_mudou.emit()
	return true


func tem_flag(f: String) -> bool:
	return f in flags


func por_flag(f: String) -> void:
	if not tem_flag(f):
		flags.append(f)


# ---------------- gravar ----------------

func para_gravar() -> Dictionary:
	return {
		"jogador": {"nome": nome, "nivel": nivel, "xp": xp, "atributos": atributos, "pontos_livres": pontos_livres,
					"hp": hp, "mp": mp, "tratamento": tratamento, "aparencia": aparencia, "origem": origem,
					"skill_unica": skill_unica, "classe": classe, "skills_arma": skills_arma, "skills_vida": skills_vida,
					"skills_barra": skills_barra, "pontos_guilda": pontos_guilda},
		"ouro": ouro, "equipamento": {"arma": arma_equipada, "arma_2": arma_2}, "inventario": inventario.para_gravar(), "azar_baus": azar_baus, "andares": {"desbloqueados": andar_maximo}, "flags": flags,
		"missoes": missoes, "amizade": amizade, "dificuldade": dificuldade, "tempo_jogado": tempo_jogado,
	}


func carregar(d: Dictionary) -> void:
	var j: Dictionary = d.get("jogador", {})
	nome = j.get("nome", "Jogador")
	nivel = int(j.get("nivel", 1))
	xp = int(j.get("xp", 0))
	atributos = j.get("atributos", atributos)
	pontos_livres = int(j.get("pontos_livres", 0))
	tratamento = j.get("tratamento", "ele")
	aparencia = j.get("aparencia", aparencia)
	origem = j.get("origem", "")
	skill_unica = j.get("skill_unica", "")
	classe = j.get("classe", "")
	skills_arma = j.get("skills_arma", {})
	skills_vida = j.get("skills_vida", {})
	skills_barra = j.get("skills_barra", ["", "", "", "", "", ""])
	pontos_guilda = int(j.get("pontos_guilda", 0))
	ouro = int(d.get("ouro", 0))
	arma_equipada = d.get("equipamento", {}).get("arma", "espada_cobre")
	arma_2 = d.get("equipamento", {}).get("arma_2", "")
	inventario.carregar(d.get("inventario", {}))
	azar_baus = int(d.get("azar_baus", 0))
	andar_maximo = int(d.get("andares", {}).get("desbloqueados", 1))
	flags.assign(d.get("flags", []))
	missoes = d.get("missoes", {})
	amizade = d.get("amizade", {})
	dificuldade = d.get("dificuldade", "normal")
	tempo_jogado = float(d.get("tempo_jogado", 0.0))
	encher()
	hp = min(float(j.get("hp", hp)), hp_maximo())
	mp = min(float(j.get("mp", mp)), mp_maximo())
