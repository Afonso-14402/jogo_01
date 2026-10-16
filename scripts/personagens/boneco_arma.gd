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
var flip: bool = false:
	set(v):
		flip = v
		if sprite:
			sprite.flip_h = v


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
	sprite = Sprite3D.new()
	sprite.texture = viewport.get_texture()
	sprite.billboard = BaseMaterial3D.BILLBOARD_FIXED_Y
	sprite.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
	sprite.pixel_size = 1.0 / 16.0
	sprite.shaded = true
	sprite.alpha_cut = SpriteBase3D.ALPHA_CUT_DISCARD
	sprite.offset = Vector2(0, LADO / 2.0)
	add_child(sprite)


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


func esconder_arma() -> void:
	arma.visible = false
