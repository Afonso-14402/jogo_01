class_name EfeitosCombate
extends RefCounted
## Números de dano, piscar a branco, hitstop e efeitos de impacto (docs/SISTEMAS.md, secção 4.4).

const CORES := {"normal": Color.WHITE, "critico": Color("f9c22b"), "magia": Color("8fd3ff"), "cura": Color("91db69"),
	"veneno": Color("a884f3"), "imune": Color("9babb2"), "jogador": Color("e83b3b"), "texto": Color("8fd3ff")}
static var _hitstop_ativo: bool = false


static func numero(arvore: SceneTree, posicao: Vector3, texto: String, tipo: String = "normal") -> void:
	if not Opcoes.v("numeros_dano") and texto.is_valid_int():
		return
	var l := Label3D.new()
	l.text = texto
	l.billboard = BaseMaterial3D.BILLBOARD_ENABLED
	l.no_depth_test = true
	l.fixed_size = true
	l.pixel_size = {"critico": 0.003, "texto": 0.0013}.get(tipo, 0.0022)
	l.font_size = 28
	l.outline_size = 8
	l.modulate = Color(tipo) if tipo.begins_with("#") else CORES.get(tipo, Color.WHITE)
	l.outline_modulate = Color("2e222f")
	l.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
	arvore.current_scene.add_child(l)
	l.global_position = posicao + Vector3(randf_range(-0.3, 0.3), 1.8, 0)
	var t := l.create_tween().set_parallel()
	t.tween_property(l, "global_position:y", l.global_position.y + 0.9, 0.7).set_ease(Tween.EASE_OUT).set_trans(Tween.TRANS_QUAD)
	t.tween_property(l, "modulate:a", 0.0, 0.3).set_delay(0.45)
	t.chain().tween_callback(l.queue_free)


## Pisca a branco: o sprite fica "aceso" por instantes (cores ×8 ficam brancas).
static func piscar(sprite: GeometryInstance3D, duracao: float = 0.1) -> void:
	if not is_instance_valid(sprite):
		return
	var sombreado: bool = sprite.shaded
	sprite.shaded = false
	sprite.modulate = Color(8, 8, 8)
	var t := sprite.create_tween()
	t.tween_interval(duracao)
	t.tween_callback(func():
		if is_instance_valid(sprite):
			sprite.modulate = Color.WHITE
			sprite.shaded = sombreado)


## Congela o jogo por instantes para o golpe "pesar".
static func hitstop(arvore: SceneTree, duracao: float) -> void:
	if _hitstop_ativo:
		return
	_hitstop_ativo = true
	Engine.time_scale = 0.05
	await arvore.create_timer(duracao, true, false, true).timeout
	Engine.time_scale = 1.0
	_hitstop_ativo = false


## Um efeito animado de arte/efeitos (tira de frames) no mundo, que se apaga sozinho.
## escala: 1, 2, 3... (inteira, para os píxeis ficarem certos): para as ondas das skills de área grandes.
static func animado(arvore: SceneTree, nome: String, posicao: Vector3, fps: float = 18.0, espelhar: bool = false, escala: float = 1.0) -> void:
	var caminho := "res://arte/efeitos/%s.png" % nome
	if not ResourceLoader.exists(caminho):
		return
	var tex: Texture2D = load(caminho)
	var lado := tex.get_height()
	var sf := SpriteFrames.new()
	sf.set_animation_loop("default", false)
	sf.set_animation_speed("default", fps)
	for i in range(tex.get_width() / lado):
		var at := AtlasTexture.new()
		at.atlas = tex
		at.region = Rect2(i * lado, 0, lado, lado)
		sf.add_frame("default", at)
	var s := AnimatedSprite3D.new()
	s.sprite_frames = sf
	s.billboard = BaseMaterial3D.BILLBOARD_ENABLED
	s.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
	s.pixel_size = 1.0 / 16.0
	s.shaded = false
	s.no_depth_test = true
	s.render_priority = 10
	s.flip_h = espelhar
	s.scale = Vector3.ONE * escala
	arvore.current_scene.add_child(s)
	s.global_position = posicao
	s.play("default")
	s.animation_finished.connect(s.queue_free)
