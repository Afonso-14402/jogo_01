extends GutTest
## Por dentro dos edifícios (docs/CIDADES.md 1.6, dados/interiores.json).


func test_os_moveis_existem() -> void:
	for tipo in Dados.tabela("interiores").tipos:
		for m in Dados.tabela("interiores").tipos[tipo].moveis:
			var c: String = m[0] if String(m[0]).begins_with("res://") else "res://arte/moveis/%s.glb" % m[0]
			assert_true(ResourceLoader.exists(c), "%s: %s" % [tipo, c])


func test_texturas_de_chao_e_parede() -> void:
	for tipo in Dados.tabela("interiores").tipos:
		var d: Dictionary = Dados.tabela("interiores").tipos[tipo]
		assert_true(ResourceLoader.exists("res://arte/interiores/chao_%s.png" % d.chao), tipo)
		assert_true(ResourceLoader.exists("res://arte/interiores/parede_%s.png" % d.parede), tipo)


func test_entrar_e_sair() -> void:
	var mundo := Node3D.new()
	add_child_autofree(mundo)
	Interior.entrar(mundo, "taberna", 0, "Taberna", Vector3(1, 0, 2))
	assert_true(Jogo.dentro)
	assert_not_null(Interior.atual)
	Interior.atual.sair()
	assert_false(Jogo.dentro)
	assert_null(Interior.atual)
