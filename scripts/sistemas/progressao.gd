class_name Progressao
extends RefCounted
## Skills que sobem com o uso, classes e rank (docs/PROGRESSAO.md; números em dados/constantes.json).


## Nível de uma skill de arma (1–10). Passar do nível N para N+1 custa 50 × N² pontos.
## Devolve [nível, pontos dentro do nível, pontos precisos para o seguinte].
static func nivel_arma(c: Dictionary, pontos: float) -> Array:
	var n := 1
	var resto := pontos
	while n < int(c.skill_arma_max):
		var custo := float(c.skill_arma_base) * n * n
		if resto < custo:
			return [n, resto, custo]
		resto -= custo
		n += 1
	return [n, 0.0, 0.0]


## Nível de uma skill de vida (1–50). Passar do nível N para N+1 custa 20 × N^1,8 ações.
static func nivel_vida(c: Dictionary, acoes: float) -> Array:
	var n := 1
	var resto := acoes
	while n < int(c.skill_vida_max):
		var custo := roundf(float(c.skill_vida_base) * pow(n, float(c.skill_vida_expoente)))
		if resto < custo:
			return [n, resto, custo]
		resto -= custo
		n += 1
	return [n, 0.0, 0.0]


## Rank de aventureiro pelos pontos de Guilda (o SSS também precisa do andar 100).
static func rank(c: Dictionary, pontos: int, andar_maximo: int = 1) -> String:
	var r := "F"
	for l in c.ranks:
		if pontos >= int(l[1]) and (l[0] != "SSS" or andar_maximo >= 100):
			r = l[0]
	return r


## As skills de arma especiais (níveis 3, 6 e 10) já aprendidas para um tipo de arma.
static func especiais_arma(tipo: String, nivel: int) -> Array:
	var r := []
	for s in Dados.tabela("skills_armas").values():
		if s.arma == tipo and int(s.nivel) <= nivel:
			r.append(s)
	return r


## A linha de classes até à atual (ex.: cavaleiro -> [espadachim, cavaleiro]).
static func linha_classes(classe: String) -> Array:
	var r := []
	var atual := classe
	while atual != "":
		var d := Dados.obter("classes", atual)
		if d.is_empty():
			break
		r.push_front(d)
		atual = d.get("anterior") if d.get("anterior") else ""
	return r


## Skills de classe já desbloqueadas pelo nível.
static func skills_classe(classe: String, nivel: int) -> Array:
	var r := []
	for c in linha_classes(classe):
		for s in c.skills:
			if int(s.nivel) <= nivel:
				r.append(s)
	return r
