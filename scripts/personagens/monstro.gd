class_name Monstro
extends CharacterBody3D
## Monstro base (docs/PROGRAMACAO.md, secção 6; docs/SISTEMAS.md, secção 6).
## Valores pelo nível e pelo tipo; IA: DESCANSO → ALERTA → PERSEGUIR → ATACAR (com aviso) → REGRESSO / FUGIR → MORTO.

signal morreu(monstro: Monstro)

const ANIMS := {"parado": [5, true], "mover": [8, true], "atacar": [10, false], "dano": [8, false], "morrer": [7, false]}
const ATAQUE_PADRAO := {"id": "golpe", "mult": 1.0, "alcance": 1.5, "aviso": 0.4, "recarga": 1.4}

var id: String = ""
var dados: Dictionary = {}
var nivel: int = 1
var tipo: String = "normal"
var hp: float = 1.0
var hp_max: float = 1.0
var atq: float = 1.0
var def: float = 0.0
var res: float = 0.0
var vel: float = 3.0
var ponto_inicial := Vector3.ZERO
var olhar_x: float = 1.0
var estado: String = "descanso"

var sprite: AnimatedSprite3D
var hitbox: Hitbox
var hurtbox: Hurtbox
var estados: Estados
var _mira: Node3D
var _marca: MeshInstance3D
var _alvo: Node3D
var _t: float = 0.0
var _recargas: Dictionary = {}
var _ataque: Dictionary = {}
var _passeio := Vector3.ZERO
var _gravidade: float = ProjectSettings.get_setting("physics/3d/default_gravity", 9.8)
var _tamanho_px: int = 32
static var _atacantes: int = 0


## id: o monstro em dados/monstros.json · nivel: o do andar · tipo_extra: "elite", "com_nome"... (ou "")
func configurar(id_: String, nivel_: int, tipo_extra: String = "") -> Monstro:
	id = id_
	nivel = nivel_
	dados = Dados.monstro(id)
	if dados.is_empty():
		dados = Dados.obter("bosses", id)
	tipo = tipo_extra if tipo_extra != "" else dados.get("tipo", "normal")
	return self


func _ready() -> void:
	add_to_group("monstros")
	collision_layer = 1 << 2
	collision_mask = 1 | (1 << 2)
	ponto_inicial = global_position
	var c := Dados.constantes
	var m: Dictionary = c.tipos_monstro.get(tipo, c.tipos_monstro.normal)
	hp_max = Formulas.monstro_hp(c, nivel, m.hp)
	hp = hp_max
	atq = Formulas.monstro_atq(c, nivel, m.atq)
	def = Formulas.monstro_def(c, nivel, m["def"])
	res = Formulas.monstro_res(c, nivel, m["def"])
	vel = float(c.monstro_velocidade) * float(m.vel) * float(dados.get("velocidade", 1.0))
	_criar_corpo()
	estados = Estados.new()
	estados.e_boss = tipo in ["guardiao", "mini_boss", "boss"]
	estados.altura = _tamanho_px / 16.0 * 0.7 + 0.2
	add_child(estados)
	var cor_base := sprite.modulate
	estados.mudou.connect(func():
		# congelado fica azul-gelo; queimadura um pouco avermelhado
		sprite.modulate = cor_base * (Color(0.65, 0.85, 1.4) if estados.tem("congelado") else (Color(1.25, 0.85, 0.8) if estados.tem("queimadura") else Color.WHITE)))
	_mudar("descanso")


func _criar_corpo() -> void:
	var prefixo: String = dados.get("sprite", "res://arte/regioes/r01_floresta/monstros/" + id)
	var sf := Folhas.criar(prefixo, ANIMS, ["lado"])
	_tamanho_px = 32
	if sf.has_animation("parado_lado"):
		_tamanho_px = sf.get_frame_texture("parado_lado", 0).get_height()
	sprite = Folhas.boneco(sf, _tamanho_px)
	add_child(sprite)
	if tipo == "elite":   # versão Elite: mudança de cor feita pelo jogo
		sprite.modulate = Color(1.3, 0.9, 1.4)
	var metros := _tamanho_px / 16.0
	var raio: float = clamp(metros * 0.22, 0.3, 2.5)
	var forma := CollisionShape3D.new()
	var cil := CylinderShape3D.new()
	cil.radius = raio
	cil.height = max(0.6, metros * 0.6)
	forma.shape = cil
	forma.position.y = cil.height / 2.0
	add_child(forma)
	add_child(Folhas.sombra(raio * 1.3))
	hurtbox = Hurtbox.criar(self, 1 << 2, raio + 0.1, metros * 0.7)
	add_child(hurtbox)
	_mira = Node3D.new()
	add_child(_mira)
	hitbox = Hitbox.new()
	hitbox.dono = self
	hitbox.collision_layer = 0
	hitbox.collision_mask = 1 << 1
	hitbox.calcular_golpe = _calcular_golpe
	_mira.add_child(hitbox)
	_marca = MeshInstance3D.new()
	var plano := PlaneMesh.new()
	_marca.mesh = plano
	var mat := StandardMaterial3D.new()
	mat.albedo_color = Color(0.91, 0.23, 0.23, 0.35)
	mat.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
	mat.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	_marca.material_override = mat
	_marca.visible = false
	_marca.position.y = 0.03
	_mira.add_child(_marca)


# ------------------------------------------------------------------ IA ------------------------------------------------------------------

func _physics_process(delta: float) -> void:
	if not is_on_floor():
		velocity.y -= _gravidade * delta
	else:
		velocity.y = 0.0
	_t += delta
	for k in _recargas:
		_recargas[k] = max(0.0, _recargas[k] - delta)
	if _alvo == null or not is_instance_valid(_alvo):
		_alvo = get_tree().get_first_node_in_group("jogador")
	if estado != "morto" and estados.flag("parado"):
		if estado in ["aviso", "atacar"]:
			_mudar("dano")
		_parar(delta)
		move_and_slide()
		return
	match estado:
		"descanso":
			_descanso(delta)
		"alerta":
			_parar(delta)
			if _t >= float(Dados.c("ia_alerta")):
				_mudar("perseguir")
		"perseguir":
			_perseguir()
		"aviso":
			_parar(delta)
			if _t >= float(_ataque.get("aviso", 0.4)):
				_golpear()
		"atacar":
			_parar(delta)
			if _t >= 0.35:
				_fim_ataque()
		"regresso":
			_regressar()
		"fugir":
			_fugir()
		"dano":
			_parar(delta)
			if _t >= 0.25:
				_mudar("perseguir")
		_:
			_parar(delta)
	move_and_slide()
	if abs(velocity.x) > 0.1:
		olhar_x = sign(velocity.x)
	sprite.flip_h = olhar_x < 0.0


func _parar(delta: float) -> void:
	velocity.x = move_toward(velocity.x, 0.0, 20.0 * delta)
	velocity.z = move_toward(velocity.z, 0.0, 20.0 * delta)


func _vel() -> float:
	return vel * estados.mult("vel_mult")


func _distancia_alvo() -> float:
	if _alvo == null:
		return INF
	return global_position.distance_to(_alvo.global_position)


func _visao() -> float:
	var v := float(Dados.c("ia_visao"))
	if dados.get("noturno", false):
		v = float(Dados.c("ia_visao_noturno"))
	elif Tempo.e_noite():
		v = float(Dados.c("ia_visao_noite"))
	return v


func _descanso(_delta: float) -> void:
	# passeia devagar à volta do ponto inicial
	if _t > 2.5 or _passeio == Vector3.ZERO:
		_t = 0.0
		_passeio = ponto_inicial + Vector3(randf_range(-3, 3), 0, randf_range(-3, 3))
	var d := _passeio - global_position
	d.y = 0.0
	if d.length() > 0.3:
		velocity.x = d.normalized().x * _vel() * 0.35
		velocity.z = d.normalized().z * _vel() * 0.35
		_anim("mover")
	else:
		velocity.x = 0.0
		velocity.z = 0.0
		_anim("parado")
	if _alvo and _alvo.get("estado") != "morto" and _distancia_alvo() < _visao():
		_mudar("alerta")
		_exclamacao()


func _perseguir() -> void:
	if _alvo == null or _alvo.get("estado") == "morto":
		_mudar("regresso")
		return
	if dados.get("cobarde", false) and hp < hp_max * 0.2:
		_mudar("fugir")
		return
	if global_position.distance_to(ponto_inicial) > float(Dados.c("ia_distancia_maxima")):
		_mudar("regresso")
		return
	var ataque := _escolher_ataque()
	var dist := _distancia_alvo()
	var d := _alvo.global_position - global_position
	d.y = 0.0
	if ataque and dist <= float(ataque.alcance) and _atacantes < int(Dados.c("ia_max_atacantes")) and not estados.flag("sem_atacar"):
		_ataque = ataque
		_comecar_aviso(d)
		return
	# perto mas sem vez para atacar (ou em recarga): rodeia o jogador
	var alvo_dir := d.normalized()
	if dist < 2.2:
		alvo_dir = alvo_dir.rotated(Vector3.UP, PI / 2.0) * 0.6
	velocity.x = alvo_dir.x * _vel()
	velocity.z = alvo_dir.z * _vel()
	_anim("mover")


func _escolher_ataque() -> Dictionary:
	var lista: Array = dados.get("ataques", [ATAQUE_PADRAO])
	var possiveis := []
	for a in lista:
		if _recargas.get(a.id, 0.0) <= 0.0:
			possiveis.append(a)
	if possiveis.is_empty():
		return {}
	return possiveis[randi() % possiveis.size()]


func _comecar_aviso(d: Vector3) -> void:
	_atacantes += 1
	olhar_x = sign(d.x) if abs(d.x) > 0.05 else olhar_x
	_mira.rotation.y = atan2(-d.x, -d.z)
	var alcance := float(_ataque.alcance) + 0.3
	for f in hitbox.get_children():
		f.queue_free()
	hitbox.add_child(Hitbox.caixa(1.4, alcance))
	(_marca.mesh as PlaneMesh).size = Vector2(1.4, alcance)
	_marca.position = Vector3(0, 0.03, -alcance / 2.0)
	_marca.visible = true
	_mudar("aviso")
	sprite.play("atacar_lado")
	sprite.speed_scale = 0.35   # a pose de preparação dura o aviso


func _golpear() -> void:
	_marca.visible = false
	sprite.speed_scale = 1.6
	if randf() < estados.mult("precisao"):   # Cegueira: falha 30% dos ataques
		hitbox.ligar()
	_recargas[_ataque.id] = float(_ataque.get("recarga", 1.4))
	velocity = (_mira.global_transform.basis * Vector3.FORWARD) * 2.0
	_mudar("atacar")


func _fim_ataque() -> void:
	hitbox.desligar()
	_atacantes = max(0, _atacantes - 1)
	sprite.speed_scale = 1.0
	_mudar("perseguir")


func _regressar() -> void:
	var d := ponto_inicial - global_position
	d.y = 0.0
	if d.length() < 0.8:
		hp = hp_max
		_mudar("descanso")
		return
	velocity.x = d.normalized().x * _vel()
	velocity.z = d.normalized().z * _vel()
	_anim("mover")


func _fugir() -> void:
	if _alvo == null:
		_mudar("regresso")
		return
	var d := global_position - _alvo.global_position
	d.y = 0.0
	velocity.x = d.normalized().x * _vel() * 1.1
	velocity.z = d.normalized().z * _vel() * 1.1
	_anim("mover")
	if _distancia_alvo() > _visao() * 1.5:
		_mudar("regresso")


func _mudar(novo: String) -> void:
	if estado in ["aviso", "atacar"] and not novo in ["aviso", "atacar"]:
		if estado == "aviso":
			_atacantes = max(0, _atacantes - 1)
		hitbox.desligar()
		_marca.visible = false
		sprite.speed_scale = 1.0
	estado = novo
	_t = 0.0


func _anim(nome: String) -> void:
	var a := nome + "_lado"
	if sprite.animation != a and sprite.sprite_frames.has_animation(a):
		sprite.play(a)


func _exclamacao() -> void:
	var s := Sprite3D.new()
	s.texture = load("res://arte/ui/aviso_exclamacao.png")
	s.billboard = BaseMaterial3D.BILLBOARD_ENABLED
	s.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
	s.pixel_size = 1.0 / 16.0
	s.no_depth_test = true
	s.position.y = _tamanho_px / 16.0 + 0.3
	add_child(s)
	get_tree().create_timer(0.6).timeout.connect(s.queue_free)


# ------------------------------------------------------------------ combate ------------------------------------------------------------------

func info_dano() -> Dictionary:
	var elem := {}
	for el in ["fogo", "gelo", "raio", "veneno", "luz", "sombra"]:
		elem[el] = estados.mult_elemento(el)
	return {"def": def * estados.mult("def_mult"), "res": res, "fraquezas": dados.get("fraquezas", []),
			"resistencias": dados.get("resistencias", []), "imunidades": dados.get("imunidades", []),
			"atordoado": estados.tem("atordoado"), "elem_mult": elem}


func hp_maximo_estado() -> float:
	return hp_max


func perder_hp_estado(valor: float, cor: String, minimo_1: bool) -> void:
	if estado == "morto":
		return
	hp = max(1.0 if minimo_1 else 0.0, hp - valor)
	EfeitosCombate.numero(get_tree(), global_position + Vector3(0, _tamanho_px / 32.0 - 0.6, 0), str(int(valor)), cor)
	if hp <= 0.0:
		morrer()


## O ataque atual: elemento (vem do primeiro estado com elemento) e estados que causa.
func _elemento_ataque() -> String:
	for e in _ataque.get("estados", []):
		var el: String = Estados.info(e.estado).get("elemento", "")
		if el != "":
			return el
	return dados.get("elemento", "")


func _calcular_golpe(alvo: Node) -> Dictionary:
	var info: Dictionary = alvo.info_dano() if alvo.has_method("info_dano") else {}
	var g := Dano.calcular(atq * estados.mult("dano_mult"), float(_ataque.get("mult", 1.0)), info.get("def", 0.0), info,
			_elemento_ataque(), 0.05, 1.5)
	g["empurrao"] = 1.0
	g["estados"] = _ataque.get("estados", [])
	return g


func receber_golpe(golpe: Dictionary) -> void:
	if estado == "morto":
		return
	var valor: int = int(golpe.get("valor", 0) * estados.consumir_golpe_mult())
	var pegou := estados.do_golpe(golpe.get("estados", []), null, golpe.get("origem", Vector3.INF))
	if "choque" in pegou and not golpe.get("cadeia", false):
		_choque_salta(golpe)
	var tipo_num := "imune" if golpe.get("imune") else ("critico" if golpe.get("critico") else ("magia" if golpe.get("magico") else "normal"))
	EfeitosCombate.numero(get_tree(), global_position + Vector3(0, _tamanho_px / 32.0 - 0.6, 0), "IMUNE" if golpe.get("imune") else str(valor), tipo_num)
	EfeitosCombate.piscar(sprite)
	EfeitosCombate.animado(get_tree(), "impacto", global_position + Vector3(0, _tamanho_px / 32.0, 0.3))
	hp -= valor
	if hp <= 0.0:
		morrer()
		return
	if not tipo in ["guardiao", "mini_boss", "boss"]:
		var fora: Vector3 = global_position - golpe.get("origem", global_position)
		fora.y = 0.0
		if fora.length() > 0.01:
			velocity = fora.normalized() * float(golpe.get("empurrao", 0.5)) * 8.0
		if estado != "aviso":
			_mudar("dano")
			sprite.play("dano_lado")
	if estado == "descanso" or estado == "alerta":
		_mudar("perseguir")


## Choque: salta para 2 inimigos a menos de 3 m (50% do dano).
func _choque_salta(golpe: Dictionary) -> void:
	var s: Array = Estados.info("choque").get("salta", [2, 3.0, 0.5])
	var n := 0
	for m in get_tree().get_nodes_in_group("monstros"):
		if m == self or not is_instance_valid(m) or m.estado == "morto" or n >= int(s[0]):
			continue
		if m.global_position.distance_to(global_position) < float(s[1]):
			var g := golpe.duplicate()
			g.valor = int(golpe.get("valor", 0) * float(s[2]))
			g.cadeia = true
			g.estados = []
			m.receber_golpe(g)
			EfeitosCombate.animado(get_tree(), "explosao_raio", m.global_position + Vector3(0, 0.8, 0))
			n += 1


func _largar(item: ItemChao) -> void:
	get_parent().add_child(item)
	item.global_position = global_position + Vector3(0, 0.6, 0)


func morrer() -> void:
	_mudar("morto")
	collision_layer = 0
	hurtbox.queue_free()
	sprite.play("morrer_lado")
	var c := Dados.constantes
	var m: Dictionary = c.tipos_monstro.get(tipo, c.tipos_monstro.normal)
	var xp := Formulas.xp_recebida(c, Jogo.nivel, nivel, float(m.xp))
	var rng := RandomNumberGenerator.new()
	rng.randomize()
	var ouro := Formulas.monstro_ouro(nivel, rng)
	Jogo.ganhar_xp(xp)
	_largar(ItemChao.moedas(ouro))
	for d in Loot.drops(c, dados.get("drops", []), Jogo.a("sor"), tipo == "elite", rng):
		_largar(ItemChao.criar(d[0], d[1]))
	if tipo in ["guardiao", "mini_boss", "boss"] and rng.randf() < 0.25:
		_largar(ItemChao.criar("chave_bau_ouro", 1))
	EfeitosCombate.numero(get_tree(), global_position + Vector3(0, 0.4, 0), "+%d XP" % xp, "cura")
	Eventos.monstro_morto.emit(id, nivel)
	morreu.emit(self)
	var t := create_tween()
	t.tween_interval(1.4)
	t.tween_callback(func(): sprite.alpha_cut = SpriteBase3D.ALPHA_CUT_DISABLED)
	t.tween_property(sprite, "modulate:a", 0.0, 0.6)
	t.tween_callback(queue_free)
