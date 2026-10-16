extends Node
## "Robô" de teste: carrega uma cena, joga sozinho (anda, corre, esquiva, ataca) e grava capturas de ecrã.
## Uso: xvfb-run godot --rendering-driver opengl3 --path . res://testes/robo_captura.tscn -- <cena> <pasta>

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
	elif args.size() > 3 and args[3] == "estados":   # põe estados no herói e nos monstros
		_passos = [[1.0, "estados"], [1.6, "captura"], [2.6, "captura"], [2.7, "fim"]]
	elif args.size() > 3:   # só uma captura (para ver vários andares depressa)
		_passos = [[1.5, "captura"], [1.6, "vista"], [3.0, "captura"], [3.1, "fim"]]
	process_mode = Node.PROCESS_MODE_ALWAYS
	DirAccess.make_dir_recursive_absolute(pasta)
	add_child(load(cena).instantiate())


func _process(delta: float) -> void:
	_t += delta
	# um passo por frame (com poucos FPS, vários passos podiam calhar no mesmo frame)
	if _i < _passos.size() and _t >= _passos[_i][0]:
		_fazer(_passos[_i][1])
		_i += 1


func _fazer(acao: String) -> void:
	match acao:
		"":
			pass
		"captura":
			await RenderingServer.frame_post_draw
			var img := get_viewport().get_texture().get_image()
			img.save_png("%s/captura_%02d.png" % [pasta, _n])
			_n += 1
		"vista":
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
