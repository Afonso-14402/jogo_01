class_name Hurtbox
extends Area3D
## Área que recebe dano: diz quem é o dono (o jogador ou um monstro).

var dono: Node


static func criar(dono_: Node, camada: int, raio: float = 0.45, altura: float = 1.4) -> Hurtbox:
	var h := Hurtbox.new()
	h.dono = dono_
	h.collision_layer = camada
	h.collision_mask = 0
	h.monitoring = false
	var f := CollisionShape3D.new()
	var c := CapsuleShape3D.new()
	c.radius = raio
	c.height = max(altura, raio * 2.0)
	f.shape = c
	f.position.y = c.height / 2.0
	h.add_child(f)
	return h
