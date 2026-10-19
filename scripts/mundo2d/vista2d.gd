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


## Escala "certa" para pixel art: com o zoom 3 (o normal), múltiplos de 1/3 dão píxeis todos do mesmo tamanho
## (uma árvore a 1,25× ficava com píxeis de 3 e de 4 no ecrã; a 4/3 ficam todos com 4).
static func escala_px(e: float) -> float:
	return maxf(1.0 / 3.0, round(absf(e) * 3.0) / 3.0) * signf(e if e != 0.0 else 1.0)


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
	get_viewport().disable_3d = true   # e o ecrã nem desenha o 3D (as contas e a física continuam)
	_chao()
	_varrer(cena)
	_luzes_gruta()
	get_tree().node_added.connect(_no_novo)
	_camara(true)


func _exit_tree() -> void:
	if atual == self:
		atual = null
		get_viewport().disable_3d = false
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
				agua[bz * bw + bx] = 1 if c in ["~~", "ww", ",,"] or (c == "==" and alt[bz * bw + bx] < -0.5) else 0
				if c == "%%":   # lama: um pouco abaixo, com cor de lama (a água do shader pinta-a)
					agua[bz * bw + bx] = 1
		# o topo das paredes de rocha fica plano (no 3D é irregular; visto de cima eram almofadas de alturas
		# diferentes). A beira recortada fica como está.
		var hr := a.altura_rocha()
		var img_alt: Image = a._alturas_img
		if hr > 0.0 and img_alt:
			img_alt = img_alt.duplicate()
			for bz in bh:
				for bx in bw:
					var i := bz * bw + bx
					if alt[i] >= hr - 0.9 and a.codigo(bx / Andar.POR_CEL, bz / Andar.POR_CEL) == "##":
						alt[i] = hr
						img_alt.set_pixel(bx, bz, Color(hr, 0, 0))
		var origem := Vector2(-a.largura * Andar.CEL / 2.0, -a.altura_cel * Andar.CEL / 2.0)
		var cor_agua := Color(a.kit.get("agua", "#0b8a8f")) if String(a.kit.get("agua", "")).begins_with("#") else Color("0b8a8f")
		var mat := Chao2D.material(a.regiao, a._splat, img_alt, a._mascara_agua, origem,
				Vector2(a.largura * Andar.CEL, a.altura_cel * Andar.CEL), cor_agua, a.altura_rocha())
		_por_chao(Chao2D.filas(alt, agua, bw, bh, origem, Andar.BLOCO, mat))
		RenderingServer.set_default_clear_color(Color("1c2a2a") if a.regiao != 2 else Color("120e16"))
		_fora(String(a._natureza.get("fora", "chao")), mat, origem, Vector2(a.largura * Andar.CEL, a.altura_cel * Andar.CEL), a.regiao)
	elif cena.has_method("chao_2d"):
		_por_chao(cena.chao_2d())


var _chao_baixo: Node2D
static var _shader_vazio: Shader


## O que há à volta do mapa (até 60 m para cada lado): chão (mais escuro), água ou o vazio (nuvens do céu ou o
## abismo de estrelas, lá em baixo).
func _fora(fora: String, mat: ShaderMaterial, origem: Vector2, tam: Vector2, regiao: int) -> void:
	var m := 60.0
	var a := origem - Vector2(m, m)
	var b := origem + tam + Vector2(m, m)
	var v := PackedVector2Array()
	var uv := PackedVector2Array()
	var cor := PackedColorArray()
	var info := Color(0.0, 0.2, 0.0, 0.5 if fora == "agua" else 1.0)
	Chao2D._quad(v, uv, cor, a * PX, b * PX, a, b, info)
	var arr := []
	arr.resize(Mesh.ARRAY_MAX)
	arr[Mesh.ARRAY_VERTEX] = v
	arr[Mesh.ARRAY_TEX_UV] = uv
	arr[Mesh.ARRAY_COLOR] = cor
	var am := ArrayMesh.new()
	am.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, arr)
	var mi := MeshInstance2D.new()
	mi.mesh = am
	mi.name = "Fora"
	mi.z_index = -11
	if fora == "nada":
		if _shader_vazio == null:
			_shader_vazio = Shader.new()
			_shader_vazio.code = """
shader_type canvas_item;
uniform sampler2D ruido : filter_linear, repeat_enable;
uniform float abismo = 0.0;
float aleat(vec2 p) {
	return fract(sin(dot(p, vec2(12.9898, 78.233))) * 43758.5453);
}
float nuvem(vec2 p, float esc, vec2 vel) {
	return texture(ruido, p * esc + TIME * vel).r * 0.6 + texture(ruido, p * esc * 2.3 - TIME * vel * 0.6 + 0.37).r * 0.3
			+ texture(ruido, p * esc * 7.0 + TIME * vel * 1.3 + 0.71).r * 0.1;   // (a última: as beiras fofas)
}
void fragment() {
	vec2 p = floor(UV * 8.0) / 8.0;     // píxeis de 2 (está longe, lá em baixo)
	float n1 = texture(ruido, p * 0.006 + TIME * vec2(0.004, 0.001)).r;
	float n2 = texture(ruido, p * 0.013 - TIME * vec2(0.002, 0.003) + 0.5).r;
	float n = n1 * 0.65 + n2 * 0.35;
	vec3 c;
	if (abismo < 0.5) {
		// o mar de nuvens lá em baixo: o céu fundo, fiapos longe (píxeis de 4) e nuvens fofas mais perto
		// (píxeis de 2): brancas, com a barriga sombreada e sombra no céu por baixo
		c = vec3(0.30, 0.61, 0.90);
		if (nuvem(p, 0.03, vec2(0.0015, 0.0004)) > 0.56) c = vec3(0.56, 0.83, 1.0);
		vec2 q = floor(UV * 16.0) / 16.0;   // nuvens mais perto: píxeis do tamanho dos do jogo
		vec2 v = vec2(0.004, 0.001);
		const float TAM = 0.018;   // tamanho das nuvens (maior = mais pequenas)
		float k = nuvem(q, TAM, v);
		if (k > 0.5) {
			c = vec3(1.0);
			if (nuvem(q + vec2(0.0, 1.0), TAM, v) < 0.5) c = vec3(0.78, 0.86, 0.82);
			if (nuvem(q + vec2(0.0, 0.375), TAM, v) < 0.5) c = vec3(0.61, 0.67, 0.70);
			else if (nuvem(q - vec2(0.0, 0.25), TAM, v) < 0.5) c = vec3(0.78, 0.86, 0.82);   // contorno claro em cima
		} else if (nuvem(q - vec2(1.5, 2.5), TAM, v) > 0.5) {
			c *= 0.8;   // a sombra da nuvem
		}
	} else {
		c = vec3(0.18, 0.13, 0.18);
		c = mix(c, vec3(0.27, 0.16, 0.25), step(0.5, n));
		c = mix(c, vec3(0.42, 0.24, 0.46), step(0.62, n));
		float e = aleat(floor(UV * 8.0));   // estrelas de 2 píxeis, poucas
		c = mix(c, vec3(1.0), step(0.9985, e) * (0.5 + 0.5 * sin(TIME * 2.0 + e * 60.0)));
		c = mix(c, vec3(0.66, 0.52, 0.95), step(0.997, e) * (1.0 - step(0.9985, e)));
	}
	COLOR = vec4(c, 1.0);
}
"""
		var sm := ShaderMaterial.new()
		sm.shader = _shader_vazio
		sm.set_shader_parameter("ruido", Natureza.ruido())
		sm.set_shader_parameter("abismo", 1.0 if regiao == 10 else 0.0)
		mi.material = sm
	else:
		mi.material = mat
	add_child(mi)
	move_child(mi, 0)


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
	# (os efeitos vão para a cena atual, que pode não ser a do andar: aceita-se tudo o que está no mesmo ecrã)
	if n is Node3D and n.get_viewport() == get_viewport():
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
	if n3.owner and n3.owner.scene_file_path.ends_with(".glb"):   # um bocado de uma peça .glb (a peça já tem a sua imagem)
		return false
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
	var gs := s.global_basis.get_scale().abs()
	a.scale = Vector2(k * gs.x, k * gs.y)
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
	var gs := s.global_basis.get_scale().abs()
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
	# a letra em pixel com contorno, a 1× no mundo (com o zoom 3 fica do tamanho dos bonecos); as placas
	# grandes (nomes das salas, títulos) a 2×
	ls.font = Tema.fonte_contorno()
	var grande := not l.fixed_size and l.font_size * l.pixel_size * PX > 6.0
	ls.font_size = 18 if grande else 9
	ls.font_color = l.modulate
	t.text = l.text
	t.scale = Vector2.ONE
	t.size = Vector2.ZERO
	t.reset_size()
	t.position = Vector2(round(-t.size.x / 2.0), round(-sobe_px(p) - t.size.y / 2.0))
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


static var _moveis2d: Dictionary = {}


## Os móveis desenhados em pixel art (ferramentas/arte/moveis2d.py; os regionais usam o básico): [entrada rN] ou [].
func _movel_2d(caminho: String, rot_y: float) -> Array:
	if not "/moveis/" in caminho:
		return []
	if _moveis2d.is_empty():
		_moveis2d = Dados.tabela("moveis2d")
	var nome := caminho.get_file().get_basename()
	nome = String(_moveis2d.get("regional", {}).get(nome, nome))
	var e: Dictionary = _moveis2d.get("moveis", {}).get(nome, {})
	if e.is_empty():
		return []
	var r := int(posmod(int(round(rot_y / (PI / 2.0))), 4))
	return e.get("r%d" % r, [])


func _peca_movel(fonte: Node3D, caminho: String, t: Transform3D, m: Array, estatico: bool) -> Node2D:
	var tex: Texture2D = load(String(m[0]))
	var quadros := int(m[3])
	var base := _novo_no(fonte, "peca", estatico)
	var no: Node2D
	if quadros > 1:   # a vela e a lareira: a chama mexe-se
		var sf := SpriteFrames.new()
		sf.set_animation_speed("default", 6.0)
		var w := tex.get_width() / quadros
		for q in quadros:
			var at := AtlasTexture.new()
			at.atlas = tex
			at.region = Rect2(q * w, 0, w, tex.get_height())
			sf.add_frame("default", at)
		var a := AnimatedSprite2D.new()
		a.sprite_frames = sf
		a.centered = false
		a.offset = -Vector2(float(m[1]), float(m[2]))
		a.play("default")
		a.frame = randi() % quadros
		no = a
	else:
		var sp := Sprite2D.new()
		sp.texture = tex
		sp.centered = false
		sp.offset = -Vector2(float(m[1]), float(m[2]))
		no = sp
	no.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	base.add_child(no)
	base.set_meta("t", t)
	base.position = chao_px(t.origin)
	no.position = Vector2(0, -sobe_px(t.origin))
	var nome := String(_moveis2d.get("regional", {}).get(caminho.get_file().get_basename(), caminho.get_file().get_basename()))
	if nome in LUZ_MOVEIS:
		_luz_peca(LUZ_MOVEIS[nome], t.origin, 16.0)
	return base


const LUZ_MOVEIS := {"movel_b11": "candeeiro", "movel_b12": "vela", "movel_b22": "fogueira"}


func _peca(fonte: Node3D, caminho: String, t: Transform3D, estatico: bool = false) -> Node2D:
	var mv := _movel_2d(caminho, t.basis.get_euler().y)
	if not mv.is_empty():
		return _peca_movel(fonte, caminho, t, mv, estatico)
	var tx := _textura_peca(caminho, t.basis.get_euler().y)
	if tx.is_empty():
		return null
	var base := _novo_no(fonte, "peca", estatico)
	var s := Sprite2D.new()
	s.texture = tx[0]
	s.centered = false
	s.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	var esc := t.basis.get_scale().abs()
	s.scale = Vector2(escala_px(esc.x) * (-1.0 if tx[2] else 1.0), escala_px(esc.y))
	s.offset = -tx[1]
	if tx[2]:   # espelhado: a âncora fica do outro lado
		s.offset.x = -(float(tx[0].get_width()) - tx[1].x)
	var pisavel := _e_pisavel(caminho)
	if tx[0].get_height() > 40 and not pisavel:
		s.material = _material_janela()
	base.add_child(s)
	base.set_meta("t", t)
	_por_peca(base, s, t)
	if pisavel:   # pontes e cais: anda-se por cima, ficam sempre por baixo de quem passa
		base.reparent(_camada_pisavel(), false)
		return base
	if estatico or fonte.get_parent() == cena or fonte is MultiMeshInstance3D:
		_sombra_chao(t.origin, float(tx[0].get_width()) * absf(s.scale.x) * 0.38)
	_luz_peca(caminho, t.origin, float(tx[0].get_height()) * absf(s.scale.y))
	return base


const LUZ_PECAS := {"candeeiro": [Color("fbb954"), 7.0], "lanterna": [Color("fbb954"), 6.0], "fogueira": [Color("f79617"), 9.0],
	"tocha": [Color("f79617"), 6.0], "braseiro": [Color("f79617"), 7.0], "fornalha": [Color("ea4f36"), 8.0],
	"farol": [Color("fbff86"), 12.0], "vela": [Color("fbb954"), 4.0]}
var _luzes_noite: Array[PointLight2D] = []


## As peças que dão luz (candeeiros, tochas, fogueiras, faróis) acendem-se à noite (e sempre nas grutas).
func _luz_peca(caminho: String, p: Vector3, alto_px: float) -> void:
	var nome := caminho.get_file().get_basename()
	for k in LUZ_PECAS:
		if k in nome and not "premio" in nome and not "velas_rasgadas" in nome:
			var pl := PointLight2D.new()
			pl.texture = _textura_luz()
			pl.color = LUZ_PECAS[k][0]
			pl.texture_scale = float(LUZ_PECAS[k][1]) * PX * 2.0 / 128.0
			pl.energy = 0.0
			pl.position = ecra(p) - Vector2(0, alto_px * 0.7)
			mundo.add_child(pl)
			_luzes_noite.append(pl)
			return


var _sombras: Node2D
var _rasteira: Node2D


const PISAVEIS := ["ponte", "passadico", "cais", "chao_castelo"]
var _pisavel: Node2D


func _e_pisavel(caminho: String) -> bool:
	var f := caminho.get_file()
	return "/kit/" in caminho and PISAVEIS.any(func(k): return k in f)


func _camada_pisavel() -> Node2D:
	if _pisavel == null:
		_pisavel = Node2D.new()
		_pisavel.name = "Pisaveis"
		_pisavel.z_index = -6
		add_child(_pisavel)
	return _pisavel


func _camada_rasteira() -> Node2D:
	if _rasteira == null:
		_rasteira = Node2D.new()
		_rasteira.name = "Rasteira"
		_rasteira.z_index = -8
		add_child(_rasteira)
	return _rasteira


## Sombra no chão (por baixo de tudo): uma elipse um pouco à direita e em baixo (a luz vem de cima à esquerda).
func _sombra_chao(p: Vector3, raio_px: float) -> void:
	if raio_px < 4.0:
		return
	if _sombras == null:
		_sombras = Node2D.new()
		_sombras.name = "Sombras"
		_sombras.z_index = -9
		add_child(_sombras)
	var sp := Sombra2D.criar(raio_px / PX)
	sp.position = ecra(p) + Vector2(raio_px * 0.25, 1.0)
	_sombras.add_child(sp)


func _por_peca(base: Node2D, s: Node2D, t: Transform3D) -> void:
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
		var rasteira := tex.get_height() <= 12   # erva e flores baixinhas: por baixo de tudo (não entram na ordenação)
		for i in mm.instance_count:
			var t := mi.global_transform * mm.get_instance_transform(i)
			# um só Sprite2D por planta: o sítio é o do pé (para a ordenação) e o desenho sobe com o offset
			var s := Sprite2D.new()
			s.texture = tex
			s.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
			# (um basis espelhado tem a escala toda negativa: o espelho é só para os lados, nunca de pernas para o ar)
			var esc := t.basis.get_scale().abs()
			var espelho := -1.0 if t.basis.determinant() < 0.0 or t.basis.x.x < 0.0 else 1.0
			s.scale = Vector2(escala_px(esc.x) * espelho, escala_px(esc.y))
			s.position = chao_px(t.origin)
			s.offset = Vector2(0, -tex.get_height() / 2.0 - sobe_px(t.origin) / absf(s.scale.y))
			s.material = mat2
			if rasteira:
				_camada_rasteira().add_child(s)
			else:
				mundo.add_child(s)
			if tex.get_height() >= 20:   # as coisas altas fazem sombra no chão
				_sombra_chao(t.origin, tex.get_width() * absf(s.scale.x) * 0.36)
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
	if mat is ShaderMaterial and (mat as ShaderMaterial).shader and "abismo" in (mat as ShaderMaterial).shader.code:
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
	var alto := (t.basis * Vector3(0, a.size.y, 0)).length()
	# rasas (chão, tapetes, avisos, água): desenham-se por baixo de quem está em cima delas
	var plano := alto < 0.35 or m is PlaneMesh or m is QuadMesh
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
	# ordem: as coisas rasas (chão, avisos, tapetes) contam pela beira de trás; as altas pelo meio
	base.position = Vector2(centro.x, (zmin - 0.05 if plano else (zmin + zmax) / 2.0)) * PX
	# os chãos grandes (o fundo das masmorras e das casas) vão para baixo de tudo
	base.z_index = -5 if plano and (zmax - zmin) > 6.0 and ymax < centro.y + 0.4 else 0
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
		# a sombra no chão ao pé das paredes e das caixas altas (a luz vem de cima, um pouco de trás)
		if alto > 1.2:
			var ymin := INF
			var x0 := INF
			var x1 := -INF
			for p in c:
				ymin = minf(ymin, p.y)
				x0 = minf(x0, p.x)
				x1 = maxf(x1, p.x)
			var y0 := ecra(Vector3(0, ymin, zmax)).y - org.y
			var sombra := Polygon2D.new()
			sombra.polygon = PackedVector2Array([Vector2(x0 * PX - org.x, y0), Vector2(x1 * PX - org.x, y0),
					Vector2(x1 * PX - org.x + 3, y0 + 5), Vector2(x0 * PX - org.x + 3, y0 + 5)])
			sombra.color = Color(0.18, 0.13, 0.18, 0.3)
			base.add_child(sombra)
			base.move_child(sombra, 0)


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
	luz *= 0.92   # (sem o sombreado do 3D, as caixas ficavam mais claras do que o resto)
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
	pl.energy = l.light_energy * (0.4 if not LuzesGruta.ligada else 0.8)
	pl.texture_scale = l.omni_range * PX * 2.0 / 128.0
	if l is LuzHeroi:   # a luz do herói: mais larga em 2D (não há o chão a brilhar à volta, como no 3D)
		pl.texture_scale *= 1.8
		pl.energy = 1.0
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
				var k := clampf(1.0 - d, 0.0, 1.0)
				k = floorf(k * k * 6.0 + 0.5) / 6.0   # mais forte no meio e a apagar-se aos degraus pequenos
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

var tempo_us: float = 0.0   # quanto demora cada frame da vista 2D (média, em microssegundos), para ver se pesa


func _process(delta: float) -> void:
	var t0 := Time.get_ticks_usec()
	_frame(delta)
	tempo_us = lerpf(tempo_us, float(Time.get_ticks_usec() - t0), 0.1)


func _frame(delta: float) -> void:
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
				no.visible = f3.is_visible_in_tree() and (not f3 is Light3D or (f3 as Light3D).light_energy > 0.01)
				if p.tipo == "luz" and f3 is LuzHeroi and no.get_child_count() > 0:
					(no.get_child(0) as PointLight2D).texture_scale = (f3 as OmniLight3D).omni_range * PX * 2.0 / 128.0 * 1.8
	_camara(false)
	_luz_do_dia()


func _camara(saltar: bool) -> void:
	var j := get_tree().get_first_node_in_group("jogador") as Node3D
	if j == null:
		return
	var alvo := ecra(j.global_position) + Vector2(0, -12)
	# dentro de uma casa: a câmara fica perto do meio da sala (vê-se a parede do fundo e a porta)
	if Interior.atual and is_instance_valid(Interior.atual) and Jogo.dentro:
		var meio := ecra(Interior.ORIGEM + Vector3(0, 1.0, 0))
		var meia := Vector2(Interior.atual.largura(), Interior.atual.fundo()) * PX * 0.5
		var vista := get_viewport_rect().size / camara.zoom * 0.5
		alvo.x = clampf(alvo.x, meio.x - maxf(0.0, meia.x - vista.x + 24.0), meio.x + maxf(0.0, meia.x - vista.x + 24.0))
		alvo.y = clampf(alvo.y, meio.y - maxf(0.0, meia.y - vista.y + 40.0), meio.y + maxf(0.0, meia.y - vista.y + 24.0))
	var c3 := get_viewport().get_camera_3d()
	if c3 is Camara:
		var cam: Camara = c3
		for d in ZOOM:
			if cam.distancia <= d:
				camara.zoom = Vector2.ONE * ZOOM[d]
				break
		camara.offset = Vector2(cam.h_offset, -cam.v_offset) * PX
	# numa luta com um boss, a câmara mostra os dois (e afasta-se se o boss for grande ou estiver longe)
	for b in get_tree().get_nodes_in_group("bosses"):
		if b is Boss and b.ativo and b.estado != "morto" and (b as Node3D).global_position.distance_to(j.global_position) < 26.0:
			var bp := ecra((b as Node3D).global_position) - Vector2(0, b._tamanho_px * 0.45)
			alvo = alvo.lerp(bp, 0.4)
			var precisa := absf(bp.y - alvo.y) * 2.0 + 140.0
			if precisa * camara.zoom.y > get_viewport_rect().size.y:
				camara.zoom = Vector2.ONE * maxf(2.0, floorf(get_viewport_rect().size.y / precisa))
			break
	camara.global_position = alvo
	if saltar:
		camara.reset_smoothing()
	RenderingServer.global_shader_parameter_set("jogador2d", alvo - Vector2(0, 2))
	RenderingServer.global_shader_parameter_set("jogador2d_chao", chao_px(j.global_position))


## A cor de tudo o que se vê, pela hora (CicloDia): dia claro, nascer e pôr do sol quentes, noite azul; o tempo
## nublado escurece um pouco e os relâmpagos dão um clarão.
func _luz_do_dia() -> void:
	var ciclo: CicloDia = null
	for n in cena.get_children():
		if n is CicloDia:
			ciclo = n
	var h := Tempo.hora
	var f := 1.0 if ciclo == null or ciclo.fechado else CicloDia.fator_dia(h)
	var por := 0.0 if ciclo == null or ciclo.fechado else clampf(1.0 - absf(h - 18.9) / 1.1, 0.0, 1.0) + clampf(1.0 - absf(h - 5.9) / 0.8, 0.0, 1.0)
	var c := Color(0.36, 0.4, 0.66).lerp(Color.WHITE, f)
	c = c * Color(1.0, 0.82, 0.66).lerp(Color.WHITE, 1.0 - clampf(por, 0.0, 1.0) * 0.9)   # tom quente ao nascer e ao pôr do sol
	if ciclo:
		var ef: String = ciclo.clima.get("efeito", "sol")
		if ef in ["chuva", "trovoada", "nublado", "nevao", "areia", "fumo"]:
			c = c * Color(0.84, 0.86, 0.9)
		elif ef == "escuro":
			c = c * Color(0.6, 0.6, 0.7)
		if ciclo._relampago > 0.0:
			c = c.lerp(Color(1.2, 1.2, 1.3), clampf(ciclo._relampago, 0.0, 1.0))
	if Jogo.dentro and Interior.atual and is_instance_valid(Interior.atual):   # dentro de casa: bem iluminado (velas à noite)
		c = Color(0.68, 0.6, 0.66) if f < 0.5 else Color.WHITE   # (à noite: à luz das velas e da lareira)
	elif Jogo.dentro and Masmorra.atual and is_instance_valid(Masmorra.atual):   # masmorras: à luz das tochas
		c = Color(0.62, 0.58, 0.68)
	elif LuzesGruta.ligada and not Jogo.dentro:   # grutas: escuro, mas vê-se o caminho (as luzes fazem o resto)
		c = Color(0.44, 0.42, 0.55) if not Jogo.buffs.has("visao_noturna") else Color(0.62, 0.62, 0.74)
	_luz_dia.color = _luz_dia.color.lerp(c, 0.1)
	# os candeeiros acendem-se quando escurece
	var escuro := 1.0 - clampf((c.r + c.g + c.b) / 3.0 * 1.6 - 0.45, 0.0, 1.0)
	for pl in _luzes_noite:
		if is_instance_valid(pl):
			pl.energy = escuro * 1.1
