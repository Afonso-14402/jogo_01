extends JanelaUI
## Janela de crafting (docs/INTERFACE.md, secção 5): receitas conhecidas da estação (filtrar "posso fazer"),
## ingredientes com ✓/✗, botão Fazer com barra de progresso; receitas desconhecidas aparecem como "???".
## Na forja há também o separador Melhorar (+1…+10, docs/SISTEMAS.md 11.3).

var estacao := "fogueira"
var _lista: VBoxContainer
var _info: VBoxContainer
var _titulo: Label
var _so_posso := false
var _escolhida := ""
var _modo := "fazer"          # fazer · melhorar
var _a_fazer := false
var _rng := RandomNumberGenerator.new()


func _ready() -> void:
	add_to_group("janelas")
	add_to_group("crafting_ui")
	_rng.randomize()
	_criar_janela(Vector2(180, 70), Vector2(920, 580))
	_titulo = _texto(_janela, Vector2(20, 12), 18, Color("8fd3ff"))
	var topo := HBoxContainer.new()
	topo.position = Vector2(20, 44)
	_janela.add_child(topo)
	_botao("Fazer", func(): _modo = "fazer"; _escolhida = ""; _mostrar(), topo)
	_botao("Melhorar", func(): _modo = "melhorar"; _escolhida = ""; _mostrar(), topo).name = "melhorar"
	_botao("Só o que posso fazer", func(): _so_posso = not _so_posso; _mostrar(), topo)
	var rolar := ScrollContainer.new()
	rolar.position = Vector2(20, 84)
	rolar.size = Vector2(400, 480)
	_janela.add_child(rolar)
	_lista = VBoxContainer.new()
	_lista.custom_minimum_size = Vector2(380, 0)
	rolar.add_child(_lista)
	_info = VBoxContainer.new()
	_info.position = Vector2(450, 84)
	_info.custom_minimum_size = Vector2(450, 0)
	_janela.add_child(_info)


func abrir_estacao(e: String) -> void:
	estacao = e
	_modo = "fazer"
	_escolhida = ""
	abrir(true)


func _linha(pai: Node, t: String, tam := 13, cor := Color.WHITE) -> Label:
	var l := _texto(pai, Vector2.ZERO, tam, cor)
	l.text = t
	if pai is VBoxContainer:
		l.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
		l.custom_minimum_size.x = (pai as Control).custom_minimum_size.x
	return l


func _mostrar() -> void:
	_titulo.text = Estacao.NOMES.get(estacao, estacao) + "   ·   %d ouro" % Jogo.ouro
	(_janela.find_child("melhorar", true, false) as Button).visible = estacao == "forja"
	_limpar(_lista)
	_limpar(_info)
	if _modo == "melhorar":
		_mostrar_melhorar()
		return
	for r in Crafting.da_estacao(estacao):
		var conhecida := Jogo.conhece(r.id)
		var pode := conhecida and Crafting.pode_fazer(Jogo.inventario, Jogo.ouro, r)
		if _so_posso and not pode:
			continue
		var h := HBoxContainer.new()
		_lista.add_child(h)
		var d := Inventario._dados(r.resultado)
		var ic := _icone(d.get("icone", "") if conhecida else "", 28)
		h.add_child(ic)
		var b := Button.new()
		b.text = d.get("nome_pt", r.resultado) if conhecida else "???"
		b.flat = r.id != _escolhida
		b.alignment = HORIZONTAL_ALIGNMENT_LEFT
		b.custom_minimum_size = Vector2(300, 30)
		b.add_theme_color_override("font_color", Color("91db69") if pode else (Color.WHITE if conhecida else Color("625565")))
		b.disabled = not conhecida
		b.pressed.connect(func(): _escolhida = r.id; _mostrar())
		h.add_child(b)
	if _escolhida != "":
		_mostrar_receita(Crafting.receita(_escolhida))
	else:
		_linha(_info, "Escolhe uma receita. As que estão a verde podes fazer já.\nApanhar todos os ingredientes de uma receita pela primeira vez ensina-ta.", 13, Color("9babb2"))


func _mostrar_receita(r: Dictionary) -> void:
	var d := Inventario._dados(r.resultado)
	var h := HBoxContainer.new()
	_info.add_child(h)
	h.add_child(_icone(d.get("icone", ""), 48))
	_linha(h, "  %s%s" % [d.get("nome_pt", r.resultado), (" ×%d" % r.qtd) if int(r.get("qtd", 1)) > 1 else ""], 18)
	_linha(_info, d.get("descricao_pt", ""), 12, Color("c7dcd0"))
	if d.has("def"):
		_linha(_info, "DEF %d   RES %d   (%s)" % [d.def, d.res, d.get("espaco", "")], 13)
	elif d.has("atq"):
		_linha(_info, "ATQ %d   Velocidade %.1f" % [d.atq, float(d.get("velocidade", 1))], 13)
	_linha(_info, "", 6)
	_linha(_info, "Ingredientes:", 14, Color("8fd3ff"))
	for i in Crafting.ingredientes(Jogo.inventario, r):
		var ok: bool = i[1] >= i[2]
		var l := HBoxContainer.new()
		_info.add_child(l)
		l.add_child(_icone(Inventario._dados(i[0]).get("icone", ""), 22))
		_linha(l, "  %s %s  %d / %d" % ["✓" if ok else "✗", Inventario._dados(i[0]).get("nome_pt", i[0]), i[1], i[2]], 13,
				Color("91db69") if ok else Color("e83b3b"))
	if int(r.get("ouro", 0)) > 0:
		_linha(_info, "Ouro: %d" % r.ouro, 13, Color("f9c22b") if Jogo.ouro >= int(r.ouro) else Color("e83b3b"))
	var sk: String = r.get("skill", "")
	if sk != "":
		var n := Jogo.nivel_vida(sk)
		var mestre := 2.0 if Jogo.tem_unica("mestre_artesao") else 1.0
		var c := Dados.constantes
		_linha(_info, "%s nível %d (precisa %d)" % [Dados.obter("skills_vida", sk).get("nome_pt", sk), n, r.get("skill_min", 1)], 12, Color("9babb2"))
		if Inventario.e_equipamento(r.resultado):
			_linha(_info, "Qualidade possível: Boa %d%% · Excelente %d%%" % [
				int((float(c.qualidade_boa_base) + n * float(c.qualidade_boa_por_skill)) * mestre * 100),
				int((float(c.qualidade_excelente_base) + n * float(c.qualidade_excelente_por_skill)) * mestre * 100)], 12, Color("9babb2"))
	_linha(_info, "", 6)
	var barra := _barra_progresso(0, 100, 300, Color("f9c22b"))
	barra.visible = false
	var b := _botao("Fazer", Callable(), _info)
	_info.add_child(barra)
	b.disabled = _a_fazer or not Crafting.pode_fazer(Jogo.inventario, Jogo.ouro, r)
	b.pressed.connect(func(): _fazer(r, barra, b))


## Fazer demora 1–3 s (barra) e no fim aparece o resultado.
func _fazer(r: Dictionary, barra: ProgressBar, botao: Button) -> void:
	_a_fazer = true
	botao.disabled = true
	barra.visible = true
	var lim: Array = Dados.c("crafting_tempo", [1.0, 3.0])
	var dur: float = lerpf(float(lim[0]), float(lim[1]), clampf(float(r.get("skill_min", 1)) / 45.0, 0.0, 1.0))
	var tw := create_tween()
	tw.tween_property(barra, "value", 100.0, dur)
	await tw.finished
	var res := Jogo.fazer(r.id, _rng)
	_a_fazer = false
	if res.ok:
		var q: String = res.qualidade
		Sistema.mensagem("Fizeste: %s%s." % [Inventario._dados(res.id).get("nome_pt", res.id), "" if q == "normal" else " (%s)" % q.capitalize()], "nivel")
	else:
		Sistema.mensagem(res.erro, "aviso")
	_mostrar()


func _mostrar_melhorar() -> void:
	_linha(_lista, "Armas e armaduras:", 14, Color("8fd3ff"))
	var opcoes := []
	if Jogo.arma_equipada != "":
		var e := Jogo.arma_extra
		e["id"] = Jogo.arma_equipada
		opcoes.append(["(equipada)", e])
	for k in Jogo.equipamento:
		opcoes.append(["(vestida)", Jogo.equipamento[k]])
	for e in Jogo.inventario.espacos:
		if e != null and Inventario.e_equipamento(e.id) and Inventario._dados(e.id).get("categoria", "") != "ferramenta":
			opcoes.append(["", e])
	for o in opcoes:
		var e: Dictionary = o[1]
		var d := Inventario._dados(e.id)
		var h := HBoxContainer.new()
		_lista.add_child(h)
		h.add_child(_icone(d.get("icone", ""), 28))
		var b := Button.new()
		b.text = "%s +%d %s" % [d.get("nome_pt", e.id), int(e.get("melhoria", 0)), o[0]]
		b.flat = str(e.get("inst", e.id)) != _escolhida
		b.alignment = HORIZONTAL_ALIGNMENT_LEFT
		b.custom_minimum_size = Vector2(300, 30)
		b.pressed.connect(func(): _escolhida = str(e.get("inst", e.id)); _mostrar())
		h.add_child(b)
		if str(e.get("inst", e.id)) == _escolhida:
			_mostrar_melhoria(e)
	if _escolhida == "":
		_linha(_info, "Cada +1 dá +5% de ATQ (ou DEF). Até +5 nunca falha; depois pode falhar, mas a arma nunca se parte nem desce, e cada falhanço dá +5% à tentativa seguinte.", 13, Color("9babb2"))


func _mostrar_melhoria(e: Dictionary) -> void:
	var n := int(e.get("melhoria", 0))
	var d := Inventario._dados(e.id)
	_linha(_info, "%s  +%d → +%d" % [d.get("nome_pt", e.id), n, mini(10, n + 1)], 18)
	if n >= 10:
		_linha(_info, "Já está no máximo (+10).", 13, Color("fbff86"))
		return
	var custo := Crafting.custo_melhoria(Dados.constantes, e.id, n, int(e.get("falhas", 0)), Jogo.nivel_vida("ferraria"), Jogo.tem_unica("mestre_artesao"))
	_linha(_info, "Hipótese de sucesso: %d%%" % int(round(float(custo.sucesso) * 100)), 15, Color("91db69") if custo.sucesso >= 1.0 else Color("f9c22b"))
	var pode := Jogo.ouro >= int(custo.ouro)
	for i in custo.itens:
		var tem := Jogo.inventario.contar(i[0])
		pode = pode and tem >= int(i[1])
		var l := HBoxContainer.new()
		_info.add_child(l)
		l.add_child(_icone(Inventario._dados(i[0]).get("icone", ""), 22))
		_linha(l, "  %s  %d / %d" % [Inventario._dados(i[0]).get("nome_pt", i[0]), tem, i[1]], 13, Color("91db69") if tem >= int(i[1]) else Color("e83b3b"))
	_linha(_info, "Ouro: %d" % custo.ouro, 13, Color("f9c22b") if Jogo.ouro >= int(custo.ouro) else Color("e83b3b"))
	var b := _botao("Melhorar", func():
		var r := Jogo.melhorar(e, _rng)
		if not r.ok:
			Sistema.mensagem(r.erro, "aviso")
		elif r.sucesso:
			Audio.efeito("melhoria_ok", 0.0)
			Sistema.mensagem("Sucesso! Agora está +%d." % r.melhoria, "nivel")
			if e.get("inst", "") == Jogo.arma_extra.get("inst", "-") or e.id == Jogo.arma_equipada:
				Jogo.arma_extra = e
		else:
			Audio.efeito("melhoria_falhada", 0.0)
			Sistema.mensagem("Falhou... (a próxima tentativa tem +5%)", "aviso")
		_mostrar(), _info)
	b.disabled = not pode
