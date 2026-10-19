extends CanvasLayer
## Página do diário do Aren (docs/lore/diario_aren.md): papel amarelado, letra à mão a aparecer como se fosse
## escrita. Tinta castanha, azul (as seis páginas escritas do topo) ou lápis (a 68).

const TINTAS := {"castanha": Color("694f62"), "azul": Color("4d65b4"), "lapis": Color("625565")}

var _papel: ColorRect
var _titulo: Label
var _texto: RichTextLabel
var _a_escrever := false


func _ready() -> void:
	add_to_group("pagina_ui")
	layer = 7
	process_mode = Node.PROCESS_MODE_ALWAYS
	var fundo := ColorRect.new()
	fundo.color = Color(0.08, 0.05, 0.1, 0.6)
	fundo.set_anchors_preset(Control.PRESET_FULL_RECT)
	add_child(fundo)
	var borda := ColorRect.new()
	borda.color = Color("966c6c")
	borda.position = Vector2(326, 36)
	borda.size = Vector2(628, 648)
	add_child(borda)
	_papel = ColorRect.new()
	_papel.color = Color("e3c896")
	_papel.position = Vector2(330, 40)
	_papel.size = Vector2(620, 640)
	add_child(_papel)
	for i in 14:   # manchas e linhas do papel
		var l := ColorRect.new()
		l.color = Color("c7b08b")
		l.position = Vector2(30, 90 + i * 38)
		l.size = Vector2(560, 1)
		_papel.add_child(l)
	_titulo = Label.new()
	_titulo.position = Vector2(30, 24)
	_titulo.add_theme_font_size_override("font_size", 20)
	_titulo.add_theme_color_override("font_color", Color("45293f"))
	_papel.add_child(_titulo)
	_texto = RichTextLabel.new()
	_texto.position = Vector2(30, 70)
	_texto.size = Vector2(560, 540)
	_texto.add_theme_font_size_override("normal_font_size", 16)
	_texto.add_theme_font_size_override("italics_font_size", 16)
	_texto.bbcode_enabled = true
	_texto.mouse_filter = Control.MOUSE_FILTER_IGNORE
	_papel.add_child(_texto)
	var dica := Label.new()
	dica.text = "[E] fechar"
	dica.position = Vector2(520, 612)
	dica.add_theme_color_override("font_color", Color("966c6c"))
	_papel.add_child(dica)
	visible = false


func mostrar(n: int) -> void:
	var p: Dictionary = {}
	for x in Dados.lista_simples("paginas"):
		if int(x.numero) == n:
			p = x
	if p.is_empty():
		return
	visible = true
	get_tree().paused = true
	_titulo.text = "Página %d — %s" % [n, p.titulo]
	_texto.add_theme_color_override("default_color", TINTAS.get(p.get("tinta", "castanha"), TINTAS.castanha))
	_texto.text = "[i]%s[/i]" % String(p.texto).replace("{nome}", Jogo.nome)
	_texto.visible_ratio = 0.0
	_a_escrever = true
	while _a_escrever and _texto.visible_ratio < 1.0:
		await get_tree().process_frame
		_texto.visible_characters += 2   # como se fosse escrito à mão
	_texto.visible_ratio = 1.0
	_a_escrever = false


func _unhandled_input(e: InputEvent) -> void:
	if not visible:
		return
	if e.is_action_pressed("interagir") or e.is_action_pressed("pausa") or e.is_action_pressed("atacar"):
		get_viewport().set_input_as_handled()
		if _a_escrever:
			_a_escrever = false
		else:
			visible = false
			get_tree().paused = false
