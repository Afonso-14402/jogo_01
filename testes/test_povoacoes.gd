extends GutTest
## Povoações dentro da torre (dados/povoacoes.json, docs/CIDADES.md secção 4).


func test_ha_povoacoes_em_todas_as_regioes() -> void:
	var regioes := {}
	for p in Dados.tabela("povoacoes").values():
		regioes[int(p.regiao)] = true
	assert_eq(regioes.size(), 10, "uma ou mais povoações em cada uma das 10 regiões")


func test_npcs_tem_sprite_e_falas() -> void:
	for n in Dados.tabela("npcs_povoacoes").values():
		assert_true(ResourceLoader.exists(n.sprite + "_parado_baixo.png"), "sprite de " + n.id)
		var d: Dictionary = Dados.tabela("dialogos/" + n.id)
		assert_false(d.get("primeira", []).is_empty(), "primeira conversa de " + n.id)


func test_lojas_vendem_itens_que_existem() -> void:
	for l in Dados.tabela("lojas_povoacoes").values():
		assert_false(Dados.obter("npcs_povoacoes", l.dono).is_empty(), "dono da " + l.id)
		for i in l.itens:
			assert_false(Inventario._dados(i.item).is_empty(), "%s vende %s" % [l.id, i.item])


func test_pecas_existem() -> void:
	for p in Dados.tabela("povoacoes").values():
		for c in p.edificios + p.decoracao:
			assert_true(ResourceLoader.exists(c), c)


func test_transeuntes_tem_frases() -> void:
	var t: Dictionary = Dados.tabela("transeuntes")
	assert_false(t.get("todos", []).is_empty())
	assert_false(t.get("ascendia", []).is_empty())
	for r in range(1, 11):
		assert_false(t.get("r%02d" % r, []).is_empty(), "frases da região %d" % r)
