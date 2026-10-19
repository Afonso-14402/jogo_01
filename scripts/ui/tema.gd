class_name Tema
extends RefCounted
## O tema de todos os botões do jogo: os botões do "Sistema" em pixel art (arte/ui/botao_*.png, de
## ferramentas/arte/ui.py), desenhados ao dobro (píxeis grossos como o resto do jogo) e com texto claro.

const UI := "res://arte/ui/"
const ESCALA := 2


## Muda o tema base do Godot (vale para todas as janelas, também as que estão dentro de CanvasLayers).
static func aplicar(arvore: SceneTree = null) -> void:
	criar(ThemeDB.get_default_theme())
	if arvore and not arvore.node_added.is_connected(ver_no):
		arvore.node_added.connect(ver_no)


static func criar(t: Theme = null) -> Theme:
	if t == null:
		t = Theme.new()
	t.default_font = fonte()
	t.default_font_size = 16
	var estilos := {"normal": "botao_normal", "hover": "botao_por_cima", "pressed": "botao_premido",
			"disabled": "botao_desligado", "focus": "botao_por_cima", "hover_pressed": "botao_premido"}
	for estado in estilos:
		var s := _estilo(estilos[estado])
		if estado == "focus":   # o foco (comando/teclado) só desenha a moldura clara por cima
			s.draw_center = false
		for tipo in ["Button", "OptionButton", "MenuButton"]:
			t.set_stylebox(estado, tipo, s)
	for tipo in ["Button", "OptionButton", "MenuButton"]:
		t.set_color("font_color", tipo, Color("c7dcd0"))
		t.set_color("font_hover_color", tipo, Color("ffffff"))
		t.set_color("font_focus_color", tipo, Color("ffffff"))
		t.set_color("font_pressed_color", tipo, Color("8fd3ff"))
		t.set_color("font_disabled_color", tipo, Color("7f708a"))
	return t


static var _fonte: Font
static var _contorno: Font


## A letra com contorno escuro (para os textos por cima do mapa: mensagens, nomes, números).
static func fonte_contorno() -> Font:
	if _contorno == null:
		var f: FontFile = load(UI + "fonte_pixel_contorno.fnt")
		if f == null:
			return fonte()
		f.fixed_size_scale_mode = TextServer.FIXED_SIZE_SCALE_INTEGER_ONLY
		f.fallbacks = [ThemeDB.fallback_font]
		_contorno = f
	return _contorno


## Os textos que pediam contorno (outline_size) passam para a letra com contorno desenhado.
static func ver_no(n: Node) -> void:
	if n is Control and not n is Button:
		_ver.call_deferred(n)


static func _ver(n: Variant) -> void:   # (Variant: o nó pode já ter sido apagado quando isto corre)
	if not is_instance_valid(n):
		return
	var c := n as Control
	# a letra em pixel só tem 1× e 2×: os textos pedidos com 11–13 ficavam com 1× (ilegíveis); passam a 2×
	if (c is Label or c is RichTextLabel) and c.has_theme_font_size_override("font_size" if c is Label else "normal_font_size"):
		var k_tam := "font_size" if c is Label else "normal_font_size"
		var t := c.get_theme_font_size(k_tam)
		if t >= 11 and t < 14:
			c.add_theme_font_size_override(k_tam, 14)
	for k in ["outline_size"]:
		if c.has_theme_constant_override(k) and c.get_theme_constant(k) > 0:
			if c is RichTextLabel:
				c.add_theme_font_override("normal_font", fonte_contorno())
			else:
				c.add_theme_font_override("font", fonte_contorno())


## A letra do jogo em pixel art (ferramentas/arte/fonte.py); o que ela não tiver (emojis, setas) vem da letra normal.
static func fonte() -> Font:
	if _fonte == null:
		var f: FontFile = load(UI + "fonte_pixel.fnt")
		if f == null:
			return ThemeDB.fallback_font
		f.fixed_size_scale_mode = TextServer.FIXED_SIZE_SCALE_INTEGER_ONLY
		f.fallbacks = [ThemeDB.fallback_font]
		_fonte = f
	return _fonte


static func _estilo(nome: String) -> StyleBoxTexture:
	var s := StyleBoxTexture.new()
	var img: Image = (load(UI + nome + ".png") as Texture2D).get_image()
	img.resize(img.get_width() * ESCALA, img.get_height() * ESCALA, Image.INTERPOLATE_NEAREST)
	s.texture = ImageTexture.create_from_image(img)
	for lado in [SIDE_LEFT, SIDE_TOP, SIDE_RIGHT, SIDE_BOTTOM]:
		s.set_texture_margin(lado, 3 * ESCALA)
	s.set_content_margin(SIDE_LEFT, 12)
	s.set_content_margin(SIDE_RIGHT, 12)
	s.set_content_margin(SIDE_TOP, 6)
	s.set_content_margin(SIDE_BOTTOM, 8)
	return s
