class_name Hitbox
extends Area3D
## Área que causa dano. Liga-se só durante os frames do golpe; cada alvo só leva 1 vez por golpe.

signal acertou(alvo: Node, golpe: Dictionary)

var dono: Node
var calcular_golpe: Callable   # func(alvo) -> Dictionary
var _ja: Array = []
var ligada: bool = false


func _ready() -> void:
	monitoring = false
	monitorable = false
	area_entered.connect(_entrou)


func ligar() -> void:
	_ja.clear()
	ligada = true
	monitoring = true
	# os que já estão dentro também contam
	await get_tree().physics_frame
	if ligada:
		for a in get_overlapping_areas():
			_entrou(a)


func desligar() -> void:
	ligada = false
	monitoring = false


func _entrou(area: Area3D) -> void:
	if not ligada or not area is Hurtbox:
		return
	var alvo: Node = area.dono
	if alvo == dono or alvo in _ja or not is_instance_valid(alvo):
		return
	_ja.append(alvo)
	var golpe: Dictionary = calcular_golpe.call(alvo)
	golpe["origem"] = dono.global_position if dono is Node3D else global_position
	golpe["atacante"] = dono
	if alvo.has_method("receber_golpe"):
		alvo.receber_golpe(golpe)
	acertou.emit(alvo, golpe)


## Uma caixa à frente do dono, em "distancia" metros.
static func caixa(largura: float, comprimento: float, altura: float = 1.6) -> CollisionShape3D:
	var f := CollisionShape3D.new()
	var b := BoxShape3D.new()
	b.size = Vector3(largura, altura, comprimento)
	f.shape = b
	f.position = Vector3(0, altura / 2.0, -comprimento / 2.0)
	return f
