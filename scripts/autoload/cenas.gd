extends Node
## Troca de cena com uma transição simples (escurecer e clarear).

var _cortina: ColorRect
var _camada: CanvasLayer


func _ready() -> void:
	_camada = CanvasLayer.new()
	_camada.layer = 100
	add_child(_camada)
	_cortina = ColorRect.new()
	_cortina.color = Color(0.18, 0.13, 0.18, 0.0)
	_cortina.set_anchors_preset(Control.PRESET_FULL_RECT)
	_cortina.mouse_filter = Control.MOUSE_FILTER_IGNORE
	_camada.add_child(_cortina)


func mudar(caminho: String, duracao: float = 0.3) -> void:
	var t := create_tween()
	t.tween_property(_cortina, "color:a", 1.0, duracao)
	await t.finished
	get_tree().change_scene_to_file(caminho)
	var t2 := create_tween()
	t2.tween_property(_cortina, "color:a", 0.0, duracao)
