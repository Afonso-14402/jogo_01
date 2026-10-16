class_name Interagivel
extends Area3D
## Algo com que o jogador interage com a tecla E (baú, NPC, nó de recolha, porta...) a menos de 1,5 m.
## O jogador procura o Interagivel mais perto e chama interagir(jogador).

signal usado(jogador: Node)

@export var texto: String = "Usar"
var ativo: bool = true


func _ready() -> void:
	add_to_group("interagivel")
	collision_layer = 1 << 6
	collision_mask = 0
	monitoring = false
	if get_child_count() == 0:
		var f := CollisionShape3D.new()
		var s := SphereShape3D.new()
		s.radius = 0.8
		f.shape = s
		f.position.y = 0.5
		add_child(f)


func interagir(jogador: Node) -> void:
	if ativo:
		usado.emit(jogador)
