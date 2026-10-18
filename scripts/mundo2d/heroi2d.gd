class_name Heroi2D
extends CharacterBody2D
## O herói na versão 2D (docs/PROGRAMACAO.md, secção 4A): anda nas 4 direções com as mesmas animações do
## herói (baixo, cima, lado; a esquerda é o lado espelhado) e corre. A posição é o sítio dos pés no chão
## (1 m = 16 px); o boneco sobe no ecrã com a altura do chão onde está (colinas).
## (Fase D1: só andar. O combate, as skills e o resto vêm na Fase D2.)

const ANIMS := {"parado": [5, true], "andar": [10, true]}

var recargas_skill: Dictionary = {}       # (o HUD lê estes três, como no herói 3D)
var arma: Dictionary = {}
var interagivel_perto = null
var mundo: Node   # o andar 2D (para saber a altura do chão e se se pode passar)
var direcao_olhar := Vector2(0, 1)
var sprite: AnimatedSprite2D
var camara: Camera2D
var _altura_vista: float = 0.0


func _ready() -> void:
	add_to_group("jogador")
	collision_layer = 1 << 1
	collision_mask = 1
	var forma := CollisionShape2D.new()
	var c := CircleShape2D.new()
	c.radius = 0.32 * Chao2D.PX
	forma.shape = c
	add_child(forma)
	add_child(Sombra2D.criar(0.45))
	var sf := Aparencia.frames(Jogo.aparencia, ANIMS, ["baixo", "cima", "lado"]) if Jogo.aparencia.get("penteado", "") != "" else null
	if sf == null or sf.get_animation_names().is_empty():
		sf = Folhas.criar("res://arte/heroi/heroi", ANIMS, ["baixo", "cima", "lado"])
	sprite = AnimatedSprite2D.new()
	sprite.sprite_frames = sf
	sprite.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	sprite.offset = Vector2(0, -16)   # quadros de 32×32 com os pés em baixo ao centro
	add_child(sprite)
	camara = Camera2D.new()
	camara.zoom = Vector2(3, 3)
	camara.position_smoothing_enabled = true
	camara.position_smoothing_speed = 8.0
	add_child(camara)
	_tocar("parado")


func _physics_process(delta: float) -> void:
	var d := Entrada.direcao()
	var correr := Input.is_action_pressed("correr") and d != Vector2.ZERO
	var v := Jogo.velocidade() * (float(Dados.c("correr_mult")) if correr else 1.0) * Chao2D.PX
	var antes := global_position
	velocity = d * v
	move_and_slide()
	# não se sobe nem se desce a pique (paredes e colinas altas): volta atrás nesse eixo
	if mundo and mundo.has_method("pode_passar") and not mundo.pode_passar(antes, global_position):
		var so_x := Vector2(global_position.x, antes.y)
		var so_y := Vector2(antes.x, global_position.y)
		if mundo.pode_passar(antes, so_x):
			global_position = so_x
		elif mundo.pode_passar(antes, so_y):
			global_position = so_y
		else:
			global_position = antes
	if d != Vector2.ZERO:
		direcao_olhar = d.normalized()
		_tocar("andar", 1.4 if correr else 1.0)
	else:
		_tocar("parado")
	# o boneco sobe com o chão (suave, para não dar saltos nos degraus)
	var h: float = mundo.altura_px(global_position) if mundo and mundo.has_method("altura_px") else 0.0
	_altura_vista = lerpf(_altura_vista, h, clampf(14.0 * delta, 0.0, 1.0))
	sprite.position.y = -_altura_vista
	camara.position.y = -_altura_vista


func altura_vista() -> float:
	return _altura_vista


func _tocar(nome: String, velocidade: float = 1.0) -> void:
	var dir := "lado" if absf(direcao_olhar.x) > absf(direcao_olhar.y) * 1.1 else ("cima" if direcao_olhar.y < 0.0 else "baixo")
	sprite.flip_h = dir == "lado" and direcao_olhar.x < 0.0
	var a := "%s_%s" % [nome, dir]
	if sprite.sprite_frames.has_animation(a) and sprite.animation != a:
		sprite.play(a)
	sprite.speed_scale = velocidade
