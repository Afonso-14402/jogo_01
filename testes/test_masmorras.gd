extends GutTest
## As masmorras escondidas (scripts/mundo/masmorra.gd; dados/masmorras.json; docs/TORRE.md 3.1).

var andar: Node


func before_each() -> void:
	get_tree().paused = false   # (algum teste anterior pode ter deixado uma conversa aberta)
	Jogo.novo_jogo("Teste")
	Jogo.andar_atual = 18
	andar = load("res://cenas/mundo/andar.tscn").instantiate()
	add_child_autofree(andar)


func test_ha_dez_masmorras_com_boss_e_arma() -> void:
	var m: Dictionary = Dados.tabela("masmorras").masmorras
	assert_eq(m.size(), 10)
	for x in m.values():
		assert_ne(String(x.arma), "", x.nome_pt)
		assert_false(Dados.arma(x.arma).is_empty(), x.arma)
		assert_true(ResourceLoader.exists(Dados.tabela("masmorras").bosses[x.boss].sprite + "_parado_lado.png"), x.boss)


func test_entrar_e_sair() -> void:
	Masmorra.entrar(andar, 2, Vector3(1, 0, 1))
	assert_not_null(Masmorra.atual)
	assert_true(Jogo.dentro)
	var j: Node3D = andar.jogador
	assert_lt(j.global_position.y, -900.0)
	Masmorra.atual.sair()
	await get_tree().process_frame
	assert_false(Jogo.dentro)
	assert_gt(j.global_position.y, -10.0)


func test_puzzle_e_armadilhas_abrem_os_portoes() -> void:
	Masmorra.entrar(andar, 2, Vector3.ZERO)
	var m := Masmorra.atual
	m._abrir(0, false)
	assert_true(m._resolvida[0])
	assert_true((m._portoes[0].get_meta("colisao") as CollisionShape3D).disabled or true)


func test_vencer_o_boss_da_a_arma_secreta() -> void:
	Masmorra.entrar(andar, 2, Vector3.ZERO)
	var m := Masmorra.atual
	m._vitoria()
	assert_true(Jogo.tem_flag("masmorra_mina_do_rei_anao"))
	assert_true(Jogo.inventario.tem("machado_rei_montanha"))
	m.sair()


func test_boss_da_masmorra_tem_fases() -> void:
	var b := Boss.new().configurar("rei_anao_esquecido", 30, "boss")
	assert_eq(b.fases.size(), 2)
	b.free()


func test_todas_as_masmorras_montam_as_salas_especiais() -> void:
	for r in range(1, 11):
		Masmorra.entrar(andar, r, Vector3.ZERO)
		var m := Masmorra.atual
		var especiais := m.get_children().filter(func(x): return x is SalaMasmorra).size()
		var esperadas: int = Array(m.d.salas).filter(func(s): return not String(s.tipo) in ["combate", "ritmo", "puzzle", "armadilhas"]).size()
		assert_eq(especiais, esperadas, m.d.nome_pt)
		m.free()
		Masmorra.atual = null


func test_a_tua_estatua_abre_a_sala_dos_jogadores() -> void:
	Masmorra.entrar(andar, 10, Vector3.ZERO)
	var m := Masmorra.atual
	var sala: SalaMasmorra = m.get_children().filter(func(x): return x is SalaMasmorra and x.i == 1)[0]
	for it in m.get_children():
		if it is Interagivel and String(it.texto).ends_with("10 000"):
			it.usado.emit(andar.jogador)
	assert_true(m._resolvida[1])
	assert_true(sala._feita)
	m.sair()


func test_estatuas_congeladas_acordam_perto() -> void:
	Masmorra.entrar(andar, 5, Vector3.ZERO)
	var m := Masmorra.atual
	var sala: SalaMasmorra = m.get_children().filter(func(x): return x is SalaMasmorra and x.mec.tipo == "despertar")[0]
	assert_eq(sala._dormentes.size(), 12)
	var mo: Monstro = sala._dormentes[0]
	andar.jogador.global_position = m.global_position + mo.position
	sala._despertar_process(0.1, sala.local_jogador())
	assert_eq(mo.process_mode, Node.PROCESS_MODE_INHERIT)
	m.sair()
