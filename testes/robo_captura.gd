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
var _clima := ""
var _local := ""


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
	elif args.size() > 3 and args[3] == "status":
		_passos = [[0.5, "preparar_status"], [1.4, "abrir_status"], [1.8, "captura"], [1.9, "aba_ativas"], [2.3, "captura"], [2.4, "fim"]]
	elif args.size() > 3 and args[3] == "skills":
		_passos = [[0.5, "preparar_status"], [1.2, "juntar"], [1.5, "skill_1"], [1.62, "captura"], [2.6, "skill_2"], [2.75, "captura"],
				[3.6, "skill_3"], [3.68, "captura"], [3.8, "captura"], [4.0, "fim"]]
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
	elif args.size() > 3 and args[3] == "taberna":   # os jogos da Taberna
		_passos = [[0.6, "tab_prep"], [0.8, "tab_dados"], [1.8, "captura"], [1.9, "tab_cartas"], [2.4, "captura"], [2.5, "tab_cartas2"],
				[3.0, "captura"], [3.1, "tab_jogar"], [3.6, "captura"], [3.7, "tab_braco"], [4.6, "captura"], [4.7, "fim"]]
	elif args.size() > 3 and args[3].begins_with("entrar:"):   # entrar:<código>:<hora> — entra no edifício (cidade) ou na casa n (povoação)
		var partes: PackedStringArray = args[3].split(":")
		_local = partes[1]
		Tempo.hora = float(partes[2]) if partes.size() > 2 else 11.0
		_passos = [[0.5, "entrar"], [1.6, "captura"], [1.7, "fim"]]
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
		"ir":
			var cid := get_tree().current_scene.get_child(0)
			for n in get_tree().root.find_children("*", "Node3D", true, false):
				if "locais" in n:
					cid = n
			var j := get_tree().get_first_node_in_group("jogador")
			j.global_position = cid.locais[_local] + Vector3(0, 0.5, 4.0)
			cid._rotinas(true)
		"ir_boss":
			Jogo.nivel = 12
			Jogo.encher()
			var b = get_tree().get_first_node_in_group("bosses")
			var j := get_tree().get_first_node_in_group("jogador")
			print("ROBO: boss ", b.id if b else "nenhum", " fases ", b.fases.size() if b else 0)
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
			var alt: int = a.altura_cel if "altura_cel" in a else a.altura
			if f[0] == "pov":   # à frente da povoação do andar
				a.jogador.global_position = a._centro_pov + Vector3(0, 2.0, 7.0)
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
