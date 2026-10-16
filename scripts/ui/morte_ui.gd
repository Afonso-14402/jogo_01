extends CanvasLayer
## Ecrã de morte (docs/INTERFACE.md, secção 5): o ecrã escurece, a mensagem do Sistema, a lista do que perdeste
## e o botão "Acordar".

signal _acordar

var _fundo: ColorRect
var _texto: Label
var _botao: Button


func _ready() -> void:
	add_to_group("morte_ui")
	layer = 8
	process_mode = Node.PROCESS_MODE_ALWAYS
	_fundo = ColorRect.new()
	_fundo.color = Color(0.05, 0.03, 0.06, 0.0)
	_fundo.set_anchors_preset(Control.PRESET_FULL_RECT)
	add_child(_fundo)
	_texto = Label.new()
	_texto.position = Vector2(240, 220)
	_texto.size = Vector2(800, 260)
	_texto.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	_texto.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	_texto.add_theme_font_size_override("font_size", 20)
	_texto.add_theme_color_override("font_color", Color("8fd3ff"))
	add_child(_texto)
	_botao = Button.new()
	_botao.text = "Acordar"
	_botao.position = Vector2(560, 500)
	_botao.custom_minimum_size = Vector2(160, 44)
	_botao.pressed.connect(func(): _acordar.emit())
	add_child(_botao)
	visible = false


func mostrar(perdidos: Array) -> void:
	visible = true
	_botao.visible = false
	var t := create_tween()
	t.tween_property(_fundo, "color:a", 0.92, 1.0)
	var linhas := ["[Sistema] Os teus pontos de vida chegaram a zero."]
	if perdidos.is_empty():
		linhas.append("Não perdeste nada.")
	else:
		linhas.append("Perdeste pelo caminho:")
		for p in perdidos:
			linhas.append("%s ×%d" % [Inventario._dados(p[0]).get("nome_pt", p[0]), int(p[1])])
	if Jogo.dificuldade == "hardcore":
		linhas.append("\nModo Hardcore: a aventura acaba aqui.")
	_texto.text = "\n".join(linhas)
	await t.finished
	_botao.text = "Voltar ao menu" if Jogo.dificuldade == "hardcore" else "Acordar"
	_botao.visible = true
	_botao.grab_focus()
	await _acordar
	visible = false
	_fundo.color.a = 0.0
