class_name Amizade
extends RefCounted
## Amizade com os NPCs (docs/SISTEMAS.md, secção 15; docs/NPCS.md, secção 2): 0 a 1000 pontos, 1 coração = 100.
## Falar pela 1.ª vez no dia +20; presentes (1 por dia e 2 por semana; no aniversário não conta e vale ×8).


## Dia contado desde o início (para "1 vez por dia" e "por semana").
static func dia_absoluto() -> int:
	return (Tempo.ano - 1) * 112 + Tempo.estacao * 28 + Tempo.dia


static func _reg(npc: String) -> Dictionary:
	if not Jogo.amizade.has(npc) or not (Jogo.amizade[npc] is Dictionary):
		Jogo.amizade[npc] = {"pontos": 0, "falou_dia": -1, "presente_dia": -1, "presentes_semana": 0, "semana": -1,
			"recentes": [], "vistas": []}
	return Jogo.amizade[npc]


static func pontos(npc: String) -> int:
	return int(_reg(npc).pontos)


static func coracoes(npc: String) -> int:
	return pontos(npc) / int(Dados.c("amizade_coracao", 100))


static func mudar(npc: String, valor: int) -> void:
	var r := _reg(npc)
	var antes := coracoes(npc)
	r.pontos = clampi(int(r.pontos) + valor, 0, int(Dados.c("amizade_maximo", 1000)))
	if coracoes(npc) > antes:
		Sistema.mensagem("%s: %d ❤" % [Dados.obter("npcs", npc).get("nome_pt", npc), coracoes(npc)], "nivel")


## Primeira conversa do dia: +20. Devolve true se foi a primeira.
static func falar(npc: String) -> bool:
	var r := _reg(npc)
	if int(r.falou_dia) == dia_absoluto():
		return false
	r.falou_dia = dia_absoluto()
	mudar(npc, int(Dados.c("amizade_falar", 20)))
	return true


static func falou_hoje(npc: String) -> bool:
	return int(_reg(npc).falou_dia) == dia_absoluto()


static func e_aniversario(npc: String) -> bool:
	var a = Dados.obter("npcs", npc).get("aniversario")
	return a is Dictionary and a.estacao == Tempo.nome_estacao() and int(a.dia) == Tempo.dia


## adora · gosta · neutro · nao_gosta · detesta
static func reacao(npc: String, item: String) -> String:
	var d := Dados.obter("npcs", npc)
	if item in d.get("adora", []):
		return "adora"
	if item in d.get("detesta", []):
		return "detesta"
	if item in d.get("gosta", []):
		return "gosta"
	return "neutro"


## Pode dar um presente hoje? ("" = pode; senão o motivo)
static func pode_dar(npc: String) -> String:
	if e_aniversario(npc):
		return "" if int(_reg(npc).presente_dia) != dia_absoluto() else "Já lhe deste um presente hoje."
	var r := _reg(npc)
	if int(r.presente_dia) == dia_absoluto():
		return "Já lhe deste um presente hoje."
	var semana := (dia_absoluto() - 1) / 7
	if int(r.semana) == semana and int(r.presentes_semana) >= int(Dados.c("presentes_por_semana", 2)):
		return "Já lhe deste dois presentes esta semana."
	return ""


## Dá o presente (tira-o da mochila) e devolve a reação.
static func dar(npc: String, item: String) -> String:
	if pode_dar(npc) != "" or not Jogo.inventario.tem(item):
		return ""
	var r := _reg(npc)
	var reac := reacao(npc, item)
	var v := int(Dados.c("amizade_presente", {}).get(reac, 20))
	var aniv := e_aniversario(npc)
	if aniv and v > 0:
		v *= int(Dados.c("amizade_aniversario_mult", 8))
	Jogo.inventario.retirar(item, 1)
	r.presente_dia = dia_absoluto()
	if not aniv:
		var semana := (dia_absoluto() - 1) / 7
		if int(r.semana) != semana:
			r.semana = semana
			r.presentes_semana = 0
		r.presentes_semana = int(r.presentes_semana) + 1
	mudar(npc, v)
	return reac


static func marcar_vista(npc: String, chave: String) -> void:
	var r := _reg(npc)
	if not chave in r.vistas:
		r.vistas.append(chave)


static func vista(npc: String, chave: String) -> bool:
	return chave in _reg(npc).vistas


## Lembra as últimas falas para não as repetir.
static func lembrar(npc: String, id: String) -> void:
	var r := _reg(npc)
	r.recentes.append(id)
	while r.recentes.size() > int(Dados.c("dialogo_falas_sem_repetir", 5)):
		r.recentes.pop_front()
