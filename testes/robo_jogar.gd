extends Node
## Robô que JOGA um andar sozinho, como um jogador normal, para encontrar erros e medir a dificuldade.
##
## Prepara o herói como o "jogador esperado" desse andar (testes/jogador_esperado.json, feito por
## ferramentas/equilibrio.py; regras em docs/SISTEMAS.md, secção 23), entra no andar e joga com uma IA simples:
## anda (com caminho pelas células do mapa) até ao monstro mais perto, ataca em combo, esquiva-se quando um monstro
## está no aviso (com a probabilidade "habilidade"), bebe uma poção abaixo de 35% de HP e, no fim, vai ao guardião /
## boss e luta com ele. Escreve um relatório JSON (mortes, monstros mortos, golpes, dano levado por tipo de monstro...).
##
## Uso (sem janela, o mais depressa possível; 1 frame = 1/60 s de jogo):
##   godot --headless --fixed-fps 60 --path . res://testes/robo_jogar.tscn -- <andar> [segundos] [saida.json] [modo] [habilidade]
##   modo: "andar" (monstros e depois o chefe, por defeito) · "boss" (vai logo ao guardião / boss) · "cidade" (Ascendia:
##   entra nos edifícios, abre as janelas, fala com as pessoas)
##   "pontes" (atravessa cada ponte "==" do andar de uma margem à outra)
##   habilidade: 0 a 1 (por defeito 0,5) — a hipótese de se esquivar a tempo de cada aviso
## Os erros do motor (SCRIPT ERROR...) não se apanham daqui: ferramentas/robo_jogar.py corre o robô e junta-os.

const CEL := 10.0

var andar_n := 1
var segundos := 120.0
var saida := "user://robo_jogar.json"
var modo := "andar"
var habilidade := 0.5

var andar: Node = null
var j: Jogador = null
var perfil: Dictionary = {}
var _t := 0.0
var _fim := false
var _rng := RandomNumberGenerator.new()

# entrada simulada
var _soltar: Dictionary = {}        # ação -> frame em que se larga
var _frame := 0
var _dir := Vector2.ZERO

# IA
var _alvo: Node3D = null
var _negros: Dictionary = {}        # instance_id -> até quando ignorar (inalcançável / preso)
var _caminho: Array[Vector3] = []
var _caminho_alvo := Vector3.INF
var _caminho_t := 0.0
var _ultima_pos := Vector3.ZERO
var _parado_t := 0.0
var _desvio_t := 0.0
var _desvio := Vector2.ZERO
var _alvo_desde := 0.0
var _alvo_hp := 0.0
var _avisos: Dictionary = {}        # instance_id -> {"esquivar": bool, "feito": bool}
var _ultimo_ataque := 0.0
var _fase := "monstros"             # monstros -> chefe -> escada -> fim
var _morto_desde := -1.0
var _hp_chefe_morte := -1.0

# relatório
var r := {
	"andar": 0, "modo": "", "habilidade": 0.0, "segundos": 0.0, "perfil": {},
	"heroi": {}, "mortes": 0, "mortes_causa": {}, "pocoes_usadas": 0, "pocoes_tentadas": 0, "xp": 0, "subidas_nivel": 0,
	"monstros": {}, "dano_estados": 0, "dano_outro": 0, "esquivas": 0, "avisos_vistos": 0,
	"preso": 0, "alvos_desistidos": 0, "chefe": {}, "escada": false, "erros_robo": [], "notas": [],
	"atacantes_presos": 0, "tempo_sem_ataques": 0.0, "mensagens_aviso": {}, "itens_sem_dados": [], "preso_onde": {}, "trilho": [],
}
var _inst: Dictionary = {}           # instance_id -> {id, tipo, t0, golpes, hp_ant, nivel}
var _hp_ant := 0.0
var _dano_frame := 0
var _pocoes_ant := 0
var _sem_ataques_t := 0.0


func _ready() -> void:
	process_mode = Node.PROCESS_MODE_ALWAYS
	var args := OS.get_cmdline_user_args()
	if args.size() > 0:
		andar_n = int(args[0])
	if args.size() > 1:
		segundos = float(args[1])
	if args.size() > 2:
		saida = args[2]
	if args.size() > 3:
		modo = args[3]
	if args.size() > 4:
		habilidade = float(args[4])
	_rng.seed = 1234 + andar_n
	Opcoes.valores["gravacao_automatica"] = false   # o robô não mexe nas gravações
	if OS.get_environment("SEM2D") != "":
		Opcoes.valores["vista_2d"] = false
	Tempo.hora = 10.0
	Jogo.novo_jogo("Robo")
	Jogo.origem = "atrasado"
	r.andar = andar_n
	r.modo = modo
	r.habilidade = habilidade
	if modo == "cidade":
		_preparar(maxi(andar_n, 1))
		add_child(load("res://cenas/mundo/cidade.tscn").instantiate())
		_cidade.call_deferred()
		return
	_preparar(andar_n)
	Jogo.andar_atual = andar_n
	Jogo.andar_maximo = andar_n
	if modo == "pontes":
		andar = load("res://cenas/mundo/andar.tscn").instantiate()
		add_child(andar)
		j = andar.jogador
		_pontes.call_deferred()
		return
	Eventos.jogador_dano.connect(func(v): _dano_frame += v; _atribuir_dano(v))
	Eventos.xp_ganha.connect(func(v): r.xp += v)
	Eventos.item_apanhado.connect(func(id, _q):
		if String(Inventario._dados(id).get("nome_pt", "")) == "" and not id in r.itens_sem_dados:
			r.itens_sem_dados.append(id))
	Eventos.jogador_subiu_nivel.connect(func(_n): r.subidas_nivel += 1)
	Eventos.mensagem_sistema.connect(func(t, tipo):
		if tipo == "aviso":
			r.mensagens_aviso[t] = int(r.mensagens_aviso.get(t, 0)) + 1)
	andar = load("res://cenas/mundo/andar.tscn").instantiate()
	add_child(andar)
	j = andar.jogador
	if j == null:
		_erro("o andar não criou o jogador")
		_acabar()
		return
	_hp_ant = Jogo.hp
	_pocoes_ant = Jogo.inventario.contar(perfil.get("pocao", "pocao_vida_p"))
	if modo == "boss":
		_fase = "chefe"
	r.heroi = {"nivel": Jogo.nivel, "hp": Jogo.hp_maximo(), "def": snappedf(Jogo.defesa(), 0.1), "atq_arma": j.arma.get("atq", 0),
			"arma": Jogo.arma_equipada, "atributos": Jogo.atributos.duplicate(), "classe": Jogo.classe}


## Põe o herói como o jogador esperado deste andar (testes/jogador_esperado.json).
func _preparar(n: int) -> void:
	var todos = JSON.parse_string(FileAccess.get_file_as_string("res://testes/jogador_esperado.json"))
	if not todos is Dictionary or not todos.has(str(n)):
		_erro("falta testes/jogador_esperado.json (corre python3 ferramentas/equilibrio.py)")
		return
	perfil = todos[str(n)]
	r.perfil = perfil
	Jogo.nivel = int(perfil.nivel)
	for a in perfil.atributos:
		Jogo.atributos[a] = int(perfil.atributos[a])
	Jogo.arma_equipada = perfil.arma
	Jogo.arma_extra = {"id": perfil.arma, "qtd": 1, "melhoria": int(perfil.melhoria)}
	for id in perfil.armadura:
		var d := Inventario._dados(id)
		Jogo.equipamento[d.get("espaco", "corpo")] = {"id": id, "qtd": 1, "melhoria": int(perfil.armadura_melhoria)}
	Jogo._recalcular_armadura()
	Jogo.skills_arma["espada"] = float(perfil.manejo_espada)
	for cl in ["espadachim", "mestre_de_laminas", "santo_da_espada"]:
		if Jogo.classe != perfil.classe and perfil.classe != "":
			Jogo.escolher_classe(cl)
	Jogo.inventario = Inventario.new(int(Dados.c("mochila", 30)))
	Jogo.inventario.adicionar(perfil.pocao, int(perfil.pocoes))
	Jogo.inventario.barra_rapida[0] = perfil.pocao
	Jogo.ouro = 2000
	Jogo.encher()


# ------------------------------------------------------------------ ciclo ------------------------------------------------------------------

func _physics_process(delta: float) -> void:
	if _fim or modo in ["cidade", "pontes"] or j == null:
		return
	_frame += 1
	for a in _soltar.keys():
		if _frame >= _soltar[a]:
			Input.action_release(a)
			_soltar.erase(a)
	if get_tree().paused:   # uma janela abriu (ex.: diálogo): fecha-a
		for w in get_tree().get_nodes_in_group("janelas"):
			if w.visible and w.has_method("abrir"):
				w.abrir(false)
		get_tree().paused = false
	_t += delta
	_medir()
	if _frame % 120 == 0 and andar.has_method("celula_de"):   # por onde andou (de 2 em 2 s), para ver onde fica preso
		var c: Vector2i = andar.celula_de(j.global_position)
		r.trilho.append([int(_t), c.x, c.y, j.estado, _alvo.id if is_instance_valid(_alvo) else ""])
	if _t >= segundos:
		_acabar()
		return
	if not is_instance_valid(j):
		_erro("o jogador desapareceu")
		_acabar()
		return
	if j.estado == "morto":
		_morte()
		return
	_morto_desde = -1.0
	_dir = Vector2.ZERO
	if _esquivar():
		_aplicar_dir()
		return
	if Jogo.hp < Jogo.hp_maximo() * 0.35 and j.estado == "normal" and j._pocao_recarga <= 0.0 and Jogo.inventario.tem(perfil.get("pocao", "pocao_vida_p")) \
			and not _perigo_perto():
		_carregar("pocao")
		r.pocoes_tentadas += 1
		_aplicar_dir()
		return
	_escolher_alvo()
	if _alvo:
		_ir_e_lutar()
	elif _fase == "escada":
		_ir_escada()
	_aplicar_dir()


## Carrega numa tecla durante 2 frames (para o "just_pressed" do herói).
func _carregar(acao: String) -> void:
	Input.action_press(acao)
	_soltar[acao] = _frame + 2


func _aplicar_dir() -> void:
	var d := _dir
	if _desvio_t > 0.0 and d != Vector2.ZERO:
		d = _desvio
	for par in [["mover_direita", d.x], ["mover_esquerda", -d.x], ["mover_baixo", d.y], ["mover_cima", -d.y]]:
		if par[1] > 0.05:
			Input.action_press(par[0], clampf(par[1], 0.0, 1.0))
		else:
			Input.action_release(par[0])


func _plano(a: Vector3, b: Vector3) -> float:
	return Vector2(a.x - b.x, a.z - b.z).length()


func _vivos() -> Array:
	var l := []
	for m in get_tree().get_nodes_in_group("monstros"):
		if is_instance_valid(m) and m.estado != "morto" and m.is_inside_tree():
			l.append(m)
	return l


func _e_chefe(m: Node) -> bool:
	return m.tipo in ["guardiao", "mini_boss", "boss"]


# ------------------------------------------------------------------ esquivar e poções ------------------------------------------------------------------

## Alcance do ataque que o monstro está a preparar (para saber se é perigo).
func _alcance_aviso(m: Node) -> float:
	var at: Dictionary = m._ataque
	match at.get("forma", "golpe"):
		"area":
			return float(Dados.c("boss_area_raio", 4.5)) + 0.5
		"carga":
			return float(Dados.c("boss_carga_distancia", 9.0)) + 1.0
		"projeteis":
			return 16.0
	return float(at.get("alcance", 1.5)) + 0.3 + float(m._tamanho_px) / 32.0


func _perigo_perto() -> bool:
	for m in _vivos():
		if m.estado == "aviso" and _plano(m.global_position, j.global_position) < _alcance_aviso(m) + 1.0:
			return true
	return false


func _esquivar() -> bool:
	for m in _vivos():
		var id: int = m.get_instance_id()
		if m.estado != "aviso":
			_avisos.erase(id)
			continue
		var dist := _plano(m.global_position, j.global_position)
		if dist > _alcance_aviso(m) + 0.5:
			continue
		if not _avisos.has(id):
			_avisos[id] = {"esquivar": _rng.randf() < habilidade, "feito": false}
			r.avisos_vistos += 1
		var av: Dictionary = _avisos[id]
		var falta := float(m._ataque.get("aviso", 0.4)) - float(m._t)
		if av.esquivar and not av.feito and falta <= 0.18 and j.estado in ["normal", "ataque"] and Jogo.estamina >= float(Dados.c("esquiva_custo")):
			av.feito = true
			var fora := Vector2(j.global_position.x - m.global_position.x, j.global_position.z - m.global_position.z).normalized()
			if fora == Vector2.ZERO:
				fora = Vector2(1, 0)
			if m._ataque.get("forma", "") == "carga" or float(m._ataque.get("alcance", 1.5)) > 3.0:
				fora = fora.rotated(PI / 2.0)   # ataques em linha: para o lado
			_dir = fora
			_carregar("esquivar")
			r.esquivas += 1
			return true
	return false


# ------------------------------------------------------------------ alvos e caminho ------------------------------------------------------------------

func _escolher_alvo() -> void:
	if not is_instance_valid(_alvo) or _alvo.estado == "morto":
		_alvo = null
	if _fase == "monstros" and _t > segundos * 0.55 and andar.guardiao and is_instance_valid(andar.guardiao):
		_fase = "chefe"
	if _fase == "chefe" and (andar.guardiao == null or not is_instance_valid(andar.guardiao) or andar.guardiao.estado == "morto"):
		_fase = "escada" if andar.escada else "monstros"
	var vivos := _vivos()
	# quem já me está a atacar tem prioridade (não se fica a apanhar pelas costas)
	var melhor: Node3D = null
	var dist := INF
	for m in vivos:
		if _e_chefe(m) and _fase != "chefe":
			continue
		if _negros.get(m.get_instance_id(), -1.0) > _t:
			continue
		var d := _plano(m.global_position, j.global_position)
		if m.estado in ["perseguir", "aviso", "atacar", "dano"] and d < 8.0:
			d *= 0.3
		if d < dist:
			dist = d
			melhor = m
	if _fase == "chefe" and andar.guardiao and is_instance_valid(andar.guardiao) and andar.guardiao.estado != "morto":
		var g: Node3D = andar.guardiao
		if melhor == null or _plano(melhor.global_position, j.global_position) > 6.0 or melhor == g:
			melhor = g
	if melhor != _alvo:
		_alvo = melhor
		_alvo_desde = _t
		_alvo_hp = melhor.hp if melhor else 0.0
		_caminho.clear()


func _ir_e_lutar() -> void:
	var p := _alvo.global_position
	var dist := _plano(p, j.global_position)
	# o golpe chega a alcance + 0,4 m; a "hurtbox" do monstro tem o raio do corpo (monstro.gd: tamanho/16 × 0,22, +0,1)
	var raio := clampf(float(_alvo._tamanho_px) / 16.0 * 0.22, 0.3, 2.5) + 0.1
	var alcance := float(j.arma.get("alcance", 1.8)) + raio
	# preso a um alvo muito tempo sem lhe tirar vida: desiste dele uns tempos
	if _alvo.hp < _alvo_hp - 0.5:
		_alvo_hp = _alvo.hp
		_alvo_desde = _t
	elif _t - _alvo_desde > (40.0 if _e_chefe(_alvo) else 14.0):
		_negros[_alvo.get_instance_id()] = _t + 30.0
		r.alvos_desistidos += 1
		r.notas.append("%.0fs: desisti de %s (%.0f m, estado %s)" % [_t, _alvo.id, dist, _alvo.estado])
		_alvo = null
		return
	var dir := Vector2(p.x - j.global_position.x, p.z - j.global_position.z).normalized()
	if dist <= alcance:
		_dir = dir   # a direção também serve de mira
		if _t - _ultimo_ataque > 0.12:
			_ultimo_ataque = _t
			_carregar("atacar")
		return
	_andar_para(p)


func _ir_escada() -> void:
	if andar.escada == null:
		_fase = "fim"
		return
	var p: Vector3 = andar.escada.global_position
	if _plano(p, j.global_position) < 5.0:
		r.escada = true
		r.notas.append("%.0fs: cheguei à escada (aberta: %s)" % [_t, andar.escada_livre])
		_acabar()
		return
	_andar_para(p)


## Anda para o ponto p: pelas células do mapa (procura em largura), e direito quando está perto.
func _andar_para(p: Vector3) -> void:
	var aqui := j.global_position
	_desvio_t -= get_physics_process_delta_time()
	if _plano(aqui, _ultima_pos) < 0.02 and j.estado == "normal":
		_parado_t += get_physics_process_delta_time()
	else:
		_parado_t = maxf(0.0, _parado_t - get_physics_process_delta_time() * 0.5)
	_ultima_pos = aqui
	if _parado_t > 0.8:   # preso contra alguma coisa: desvia para um lado
		_parado_t = 0.0
		_desvio = Vector2(p.x - aqui.x, p.z - aqui.z).normalized().rotated((PI / 2.0) * (1 if _rng.randf() < 0.5 else -1))
		_desvio_t = 0.7
		r.preso += 1
		var c: Vector2i = andar.celula_de(aqui)
		var chave := "%d,%d %s" % [c.x, c.y, andar.codigo(c.x, c.y)]
		r.preso_onde[chave] = int(r.preso_onde.get(chave, 0)) + 1
		_caminho.clear()
	var alvo := p
	if _plano(aqui, p) > 12.0 and andar.has_method("codigo"):
		if _caminho.is_empty() or _caminho_alvo.distance_to(p) > CEL or _t - _caminho_t > 4.0:
			_caminho = _procurar_caminho(aqui, p)
			_caminho_alvo = p
			_caminho_t = _t
			if _caminho.is_empty() and _alvo:
				_negros[_alvo.get_instance_id()] = _t + 30.0
				r.alvos_desistidos += 1
				r.notas.append("%.0fs: sem caminho para %s" % [_t, _alvo.id])
				_alvo = null
				return
		while _caminho.size() > 1 and _plano(aqui, _caminho[0]) < 3.0:
			_caminho.pop_front()
		if not _caminho.is_empty():
			alvo = _caminho[0]
	_dir = Vector2(alvo.x - aqui.x, alvo.z - aqui.z).normalized()


const PAREDES := ["TT", "##", "~~", "ww", "  "]   # o que não se atravessa a pé (andar.gd: _parede, rocha, água funda, vazio)


func _passa(cx: int, cy: int) -> bool:
	return not andar.codigo(cx, cy) in PAREDES


func _procurar_caminho(de: Vector3, para: Vector3) -> Array[Vector3]:
	var a: Vector2i = andar.celula_de(de)
	var b: Vector2i = andar.celula_de(para)
	var res: Array[Vector3] = []
	if a == b:
		res.append(para)
		return res
	var veio := {a: a}
	var fila: Array[Vector2i] = [a]
	var viz := [Vector2i(1, 0), Vector2i(-1, 0), Vector2i(0, 1), Vector2i(0, -1), Vector2i(1, 1), Vector2i(1, -1), Vector2i(-1, 1), Vector2i(-1, -1)]
	while not fila.is_empty():
		var c: Vector2i = fila.pop_front()
		if c == b:
			break
		for v in viz:
			var n: Vector2i = c + v
			if veio.has(n) or not (_passa(n.x, n.y) or n == b):
				continue
			if v.x != 0 and v.y != 0 and not (_passa(c.x + v.x, c.y) and _passa(c.x, c.y + v.y)):
				continue
			veio[n] = c
			fila.append(n)
	if not veio.has(b):
		return res
	var c := b
	while c != a:
		res.push_front(andar.centro_celula(c.x, c.y))
		c = veio[c]
	res[res.size() - 1] = para
	return res


# ------------------------------------------------------------------ medir ------------------------------------------------------------------

func _tipo_stats(id: String, tipo: String) -> Dictionary:
	if not r.monstros.has(id):
		r.monstros[id] = {"tipo": tipo, "mortos": 0, "golpes_dados": 0, "dano_dado": 0, "segundos_matar": 0.0, "golpes_levados": 0,
				"dano_levado": 0, "ataques_comecados": 0, "visto": 0}
	return r.monstros[id]


func _medir() -> void:
	# poções bebidas (conta o que desapareceu da mochila)
	var pocoes := Jogo.inventario.contar(perfil.get("pocao", "pocao_vida_p"))
	if pocoes < _pocoes_ant:
		r.pocoes_usadas += _pocoes_ant - pocoes
	_pocoes_ant = pocoes
	var hp := Jogo.hp
	var perda := _hp_ant - hp - _dano_frame
	if perda > 0.5 and j and j.estado != "morto":
		r.dano_estados += int(round(perda))
	_hp_ant = hp
	_dano_frame = 0
	var algum_ataca := false
	var a_perseguir := 0
	for m in get_tree().get_nodes_in_group("monstros"):
		if not is_instance_valid(m):
			continue
		var id: int = m.get_instance_id()
		if not _inst.has(id):
			_inst[id] = {"id": m.id, "tipo": m.tipo, "t0": -1.0, "golpes": 0, "hp_ant": m.hp, "nivel": m.nivel, "estado": m.estado}
			_tipo_stats(m.id, m.tipo).visto += 1
			m.morreu.connect(_morreu.bind(id))
		var s: Dictionary = _inst[id]
		if m.hp < s.hp_ant - 0.5:
			if s.t0 < 0.0:
				s.t0 = _t
			s.golpes += 1
			var ts := _tipo_stats(m.id, m.tipo)
			if _e_chefe(m) and r.chefe.get("quedas", []).size() < 40:   # as primeiras perdas de HP do chefe (para ver os golpes)
				r.chefe["quedas"] = r.chefe.get("quedas", []) + [[snappedf(_t, 0.01), int(s.hp_ant - m.hp), m.estado]]
			ts.golpes_dados += 1
			ts.dano_dado += int(s.hp_ant - m.hp)
		s.hp_ant = m.hp
		if m.estado == "aviso" and s.estado != "aviso":
			_tipo_stats(m.id, m.tipo).ataques_comecados += 1
		s.estado = m.estado
		if m.estado in ["aviso", "atacar", "carga"]:
			algum_ataca = true
		if m.estado == "perseguir" and _plano(m.global_position, j.global_position) < 2.5:
			a_perseguir += 1
	# monstros colados ao herói há muito tempo sem nenhum atacar = o contador de atacantes ficou preso
	if a_perseguir > 0 and not algum_ataca:
		_sem_ataques_t += get_physics_process_delta_time()
		if _sem_ataques_t > 6.0:
			r.atacantes_presos += 1
			r.notas.append("%.0fs: %d monstros colados sem atacar há 6 s (Monstro._atacantes = %d)" % [_t, a_perseguir, Monstro._atacantes])
			_sem_ataques_t = -60.0
	elif algum_ataca:
		_sem_ataques_t = 0.0
	r.tempo_sem_ataques = maxf(r.tempo_sem_ataques, _sem_ataques_t)
	if andar and andar.guardiao and is_instance_valid(andar.guardiao):
		var g: Node = andar.guardiao
		if r.chefe.is_empty():
			r.chefe = {"id": g.id, "tipo": g.tipo, "nivel": g.nivel, "hp_max": int(g.hp_max), "inicio": -1.0, "fim": -1.0, "mortes_heroi": 0}
		if r.chefe.inicio < 0.0 and (g.hp < g.hp_max or g.get("ativo") == true):
			r.chefe.inicio = _t
		r.chefe.hp_final = int(g.hp)
		if "fase" in g:
			r.chefe.fase = g.fase + 1


func _morreu(_m: Node, id: int) -> void:
	var s: Dictionary = _inst.get(id, {})
	if s.is_empty():
		return
	var ts := _tipo_stats(s.id, s.tipo)
	ts.mortos += 1
	if s.t0 >= 0.0:
		ts.segundos_matar += _t - s.t0
	if andar and _m == andar.guardiao:
		r.chefe.fim = _t
		r.chefe.hp_final = 0


## Quem me bateu? O monstro mais perto que está a golpear (ou o mais perto de todos).
func _atribuir_dano(v: int) -> void:
	if j == null or not is_instance_valid(j):
		return
	var melhor: Node = null
	var dist := INF
	for m in _vivos():
		var d := _plano(m.global_position, j.global_position)
		if m.estado in ["atacar", "carga"]:
			d -= 100.0
		if d < dist:
			dist = d
			melhor = m
	if melhor == null or dist > 30.0:
		r.dano_outro += v
		return
	var ts := _tipo_stats(melhor.id, melhor.tipo)
	ts.golpes_levados += 1
	ts.dano_levado += v
	if Jogo.hp <= 0.0:
		r.mortes_causa[melhor.id] = int(r.mortes_causa.get(melhor.id, 0)) + 1


## Morreu: conta, espera 2 s e levanta-se (no sítio de chegada; na luta com o chefe, dentro da arena)
## com o HP cheio e as poções repostas — como quem volta da Estalagem.
func _morte() -> void:
	if _morto_desde < 0.0:
		_morto_desde = _t
		r.mortes += 1
		if r.chefe.get("inicio", -1.0) >= 0.0 and _fase == "chefe":
			r.chefe.mortes_heroi += 1
		_hp_chefe_morte = andar.guardiao.hp if andar.guardiao and is_instance_valid(andar.guardiao) else -1.0
		if modo == "boss" and r.chefe.get("inicio", -1.0) >= 0.0:
			# no modo boss conta só uma vida (com as poções): quanto HP do chefe se tirou e quanto tempo se aguentou
			r.chefe.hp_final = int(_hp_chefe_morte)
			r.chefe.vivo_s = snappedf(_t - r.chefe.inicio, 0.1)
			_acabar()
		for a in ["mover_direita", "mover_esquerda", "mover_baixo", "mover_cima"]:
			Input.action_release(a)
		return
	if _t - _morto_desde < 2.0:
		return
	var ui = get_tree().get_first_node_in_group("morte_ui")
	if ui:
		ui.visible = false
	Jogo.encher()
	Jogo.inventario.adicionar(perfil.get("pocao", "pocao_vida_p"), maxi(0, int(perfil.get("pocoes", 5)) - Jogo.inventario.contar(perfil.get("pocao", "pocao_vida_p"))))
	var g = andar.guardiao
	if _fase == "chefe" and g and is_instance_valid(g) and "arena_centro" in g and g.ativo:
		j.global_position = g.arena_centro + Vector3(0, 0.5, 5.0)
	# no jogo, morrer leva-te à Estalagem e o chefe volta a ter o HP todo; aqui a luta continua de onde ficou,
	# para se ver quantas "vidas" (mortes + 1) custa vencê-lo
	if g and is_instance_valid(g) and _hp_chefe_morte > 0.0 and g.hp > _hp_chefe_morte:
		g.hp = _hp_chefe_morte
	else:
		j.global_position = andar.ponto_chegada + Vector3(0, 0.5, 0)
	_pocoes_ant = Jogo.inventario.contar(perfil.get("pocao", "pocao_vida_p"))
	j.velocity = Vector3.ZERO
	j.invencivel = 2.0
	j.mudar_estado("normal")
	_morto_desde = -1.0
	_caminho.clear()


func _erro(t: String) -> void:
	r.erros_robo.append(t)
	push_warning("ROBO: " + t)


func _acabar() -> void:
	if _fim:
		return
	_fim = true
	r.segundos = snappedf(_t, 0.1)
	r.nivel_final = Jogo.nivel
	for id in r.monstros:
		var ts: Dictionary = r.monstros[id]
		ts.segundos_matar_media = snappedf(ts.segundos_matar / maxf(1.0, ts.mortos), 0.1)
		ts.golpes_por_morte = snappedf(float(ts.golpes_dados) / maxf(1.0, ts.mortos), 0.1)
		ts.dano_por_golpe_levado = snappedf(float(ts.dano_levado) / maxf(1.0, ts.golpes_levados), 0.1)
	r.hp_max = Jogo.hp_maximo()
	r.atacantes_no_fim = Monstro._atacantes
	var f := FileAccess.open(saida, FileAccess.WRITE)
	if f:
		f.store_string(JSON.stringify(r, " "))
		f.close()
	print("ROBO: fim do andar ", andar_n, " — ", r.mortes, " mortes, ", r.monstros.values().reduce(func(s, x): return s + x.mortos, 0),
			" monstros mortos, relatório em ", saida)
	for a in ["mover_direita", "mover_esquerda", "mover_baixo", "mover_cima", "atacar", "esquivar", "pocao"]:
		Input.action_release(a)
	get_tree().quit()


# ------------------------------------------------------------------ cidade ------------------------------------------------------------------

func _esperar(s: float) -> void:
	var t0 := Time.get_ticks_msec()
	var frames := int(s * 60.0)
	for k in frames:
		await get_tree().physics_frame
	if Time.get_ticks_msec() - t0 < 0:
		pass


func _evento_acao(acao: String) -> void:
	var e := InputEventAction.new()
	e.action = acao
	e.pressed = true
	Input.parse_input_event(e)
	var e2 := InputEventAction.new()
	e2.action = acao
	e2.pressed = false
	Input.parse_input_event(e2)


## Ascendia: entra e sai de todos os edifícios, abre as janelas com as teclas, abre as lojas e as estações,
## fala com as pessoas e passeia um pouco.
func _cidade() -> void:
	await _esperar(2.0)
	var cid: Node = get_child(0)
	j = get_tree().get_first_node_in_group("jogador") as Jogador
	if j == null:
		_erro("a cidade não criou o jogador")
		_acabar()
		return
	# 1. os edifícios
	var portas := []
	for i in get_tree().get_nodes_in_group("interagivel"):
		if String(i.texto).begins_with("Entrar"):
			portas.append(i)
	r.notas.append("%d portas" % portas.size())
	for p in portas:
		p.usado.emit(j)
		await _esperar(0.6)
		if Interior.atual == null or not is_instance_valid(Interior.atual):
			_erro("não entrou: " + p.texto)
			continue
		# falar com quem lá está e usar o que houver (estações, balcões)
		for it in get_tree().get_nodes_in_group("interagivel"):
			if it is Interagivel and it.global_position.y < -300.0 and it.ativo and not String(it.texto).begins_with("Sair"):
				it.interagir(j)
				await _esperar(0.3)
				await _fechar_tudo()
		await _fechar_tudo()
		if Interior.atual and is_instance_valid(Interior.atual):
			Interior.atual.sair()
		await _esperar(0.3)
	# 2. as janelas, pelas teclas
	for acao in ["inventario", "status", "diario", "mapa", "pausa"]:
		var dlg = get_tree().get_first_node_in_group("dialogo_ui")
		if dlg and dlg.visible:
			_erro("antes de %s: a caixa de diálogo ficou aberta depois das conversas" % acao)
		_evento_acao(acao)
		await _esperar(0.4)
		var aberta := false
		for w in get_tree().get_nodes_in_group("janelas"):
			if w.visible and (w.acao == acao or (acao == "status" and w.acao == "status")):
				aberta = true
		if not aberta:
			var outras := []
			for w in get_tree().get_nodes_in_group("janelas"):
				if w.visible:
					outras.append("%s(%s)" % [w.name, w.get_script().resource_path.get_file()])
			_erro("a tecla %s não abriu a sua janela (abertas: %s)" % [acao, outras])
		_evento_acao("pausa" if acao != "pausa" else "pausa")
		await _esperar(0.3)
		await _fechar_tudo()
		if get_tree().paused:
			_erro("o jogo ficou em pausa depois de fechar %s" % acao)
			get_tree().paused = false
	# 3. as lojas e as estações
	var loja = get_tree().get_first_node_in_group("loja_ui")
	if loja:
		for dono in Dados.tabela("lojas").keys():
			loja.abrir_loja(String(dono).trim_prefix("loja_"))
			await _esperar(0.2)
		await _fechar_tudo()
	var craft = get_tree().get_first_node_in_group("crafting_ui")
	if craft:
		for e in ["forja", "alquimia", "fogao", "tear", "bancada", "joalharia"]:
			craft.abrir_estacao(e)
			await _esperar(0.2)
		await _fechar_tudo()
	# 4. falar com as pessoas
	var n := 0
	for npc in get_tree().get_nodes_in_group("npcs"):
		if n >= 12:
			break
		if npc.has_method("conversar_menu") and npc.is_inside_tree():
			j.global_position = npc.global_position + Vector3(1.0, 0.3, 0.0)
			npc.conversar_menu(j)
			await _esperar(0.5)
			await _fechar_tudo()
			n += 1
	r.notas.append("falei com %d pessoas" % n)
	# 5. passear
	for k in 20:
		var d := Vector2.from_angle(_rng.randf() * TAU)
		_dir = d
		_aplicar_dir()
		await _esperar(1.0)
	_dir = Vector2.ZERO
	_aplicar_dir()
	_acabar()


## Fecha diálogos e janelas abertas (carrega em "avançar" nos diálogos).
func _fechar_tudo() -> void:
	for k in 30:
		var algo := false
		var dlg = get_tree().get_first_node_in_group("dialogo_ui")
		if dlg and dlg.visible:
			algo = true
			if dlg.has_signal("_escolheu"):
				dlg._escolheu.emit(0)
			dlg._avancar.emit()
		for w in get_tree().get_nodes_in_group("janelas"):
			if w.visible and w.has_method("abrir"):
				w.abrir(false)
				algo = true
		if not algo:
			break
		await _esperar(0.15)
	get_tree().paused = false


# ------------------------------------------------------------------ pontes ------------------------------------------------------------------

## Cada ponte (células "==" seguidas): põe o herói na margem de um lado, anda a direito e vê se chega à outra margem.
func _pontes() -> void:
	await _esperar(0.5)
	for m in get_tree().get_nodes_in_group("monstros"):
		m.queue_free()
	var feitas := {}
	r.pontes = []
	for cy in andar.altura_cel:
		for cx in andar.largura:
			if andar.codigo(cx, cy) != "==" or feitas.has(Vector2i(cx, cy)):
				continue
			var d := Vector2i(1, 0) if andar._ponte_horizontal(cx, cy) else Vector2i(0, 1)
			var a := Vector2i(cx, cy)
			while andar.codigo(a.x - d.x, a.y - d.y) == "==":
				a -= d
			var b := a
			while andar.codigo(b.x + d.x, b.y + d.y) == "==":
				feitas[b] = true
				b += d
			feitas[b] = true
			for sentido in [1, -1]:
				var de: Vector2i = (a - d) if sentido == 1 else (b + d)
				var para: Vector2i = (b + d) if sentido == 1 else (a - d)
				if not andar.codigo(de.x, de.y) in Andar.PASSA or not andar.codigo(para.x, para.y) in Andar.PASSA:
					continue
				var p0: Vector3 = andar.centro_celula(de.x, de.y)
				p0.y = andar.altura_em(p0.x, p0.z) + 0.6
				j.global_position = p0
				j.velocity = Vector3.ZERO
				j.mudar_estado("normal")
				var alvo: Vector3 = andar.centro_celula(para.x, para.y)
				var ok := false
				for k in 60 * (4 + 3 * (b - a).length()):
					get_tree().paused = false
					_dir = Vector2(alvo.x - j.global_position.x, alvo.z - j.global_position.z).normalized()
					_aplicar_dir()
					await get_tree().physics_frame
					if andar.celula_de(j.global_position) == para:
						ok = true
						break
				_dir = Vector2.ZERO
				_aplicar_dir()
				var onde: Vector2i = andar.celula_de(j.global_position)
				r.pontes.append({"de": [de.x, de.y], "para": [para.x, para.y], "ok": ok, "ficou": [onde.x, onde.y, andar.codigo(onde.x, onde.y)]})
				if not ok:
					_erro("ponte de %s para %s: ficou preso em %s (%s)" % [de, para, onde, andar.codigo(onde.x, onde.y)])
	print("ROBO: pontes do andar ", andar_n, ": ", r.pontes.filter(func(x): return x.ok).size(), "/", r.pontes.size(), " atravessadas")
	_acabar()
