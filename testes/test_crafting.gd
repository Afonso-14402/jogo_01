extends GutTest
## Crafting, qualidade, melhorias, armaduras e recolha (docs/SISTEMAS.md, secções 11 e 12).


func before_each() -> void:
	Jogo.novo_jogo("Teste")


func _rng(s: int = 3) -> RandomNumberGenerator:
	var r := RandomNumberGenerator.new()
	r.seed = s
	return r


func test_fazer_lingote() -> void:
	Jogo.inventario.adicionar("minerio_cobre", 3)
	Jogo.inventario.adicionar("carvalho", 1)
	Jogo.ouro = 10
	var r := Jogo.fazer("lingote_cobre", _rng())
	assert_true(r.ok)
	assert_eq(Jogo.inventario.contar("lingote_cobre"), 1)
	assert_eq(Jogo.inventario.contar("minerio_cobre"), 0)
	assert_eq(Jogo.ouro, 5)
	assert_gt(float(Jogo.skills_vida.get("ferraria", 0)), 0.0)


func test_faltam_ingredientes() -> void:
	assert_false(Jogo.fazer("lingote_cobre", _rng()).ok)


func test_qualidade_com_skill_e_mestre() -> void:
	var c := Dados.constantes
	var r := _rng(9)
	var boas := 0
	for i in 2000:
		if Crafting.qualidade(c, 50, r, false) != "normal":
			boas += 1
	# 50 de skill: Boa 50% + Excelente 17% ≈ 67%
	assert_between(boas, 1200, 1500)


func test_custo_melhoria() -> void:
	var c := Dados.constantes
	var m := Crafting.custo_melhoria(c, "espada_cobre", 0)
	assert_eq(m.itens, [["lingote_cobre", 1]])
	assert_eq(m.sucesso, 1.0)
	var m9 := Crafting.custo_melhoria(c, "espada_ferro", 8)
	assert_eq(m9.itens[0], ["lingote_ferro", 9])
	assert_eq(m9.itens.size(), 3, "lingotes + cristais + gema")
	assert_almost_eq(float(m9.sucesso), 0.45 + 0.002, 0.0001)
	assert_almost_eq(float(Crafting.custo_melhoria(c, "espada_ferro", 8, 2).sucesso), 0.552, 0.0001, "+5% por falhanço")


func test_melhorar_ate_5_nunca_falha() -> void:
	Jogo.inventario.adicionar("lingote_cobre", 15)
	Jogo.ouro = 10000
	var e := Jogo.arma_extra
	e["id"] = Jogo.arma_equipada
	for i in 5:
		assert_true(Jogo.melhorar(e, _rng(i)).sucesso)
	assert_eq(int(Jogo.arma_extra.melhoria), 5)
	assert_almost_eq(Jogo.mult_arma_equipada(), 1.25, 0.001)


func test_falhar_nao_desce() -> void:
	var e := {"id": "espada_cobre", "melhoria": 9, "falhas": 0}
	Jogo.inventario.adicionar("lingote_cobre", 10)
	Jogo.inventario.adicionar("seiva_cristalizada", 3)
	Jogo.inventario.adicionar("rubi_pequeno", 1)
	Jogo.ouro = 10000
	var r := RandomNumberGenerator.new()
	var res := {}
	for s in 50:   # procura uma semente que falhe (30% de sucesso)
		r.seed = s
		if r.randf() >= 0.302:
			r.seed = s
			res = Jogo.melhorar(e, r)
			break
	assert_false(res.sucesso)
	assert_eq(int(e.melhoria), 9)
	assert_eq(int(e.falhas), 1)


func test_armadura_da_def() -> void:
	var antes := Jogo.defesa()
	Jogo.inventario.adicionar("couro_javali_corpo")
	var i := -1
	for k in Jogo.inventario.tamanho():
		if Jogo.inventario.espacos[k] != null and Jogo.inventario.espacos[k].id == "couro_javali_corpo":
			i = k
	assert_true(Jogo.equipar_do_espaco(i))
	assert_almost_eq(Jogo.defesa(), antes + 4.0, 0.01)
	assert_true(Jogo.desequipar("corpo"))
	assert_almost_eq(Jogo.defesa(), antes, 0.01)


func test_descobrir_receita() -> void:
	Jogo.receitas.erase("pocao_estamina")
	Jogo.apanhar("flor_de_mel")
	assert_false(Jogo.conhece("pocao_estamina"))
	Jogo.apanhar("agua_limpa")
	assert_true(Jogo.conhece("pocao_estamina"))


func test_tier_ferramenta() -> void:
	assert_eq(Jogo.tier_ferramenta("picareta"), 0)
	Jogo.inventario.adicionar("picareta_ferro")
	assert_eq(Jogo.tier_ferramenta("picareta"), 2)
