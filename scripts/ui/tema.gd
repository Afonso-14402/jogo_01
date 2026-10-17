class_name Tema
extends RefCounted
## O tema de todos os botões do jogo: os botões do "Sistema" em pixel art (arte/ui/botao_*.png, de
## ferramentas/arte/ui.py), desenhados ao dobro (píxeis grossos como o resto do jogo) e com texto claro.

const UI := "res://arte/ui/"
const ESCALA := 2


## Muda o tema base do Godot (vale para todas as janelas, também as que estão dentro de CanvasLayers).
static func aplicar() -> void:
	criar(ThemeDB.get_default_theme())


static func criar(t: Theme = null) -> Theme:
	if t == null:
		t = Theme.new()
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
		t.set_color("font_outline_color", tipo, Color("2e222f"))
		t.set_constant("outline_size", tipo, 4)
	return t


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
