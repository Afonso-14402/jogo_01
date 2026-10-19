extends GutTest
## Coleções: conquistas, títulos, páginas e peixes (docs/ATIVIDADES.md, secções 5–7).


func before_each() -> void:
	Jogo.novo_jogo("Teste")
	Tempo.hora = 9.0
	Tempo.dia = 1
	Tempo.estacao = 0


func test_primeiro_monstro_da_conquista() -> void:
	Eventos.monstro_morto.emit("slime_verde", 1)
	Colecoes.verificar()
	assert_eq(int(Jogo.contadores.monstros), 1)
	assert_eq(int(Jogo.bestiario.slime_verde), 1)
	assert_true(Jogo.conquistas.any(func(c): return Dados.obter("conquistas", c).nome_pt == "Primeiro monstro"))


func test_chegar_ao_andar_10() -> void:
	Jogo.andar_maximo = 10
	Colecoes.verificar()
	assert_true(Jogo.conquistas.any(func(c): return Dados.obter("conquistas", c).nome_pt == "Chegar ao andar 10"))


func test_titulo_do_boss() -> void:
	Jogo.por_flag("boss_javali_rei")
	Colecoes.verificar()
	assert_true(Jogo.titulos.any(func(t): return Dados.obter("titulos", t).nome_pt == "Caçador de Reis"))


func test_paginas() -> void:
	Colecoes.pagina(3)
	Colecoes.pagina(1)
	Colecoes.pagina(3)
	assert_eq(Jogo.paginas, [1, 3])
	assert_eq(Dados.lista_simples("paginas").size(), 100)
	assert_string_contains(Dados.lista_simples("paginas")[0].texto, "Acordei num prado")


func test_peixes_do_andar_e_hora() -> void:
	var ui := preload("res://scripts/ui/pesca_ui.gd").new()
	add_child_autofree(ui)
	ui._rng.seed = 1
	Dados.constantes.pesca_lixo = 0.0
	var vistos := {}
	for i in 60:
		vistos[ui.escolher_peixe(3, false)] = true
	assert_true(vistos.has("truta_ribeiro") or vistos.has("perca_prateada"))
	assert_false(vistos.has("carpa_dourada"), "a carpa dourada é do andar 9")
	Dados.constantes.pesca_lixo = 0.1


func test_conquistas_tem_regras() -> void:
	var com_regra := Dados.tabela("conquistas").values().filter(func(c): return c.regra != "")
	assert_gt(com_regra.size(), 40)
