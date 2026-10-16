class_name Transeunte
extends CharacterBody3D
## Gente na rua (docs/CIDADES.md, secção 4.1): pessoas sem nome, cada uma com um aspeto ao acaso (as mesmas peças
## do herói: penteado, pele, cabelo, olhos e roupa), que passeiam pela povoação e dizem uma frase se lhes falares.

const ANIMS := {"parado": [4, true], "andar": [8, true]}

var lugar: String = "ascendia"       # que lista de frases usa (dados/transeuntes.json)
var pontos: Callable                 # () -> Vector3: um sítio para onde ir a seguir
var aparencia: Dictionary = {}

var _s: AnimatedSprite3D
var _destino := Vector3.INF
var _espera: float = 0.0
var _preso: float = 0.0
var _ultima := Vector3.ZERO
var _balao: Label3D
var _balao_t: float = 0.0
var _gravidade: float = ProjectSettings.get_setting("physics/3d/default_gravity", 9.8)


static func aparencia_ao_acaso() -> Dictionary:
	var ap := {}
	for parte in ["penteado", "pele", "cabelo", "olhos", "roupa"]:
		var op := Aparencia.opcoes("penteados" if parte == "penteado" else parte)
		if not op.is_empty():
			ap[parte] = op.pick_random()
	return ap


func _ready() -> void:
	add_to_group("transeuntes")
	collision_layer = 0          # não empurram o herói nem os monstros
	collision_mask = 1
	var f := CollisionShape3D.new()
	var c := CapsuleShape3D.new()
	c.radius = 0.25
	c.height = 1.3
	f.shape = c
	f.position.y = 0.65
	add_child(f)
	if aparencia.is_empty():
		aparencia = aparencia_ao_acaso()
	_s = Folhas.boneco(Aparencia.frames(aparencia, ANIMS, ["baixo", "cima", "lado"]), 32)
	add_child(_s)
	add_child(Folhas.sombra(0.35))
	var inter := Interagivel.new()
	inter.texto = "Falar"
	add_child(inter)
	inter.usado.connect(_falar)
	_balao = Label3D.new()
	_balao.font_size = 36
	_balao.pixel_size = 0.006
	_balao.outline_size = 10
	_balao.billboard = BaseMaterial3D.BILLBOARD_ENABLED
	_balao.position.y = 2.3
	_balao.width = 420
	_balao.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	_balao.visible = false
	add_child(_balao)
	_anim("parado", "baixo")
	_espera = randf_range(0.0, 3.0)


func _anim(nome: String, dir: String) -> void:
	var a := "%s_%s" % [nome, dir]
	if _s.sprite_frames.has_animation(a) and _s.animation != a:
		_s.play(a)


## Uma frase ao acaso: a lista do sítio e, às vezes, uma das de "todos".
func frase() -> String:
	var t: Dictionary = Dados.tabela("transeuntes")
	var lista: Array = t.get(lugar, [])
	if lista.is_empty() or randf() < 0.3:
		lista = t.get("todos", ["Olá!"])
	return Sistema.genero(lista.pick_random())


func _falar(j: Node) -> void:
	_destino = Vector3.INF
	_espera = 3.5
	var d: Vector3 = (j as Node3D).global_position - global_position
	if absf(d.x) > absf(d.z):
		_anim("parado", "lado")
		_s.flip_h = d.x < 0.0
	else:
		_anim("parado", "baixo" if d.z > 0.0 else "cima")
	_balao.text = frase()
	_balao.visible = true
	_balao_t = 3.5


func _physics_process(delta: float) -> void:
	velocity.y = 0.0 if is_on_floor() else velocity.y - _gravidade * delta
	if _balao_t > 0.0:
		_balao_t -= delta
		_balao.visible = _balao_t > 0.0
	if _destino == Vector3.INF:
		velocity.x = 0.0
		velocity.z = 0.0
		_espera -= delta
		if _espera <= 0.0 and pontos.is_valid():
			_destino = pontos.call()
			_preso = 0.0
			_ultima = global_position
	else:
		var d := _destino - global_position
		d.y = 0.0
		_preso += delta
		if _preso > 2.5:   # encalhado numa parede: desiste e escolhe outro sítio
			if global_position.distance_to(_ultima) < 0.8:
				_destino = Vector3.INF
				_espera = 0.5
			_preso = 0.0
			_ultima = global_position
		if d.length() < 0.4:
			_destino = Vector3.INF
			_espera = randf_range(2.0, 7.0)   # para um bocado (a olhar as montras, a conversar...)
			_anim("parado", "baixo")
			velocity.x = 0.0
			velocity.z = 0.0
		elif _destino != Vector3.INF:
			var v := d.normalized() * 1.6
			velocity.x = v.x
			velocity.z = v.z
			if absf(d.x) > absf(d.z):
				_anim("andar", "lado")
				_s.flip_h = d.x < 0.0
			else:
				_anim("andar", "baixo" if d.z > 0.0 else "cima")
	move_and_slide()
