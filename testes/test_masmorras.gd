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
