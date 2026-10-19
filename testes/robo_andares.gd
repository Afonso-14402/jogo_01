extends Node
## Robô: monta os 100 andares um a um e verifica que cada um tem jogador, chegada, Zona Segura, escada,
## guardião (se a ficha tiver) e monstros. Uso: godot --headless --path . res://testes/robo_andares.tscn

var problemas: Array[String] = []


func _ready() -> void:
	var de := 1
	var ate := 100
	var args := OS.get_cmdline_user_args()
	if args.size() >= 2:
		de = int(args[0])
		ate = int(args[1])
	for n in range(de, ate + 1):
		Jogo.andar_atual = n
		var t0 := Time.get_ticks_msec()
		var a: Andar = load("res://cenas/mundo/andar.tscn").instantiate()
		add_child(a)
		await get_tree().process_frame
		await get_tree().physics_frame
		var ms := Time.get_ticks_msec() - t0
		var monstros := a.get_tree().get_nodes_in_group("monstros").size()
		var linha := "andar %3d %-32s %4d ms  %dx%d  monstros %2d  guardiao %s  escada %s" % [n, a.dados.get("nome_pt", "?").left(32), ms,
				a.largura, a.altura_cel, monstros, "sim" if a.guardiao else "-", "sim" if a.escada else "-"]
		print(linha)
		if a.jogador == null or a.largura == 0:
			problemas.append("andar %d: não montou" % n)
		if a.escada == null and n < 100 and not (n % 10 == 0):
			problemas.append("andar %d: sem escada" % n)
		if monstros == 0:
			problemas.append("andar %d: sem monstros" % n)
		if a.dados.get("guardiao") and a.guardiao == null:
			problemas.append("andar %d: guardião %s não apareceu" % [n, a.dados.guardiao])
		a.queue_free()
		await get_tree().process_frame
	print("PROBLEMAS (%d):" % problemas.size())
	for p in problemas:
		print("  ", p)
	get_tree().quit()
