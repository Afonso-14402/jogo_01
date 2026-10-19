class_name JanelaUI
extends CanvasLayer
## Base das janelas do jogo (mochila, status...): fundo azul do Sistema, abre/fecha com uma ação e põe o jogo em pausa.

const UI := "res://arte/ui/"

var acao := ""            # ação de entrada que abre/fecha (ex.: "inventario")
var _janela: NinePatchRect


func _criar_janela(pos: Vector2, tam: Vector2) -> void:
	layer = 5
	process_mode = Node.PROCESS_MODE_ALWAYS
	var fundo := ColorRect.new()   # escurece o jogo por trás
	fundo.color = Color(0.08, 0.05, 0.1, 0.55)
	fundo.set_anchors_preset(Control.PRESET_FULL_RECT)
	add_child(fundo)
	_janela = NinePatchRect.new()
	_janela.texture = load(UI + "janela_sistema.png")
	for m in ["patch_margin_left", "patch_margin_right", "patch_margin_top", "patch_margin_bottom"]:
		_janela.set(m, 6)
	_janela.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	_janela.position = pos
	_janela.size = tam
	add_child(_janela)
	visible = false


func _unhandled_input(e: InputEvent) -> void:
	if (acao != "" and acao != "pausa" and e.is_action_pressed(acao)) or (visible and acao != "pausa" and e.is_action_pressed("pausa")):
		if not visible:
			# fecha as outras janelas abertas
			for j in get_tree().get_nodes_in_group("janelas"):
				if j != self and j.visible:
					j.abrir(false)
		abrir(not visible)
		get_viewport().set_input_as_handled()


func abrir(sim: bool) -> void:
	if sim != visible:
		Audio.efeito("abrir_janela" if sim else "fechar_janela", 0.0)
	visible = sim
	get_tree().paused = sim
	if sim:
		_mostrar()


func _mostrar() -> void:
	pass


func _limpar(no: Node) -> void:
	for c in no.get_children():
		c.queue_free()


func _botao(texto: String, cb: Callable = Callable(), pai: Node = null) -> Button:
	var b := Button.new()
	b.text = texto
	b.add_theme_font_size_override("font_size", 14)
	if cb.is_valid():
		b.pressed.connect(cb)
	if pai:
		pai.add_child(b)
	return b


func _texto(pai: Node, pos: Vector2, tam: int, cor := Color.WHITE) -> Label:
	var l := Label.new()
	l.position = pos
	# (a letra em pixel só tem 1× e 2×: os textos de 12–13 passam a 2×, que se lê bem; ver scripts/ui/tema.gd)
	l.add_theme_font_size_override("font_size", 14 if tam >= 12 and tam < 14 else tam)
	l.add_theme_color_override("font_color", cor)
	l.add_theme_color_override("font_outline_color", Color("2e222f"))
	l.add_theme_constant_override("outline_size", 4)
	l.mouse_filter = Control.MOUSE_FILTER_IGNORE
	pai.add_child(l)
	return l


func _icone(caminho: String, tam: float) -> TextureRect:
	var t := TextureRect.new()
	if caminho != "" and ResourceLoader.exists(caminho):
		t.texture = load(caminho)
	t.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	t.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	t.custom_minimum_size = Vector2(tam, tam)
	t.size = Vector2(tam, tam)
	t.mouse_filter = Control.MOUSE_FILTER_IGNORE
	t.size_flags_vertical = Control.SIZE_SHRINK_CENTER
	return t


func _barra_progresso(valor: float, maximo: float, largura: float, cor: Color) -> ProgressBar:
	var b := ProgressBar.new()
	b.custom_minimum_size = Vector2(largura, 8)
	b.max_value = max(1.0, maximo)
	b.value = valor
	b.show_percentage = false
	b.size_flags_vertical = Control.SIZE_SHRINK_CENTER
	var f := StyleBoxFlat.new()
	f.bg_color = cor
	b.add_theme_stylebox_override("fill", f)
	var fundo := StyleBoxFlat.new()
	fundo.bg_color = Color("2e222f")
	b.add_theme_stylebox_override("background", fundo)
	return b
