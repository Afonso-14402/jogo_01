class_name Crafting
extends RefCounted
## Crafting, qualidade, melhorias +1…+10 e reciclar (docs/SISTEMAS.md, secção 11). Tudo recebe o RNG para os testes.

const METAIS := ["cobre", "ferro", "aco", "prata", "gelo_eterno", "coral_abissal", "obsidiana", "mitril", "oricalco", "estelar"]


static func receita(id: String) -> Dictionary:
	return Dados.obter("receitas", id)


## Receitas de uma estação (forja, alquimia, fogao, fogueira, tear...). A fogueira também serve para o fogão? Não: só 🔥.
static func da_estacao(estacao: String) -> Array:
	var r := []
	for x in Dados.tabela("receitas").values():
		if x.estacao == estacao or (estacao == "fogao" and x.estacao == "fogueira"):
			r.append(x)
	return r


## Falta algum ingrediente? Devolve [[id, tenho, preciso]] de todos.
static func ingredientes(inv: Inventario, r: Dictionary) -> Array:
	var out := []
	for i in r.ingredientes:
		out.append([i[0], inv.contar(i[0]), int(i[1])])
	return out


static func pode_fazer(inv: Inventario, ouro: int, r: Dictionary) -> bool:
	if ouro < int(r.get("ouro", 0)):
		return false
	for i in ingredientes(inv, r):
		if i[1] < i[2]:
			return false
	return true


## Qualidade (11.2): Boa = 10% + skill × 0,8% · Excelente = 2% + skill × 0,3% (Mestre Artesão ×2).
static func qualidade(c: Dictionary, nivel_skill: int, rng: RandomNumberGenerator, mestre: bool = false) -> String:
	var m := 2.0 if mestre else 1.0
	var exc := (float(c.qualidade_excelente_base) + nivel_skill * float(c.qualidade_excelente_por_skill)) * m
	var boa := (float(c.qualidade_boa_base) + nivel_skill * float(c.qualidade_boa_por_skill)) * m
	var x := rng.randf()
	if x < exc:
		return "excelente"
	if x < exc + boa:
		return "boa"
	return "normal"


## Tier do metal de uma arma/armadura (pelo id: espada_ferro -> 2). 1 se não souber.
static func tier(id: String) -> int:
	var d := Inventario._dados(id)
	if d.has("tier"):
		return int(d.tier)
	for i in METAIS.size():
		if id.ends_with("_" + METAIS[i]):
			return i + 1
	return 1


## Materiais do tier para melhorar (dados/materiais_tier.json): [lingote, cristal, gema].
static func materiais_tier(t: int) -> Array:
	var d: Dictionary = Dados.lista_simples("materiais_tier")[clampi(t, 1, 10) - 1]
	return [d.lingote, d.cristal, d.gema]


## O que custa passar de +n para +n+1: {"itens": [[id, qtd]], "ouro", "sucesso"}.
static func custo_melhoria(c: Dictionary, id: String, melhoria_atual: int, falhas: int = 0, nivel_ferraria: int = 1,
		mestre: bool = false) -> Dictionary:
	var n := melhoria_atual + 1
	var mats := materiais_tier(tier(id))
	var itens := [[mats[0], n]]
	if int(c.melhoria_cristais[n - 1]) > 0:
		itens.append([mats[1], int(c.melhoria_cristais[n - 1])])
	if int(c.melhoria_gemas[n - 1]) > 0:
		itens.append([mats[2], int(c.melhoria_gemas[n - 1])])
	var preco := float(Inventario._dados(id).get("preco", 100))
	var sucesso := float(c.melhoria_sucesso[n - 1]) + falhas * float(c.melhoria_falha_bonus) + nivel_ferraria * float(c.melhoria_ferraria)
	if mestre:
		sucesso += float(c.mestre_artesao_melhoria)
	return {"itens": itens, "ouro": int(preco * float(c.melhoria_ouro) * n), "sucesso": minf(1.0, sucesso)}


## Multiplicador de ATQ/DEF de uma instância: melhoria (+5% cada) × raridade × qualidade.
static func mult_instancia(c: Dictionary, inst: Dictionary) -> float:
	var m := 1.0 + int(inst.get("melhoria", 0)) * float(c.melhoria_atq)
	m *= Loot.mult_raridade(c, inst.get("raridade", "comum"))
	m *= float(c.qualidade_mult.get(inst.get("qualidade", "normal"), 1.0))
	return m
