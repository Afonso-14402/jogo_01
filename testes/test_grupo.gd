extends GutTest
## O grupo de companheiros (docs/SISTEMAS.md, secção 20): contratar, equipa, valores, itens, ordens e especiais.


func before_each() -> void:
	Jogo.novo_jogo("Teste")


func test_ha_26_companheiros_com_sprite_e_retrato() -> void:
	var t := Grupo.todos()
	assert_eq(t.size(), 26)
	for d in t:
		assert_true(ResourceLoader.exists(String(d.sprite) + "_parado_baixo.png"), d.id)
		assert_true(ResourceLoader.exists(String(d.retrato) + "normal.png"), d.id)
		assert_false(Dados.arma(String(d.arma) + "_cobre").is_empty(), d.id)


func test_contratar_paga_e_entra_na_equipa() -> void:
	Jogo.ouro = 100
	assert_true(Grupo.recrutar("duarte"))
	assert_eq(Jogo.ouro, 20)
	assert_true(Grupo.na_equipa("duarte"))
	assert_false(Grupo.recrutar("duarte"))   # já é teu


func test_sem_ouro_nao_contrata() -> void:
	Jogo.ouro = 10
	assert_false(Grupo.recrutar("leonor"))
	assert_false(Grupo.conhecido("leonor"))


func test_os_da_guilda_aparecem_conforme_o_andar() -> void:
	Jogo.ouro = 9999
	assert_false(Grupo.disponivel("ines"))
	Jogo.andar_maximo = 15
	assert_true(Grupo.disponivel("ines"))


func test_equipa_ate_3() -> void:
	Jogo.ouro = 9999
	for id in ["duarte", "leonor", "sancha", "vasco"]:
		Grupo.recrutar(id)
	assert_eq(Jogo.companheiros.size(), 3)
	assert_true(Grupo.conhecido("vasco"))
	assert_false(Grupo.na_equipa("vasco"))
	Grupo.sair("duarte")
	assert_true(Grupo.juntar("vasco"))


func test_escondido_pede_nivel() -> void:
	assert_false(Grupo.disponivel("bartolomeu"))
	Jogo.nivel = 3
	assert_true(Grupo.disponivel("bartolomeu"))


func test_nivel_e_valores() -> void:
	Jogo.nivel = 12
	assert_eq(Grupo.nivel("duarte"), 10)
	# arma própria do tier do nível 10 (cobre) e ×0,85 por ser da Guilda
	assert_eq(String(Grupo.arma("duarte").id), "espada_cobre")
	assert_gt(Grupo.hp_max("duarte"), 100.0)
	assert_gt(Grupo.hp_max("gorvan"), Grupo.hp_max("duarte"))   # os da Guilda têm ×0,85
	Jogo.nivel = 25
	assert_eq(String(Grupo.arma("duarte").id), "espada_aco")


func test_dar_e_tirar_arma() -> void:
	Jogo.ouro = 100
	Grupo.recrutar("duarte")
	Jogo.inventario.adicionar("espada_ferro", 1)
	var i := -1
	for k in Jogo.inventario.espacos.size():
		var e = Jogo.inventario.espacos[k]
		if e != null and e.id == "espada_ferro":
			i = k
	assert_true(Grupo.dar_arma("duarte", i))
	assert_eq(String(Grupo.arma("duarte").id), "espada_ferro")
	assert_eq(Jogo.inventario.contar("espada_ferro"), 0)
	Grupo.tirar_arma("duarte")
	assert_eq(Jogo.inventario.contar("espada_ferro"), 1)


func test_nao_da_arma_que_nao_sabe_usar() -> void:
	Jogo.ouro = 200
	Grupo.recrutar("leonor")
	Jogo.inventario.adicionar("espada_ferro", 1)
	for k in Jogo.inventario.espacos.size():
		var e = Jogo.inventario.espacos[k]
		if e != null and e.id == "espada_ferro":
			assert_false(Grupo.dar_arma("leonor", k))


func test_pocoes() -> void:
	Jogo.ouro = 200
	Grupo.recrutar("sancha")
	var antes := Jogo.inventario.contar("pocao_vida_p")
	assert_true(Grupo.dar_pocao("sancha"))
	assert_eq(Jogo.inventario.contar("pocao_vida_p"), antes - 1)
	assert_eq(Grupo.estado("sancha").pocoes.size(), 1)
	Grupo.tirar_pocoes("sancha")
	assert_eq(Jogo.inventario.contar("pocao_vida_p"), antes)


func test_ordens_rodam() -> void:
	Jogo.ouro = 200
	Grupo.recrutar("duarte")
	assert_eq(Grupo.ordem("duarte"), "atacar")
	Grupo.rodar_ordens()
	assert_eq(Grupo.ordem("duarte"), "defender")


func test_especial_mais_ouro() -> void:
	Jogo.nivel = 20
	Jogo.ouro = 0
	Jogo.ganhar_ouro(100, true)
	var sem := Jogo.ouro
	Jogo.ouro = 100
	Grupo.recrutar("pim")
	Jogo.ouro = 0
	Jogo.ganhar_ouro(100, true)
	assert_gt(Jogo.ouro, sem)


func test_gravar_e_carregar_o_grupo() -> void:
	Jogo.ouro = 500
	Grupo.recrutar("duarte")
	Grupo.recrutar("leonor")
	Grupo.mudar_ordem("leonor", "ficar")
	var g := Jogo.para_gravar()
	Jogo.novo_jogo("Outro")
	assert_true(Jogo.companheiros.is_empty())
	Jogo.carregar(JSON.parse_string(JSON.stringify(g)))
	assert_eq(Jogo.companheiros, ["duarte", "leonor"])
	assert_eq(Grupo.ordem("leonor"), "ficar")
