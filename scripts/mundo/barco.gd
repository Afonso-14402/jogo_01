class_name Barco
extends Node3D
## O barco do oceano (`JJ` nos mapas; docs/SISTEMAS.md 2.5): E ao pé dele para entrar; o herói leva-o pela água funda
## (Jogador.entrar_barco / sair_barco). Balança na água (2 quadros).

var sprite: AnimatedSprite3D
var inter: Interagivel


func _ready() -> void:
	add_to_group("barcos")
	var tex: Texture2D = load("res://arte/objetos/barco.png")
	var sf := SpriteFrames.new()
	sf.set_animation_speed("default", 2.0)
	for i in 2:
		var at := AtlasTexture.new()
		at.atlas = tex
		at.region = Rect2(i * 40, 0, 40, 24)
		sf.add_frame("default", at)
	sprite = AnimatedSprite3D.new()
	sprite.sprite_frames = sf
	sprite.billboard = BaseMaterial3D.BILLBOARD_FIXED_Y
	sprite.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
	sprite.pixel_size = 1.0 / 16.0
	sprite.alpha_cut = SpriteBase3D.ALPHA_CUT_DISCARD
	sprite.offset = Vector2(0, 8)
	add_child(sprite)
	sprite.play("default")
	inter = Interagivel.new()
	inter.texto = "Entrar no barco"
	add_child(inter)
	inter.usado.connect(func(j): if j.has_method("entrar_barco"): j.entrar_barco(self))
