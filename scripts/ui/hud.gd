extends CanvasLayer
## HUD (docs/INTERFACE.md, secção 2): retrato, nome, nível, barras de HP/MP/Estamina e mensagens do Sistema.

const UI := "res://arte/ui/"

var _hp: TextureProgressBar
var _mp: TextureProgressBar
var _est: TextureProgressBar
var _xp: TextureProgressBar
var _nome: Label
var _mensagens: VBoxContainer
var _hora: Label
var _ouro: Label
var _aviso_usar: Label
var _rapida: Array = []    # [[TextureRect ícone, Label quantidade]]
var _arma_icone: TextureRect
var _skills: Array = []   # [[TextureRect ícone, ColorRect recarga]]
var _icones_estados: HBoxContainer
var _cegueira: TextureRect
var _assinatura_estados := ""


func _ready() -> void:
	var raiz := Control.new()
	raiz.set_anchors_preset(Control.PRESET_FULL_RECT)
	raiz.mouse_filter = Control.MOUSE_FILTER_IGNORE
	add_child(raiz)
	var caixa := _janela(Vector2(12, 12), Vector2(300, 92))
	raiz.add_child(caixa)
	var retrato := TextureRect.new()
	retrato.texture = load("res://arte/retratos/heroi_normal.png")
	retrato.position = Vector2(8, 10)
	retrato.size = Vector2(72, 72)
	retrato.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	retrato.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	caixa.add_child(retrato)
	_nome = _texto(caixa, Vector2(88, 6), 14)
	_hp = _barra(caixa, "hp", Vector2(88, 28), 200)
	_mp = _barra(caixa, "mp", Vector2(88, 46), 160)
	_est = _barra(caixa, "estamina", Vector2(88, 62), 140)
	_xp = _barra(caixa, "xp", Vector2(88, 78), 200, 6)
	_hora = _texto(raiz, Vector2(1180, 16), 16)
	_ouro = _texto(raiz, Vector2(1120, 40), 14)
	_ouro.add_theme_color_override("font_color", Color("f9c22b"))
	# barra rápida (6 espaços) e a arma, em baixo
	for i in 6:
		var casa := TextureRect.new()
		casa.texture = load(UI + "casa.png")
		casa.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
		casa.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
		casa.position = Vector2(470 + i * 52, 650)
		casa.size = Vector2(48, 48)
		raiz.add_child(casa)
		var ic := TextureRect.new()
		ic.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
		ic.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
		ic.position = Vector2(8, 8)
		ic.size = Vector2(32, 32)
		casa.add_child(ic)
		var q := _texto(casa, Vector2(28, 28), 12)
		var tecla := _texto(casa, Vector2(3, 0), 10)
		tecla.text = "Q" if i == 0 else ""
		_rapida.append([ic, q])
	# barra de skills (teclas 1–6), por cima da barra rápida
	for i in 6:
		var casa := TextureRect.new()
		casa.texture = load(UI + "casa.png")
		casa.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
		casa.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
		casa.position = Vector2(474 + i * 52, 604)
		casa.size = Vector2(40, 40)
		raiz.add_child(casa)
		var ic := TextureRect.new()
		ic.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
		ic.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
		ic.position = Vector2(4, 4)
		ic.size = Vector2(32, 32)
		casa.add_child(ic)
		var rec := ColorRect.new()
		rec.color = Color(0.1, 0.07, 0.12, 0.7)
		rec.position = Vector2(4, 4)
		rec.size = Vector2(32, 0)
		casa.add_child(rec)
		_texto(casa, Vector2(2, -2), 10).text = str(i + 1)
		_skills.append([ic, rec])
	var casa_arma := TextureRect.new()
	casa_arma.texture = load(UI + "casa_selecionada.png")
	casa_arma.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	casa_arma.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	casa_arma.position = Vector2(796, 642)
	casa_arma.size = Vector2(56, 56)
	raiz.add_child(casa_arma)
	_arma_icone = TextureRect.new()
	_arma_icone.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	_arma_icone.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	_arma_icone.position = Vector2(8, 8)
	_arma_icone.size = Vector2(40, 40)
	casa_arma.add_child(_arma_icone)
	_aviso_usar = _texto(raiz, Vector2(560, 470), 16)
	_icones_estados = HBoxContainer.new()
	_icones_estados.position = Vector2(14, 108)
	_icones_estados.add_theme_constant_override("separation", 4)
	raiz.add_child(_icones_estados)
	# Cegueira: o ecrã escurece à volta
	var g := GradientTexture2D.new()
	g.fill = GradientTexture2D.FILL_RADIAL
	g.fill_from = Vector2(0.5, 0.5)
	g.fill_to = Vector2(1.0, 0.5)
	g.gradient = Gradient.new()
	g.gradient.set_color(0, Color(0, 0, 0, 0))
	g.gradient.set_color(1, Color(0.05, 0.03, 0.06, 0.97))
	g.gradient.set_offset(0, 0.25)
	_cegueira = TextureRect.new()
	_cegueira.texture = g
	_cegueira.set_anchors_preset(Control.PRESET_FULL_RECT)
	_cegueira.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	_cegueira.mouse_filter = Control.MOUSE_FILTER_IGNORE
	_cegueira.visible = false
	raiz.add_child(_cegueira)
	raiz.move_child(_cegueira, 0)
	_mensagens = VBoxContainer.new()
	_mensagens.position = Vector2(16, 140)
	_mensagens.mouse_filter = Control.MOUSE_FILTER_IGNORE
	raiz.add_child(_mensagens)
	add_child(preload("res://scripts/ui/inventario_ui.gd").new())
	add_child(preload("res://scripts/ui/status_ui.gd").new())
	add_child(preload("res://scripts/ui/crafting_ui.gd").new())
	Eventos.stats_mudaram.connect(_atualizar)
	Eventos.mensagem_sistema.connect(_mensagem)
	Eventos.xp_ganha.connect(func(_v): _atualizar())
	Eventos.ouro_mudou.connect(func(_v): _atualizar())
	Eventos.item_apanhado.connect(func(_a, _b): _atualizar())
	Jogo.inventario.mudou.connect(_atualizar)
	_atualizar()


func _process(_delta: float) -> void:
	_est.value = Jogo.estamina
	_mp.value = Jogo.mp
	_hora.text = Tempo.texto_hora()
	var j := get_tree().get_first_node_in_group("jogador")
	_mostrar_estados()
	for i in 6:
		var id: String = Jogo.skills_barra[i]
		var ic: TextureRect = _skills[i][0]
		var rec: ColorRect = _skills[i][1]
		var sk := Jogo.skill(id) if id != "" else {}
		var caminho: String = sk.get("icone", "")
		if caminho == "":
			ic.texture = null
		elif ic.texture == null or ic.texture.resource_path != caminho:
			ic.texture = load(caminho)
		var falta: float = j.recargas_skill.get(id, 0.0) if j else 0.0
		rec.size.y = 32.0 * clampf(falta / max(0.1, float(sk.get("recarga", 1.0))), 0.0, 1.0)
		rec.position.y = 36.0 - rec.size.y
		ic.modulate = Color(0.45, 0.45, 0.5) if sk.has("arma") and j and sk.arma != j.arma.get("tipo", "") else Color.WHITE
	var it = j.interagivel_perto if j else null
	_aviso_usar.text = "[E] %s" % it.texto if it else ""
	if j and j.arma.get("icone", "") != "" and _arma_icone.texture == null:
		_arma_icone.texture = load(j.arma.icone)


## Ícones dos estados ativos (veneno, frio...) e dos bónus das poções, debaixo das barras.
func _mostrar_estados() -> void:
	var e = Jogo.estados
	var lista: Array = []
	if e and is_instance_valid(e):
		lista = e.ativos.keys()
	_cegueira.visible = "cegueira" in lista
	var assinatura := ",".join(lista) + "|" + ",".join(Jogo.buffs.keys())
	if assinatura == _assinatura_estados:
		return
	_assinatura_estados = assinatura
	for c in _icones_estados.get_children():
		c.queue_free()
	for id in lista:
		var caminho := "res://arte/efeitos/estado_%s.png" % id
		if not ResourceLoader.exists(caminho):
			continue
		var at := AtlasTexture.new()
		at.atlas = load(caminho)
		at.region = Rect2(0, 0, 9, at.atlas.get_height())
		var t := TextureRect.new()
		t.texture = at
		t.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
		t.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
		t.custom_minimum_size = Vector2(27, 33)
		t.tooltip_text = Estados.info(id).get("nome_pt", id)
		_icones_estados.add_child(t)
	for k in Jogo.buffs:
		var l := _texto(_icones_estados, Vector2.ZERO, 12)
		l.text = {"atq": "ATQ+", "def": "DEF+", "velocidade": "VEL+", "regenerar": "REGEN"}.get(k, k)
		l.add_theme_color_override("font_color", Color("91db69"))


func _atualizar() -> void:
	_nome.text = "%s   Nv %d" % [Jogo.nome, Jogo.nivel]
	_hp.max_value = Jogo.hp_maximo()
	_hp.value = Jogo.hp
	_mp.max_value = Jogo.mp_maximo()
	_est.max_value = Jogo.estamina_maxima()
	_xp.max_value = Jogo.xp_para_subir()
	_xp.value = Jogo.xp
	_ouro.text = "%d ouro" % Jogo.ouro
	for i in 6:
		var id: String = Jogo.inventario.barra_rapida[i]
		var ic: TextureRect = _rapida[i][0]
		var q: Label = _rapida[i][1]
		var icone: String = Inventario._dados(id).get("icone", "") if id != "" else ""
		ic.texture = load(icone) if icone != "" and ResourceLoader.exists(icone) else null
		var n := Jogo.inventario.contar(id) if id != "" else 0
		q.text = str(n) if n > 0 else ""
		ic.modulate.a = 1.0 if n > 0 else 0.35
	var arma: Dictionary = Dados.arma(Jogo.arma_equipada)
	if arma.get("icone", "") != "" and ResourceLoader.exists(arma.icone):
		_arma_icone.texture = load(arma.icone)


func _mensagem(texto: String, _tipo: String) -> void:
	var l := Label.new()
	l.text = texto
	l.add_theme_color_override("font_color", Color("8fd3ff"))
	l.add_theme_color_override("font_outline_color", Color("2e222f"))
	l.add_theme_constant_override("outline_size", 4)
	_mensagens.add_child(l)
	if _mensagens.get_child_count() > 6:
		_mensagens.get_child(0).queue_free()
	var t := create_tween()
	t.tween_interval(4.0)
	t.tween_property(l, "modulate:a", 0.0, 0.6)
	t.tween_callback(l.queue_free)


func _janela(pos: Vector2, tam: Vector2) -> NinePatchRect:
	var j := NinePatchRect.new()
	j.texture = load(UI + "janela_sistema.png")
	j.patch_margin_left = 6
	j.patch_margin_right = 6
	j.patch_margin_top = 6
	j.patch_margin_bottom = 6
	j.position = pos
	j.size = tam
	j.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	return j


func _barra(pai: Control, nome: String, pos: Vector2, largura: float, altura: float = 12) -> TextureProgressBar:
	var b := TextureProgressBar.new()
	b.texture_under = load(UI + "barra_moldura.png")
	b.texture_progress = load(UI + "barra_%s.png" % nome)
	b.nine_patch_stretch = true
	b.stretch_margin_left = 2
	b.stretch_margin_right = 2
	b.stretch_margin_top = 2
	b.stretch_margin_bottom = 2
	b.texture_progress_offset = Vector2(1, 1)
	b.position = pos
	b.size = Vector2(largura, altura)
	b.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	pai.add_child(b)
	return b


func _texto(pai: Control, pos: Vector2, tam: int) -> Label:
	var l := Label.new()
	l.position = pos
	l.add_theme_font_size_override("font_size", tam)
	l.add_theme_color_override("font_color", Color.WHITE)
	l.add_theme_color_override("font_outline_color", Color("2e222f"))
	l.add_theme_constant_override("outline_size", 4)
	pai.add_child(l)
	return l
