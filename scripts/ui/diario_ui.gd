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
