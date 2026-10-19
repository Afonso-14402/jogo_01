extends Node
## Ações de entrada (docs/PROGRAMACAO.md, secção 8) e o tipo de controlo em uso (teclado, comando ou toque).

signal dispositivo_mudou(tipo: String)

var dispositivo: String = "teclado"

# ação: [teclas..., "rato:1", "pad:0" (botão), "eixo:0+" (eixo do comando)]
const ACOES := {
	"mover_cima": [KEY_W, KEY_UP, "eixo:1-"],
	"mover_baixo": [KEY_S, KEY_DOWN, "eixo:1+"],
	"mover_esquerda": [KEY_A, KEY_LEFT, "eixo:0-"],
	"mover_direita": [KEY_D, KEY_RIGHT, "eixo:0+"],
	"atacar": ["rato:1", "pad:2"],
	"ataque_forte": ["rato:2", "pad:3"],
	"esquivar": [KEY_SPACE, "pad:1"],
	"interagir": [KEY_E, "pad:0"],
	"skill_1": [KEY_1], "skill_2": [KEY_2], "skill_3": [KEY_3],
	"skill_4": [KEY_4], "skill_5": [KEY_5], "skill_6": [KEY_6],
	"pocao": [KEY_Q, "pad:12"],
	"trocar_arma": [KEY_R, "pad:11"],
	"skill_unica": [KEY_F],
	"correr": [KEY_SHIFT, "pad:7"],
	"mapa": [KEY_M, KEY_TAB, "pad:4"],
	"inventario": [KEY_I],
	"status": [KEY_C],
	"diario": [KEY_J],
	"pausa": [KEY_ESCAPE, KEY_P, "pad:6"],
	"montada": [KEY_Z, "pad:8"],
	"zoom_mais": ["roda:4"],
	"zoom_menos": ["roda:5"],
}


func _ready() -> void:
	criar_acoes()


func criar_acoes() -> void:
	for acao in ACOES:
		if InputMap.has_action(acao):
			continue
		InputMap.add_action(acao, 0.3)
		for e in ACOES[acao]:
			InputMap.action_add_event(acao, _evento(e))


static func _evento(e: Variant) -> InputEvent:
	if e is int:
		var k := InputEventKey.new()
		k.physical_keycode = e
		return k
	var partes: PackedStringArray = String(e).split(":")
	match partes[0]:
		"rato", "roda":
			var m := InputEventMouseButton.new()
			m.button_index = int(partes[1])
			return m
		"pad":
			var b := InputEventJoypadButton.new()
			b.button_index = int(partes[1])
			return b
		"eixo":
			var a := InputEventJoypadMotion.new()
			a.axis = int(partes[1].left(1))
			a.axis_value = -1.0 if partes[1].ends_with("-") else 1.0
			return a
	return null


func _input(evento: InputEvent) -> void:
	var tipo := dispositivo
	if (evento is InputEventMouse) and evento.device == InputEvent.DEVICE_ID_EMULATION:
		return   # rato "fingido" a partir de um toque: não muda o dispositivo
	if evento is InputEventKey or evento is InputEventMouseButton:
		tipo = "teclado"
	elif evento is InputEventJoypadButton or (evento is InputEventJoypadMotion and abs(evento.axis_value) > 0.5):
		tipo = "comando"
	elif evento is InputEventScreenTouch:
		tipo = "toque"
	if tipo != dispositivo:
		dispositivo = tipo
		_rato_nas_acoes(tipo != "toque")   # no telemóvel, tocar no ecrã não pode contar como "clique para atacar"
		dispositivo_mudou.emit(tipo)


func _rato_nas_acoes(com_rato: bool) -> void:
	for acao in ACOES:
		for e in ACOES[acao]:
			if e is String and (e.begins_with("rato:") or e.begins_with("roda:")):
				var ev := _evento(e)
				if com_rato and not InputMap.action_has_event(acao, ev):
					InputMap.action_add_event(acao, ev)
				elif not com_rato:
					InputMap.action_erase_event(acao, ev)


## É um telemóvel ou tablet? (mostra os controlos de toque)
func e_telemovel() -> bool:
	return OS.has_feature("mobile") or OS.has_feature("web_android") or OS.has_feature("web_ios") or dispositivo == "toque"


## Direção do movimento (x = direita, y = baixo no ecrã), com zona morta.
func direcao() -> Vector2:
	return Input.get_vector("mover_esquerda", "mover_direita", "mover_cima", "mover_baixo")
