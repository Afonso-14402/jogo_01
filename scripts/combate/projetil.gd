class_name Projetil
extends Area3D
## Flecha, virote ou magia: voa em linha reta até "alcance" metros e acerta o primeiro alvo.

signal acertou(alvo: Node, golpe: Dictionary)

var textura: String = "res://arte/efeitos/flecha.png"
var dono: Node
var direcao := Vector3.FORWARD
var velocidade: float = 20.0
var alcance: float = 15.0
var calcular_golpe: Callable
var mascara: int = 1 << 2
var _percorrido: float = 0.0
var _sprite: AnimatedSprite3D


func _ready() -> void:
	collision_layer = 1 << 4
	collision_mask = mascara | 1
	var f := CollisionShape3D.new()
	var s := SphereShape3D.new()
	s.radius = 0.3
	f.shape = s
	add_child(f)
	var tex: Texture2D = load(textura)
	var lado := tex.get_height()
	var sf := SpriteFrames.new()
	sf.set_animation_speed("default", 12)
	for i in range(tex.get_width() / lado):
		var at := AtlasTexture.new()
		at.atlas = tex
		at.region = Rect2(i * lado, 0, lado, lado)
		sf.add_frame("default", at)
	_sprite = AnimatedSprite3D.new()
	_sprite.sprite_frames = sf
	_sprite.billboard = BaseMaterial3D.BILLBOARD_ENABLED
	_sprite.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
	_sprite.pixel_size = 1.0 / 16.0
	_sprite.shaded = false
	_sprite.flip_h = direcao.x < 0.0
	add_child(_sprite)
	_sprite.play("default")
	area_entered.connect(_area)
	body_entered.connect(_corpo)


func _physics_process(delta: float) -> void:
	var passo := velocidade * delta
	global_position += direcao * passo
	_percorrido += passo
	if _percorrido >= alcance:
		queue_free()


func _area(area: Area3D) -> void:
	if not area is Hurtbox or area.dono == dono:
		return
	var alvo: Node = area.dono
	var golpe: Dictionary = calcular_golpe.call(alvo)
	golpe["origem"] = global_position - direcao
	golpe["atacante"] = dono
	if alvo.has_method("receber_golpe"):
		alvo.receber_golpe(golpe)
	acertou.emit(alvo, golpe)
	queue_free()


func _corpo(corpo: Node) -> void:
	if corpo is StaticBody3D:   # bate numa parede ou numa árvore
		queue_free()
