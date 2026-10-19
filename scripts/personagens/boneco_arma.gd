class_name BonecoArma
extends Node3D
## Corpo do herói + arma, desenhados num SubViewport 2D (docs/PROGRAMACAO.md, secção 4.1) e mostrados
## no mundo num Sprite3D virado para a câmara. A arma roda em 2D por cima (ou por trás) do corpo.

const LADO := 96                      # tamanho do SubViewport (herói 32 px + espaço para armas de 48 px)
const MAO := Vector2(52, 82)          # onde fica a mão (aprox.) no SubViewport

var viewport: SubViewport
var corpo: AnimatedSprite2D
var arma: Sprite2D
var sprite: Sprite3D
var silhueta: Sprite3D
var _rasto: Array[Sprite2D] = []   # cópias da arma nos ângulos de há pouco: o rasto do golpe
var _antes: Array = []             # [ângulo, posição, z] dos últimos quadros
var flip: bool = false:
	set(v):
		flip = v
		if sprite:
			sprite.flip_h = v
		if silhueta:
			silhueta.flip_h = v


func _init(frames: SpriteFrames) -> void:
	viewport = SubViewport.new()
	viewport.size = Vector2i(LADO, LADO)
	viewport.transparent_bg = true
	viewport.disable_3d = true
	viewport.canvas_item_default_texture_filter = Viewport.DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_NEAREST
	viewport.render_target_update_mode = SubViewport.UPDATE_ALWAYS
	add_child(viewport)
	corpo = AnimatedSprite2D.new()
	corpo.sprite_frames = frames
	corpo.position = Vector2(LADO / 2.0, LADO - 16)
	corpo.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	viewport.add_child(corpo)
	arma = Sprite2D.new()
	arma.centered = false
	arma.visible = false
	arma.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	viewport.add_child(arma)
	for i in 3:
		var r := Sprite2D.new()
		r.centered = false
		r.visible = false
		r.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
		r.modulate = Color(1.5, 1.6, 1.8, 0.5 - i * 0.14)
		viewport.add_child(r)
		_rasto.append(r)
	sprite = Sprite3D.new()
	sprite.texture = viewport.get_texture()
	sprite.billboard = BaseMaterial3D.BILLBOARD_FIXED_Y
	sprite.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
	sprite.pixel_size = 1.0 / 16.0
	sprite.shaded = true
	sprite.alpha_cut = SpriteBase3D.ALPHA_CUT_DISCARD
	sprite.offset = Vector2(0, LADO / 2.0)
	add_child(sprite)
	# silhueta: quando o herói fica atrás de rochas ou árvores, vê-se a sombra dele em azul por cima
	silhueta = Sprite3D.new()
	silhueta.texture = sprite.texture
	silhueta.billboard = BaseMaterial3D.BILLBOARD_FIXED_Y
	silhueta.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
	silhueta.pixel_size = sprite.pixel_size
	silhueta.offset = sprite.offset
	silhueta.shaded = false
	silhueta.no_depth_test = true
	silhueta.alpha_cut = SpriteBase3D.ALPHA_CUT_DISABLED
	silhueta.modulate = Color(0.45, 0.6, 1.0, 0.4)
	silhueta.render_priority = -1
	add_child(silhueta)


func tocar(nome: String, velocidade: float = 1.0) -> void:
	if corpo.animation != nome or not corpo.is_playing():
		corpo.play(nome)
	corpo.speed_scale = velocidade


func recomecar(nome: String, velocidade: float = 1.0) -> void:
	corpo.play(nome)
	corpo.frame = 0
	corpo.speed_scale = velocidade


func tem(nome: String) -> bool:
	return corpo.sprite_frames.has_animation(nome)


func por_arma(textura: Texture2D) -> void:
	arma.texture = textura
	if textura:
		arma.offset = Vector2(-textura.get_width() / 2.0, -textura.get_height() + 3)


## Põe a arma na mão: ângulo em graus (0 = para cima, positivo = sentido dos ponteiros), deslocação em píxeis,
## e se fica por trás do corpo (de costas).
func pose_arma(angulo: float, deslocar := Vector2.ZERO, atras: bool = false) -> void:
	arma.visible = arma.texture != null
	arma.rotation_degrees = angulo
	arma.position = MAO + deslocar
	arma.z_index = -1 if atras else 1
	# o rasto: a arma de 2, 4 e 6 quadros atrás, mais clara e transparente, só quando se mexe depressa
	_antes.push_front([angulo, arma.position, arma.z_index])
	if _antes.size() > 7:
		_antes.pop_back()
	for i in _rasto.size():
		var r := _rasto[i]
		var k := 2 + i * 2
		if arma.visible and k < _antes.size() and (absf(_antes[k][0] - angulo) > 14.0 or _antes[k][1].distance_to(arma.position) > 5.0):
			r.texture = arma.texture
			r.offset = arma.offset
			r.rotation_degrees = _antes[k][0]
			r.position = _antes[k][1]
			r.z_index = _antes[k][2]
			r.visible = true
		else:
			r.visible = false


## A arma ao longo de um golpe (p de 0 a 1): prepara (puxa atrás, 0–25%), golpe rápido (25–50%) e acompanha.
## anim: a animação do corpo (ataque_corte, ataque_pesado...); tipo: o tipo de arma (para a besta).
func pose_golpe(anim: String, p: float, atras: bool, tipo: String = "") -> void:
	var prep := clampf(p / 0.25, 0.0, 1.0)
	var g := ease(clampf((p - 0.25) / 0.25, 0.0, 1.0), 0.35)
	match anim:
		"ataque_corte":
			pose_arma(lerpf(lerpf(-60.0, -125.0, prep), 125.0, g), Vector2(0, -4), atras)
		"ataque_pesado":
			pose_arma(lerpf(lerpf(-90.0, -175.0, prep), 110.0, g), Vector2(-2, -6 + 3.0 * g), atras)
		"ataque_estocada":   # a lança agarra-se pelo meio da haste (não pela ponta de trás)
			var meio := arma.texture.get_height() * 0.32 if arma.texture else 0.0
			pose_arma(90.0, Vector2(lerpf(lerpf(0.0, -9.0, prep), 12.0, g) - meio, -5), atras)
		"ataque_disparo":   # o arco/besta recua um pouco ao disparar
			pose_arma(90.0 if tipo == "besta" else 0.0, Vector2(4.0 - 8.0 * g * (1.0 - g), -8), atras)
		"ataque_magia":     # o cajado sobe a carregar e desce a lançar
			pose_arma(lerpf(lerpf(0.0, -40.0, prep), 20.0, g), Vector2(2, -10 - 3.0 * prep * (1.0 - g)), atras)
		_:
			esconder_arma()


func esconder_arma() -> void:
	arma.visible = false
	_antes.clear()
	for r in _rasto:
		r.visible = false


## Um "fantasma" do boneco que fica no sítio e se desvanece (investidas, esquivas rápidas).
func fantasma(cor := Color(0.6, 0.85, 1.0, 0.55)) -> void:
	var img := viewport.get_texture().get_image()
	if img == null or not is_inside_tree():
		return
	var s := Sprite3D.new()
	s.texture = ImageTexture.create_from_image(img)
	s.billboard = sprite.billboard
	s.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
	s.pixel_size = sprite.pixel_size
	s.offset = sprite.offset
	s.flip_h = sprite.flip_h
	s.shaded = false
	s.alpha_cut = SpriteBase3D.ALPHA_CUT_DISABLED
	s.modulate = cor
	get_tree().current_scene.add_child(s)
	s.global_position = global_position
	var t := s.create_tween()
	t.tween_property(s, "modulate:a", 0.0, 0.3)
	t.tween_callback(s.queue_free)
