class_name Arena
extends Node3D
## A Arena da Capitã Freya (docs/ATIVIDADES.md 4.6 e 4.9; dados/minijogos.json, "arena"): ondas de monstros das
## regiões já conhecidas, numa arena redonda com bancadas e público. Constrói-se longe (como as casas por dentro).
## Perder não é morrer: sais com 1 HP e sem prémio.

const ORIGEM := Vector3(0, -700, 0)
const RAIO := 13.0

static var atual: Arena

var cat: Dictionary = {}
var porta := Vector3.ZERO
var _onda: int = 0
var _vivos: int = 0
var _pausa: float = -1.0
var _cfg: Dictionary = {}
var _publico: Array[Node3D] = []
var _rng := RandomNumberGenerator.new()
var _acabou: bool = false


static func entrar(mundo: Node, categoria: String, porta_: Vector3) -> void:
	if atual != null and is_instance_valid(atual):
		return
	var cfg: Dictionary = Dados.tabela("minijogos")
	for c in cfg.get("arena", []):
		if c.id == categoria:
			if not Condicoes.avaliar(c.get("cond", "")):
				Sistema.mensagem("A Arena de %s abre com: %s." % [c.nome_pt, c.abre_pt], "aviso")
				return
			var a := Arena.new()
			a.cat = c
			a.porta = porta_
			a.position = ORIGEM   # antes de entrar na árvore: o _ready já constrói tudo no sítio certo
			mundo.add_child(a)
			atual = a
			Jogo.dentro = true
			var j := mundo.get_tree().get_first_node_in_group("jogador") as Node3D
			if j:
				j.global_position = ORIGEM + Vector3(0, 0.5, RAIO - 3.0)
			var cam := mundo.get_viewport().get_camera_3d()
			if cam and cam.has_method("saltar"):
				cam.saltar()
			Sistema.mensagem("Arena de %s: %d ondas. Boa sorte!" % [c.nome_pt, int(c.ondas)], "andar")
			return


func _ready() -> void:
	_cfg = Dados.tabela("minijogos")
	_rng.randomize()
	var corpo := StaticBody3D.new()
	add_child(corpo)
	var escuro := StandardMaterial3D.new()
	escuro.albedo_color = Color("2e222f")
	escuro.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	_caixa(Vector3(0, -0.5, 0), Vector3(120, 0.2, 120), escuro, null)
	# a areia
	var areia := _material("res://arte/regioes/r06_oceano/natureza/chao_base.png", 0.25)
	var chao := MeshInstance3D.new()
	var cil := CylinderMesh.new()
	cil.top_radius = RAIO
	cil.bottom_radius = RAIO
	cil.height = 0.2
	cil.radial_segments = 48
	chao.mesh = cil
	chao.material_override = areia
	chao.position.y = -0.1
	add_child(chao)
	var f := CollisionShape3D.new()
	var cc := CylinderShape3D.new()
	cc.radius = RAIO
	cc.height = 0.2
	f.shape = cc
	f.position.y = -0.1
	corpo.add_child(f)
	# o muro à volta e as bancadas (três degraus) com público
	var pedra := _material("res://arte/interiores/parede_pedra.png", 0.5)
	var madeira := _material("res://arte/interiores/chao_madeira.png", 0.5)
	for k in 32:
		var ang := k * TAU / 32.0
		var dir := Vector3(cos(ang), 0, sin(ang))
		var b := _caixa(dir * (RAIO + 0.3), Vector3(2.7, 1.6, 0.6), pedra, corpo)
		b.look_at(global_position + dir * 100.0 + Vector3(0, 0.8, 0), Vector3.UP)
		b.global_position = ORIGEM + dir * (RAIO + 0.3) + Vector3(0, 0.8, 0)
		for d in 3:
			var g := _caixa(dir * (RAIO + 1.6 + d * 1.4), Vector3(3.2 + d * 0.3, 0.6, 1.4), madeira, null)
			g.look_at(ORIGEM + dir * 100.0, Vector3.UP)
			g.global_position = ORIGEM + dir * (RAIO + 1.6 + d * 1.4) + Vector3(0, 1.6 + d * 0.6, 0)
			if _rng.randf() < 0.55 and sin(ang) < 0.2:   # público (não à frente da câmara)
				_espectador(ORIGEM + dir * (RAIO + 1.6 + d * 1.4) + Vector3(0, 1.9 + d * 0.6, 0))
	for k in 4:   # tochas
		var l := OmniLight3D.new()
		l.light_color = Color("f79617")
		l.omni_range = 12.0
		l.light_energy = 1.2
		var ang := k * TAU / 4.0 + PI / 4.0
		l.position = Vector3(cos(ang), 0, sin(ang)) * (RAIO - 1.0) + Vector3(0, 3.0, 0)
		add_child(l)
	_pausa = 2.0


func _material(caminho: String, esc: float) -> StandardMaterial3D:
	var m := StandardMaterial3D.new()
	if ResourceLoader.exists(caminho):
		m.albedo_texture = load(caminho)
	m.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
	m.uv1_triplanar = true
	m.uv1_world_triplanar = true
	m.uv1_scale = Vector3.ONE * esc
	return m


func _caixa(p: Vector3, tam: Vector3, mat: Material, corpo: StaticBody3D) -> MeshInstance3D:
	var mi := MeshInstance3D.new()
	var b := BoxMesh.new()
	b.size = tam
	mi.mesh = b
	mi.material_override = mat
	mi.position = p
	add_child(mi)
	if corpo:
		var c := CollisionShape3D.new()
		var s := BoxShape3D.new()
		s.size = tam
		c.shape = s
		c.position = p + Vector3(0, tam.y / 2.0, 0)
		corpo.add_child(c)
	return mi


func _espectador(p: Vector3) -> void:
	var s := Folhas.boneco(Aparencia.frames(Transeunte.aparencia_ao_acaso(), {"parado": [4, true]}, ["baixo"]), 32)
	add_child(s)
	s.global_position = p
	s.play("parado_baixo")
	_publico.append(s)


func _process(delta: float) -> void:
	# o público salta quando acaba uma onda
	for i in _publico.size():
		var s := _publico[i]
		s.offset.y = 16.0 + (absf(sin(Time.get_ticks_msec() / 120.0 + i)) * 4.0 if _pausa > 0.0 else 0.0)
	if _acabou or _pausa < 0.0:
		return
	_pausa -= delta
	if _pausa <= 0.0:
		_pausa = -1.0
		_nova_onda()


func _pool() -> Array:
	var r := []
	for m in Dados.tabela("monstros").values():
		if int(m.get("regiao", 1)) <= int(cat.get("regioes", 3)) and m.get("tipo", "") in ["fraco", "normal", "rapido", "tanque", "mago", "voador"]:
			r.append(m.id)
	return r


func _nova_onda() -> void:
	_onda += 1
	var total := int(cat.get("ondas", 5))
	var ultima_boss: bool = cat.get("boss", false) and _onda == total
	Sistema.mensagem("Onda %d/%d%s" % [_onda, total, " — BOSS DESPERTO!" if ultima_boss else ""], "andar")
	var pool := _pool()
	var n := 1 if ultima_boss else mini(int(_cfg.get("arena_max_onda", 6)), 2 + _onda / 2)
	_vivos = 0
	for i in n:
		var id: String = pool[_rng.randi() % pool.size()]
		if ultima_boss:
			var fortes: Array = Dados.tabela("monstros").values().filter(func(m): return m.get("tipo", "") == "com_nome")
			if not fortes.is_empty():
				id = fortes[_rng.randi() % fortes.size()].id
		var m := Monstro.new().configurar(id, Jogo.nivel + _onda / 3 + (5 if ultima_boss else 0), "elite" if ultima_boss else "")
		add_child(m)
		var ang := _rng.randf() * TAU
		m.global_position = ORIGEM + Vector3(cos(ang), 0, sin(ang)) * 8.0 + Vector3(0, 0.5, 0)
		m.morreu.connect(_morreu)
		_vivos += 1


func _morreu(_m: Monstro) -> void:
	_vivos -= 1
	if _vivos > 0 or _acabou:
		return
	if _onda >= int(cat.get("ondas", 5)):
		_ganhar()
		return
	Jogo.hp = minf(Jogo.hp_maximo(), Jogo.hp + Jogo.hp_maximo() * float(_cfg.get("arena_cura", 0.2)))
	Sistema.mensagem("Onda vencida! O público aplaude.", "nivel")
	_pausa = float(_cfg.get("arena_pausa", 3.0))


func _ganhar() -> void:
	_acabou = true
	_pausa = 3.0
	Jogo.ganhar_ouro(int(cat.get("ouro", 1000)))
	# uma arma do tier mais alto que já conheces, com a raridade do prémio
	var tier := clampi((Jogo.andar_maximo - 1) / 10 + 1, 1, 10)
	var armas := []
	for id in Dados.tabela("armas"):
		var a: Dictionary = Dados.tabela("armas")[id]
		if int(a.get("tier", 0)) == tier and a.get("categoria", "") == "normal":
			armas.append(id)
	if not armas.is_empty():
		var arma: String = armas[_rng.randi() % armas.size()]
		Jogo.inventario.adicionar(arma, 1, {"raridade": cat.get("raridade", "raro")})
		Sistema.mensagem("Prémio da Arena: %s (%s)!" % [Dados.arma(arma).get("nome_pt", arma), cat.get("raridade", "raro")], "nivel")
	if cat.get("titulo_pt", "") != "":
		Jogo.por_flag("titulo_" + String(cat.titulo_pt).to_snake_case())
		Colecoes.verificar()
	Jogo.por_flag("arena_venceu_" + String(cat.id))
	Sistema.mensagem("VENCESTE A ARENA DE %s! +%d ouro." % [String(cat.nome_pt).to_upper(), int(cat.get("ouro", 0))], "nivel")
	get_tree().create_timer(3.0).timeout.connect(sair)


## Perder: não se morre na Arena (docs/ATIVIDADES.md 4.9).
func perder() -> void:
	if _acabou:
		return
	_acabou = true
	Jogo.hp = 1.0
	Sistema.mensagem("Caíste na areia… A Capitã Freya tira-te da arena. Para a próxima!", "aviso")
	sair()


func sair() -> void:
	var j := get_tree().get_first_node_in_group("jogador") as Node3D
	if j:
		j.global_position = porta + Vector3(0, 0.5, 0)
		if j.has_method("mudar_estado"):
			j.mudar_estado("normal")
	Jogo.dentro = false
	atual = null
	var cam := get_viewport().get_camera_3d()
	if cam and cam.has_method("saltar"):
		cam.saltar()
	queue_free()
