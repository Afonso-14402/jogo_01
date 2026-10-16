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
	_mensagens = VBoxContainer.new()
	_mensagens.position = Vector2(16, 140)
	_mensagens.mouse_filter = Control.MOUSE_FILTER_IGNORE
	raiz.add_child(_mensagens)
	Eventos.stats_mudaram.connect(_atualizar)
	Eventos.mensagem_sistema.connect(_mensagem)
	Eventos.xp_ganha.connect(func(_v): _atualizar())
	_atualizar()


func _process(_delta: float) -> void:
	_est.value = Jogo.estamina
	_mp.value = Jogo.mp
	_hora.text = Tempo.texto_hora()


func _atualizar() -> void:
	_nome.text = "%s   Nv %d" % [Jogo.nome, Jogo.nivel]
	_hp.max_value = Jogo.hp_maximo()
	_hp.value = Jogo.hp
	_mp.max_value = Jogo.mp_maximo()
	_est.max_value = Jogo.estamina_maxima()
	_xp.max_value = Jogo.xp_para_subir()
	_xp.value = Jogo.xp


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
