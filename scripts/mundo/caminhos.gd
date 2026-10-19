class_name Caminhos
extends RefCounted
## Caminho garantido (docs/mapas/README.md): se a Zona Segura, o guardião, o boss ou a escada não se alcançam a pé a
## partir da chegada, abre-se o caminho mais curto até lá — um passadiço (==) por cima da água, da lava ou do vazio,
## ou um trilho (::) pela rocha. Enquanto não há barco nem nadar, é isto que deixa acabar todos os andares.

const PAREDES := ["TT", "##", "~~", "ww", "  "]
const ALVOS := ["SS", "GG", "BB", ">>"]
const LADOS := [Vector2i(1, 0), Vector2i(-1, 0), Vector2i(0, 1), Vector2i(0, -1)]


## Muda a grelha (cópia) e devolve-a; abertos recebe as células trocadas (para o robô e os testes).
static func garantir(grelha: Array, abertos: Array = []) -> Array:
	var g: Array = grelha.duplicate(true)
	var alt := g.size()
	if alt == 0:
		return g
	var lar: int = g[0].size()
	var cod := func(p: Vector2i) -> String:
		return g[p.y][p.x] if p.x >= 0 and p.y >= 0 and p.x < lar and p.y < alt else "TT"
	var inicio := Vector2i(-1, -1)
	for y in alt:
		for x in lar:
			if g[y][x] in ["EE", "AA"] and inicio.x < 0:
				inicio = Vector2i(x, y)
	if inicio.x < 0:
		return g
	for alvo in ALVOS:
		var vis := _alcance(g, inicio, cod)
		var existe := false
		var chega := false
		for y in alt:
			for x in lar:
				if g[y][x] == alvo:
					existe = true
					chega = chega or vis.has(Vector2i(x, y))
		if not existe or chega:
			continue
		# 0-1 BFS: andar no chão custa 0, atravessar uma parede custa 1 (a borda do mapa quase nunca)
		var dist := {}
		var veio := {}
		var fila: Array = []
		for p in vis:
			dist[p] = 0
			fila.append(p)
		var fim := Vector2i(-1, -1)
		while not fila.is_empty():
			var p: Vector2i = fila.pop_front()
			if cod.call(p) == alvo:
				fim = p
				break
			for d in LADOS:
				var q: Vector2i = p + d
				if q.x < 0 or q.y < 0 or q.x >= lar or q.y >= alt:
					continue
				var c: String = cod.call(q)
				var borda := q.x == 0 or q.y == 0 or q.x == lar - 1 or q.y == alt - 1
				var custo := 0 if not c in PAREDES else (50 if borda and c != alvo else 1)
				if c == alvo:
					custo = 0
				var nd: int = dist[p] + custo
				if nd < int(dist.get(q, 1 << 30)):
					dist[q] = nd
					veio[q] = p
					if custo == 0:
						fila.push_front(q)
					else:
						fila.push_back(q)
		var p := fim
		while p.x >= 0 and veio.has(p):
			var c: String = cod.call(p)
			if c in PAREDES:
				g[p.y][p.x] = "==" if c in ["~~", "ww", "  "] else "::"
				abertos.append(p)
			p = veio[p]
	return g


static func _alcance(g: Array, inicio: Vector2i, cod: Callable) -> Dictionary:
	var vis := {inicio: true}
	var fila: Array = [inicio]
	while not fila.is_empty():
		var p: Vector2i = fila.pop_back()
		for d in LADOS:
			var q: Vector2i = p + d
			if not vis.has(q) and not cod.call(q) in PAREDES:
				vis[q] = true
				fila.append(q)
	return vis
