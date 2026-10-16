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
	[3.65, "captura"], [4.0, "-mover_cima"], [4.2, "mover_esquerda"], [5.5, "captura"], [5.6, "-mover_esquerda"], [6.0, "fim"],
]
var _i := 0


func _ready() -> void:
	var args := OS.get_cmdline_user_args()
	if args.size() > 0:
		cena = args[0]
	if args.size() > 1:
		pasta = args[1]
	DirAccess.make_dir_recursive_absolute(pasta)
	add_child(load(cena).instantiate())


func _process(delta: float) -> void:
	_t += delta
	while _i < _passos.size() and _t >= _passos[_i][0]:
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
		"fim":
			print("ROBO: fim, ", _n, " capturas; HP ", Jogo.hp, "/", Jogo.hp_maximo(), " XP ", Jogo.xp)
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
