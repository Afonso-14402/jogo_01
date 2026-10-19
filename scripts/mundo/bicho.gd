class_name Bicho
extends Node3D
## Um bicho pequeno de ambiente (dados/vida.json): borboletas, pássaros, coelhos, sapos, lagartos, caranguejos...
## Não se luta com eles: andam à vontade e fogem quando o jogador se aproxima.
##   voa   — anda no ar à volta de casa (borboleta, morcego, libelinha)
##   ave   — no chão a bicar; levanta voo se o jogador chegar perto e pousa noutro sítio
##   salta — dá saltinhos; foge aos saltos (coelho, sapo)
##   anda  — corre aos bocadinhos; foge a correr (lagarto, caranguejo)

const PASTA := "res://arte/vida/"
const ANIMS := {
	"voa": {"voar": [10, true]},
	"ave": {"parado": [3, true], "bicar": [8, true], "voar": [12, true]},
	"salta": {"parado": [3, true], "saltar": [10, false]},
	"anda": {"parado": [3, true], "correr": [12, true], "andar": [10, true]},
	"peixe": {"saltar": [8, false]},
}

var sprite_nome: String = "borboleta_amarela"
var tipo: String = "voa"
var mundo: Node          # o andar (altura_em, ponto_bicho)
var casa := Vector3.ZERO

var _s: AnimatedSprite3D
var _sombra: MeshInstance3D
var _alvo := Vector3.ZERO
var _t: float = 0.0
var _estado: String = "parado"
var _de := Vector3.ZERO
var _salto: float = 0.0
var _fase: float = 0.0
var _vel: float = 1.0

static var _cache: Dictionary = {}


static func frames(nome: String, t: String) -> SpriteFrames:
	var chave := nome + "|" + t
	if _cache.has(chave):
		return _cache[chave]
	var sf := SpriteFrames.new()
	sf.remove_animation("default")
	var anims: Dictionary = ANIMS.get(t, {})
	for a in anims:
		var caminho := "%s%s_%s.png" % [PASTA, nome, a]
		if not ResourceLoader.exists(caminho):
			continue
		var tex: Texture2D = load(caminho)
		var lado := tex.get_height()
		sf.add_animation(a)
		sf.set_animation_speed(a, anims[a][0])
		sf.set_animation_loop(a, anims[a][1])
		for i in range(tex.get_width() / lado):
			var at := AtlasTexture.new()
			at.atlas = tex
			at.region = Rect2(i * lado, 0, lado, lado)
			sf.add_frame(a, at)
	_cache[chave] = sf
	return sf


func _ready() -> void:
	var sf := frames(sprite_nome, tipo)
	if sf.get_animation_names().is_empty():
		queue_free()
		return
	var lado := 16
	var primeira: String = sf.get_animation_names()[0]
	lado = sf.get_frame_texture(primeira, 0).get_height()
	_s = Folhas.boneco(sf, lado)
	add_child(_s)
	_fase = randf() * TAU
	_vel = {"voa": 1.1, "ave": 1.0, "salta": 2.6, "anda": 2.2}.get(tipo, 1.0)
	if sprite_nome == "morcego":
		_vel = 2.6
	elif sprite_nome == "libelinha":
		_vel = 2.8
	if tipo != "voa":
		_sombra = Folhas.sombra(0.16)
		add_child(_sombra)
	else:
		_s.offset.y = 0.0
	_animar("voar" if tipo == "voa" else "parado")
	casa = global_position
	_alvo = global_position
	_s.frame = randi() % maxi(1, sf.get_frame_count(_s.animation))


func _animar(a: String) -> void:
	if _s.sprite_frames.has_animation(a):
		if _s.animation != a or not _s.is_playing():
			_s.play(a)
	elif a == "correr" and _s.sprite_frames.has_animation("andar"):
		_s.play("andar")


func _chao(p: Vector3) -> float:
	return mundo.altura_em(p.x, p.z) if mundo and mundo.has_method("altura_em") else 0.0


func _jogador() -> Node3D:
	return get_tree().get_first_node_in_group("jogador") as Node3D


func _process(delta: float) -> void:
	if _s == null:
		return
	_t -= delta
	_fase += delta
	var j := _jogador()
	var dj: float = INF
	if j:
		dj = Vector2(j.global_position.x - global_position.x, j.global_position.z - global_position.z).length()
	match tipo:
		"voa":
			_voar(delta)
		"ave":
			_ave(delta, j, dj)
		"salta":
			_saltar(delta, j, dj)
		"anda":
			_andar(delta, j, dj)


func _novo_alvo(raio: float) -> Vector3:
	var a := randf() * TAU
	var r := sqrt(randf()) * raio
	var p := casa + Vector3(cos(a) * r, 0, sin(a) * r)
	if mundo and mundo.has_method("ponto_aberto") and not mundo.ponto_aberto(p):
		return casa
	return p


func _voar(delta: float) -> void:
	var noturno := sprite_nome == "morcego"
	if _t <= 0.0 or Vector2(_alvo.x - position.x, _alvo.z - position.z).length() < 0.3:
		_alvo = _novo_alvo(6.0)
		_alvo.y = _chao(_alvo) + (randf_range(1.6, 3.4) if noturno else randf_range(0.5, 1.9))
		_t = randf_range(2.0, 5.0)
		if sprite_nome == "libelinha" and randf() < 0.4:
			_t = randf_range(0.6, 1.4)   # a libelinha para no ar de repente
			_alvo = position
	var d := _alvo - position
	if d.length() > 0.05:
		position += d.normalized() * minf(d.length(), _vel * delta)
		if absf(d.x) > 0.05:
			_s.flip_h = d.x < 0.0
	# bater de asas: sobe e desce um pouco
	_s.position.y = sin(_fase * (9.0 if noturno else 6.0)) * 0.08


func _ave(delta: float, j: Node3D, dj: float) -> void:
	if _estado == "voo":
		position += _de * delta
		_de.y = minf(_de.y + 2.0 * delta, 5.0)
		if _sombra:
			_sombra.global_position = Vector3(global_position.x, _chao(global_position) + 0.03, global_position.z)
			_sombra.visible = position.y - _chao(position) < 6.0
		if _t <= 0.0:   # pousa noutro sítio, longe do jogador
			var novo: Vector3 = mundo.ponto_bicho(j.global_position if j else Vector3.ZERO, 14.0) if mundo and mundo.has_method("ponto_bicho") else casa
			casa = novo
			position = Vector3(novo.x, _chao(novo), novo.z)
			if _sombra:
				_sombra.position = Vector3(0, 0.03, 0)
				_sombra.visible = true
			_estado = "parado"
			_animar("parado")
		return
	position.y = _chao(position)
	if dj < 4.0:
		_estado = "voo"
		_t = 4.0
		var fora := (global_position - j.global_position)
		fora.y = 0
		fora = fora.normalized() if fora.length() > 0.01 else Vector3.RIGHT
		_de = fora * 5.5 + Vector3(0, 3.0, 0)
		_s.flip_h = fora.x < 0.0
		_animar("voar")
		return
	if _t <= 0.0:
		_t = randf_range(0.8, 2.4)
		var r := randf()
		if r < 0.45:
			_animar("bicar")
		elif r < 0.75:
			_animar("parado")
		else:   # saltinho para o lado
			var p := _novo_alvo(1.2)
			_s.flip_h = p.x < position.x
			position = Vector3(p.x, _chao(p), p.z)
			_animar("parado")


func _saltar(delta: float, j: Node3D, dj: float) -> void:
	if _salto > 0.0:
		_salto -= delta
		var f := 1.0 - _salto / 0.45
		var p := _de.lerp(_alvo, clampf(f, 0.0, 1.0))
		position = Vector3(p.x, _chao(p) + sin(PI * clampf(f, 0.0, 1.0)) * 0.45, p.z)
		if _sombra:
			_sombra.position.y = _chao(p) - position.y + 0.03
		if _salto <= 0.0:
			_animar("parado")
			_t = 0.15 if _estado == "fuga" else randf_range(1.2, 3.5)
		return
	position.y = _chao(position)
	if _sombra:
		_sombra.position.y = 0.03
	_estado = "fuga" if dj < 5.0 else ("parado" if dj > 8.0 else _estado)
	if _t > 0.0:
		return
	_de = position
	if _estado == "fuga" and j:
		var fora := global_position - j.global_position
		fora.y = 0
		_alvo = position + fora.normalized() * 2.2
		if mundo and mundo.has_method("ponto_aberto") and not mundo.ponto_aberto(_alvo):
			_alvo = position + fora.normalized().rotated(Vector3.UP, PI / 2.0) * 2.0
	else:
		_alvo = _novo_alvo(3.0)
	_alvo.y = _chao(_alvo)
	_s.flip_h = _alvo.x < position.x
	_salto = 0.45
	_animar("saltar")
	_s.frame = 0


func _andar(delta: float, j: Node3D, dj: float) -> void:
	position.y = _chao(position)
	if dj < 4.5 and j:
		var fora := global_position - j.global_position
		fora.y = 0
		_alvo = position + fora.normalized() * 3.0
		_estado = "fuga"
		_t = 1.0
	var d := _alvo - position
	d.y = 0
	if d.length() > 0.1:
		var v := _vel * (1.8 if _estado == "fuga" else 1.0)
		var passo := d.normalized() * minf(d.length(), v * delta)
		if mundo and mundo.has_method("ponto_aberto") and not mundo.ponto_aberto(position + passo * 4.0):
			_alvo = position
		else:
			position += passo
		# o caranguejo anda de lado: não se vira
		if sprite_nome != "caranguejo":
			_s.flip_h = d.x < 0.0
		_animar("correr" if _estado == "fuga" or sprite_nome != "caranguejo" else "andar")
	else:
		_animar("parado")
		if _t <= 0.0:
			_estado = "parado"
			_t = randf_range(1.0, 4.0)
			if randf() < 0.6:
				_alvo = _novo_alvo(3.0)
