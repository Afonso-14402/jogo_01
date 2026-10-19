extends GutTest
## As cenas da história (scripts/autoload/historia.gd; dados/cenas.json, de docs/guiao/).


func before_each() -> void:
	Jogo.novo_jogo("Teste")
	Historia._fila.clear()
	Historia._zonas.clear()


func test_ha_cenas_de_todos_os_capitulos() -> void:
	var caps := {}
	for c in Historia.cenas().values():
		caps[int(c.capitulo)] = true
	for k in range(1, 11):
		assert_true(caps.has(k), "capítulo %d" % k)


func test_entrar_no_andar_11_poe_a_cena_da_mina() -> void:
	Jogo.andar_maximo = 11
	Historia._andar(11)
	await wait_seconds(2.0)
	assert_true("cena_c2_01_mina" in Historia._fila)
	assert_true(Historia.vista("cena_c2_01_mina"))


func test_vencer_a_aranha_mae() -> void:
	Historia._vencer("aranha_mae")
	await wait_seconds(3.0)
	assert_true("cena_c2_04_aranha_depois" in Historia._fila)


func test_h06_avanca_e_o_fausto_fecha_e_abre_a_h07() -> void:
	Jogo.andar_maximo = 18
	Historia.progressao()
	assert_eq(Missoes.estado("H_06"), "ativa")
	Historia.efeito({"missao_passo": "H_06"})
	Historia.efeito({"missao_passo": "H_06"})
	assert_eq(Historia.cena_npc("fausto"), "cena_c2_07b_fausto")
	Historia.efeito({"missao_concluir": "H_06", "missao_aceitar": "H_07"})
	assert_eq(Missoes.estado("H_06"), "concluida")
	assert_eq(Missoes.estado("H_07"), "ativa")
	assert_eq(Historia.cena_npc("fausto"), "")


func test_capitulo_1_abre_h04_e_depois_h05() -> void:
	Jogo.andar_maximo = 3
	Historia.progressao()
	assert_eq(Missoes.estado("H_04"), "ativa")
	assert_eq(Missoes.estado("H_05"), "inativa")
	Historia.efeito({"missao_concluir": "H_04"})
	Historia.progressao()
	assert_eq(Missoes.estado("H_05"), "ativa")


func test_portao_anao_toca_a_forja() -> void:
	Historia.acontecer("Grande Portão Anão")
	await wait_seconds(1.0)
	assert_true("cena_c2_07_forja" in Historia._fila)
