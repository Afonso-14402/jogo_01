extends JanelaUI
## Diário (J) e Quadro da Guilda (docs/INTERFACE.md, secções 4 e 5): missões ativas (a história com ⭐ primeiro),
## passos com o progresso e recompensas; no quadro, as missões que podes aceitar (como papéis pregados).

var modo := "diario"          # diario · quadro
var _lista: VBoxContainer
var _info: VBoxContainer
var _titulo: Label
var _aba := "ativas"
var _escolhida := ""


func _ready() -> void:
	acao = "diario"
	add_to_group("janelas")
	add_to_group("diario_ui")
	_criar_janela(Vector2(160, 60), Vector2(960, 600))
	_titulo = _texto(_janela, Vector2(20, 12), 18, Color("8fd3ff"))
	var abas := HBoxContainer.new()
	abas.position = Vector2(20, 44)
	abas.name = "abas"
	_janela.add_child(abas)
	_botao("Ativas", func(): _aba = "ativas"; _escolhida = ""; _mostrar(), abas)
	_botao("Concluídas", func(): _aba = "concluidas"; _escolhida = ""; _mostrar(), abas)
	for a in [["paginas", "Páginas"], ["bestiario", "Bestiário"], ["peixes", "Peixes"], ["titulos", "Títulos"], ["conquistas", "Conquistas"]]:
		_botao(a[1], func(): _aba = a[0]; _escolhida = ""; _mostrar(), abas)
	var rolar := ScrollContainer.new()
	rolar.position = Vector2(20, 84)
	rolar.size = Vector2(420, 500)
	_janela.add_child(rolar)
	_lista = VBoxContainer.new()
	_lista.custom_minimum_size = Vector2(400, 0)
	rolar.add_child(_lista)
	_info = VBoxContainer.new()
	_info.position = Vector2(470, 84)
	_info.custom_minimum_size = Vector2(470, 0)
	_janela.add_child(_info)
	Eventos.missao_mudou.connect(func(_i): if visible: _mostrar())


func abrir_quadro() -> void:
	modo = "quadro"
	_escolhida = ""
	abrir(true)


func abrir(sim: bool) -> void:
	super.abrir(sim)
	if not sim:
		modo = "diario"


func _linha(pai: Node, t: String, tam := 13, cor := Color.WHITE) -> Label:
	var l := _texto(pai, Vector2.ZERO, tam, cor)
	l.text = t
	if pai is VBoxContainer:
		l.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
		l.custom_minimum_size.x = (pai as Control).custom_minimum_size.x
	return l


func _mostrar() -> void:
	_limpar(_lista)
	_limpar(_info)
	(_janela.get_node("abas") as Control).visible = modo == "diario"
	var ids: Array = []
	if modo == "quadro":
		_titulo.text = "Quadro da Guilda   ·   Rank %s (%d pontos)   ·   %d/10 missões" % [Jogo.rank(), Jogo.pontos_guilda, Missoes.ativas().size()]
		ids = Missoes.quadro_disponiveis().map(func(m): return m.id)
	elif _aba in ["paginas", "bestiario", "peixes", "titulos", "conquistas"]:
		_titulo.text = "Diário"
		call("_aba_" + _aba)
		return
	else:
		_titulo.text = "Diário   ·   Rank %s" % Jogo.rank()
		for id in Jogo.missoes:
			var e := Missoes.estado(id)
			if (_aba == "ativas" and e in ["ativa", "pronta"]) or (_aba == "concluidas" and e == "concluida"):
				ids.append(id)
		ids.sort_custom(func(a, b): return int(Missoes.dados(a).get("tipo", "") == "historia") > int(Missoes.dados(b).get("tipo", "") == "historia"))
	if ids.is_empty():
		_linha(_lista, "Nada por aqui." if modo == "diario" else "Não há missões novas. Volta amanhã às 6:00.", 13, Color("9babb2"))
	for id in ids:
		var d := Missoes.dados(id)
		var b := Button.new()
		var pronta := Missoes.estado(id) == "pronta"
		b.text = "%s%s%s%s" % ["⭐ " if d.get("tipo", "") == "historia" else "", ("[%s] " % d.rank) if d.get("rank", "") != "" else "",
			d.get("nome_pt", id), "  ✓" if pronta else ""]
		b.flat = id != _escolhida
		b.alignment = HORIZONTAL_ALIGNMENT_LEFT
		b.custom_minimum_size = Vector2(400, 30)
		b.add_theme_color_override("font_color", Color("91db69") if pronta else Color.WHITE)
		b.pressed.connect(func(): _escolhida = id; _mostrar())
		_lista.add_child(b)
	if _escolhida != "":
		_detalhes(_escolhida)


func _detalhes(id: String) -> void:
	var d := Missoes.dados(id)
	_linha(_info, d.get("nome_pt", id), 18)
	var quem: String = Dados.obter("npcs", d.get("dada_por", "")).get("nome_pt", d.get("dada_por_pt", ""))
	if quem != "":
		_linha(_info, "Quem pede: " + quem, 12, Color("9babb2"))
	_linha(_info, d.get("descricao_pt", ""), 13, Color("c7dcd0"))
	_linha(_info, "", 6)
	var passos: Array = d.get("passos", [])
	for i in passos.size():
		var p: Dictionary = passos[i]
		var ok := Missoes.estado(id) != "inativa" and Missoes.passo_feito(id, i)
		var pr := Missoes.progresso(id, i)
		var t := ""
		match p.tipo:
			"matar":
				t = "Matar %s%s" % [Dados.monstro(p.monstro).get("nome_pt", p.monstro), (" (andar %d)" % p.andar) if p.has("andar") else ""]
			"derrotar":
				var nm: String = Dados.monstro(p.monstro).get("nome_pt", Dados.obter("bosses", p.monstro).get("nome_pt", p.monstro))
				t = "Vencer: %s" % nm
			"apanhar":
				t = "Trazer %s" % Inventario._dados(p.item).get("nome_pt", p.item)
			"ir_a":
				t = "Chegar ao andar %d" % p.andar
			"pescar":
				t = "Pescar peixes"
			"explorar":
				t = "Explorar %d%% do andar %d" % [int(p.percent * 100), p.andar]
			"falar":
				t = "Falar com %s" % Dados.obter("npcs", p.npc).get("nome_pt", p.npc)
			_:
				t = String(p.get("texto", "")).capitalize() if p.get("texto", "") == "" else String(p.texto)
		if int(p.get("qtd", 1)) > 1 and Missoes.estado(id) != "inativa":
			t += "  %d/%d" % [pr[0], pr[1]]
		elif int(p.get("qtd", 1)) > 1:
			t += "  ×%d" % p.qtd
		_linha(_info, ("✓ " if ok else "• ") + t, 13, Color("91db69") if ok else Color.WHITE)
	_linha(_info, "", 6)
	var r: Dictionary = d.get("recompensas", {})
	var rt: String = r.get("texto", "")
	if rt == "":
		rt = ", ".join([("%d ouro" % r.ouro) if r.has("ouro") else "", ("%d pontos de Guilda" % r.pontos_guilda) if int(r.get("pontos_guilda", 0)) > 0 else ""].filter(func(x): return x != ""))
	_linha(_info, "Recompensa: " + rt, 13, Color("f9c22b"))
	if modo == "quadro" and Missoes.estado(id) == "inativa":
		var motivo := Missoes.pode_aceitar(id)
		var b := _botao("Aceitar", func(): Missoes.aceitar(id); _escolhida = ""; _mostrar(), _info)
		b.disabled = motivo != ""
		if motivo != "":
			_linha(_info, motivo, 12, Color("e83b3b"))


# ------------------------------------------------------------------ coleções ------------------------------------------------------------------

func _item_lista(texto: String, icone: String, ativo: bool, cb: Callable) -> void:
	var h := HBoxContainer.new()
	_lista.add_child(h)
	var ic := _icone(icone, 24)
	ic.modulate = Color.WHITE if ativo else Color(0.2, 0.2, 0.25)
	h.add_child(ic)
	var b := Button.new()
	b.text = texto
	b.flat = true
	b.alignment = HORIZONTAL_ALIGNMENT_LEFT
	b.custom_minimum_size = Vector2(360, 26)
	b.disabled = not ativo
	b.pressed.connect(cb)
	h.add_child(b)


## As 100 páginas por ordem, com buracos nas que faltam ("Página 7 — ?").
func _aba_paginas() -> void:
	_titulo.text = "Diário de A.   ·   %d/100 páginas" % Jogo.paginas.size()
	for p in Dados.lista_simples("paginas"):
		var tem := int(p.numero) in Jogo.paginas
		_item_lista("Página %d — %s" % [p.numero, p.titulo if tem else "?"], "res://arte/icones/pagina_diario.png", tem, func():
			var ui = get_tree().get_first_node_in_group("pagina_ui")
			abrir(false)
			if ui:
				ui.mostrar(int(p.numero)))


## Bestiário (com o Velho Fausto): os que já venceste; fraquezas com 5, drops com 10.
func _aba_bestiario() -> void:
	var todos: Array = Dados.tabela("monstros").values()
	_titulo.text = "Bestiário   ·   %d/%d" % [Jogo.bestiario.size(), todos.size()]
	todos.sort_custom(func(a, b): return int(a.regiao) * 1000 + (a.andares[0] if not a.andares.is_empty() else 0) < int(b.regiao) * 1000 + (b.andares[0] if not b.andares.is_empty() else 0))
	for m in todos:
		var n := int(Jogo.bestiario.get(m.id, 0))
		var icone: String = String(m.get("sprite", "")) + "_parado_lado.png"
		_item_lista("%s%s" % [m.nome_pt if n > 0 else "???", ("  ×%d" % n) if n > 0 else ""], "", n > 0, func(): _escolhida = m.id; _detalhe_monstro(m))


func _detalhe_monstro(m: Dictionary) -> void:
	_limpar(_info)
	var n := int(Jogo.bestiario.get(m.id, 0))
	_linha(_info, m.nome_pt, 18)
	_linha(_info, "Região %d · andares %s · vencidos: %d" % [m.regiao, ", ".join(m.andares.map(func(x): return str(int(x)))), n], 12, Color("9babb2"))
	_linha(_info, m.get("comportamento", ""), 13, Color("c7dcd0"))
	if n >= 5:
		_linha(_info, "Fraco a: %s · Resiste a: %s" % [", ".join(m.get("fraquezas", [])) if not m.get("fraquezas", []).is_empty() else "—",
			", ".join(m.get("resistencias", [])) if not m.get("resistencias", []).is_empty() else "—"], 13, Color("91db69"))
	else:
		_linha(_info, "Vence-o 5 vezes para saberes as fraquezas.", 12, Color("9babb2"))
	if n >= 10:
		var drops: Array = m.get("drops", []).map(func(d): return "%s (%d%%)" % [Inventario._dados(d.item).get("nome_pt", d.item), int(float(d.hipotese) * 100)])
		_linha(_info, "Drops: " + ", ".join(drops), 13, Color("f9c22b"))


func _aba_peixes() -> void:
	var todos: Array = Dados.tabela("peixes").values()
	_titulo.text = "Peixes   ·   %d/%d espécies" % [Jogo.peixes.size(), todos.size()]
	for p in todos:
		var n := int(Jogo.peixes.get(p.id, 0))
		_item_lista("%s%s" % [p.nome_pt if n > 0 else "???", ("  ×%d" % n) if n > 0 else ""], Inventario._dados(p.id).get("icone", ""), true, func():
			_limpar(_info)
			_linha(_info, p.nome_pt if n > 0 else "???", 18)
			_linha(_info, "%s · %s" % [String(p.raridade).capitalize(), p.onde_pt], 13, Color("c7dcd0"))
			_linha(_info, "Quando: " + String(p.quando_pt), 13, Color("9babb2")))


func _aba_titulos() -> void:
	var todos: Array = Dados.tabela("titulos").values()
	_titulo.text = "Títulos   ·   %d/%d" % [Jogo.titulos.size(), todos.size()]
	for t in todos:
		var tem: bool = t.id in Jogo.titulos
		_item_lista(("★ " if Jogo.titulo == t.id else "") + (t.nome_pt if tem else "???"), "", true, func():
			_limpar(_info)
			_linha(_info, t.nome_pt if tem else "???", 18)
			_linha(_info, "Como: " + t.como_pt, 13, Color("c7dcd0"))
			if t.bonus_pt != "" and t.bonus_pt != "—":
				_linha(_info, "Bónus: " + t.bonus_pt, 13, Color("91db69"))
			if tem:
				_botao("Usar este título", func(): Jogo.titulo = t.id; _mostrar(), _info))


func _aba_conquistas() -> void:
	var todas: Array = Dados.tabela("conquistas").values()
	_titulo.text = "Conquistas   ·   %d/%d" % [Jogo.conquistas.size(), todas.size()]
	var grupo := ""
	for c in todas:
		if c.grupo != grupo:
			grupo = c.grupo
			_linha(_lista, grupo, 14, Color("8fd3ff"))
		var tem: bool = c.id in Jogo.conquistas
		_linha(_lista, ("✓ " if tem else "· ") + c.nome_pt, 13, Color("91db69") if tem else Color("9babb2"))
