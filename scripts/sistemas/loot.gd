class_name Loot
extends RefCounted
## Drops e baús (docs/SISTEMAS.md, secção 9). Tudo recebe o RandomNumberGenerator para os testes serem certos.


## Rola a tabela de drops de um monstro: [{item, hipotese, qtd: [min, max]}] -> [[id, qtd]]
static func drops(c: Dictionary, tabela: Array, sor: int, elite: bool, rng: RandomNumberGenerator, sorte_heroi: bool = false) -> Array:
	var r := []
	var mult := (1.0 + sor * float(c.drop_por_sor)) * (float(c.drop_elite) if elite else 1.0) * (float(c.drop_sorte_heroi) if sorte_heroi else 1.0)
	for linha in tabela:
		if rng.randf() < float(linha.get("hipotese", 0.0)) * mult:
			var q: Array = linha.get("qtd", [1, 1])
			r.append([linha.item, rng.randi_range(int(q[0]), int(q[1]))])
	return r


## Raridade de uma arma/armadura. A Sorte passa 1% de Comum para cima a cada 50 SOR; o Mítico só a partir do andar 91.
## minimo: raridade mínima (ex.: "incomum" nos baús de prata).
static func raridade(c: Dictionary, sor: int, andar: int, rng: RandomNumberGenerator, minimo: String = "comum") -> String:
	var tabela: Array = c.raridades
	var chances: Array[float] = []
	for l in tabela:
		chances.append(float(l[1]))
	var passar: float = min(chances[0] - 0.05, float(sor / int(c.raridade_sor_por_ponto)) * 0.01)
	chances[0] -= passar
	var resto := 0.0
	for i in range(1, chances.size()):
		resto += chances[i]
	for i in range(1, chances.size()):
		chances[i] += passar * chances[i] / resto
	if andar < int(c.mitico_andar_minimo):
		chances[chances.size() - 1] = 0.0
	var inicio := 0
	for i in tabela.size():
		if tabela[i][0] == minimo:
			inicio = i
	var total := 0.0
	for i in range(inicio, chances.size()):
		total += chances[i]
	var x := rng.randf() * total
	for i in range(inicio, chances.size()):
		x -= chances[i]
		if x <= 0.0:
			return tabela[i][0]
	return tabela[inicio][0]


static func mult_raridade(c: Dictionary, nome: String) -> float:
	for l in c.raridades:
		if l[0] == nome:
			return float(l[2])
	return 1.0


## Conteúdo de um baú: {"itens": [[id, qtd, extra]], "ouro": n}
static func bau(c: Dictionary, tipo: String, andar: int, regiao: int, sor: int, rng: RandomNumberGenerator, azar: int = 0) -> Dictionary:
	var materiais := _da_regiao(regiao, "material")
	var consumiveis := _da_regiao(regiao, "consumivel")
	var armas := _armas_tier(regiao)
	var r := {"itens": [], "ouro": 0}
	match tipo:
		"madeira":
			for i in rng.randi_range(2, 4):
				if not materiais.is_empty():
					r.itens.append([materiais[rng.randi() % materiais.size()], rng.randi_range(1, 3), {}])
			r.ouro = rng.randi_range(5 * andar, 12 * andar)
			if rng.randf() < 0.3 and not consumiveis.is_empty():
				r.itens.append([consumiveis[rng.randi() % consumiveis.size()], 1, {}])
		"prata", "ouro":
			var minimo := "incomum" if tipo == "prata" else "raro"
			if azar >= int(c.azar_baus) - 1:
				minimo = "epico"
			if not armas.is_empty():
				r.itens.append([armas[rng.randi() % armas.size()], 1, {"raridade": raridade(c, sor, andar, rng, minimo)}])
			for i in rng.randi_range(1, 3):
				if not materiais.is_empty():
					r.itens.append([materiais[rng.randi() % materiais.size()], rng.randi_range(2, 4), {}])
			r.ouro = rng.randi_range(20 * andar, 40 * andar) * (3 if tipo == "ouro" else 1)
	return r


static func _da_regiao(regiao: int, categoria: String) -> Array:
	var r := []
	for id in Dados.tabela("itens"):
		var it: Dictionary = Dados.tabela("itens")[id]
		if int(it.get("regiao", 0)) == regiao and it.get("categoria", "") == categoria:
			r.append(id)
	return r


static func _armas_tier(tier: int) -> Array:
	var r := []
	for id in Dados.tabela("armas"):
		var a: Dictionary = Dados.tabela("armas")[id]
		if int(a.get("tier", 0)) == tier and a.get("categoria", "") == "normal":
			r.append(id)
	return r
