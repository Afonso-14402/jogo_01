extends GutTest
## Caminho garantido (scripts/mundo/caminhos.gd): em todos os andares chega-se a pé à Zona Segura, ao guardião,
## ao boss e à escada (o 67 abre-se com o puzzle das estátuas-guindaste).


func test_todos_os_andares_tem_caminho() -> void:
	for n in range(1, 101):
		if n in Andar.CAMINHO_POR_PUZZLE:
			continue
		var g: Array = Caminhos.garantir(Dados.tabela("andares/a%03d" % n).get("grelha", []))
		var inicio := Vector2i(-1, -1)
		for y in g.size():
			for x in g[y].size():
				if g[y][x] in ["EE", "AA"] and inicio.x < 0:
					inicio = Vector2i(x, y)
		var cod := func(p: Vector2i) -> String:
			return g[p.y][p.x] if p.x >= 0 and p.y >= 0 and p.y < g.size() and p.x < g[0].size() else "TT"
		var vis := Caminhos._alcance(g, inicio, cod)
		for alvo in Caminhos.ALVOS:
			var existe := false
			var chega := false
			for y in g.size():
				for x in g[y].size():
					if g[y][x] == alvo:
						existe = true
						chega = chega or vis.has(Vector2i(x, y))
			assert_true(not existe or chega, "andar %d: não se chega a %s" % [n, alvo])


func test_so_abre_o_que_falta() -> void:
	var g := [["TT", "TT", "TT", "TT", "TT"],
			["TT", "EE", "~~", "GG", "TT"],
			["TT", "..", "##", "..", "TT"],
			["TT", "TT", "TT", "TT", "TT"]]
	var abertos := []
	var r := Caminhos.garantir(g, abertos)
	assert_eq(abertos.size(), 1)
	assert_true(r[1][2] == "==" or r[2][2] == "::")
	assert_eq(g[1][2], "~~", "a grelha original não muda")
