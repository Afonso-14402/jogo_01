class_name Vida
extends Node3D
## A vida do andar (dados/vida.json, docs/ARTE.md 6.1): bichos de ambiente, partículas no ar (pirilampos, pólen,
## esporos, brasas, folhas a cair...), peixes a saltar na água e bandos de pássaros a passar no céu.
## Só os bichos perto do jogador se mexem (poupa o telemóvel).

const PERTO := 42.0
const AR := {
	# tipo: [cor, tamanho (m), quantidade, vida (s), gravidade, altura, textura]
	"pirilampos": ["#cddf6c", 0.11, 46, 5.0, Vector3(0, 0.02, 0), 1.1, ""],
	"polen": ["#fbff86", 0.07, 30, 7.0, Vector3(0.12, -0.02, 0.05), 1.6, ""],
	"esporos": ["#8fd3ff", 0.07, 40, 7.0, Vector3(0, 0.14, 0), 1.0, ""],
	"brasas": ["#f79617", 0.08, 50, 3.5, Vector3(0.1, 0.7, 0), 0.6, ""],
	"fogos_fatuos": ["#30e1b9", 0.18, 10, 7.0, Vector3(0, 0.05, 0), 1.3, ""],
	"orbes": ["#a884f3", 0.1, 34, 6.0, Vector3(0, 0.25, 0), 1.0, ""],
	"folhas_verde": ["#ffffff", 0.5, 14, 8.0, Vector3(0.35, -0.5, 0.15), 4.5, "res://arte/vida/folha_cair_verde.png"],
	"folhas_laranja": ["#ffffff", 0.5, 14, 8.0, Vector3(0.35, -0.5, 0.15), 4.5, "res://arte/vida/folha_cair_laranja.png"],
	"folhas_rosa": ["#ffffff", 0.5, 16, 8.0, Vector3(0.35, -0.5, 0.15), 4.5, "res://arte/vida/folha_cair_rosa.png"],
}
const MAU_TEMPO := ["chuva", "trovoada", "nevao", "areia"]

var mundo: Node
var regiao: int = 1

var _cfg: Dictionary = {}
var _bichos: Array[Bicho] = []
var _quando: Dictionary = {}      # Bicho / partículas -> "dia" · "noite" · "sempre"
var _ar: Array[CPUParticles3D] = []
var _agua: Array[Vector3] = []
var _t_ver: float = 0.0
var _t_peixe: float = 4.0
var _t_bando: float = 10.0
var _bandos: Array = []           # [{nos: [Node3D], sombras: [Node3D], vel: Vector3, t: float}]


func _ready() -> void:
	_cfg = Dados.tabela("vida").get(str(regiao), {})
	if _cfg.is_empty():
		return
	var abertas: int = mundo.celulas_abertas().size() if mundo and mundo.has_method("celulas_abertas") else 40
	for b in _cfg.get("bichos", []):
		var n := clampi(roundi(float(b.get("por_100", 4)) * abertas / 100.0), 1, 26)
		for i in n:
			var p: Vector3 = mundo.ponto_bicho(Vector3.INF, 0.0) if mundo else Vector3.ZERO
			if p == Vector3.INF:
				continue
			var bi := Bicho.new()
			var lista: Array = b.get("sprite", ["borboleta_amarela"])
			bi.sprite_nome = lista[i % lista.size()]
			bi.tipo = b.get("tipo", "voa")
			bi.mundo = mundo
			add_child(bi)
			bi.global_position = p + (Vector3(0, randf_range(0.6, 1.6), 0) if bi.tipo == "voa" else Vector3.ZERO)
			bi.casa = bi.global_position
			_bichos.append(bi)
			_quando[bi] = b.get("quando", "dia")
	for a in _cfg.get("ar", []):
		var p := _particulas(a.get("tipo", ""))
		if p:
			_quando[p] = a.get("quando", "sempre")
	if _cfg.get("peixes", false) and mundo and mundo.has_method("pontos_agua"):
		_agua = mundo.pontos_agua()
	_ver()


func _hora_de(q: String) -> bool:
	var h: float = Tempo.hora
	match q:
		"dia":
			return h >= 6.0 and h < 19.5
		"noite":
			return h >= 19.0 or h < 6.0
	return true


func _mau_tempo() -> bool:
	return str(Tempo.clima(regiao).get("efeito", "sol")) in MAU_TEMPO


## De segundo a segundo: quem aparece (hora e tempo) e quem se mexe (perto do jogador).
func _ver() -> void:
	var j := get_tree().get_first_node_in_group("jogador") as Node3D
	var mau := _mau_tempo()
	for b in _bichos:
		if not is_instance_valid(b):
			continue
		var q: String = _quando.get(b, "dia")
		var ativo := _hora_de(q) and not (mau and q == "dia")
		b.visible = ativo
		b.set_process(ativo and (j == null or b.global_position.distance_to(j.global_position) < PERTO))
	for p in _ar:
		var q: String = _quando.get(p, "sempre")
		p.emitting = _hora_de(q) and not (mau and p.name in ["polen", "pirilampos"])


func _process(delta: float) -> void:
	if _cfg.is_empty():
		return
	_t_ver -= delta
	if _t_ver <= 0.0:
		_t_ver = 1.0
		_ver()
	var j := get_tree().get_first_node_in_group("jogador") as Node3D
	if j == null:
		return
	for p in _ar:
		p.global_position = j.global_position + Vector3(0, float(p.get_meta("altura", 1.0)), -2.0)
		p.visible = not Jogo.dentro
	_peixes(delta, j)
	_passar_bandos(delta, j)


# ------------------------------------------------------------------ partículas ------------------------------------------------------------------

func _particulas(tipo: String) -> CPUParticles3D:
	if not AR.has(tipo):
		return null
	var d: Array = AR[tipo]
	var p := CPUParticles3D.new()
	p.name = tipo
	p.amount = int(d[2])
	p.lifetime = float(d[3])
	p.preprocess = float(d[3])
	p.local_coords = false
	p.emission_shape = CPUParticles3D.EMISSION_SHAPE_BOX
	p.emission_box_extents = Vector3(16, 1.0 if tipo != "fogos_fatuos" else 1.4, 13)
	p.gravity = d[4]
	p.direction = Vector3(0, 1, 0)
	p.spread = 180.0
	p.initial_velocity_min = 0.05
	p.initial_velocity_max = 0.35 if tipo != "brasas" else 0.8
	p.set_meta("altura", d[5])
	var q := QuadMesh.new()
	q.size = Vector2(d[1], d[1])
	var m := StandardMaterial3D.new()
	m.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	m.billboard_mode = BaseMaterial3D.BILLBOARD_PARTICLES
	m.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
	m.vertex_color_use_as_albedo = true
	var textura: String = d[6]
	if textura != "" and ResourceLoader.exists(textura):
		var tex: Texture2D = load(textura)
		m.albedo_texture = tex
		m.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA_SCISSOR
		m.particles_anim_h_frames = maxi(1, tex.get_width() / tex.get_height())
		m.particles_anim_v_frames = 1
		m.particles_anim_loop = true
		p.anim_speed_min = 0.6
		p.anim_speed_max = 1.2
		q.size = Vector2(0.3, 0.3)
		p.color = Color.WHITE
		m.shading_mode = BaseMaterial3D.SHADING_MODE_PER_PIXEL   # as folhas apanham a luz (à noite ficam escuras)
	else:
		m.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
		m.blend_mode = BaseMaterial3D.BLEND_MODE_ADD if tipo in ["pirilampos", "fogos_fatuos", "orbes", "brasas", "esporos"] else BaseMaterial3D.BLEND_MODE_MIX
		# acende e apaga devagar (os pirilampos piscam)
		var g := Gradient.new()
		var c := Color(d[0])
		g.offsets = PackedFloat32Array([0.0, 0.2, 0.45, 0.55, 0.8, 1.0])
		var meio := c if tipo != "pirilampos" else c * Color(1, 1, 1, 0.35)
		g.colors = PackedColorArray([Color(c, 0.0), c, meio, c, c, Color(c, 0.0)])
		p.color_ramp = g
	q.material = m
	p.mesh = q
	add_child(p)
	_ar.append(p)
	return p


# ------------------------------------------------------------------ peixes ------------------------------------------------------------------

func _peixes(delta: float, j: Node3D) -> void:
	if _agua.is_empty():
		return
	_t_peixe -= delta
	if _t_peixe > 0.0:
		return
	_t_peixe = randf_range(3.0, 8.0)
	var perto: Array[Vector3] = []
	for a in _agua:
		if a.distance_to(j.global_position) < 18.0:
			perto.append(a)
	if perto.is_empty():
		return
	var sf := Bicho.frames("peixe", "peixe")
	if not sf.has_animation("saltar"):
		return
	var s := Folhas.boneco(sf, sf.get_frame_texture("saltar", 0).get_height())
	add_child(s)
	s.global_position = perto[randi() % perto.size()] + Vector3(randf_range(-1.5, 1.5), 0.05, randf_range(-1.5, 1.5))
	s.flip_h = randf() < 0.5
	s.play("saltar")
	s.animation_finished.connect(s.queue_free)


# ------------------------------------------------------------------ bandos ------------------------------------------------------------------

func _passar_bandos(delta: float, j: Node3D) -> void:
	for b in _bandos.duplicate():
		b.t -= delta
		for i in b.nos.size():
			var n: Node3D = b.nos[i]
			n.global_position += b.vel * delta
			var sombra: Node3D = b.sombras[i]
			var chao: float = mundo.altura_em(n.global_position.x, n.global_position.z) if mundo else 0.0
			sombra.global_position = Vector3(n.global_position.x, chao + 0.04, n.global_position.z + 2.5)
		if b.t <= 0.0:
			for n in b.nos + b.sombras:
				n.queue_free()
			_bandos.erase(b)
	var sprite: String = _cfg.get("bandos", "")
	if sprite == "" or not _hora_de("dia") or _mau_tempo():
		return
	_t_bando -= delta
	if _t_bando > 0.0:
		return
	_t_bando = randf_range(22.0, 48.0)
	var sf := Bicho.frames(sprite, "ave")
	if not sf.has_animation("voar"):
		return
	var lado := -1.0 if randf() < 0.5 else 1.0
	var vel := Vector3(-lado * 7.0, 0, randf_range(-1.5, 1.5))
	var inicio := j.global_position + Vector3(lado * 26.0, 8.0, randf_range(-8.0, 4.0))
	var b := {"nos": [], "sombras": [], "vel": vel, "t": 8.0}
	var n := randi_range(3, 6)
	for i in n:
		var s := Folhas.boneco(sf, sf.get_frame_texture("voar", 0).get_height())
		s.offset.y = 0
		s.flip_h = vel.x < 0.0
		add_child(s)
		# em V: o primeiro à frente, os outros atrás e para os lados
		var k := (i + 1) / 2
		var lado_v := -1.0 if i % 2 else 1.0
		s.global_position = inicio + Vector3(lado * k * 1.3, randf_range(-0.3, 0.3), lado_v * k * 1.0)
		s.play("voar")
		s.frame = randi() % 4
		var sombra := Folhas.sombra(0.22)
		add_child(sombra)
		b.nos.append(s)
		b.sombras.append(sombra)
	_bandos.append(b)
