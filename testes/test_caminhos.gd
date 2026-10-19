extends GutTest
## Caminho garantido (scripts/mundo/caminhos.gd): em todos os andares chega-se (a pé ou a nadar) à Zona Segura, ao guardião,
## ao boss e à escada (o 67 abre-se com o puzzle das estátuas-guindaste).


func test_todos_os_andares_tem_caminho() -> void:
	for n in range(1, 101):
		if n in Andar.CAMINHO_POR_PUZZLE:
			continue
		var d := Dados.tabela("andares/a%03d" % n)
		var nada := int(d.get("regiao", 1)) != 7   # como no andar.gd: fora do vulcão a água funda nada-se
		var g: Array = Caminhos.garantir(d.get("grelha", []), [], nada)
		var paredes: Array = Caminhos.PAREDES.filter(func(c): return not (nada and c in ["~~", "ww"]))
		var inicio := Vector2i(-1, -1)
		for y in g.size():
			for x in g[y].size():
				if g[y][x] in ["EE", "AA"] and inicio.x < 0:
					inicio = Vector2i(x, y)
		var cod := func(p: Vector2i) -> String:
			return g[p.y][p.x] if p.x >= 0 and p.y >= 0 and p.y < g.size() and p.x < g[0].size() else "TT"
		var vis := Caminhos._alcance(g, inicio, cod, paredes)
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
