extends GutTest
## Mochila, drops e baús (docs/SISTEMAS.md, secções 9 e 13).


func _rng(semente: int = 7) -> RandomNumberGenerator:
	var r := RandomNumberGenerator.new()
	r.seed = semente
	return r


func test_empilha_ate_ao_maximo() -> void:
	var inv := Inventario.new(3)
	assert_eq(inv.adicionar("gel_slime", 150), 0)
	assert_eq(inv.contar("gel_slime"), 150)
	assert_eq(inv.livres(), 1)


func test_mochila_cheia_devolve_o_que_sobra() -> void:
	var inv := Inventario.new(1)
	assert_eq(inv.adicionar("gel_slime", 120), 21)


func test_armas_nao_empilham_e_tem_instancia() -> void:
	var inv := Inventario.new(5)
	inv.adicionar("espada_cobre", 2, {"raridade": "raro"})
	assert_eq(inv.livres(), 3)
	assert_eq(inv.espacos[0].raridade, "raro")
	assert_ne(inv.espacos[0].inst, inv.espacos[1].inst)


func test_retirar_e_itens_de_missao() -> void:
	var inv := Inventario.new(5)
	inv.adicionar("gel_slime", 10)
	assert_eq(inv.retirar("gel_slime", 4), 4)
	assert_eq(inv.contar("gel_slime"), 6)
	inv.adicionar("chave_bau_ouro", 1)
	assert_true(inv.tem("chave_bau_ouro"))
	assert_eq(inv.livres(), 4, "itens de missão não ocupam espaço")


func test_gravar_e_carregar_mochila() -> void:
	var inv := Inventario.new(5)
	inv.adicionar("gel_slime", 3)
	inv.barra_rapida[0] = "pocao_vida_p"
	var b := Inventario.new(5)
	b.carregar(JSON.parse_string(JSON.stringify(inv.para_gravar())))
	assert_eq(b.contar("gel_slime"), 3)
	assert_eq(b.barra_rapida[0], "pocao_vida_p")


func test_pocao_cura_e_gasta() -> void:
	Jogo.novo_jogo("Teste")
	Jogo.hp = 1
	assert_true(Jogo.usar_consumivel("pocao_vida_p"))
	assert_gt(Jogo.hp, 1.0)
	assert_eq(Jogo.inventario.contar("pocao_vida_p"), 2)


func test_equipar_arma_da_mochila() -> void:
	Jogo.novo_jogo("Teste")
	Jogo.inventario.adicionar("espada_ferro")
	var i := Jogo.inventario.espacos.find(Jogo.inventario.espacos.filter(func(e): return e and e.id == "espada_ferro")[0])
	assert_true(Jogo.equipar_do_espaco(i))
	assert_eq(Jogo.arma_equipada, "espada_ferro")
	assert_true(Jogo.inventario.tem("espada_cobre"))


func test_drops_com_semente_sao_iguais() -> void:
	var c: Dictionary = Dados.constantes
	var tabela: Array = Dados.monstro("slime_verde").drops
	assert_eq(Loot.drops(c, tabela, 5, false, _rng()), Loot.drops(c, tabela, 5, false, _rng()))


func test_mitico_so_no_andar_91() -> void:
	var c: Dictionary = Dados.constantes
	var r := _rng(3)
	var viu := false
	for i in 500:
		viu = viu or Loot.raridade(c, 500, 50, r) == "mitico"
	assert_false(viu)


func test_bau_de_prata_pelo_menos_incomum() -> void:
	var c: Dictionary = Dados.constantes
	var r := _rng(11)
	for i in 50:
		var b := Loot.bau(c, "prata", 5, 1, 5, r)
		for it in b.itens:
			if it[2].has("raridade"):
				assert_ne(it[2].raridade, "comum")
