extends GutTest
## Fórmulas de docs/SISTEMAS.md: os valores das tabelas do documento têm de sair iguais.

var c: Dictionary


func before_all() -> void:
	c = Dados.ler_json("res://dados/constantes.json")


func test_xp_para_subir_igual_a_tabela() -> void:
	var tabela := {1: 100, 2: 202, 5: 707, 10: 2041, 20: 6084, 50: 26191, 99: 78031}
	for nivel in tabela:
		assert_eq(Formulas.xp_para_subir(c, nivel), tabela[nivel], "nível %d" % nivel)


func test_xp_de_monstro_igual_a_tabela() -> void:
	var tabela := {1: 11, 2: 15, 5: 32, 10: 68, 20: 155, 50: 493}
	for nivel in tabela:
		assert_eq(Formulas.xp_monstro(c, nivel), tabela[nivel], "nível %d" % nivel)


func test_monstro_mais_baixo_da_so_20_por_cento() -> void:
	var cheia := Formulas.xp_recebida(c, 10, 10)
	var baixa := Formulas.xp_recebida(c, 15, 10)
	assert_eq(cheia, 68)
	assert_eq(baixa, int(68 * 0.2))


func test_valores_dos_monstros_por_nivel() -> void:
	var hp := {1: 47, 10: 280, 20: 605, 30: 1000, 50: 2000, 70: 3280, 100: 5725}
	for nivel in hp:
		assert_eq(Formulas.monstro_hp(c, nivel), hp[nivel], "HP nível %d" % nivel)
	assert_almost_eq(Formulas.monstro_atq(c, 10), 29.0, 0.01)
	assert_almost_eq(Formulas.monstro_atq(c, 100), 326.0, 0.01)
	assert_eq(Formulas.monstro_hp(c, 10, c.tipos_monstro.boss.hp), 280 * 24)


func test_jogador_derivados() -> void:
	assert_eq(Formulas.hp_maximo(c, 5, 1), 168)
	assert_eq(Formulas.mp_maximo(c, 5, 1), 62)
	assert_eq(Formulas.estamina_maxima(c, 5), 105)
	assert_eq(Formulas.estamina_maxima(c, 300), 250, "estamina tem máximo de 250")
	assert_almost_eq(Formulas.velocidade(c, 5), 4.545, 0.001)
	assert_almost_eq(Formulas.velocidade(c, 300), 6.5, 0.001, "velocidade máxima 6,5")
	assert_almost_eq(Formulas.critico(c, 5, 5), 0.0625, 0.0001)
	assert_almost_eq(Formulas.critico(c, 300, 300, 0.5), 0.75, 0.0001, "crítico máximo 75%")


func test_dano() -> void:
	assert_eq(Formulas.dano(100.0, 1.0, 0.0, 1.0, 1.0, 1.0), 100)
	assert_eq(Formulas.dano(100.0, 1.0, 100.0, 1.0, 1.0, 1.0), 50, "DEF 100 corta para metade")
	assert_eq(Formulas.dano(100.0, 1.4, 0.0, 1.5, 1.5, 1.0), 315, "3.º golpe + fraqueza + crítico")
	assert_eq(Formulas.dano(1.0, 1.0, 500.0, 0.5, 1.0, 0.95), 1, "o dano mínimo é 1")
	assert_eq(Formulas.dano(100.0, 1.0, 0.0, 0.0, 1.0, 1.0), 0, "imune = 0")


func test_elementos() -> void:
	assert_eq(Formulas.mult_elemento(c, "fogo", ["fogo"], [], []), 1.5)
	assert_eq(Formulas.mult_elemento(c, "gelo", [], ["gelo"], []), 0.5)
	assert_eq(Formulas.mult_elemento(c, "luz", [], [], ["luz"]), 0.0)
	assert_eq(Formulas.mult_elemento(c, "fisico", ["fogo"], [], []), 1.0)


func test_atq_fisico_usa_for_ou_des() -> void:
	assert_almost_eq(Formulas.atq_fisico(c, 12.0, 0, 1.0, 10, 4, false), 27.0, 0.001)
	assert_almost_eq(Formulas.atq_fisico(c, 12.0, 0, 1.0, 10, 4, true), 18.0, 0.001)
	assert_almost_eq(Formulas.atq_fisico(c, 12.0, 10, 1.0, 0, 0, false), 18.0, 0.001, "+10 dá +50%")
