extends Node
## "Robô" de teste: carrega uma cena, joga sozinho (anda, corre, esquiva, ataca) e grava capturas de ecrã.
## Uso: xvfb-run godot --rendering-driver opengl3 --path . res://testes/robo_captura.tscn -- <cena> <pasta>

var _corrida := ""
var cena := "res://cenas/teste/teste_chao.tscn"
var pasta := "user://capturas"
var _t := 0.0
var _n := 0
var _passos := [
	[0.0, ""], [1.0, "captura"], [1.2, "mover_direita"], [2.0, "captura"], [2.1, "-mover_direita"],
	[2.2, "atacar"], [2.32, "captura"], [2.6, "atacar"], [2.72, "captura"], [3.1, "mover_cima"], [3.6, "esquivar"],
	[3.65, "captura"], [4.0, "-mover_cima"], [4.2, "mover_esquerda"], [5.5, "captura"], [5.6, "-mover_esquerda"], [5.7, "vista"], [7.5, "captura"], [7.6, "fim"],
]
var _i := 0
var _clima := ""
var _local := ""
# Para as imagens da página do jogo (docs/PUBLICACAO.md, secção 3), com variáveis de ambiente:
#   ROBO_TAM=1920x1080  janela maior (o jogo amplia 1,5× em vez de ficar a 1280×720)
#   ROBO_ZOOM=2.6667    zoom fixo da câmara 2D (com ROBO_TAM=1920x1080: 2 dá píxeis de 3 e 2.6667 píxeis de 4)
#   ROBO_SEM_HUD=1      esconde o HUD, o minimapa e as mensagens (para GIFs pequenos)
var _zoom := 0.0
var _gravar := 0          # capturas seguidas (uma por frame) que ainda faltam
var _reflexo := false     # esquiva os golpes do boss no último momento e responde com golpes
var _reflexo_fase := 0
var _reflexo_t := 0.0
var _reflexo_acoes: Array = []
var _desvio := Vector3.ZERO


func _ready() -> void:
	var args := OS.get_cmdline_user_args()
	if args.size() > 0:
		cena = args[0]
	if args.size() > 1:
		pasta = args[1]
	if args.size() > 2:
		Jogo.andar_atual = int(args[2])
	if args.size() > 3 and args[3] == "inventario":   # abre a mochila com alguns itens
		_passos = [[1.5, "captura"], [1.6, "inventario"], [2.2, "captura"], [2.3, "fim"]]
	elif args.size() > 3 and args[3].begins_with("grupo:"):   # grupo:<id,id,...> — com companheiros contra monstros
		Jogo.nivel = 8
		Jogo.ouro = 99999
		Jogo.andar_maximo = 99
		for idc in args[3].substr(6).split(","):
			Jogo.nivel = maxi(Jogo.nivel, 99 if Grupo.dados(idc).get("origem", "") == "escondido" else 8)
			Grupo.recrutar(idc)
			Grupo.dar_pocao(idc)
		Jogo.nivel = 8
		Jogo.encher()
		Tempo.hora = 11.0
		_passos = [[0.8, "juntar_longe"]]
		for i in 50:   # 50 capturas seguidas (para GIF): os golpes e as skills deles
			_passos.append([1.4 + i * 0.09, "captura"])
		_passos.append([6.0, "fim"])
	elif args.size() > 3 and args[3] == "nadar":   # entra na água funda mais perto e nada (com o Ar a descer no oceano)
		Tempo.hora = 11.0
		_passos = [[0.8, "ir_agua"], [1.0, "mover_direita"], [1.6, "captura"], [2.6, "captura"], [3.0, "atacar"], [3.2, "info_agua"],
				[3.3, "captura"], [3.4, "fim"]]
	elif args.size() > 3 and args[3] == "barco":   # entra no barco do andar e rema para a água funda
		Tempo.hora = 11.0
		_passos = [[1.0, "ir_barco"], [1.2, "mover_direita"], [2.4, "captura"], [3.4, "-mover_direita"], [3.5, "info_barco"], [3.6, "captura"], [3.7, "fim"]]
	elif args.size() > 3 and args[3] == "barco_sair":   # entra no barco e sai logo para o cais
		Tempo.hora = 11.0
		_passos = [[1.0, "ir_barco"], [1.5, "sair_barco"], [1.8, "info_barco"], [1.9, "fim"]]
	elif args.size() > 3 and args[3] == "corrente":   # no meio de uma corrente (ww) e ver para onde leva
		Tempo.hora = 11.0
		_passos = [[1.0, "ir_corrente"], [3.0, "info_barco"], [3.1, "captura"], [3.2, "fim"]]
	elif args.size() > 3 and args[3] == "contratar":   # a lista da Lyra
		Jogo.ouro = 300
		Jogo.andar_maximo = 16
		_passos = [[1.0, "contratar"], [1.5, "captura"], [1.6, "fim"]]
	elif args.size() > 3 and args[3] == "escondido":   # vai ter com o companheiro escondido do andar e fala com ele
		Jogo.nivel = 99
		Tempo.hora = 11.0
		_passos = [[1.0, "ir_escondido"], [2.0, "captura"], [2.1, "falar_escondido"], [2.6, "captura"], [2.7, "fim"]]
	elif args.size() > 3 and args[3] == "status":
		_passos = [[0.5, "preparar_status"], [1.4, "abrir_status"], [1.8, "captura"], [1.9, "aba_ativas"], [2.3, "captura"], [2.4, "fim"]]
	elif args.size() > 3 and args[3] == "skills":
		_passos = [[0.5, "preparar_status"], [1.2, "juntar"], [1.5, "skill_1"], [1.62, "captura"], [2.6, "skill_2"], [2.75, "captura"],
				[3.6, "skill_3"], [3.68, "captura"], [3.8, "captura"], [4.0, "fim"]]
	elif args.size() > 3 and args[3] == "skills_filme":   # 4 skills do herói (área, vários golpes, linha, investida), para GIF
		_passos = [[0.5, "preparar_status"], [0.6, "barra_filme"], [1.2, "juntar"], [1.5, "skill_1"], [2.6, "skill_2"], [3.6, "skill_3"], [4.6, "skill_4"]]
		for i in 44:
			_passos.append([1.45 + i * 0.09, "captura"])
		_passos.sort_custom(func(a, b): return a[0] < b[0])
		_passos.append([5.6, "fim"])
	elif args.size() > 3 and args[3] == "crafting":
		_passos = [[0.8, "preparar_crafting"], [1.2, "abrir_forja"], [1.6, "captura"], [1.7, "aba_melhorar"], [2.1, "captura"], [2.2, "fim"]]
	elif args.size() > 3 and args[3] == "recolha":
		_passos = [[0.8, "ir_recolha"], [1.6, "captura"], [1.7, "usar"], [2.2, "usar"], [2.7, "usar"], [2.8, "captura"], [3.4, "captura"], [3.5, "fim"]]
	elif args.size() > 3 and args[3].begins_with("clima"):   # clima:<efeito>:<hora>
		var partes: PackedStringArray = args[3].split(":")
		Tempo.hora = float(partes[2])
		_clima = partes[1]
		_passos = [[0.3, "clima"], [2.0, "captura"], [2.1, "fim"]]
	elif args.size() > 3 and args[3] == "dialogo":
		_passos = [[0.6, "npc"], [1.0, "falar_npc"], [2.6, "captura"], [2.7, "avancar"], [4.6, "avancar"], [6.4, "captura"], [6.5, "fim"]]
	elif args.size() > 3 and args[3] == "missoes":
		_passos = [[0.6, "preparar_missoes"], [1.0, "abrir_quadro"], [1.5, "captura"], [1.6, "abrir_diario"], [2.0, "captura"], [2.1, "fim"]]
	elif args.size() > 3 and args[3] == "mapa":   # vista de muito alto, às 10:00
		Tempo.hora = 10.0
		_passos = [[0.3, "longe"], [2.5, "captura"], [2.6, "fim"]]
	elif args.size() > 3 and args[3].begins_with("ir:"):   # ir:<código do edifício> (cidade), às 10:00
		Tempo.hora = 10.0
		_local = args[3].substr(3)
		_passos = [[0.4, "ir"], [2.0, "captura"], [2.1, "fim"]]
	elif args.size() > 3 and args[3].begins_with("pov"):   # pov[:hora] — no meio da povoação do andar
		Tempo.hora = float(args[3].split(":")[1]) if ":" in args[3] else 11.0
		_passos = [[0.4, "pov"], [1.8, "captura"], [1.9, "fim"]]
	elif args.size() > 3 and args[3] == "boss":
		_passos = [[0.6, "ir_boss"], [1.6, "captura"], [3.2, "captura"], [3.3, "fase"], [4.4, "captura"], [5.6, "captura"], [5.7, "matar_boss"], [7.5, "captura"], [7.6, "fim"]]
	elif args.size() > 3 and args[3] == "mapa_ui":
		_passos = [[0.6, "explorar"], [1.4, "captura"], [1.5, "abrir_mapa"], [2.2, "captura"], [2.3, "torre"], [2.8, "captura"], [2.9, "fim"]]
	elif args.size() > 3 and args[3] == "debug_mm":
		_passos = [[1.0, "debug_mm"], [1.1, "fim"]]
	elif args.size() > 3 and args[3] == "debug_ap":
		_passos = [[1.0, "debug_ap"], [1.1, "fim"]]
	elif args.size() > 3 and args[3] == "p2":   # o início do jogo (cena P2 do prólogo)
		Jogo.novo_jogo("Mira")
		Jogo.aparencia = {"penteado": "rabo", "pele": "morena", "cabelo": "ruivo", "olhos": "verde", "roupa": "camisola_capuz"}
		Jogo.tratamento = "ela"
		Jogo.por_flag("prologo_p2")
		Tempo.hora = 7.0
		_passos = [[5.0, "captura"], [9.0, "captura"], [9.1, "fim"]]
	elif args.size() > 3 and args[3].begins_with("chamar:"):   # chamar:<método da cena> e capturar
		_local = args[3].substr(7)
		_passos = [[0.5, "chamar"], [1.8, "captura"], [5.5, "captura"], [5.6, "fim"]]
	elif args.size() > 3 and args[3].begins_with("filme:"):   # filme:<fx>:<fz>:<hora> — 40 capturas seguidas (para GIF)
		var partes: PackedStringArray = args[3].split(":")
		_local = partes[1] + ":" + partes[2]
		Tempo.hora = float(partes[3]) if partes.size() > 3 else 10.0
		_passos = [[0.5, "pos"], [0.6, "medio_perto"]]
		for i in 40:
			_passos.append([3.0 + i * 0.1, "captura"])
		_passos.append([7.2, "fim"])
	elif args.size() > 3 and args[3].begins_with("pos:"):   # pos:<fx>:<fz>:<hora> (fração do mapa, -0.5 a 0.5)
		var partes: PackedStringArray = args[3].split(":")
		_local = partes[1] + ":" + partes[2]
		Tempo.hora = float(partes[3]) if partes.size() > 3 else 10.0
		_passos = [[0.5, "pos"], [2.2, "captura"], [2.3, "medio"], [3.4, "captura"], [3.5, "fim"]]
	elif args.size() > 3 and args[3].begins_with("orto:"):   # orto:<inclinação>:<altura vista em m> — câmara sem perspetiva
		var partes: PackedStringArray = args[3].split(":")
		_local = partes[1] + ":" + partes[2]
		Tempo.hora = 10.0
		_passos = [[0.3, "orto"], [2.2, "captura"], [2.3, "fim"]]
	elif args.size() > 3 and args[3] == "passeio":   # anda, ataca e esquiva, com 50 capturas seguidas (para GIF)
		_passos = [[0.5, "juntar"], [0.9, "mover_direita"], [1.7, "-mover_direita"], [1.75, "atacar"], [2.1, "atacar"], [2.5, "mover_baixo"],
				[3.2, "-mover_baixo"], [3.25, "mover_esquerda"], [3.5, "esquivar"], [3.9, "-mover_esquerda"], [4.0, "atacar"]]
		for i in 50:
			_passos.append([0.95 + i * 0.08, "captura"])
		_passos.sort_custom(func(a, b): return a[0] < b[0])
		_passos.append([5.0, "fim"])
	elif args.size() > 3 and args[3] == "taberna":   # os jogos da Taberna
		_passos = [[0.6, "tab_prep"], [0.8, "tab_dados"], [1.8, "captura"], [1.9, "tab_cartas"], [2.4, "captura"], [2.5, "tab_cartas2"],
				[3.0, "captura"], [3.1, "tab_jogar"], [3.6, "captura"], [3.7, "tab_braco"], [4.6, "captura"], [4.7, "fim"]]
	elif args.size() > 3 and args[3].begins_with("entrar:"):   # entrar:<código>:<hora> — entra no edifício (cidade) ou na casa n (povoação)
		var partes: PackedStringArray = args[3].split(":")
		_local = partes[1]
		Tempo.hora = float(partes[2]) if partes.size() > 2 else 11.0
		_passos = [[0.5, "entrar"], [1.6, "captura"], [1.7, "fim"]]
	elif args.size() > 3 and args[3] == "arena":   # Arena de Bronze: entrar e ver a 1.ª onda
		Tempo.hora = 15.0
		_passos = [[0.5, "arena"], [3.6, "captura"], [3.7, "medio_perto"], [4.6, "captura"], [4.7, "fim"]]
	elif args.size() > 3 and args[3].begins_with("corrida:"):   # corrida:<id> — 3 capturas a correr
		_corrida = args[3].split(":")[1]
		_passos = [[0.6, "corrida"], [2.6, "captura"], [4.6, "captura"], [6.6, "captura"], [6.7, "fim"]]
	elif args.size() > 3 and args[3].begins_with("masmorra:"):   # masmorra:<região> — a 1.ª sala e a sala do boss
		_corrida = args[3].split(":")[1]
		_passos = [[0.6, "masmorra"], [2.6, "captura"], [2.7, "masmorra_sala2"], [4.6, "captura"], [4.7, "masmorra_sala3"], [6.6, "captura"],
				[6.7, "masmorra_boss"], [8.6, "captura"], [8.7, "fim"]]
	elif args.size() > 3 and args[3] == "ritmo":
		_passos = [[0.6, "ritmo"], [3.4, "captura"], [3.5, "fim"]]
	elif args.size() > 3 and args[3] == "aldeoes":   # Ascendia: os aldeões mais perto dizem uma frase
		Tempo.hora = 11.0
		_local = "Fn"
		_passos = [[0.4, "ir"], [1.6, "falar_aldeoes"], [2.2, "captura"], [2.3, "fim"]]
	elif args.size() > 3 and args[3] == "colecoes":
		_passos = [[0.5, "preparar_col"], [0.8, "abrir_pagina"], [2.6, "captura"], [2.7, "fechar_pagina"], [2.9, "pescar"],
				[3.2, "fisgar"], [3.9, "captura"], [4.0, "abrir_bestiario"], [4.4, "captura"], [4.5, "fim"]]
	elif args.size() > 3 and args[3] == "toque":
		_passos = [[0.6, "toque"], [1.5, "captura"], [1.6, "fim"]]
	elif args.size() > 3 and args[3] == "estados":   # põe estados no herói e nos monstros
		_passos = [[1.0, "estados"], [1.6, "captura"], [2.6, "captura"], [2.7, "fim"]]
	elif args.size() > 3 and args[3].begins_with("esquiva"):   # esquiva[:segundos] — luta com o boss: esquiva no último momento e golpeia; grava todos os frames (para GIF)
		var seg := float(args[3].split(":")[1]) if ":" in args[3] else 12.0
		for idc in ["c1_02_javali_antes", "c1_03_javali_depois"]:   # sem as cenas da história (a conversa com o Kai)
			Jogo.por_flag("cena_cena_" + idc)
		_passos = [[0.6, "ir_boss_filme"], [1.2, "gravar:%d" % int(seg * 20.0)], [1.4 + seg * 1.6, "fim"]]
	elif args.size() > 3 and args[3].begins_with("praca"):   # praca[:hora[:código[:dx:dz]]] — Ascendia, com os aldeões à volta (para a página do jogo)
		var partes: PackedStringArray = args[3].split(":")
		Tempo.hora = float(partes[1]) if partes.size() > 1 else 17.0
		_local = partes[2] if partes.size() > 2 else "Fn"
		_desvio = Vector3(float(partes[3]), 0, float(partes[4])) if partes.size() > 4 else Vector3.ZERO
		_passos = [[0.4, "ir"], [1.0, "juntar_aldeoes"], [2.6, "captura"], [2.7, "fim"]]
	elif args.size() > 3 and args[3] == "forja":   # a Forja do Brom: entra, chega-se ao Brom, e depois abre a forja
		Tempo.hora = 11.0
		_local = "Fo"
		_passos = [[0.5, "entrar"], [1.2, "mover_cima"], [1.5, "-mover_cima"], [2.8, "captura"], [2.9, "preparar_crafting"],
				[3.0, "abrir_forja"], [3.6, "captura"], [3.7, "fim"]]
	elif args.size() > 3:   # só uma captura (para ver vários andares depressa)
		_passos = [[1.5, "captura"], [1.6, "vista"], [3.0, "captura"], [3.1, "fim"]]
	process_mode = Node.PROCESS_MODE_ALWAYS
	if OS.get_environment("SEM2D") != "":
		Opcoes.valores["vista_2d"] = false
	var tam := OS.get_environment("ROBO_TAM")
	if tam != "":
		var p := tam.split("x")
		get_tree().root.content_scale_stretch = Window.CONTENT_SCALE_STRETCH_FRACTIONAL
		get_window().size = Vector2i(int(p[0]), int(p[1]))
	_zoom = float(OS.get_environment("ROBO_ZOOM"))
	process_priority = 1000   # depois da Vista2D (para o zoom fixo ganhar)
	DirAccess.make_dir_recursive_absolute(pasta)
	add_child(load(cena).instantiate())


func _process(delta: float) -> void:
	_t += delta
	# um passo por frame (com poucos FPS, vários passos podiam calhar no mesmo frame)
	if _i < _passos.size() and _t >= _passos[_i][0]:
		_fazer(_passos[_i][1])
		_i += 1
	if _zoom > 0.0 and Vista2D.atual and is_instance_valid(Vista2D.atual):
		Vista2D.atual.camara.zoom = Vector2.ONE * _zoom
	if OS.get_environment("ROBO_SEM_HUD") != "":
		for n in get_tree().root.find_children("*", "CanvasLayer", true, false):
			for k in [n, n.get_parent()]:
				if k and k.get_script() and "/ui/" in (k.get_script() as Script).resource_path:
					n.visible = false
	if _reflexo:
		_reagir()
	if _gravar > 0:
		_gravar -= 1
		_fazer("captura")


## O "reflexo" do filme da esquiva: quando o golpe do boss está quase a sair, esquiva para o lado (de lado em
## relação ao boss) e logo a seguir vira-se para ele e dá 3 golpes.
func _reagir() -> void:
	var b = get_tree().get_first_node_in_group("bosses")
	var j := get_tree().get_first_node_in_group("jogador") as Node3D
	if b == null or j == null or b.estado == "morto":
		return
	var d: Vector3 = b.global_position - j.global_position
	d.y = 0.0
	var dt := _t - _reflexo_t
	if _reflexo_fase != 1 and b.estado == "aviso" and b._t >= float(b._ataque.get("aviso", 0.5)) - 0.1:
		# o golpe está quase a sair: esquiva de lado (em relação à linha boss → herói)
		for a in _reflexo_acoes:
			Input.action_release(a)
		var lado := Vector2(-d.z, d.x)
		_reflexo_acoes = [("mover_direita" if lado.x > 0 else "mover_esquerda") if absf(lado.x) > absf(lado.y) else ("mover_baixo" if lado.y > 0 else "mover_cima")]
		for a in _reflexo_acoes:
			Input.action_press(a)
		_fazer("esquivar")
		_reflexo_t = _t
		_reflexo_fase = 1
		return
	match _reflexo_fase:
		1:   # a esquiva acabou: vira-se para o boss e chega-se a ele
			if dt > 0.3:
				for a in _reflexo_acoes:
					Input.action_release(a)
				_reflexo_acoes = []
				if absf(d.x) > 0.5:
					_reflexo_acoes.append("mover_direita" if d.x > 0 else "mover_esquerda")
				if absf(d.z) > 0.5:
					_reflexo_acoes.append("mover_baixo" if d.z > 0 else "mover_cima")
				for a in _reflexo_acoes:
					Input.action_press(a)
				_reflexo_fase = 2
		2:   # perto o bastante: 3 golpes
			if d.length() < 2.8 or dt > 2.0:
				for a in _reflexo_acoes:
					Input.action_release(a)
				_reflexo_acoes = []
				for k in 3:
					get_tree().create_timer(0.02 + k * 0.32).timeout.connect(_fazer.bind("atacar"))
				_reflexo_fase = 3
		3:   # um pouco depois, se o boss não atacar, volta à carga
			if dt > (1.0 if d.length() > 3.2 else 1.5):
				_reflexo_t = _t - 0.31
				_reflexo_fase = 1
		_:   # ao princípio: vai ter com o boss
			_reflexo_t = _t - 0.31
			_reflexo_fase = 1


func _fazer(acao: String) -> void:
	if acao.begins_with("gravar:"):
		_gravar = int(acao.substr(7))
		return
	match acao:
		"":
			pass
		"ir_boss_filme":   # como ir_boss, mas sem invencibilidade (o herói não pisca) e forte para aguentar
			Jogo.nivel = 30
			Jogo.encher()
			var b = get_tree().get_first_node_in_group("bosses")
			var j := get_tree().get_first_node_in_group("jogador")
			if b:
				j.global_position = b.arena_centro + Vector3(-1.5, 0.5, 4.5)
			j.invencivel = 0.0
			_reflexo = true
		"juntar_aldeoes":   # os aldeões mais perto vêm para a praça, à volta do herói
			var j := get_tree().get_first_node_in_group("jogador") as Node3D
			var gente := get_tree().get_nodes_in_group("transeuntes")
			gente.sort_custom(func(a, b): return a.global_position.distance_to(j.global_position) < b.global_position.distance_to(j.global_position))
			var lugares := [Vector3(-4.5, 0.3, -1.0), Vector3(3.5, 0.3, -2.5), Vector3(5.0, 0.3, 1.5), Vector3(-2.5, 0.3, 2.5),
					Vector3(-7.0, 0.3, 2.0), Vector3(1.5, 0.3, -4.5), Vector3(8.0, 0.3, -1.0), Vector3(-8.5, 0.3, -3.0)]
			for k in mini(lugares.size(), gente.size()):
				gente[k].global_position = j.global_position + lugares[k]
		"captura":
			print("ROBO: process ", snappedf(Performance.get_monitor(Performance.TIME_PROCESS) * 1000.0, 0.01), " ms")
			if Vista2D.atual:
				var jj := get_tree().get_first_node_in_group("jogador") as Node3D
				print("ROBO 2D: vista ", int(Vista2D.atual.tempo_us), " us  process ", snappedf(Performance.get_monitor(Performance.TIME_PROCESS) * 1000.0, 0.01), " ms  física ",
						snappedf(Performance.get_monitor(Performance.TIME_PHYSICS_PROCESS) * 1000.0, 0.01), " ms  nós ",
						Performance.get_monitor(Performance.OBJECT_NODE_COUNT), "  2D ", Vista2D.atual.mundo.get_child_count())
				print("ROBO 2D: camara ", Vista2D.atual.camara.global_position, " heroi ", Vista2D.ecra(jj.global_position) if jj else Vector2.ZERO,
						" ", Vista2D.atual._proxies.size(), " espelhos")
				if OS.get_environment("DEBUG2D") != "":
					var hp: Vector2 = Vista2D.ecra(jj.global_position)
					for pr in Vista2D.atual._proxies:
						var no: Node2D = pr.no
						if pr.tipo == "caixa" and no.visible:
							for pg in no.get_children():
								if pg is Polygon2D:
									var r := Rect2(pg.polygon[0], Vector2.ZERO)
									for q in pg.polygon:
										r = r.expand(q)
									r.position += no.global_position
									if r.has_point(hp):
										print("  CAIXA ", pr.fonte.name, " ", pr.fonte.get_parent().name, " y-sort ", no.position.y, " rect ", r, " cor ", pg.color, " z ", no.z_index)
						elif pr.tipo in ["sprite", "animado"] and absf(no.position.x - hp.x) < 20 and absf(no.position.y - hp.y - 0) < 40:
							print("  SPRITE ", pr.fonte.name, " y ", no.position.y, " vis ", no.get_child(0).visible)
			await RenderingServer.frame_post_draw
			var img := get_viewport().get_texture().get_image()
			img.save_png("%s/captura_%02d.png" % [pasta, _n])
			_n += 1
		"ir":
			var cid := get_tree().current_scene.get_child(0)
			for n in get_tree().root.find_children("*", "Node3D", true, false):
				if "locais" in n:
					cid = n
			var j := get_tree().get_first_node_in_group("jogador")
			j.global_position = cid.locais[_local] + Vector3(0, 0.5, 4.0) + _desvio
			cid._rotinas(true)
		"pov":
			var a := get_tree().current_scene.get_child(0)
			var j := get_tree().get_first_node_in_group("jogador")
			if "_centro_pov" in a and a._centro_pov != Vector3.ZERO:
				j.global_position = a._centro_pov + Vector3(0, 0.5, 6.0)
			else:
				print("ROBO: este andar não tem povoação")
		"ir_boss":
			Jogo.nivel = 12
			Jogo.encher()
			var b = get_tree().get_first_node_in_group("bosses")
			var j := get_tree().get_first_node_in_group("jogador")
			print("ROBO: boss ", b.id if b else "nenhum", " fases ", b.fases.size() if b else 0)
			if b:
				print("ROBO: boss em ", b.global_position, " sprite vis ", b.sprite.is_visible_in_tree(), " anim ", b.sprite.animation, " tam ", b._tamanho_px, " mod ", b.sprite.modulate)
				if Vista2D.atual:
					for pr in Vista2D.atual._proxies:
						if pr.fonte == b.sprite:
							var a2: AnimatedSprite2D = pr.no.get_child(0)
							print("ROBO: espelho do boss em ", pr.no.global_position, " + ", a2.position, " vis ", a2.visible, " anim ", a2.animation, " escala ", a2.scale, " z ", pr.no.z_index)
			j.global_position = b.arena_centro + Vector3(0, 0.5, 6.0)
			j.invencivel = 999.0
		"fase":
			var b = get_tree().get_first_node_in_group("bosses")
			b.hp = b.hp_max * 0.5
			var j := get_tree().get_first_node_in_group("jogador")
			b.receber_golpe(j.golpe_com(b, 1.0, "", []))
			print("ROBO: fase agora ", b.fase + 1)
		"matar_boss":
			var b = get_tree().get_first_node_in_group("bosses")
			b._invencivel = 0.0
			b.hp = 1.0
			var j := get_tree().get_first_node_in_group("jogador")
			b.receber_golpe(j.golpe_com(b, 1.0, "", []))
			print("ROBO: boss morto ", b.estado, " flags ", Jogo.flags)
		"explorar":
			var vistas: Dictionary = Jogo.explorado.get_or_add(str(Jogo.andar_atual), {})
			for y in 12:
				for x in 15:
					if (x + y * 3) % 7 < 5:
						vistas["%d,%d" % [x, y + 3]] = true
			Jogo.cristais = [1, 5]
			Jogo.andar_maximo = 12
		"abrir_mapa":
			var m = get_tree().get_first_node_in_group("mapa_ui")
			m.abrir(true)
		"torre":
			var m = get_tree().get_first_node_in_group("mapa_ui")
			m._aba = "torre"
			m._mostrar()
		"debug_mm":
			var n := 0
			var c := 0
			for mi in get_tree().root.find_children("*", "MultiMeshInstance3D", true, false):
				n += 1
				if mi.multimesh.use_colors:
					c += 1
					print("ROBO: cores ", mi.multimesh.mesh.resource_path, " ", mi.material_override, " ", mi.multimesh.get_instance_color(5))
			print("ROBO: multimeshes ", n, " com cor ", c)
		"debug_ap":
			var j := get_tree().get_first_node_in_group("jogador")
			var m: ShaderMaterial = j.boneco.corpo.material
			print("ROBO: material ", m, " n=", m.get_shader_parameter("n") if m else -1)
			if m:
				print("ROBO: de ", m.get_shader_parameter("de").slice(5, 8), " para ", m.get_shader_parameter("para").slice(5, 8))
			var img: Image = j.boneco.viewport.get_texture().get_image()
			var cores := {}
			for x in img.get_width():
				for y in img.get_height():
					var c := img.get_pixel(x, y)
					if c.a > 0.5:
						cores[c.to_html(false)] = true
			print("ROBO: cores ", cores.keys().slice(0, 30))
		"chamar":
			var cena := get_child(get_child_count() - 1)
			for parte in _local.split(","):
				var p: PackedStringArray = parte.split("=")
				if p.size() == 2:   # caminho=valor (ex.: _dir=1)
					cena.set(p[0], int(p[1]))
				else:
					cena.call(parte)
		"preparar_col":
			Jogo.apanhar("cana_bambu")
			for k in 7:
				Eventos.monstro_morto.emit("slime_verde", 1)
			Eventos.monstro_morto.emit("lobo_cinzento", 2)
			Colecoes.pagina(1)
			Colecoes.pagina(2)
		"abrir_pagina":
			get_tree().get_first_node_in_group("pagina_ui").mostrar(1)
		"fechar_pagina":
			var ui = get_tree().get_first_node_in_group("pagina_ui")
			ui.visible = false
			get_tree().paused = false
		"pescar":
			get_tree().get_first_node_in_group("pesca_ui").pescar(3, false)
		"fisgar":
			get_tree().get_first_node_in_group("pesca_ui")._comecar_puxar()
		"abrir_bestiario":
			var p = get_tree().get_first_node_in_group("pesca_ui")
			p._acabar(true, "")
			var q = get_tree().get_first_node_in_group("diario_ui")
			q.abrir(true)
			q._aba = "bestiario"
			q._mostrar()
			q._detalhe_monstro(Dados.monstro("slime_verde"))
		"toque":
			Entrada.dispositivo = "toque"
			Entrada.dispositivo_mudou.emit("toque")
			var ev := InputEventScreenTouch.new()
			ev.index = 0
			ev.position = Vector2(220, 520)
			ev.pressed = true
			Input.parse_input_event(ev)
			var dr := InputEventScreenDrag.new()
			dr.index = 0
			dr.position = Vector2(270, 500)
			Input.parse_input_event(dr)
		"longe":
			var cam := get_viewport().get_camera_3d()
			if cam is Camara:
				cam.distancia = 190.0
				cam.rotation_degrees.x = -68.0
				cam.far = 600.0
		"pos":
			var a: Node = get_child(0)
			var f: PackedStringArray = _local.split(":")
			var alt: int = a.altura_cel if "altura_cel" in a else (a.altura if "altura" in a else 0)
			if f[0] == "pov":   # à frente da povoação do andar
				a.jogador.global_position = a._centro_pov + Vector3(0, 2.0, 7.0)
			elif f[0] == "ponto":   # ao pé do primeiro ponto com esta marca (ex.: !!)
				for pt in a.dados.pontos:
					if pt.marca == f[1]:
						a.jogador.global_position = a.centro_celula(int(pt.x), int(pt.y)) + Vector3(0, 2.0, 5.0)
						break
			else:
				a.jogador.global_position = Vector3(float(f[0]) * a.largura * 10.0, 3.0, float(f[1]) * alt * 10.0)
		"entrar":
			var a: Node = get_child(0)
			var j := get_tree().get_first_node_in_group("jogador") as Node3D
			var alvo := Vector3.INF
			if "locais" in a and a.locais.has(_local):
				alvo = a.locais[_local]
			var portas: Array = []
			for i in get_tree().get_nodes_in_group("interagivel"):
				if String(i.texto).begins_with("Entrar"):
					portas.append(i)
			if alvo != Vector3.INF:
				portas.sort_custom(func(x, y): return x.global_position.distance_to(alvo) < y.global_position.distance_to(alvo))
			elif _local.is_valid_int() and portas.size() > int(_local):
				portas = [portas[int(_local)]]
			if not portas.is_empty():
				portas[0].usado.emit(j)
		"orto":
			var cam := get_viewport().get_camera_3d()
			var f: PackedStringArray = _local.split(":")
			if cam is Camara:
				cam.rotation_degrees.x = -float(f[0])
				if float(f[1]) > 0.0:
					cam.projection = Camera3D.PROJECTION_ORTHOGONAL
					cam.size = float(f[1])
				cam.saltar()
		"ritmo":
			get_tree().get_first_node_in_group("ritmo_ui").dancar("mia")
		"corrida":
			get_tree().get_first_node_in_group("corrida_ui").correr(_corrida)
		"masmorra":
			Masmorra.entrar(get_child(0), int(_corrida), Vector3.ZERO)
		"masmorra_sala2", "masmorra_sala3", "masmorra_boss":
			var j := get_tree().get_first_node_in_group("jogador") as Node3D
			if j and Masmorra.atual:
				var i: int = {"masmorra_sala2": 1, "masmorra_sala3": 2}.get(acao, 3)
				j.global_position = Masmorra.ORIGEM + Masmorra.atual.centro(i) + Vector3(0, 0.5, Masmorra.FUNDO / 2.0 - 2.0)
				var cam := get_viewport().get_camera_3d()
				if cam and cam.has_method("saltar"):
					cam.saltar()
		"arena":
			Jogo.pontos_guilda = 100000
			Jogo.andar_maximo = 12
			Arena.entrar(get_child(0), "bronze", Vector3(0, 1, 0))
		"tab_prep":
			Jogo.ouro = 800
			for m in ["slime_verde", "coelho_chifre", "lobo_cinzento", "javali", "cogumelo_andante", "abelha_gigante", "morcego", "golem_pedra"]:
				Jogo.bestiario[m] = 3
		"tab_dados":
			var ui = get_tree().get_first_node_in_group("taberna_ui")
			ui.abrir_dados()
			ui._aposta = 50
			ui._dados_comecar()
		"tab_cartas":
			get_tree().get_first_node_in_group("taberna_ui").abrir_cartas("rook")
		"tab_cartas2":
			var ui = get_tree().get_first_node_in_group("taberna_ui")
			ui._aposta = 50
			ui._cartas_comecar()
		"tab_jogar":
			var ui = get_tree().get_first_node_in_group("taberna_ui")
			ui._cartas_jogar(ui._mao[0])
		"tab_braco":
			var ui = get_tree().get_first_node_in_group("taberna_ui")
			ui.abrir_braco("brom")
			ui._aposta = 50
			ui._braco_comecar()
		"falar_aldeoes":
			var j := get_tree().get_first_node_in_group("jogador") as Node3D
			var gente := get_tree().get_nodes_in_group("transeuntes")
			gente.sort_custom(func(a, b): return a.global_position.distance_to(j.global_position) < b.global_position.distance_to(j.global_position))
			for k in mini(3, gente.size()):
				gente[k].global_position = j.global_position + Vector3(-3.0 + k * 3.0, 0.3, -2.5)
				gente[k]._dizer()
		"medio_perto":
			var cam := get_viewport().get_camera_3d()
			if cam is Camara:
				cam.distancia = 24.0
		"medio":
			var cam := get_viewport().get_camera_3d()
			if cam is Camara:
				cam.distancia = 34.0
				cam.rotation_degrees.x = -42.0
		"vista":
			var cam2 := get_viewport().get_camera_2d()
			if cam2:
				cam2.zoom = Vector2(1.5, 1.5)
			var cam := get_viewport().get_camera_3d()
			if cam is Camara:
				cam.distancia = 70.0
				cam.rotation_degrees.x = -60.0
		"estados":
			var j := get_tree().get_first_node_in_group("jogador")
			j.estados.aplicar("veneno")
			j.estados.aplicar("frio")
			Jogo.usar_consumivel("pocao_vida_p")
			Jogo.buffs["atq"] = [0.2, 60.0]
			var n := 0
			for m in get_tree().get_nodes_in_group("monstros"):
				m.global_position = j.global_position + Vector3(2 + n * 1.5, 0, -1.5)
				m.estados.aplicar(["queimadura", "congelado", "veneno", "atordoado"][n % 4])
				n += 1
				if n >= 4:
					break
		"preparar_status":
			Jogo.origem = "dormir"
			Jogo.skill_unica = "olho_do_sistema"
			Jogo.ganhar_xp(6000)
			Jogo.treinar_arma("espada", 300)
			Jogo.treinar_arma("arco", 60)
			Jogo.treinar_vida("mineracao", 45)
			Jogo.nivel = 25
			Jogo.escolher_classe("espadachim")
			Jogo.skills_barra = ["lamina_de_vento", "corte_rapido", "corte_duplo", "", "", ""]
			Jogo.encher()
			for m in get_tree().get_nodes_in_group("monstros"):
				m.queue_free()
		"juntar":
			var j := get_tree().get_first_node_in_group("jogador")
			j.direcao_olhar = Vector2(1, 0)
			for k in 4:
				var m: Monstro = Monstro.new().configurar("slime_verde", 3)
				j.get_parent().add_child(m)
				m.global_position = j.global_position + Vector3(2.0 + k * 1.3, 0.2, 0.3 * (k % 2))
		"juntar_longe":   # monstros a 6 m (para os companheiros lutarem)
			var j := get_tree().get_first_node_in_group("jogador")
			for k in 5:
				var m: Monstro = Monstro.new().configurar("slime_verde", 4)
				j.get_parent().add_child(m)
				m.global_position = j.global_position + Vector3(5.0 + k * 1.2, 0.2, -1.0 + 0.6 * k)
		"ir_escondido":
			var e := get_tree().get_first_node_in_group("escondidos") as Node3D
			var j := get_tree().get_first_node_in_group("jogador") as Node3D
			if e:
				j.global_position = e.global_position + Vector3(0, 0.5, 1.2)
				print("ROBO: escondido em ", e.global_position)
			else:
				print("ROBO: nenhum escondido neste andar")
		"falar_escondido":
			var e := get_tree().get_first_node_in_group("escondidos")
			if e:
				get_tree().get_first_node_in_group("grupo_ui").abrir_recrutar(e.id)
		"ir_agua":   # a célula de água funda mais perto da chegada
			var a = get_child(0)
			var j := get_tree().get_first_node_in_group("jogador") as Node3D
			var melhor := Vector3.INF
			for cy in a.altura_cel:
				for cx in a.largura:
					if a.codigo(cx, cy) == "~~":
						var p: Vector3 = a.centro_celula(cx, cy)
						if melhor == Vector3.INF or p.distance_to(j.global_position) < melhor.distance_to(j.global_position):
							melhor = p
			if melhor != Vector3.INF:
				j.global_position = melhor + Vector3(-2.0, 0.5, 0)
		"ir_barco":
			var b = get_tree().get_first_node_in_group("barcos")
			var j = get_tree().get_first_node_in_group("jogador")
			if b:
				j.global_position = b.global_position + Vector3(0, 0.5, 0.8)
				j.entrar_barco(b)
			print("ROBO: barco ", b != null)
		"ir_corrente":
			var a = get_child(0)
			var j = get_tree().get_first_node_in_group("jogador")
			for cy in a.altura_cel:
				for cx in a.largura:
					if a.codigo(cx, cy) == "ww":
						j.global_position = a.centro_celula(cx, cy) + Vector3(0, 0.5, 0)
						print("ROBO: corrente início ", j.global_position, " leva ", a.corrente_em(j.global_position))
						return
		"sair_barco":
			get_tree().get_first_node_in_group("jogador").sair_barco()
		"info_barco":
			var j = get_tree().get_first_node_in_group("jogador")
			print("ROBO: no barco=", j.barco != null, " a_nadar=", j.a_nadar, " ar=", snappedf(Jogo.ar, 0.1), " pos=", j.global_position)
		"info_agua":
			var j := get_tree().get_first_node_in_group("jogador")
			print("ROBO: a_nadar=", j.a_nadar, " ar=", snappedf(Jogo.ar, 0.1), " estado=", j.estado, " encharcado=", j.estados.tem("encharcado"))
		"contratar":
			get_tree().get_first_node_in_group("grupo_ui").abrir_modo("contratar")
		"abrir_grupo":
			var g = get_tree().get_first_node_in_group("grupo_ui")
			if g:
				g.abrir(true)
		"barra_filme":
			Jogo.treinar_arma("espada", 2000)
			Jogo.skills_barra = ["lamina_giratoria", "corte_duplo", "lamina_de_vento", "corte_rapido", "", ""]
			Jogo.mp = 999
			Jogo.estamina = 999
		"skill_4":
			var j := get_tree().get_first_node_in_group("jogador")
			j._ultimo_rato = -100.0
			j.direcao_olhar = Vector2(1, 0)
			j.usar_skill(3)
		"skill_1", "skill_2", "skill_3":
			var j := get_tree().get_first_node_in_group("jogador")
			j._ultimo_rato = -100.0
			j.direcao_olhar = Vector2(1, 0)
			j.usar_skill(int(acao.right(1)) - 1)
		"abrir_status":
			for ui in get_tree().get_nodes_in_group("janelas"):
				if ui.acao == "status":
					ui.abrir(true)
		"aba_ativas":
			for ui in get_tree().get_nodes_in_group("janelas"):
				if ui.acao == "status":
					ui._separador = "ativas"
					ui._mostrar()
		"preparar_crafting":
			for par in [["minerio_cobre", 7], ["carvalho", 3], ["lingote_cobre", 4], ["couro_javali", 2], ["erva_verde", 4], ["agua_limpa", 2]]:
				Jogo.apanhar(par[0], par[1])
			Jogo.ganhar_ouro(500)
		"abrir_forja":
			var ui = get_tree().get_first_node_in_group("crafting_ui")
			ui.abrir_estacao("forja")
			ui._escolhida = "lingote_cobre"
			ui._mostrar()
		"aba_melhorar":
			var ui = get_tree().get_first_node_in_group("crafting_ui")
			ui._modo = "melhorar"
			ui._escolhida = "espada_cobre"
			ui._mostrar()
		"ir_recolha":
			Jogo.apanhar("picareta_cobre")
			Jogo.apanhar("machado_lenhador_cobre")
			var j := get_tree().get_first_node_in_group("jogador")
			var melhor: Node3D = null
			for n in get_tree().get_nodes_in_group("recolha"):
				if n.ferramenta == "picareta" or melhor == null:
					melhor = n
			print("ROBO: nós de recolha: ", get_tree().get_nodes_in_group("recolha").size(), " -> ", melhor.item, " ", melhor.ferramenta)
			j.global_position = melhor.global_position + Vector3(-1.4, 0.3, 0.4)
		"usar":
			var j := get_tree().get_first_node_in_group("jogador")
			j.estado = "normal"
			var it = j._procurar_interagivel()
			if it:
				it.interagir(j)
		"clima":
			for n in get_tree().root.find_children("*", "CicloDia", true, false):
				n.clima = {"efeito": _clima, "nome_pt": _clima}
				n._aplicar_clima()
		"npc":
			var j := get_tree().get_first_node_in_group("jogador")
			var n := NPC.new().configurar("lyra")
			j.get_parent().add_child(n)
			n.global_position = j.global_position + Vector3(1.2, 0.2, -0.4)
		"falar_npc":
			var j := get_tree().get_first_node_in_group("jogador")
			get_tree().get_first_node_in_group("npcs").conversar_menu(j)
		"avancar":
			get_tree().get_first_node_in_group("dialogo_ui")._avancar.emit()
		"preparar_missoes":
			Missoes.gerar_quadro()
			Missoes.aceitar("G_F_01")
			Missoes.aceitar("H_04")
			for k in 4:
				Eventos.monstro_morto.emit("slime_verde", 1)
		"abrir_quadro":
			var q = get_tree().get_first_node_in_group("diario_ui")
			q.abrir_quadro()
			q._escolhida = Jogo.quadro[0].id
			q._mostrar()
		"abrir_diario":
			var q = get_tree().get_first_node_in_group("diario_ui")
			q.abrir(false)
			q.abrir(true)
			q._escolhida = "G_F_01"
			q._mostrar()
		"inventario":
			for id in ["gel_slime", "espada_ferro", "arco_cobre", "pocao_mana_p", "chave_bau_ouro"]:
				Jogo.apanhar(id, 3 if id == "gel_slime" else 1, {"raridade": "raro"} if id == "espada_ferro" else {})
			Jogo.ganhar_ouro(120)
			var ui = get_tree().get_first_node_in_group("inventario_ui")
			ui.abrir(true)
			ui._escolhido = 1
			ui._mostrar()
		"fim":
			var j := get_tree().get_first_node_in_group("jogador")
			print("ROBO: fim, ", _n, " capturas; HP ", Jogo.hp, "/", Jogo.hp_maximo(), " XP ", Jogo.xp, " jogador em ", j.global_position if j else "?")
			get_tree().quit()
		_:
			var largar := acao.begins_with("-")
			var a := acao.trim_prefix("-")
			if a in ["atacar", "esquivar"]:
				Input.action_press(a)
				await get_tree().physics_frame
				await get_tree().physics_frame
				Input.action_release(a)
			elif largar:
				Input.action_release(a)
			else:
				Input.action_press(a)
