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
var anims: Dictionary = ANIMS
var _olho: Label3D
var _mira: Node3D
var _marca: MeshInstance3D
var _alvo: Node3D
var _t: float = 0.0
var _recargas: Dictionary = {}
var _ataque: Dictionary = {}
var _passeio := Vector3.ZERO
var _gravidade: float = ProjectSettings.get_setting("physics/3d/default_gravity", 9.8)
var _tamanho_px: int = 32
var _vida_t: float = 0.0      # relógio da animação do corpo (respirar, saltitar)
var _bote: float = 0.0        # encolher quando leva um golpe (1 → 0)
var _fase_resp: float = randf() * TAU
static var _atacantes: int = 0
var _t_alvo: float = 0.0


## id: o monstro em dados/monstros.json · nivel: o do andar · tipo_extra: "elite", "com_nome"... (ou "")
func configurar(id_: String, nivel_: int, tipo_extra: String = "") -> Monstro:
	id = id_
	nivel = nivel_
	dados = Dados.monstro(id)
	if dados.is_empty():
		dados = Dados.obter("bosses", id)
	if dados.is_empty():   # os bosses das masmorras escondidas
		dados = Dados.tabela("masmorras").get("bosses", {}).get(id, {})
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
	if Jogo.tem_unica("olho_do_sistema"):   # vês o nível, o HP e as fraquezas
		_olho = Label3D.new()
		_olho.billboard = BaseMaterial3D.BILLBOARD_ENABLED
		_olho.no_depth_test = true
		_olho.fixed_size = true
		_olho.pixel_size = 0.0011
		_olho.font_size = 22
		_olho.outline_size = 6
		_olho.modulate = Color("8fd3ff")
		_olho.position.y = _tamanho_px / 16.0 * 0.7 + 0.6
		add_child(_olho)
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
	var sf := Folhas.criar(prefixo, anims, ["lado"])
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
	# quem está em água funda ou lava (o Titã de Magma, os monstros do mar) fica à superfície, não se afunda
	if global_position.y < ponto_inicial.y - 0.9 and global_position.y < -0.6:
		global_position.y = maxf(global_position.y, -0.6)
		velocity.y = maxf(velocity.y, 0.0)
	_t += delta
	for k in _recargas:
		_recargas[k] = max(0.0, _recargas[k] - delta)
	_t_alvo -= delta
	if _alvo == null or not is_instance_valid(_alvo) or (_t_alvo <= 0.0 and not estado in ["aviso", "atacar"]):
		_t_alvo = 0.4
		_alvo = _escolher_alvo()
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
	if _olho:
		_olho.visible = _alvo != null and _distancia_alvo() < 9.0 and _mais_perto()
		_olho.text = "Nv %d  %d/%d%s" % [nivel, int(hp), int(hp_max), ("\nFraco: " + ", ".join(dados.get("fraquezas", []))) if dados.get("fraquezas") else ""]
	if abs(velocity.x) > 0.1:
		olhar_x = sign(velocity.x)
	sprite.flip_h = olhar_x < 0.0
	_animar_corpo(delta)


## O corpo mexe-se por cima das animações desenhadas (feito pelo jogo, docs/ARTE.md secção 0): respira parado,
## saltita a andar, agacha-se no aviso do ataque, estica-se no golpe e encolhe quando leva um golpe.
func _animar_corpo(delta: float) -> void:
	if estado == "morto":
		return
	_vida_t += delta
	var sx := 1.0
	var sy := 1.0
	var py := 0.0
	var plano := Vector2(velocity.x, velocity.z).length()
	match estado:
		"aviso":
			var k := clampf(_t / maxf(0.1, float(_ataque.get("aviso", 0.4))), 0.0, 1.0)
			sy = 1.0 - 0.13 * k
			sx = 1.0 + 0.1 * k
		"atacar":
			var k := clampf(1.0 - _t / 0.22, 0.0, 1.0)
			sy = 1.0 + 0.12 * k
			sx = 1.0 - 0.08 * k
		_:
			if plano > 0.3:
				var sal := absf(sin(_vida_t * (5.0 + plano * 1.2)))
				py = sal * 0.05 * _tamanho_px / 16.0
				sy = 1.0 + (sal - 0.5) * 0.07
				sx = 1.0 - (sy - 1.0) * 0.6
			else:
				var r := sin(_vida_t * 2.4 + _fase_resp) * 0.025
				sy = 1.0 + r
				sx = 1.0 - r * 0.6
	if _bote > 0.0:
		_bote = maxf(0.0, _bote - delta * 6.0)
		sx += 0.22 * _bote
		sy -= 0.18 * _bote
	sprite.scale = Vector3(sx, sy, 1.0)
	sprite.position.y = py


## (o Olho do Sistema mostra só o monstro mais perto: com vários, os textos ficavam uns por cima dos outros)
func _mais_perto() -> bool:
	var d := _distancia_alvo()
	for m in get_tree().get_nodes_in_group("monstros"):
		if m != self and m.estado != "morto" and m.global_position.distance_to(_alvo.global_position) < d:
			return false
	return true


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
	if _alvo != null and _alvo.get("estado") == "morto" and _alvo is Companheiro:   # o companheiro caiu: vai a outro
		_alvo = _escolher_alvo()
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


## O alvo: o herói ou o companheiro mais perto (docs/SISTEMAS.md, secção 20); quem provoca puxa-os a todos.
## Os guardiões e os bosses escolhem sempre o herói.
func _escolher_alvo() -> Node3D:
	var j := get_tree().get_first_node_in_group("jogador") as Node3D
	if tipo in ["guardiao", "mini_boss", "boss"] or Jogo.companheiros.is_empty():
		return j
	var melhor := j
	var dist := global_position.distance_to(j.global_position) if j else INF
	for c in get_tree().get_nodes_in_group("companheiros"):
		if c.estado == "morto" or c.invisivel():
			continue
		if c.provocando(global_position):
			return c
		var dc: float = global_position.distance_to(c.global_position)
		if dc < dist - 0.5:
			dist = dc
			melhor = c
	return melhor


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
	_bote = 1.0
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
	for d in Loot.drops(c, dados.get("drops", []), Jogo.a("sor"), tipo == "elite", rng, Jogo.tem_unica("sorte_do_heroi")):
		_largar(ItemChao.criar(d[0], d[1]))
	if tipo in ["guardiao", "mini_boss", "boss"] and rng.randf() < 0.25:
		_largar(ItemChao.criar("chave_bau_ouro", 1))
	EfeitosCombate.numero(get_tree(), global_position + Vector3(0, 0.4, 0), "+%d XP" % xp, "cura")
	if tipo == "elite":
		Colecoes.contar("elites")
	if id == "mimico":
		Colecoes.contar("mimicos")
	if tipo in ["guardiao", "mini_boss", "boss"]:
		Colecoes.contar("guardioes" if tipo == "guardiao" else "bosses")
		Jogo.por_flag("boss_" + id)
		Eventos.boss_derrotado.emit(id)
	Eventos.monstro_morto.emit(id, nivel)
	morreu.emit(self)
	_desfazer()


## Morrer: a animação de cair, um pisco branco e o corpo desfaz-se num "puf" de fumo (os grandes, maior).
func _desfazer() -> void:
	sprite.scale = Vector3.ONE
	sprite.position.y = 0.0
	var metros := _tamanho_px / 16.0
	var t := create_tween()
	t.tween_interval(0.9)
	t.tween_callback(func(): EfeitosCombate.piscar(sprite, 0.12))
	t.tween_interval(0.15)
	t.tween_callback(func():
		var n := 1 if metros <= 2.5 else (3 if metros <= 4.5 else 5)
		for i in n:
			var o := Vector3(randf_range(-0.4, 0.4), randf_range(0.0, 0.5), 0.2) * metros * (0.0 if i == 0 else 1.0)
			EfeitosCombate.animado(get_tree(), "fumo_morte", global_position + Vector3(0, metros * 0.3, 0.3) + o, 14.0)
		sprite.alpha_cut = SpriteBase3D.ALPHA_CUT_DISABLED)
	t.parallel().tween_property(sprite, "scale", Vector3(1.3, 0.2, 1.0), 0.25)
	t.parallel().tween_property(sprite, "modulate:a", 0.0, 0.25)
	t.tween_interval(0.4)
	t.tween_callback(queue_free)
