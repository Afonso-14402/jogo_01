extends Node
## Música (com mistura suave entre faixas) e efeitos sonoros. Os ficheiros vêm de res://musica e res://sons.

var _musica_a: AudioStreamPlayer
var _musica_b: AudioStreamPlayer
var _faixa_atual: String = ""
var volume_musica: float = 0.8
var volume_efeitos: float = 1.0


func _ready() -> void:
	_musica_a = AudioStreamPlayer.new()
	_musica_b = AudioStreamPlayer.new()
	add_child(_musica_a)
	add_child(_musica_b)


func tocar_musica(nome: String, mistura: float = 1.5) -> void:
	if nome == _faixa_atual:
		return
	var caminho := "res://musica/%s.ogg" % nome
	if not ResourceLoader.exists(caminho):
		return
	_faixa_atual = nome
	var nova := _musica_b if _musica_a.playing else _musica_a
	var velha := _musica_a if nova == _musica_b else _musica_b
	nova.stream = load(caminho)
	nova.volume_db = -40.0
	nova.play()
	var t := create_tween().set_parallel()
	t.tween_property(nova, "volume_db", linear_to_db(volume_musica), mistura)
	t.tween_property(velha, "volume_db", -40.0, mistura)


func efeito(nome: String) -> void:
	var caminho := "res://sons/%s.ogg" % nome
	if not ResourceLoader.exists(caminho):
		return
	var p := AudioStreamPlayer.new()
	p.stream = load(caminho)
	p.volume_db = linear_to_db(volume_efeitos)
	add_child(p)
	p.play()
	p.finished.connect(p.queue_free)
