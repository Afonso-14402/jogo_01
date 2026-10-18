extends Node
## Fotografa as peças 3D (.glb) em sprites 2D para a vista 2D (OBJETIVO.md, Fase D; docs/PROGRAMACAO.md, 4A).
##
## A projeção é a mesma do chão 2D: 1 m = 16 px; o ponto (x, y, z) vai para (x, z − 0,8·y) no ecrã (o alto sobe,
## o lado de frente vê-se). Um shader troca os materiais das peças: faz esta projeção (com uma câmara a olhar
## a direito para baixo) e uma luz simples de cima à esquerda, sem sombras. Depois ferramentas/arte/glb_sprites.py
## passa as imagens à paleta Resurrect 64 e põe-lhes o contorno escuro, como o resto da arte.
##
## Saída: arte/sprites2d/<caminho do .glb sem .glb>_r<rotação>.png (rotação 0–3 = 0°, 90°, 180°, 270° à volta do
## eixo vertical) e dados/sprites2d.json {caminho do .glb: {"r0": [largura, altura, âncora x, âncora y], ...}}.
## A âncora é o píxel onde fica a origem da peça (o sítio do chão onde ela foi posta).
##
## Uso: xvfb-run -a godot --rendering-driver opengl3 --path . res://ferramentas/arte/glb_sprites.tscn [-- pasta ...]

const PX := 16.0
const SOBE := 0.8
const SAIDA := "res://arte/sprites2d/"
const UMA_ROTACAO := ["/kit/"]   # peças do kit (rochas, árvores...) postas com rotação ao calhas: chega uma
const QUATRO := ["ponte", "passadico", "cais", "escadas", "chao_castelo"]   # (menos as pontes: põem-se ao alto ou deitadas)

var _fila: Array = []        # [[caminho, rotação]]
var _vp: SubViewport
var _cam: Camera3D
var _atual: Node3D
var _mapa: Dictionary = {}
var _shader: Shader
var _n := 0


func _ready() -> void:
	var pastas: Array = Array(OS.get_cmdline_user_args())
	if pastas.is_empty():
		pastas = ["res://arte"]
	for p in pastas:
		var c: String = p if p.begins_with("res://") else "res://" + p
		if c.ends_with(".glb"):
			for r in (1 if UMA_ROTACAO.any(func(k): return k in c) and not QUATRO.any(func(k): return k in c.get_file()) else 4):
				_fila.append([c, r])
		else:
			_listar(c)
	var antigo := FileAccess.get_file_as_string("res://dados/sprites2d.json")
	if antigo != "":
		_mapa = JSON.parse_string(antigo)
	_vp = SubViewport.new()
	_vp.transparent_bg = true
	_vp.own_world_3d = true
	_vp.render_target_update_mode = SubViewport.UPDATE_ALWAYS
	_vp.msaa_3d = Viewport.MSAA_DISABLED
	add_child(_vp)
	var env := WorldEnvironment.new()
	env.environment = Environment.new()
	env.environment.background_mode = Environment.BG_CLEAR_COLOR
	_vp.add_child(env)
	_cam = Camera3D.new()
	_cam.projection = Camera3D.PROJECTION_ORTHOGONAL
	_cam.keep_aspect = Camera3D.KEEP_HEIGHT
	_cam.near = 0.05
	_cam.far = 4000.0
	_cam.rotation_degrees = Vector3(-90, 0, 0)   # a olhar a direito para baixo; o cimo do ecrã é o norte (−z)
	_vp.add_child(_cam)
	_shader = Shader.new()
	_shader.code = """
shader_type spatial;
render_mode unshaded, cull_disabled, world_vertex_coords, depth_draw_opaque;
uniform sampler2D tex : source_color, filter_nearest, repeat_enable;
uniform vec4 cor : source_color = vec4(1.0);
uniform float usa_tex = 0.0;
uniform vec3 emissao = vec3(0.0);
uniform vec3 uv_escala = vec3(1.0);
uniform vec3 uv_desvio = vec3(0.0);
uniform float alfa_corte = 0.0;
varying vec3 normal_mundo;
void vertex() {
	normal_mundo = normalize(NORMAL);
	UV = UV * uv_escala.xy + uv_desvio.xy;
	// a projeção 2D: o alto vai para norte; a "profundidade" é a distância a quem vê (de cima e de sul)
	vec3 w = VERTEX;
	VERTEX = vec3(w.x, w.y + 0.8 * w.z + 1000.0, w.z - 0.8 * w.y);
}
void fragment() {
	vec4 c = cor;
	if (usa_tex > 0.5) c *= texture(tex, UV);
	if (alfa_corte > 0.0 && c.a < alfa_corte) discard;
	vec3 l = normalize(vec3(-0.55, 0.75, 0.45));   // luz de cima, à esquerda, um pouco de frente
	float d = max(dot(normal_mundo, l), 0.0);
	float k = 0.55 + 0.5 * d;
	ALBEDO = c.rgb * k + emissao;
}
"""
	_seguinte.call_deferred()


func _listar(pasta: String) -> void:
	var d := DirAccess.open(pasta)
	if d == null:
		return
	for f in d.get_files():
		if f.ends_with(".glb"):
			var caminho := pasta.path_join(f)
			var rots := 1 if UMA_ROTACAO.any(func(k): return k in caminho) and not QUATRO.any(func(k): return k in caminho.get_file()) else 4
			for r in rots:
				_fila.append([caminho, r])
	for sub in d.get_directories():
		if sub != "sprites2d":
			_listar(pasta.path_join(sub))


func _material(base: Material) -> ShaderMaterial:
	var m := ShaderMaterial.new()
	m.shader = _shader
	if base is StandardMaterial3D:
		var s: StandardMaterial3D = base
		m.set_shader_parameter("cor", s.albedo_color)
		if s.albedo_texture:
			m.set_shader_parameter("tex", s.albedo_texture)
			m.set_shader_parameter("usa_tex", 1.0)
		m.set_shader_parameter("uv_escala", s.uv1_scale)
		m.set_shader_parameter("uv_desvio", s.uv1_offset)
		if s.emission_enabled:
			var e := s.emission * s.emission_energy_multiplier * 0.35
			m.set_shader_parameter("emissao", Vector3(e.r, e.g, e.b))
		if s.transparency != BaseMaterial3D.TRANSPARENCY_DISABLED:
			m.set_shader_parameter("alfa_corte", 0.5)
	return m


func _trocar_materiais(no: Node) -> void:
	if no is MeshInstance3D and (no as MeshInstance3D).mesh:
		var mi: MeshInstance3D = no
		for i in mi.mesh.get_surface_count():
			var base := mi.get_active_material(i)
			mi.set_surface_override_material(i, _material(base))
	for f in no.get_children():
		_trocar_materiais(f)


func _caixa(no: Node, t: Transform3D, a: Array) -> void:
	var tt := t
	if no is Node3D:
		tt = t * (no as Node3D).transform
	if no is MeshInstance3D and (no as MeshInstance3D).mesh:
		var b: AABB = (no as MeshInstance3D).mesh.get_aabb()
		for i in 8:
			a.append(tt * b.get_endpoint(i))
	for f in no.get_children():
		_caixa(f, tt, a)


func _seguinte() -> void:
	if _atual:
		_atual.queue_free()
		_atual = null
	if _fila.is_empty():
		var f := FileAccess.open("res://dados/sprites2d.json", FileAccess.WRITE)
		f.store_string(JSON.stringify(_mapa, "", true))
		f.close()
		print("GLB_SPRITES: %d imagens" % _n)
		get_tree().quit()
		return
	var item: Array = _fila.pop_front()
	var caminho: String = item[0]
	var r: int = item[1]
	var cena := load(caminho) as PackedScene
	if cena == null:
		_seguinte.call_deferred()
		return
	_atual = cena.instantiate()
	_atual.rotation.y = r * PI / 2.0
	_trocar_materiais(_atual)
	var pts: Array = []
	_caixa(_atual, Transform3D.IDENTITY, pts)   # (a rotação já está no transform da peça)
	if pts.is_empty():
		_seguinte.call_deferred()
		return
	var x0 := INF
	var x1 := -INF
	var s0 := INF
	var s1 := -INF
	for p: Vector3 in pts:
		x0 = minf(x0, p.x)
		x1 = maxf(x1, p.x)
		s0 = minf(s0, p.z - SOBE * p.y)
		s1 = maxf(s1, p.z - SOBE * p.y)
	var w := int(ceil((x1 - x0) * PX)) + 4
	var h := int(ceil((s1 - s0) * PX)) + 4
	w = clampi(w, 4, 1024)
	h = clampi(h, 4, 1024)
	_vp.size = Vector2i(w, h)
	_cam.size = h / PX
	var cx := (x0 + x1) / 2.0
	var cs := (s0 + s1) / 2.0
	# o centro da imagem: no plano projetado (x, z − 0,8·y); a câmara vê o "chão" projetado em y' grande
	_cam.position = Vector3(cx + (w - (x1 - x0) * PX) * 0.0, 3000.0, cs)
	_vp.add_child(_atual)
	await RenderingServer.frame_post_draw
	await RenderingServer.frame_post_draw
	var img := _vp.get_texture().get_image()
	var rel := caminho.trim_prefix("res://arte/").trim_suffix(".glb")
	var destino := SAIDA + rel + "_r%d.png" % r
	DirAccess.make_dir_recursive_absolute(ProjectSettings.globalize_path(destino.get_base_dir()))
	img.save_png(ProjectSettings.globalize_path(destino))
	# a origem da peça (0, 0, 0) no ecrã: x = 0, linha = 0 (projetada)
	var ax := (0.0 - cx) * PX + w / 2.0
	var ay := (0.0 - cs) * PX + h / 2.0
	var e: Dictionary = _mapa.get(caminho, {})
	e["r%d" % r] = [w, h, snappedf(ax, 0.5), snappedf(ay, 0.5)]
	_mapa[caminho] = e
	_n += 1
	if _n % 100 == 0:
		print("GLB_SPRITES: ", _n, " (faltam ", _fila.size(), ")")
	_seguinte.call_deferred()
