extends GutTest
## Estado do jogador: subir de nível, pontos, estamina, gravar e carregar.


func before_each() -> void:
	Jogo.novo_jogo("Teste")


func test_subir_de_nivel_da_pontos_e_enche_hp() -> void:
	Jogo.hp = 10
	Jogo.ganhar_xp(100)
	assert_eq(Jogo.nivel, 2)
	assert_eq(Jogo.xp, 0)
	assert_eq(Jogo.pontos_livres, 5)
	assert_eq(int(Jogo.hp), Jogo.hp_maximo())


func test_xp_a_mais_sobe_varios_niveis() -> void:
	Jogo.ganhar_xp(100 + 202 + 50)
	assert_eq(Jogo.nivel, 3)
	assert_eq(Jogo.xp, 50)


func test_gastar_pontos() -> void:
	Jogo.ganhar_xp(100)
	assert_true(Jogo.gastar_ponto("vit"))
	assert_eq(Jogo.a("vit"), 6)
	assert_eq(Jogo.pontos_livres, 4)


func test_esquiva_precisa_de_estamina() -> void:
	Jogo.estamina = 20
	assert_false(Jogo.gastar_estamina(25))
	Jogo.estamina = 30
	assert_true(Jogo.gastar_estamina(25))
	assert_almost_eq(Jogo.estamina, 5.0, 0.001)


func test_gravar_e_carregar() -> void:
	Jogo.ganhar_xp(150)
	Jogo.ganhar_ouro(77)
	Jogo.por_flag("prologo_feito")
	assert_true(Gravar.gravar(9))
	Jogo.novo_jogo("Outro")
	assert_true(Gravar.carregar(9))
	assert_eq(Jogo.nome, "Teste")
	assert_eq(Jogo.nivel, 2)
	assert_eq(Jogo.ouro, 77)
	assert_true(Jogo.tem_flag("prologo_feito"))
	DirAccess.remove_absolute(ProjectSettings.globalize_path(Gravar.caminho(9)))
