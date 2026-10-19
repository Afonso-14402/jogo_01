class_name ItemChao
extends Node3D
## Um item caído no chão: salta, flutua e vem ter com o jogador quando ele passa perto (íman).

var id: String = ""
var qtd: int = 1
var extra: Dictionary = {}
var ouro: int = 0
var _t: float = 0.0
var _sprite: Sprite3D
var _vel := Vector3.ZERO
var _apanhado := false


static func criar(id_: String, qtd_: int = 1, extra_: Dictionary = {}) -> ItemChao:
	var i := ItemChao.new()
	i.id = id_
	i.qtd = qtd_
	i.extra = extra_
	return i


static func moedas(valor: int) -> ItemChao:
	var i := ItemChao.new()
	i.ouro = valor
	return i


func _ready() -> void:
	_sprite = Sprite3D.new()
	var caminho: String = "res://arte/ui/mapa_missao.png" if ouro > 0 else Inventario._dados(id).get("icone", "")
	if ouro > 0 and ResourceLoader.exists("res://arte/icones/moeda_ouro.png"):
		caminho = "res://arte/icones/moeda_ouro.png"
	_sprite.texture = load(caminho) if ResourceLoader.exists(caminho) else load("res://arte/efeitos/brilho_item.png")
	_sprite.billboard = BaseMaterial3D.BILLBOARD_ENABLED
	_sprite.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
	_sprite.pixel_size = 1.0 / 20.0
	_sprite.shaded = false
	_sprite.position.y = 0.4
	add_child(_sprite)
	var r: String = extra.get("raridade", "comum")
	if r != "comum":
		_sprite.modulate = {"incomum": Color(0.8, 1.3, 0.8), "raro": Color(0.8, 0.9, 1.4), "epico": Color(1.2, 0.8, 1.4),
							"lendario": Color(1.5, 1.1, 0.6), "mitico": Color(1.6, 1.6, 1.6)}.get(r, Color.WHITE)
	_vel = Vector3(randf_range(-2, 2), 4.0, randf_range(-2, 2))


func _process(delta: float) -> void:
	_t += delta
	if _vel != Vector3.ZERO:
		position += _vel * delta
		_vel.y -= 14.0 * delta
		if position.y <= _chao() and _vel.y < 0.0:
			position.y = _chao()
			_vel = Vector3.ZERO
		return
	_sprite.position.y = 0.4 + sin(_t * 3.0) * 0.08
	var j := get_tree().get_first_node_in_group("jogador") as Node3D
	if j == null or _apanhado or _t < 0.5:
		return
	var d := j.global_position - global_position
	if d.length() < Grupo.raio_iman(float(Dados.c("item_iman", 1.6)) * 2.0):
		global_position += d.normalized() * min(d.length(), 9.0 * delta)
	if d.length() < 0.6:
		_apanhar()


func _chao() -> float:
	var a := get_parent()
	while a and not a is Andar:
		a = a.get_parent()
	return (a as Andar).altura_em(global_position.x, global_position.z) if a else 0.0


func _apanhar() -> void:
	_apanhado = true
	if ouro > 0:
		Jogo.ganhar_ouro(ouro, true)
		Sistema.mensagem("Obtiveste: %d de ouro" % ouro)
	elif not Jogo.apanhar(id, qtd, extra):
		_apanhado = false
		_t = -2.0   # mochila cheia: fica no chão
		return
	Audio.efeito("apanhar")
	queue_free()
