class_name CicloDia
extends Node
## Dia e noite e tempo atmosférico (docs/SISTEMAS.md, secção 14): a luz do sol, o céu e o nevoeiro mudam com a hora;
## o clima do dia (chuva, neve, nevoeiro, areia, cinza...) mostra partículas e muda a luz. A chuva deixa Encharcado.
## Em andares fechados (grutas) a hora não muda a luz.

const NOITE := Color("1c1b33")
const ENTARDECER := Color("f79617")
const COR_SOL := Color("fff4e0")
const COR_POR := Color("fca790")
const COR_LUA := Color("8fd3ff")

var env: Environment
var sol: DirectionalLight3D
var ceu := Color("7fa0c8")
var nevoeiro := Color("c8e0d0")
var densidade: float = 0.01
var luz: float = 0.6
var fechado := false
var regiao := 0
var clima: Dictionary = {}
var _particulas: CPUParticles3D
var _relampago := 0.0
var _proximo_relampago := 8.0
var _t_chuva := 0.0


func _ready() -> void:
	clima = Tempo.clima(regiao)
	_aplicar_clima()
	Tempo.novo_dia.connect(func(_d):
		clima = Tempo.clima(regiao)
		_aplicar_clima())


## 0 de noite, 1 de dia, a passar devagar na madrugada (5–6) e ao entardecer (18–20).
static func fator_dia(h: float) -> float:
	if h >= 6.0 and h < 18.0:
		return 1.0
	if h >= 5.0 and h < 6.0:   # madrugada
		return smoothstep(5.0, 6.0, h)
	if h >= 18.0 and h < 20.0:
		return 1.0 - smoothstep(18.0, 20.0, h)
	return 0.0


func _process(delta: float) -> void:
	var h := Tempo.hora
	var f := 1.0 if fechado else fator_dia(h)
	var por := 0.0 if fechado else clampf(1.0 - absf(h - 19.0), 0.0, 1.0) + clampf(1.0 - absf(h - 5.8) * 1.5, 0.0, 1.0)
	var nublado := 0.55 if clima.get("efeito", "sol") in ["chuva", "trovoada", "nublado", "nevao", "areia", "fumo"] else 1.0
	if clima.get("efeito", "") == "escuro":
		nublado = 0.4
	if sol:
		var alto := sin(PI * clampf((h - 6.0) / 12.0, 0.0, 1.0))
		sol.rotation_degrees.x = -lerpf(25.0, 62.0, alto) if f > 0.0 else -50.0
		sol.light_energy = lerpf(0.14, 0.75, f) * nublado + _relampago * 2.5
		sol.light_color = COR_LUA.lerp(COR_SOL, f).lerp(COR_POR, por * 0.6)
	if env:
		var c := NOITE.lerp(ceu, f).lerp(ENTARDECER, por * 0.35)
		if nublado < 1.0:
			c = c.lerp(Color("625565"), 0.35)
		env.background_color = c.lerp(Color.WHITE, _relampago * 0.6)
		env.ambient_light_color = c.lerp(Color.WHITE, 0.25)
		env.ambient_light_energy = luz * 0.55 * lerpf(0.45, 1.0, f) + _relampago
		env.fog_light_color = nevoeiro.lerp(c, 0.5).lerp(NOITE, (1.0 - f) * 0.6)
	_efeitos(delta)


func _aplicar_clima() -> void:
	if _particulas:
		_particulas.queue_free()
		_particulas = null
	var ef: String = clima.get("efeito", "sol")
	if env:
		var mult: float = {"nevoeiro": 2.5, "nevoeiro_roxo": 2.5, "fumo": 1.8, "areia": 2.0, "nevao": 2.0, "chuva": 1.4, "trovoada": 1.5}.get(ef, 1.0)
		env.fog_density = densidade * 0.35 * mult
		if ef == "nevoeiro_roxo":
			nevoeiro = Color("6b3e75")
		elif ef == "areia":
			nevoeiro = Color("f9c22b")
	if fechado:
		return
	match ef:
		"chuva", "trovoada":
			_particulas = _chuva(700 if ef == "chuva" else 1100)
		"neve":
			_particulas = _flocos("res://arte/efeitos/particula_neve.png", 300, -2.0, Vector3(0.6, 0, 0.2))
		"nevao":
			_particulas = _flocos("res://arte/efeitos/particula_neve.png", 900, -4.0, Vector3(5.0, 0, 1.0))
		"cinza":
			_particulas = _flocos("res://arte/efeitos/particula_cinza.png", 250, -1.2, Vector3(0.4, 0, 0.3))
		"brasas":
			_particulas = _flocos("res://arte/efeitos/particula_brasa.png", 200, -3.0, Vector3(0.5, 0, 0.5))
		"areia":
			_particulas = _flocos("res://arte/efeitos/poeira.png", 400, -0.3, Vector3(9.0, 0, 2.0))
	if _particulas:
		add_child(_particulas)
	if ef != "sol" and ef != "nenhum":
		Sistema.mensagem("Tempo: %s." % clima.get("nome_pt", ef))


func _chuva(n: int) -> CPUParticles3D:
	var p := _base(n, 0.9)
	var q := QuadMesh.new()
	q.size = Vector2(0.03, 0.55)
	var m := StandardMaterial3D.new()
	m.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	m.albedo_color = Color(0.56, 0.83, 1.0, 0.55)
	m.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
	m.billboard_mode = BaseMaterial3D.BILLBOARD_FIXED_Y
	q.material = m
	p.mesh = q
	p.gravity = Vector3(0, -38, 0)
	p.initial_velocity_min = 4.0
	p.initial_velocity_max = 6.0
	p.direction = Vector3(0.1, -1, 0)
	return p


func _flocos(textura: String, n: int, queda: float, vento: Vector3) -> CPUParticles3D:
	var p := _base(n, 6.0)
	var q := QuadMesh.new()
	q.size = Vector2(0.25, 0.25)
	var m := StandardMaterial3D.new()
	m.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	m.albedo_texture = load(textura) if ResourceLoader.exists(textura) else null
	m.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
	m.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA_SCISSOR
	m.billboard_mode = BaseMaterial3D.BILLBOARD_ENABLED
	if textura.ends_with("poeira.png"):   # a folha da poeira tem 4 frames: usa só o primeiro
		m.uv1_scale = Vector3(0.25, 1, 1)
		m.albedo_color = Color("fbb954")
	q.material = m
	p.mesh = q
	p.gravity = Vector3(vento.x, queda, vento.z)
	p.initial_velocity_min = 0.2
	p.initial_velocity_max = 0.8
	p.direction = Vector3(0, -1, 0)
	p.spread = 30.0
	return p


func _base(n: int, vida: float) -> CPUParticles3D:
	var p := CPUParticles3D.new()
	p.amount = n
	p.lifetime = vida
	p.preprocess = vida
	p.local_coords = false
	p.emission_shape = CPUParticles3D.EMISSION_SHAPE_BOX
	p.emission_box_extents = Vector3(22, 1, 18)
	return p


func _efeitos(delta: float) -> void:
	var cam := get_viewport().get_camera_3d()
	var j := get_tree().get_first_node_in_group("jogador")
	var centro: Vector3 = j.global_position if j else (cam.global_position if cam else Vector3.ZERO)
	if _particulas:
		_particulas.global_position = centro + Vector3(0, 11, 0)
	var ef: String = clima.get("efeito", "sol")
	# trovoada: relâmpagos de vez em quando
	_relampago = maxf(0.0, _relampago - delta * 4.0)
	if ef == "trovoada" and not fechado:
		_proximo_relampago -= delta
		if _proximo_relampago <= 0.0:
			_proximo_relampago = randf_range(6.0, 14.0)
			_relampago = 1.0
			if cam and cam.has_method("tremer"):
				cam.tremer(0.1, 0.3)
	# a chuva deixa Encharcado (raio ×1,5, fogo ×0,5)
	if ef in ["chuva", "trovoada"] and not fechado and j and "estados" in j and j.estados:
		_t_chuva += delta
		if _t_chuva >= float(Dados.c("chuva_encharcado_cada", 4.0)):
			_t_chuva = 0.0
			j.estados.aplicar("encharcado")
