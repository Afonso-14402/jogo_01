class_name Escondido
extends Node3D
## Um companheiro escondido à espera num sítio afastado do andar (docs/NPCS.md, secção 4.2). Brilha um pouco para
## se ver de perto; com a tecla E abre a janela Grupo com o cartão dele (o que pede e a habilidade especial).

const ANIMS := {"parado": [4, true]}

var id: String = ""
var _sprite: AnimatedSprite3D


func _ready() -> void:
	add_to_group("escondidos")
	var d := Grupo.dados(id)
	_sprite = Folhas.boneco(Folhas.criar(String(d.get("sprite", "res://arte/npcs/" + id)), ANIMS, ["baixo"]), 32)
	add_child(_sprite)
	_sprite.play("parado_baixo")
	add_child(Folhas.sombra(0.4))
	var inter := Interagivel.new()
	inter.texto = "Falar com %s" % d.get("nome_pt", id)
	add_child(inter)
	inter.usado.connect(func(_j):
		var ui = get_tree().get_first_node_in_group("grupo_ui")
		if ui:
			ui.abrir_recrutar(id))
	# um brilho que sobe de vez em quando (para quem passa perto reparar)
	var t := create_tween().set_loops()
	t.tween_interval(2.5)
	t.tween_callback(func(): EfeitosCombate.animado(get_tree(), "brilho_item", global_position + Vector3(randf_range(-0.4, 0.4), 1.6, 0.1), 10.0))


func _process(_delta: float) -> void:
	if Grupo.conhecido(id):   # já foi recrutado: o boneco do companheiro substitui este
		queue_free()
