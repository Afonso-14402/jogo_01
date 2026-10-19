class_name Folhas
extends RefCounted
## Transforma as tiras de animação (PNG com N frames quadrados lado a lado) em SpriteFrames.

static var _cache: Dictionary = {}


## prefixo: ex. "res://arte/heroi/heroi"  →  heroi_<anim>_<dir>.png
## anims: {nome: [fps, repetir]}  ·  dirs: ex. ["baixo", "cima", "lado"] ou ["lado"]
static func criar(prefixo: String, anims: Dictionary, dirs: Array) -> SpriteFrames:
	var chave := prefixo + str(anims.keys()) + str(dirs)
	if _cache.has(chave):
		return _cache[chave]
	var sf := SpriteFrames.new()
	sf.remove_animation("default")
	for nome in anims:
		for d in dirs:
			var caminho := "%s_%s_%s.png" % [prefixo, nome, d]
			if not ResourceLoader.exists(caminho):
				continue
			var tex: Texture2D = load(caminho)
			var lado := tex.get_height()
			var a := "%s_%s" % [nome, d]
			sf.add_animation(a)
			sf.set_animation_speed(a, anims[nome][0])
			sf.set_animation_loop(a, anims[nome][1])
			for i in range(tex.get_width() / lado):
				var at := AtlasTexture.new()
				at.atlas = tex
				at.region = Rect2(i * lado, 0, lado, lado)
				sf.add_frame(a, at)
	_cache[chave] = sf
	return sf


## Um AnimatedSprite3D pronto para pixel art: billboard, nítido, pés no chão, 16 px = 1 m.
static func boneco(sf: SpriteFrames, tamanho_px: int = 32) -> AnimatedSprite3D:
	var s := AnimatedSprite3D.new()
	s.sprite_frames = sf
	s.billboard = BaseMaterial3D.BILLBOARD_FIXED_Y
	s.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
	s.pixel_size = 1.0 / float(Dados.c("pixeis_por_metro", 16))
	s.shaded = true
	s.alpha_cut = SpriteBase3D.ALPHA_CUT_DISCARD
	s.offset = Vector2(0, tamanho_px / 2.0)
	return s


## Sombra redonda no chão (fica melhor do que a sombra real do sprite).
static func sombra(raio: float = 0.4) -> MeshInstance3D:
	var m := MeshInstance3D.new()
	var plano := PlaneMesh.new()
	plano.size = Vector2(raio * 2.0, raio * 1.4)
	m.mesh = plano
	var g := Gradient.new()
	g.set_color(0, Color(0.18, 0.13, 0.18, 0.55))
	g.set_color(1, Color(0.18, 0.13, 0.18, 0.0))
	var tex := GradientTexture2D.new()
	tex.gradient = g
	tex.fill = GradientTexture2D.FILL_RADIAL
	tex.fill_from = Vector2(0.5, 0.5)
	tex.fill_to = Vector2(1.0, 0.5)
	var mat := StandardMaterial3D.new()
	mat.albedo_texture = tex
	mat.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
	mat.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	m.material_override = mat
	m.position.y = 0.02
	m.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
	return m
