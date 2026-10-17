class_name Camara
extends Camera3D
## Câmara do jogo (docs/PROGRAMACAO.md, secção 4.2): perspetiva, FOV 30°, inclinada −35°, a ~16 m,
## segue o alvo com suavização e um pouco à frente; zoom com a roda; tremer().

var alvo: Node3D
var distancia: float = 16.0
var _tremor: float = 0.0
var _tremor_t: float = 0.0
var _avanco := Vector3.ZERO
var _transparentes: Array = []   # objetos que estão entre a câmara e o alvo (ficam meio transparentes)


func _ready() -> void:
	fov = float(Dados.c("camara_fov", 30.0))
	rotation_degrees.x = float(Dados.c("camara_inclinacao", -35.0))
	distancia = float(Dados.c("camara_distancia", 16.0))
	near = 0.5
	far = 200.0
	if alvo:
		global_position = _posicao_desejada()


func _process(delta: float) -> void:
	if alvo == null:
		return
	if Input.is_action_just_pressed("zoom_mais"):
		distancia = max(float(Dados.c("camara_distancia_min")), distancia - 1.5)
	if Input.is_action_just_pressed("zoom_menos"):
		distancia = min(float(Dados.c("camara_distancia_max")), distancia + 1.5)
	var vel: Vector3 = alvo.velocity if "velocity" in alvo else Vector3.ZERO
	var plano := Vector3(vel.x, 0, vel.z)
	var desejado_avanco := plano.normalized() * float(Dados.c("camara_avanco", 1.5)) if plano.length() > 0.5 else Vector3.ZERO
	_avanco = _avanco.lerp(desejado_avanco, clamp(2.0 * delta, 0.0, 1.0))
	var k: float = clamp(float(Dados.c("camara_suavizar", 8.0)) * delta, 0.0, 1.0)
	global_position = global_position.lerp(_posicao_desejada(), k)
	_ver_alvo()
	if _tremor_t > 0.0:
		_tremor_t -= delta
		h_offset = randf_range(-_tremor, _tremor)
		v_offset = randf_range(-_tremor, _tremor)
	else:
		h_offset = 0.0
		v_offset = 0.0


## Salta logo para o alvo (ao entrar ou sair de uma casa), sem viajar pelo mapa.
func saltar() -> void:
	_avanco = Vector3.ZERO
	if alvo:
		global_position = _posicao_desejada()


func _posicao_desejada() -> Vector3:
	var ang := deg_to_rad(-rotation_degrees.x)
	var foco := alvo.global_position + _avanco + Vector3(0, 0.8, 0)
	return foco + Vector3(0, sin(ang) * distancia, cos(ang) * distancia)


## O que estiver entre a câmara e o alvo (árvores, paredes, casas) fica meio transparente.
## Os objetos que tapam a vista estão no grupo "tapa_vista" e têm a meta "raio" (tamanho em metros).
func _ver_alvo() -> void:
	var tapam: Array = []
	var a := global_position
	var b := alvo.global_position + Vector3(0, 0.8, 0)
	for no in get_tree().get_nodes_in_group("tapa_vista"):
		var n3 := no as Node3D
		var raio: float = n3.get_meta("raio", 1.5) if n3 else 1.5
		if n3 == null or n3.global_position.distance_to(b) > 20.0 + raio:
			continue
		var centro := n3.global_position + Vector3(0, n3.get_meta("altura", raio), 0)
		var p := Geometry3D.get_closest_point_to_segment(centro, a, b)
		if p.distance_to(centro) < raio and p.distance_to(b) > 0.6:
			tapam.append(n3)
	for v in _transparentes:
		if is_instance_valid(v) and not v in tapam:
			_transparencia(v, 0.0)
	for v in tapam:
		_transparencia(v, 0.7)
	_transparentes = tapam


## Meio transparente: troca os materiais por cópias com alfa (funciona em todos os renderizadores).
static func _transparencia(no: Node, valor: float) -> void:
	if no is MeshInstance3D and no.mesh:
		var m: MeshInstance3D = no
		for i in m.mesh.get_surface_count():
			if valor <= 0.0:
				m.set_surface_override_material(i, null)
				continue
			if m.get_surface_override_material(i) != null:
				continue
			var base := m.mesh.surface_get_material(i)
			if base is StandardMaterial3D:
				var t: StandardMaterial3D = base.duplicate()
				t.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
				t.albedo_color.a = 1.0 - valor
				m.set_surface_override_material(i, t)
	for f in no.get_children():
		_transparencia(f, valor)


func tremer(forca: float = 0.15, duracao: float = 0.2) -> void:
	if not Opcoes.v("tremor"):
		return
	_tremor = forca
	_tremor_t = duracao
