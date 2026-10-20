extends CanvasLayer
## Controlos de toque (docs/INTERFACE.md, secção 2 "Telemóvel"): joystick à esquerda (onde tocares), botão de ataque
## grande à direita, esquiva, 4 skills, poção, "Usar" (só quando há algo para interagir), pausa e mochila.
## Os botões são TouchScreenButton ligados às ações; o joystick carrega nas ações de mover com a força certa.
## Opções: tamanho e transparência dos botões, modo canhoto (inverte os lados).

const UI := "res://arte/ui/"
const ZONA_MORTA := 0.2

var _base: Sprite2D
var _bola: Sprite2D
var _toque_joystick := -1
var _centro := Vector2.ZERO
var _raio := 70.0
var _usar: TouchScreenButton
var _botoes: Array = []


func _ready() -> void:
	layer = 4
	process_mode = Node.PROCESS_MODE_ALWAYS
	_base = Sprite2D.new()
	_base.texture = load(UI + "toque_joystick_base.png")
	_base.scale = Vector2(3, 3)
	_base.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	_base.visible = false
	add_child(_base)
	_bola = Sprite2D.new()
	_bola.texture = load(UI + "toque_joystick_bola.png")
	_bola.scale = Vector2(3, 3)
	_bola.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	_bola.visible = false
	add_child(_bola)
	var esc := float(Opcoes.v("botoes_tamanho") if Opcoes.v("botoes_tamanho") != null else 1.0)
	var canhoto: bool = Opcoes.v("canhoto") == true
	var x0 := 1280.0
	# [ação, textura, posição (a contar da direita), tamanho]
	for b in [["atacar", "toque_atacar.png", Vector2(150, 190), 3.0], ["esquivar", "toque_botao.png", Vector2(70, 110), 2.6],
			["skill_1", "toque_botao.png", Vector2(250, 300), 2.2], ["skill_2", "toque_botao.png", Vector2(170, 330), 2.2],
			["skill_3", "toque_botao.png", Vector2(260, 220), 2.2], ["skill_4", "toque_botao.png", Vector2(90, 330), 2.2],
			["pocao", "toque_botao.png", Vector2(340, 180), 2.2], ["interagir", "toque_botao.png", Vector2(300, 100), 2.6],
			["ataque_forte", "toque_botao.png", Vector2(60, 240), 2.2]]:
		var t := TouchScreenButton.new()
		t.texture_normal = load(UI + b[1])
		t.action = b[0]
		t.scale = Vector2(b[3], b[3]) * esc
		var tam: Vector2 = t.texture_normal.get_size() * t.scale
		var px: float = b[2].x if canhoto else x0 - b[2].x - tam.x
		t.position = Vector2(px, 720 - b[2].y - tam.y * 0.5)
		t.modulate.a = float(Opcoes.v("botoes_alfa") if Opcoes.v("botoes_alfa") != null else 0.75)
		t.visibility_mode = TouchScreenButton.VISIBILITY_ALWAYS
		add_child(t)
		var l := Label.new()
		l.text = {"atacar": "⚔", "esquivar": "»", "pocao": "Q", "interagir": "Usar", "ataque_forte": "!!"}.get(b[0], String(b[0]).right(1))
		l.position = tam / t.scale * 0.5 - Vector2(8, 12)
		l.add_theme_font_size_override("font_size", 10)
		t.add_child(l)
		_botoes.append(t)
		if b[0] == "interagir":
			_usar = t
	# a pausa fica logo à direita do quadro do herói (no canto tapava o retrato), dos dois lados
	for b in [["pausa", Vector2(324, 16), "II"], ["inventario", Vector2(20, 600), ""]]:
		var t := TouchScreenButton.new()
		t.texture_normal = load(UI + "toque_botao.png")
		t.action = b[0]
		t.scale = Vector2(2, 2)
		t.position = b[1] if not canhoto or b[0] == "pausa" else Vector2(1280 - b[1].x - 48, b[1].y)
		add_child(t)
		if b[0] == "inventario":   # o ícone da mochila (a letra do jogo não tem emojis)
			var ic := Sprite2D.new()
			ic.texture = load("res://arte/icones/mochila_couro.png")
			ic.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
			ic.position = t.texture_normal.get_size() * 0.5
			t.add_child(ic)
		else:
			var l := Label.new()
			l.text = b[2]
			l.position = Vector2(4, 2)
			l.add_theme_font_size_override("font_size", 9)
			t.add_child(l)
		_botoes.append(t)
	_mostrar(Entrada.e_telemovel())
	Entrada.dispositivo_mudou.connect(func(_t): _mostrar(Entrada.e_telemovel()))


func _mostrar(sim: bool) -> void:
	visible = sim
	for b in _botoes:
		b.visible = sim


func _process(_delta: float) -> void:
	if not visible:
		return
	var j := get_tree().get_first_node_in_group("jogador")
	if _usar:
		_usar.visible = j != null and j.interagivel_perto != null


## O joystick aparece onde tocares na metade esquerda (direita no modo canhoto).
func _input(e: InputEvent) -> void:
	if not visible:
		return
	var canhoto: bool = Opcoes.v("canhoto") == true
	if e is InputEventScreenTouch:
		var lado_certo: bool = (e.position.x > 640.0) if canhoto else (e.position.x < 640.0)
		if e.pressed and _toque_joystick < 0 and lado_certo and e.position.y > 120:
			_toque_joystick = e.index
			_centro = e.position
			_base.position = _centro
			_bola.position = _centro
			_base.visible = true
			_bola.visible = true
		elif not e.pressed and e.index == _toque_joystick:
			_toque_joystick = -1
			_base.visible = false
			_bola.visible = false
			_mover(Vector2.ZERO)
	elif e is InputEventScreenDrag and e.index == _toque_joystick:
		var d: Vector2 = (e.position - _centro).limit_length(_raio)
		_bola.position = _centro + d
		_mover(d / _raio)


func _mover(v: Vector2) -> void:
	if v.length() < ZONA_MORTA:
		v = Vector2.ZERO
	for par in [["mover_direita", maxf(0.0, v.x)], ["mover_esquerda", maxf(0.0, -v.x)], ["mover_baixo", maxf(0.0, v.y)], ["mover_cima", maxf(0.0, -v.y)]]:
		if par[1] > 0.0:
			Input.action_press(par[0], par[1])
		else:
			Input.action_release(par[0])
