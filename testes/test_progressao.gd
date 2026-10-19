extends GutTest
## Sistema isekai: skills que sobem com o uso, classes, origem, Skill Única e rank (docs/PROGRESSAO.md).


func before_each() -> void:
	Jogo.novo_jogo("Teste")


func test_niveis_da_skill_de_arma() -> void:
	var c := Dados.constantes
	assert_eq(Progressao.nivel_arma(c, 0)[0], 1)
	assert_eq(Progressao.nivel_arma(c, 49)[0], 1)
	assert_eq(Progressao.nivel_arma(c, 50)[0], 2)
	assert_eq(Progressao.nivel_arma(c, 250)[0], 3)
	assert_eq(Progressao.nivel_arma(c, 14249)[0], 9)
	assert_eq(Progressao.nivel_arma(c, 14250)[0], 10, "nível 10 ≈ 14 000 golpes")
	assert_eq(Progressao.nivel_arma(c, 999999)[0], 10)


func test_niveis_da_skill_de_vida() -> void:
	var c := Dados.constantes
	assert_eq(Progressao.nivel_vida(c, 19)[0], 1)
	assert_eq(Progressao.nivel_vida(c, 20)[0], 2)


func test_treinar_arma_ensina_especial_no_nivel_3() -> void:
	Jogo.treinar_arma("espada", 250)
	assert_eq(Jogo.nivel_arma("espada"), 3)
	assert_true("corte_duplo" in Jogo.skills_barra)
	assert_almost_eq(Jogo.mult_arma("espada"), 1.06, 0.001)


func test_aprendiz_rapido() -> void:
	Jogo.skill_unica = "aprendiz_rapido"
	Jogo.treinar_arma("arco", 100)
	assert_eq(float(Jogo.skills_arma.arco), 150.0)


func test_origem_dormir_da_estamina() -> void:
	var antes := Jogo.estamina_maxima()
	Jogo.origem = "dormir"
	assert_eq(Jogo.estamina_maxima(), int(antes * 1.1))


func test_classe_precisa_de_nivel_e_ordem() -> void:
	assert_false(Jogo.escolher_classe("espadachim"), "só no nível 10")
	Jogo.nivel = 10
	assert_false(Jogo.escolher_classe("cavaleiro"), "primeiro a classe base")
	assert_true(Jogo.escolher_classe("espadachim"))
	assert_true("corte_rapido" in Jogo.skills_barra)
	assert_almost_eq(Jogo.mult_arma("espada"), 1.0 + 0.02 + 0.10, 0.001)
	assert_almost_eq(Jogo.mult_arma("arco"), 1.02, 0.001)


func test_passivas_da_classe() -> void:
	Jogo.nivel = 45
	Jogo.escolher_classe("espadachim")
	Jogo.classe = "cavaleiro"
	var hp_sem := Formulas.hp_maximo(Dados.constantes, Jogo.a("vit"), 45, 0)
	assert_eq(Jogo.hp_maximo(), int(hp_sem * 1.10), "Armadura de Honra: +10% HP")


func test_rank() -> void:
	var c := Dados.constantes
	assert_eq(Progressao.rank(c, 0), "F")
	assert_eq(Progressao.rank(c, 450), "D")
	assert_eq(Progressao.rank(c, 70000, 50), "SS", "SSS precisa do andar 100")
	assert_eq(Progressao.rank(c, 70000, 100), "SSS")


func test_mao_de_midas() -> void:
	Jogo.skill_unica = "mao_de_midas"
	Jogo.ganhar_ouro(100, true)
	assert_eq(Jogo.ouro, int(150 * (1.0 + 5 * 0.005)))
