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
var dificuldade: String = "normal"
var aparencia: Dictionary = {"penteado": "espetado", "pele": "clara", "cabelo": "castanho_avermelhado", "olhos": "preto", "roupa": "aventureiro"}

var andar_maximo: int = 1
var flags: Array[String] = []
var amizade: Dictionary = {}
var missoes: Dictionary = {}
var tempo_jogado: float = 0.0

# bónus vindos do equipamento (o inventário preenche isto)
var bonus := {"hp": 0, "def": 0.0, "res": 0.0, "critico": 0.0}


func _ready() -> void:
	novo_jogo()


func _process(delta: float) -> void:
	tempo_jogado += delta


func novo_jogo(nome_jogador: String = "Jogador") -> void:
	nome = nome_jogador
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
	encher()


func a(nome_atributo: String) -> int:
	return int(atributos.get(nome_atributo, 0))


# ---------------- valores derivados ----------------

func hp_maximo() -> int:
	return Formulas.hp_maximo(Dados.constantes, a("vit"), nivel, bonus.hp)


func mp_maximo() -> int:
	return Formulas.mp_maximo(Dados.constantes, a("int"), nivel)


func estamina_maxima() -> int:
	return Formulas.estamina_maxima(Dados.constantes, a("agi"))


func velocidade() -> float:
	return Formulas.velocidade(Dados.constantes, a("agi"))


func critico(bonus_arma: float = 0.0) -> float:
	return Formulas.critico(Dados.constantes, a("des"), a("sor"), bonus_arma + bonus.critico)


func defesa() -> float:
	return Formulas.defesa(Dados.constantes, bonus["def"], a("vit"))


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
	hp = min(float(hp_maximo()), hp + valor)
	Eventos.stats_mudaram.emit()


func ganhar_ouro(valor: int) -> void:
	ouro += valor
	Eventos.ouro_mudou.emit(ouro)


func ganhar_xp(valor: int) -> void:
	if nivel >= int(Dados.c("nivel_maximo", 100)):
		return
	xp += valor
	Eventos.xp_ganha.emit(valor)
	while nivel < int(Dados.c("nivel_maximo", 100)) and xp >= xp_para_subir():
		xp -= xp_para_subir()
		nivel += 1
		pontos_livres += int(Dados.c("pontos_por_nivel", 5))
		encher()
		Sistema.mensagem("Subiste para o nível %d!" % nivel, "nivel")
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


func tem_flag(f: String) -> bool:
	return f in flags


func por_flag(f: String) -> void:
	if not tem_flag(f):
		flags.append(f)


# ---------------- gravar ----------------

func para_gravar() -> Dictionary:
	return {
		"jogador": {"nome": nome, "nivel": nivel, "xp": xp, "atributos": atributos, "pontos_livres": pontos_livres,
					"hp": hp, "mp": mp, "tratamento": tratamento, "aparencia": aparencia},
		"ouro": ouro, "equipamento": {"arma": arma_equipada}, "andares": {"desbloqueados": andar_maximo}, "flags": flags,
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
	ouro = int(d.get("ouro", 0))
	arma_equipada = d.get("equipamento", {}).get("arma", "espada_cobre")
	andar_maximo = int(d.get("andares", {}).get("desbloqueados", 1))
	flags.assign(d.get("flags", []))
	missoes = d.get("missoes", {})
	amizade = d.get("amizade", {})
	dificuldade = d.get("dificuldade", "normal")
	tempo_jogado = float(d.get("tempo_jogado", 0.0))
	encher()
	hp = min(float(j.get("hp", hp)), hp_maximo())
	mp = min(float(j.get("mp", mp)), mp_maximo())
