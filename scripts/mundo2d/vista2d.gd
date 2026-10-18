class_name Vista2D
extends Node2D
## A VISTA 2D do jogo (OBJETIVO.md, Fase D; docs/PROGRAMACAO.md, secção 4A).
##
## As contas do jogo (física, combate, monstros, puzzles, povoações, masmorras, cidade) continuam a fazer-se no
## plano (x, z), em metros, como sempre. Esta vista desenha TUDO em 2D, sem perspetiva: o chão em pixel art
## (Chao2D), e por cada coisa do mundo um "espelho" 2D no sítio certo:
##   AnimatedSprite3D / Sprite3D → AnimatedSprite2D / Sprite2D (as mesmas folhas de animação)
##   Label3D                    → Label (números de dano, nomes, placas)
##   peças .glb                 → a fotografia delas em pixel art (arte/sprites2d, ferramentas/arte/glb_sprites.gd)
##   plantas (MultiMesh)        → um Sprite2D por planta
##   caixas, planos, cilindros  → o topo e o lado de frente desenhados em 2D (paredes das masmorras, avisos...)
##   OmniLight3D                → PointLight2D; a luz do sol → a cor da hora (CanvasModulate)
## A projeção: o ponto (x, y, z) fica no ecrã em (x, z − 0,8·y) × 16 px. A ordem de desenho é pelo z (y-sort):
## o que está mais à frente (mais a sul) desenha-se por cima. A câmara 3D continua a existir (para as contas),
## mas não desenha nada.

const PX := 16.0
const SOBE := 0.8
const ZOOM := {13.0: 4.0, 19.0: 3.0, 99.0: 2.0}   # distância da câmara 3D (zoom do jogador) → zoom 2D

static var atual: Vista2D

var cena: Node            # Andar ou Cidade (a cena 3D por baixo)
var mundo: Node2D         # o nó com y-sort onde fica tudo
var camara: Camera2D
var _proxies: Array = []   # [{fonte, no, tipo, ...}]
var _vistos: Dictionary = {}   # instance_id da fonte → true
var _novos: Array = []
var _shader_janela: Shader
var _shader_agua: Shader
var _mats: Dictionary = {}
var _sprites: Dictionary = {}   # dados/sprites2d.json
var _luz_dia: CanvasModulate
var _t_estatico := 0.0
var _chuva: CPUParticles2D


static func ligada() -> bool:
	return bool(Opcoes.v("vista_2d"))


func _ready() -> void:
	atual = self
	cena = get_parent()
	_sprites = JSON.parse_string(FileAccess.get_file_as_string("res://dados/sprites2d.json")) if FileAccess.file_exists("res://dados/sprites2d.json") else {}
	if _sprites == null:
		_sprites = {}
	mundo = Node2D.new()
	mundo.name = "Mundo2D"
	mundo.y_sort_enabled = true
	add_child(mundo)
	camara = Camera2D.new()
	camara.zoom = Vector2(3, 3)
	camara.position_smoothing_enabled = true
	camara.position_smoothing_speed = 8.0
	add_child(camara)
	camara.make_current()
	_luz_dia = CanvasModulate.new()
	add_child(_luz_dia)
	var c3 := get_viewport().get_camera_3d()
	if c3:
		c3.cull_mask = 0   # a câmara 3D só serve para as contas: não desenha nada
	_chao()
	_varrer(cena)
	_luzes_gruta()
	get_tree().node_added.connect(_no_novo)
	_camara(true)


func _exit_tree() -> void:
	if atual == self:
		atual = null
	if get_tree().node_added.is_connected(_no_novo):
		get_tree().node_added.disconnect(_no_novo)


# ------------------------------------------------------------------ projeção ------------------------------------------------------------------

## Um ponto do mundo 3D (metros) → o sítio do chão no ecrã 2D (px) e quanto sobe pela altura.
static func chao_px(p: Vector3) -> Vector2:
	return Vector2(p.x, p.z) * PX


static func sobe_px(p: Vector3) -> float:
	return p.y * SOBE * PX


static func ecra(p: Vector3) -> Vector2:
	return Vector2(p.x * PX, (p.z - p.y * SOBE) * PX)


## O sítio do mundo (no plano à altura y) que fica debaixo do rato.
func rato_no_mundo(altura: float) -> Vector3:
	var m := get_global_mouse_position()
	return Vector3(m.x / PX, altura, m.y / PX + altura * SOBE)


# ------------------------------------------------------------------ chão ------------------------------------------------------------------

func _chao() -> void:
	if cena is Andar:
		var a: Andar = cena
		var bw := a.largura * Andar.POR_CEL
		var bh := a.altura_cel * Andar.POR_CEL
		var agua := PackedByteArray()
		agua.resize(bw * bh)
		var alt := a._alturas.duplicate()
		for bz in bh:
			for bx in bw:
				var c := a.codigo(bx / Andar.POR_CEL, bz / Andar.POR_CEL)
				agua[bz * bw + bx] = 1 if c in ["~~", "ww", ",,"] else 0
				if c == "%%":   # lama: um pouco abaixo, com cor de lama (a água do shader pinta-a)
					agua[bz * bw + bx] = 1
		var origem := Vector2(-a.largura * Andar.CEL / 2.0, -a.altura_cel * Andar.CEL / 2.0)
		var cor_agua := Color(a.kit.get("agua", "#0b8a8f")) if String(a.kit.get("agua", "")).begins_with("#") else Color("0b8a8f")
		var mat := Chao2D.material(a.regiao, a._splat, a._alturas_img, a._mascara_agua, origem,
				Vector2(a.largura * Andar.CEL, a.altura_cel * Andar.CEL), cor_agua, a.altura_rocha())
		_por_chao(Chao2D.filas(alt, agua, bw, bh, origem, Andar.BLOCO, mat))
		RenderingServer.set_default_clear_color(Color("1c2a2a") if a.regiao != 2 else Color("120e16"))
	elif cena.has_method("chao_2d"):
		_por_chao(cena.chao_2d())


var _chao_baixo: Node2D


## O chão plano vai para uma camada por baixo de tudo; as colinas e paredes entram no y-sort do mundo.
func _por_chao(filas: Array) -> void:
	if _chao_baixo == null:
		_chao_baixo = Node2D.new()
		_chao_baixo.name = "ChaoBaixo"
		_chao_baixo.z_index = -10
		add_child(_chao_baixo)
		move_child(_chao_baixo, 0)
	for par in filas:
		if par[1]:
			mundo.add_child(par[0])
		else:
			_chao_baixo.add_child(par[0])


# ------------------------------------------------------------------ espelhos ------------------------------------------------------------------

func _no_novo(n: Node) -> void:
	if n is Node3D and cena.is_ancestor_of(n):
		_novos.append(n)


func _varrer(n: Node) -> void:
	if not _espelhar(n):
		return
	for f in n.get_children():
		_varrer(f)


## Cria o espelho 2D de um nó 3D; devolve false se os filhos já ficam incluídos (peças .glb) ou não interessam.
func _espelhar(n: Node) -> bool:
	if not n is Node3D or _vistos.has(n.get_instance_id()):
		return not n is Node3D or not _vistos.has(n.get_instance_id())
	if n is CanvasItem:
		return false
	_vistos[n.get_instance_id()] = true
	var n3 := n as Node3D
	if n3.scene_file_path.ends_with(".glb"):
		_peca(n3, n3.scene_file_path, n3.global_transform)
		return false
	if n is AnimatedSprite3D:
		_sprite_animado(n)
	elif n is Sprite3D:
		_sprite(n)
	elif n is Label3D:
		_rotulo(n)
	elif n is MultiMeshInstance3D:
		_multimesh(n)
	elif n is MeshInstance3D:
		_malha(n)
	elif n is OmniLight3D:
		_luz(n)
	elif n is CPUParticles3D:
		_particulas(n)
	return true


func _novo_no(fonte: Node3D, tipo: String, estatico: bool = false) -> Node2D:
	var base := Node2D.new()
	mundo.add_child(base)
	_proxies.append({"fonte": fonte, "no": base, "tipo": tipo, "estatico": estatico})
	return base


func _posicionar(base: Node2D, fonte: Node3D, alvo: CanvasItem) -> void:
	var p := fonte.global_position
	base.position = chao_px(p)
	(alvo as Node2D).position.y = -sobe_px(p)


# --- sprites ---

func _sprite_animado(s: AnimatedSprite3D) -> void:
	if s.no_depth_test and s.render_priority < 0:   # a silhueta do herói atrás das coisas: em 2D não faz falta
		return
	var base := _novo_no(s, "animado")
	var a := AnimatedSprite2D.new()
	a.sprite_frames = s.sprite_frames
	a.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	base.add_child(a)
	if s.no_depth_test:
		base.z_index = 40
	_atualizar_animado(s, a, base)


func _atualizar_animado(s: AnimatedSprite3D, a: AnimatedSprite2D, base: Node2D) -> void:
	_posicionar(base, s, a)
	if a.sprite_frames != s.sprite_frames:
		a.sprite_frames = s.sprite_frames
	if a.animation != s.animation:
		a.animation = s.animation
	a.frame = s.frame
	a.flip_h = s.flip_h
	a.modulate = s.modulate
	a.visible = s.is_visible_in_tree()
	var k := s.pixel_size * PX
	var gs := s.global_basis.get_scale()
	a.scale = Vector2(k * gs.x * s.scale.x / maxf(0.001, s.scale.x), k * gs.y) if false else Vector2(k * gs.x, k * gs.y)
	a.centered = s.centered
	a.offset = Vector2(s.offset.x, -s.offset.y)


func _sprite(s: Sprite3D) -> void:
	if s.no_depth_test and s.render_priority < 0:
		return
	var base := _novo_no(s, "sprite")
	var a := Sprite2D.new()
	a.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	base.add_child(a)
	if s.no_depth_test:
		base.z_index = 40
	_atualizar_sprite(s, a, base)


func _atualizar_sprite(s: Sprite3D, a: Sprite2D, base: Node2D) -> void:
	_posicionar(base, s, a)
	a.texture = s.texture
	a.hframes = s.hframes
	a.vframes = s.vframes
	a.frame = s.frame
	a.region_enabled = s.region_enabled
	a.region_rect = s.region_rect
	a.flip_h = s.flip_h
	a.flip_v = s.flip_v
	a.modulate = s.modulate
	a.visible = s.is_visible_in_tree() and s.texture != null
	var k := s.pixel_size * PX
	var gs := s.global_basis.get_scale()
	a.scale = Vector2(k * gs.x, k * gs.y)
	a.centered = s.centered
	a.offset = Vector2(s.offset.x, -s.offset.y)


# --- textos ---

func _rotulo(l: Label3D) -> void:
	var base := _novo_no(l, "rotulo")
	var t := Label.new()
	var ls := LabelSettings.new()
	t.label_settings = ls
	t.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	t.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
	t.mouse_filter = Control.MOUSE_FILTER_IGNORE
	base.add_child(t)
	base.z_index = 45
	_atualizar_rotulo(l, t, base)


func _atualizar_rotulo(l: Label3D, t: Label, base: Node2D) -> void:
	var p := l.global_position
	base.position = chao_px(p)
	var ls := t.label_settings
	# tamanho no mundo 2D (px): os fixos (números de dano, o "olho") ficam pequenos e legíveis
	var mundo_px: float = clampf(l.font_size * l.pixel_size * PX, 5.0, 14.0) if not l.fixed_size else clampf(l.font_size * l.pixel_size * 120.0, 6.0, 12.0)
	ls.font_size = int(mundo_px * 3.0)
	ls.font_color = l.modulate
	ls.outline_size = int(l.outline_size * 0.6) + 2
	ls.outline_color = l.outline_modulate
	t.text = l.text
	t.scale = Vector2.ONE / 3.0
	t.size = Vector2.ZERO
	t.reset_size()
	t.position = Vector2(-t.size.x / 6.0, -sobe_px(p) - t.size.y / 6.0)
	t.visible = l.is_visible_in_tree() and l.modulate.a > 0.02


# --- peças .glb (fotografadas em arte/sprites2d) ---

func _textura_peca(caminho: String, rot_y: float) -> Array:
	var e: Dictionary = _sprites.get(caminho, {})
	if e.is_empty():
		return []
	var r := int(posmod(int(round(rot_y / (PI / 2.0))), 4))
	var chave := "r%d" % r
	var flip := false
	if not e.has(chave):
		chave = "r0"
		flip = r % 2 == 1
	var png := "res://arte/sprites2d/" + caminho.trim_prefix("res://arte/").trim_suffix(".glb") + "_%s.png" % chave
	if not ResourceLoader.exists(png):
		return []
	var info: Array = e[chave]
	return [load(png), Vector2(float(info[2]), float(info[3])), flip]


func _peca(fonte: Node3D, caminho: String, t: Transform3D, estatico: bool = false) -> Node2D:
	var tx := _textura_peca(caminho, t.basis.get_euler().y)
	if tx.is_empty():
		return null
	var base := _novo_no(fonte, "peca", estatico)
	var s := Sprite2D.new()
	s.texture = tx[0]
	s.centered = false
	s.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	var esc := t.basis.get_scale()
	s.scale = Vector2(esc.x * (-1.0 if tx[2] else 1.0), esc.y)
	s.offset = -tx[1]
	if tx[2]:   # espelhado: a âncora fica do outro lado
		s.offset.x = -(float(tx[0].get_width()) - tx[1].x)
	if tx[0].get_height() > 40:
		s.material = _material_janela()
	base.add_child(s)
	base.set_meta("t", t)
	_por_peca(base, s, t)
	return base


func _por_peca(base: Node2D, s: Sprite2D, t: Transform3D) -> void:
	base.position = chao_px(t.origin)
	s.position = Vector2(0, -sobe_px(t.origin))


# --- plantas e peças repetidas (MultiMesh) ---

func _multimesh(mi: MultiMeshInstance3D) -> void:
	var mm := mi.multimesh
	if mm == null or mm.mesh == null:
		return
	var mat: Material = mi.material_override if mi.material_override else mm.mesh.surface_get_material(0)
	if _e_chao(mat) or mi.has_meta("chao"):
		return
	if mat is ShaderMaterial and (mat as ShaderMaterial).shader == Natureza._shader_planta:
		var tex: Texture2D = (mat as ShaderMaterial).get_shader_parameter("tex")
		var mat2 := _material_planta(mat as ShaderMaterial, tex)
		for i in mm.instance_count:
			var t := mi.global_transform * mm.get_instance_transform(i)
			var base := Node2D.new()
			base.position = chao_px(t.origin)
			var s := Sprite2D.new()
			s.texture = tex
			s.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
			s.offset = Vector2(0, -tex.get_height() / 2.0)
			var esc := t.basis.get_scale()
			s.scale = Vector2(esc.x * (-1.0 if t.basis.x.x < 0.0 else 1.0), esc.y)
			s.position.y = -sobe_px(t.origin)
			s.material = mat2
			base.add_child(s)
			mundo.add_child(base)
		return
	if mi.has_meta("glb"):
		if int(mi.get_meta("parte", 0)) != 0:
			return
		var caminho: String = mi.get_meta("glb")
		var parte_t: Transform3D = mi.get_meta("parte_t", Transform3D())
		for i in mm.instance_count:
			var t := mi.global_transform * mm.get_instance_transform(i) * parte_t.affine_inverse()
			_peca(mi, caminho, t, true)
		return
	# malhas feitas no código, repetidas (blocos de cor): desenha-se cada uma como uma caixa
	for i in mm.instance_count:
		_caixa_2d(mi, mm.mesh, mi.global_transform * mm.get_instance_transform(i), mat, true)


func _e_chao(mat: Material) -> bool:
	if not mat is ShaderMaterial:
		return false
	var sh := (mat as ShaderMaterial).shader
	if sh == Natureza._shader_chao:
		return true
	return sh != null and "espuma" in sh.code and (cena is Andar or cena.has_method("chao_2d"))


# --- caixas, planos, cilindros, esferas ---

func _malha(mi: MeshInstance3D) -> void:
	if mi.mesh == null:
		return
	var mat := mi.get_active_material(0)
	if _e_sombra(mi, mat):
		var base := _novo_no(mi, "sombra")
		var pm := mi.mesh as PlaneMesh
		var sp := Sombra2D.criar(pm.size.x / 2.0)
		base.add_child(sp)
		return
	if _e_chao(mat) and mi.get_parent() == cena:
		return
	_caixa_2d(mi, mi.mesh, mi.global_transform, mat, false)


func _e_sombra(mi: MeshInstance3D, mat: Material) -> bool:
	return mi.mesh is PlaneMesh and mat is StandardMaterial3D and (mat as StandardMaterial3D).albedo_texture is GradientTexture2D


## Desenha uma malha como em 2D: o topo (os cantos de cima projetados) e os lados virados para sul.
func _caixa_2d(fonte: Node3D, m: Mesh, t: Transform3D, mat: Material, estatico: bool) -> void:
	var a := m.get_aabb()
	if a.size.length() < 0.01:
		return
	var base := _novo_no(fonte, "caixa", estatico)
	base.set_meta("malha", m)
	base.set_meta("mat", mat)
	base.set_meta("t0", t)
	_desenhar_caixa(base, m, t, mat)


func _desenhar_caixa(base: Node2D, m: Mesh, t: Transform3D, mat: Material) -> void:
	for f in base.get_children():
		f.queue_free()
	var a := m.get_aabb()
	var plano := a.size.y < 0.05 or m is PlaneMesh or m is QuadMesh
	var cor := Color.WHITE
	var tex: Texture2D = null
	var agua := false
	var brilha := false
	if mat is StandardMaterial3D:
		var sm: StandardMaterial3D = mat
		cor = sm.albedo_color
		tex = sm.albedo_texture
		brilha = sm.emission_enabled or sm.shading_mode == BaseMaterial3D.SHADING_MODE_UNSHADED
	elif mat is ShaderMaterial:
		var shm: ShaderMaterial = mat
		for k in ["cor", "albedo", "agua_cor"]:
			var v = shm.get_shader_parameter(k)
			if v is Color:
				cor = v
		for k in ["tex", "t_base", "textura"]:
			var v = shm.get_shader_parameter(k)
			if v is Texture2D:
				tex = v
		agua = shm.shader != null and "espuma" in shm.shader.code
	# os 8 cantos no mundo
	var c: Array[Vector3] = []
	for i in 8:
		c.append(t * a.get_endpoint(i))
	var centro := t * a.get_center()
	var ymax := -INF
	var zmin := INF
	var zmax := -INF
	for p in c:
		ymax = maxf(ymax, p.y)
		zmin = minf(zmin, p.z)
		zmax = maxf(zmax, p.z)
	# ordem: as coisas rasas (avisos no chão, tapetes) contam pela beira de trás; as altas pelo meio
	base.position = Vector2(centro.x, (zmin if plano else (zmin + zmax) / 2.0)) * PX
	var org := base.position
	# topo: os cantos de cima (os 4 com y maior)
	var cima: Array = c.duplicate()
	cima.sort_custom(func(p, q): return p.y > q.y)
	var topo: Array = cima.slice(0, 4)
	_poligono(base, _ordenar(topo.map(func(p): return ecra(p) - org)), cor, tex, agua, brilha, 1.0)
	if not plano:
		# os lados com a normal para sul (+z): as 6 faces da caixa, por índices dos cantos do AABB
		var faces := [[0, 1, 3, 2], [4, 5, 7, 6], [0, 1, 5, 4], [2, 3, 7, 6], [0, 2, 6, 4], [1, 3, 7, 5]]
		for f in faces:
			var pts: Array = f.map(func(i): return c[i])
			var n: Vector3 = (pts[1] - pts[0]).cross(pts[2] - pts[0])
			var meio: Vector3 = (pts[0] + pts[1] + pts[2] + pts[3]) / 4.0
			if n.dot(meio - centro) < 0.0:
				n = -n
			if n.normalized().z > 0.2 and absf(n.normalized().y) < 0.6:
				_poligono(base, _ordenar(pts.map(func(p): return ecra(p) - org)), cor, tex, agua, brilha, 0.74)


func _ordenar(pts: Array) -> PackedVector2Array:
	var m := Vector2.ZERO
	for p in pts:
		m += p
	m /= maxf(1.0, pts.size())
	pts.sort_custom(func(p, q): return (p - m).angle() < (q - m).angle())
	return PackedVector2Array(pts)


func _poligono(base: Node2D, pts: PackedVector2Array, cor: Color, tex: Texture2D, agua: bool, brilha: bool, luz: float) -> void:
	var pg := Polygon2D.new()
	pg.polygon = pts
	pg.color = Color(cor.r * luz, cor.g * luz, cor.b * luz, cor.a) if not brilha else cor
	if agua:
		pg.color = Color.WHITE
		var mat := ShaderMaterial.new()
		mat.shader = _agua_shader()
		mat.set_shader_parameter("cor", cor)
		pg.material = mat
		pg.uv = pts
	elif tex:
		pg.texture = tex
		pg.texture_repeat = CanvasItem.TEXTURE_REPEAT_ENABLED
		pg.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
		var uv := PackedVector2Array()
		for p in pts:
			uv.append(p + base.position)
		pg.uv = uv
	base.add_child(pg)


# --- luzes ---

func _luz(l: OmniLight3D) -> void:
	var base := _novo_no(l, "luz")
	var pl := PointLight2D.new()
	pl.texture = _textura_luz()
	pl.color = l.light_color
	pl.energy = l.light_energy * 0.8
	pl.texture_scale = l.omni_range * PX * 2.0 / 128.0
	pl.blend_mode = Light2D.BLEND_MODE_ADD
	base.add_child(pl)
	_posicionar(base, l, pl)


static var _tex_luz: Texture2D


## A mancha de luz em 4 degraus (como em pixel art), em vez de um degradê liso.
func _textura_luz() -> Texture2D:
	if _tex_luz == null:
		var img := Image.create(128, 128, false, Image.FORMAT_RGBA8)
		for y in 128:
			for x in 128:
				var d := Vector2(x - 63.5, y - 63.5).length() / 64.0
				var k := floorf(clampf(1.0 - d, 0.0, 1.0) * 4.0 + 0.6) / 4.0
				img.set_pixel(x, y, Color(1, 1, 1, k))
		_tex_luz = ImageTexture.create_from_image(img)
	return _tex_luz


## As coisas que brilham nas grutas (LuzesGruta: cogumelos, cristais, tochas, a Zona Segura) dão luz a sério.
func _luzes_gruta() -> void:
	if not LuzesGruta.ligada:
		return
	for f in LuzesGruta._fontes:
		var p: Vector3 = f[0]
		var pl := PointLight2D.new()
		pl.texture = _textura_luz()
		pl.color = f[1]
		pl.energy = float(f[3]) * 0.9
		pl.texture_scale = float(f[2]) * PX * 2.0 / 128.0
		pl.position = ecra(p)
		mundo.add_child(pl)


# --- partículas (chuva, neve, cinza, pirilampos, pólen...) ---

func _particulas(p3: CPUParticles3D) -> void:
	var base := _novo_no(p3, "particulas")
	base.z_index = 30
	var p := CPUParticles2D.new()
	p.amount = p3.amount
	p.lifetime = p3.lifetime
	p.preprocess = p3.preprocess
	p.explosiveness = p3.explosiveness
	p.randomness = p3.randomness
	p.local_coords = false
	p.emission_shape = CPUParticles2D.EMISSION_SHAPE_RECTANGLE
	var ex := p3.emission_box_extents
	p.emission_rect_extents = Vector2(ex.x, ex.z + ex.y * SOBE) * PX
	var g := p3.gravity
	p.gravity = Vector2(g.x, g.z - g.y * SOBE) * PX
	var d := p3.direction
	p.direction = Vector2(d.x, d.z - d.y * SOBE).normalized() if Vector2(d.x, d.z - d.y * SOBE).length() > 0.01 else Vector2(0, 1)
	p.spread = p3.spread
	p.initial_velocity_min = p3.initial_velocity_min * PX
	p.initial_velocity_max = p3.initial_velocity_max * PX
	p.color = p3.color
	p.color_ramp = p3.color_ramp
	p.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	var q := p3.mesh as QuadMesh
	var m := (q.material if q else null) as StandardMaterial3D
	var tam := q.size * PX if q else Vector2(4, 4)
	if m and m.albedo_texture:
		p.texture = m.albedo_texture
		var hf := maxi(1, m.particles_anim_h_frames)
		var cm := CanvasItemMaterial.new()
		cm.particles_animation = hf > 1
		cm.particles_anim_h_frames = hf
		cm.particles_anim_v_frames = 1
		cm.particles_anim_loop = true
		p.material = cm
		p.anim_speed_min = p3.anim_speed_min
		p.anim_speed_max = p3.anim_speed_max
		var lado := float(m.albedo_texture.get_height())
		p.scale_amount_min = maxf(tam.x, 2.0) / lado
		p.scale_amount_max = p.scale_amount_min
		if m.uv1_scale.x < 0.99:   # (a poeira: só o 1.º quadro da folha)
			cm.particles_animation = true
			cm.particles_anim_h_frames = maxi(1, int(round(1.0 / m.uv1_scale.x)))
			p.anim_speed_min = 0.0
			p.anim_speed_max = 0.0
		if m.albedo_color != Color.WHITE:
			p.color = m.albedo_color
	else:
		var img := Image.create(maxi(1, int(round(tam.x))), maxi(1, int(round(tam.y))), false, Image.FORMAT_RGBA8)
		img.fill(m.albedo_color if m else Color.WHITE)
		p.texture = ImageTexture.create_from_image(img)
	base.add_child(p)
	_atualizar_particulas(p3, p, base)


func _atualizar_particulas(p3: CPUParticles3D, p: CPUParticles2D, base: Node2D) -> void:
	base.position = Vector2.ZERO
	p.position = ecra(p3.global_position)
	p.emitting = p3.emitting
	base.visible = p3.is_visible_in_tree()


# ------------------------------------------------------------------ materiais 2D ------------------------------------------------------------------

func _material_janela() -> ShaderMaterial:
	if _mats.has("janela"):
		return _mats.janela
	if _shader_janela == null:
		_shader_janela = Shader.new()
		_shader_janela.code = """
shader_type canvas_item;
uniform float vento = 0.0;
uniform float alto = 32.0;
global uniform vec2 jogador2d;
varying vec2 base;
varying vec2 mundo_px;
float bayer(vec2 p) {
	ivec2 i = ivec2(mod(p, 4.0));
	int m[16] = int[](0, 8, 2, 10, 12, 4, 14, 6, 3, 11, 1, 9, 15, 7, 13, 5);
	return float(m[i.y * 4 + i.x]) / 16.0;
}
void vertex() {
	base = (MODEL_MATRIX * vec4(0.0, 0.0, 0.0, 1.0)).xy;
	float fase = base.x * 0.023 + base.y * 0.014;
	float h = clamp(1.0 - UV.y, 0.0, 1.0);
	float s = sin(TIME * 1.5 + fase) * 0.65 + sin(TIME * 2.6 + fase * 1.7) * 0.25 + sin(TIME * 0.4 + fase * 0.3) * 0.5;
	VERTEX.x += round(s * vento * h * h * 0.06 * alto);
	mundo_px = (MODEL_MATRIX * vec4(VERTEX, 0.0, 1.0)).xy;
}
void fragment() {
	vec4 c = texture(TEXTURE, UV);
	// o herói está atrás (a planta / a casa fica mais a sul): abre-se uma janela redonda à volta dele
	if (base.y > jogador2d.y + 22.0 && mundo_px.y < jogador2d.y + 12.0) {
		float d = length((mundo_px - jogador2d) * vec2(1.0, 0.8));
		float k = clamp((d - 18.0) / 16.0, 0.0, 1.0);
		if (bayer(floor(UV * vec2(textureSize(TEXTURE, 0)))) >= k) c.a = 0.0;
	}
	COLOR = c;
}
"""
	var m := ShaderMaterial.new()
	m.shader = _shader_janela
	_mats.janela = m
	return m


func _material_planta(origem: ShaderMaterial, tex: Texture2D) -> ShaderMaterial:
	var chave := "planta|" + str(origem.get_instance_id())
	if _mats.has(chave):
		return _mats[chave]
	_material_janela()
	var m := ShaderMaterial.new()
	m.shader = _shader_janela
	m.set_shader_parameter("vento", origem.get_shader_parameter("vento"))
	m.set_shader_parameter("alto", float(tex.get_height()))
	_mats[chave] = m
	return m


func _agua_shader() -> Shader:
	if _shader_agua == null:
		_shader_agua = Shader.new()
		_shader_agua.code = """
shader_type canvas_item;
uniform vec4 cor : source_color;
float aleat(vec2 p) {
	return fract(sin(dot(p, vec2(12.9898, 78.233))) * 43758.5453);
}
void fragment() {
	vec2 q = floor(UV);
	vec3 c = cor.rgb;
	float fila = floor(q.y / 6.0);
	float sx = q.x + floor(TIME * (1.0 + floor(aleat(vec2(fila, 3.0)) * 3.0)));
	float r = aleat(vec2(floor(sx / 12.0), fila));
	if (r < 0.4 && mod(q.y, 6.0) == 2.0 && mod(sx, 12.0) >= 2.0 && mod(sx, 12.0) < 5.0 + floor(r * 10.0))
		c = mix(c, vec3(1.0), 0.45 * step(-0.2, sin(TIME * 1.4 + r * 31.0)));
	COLOR = vec4(c, cor.a * 0.92);
}
"""
	return _shader_agua


# ------------------------------------------------------------------ todos os frames ------------------------------------------------------------------

func _process(delta: float) -> void:
	if not _novos.is_empty():
		var lista := _novos
		_novos = []
		for n in lista:
			if is_instance_valid(n) and n.is_inside_tree():
				_varrer(n)
	_t_estatico += delta
	var rever_estaticos := _t_estatico > 0.5
	if rever_estaticos:
		_t_estatico = 0.0
	var i := 0
	while i < _proxies.size():
		var p: Dictionary = _proxies[i]
		var fonte = p.fonte
		var no: Node2D = p.no
		if not is_instance_valid(fonte) or not fonte.is_inside_tree():
			no.queue_free()
			_vistos.erase(p.get("id", 0))
			_proxies.remove_at(i)
			continue
		i += 1
		if p.estatico and not rever_estaticos:
			continue
		match p.tipo:
			"animado":
				_atualizar_animado(fonte, no.get_child(0), no)
			"sprite":
				_atualizar_sprite(fonte, no.get_child(0), no)
			"rotulo":
				_atualizar_rotulo(fonte, no.get_child(0), no)
			"peca":
				if not p.estatico:
					var t: Transform3D = (fonte as Node3D).global_transform
					_por_peca(no, no.get_child(0), t)
				no.visible = (fonte as Node3D).is_visible_in_tree()
			"caixa":
				if not p.estatico:
					var t: Transform3D = (fonte as Node3D).global_transform
					if not t.is_equal_approx(no.get_meta("t0")):
						no.set_meta("t0", t)
						_desenhar_caixa(no, no.get_meta("malha"), t, no.get_meta("mat"))
				no.visible = (fonte as Node3D).is_visible_in_tree()
			"particulas":
				_atualizar_particulas(fonte, no.get_child(0), no)
			"sombra", "luz":
				var f3 := fonte as Node3D
				no.position = chao_px(f3.global_position)
				if no.get_child_count() > 0:
					(no.get_child(0) as Node2D).position.y = -sobe_px(f3.global_position) if p.tipo == "luz" else 0.0
				no.visible = f3.is_visible_in_tree()
	_camara(false)
	_luz_do_dia()


func _camara(saltar: bool) -> void:
	var j := get_tree().get_first_node_in_group("jogador") as Node3D
	if j == null:
		return
	var alvo := ecra(j.global_position) + Vector2(0, -12)
	var c3 := get_viewport().get_camera_3d()
	if c3 is Camara:
		var cam: Camara = c3
		for d in ZOOM:
			if cam.distancia <= d:
				camara.zoom = Vector2.ONE * ZOOM[d]
				break
		camara.offset = Vector2(cam.h_offset, -cam.v_offset) * PX
	camara.global_position = alvo
	if saltar:
		camara.reset_smoothing()
	RenderingServer.global_shader_parameter_set("jogador2d", alvo - Vector2(0, 2))


## A cor da luz do sol e do céu (CicloDia) passa a cor de tudo o que se vê.
func _luz_do_dia() -> void:
	var sol: DirectionalLight3D = null
	var env: Environment = null
	for n in cena.get_children():
		if n is DirectionalLight3D:
			sol = n
		elif n is WorldEnvironment:
			env = (n as WorldEnvironment).environment
	if sol == null or env == null:
		return
	var luz := sol.light_color * clampf(sol.light_energy / 0.75, 0.0, 1.2)
	var amb := env.ambient_light_color * env.ambient_light_energy
	var c := Color(clampf(luz.r * 0.62 + amb.r * 0.55, 0.12, 1.0), clampf(luz.g * 0.62 + amb.g * 0.55, 0.12, 1.0),
			clampf(luz.b * 0.62 + amb.b * 0.55, 0.14, 1.0))
	_luz_dia.color = _luz_dia.color.lerp(c, 0.1)
