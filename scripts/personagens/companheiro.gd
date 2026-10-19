class_name Companheiro
extends CharacterBody3D
## Um companheiro no andar (docs/SISTEMAS.md, secção 20): segue o herói, luta conforme a ordem, sai dos avisos
## vermelhos, usa a skill própria e a ensinada, bebe as poções que lhe deste e, se cair, levanta-se passados 30 s
## (ou logo, com uma poção tua: tecla E ao pé dele). Valores e itens: autoload Grupo.

const ANIMS := {"parado": [4, true], "andar": [8, true]}
const DISTANCIA := ["arco", "besta", "cajado"]
const PROJETIL := {"arco": "flecha", "besta": "virote", "cajado": "projetil_luz"}

var id: String = ""
var d: Dictionary = {}
var hp: float = 1.0
var hp_max: float = 1.0
var estado: String = "normal"   # normal, ataque, skill, esquiva, morto (caído)
var direcao := Vector2(0, 1)
var olhar_x: float = 1.0

var boneco: BonecoArma
var hitbox: Hitbox
var hurtbox: Hurtbox
var estados: Estados
var _mira: Node3D
var _arma: Dictionary = {}
var _alvo: Node3D
var _inter: Interagivel
var _rotulo: Label3D
var _gravidade: float = ProjectSettings.get_setting("physics/3d/default_gravity", 9.8)
var _t_alvo: float = 0.0
var _espera: float = 0.6        # entre ataques normais
var _ataque_t: float = 0.0
var _ataque_dur: float = 0.5
var _disparou: bool = false
var _skill_r: float = 4.0       # recargas: skill própria e ensinada
var _ensinada_r: float = 7.0
var _pocao_r: float = 0.0
var _caido_t: float = 0.0
var _provocar_t: float = 0.0
var _def_extra: float = 0.0
var _invencivel: float = 0.0
var _esquiva_t: float = 0.0
var _esquiva_dir := Vector3.ZERO
var _skill_t: float = 0.0
var _lento_t: float = 0.0


func _ready() -> void:
	add_to_group("companheiros")
	add_to_group("aliados")
	d = Grupo.dados(id)
	collision_layer = 1 << 3
	collision_mask = 1
	var forma := CollisionShape3D.new()
	var cap := CapsuleShape3D.new()
	cap.radius = 0.3
	cap.height = 1.4
	forma.shape = cap
	forma.position.y = 0.7
	add_child(forma)
	boneco = BonecoArma.new(Folhas.criar(String(d.get("sprite", "res://arte/npcs/" + id)), ANIMS, ["baixo", "cima", "lado"]))
	add_child(boneco)
	add_child(Folhas.sombra(0.42))
	hurtbox = Hurtbox.criar(self, 1 << 1)
	add_child(hurtbox)
	_mira = Node3D.new()
	add_child(_mira)
	hitbox = Hitbox.new()
	hitbox.dono = self
	hitbox.collision_layer = 0
	hitbox.collision_mask = 1 << 2
	hitbox.calcular_golpe = func(alvo): return _golpe(alvo, 1.0, "", [])
	_mira.add_child(hitbox)
	estados = Estados.new()
	add_child(estados)
	_inter = Interagivel.new()
	_inter.texto = "Dar uma poção a %s" % d.get("nome_pt", id)
	_inter.ativo = false
	add_child(_inter)
	_inter.usado.connect(func(_j): _dar_pocao_tua())
	_rotulo = Label3D.new()
	_rotulo.billboard = BaseMaterial3D.BILLBOARD_ENABLED
	_rotulo.no_depth_test = true
	_rotulo.fixed_size = true
	_rotulo.pixel_size = 0.0011
	_rotulo.font_size = 20
	_rotulo.outline_size = 6
	_rotulo.modulate = Color("f9c22b")
	_rotulo.position.y = 2.3
	_rotulo.visible = false
	add_child(_rotulo)
	recalcular()
	hp = hp_max
	_tocar("parado")


## Valores outra vez (subiste de nível, deste-lhe uma arma ou uma peça).
func recalcular() -> void:
	var pct := hp / hp_max if hp_max > 0.0 else 1.0
	hp_max = Grupo.hp_max(id)
	hp = clampf(hp_max * pct, 0.0, hp_max)
	_arma = Grupo.arma(id)
	var spr := String(_arma.get("sprite", ""))
	boneco.por_arma(load(spr) if spr != "" and ResourceLoader.exists(spr) else null)
	for f in hitbox.get_children():
		f.queue_free()
	var t: Array = Jogador.TIPOS.get(_arma.get("tipo", "espada"), Jogador.TIPOS.espada)
	if t[2] > 0.0:
		hitbox.add_child(Hitbox.caixa(t[2], float(_arma.get("alcance", 1.8)) + 0.4))


func _distancia() -> bool:
	return String(_arma.get("tipo", "")) in DISTANCIA


func _alcance() -> float:
	return 6.5 if _distancia() else float(_arma.get("alcance", 1.6)) + 0.3


# ------------------------------------------------------------------ ciclo ------------------------------------------------------------------

func _physics_process(delta: float) -> void:
	if not is_on_floor():
		velocity.y -= _gravidade * delta
	else:
		velocity.y = 0.0
	_espera = maxf(0.0, _espera - delta)
	_skill_r = maxf(0.0, _skill_r - delta)
	_ensinada_r = maxf(0.0, _ensinada_r - delta)
	_pocao_r = maxf(0.0, _pocao_r - delta)
	_invencivel = maxf(0.0, _invencivel - delta)
	_provocar_t = maxf(0.0, _provocar_t - delta)
	if _provocar_t <= 0.0:
		_def_extra = 0.0
	var j := get_tree().get_first_node_in_group("jogador") as Node3D
	if estado == "morto":
		_caido_t -= delta
		_rotulo.text = "Caído (%d s)" % ceili(maxf(0.0, _caido_t))
		if _caido_t <= 0.0:
			levantar(float(Grupo.c("levantar_hp", 0.5)))
		_travar(delta)
		move_and_slide()
		return
	if j and global_position.distance_to(j.global_position) > float(Grupo.c("teletransporte", 14.0)) and Grupo.ordem(id) != "ficar":
		_ao_pe_de(j)   # ficou para trás (masmorra, escada, buraco): aparece ao lado do herói
	if estados.flag("parado"):
		_travar(delta)
		move_and_slide()
		return
	_beber_se_preciso()
	_aura_tempo(delta)
	match estado:
		"ataque":
			_atacar(delta)
		"skill":
			_skill_t -= delta
			if _skill_t <= 0.0:
				estado = "normal"
		"esquiva":
			velocity.x = _esquiva_dir.x * 7.0
			velocity.z = _esquiva_dir.z * 7.0
			_esquiva_t -= delta
			if _esquiva_t <= 0.0:
				estado = "normal"
		_:
			_pensar(delta, j)
	move_and_slide()
	if absf(velocity.x) > 0.1:
		olhar_x = signf(velocity.x)
	var plano := Vector2(velocity.x, velocity.z)
	if estado == "normal":
		if plano.length() > 0.3:
			direcao = plano.normalized()
			_tocar("andar", clampf(plano.length() / 4.5, 0.8, 1.6))
		else:
			_tocar("parado")
	boneco.visible = _invencivel <= 0.0 or int(_invencivel * 20.0) % 2 == 0


func _travar(delta: float) -> void:
	velocity.x = move_toward(velocity.x, 0.0, 25.0 * delta)
	velocity.z = move_toward(velocity.z, 0.0, 25.0 * delta)


func _ao_pe_de(j: Node3D) -> void:
	var i := maxi(0, Jogo.companheiros.find(id))
	global_position = j.global_position + Vector3(-1.4 + 1.4 * i, 0.3, 1.2)
	velocity = Vector3.ZERO
	EfeitosCombate.animado(get_tree(), "poeira", global_position + Vector3(0, 0.4, 0))


func _vel() -> float:
	return Jogo.velocidade() * 1.05 * estados.mult("vel_mult")


## Decide o que fazer: escolher alvo conforme a ordem, fugir dos avisos, atacar, usar skills ou seguir o herói.
func _pensar(delta: float, j: Node3D) -> void:
	var ordem := Grupo.ordem(id)
	_t_alvo -= delta
	if _t_alvo <= 0.0 or (_alvo != null and (not is_instance_valid(_alvo) or _alvo.estado == "morto")):
		_t_alvo = 0.3
		_alvo = _escolher_alvo(ordem, j)
	if _fugir_de_aviso():
		return
	if _alvo != null and is_instance_valid(_alvo):
		var dv := _alvo.global_position - global_position
		dv.y = 0.0
		var dist := dv.length()
		if _usar_skills(dist):
			return
		if dist > _alcance():
			_mover(dv.normalized(), 1.0)
		elif _distancia() and dist < 2.5:
			_mover(-dv.normalized(), 0.8)   # arqueiros e magos não ficam colados
		else:
			_travar(delta)
			direcao = Vector2(dv.x, dv.z).normalized()
			if _espera <= 0.0:
				_comecar_ataque()
		return
	if ordem == "ficar" or j == null:
		_travar(delta)
		return
	# seguir o herói: atrás dele, cada um no seu lado
	var i := maxi(0, Jogo.companheiros.find(id))
	var lado := Vector3(-1.6 + 1.6 * i, 0.0, 1.6)
	var destino := j.global_position + lado
	var dd := destino - global_position
	dd.y = 0.0
	var seg: Array = Grupo.c("seguir", [2.0, 4.0])
	var longe := global_position.distance_to(j.global_position)
	if dd.length() > 0.6 and longe > float(seg[0]):
		_mover(dd.normalized(), 1.4 if longe > float(seg[1]) + 2.0 else 1.0)
	else:
		_travar(delta)


func _mover(dir: Vector3, mult: float) -> void:
	velocity.x = dir.x * _vel() * mult
	velocity.z = dir.z * _vel() * mult


func _escolher_alvo(ordem: String, j: Node3D) -> Node3D:
	if ordem == "seguir" or j == null:
		return null
	var melhor: Node3D = null
	var melhor_d := INF
	var raio := float(Grupo.c("atacar_raio", 10.0))
	for m in get_tree().get_nodes_in_group("monstros"):
		if not is_instance_valid(m) or m.estado == "morto":
			continue
		var dj: float = m.global_position.distance_to(j.global_position)
		var dm: float = m.global_position.distance_to(global_position)
		match ordem:
			"defender":
				if dj > float(Grupo.c("defender_raio", 3.0)):
					continue
			"ficar":
				if dm > 6.0:
					continue
			_:
				# não vai acordar monstros que estão a descansar longe de ti
				if dj > raio or (m.estado == "descanso" and dj > 5.0 and dm > 4.0):
					continue
		var custo := dm + (0.0 if m.estado in ["perseguir", "aviso", "atacar", "dano"] else 3.0)
		if custo < melhor_d:
			melhor_d = custo
			melhor = m
	return melhor


## Um monstro a preparar um golpe mesmo ao lado: salta para trás (como a esquiva do herói, sem estamina).
func _fugir_de_aviso() -> bool:
	for m in get_tree().get_nodes_in_group("monstros"):
		if not is_instance_valid(m) or m.estado != "aviso":
			continue
		var dv: Vector3 = global_position - m.global_position
		dv.y = 0.0
		if dv.length() < 2.4 and randf() < 0.6:
			_esquiva_dir = dv.normalized() if dv.length() > 0.05 else Vector3.BACK
			_esquiva_t = 0.25
			_invencivel = maxf(_invencivel, 0.2)
			estado = "esquiva"
			hitbox.desligar()
			boneco.esconder_arma()
			return true
	return false


# ------------------------------------------------------------------ ataque normal ------------------------------------------------------------------

func _comecar_ataque() -> void:
	_ataque_dur = 1.0 / maxf(0.3, float(_arma.get("velocidade", 1.0)) * estados.mult("atq_vel_mult"))
	_ataque_t = 0.0
	_disparou = false
	_mira.rotation.y = atan2(-direcao.x, -direcao.y)
	estado = "ataque"
	_tocar("andar", 1.6, true)


func _atacar(delta: float) -> void:
	_ataque_t += delta
	var p := _ataque_t / _ataque_dur
	_travar(delta)
	_pose_arma(p)
	if _distancia():
		if p >= 0.45 and not _disparou:
			_disparou = true
			_disparar(1.0, "", [])
	elif p >= 0.3 and p < 0.65 and not hitbox.ligada:
		hitbox.ligar()
		Audio.efeito(String(Jogador.SOM_GOLPE.get(_arma.get("tipo", "espada"), "corte")), 0.1, 0.6)
	elif p >= 0.65 and hitbox.ligada:
		hitbox.desligar()
	if p >= 1.0:
		hitbox.desligar()
		boneco.esconder_arma()
		_espera = 0.35   # um pouco mais lentos do que tu: o herói continua a ser o herói
		estado = "normal"


func _pose_arma(p: float) -> void:
	var atras := _nome_direcao() == "cima"
	var e := ease(clampf((p - 0.15) / 0.5, 0.0, 1.0), 0.4)
	match String(_arma.get("tipo", "espada")):
		"lanca":
			boneco.pose_arma(90.0, Vector2(lerpf(-8.0, 10.0, e), -6), atras)
		"arco":
			boneco.pose_arma(0.0, Vector2(4, -8), atras)
		"besta":
			boneco.pose_arma(90.0, Vector2(4, -8), atras)
		"cajado":
			boneco.pose_arma(lerpf(-30.0, 15.0, e), Vector2(2, -10), atras)
		"espada_grande", "machado", "martelo":
			boneco.pose_arma(lerpf(-170.0, 100.0, e), Vector2(-2, -6), atras)
		"manoplas":
			boneco.esconder_arma()
		_:
			boneco.pose_arma(lerpf(-110.0, 120.0, e), Vector2(0, -4), atras)


func _disparar(mult: float, el: String, est: Array, desvio: float = 0.0) -> void:
	var tipo := String(_arma.get("tipo", "arco"))
	var p := Projetil.new()
	var nome: String = "projetil_" + el if el != "" else String(PROJETIL.get(tipo, "flecha"))
	p.textura = "res://arte/efeitos/%s.png" % nome
	if not ResourceLoader.exists(p.textura):
		p.textura = "res://arte/efeitos/flecha.png"
	p.dono = self
	p.alcance = maxf(10.0, float(_arma.get("alcance", 12.0)))
	p.velocidade = 20.0 if tipo != "cajado" else 14.0
	p.direcao = Vector3(direcao.x, 0, direcao.y).normalized().rotated(Vector3.UP, desvio)
	if _alvo and is_instance_valid(_alvo):   # apontam bem (não têm rato)
		var dv := _alvo.global_position - global_position
		dv.y = 0.0
		if dv.length() > 0.1:
			p.direcao = dv.normalized().rotated(Vector3.UP, desvio)
	var elem := el if el != "" else (String(_arma.get("elemento", "")) if _arma.get("elemento") else "")
	p.calcular_golpe = func(alvo): return _golpe(alvo, mult, elem, est)
	get_tree().current_scene.add_child(p)
	p.global_position = global_position + Vector3(0, 1.0, 0) + p.direcao * 0.6
	Audio.efeito("arco_disparar" if tipo != "cajado" else "feitico_" + (elem if elem != "" else "luz"), 0.1, 0.6)


## Um golpe do companheiro (mesmas fórmulas do herói, com os valores dele).
func _golpe(alvo: Node, mult: float, el: String, est: Array) -> Dictionary:
	var k := Dados.constantes
	var info: Dictionary = alvo.info_dano() if alvo.has_method("info_dano") else {}
	var magico := String(_arma.get("tipo", "")) == "cajado"
	var a := Grupo.atributos(id)
	var crit := Formulas.critico(k, int(a.des), int(a.sor), float(_arma.get("critico", 0.0)))
	var elem := el if el != "" else (String(_arma.get("elemento", "")) if _arma.get("elemento") else "")
	var lista := est if not est.is_empty() else Array(_arma.get("efeitos", [])).filter(func(e): return not e.get("so_carregado", false))
	var g := Dano.calcular(Grupo.atq(id), mult * estados.mult("dano_mult") * Jogo.dif("feito"),
			float(info.get("res", 0.0) if magico else info.get("def", 0.0)), info, elem, crit, float(k.critico_dano), magico)
	g["empurrao"] = float(k.empurrao)
	g["estados"] = lista
	g["origem"] = global_position
	return g


# ------------------------------------------------------------------ skills ------------------------------------------------------------------

func _usar_skills(dist: float) -> bool:
	if estados.flag("sem_skills"):
		return false
	var s: Dictionary = d.get("skill", {})
	if _skill_r <= 0.0 and not s.is_empty() and _skill_serve(s, dist):
		_skill_r = float(Grupo.c("skill_recarga", 15.0))
		_executar(s)
		return true
	var ens := String(Grupo.estado(id).ensinada)
	if ens != "" and _ensinada_r <= 0.0:
		var sk := Jogo.skill(ens)
		if not sk.is_empty() and _skill_serve(sk, dist):
			_ensinada_r = float(sk.get("recarga", 8.0)) * float(Grupo.c("ensinada_recarga_mult", 1.5))
			_executar(sk)
			return true
	return false


## Vale a pena usar a skill agora? (perto o suficiente; a de curar só com alguém ferido)
func _skill_serve(s: Dictionary, dist: float) -> bool:
	match String(s.get("forma", "golpe")):
		"cura_grupo", "cura":
			if Jogo.hp < Jogo.hp_maximo() * 0.7 or hp < hp_max * 0.6:
				return true
			for n in get_tree().get_nodes_in_group("companheiros"):
				if n.estado != "morto" and n.hp < n.hp_max * 0.6:
					return true
			return false
		"projetil", "linha", "area_alvo":
			return dist <= 8.0
		"area", "provocar":
			return dist <= float(s.get("dist", 3.0)) * 0.9
		"investida":
			return dist <= float(s.get("dist", 4.0)) + 1.0
	return dist <= _alcance() + 0.3


func _executar(s: Dictionary) -> void:
	var forma := String(s.get("forma", "golpe"))
	var mult := float(s.get("mult", 1.5))
	var el: String = String(s.get("elemento", "")) if s.get("elemento") else ""
	var est: Array = s.get("estados", [])
	var dir := Vector3(direcao.x, 0, direcao.y).normalized()
	if _alvo and is_instance_valid(_alvo):
		var dv := _alvo.global_position - global_position
		dv.y = 0.0
		if dv.length() > 0.1:
			dir = dv.normalized()
			direcao = Vector2(dir.x, dir.z)
	var n := int(s.get("golpes", 1))
	EfeitosCombate.numero(get_tree(), global_position + Vector3(0, 0.6, 0), String(s.get("nome_pt", "")), "texto")
	estado = "skill"
	_skill_t = 0.35
	_tocar("andar", 1.8, true)
	_pose_arma(0.6)
	match forma:
		"multi":
			_skill_t = 0.1 * n + 0.15
			for k in n:
				_atingir(global_position + dir * 1.2, 1.6, mult, el, est)
				EfeitosCombate.animado(get_tree(), "corte", global_position + dir * 1.2 + Vector3(randf_range(-0.4, 0.4), 1.0, 0), 30.0)
				await get_tree().create_timer(0.1).timeout
				if not is_instance_valid(self) or estado == "morto":
					return
		"area":
			var raio := float(s.get("dist", 3.0))
			_atingir(global_position, raio, mult, el, est)
			for a in 6:
				var ang := TAU * a / 6.0
				EfeitosCombate.animado(get_tree(), "explosao_" + (el if el != "" else "fisico"),
						global_position + Vector3(cos(ang) * raio * 0.6, 0.6, sin(ang) * raio * 0.6))
		"area_alvo":   # chuva (de flechas, de estrelas, de neve) em cima do alvo
			var centro := _alvo.global_position if _alvo and is_instance_valid(_alvo) else global_position + dir * 4.0
			var raio := float(s.get("dist", 3.0))
			_skill_t = 0.3 * n + 0.1
			for k in n:
				_atingir(centro, raio, mult, el, est)
				for a in 4:
					EfeitosCombate.animado(get_tree(), "explosao_" + (el if el != "" else "fisico"),
							centro + Vector3(randf_range(-raio, raio) * 0.6, 0.6, randf_range(-raio, raio) * 0.6))
				await get_tree().create_timer(0.3).timeout
				if not is_instance_valid(self) or estado == "morto":
					return
		"linha":
			var comp := float(s.get("dist", 6.0))
			_atingir(global_position, comp, mult, el, est, dir)
			for k in int(comp / 1.5):
				EfeitosCombate.animado(get_tree(), "explosao_" + el if el != "" else "corte_pesado", global_position + dir * (1.0 + k * 1.5) + Vector3(0, 0.8, 0))
		"investida":
			var dist := float(s.get("dist", 4.0))
			_skill_t = 0.25
			velocity = dir * dist / 0.22
			_invencivel = maxf(_invencivel, 0.25)
			await get_tree().create_timer(0.22).timeout
			if not is_instance_valid(self) or estado == "morto":
				return
			velocity = Vector3.ZERO
			_atingir(global_position + dir * 0.8, 2.0, mult, el, est)
			EfeitosCombate.animado(get_tree(), "explosao_" + (el if el != "" else "fisico"), global_position + dir + Vector3(0, 0.6, 0))
		"projetil":
			for k in n:
				_disparar(mult, el, est, (k - (n - 1) / 2.0) * 0.15)
		"provocar":
			_provocar_t = float(s.get("dura", 5.0))
			_def_extra = float(s.get("buff", {}).get("valor", 0.3))
			EfeitosCombate.animado(get_tree(), "subir_nivel", global_position + Vector3(0, 1, 0))
		"cura_grupo", "cura":
			var f := float(s.get("cura", 0.25)) if forma == "cura_grupo" else 0.3
			if Jogo.hp > 0.0:
				Jogo.curar(Jogo.hp_maximo() * f)
				var j := get_tree().get_first_node_in_group("jogador") as Node3D
				if j:
					EfeitosCombate.animado(get_tree(), "cura", j.global_position + Vector3(0, 1, 0))
			for c in get_tree().get_nodes_in_group("companheiros"):
				if c.estado != "morto":
					c.curar(c.hp_max * f)
		_:   # golpe e golpe_estado
			_atingir(global_position + dir * 1.2, _alcance() + 0.6, mult, el, est)
			EfeitosCombate.animado(get_tree(), "corte_pesado", global_position + dir * 1.2 + Vector3(0, 1.0, 0))


func _atingir(centro: Vector3, raio: float, mult: float, el: String, est: Array, linha := Vector3.ZERO) -> void:
	for m in get_tree().get_nodes_in_group("monstros"):
		if not is_instance_valid(m) or m.estado == "morto":
			continue
		var dv: Vector3 = m.global_position - centro
		dv.y = 0.0
		var dentro := false
		if linha != Vector3.ZERO:
			var ao_longo := dv.dot(linha)
			dentro = ao_longo >= -0.5 and ao_longo <= raio and (dv - linha * ao_longo).length() < 1.3
		else:
			dentro = dv.length() <= raio
		if dentro:
			var g := _golpe(m, mult, el, est)
			g["skill"] = true
			g["atacante"] = self
			m.receber_golpe(g)


## Provocar (Duarte, Ssark): os monstros perto vão a ele.
func provocando(de: Vector3) -> bool:
	if _provocar_t <= 0.0 or estado == "morto":
		return false
	return de.distance_to(global_position) <= float(d.get("skill", {}).get("dist", 6.0))


func invisivel() -> bool:
	return d.get("especial", {}).get("id", "") == "invisivel"


## Tempo Lento (Cronos): os inimigos à volta ficam lentos.
func _aura_tempo(delta: float) -> void:
	var es: Dictionary = d.get("especial", {})
	if es.get("id", "") != "tempo_lento":
		return
	_lento_t -= delta
	if _lento_t > 0.0:
		return
	_lento_t = 1.0
	for m in get_tree().get_nodes_in_group("monstros"):
		if is_instance_valid(m) and m.estado != "morto" and m.global_position.distance_to(global_position) <= float(es.valor):
			m.estados.aplicar("lentidao", 1.5)


# ------------------------------------------------------------------ vida ------------------------------------------------------------------

func info_dano() -> Dictionary:
	var elem := {}
	for el in ["fogo", "gelo", "raio", "veneno", "luz", "sombra"]:
		elem[el] = estados.mult_elemento(el)
	var dr := Grupo.defesa(id)
	return {"def": float(dr[0]) * (1.0 + _def_extra) * estados.mult("def_mult"), "res": float(dr[1]) * (1.0 + _def_extra),
			"fraquezas": [], "resistencias": [], "imunidades": [], "atordoado": estados.tem("atordoado"), "elem_mult": elem}


func hp_maximo_estado() -> float:
	return hp_max


func perder_hp_estado(valor: float, cor: String, minimo_1: bool) -> void:
	if estado == "morto":
		return
	hp = maxf(1.0 if minimo_1 else 0.0, hp - valor)
	EfeitosCombate.numero(get_tree(), global_position, str(int(valor)), cor)
	if hp <= 0.0:
		cair()


func receber_golpe(golpe: Dictionary) -> void:
	if estado == "morto" or _invencivel > 0.0:
		return
	var m := estados.consumir_golpe_mult() * Jogo.dif("recebido")
	if d.get("especial", {}).get("id", "") == "pele_de_pedra":   # Golias: só metade
		m *= float(d.especial.valor)
	var valor := maxi(1, int(golpe.get("valor", 1) * m))
	estados.do_golpe(golpe.get("estados", []), null, golpe.get("origem", Vector3.INF))
	EfeitosCombate.numero(get_tree(), global_position, str(valor), "normal")
	EfeitosCombate.piscar(boneco.sprite)
	hp -= valor
	_invencivel = 0.35
	hitbox.desligar()
	if hp <= 0.0:
		cair()
		return
	var fora: Vector3 = global_position - golpe.get("origem", global_position)
	fora.y = 0.0
	if fora.length() > 0.01:
		velocity = fora.normalized() * 4.0


func curar(valor: float) -> void:
	if estado == "morto" or valor <= 0.0:
		return
	var antes := hp
	hp = minf(hp_max, hp + valor)
	if hp - antes >= 1.0:
		EfeitosCombate.numero(get_tree(), global_position + Vector3(0, 0.4, 0), "+%d" % int(hp - antes), "cura")


func _beber_se_preciso() -> void:
	var lista: Array = Grupo.estado(id).pocoes
	if lista.is_empty() or _pocao_r > 0.0 or hp > hp_max * float(Grupo.c("pocao_hp", 0.35)):
		return
	var it: String = lista.pop_back()
	_pocao_r = float(Grupo.c("pocao_recarga", 8.0))
	curar(Grupo.cura_pocao(it, hp_max))
	EfeitosCombate.animado(get_tree(), "cura", global_position + Vector3(0, 1, 0))
	Audio.efeito("beber_pocao", 0.05, 0.6)


func cair() -> void:
	hp = 0.0
	estado = "morto"
	hitbox.desligar()
	boneco.esconder_arma()
	_caido_t = float(Grupo.c("levantar", 30.0))
	boneco.sprite.modulate = Color(0.55, 0.5, 0.65)
	_tocar("parado")
	_rotulo.visible = true
	_inter.ativo = true
	Sistema.mensagem("%s caiu! Levanta-se em %d s (ou dá-lhe uma poção: E)." % [d.get("nome_pt", id), int(_caido_t)], "aviso")


func levantar(fracao: float) -> void:
	estado = "normal"
	hp = hp_max * fracao
	boneco.sprite.modulate = Color.WHITE
	_rotulo.visible = false
	_inter.ativo = false
	_invencivel = 1.5
	EfeitosCombate.animado(get_tree(), "cura", global_position + Vector3(0, 1, 0))


func _dar_pocao_tua() -> void:
	var p := Grupo.pocoes_na_mochila()
	if p.is_empty():
		Sistema.mensagem("Não tens poções de vida.", "aviso")
		return
	Jogo.inventario.retirar(p[-1], 1)
	levantar(maxf(float(Grupo.c("levantar_hp", 0.5)), Grupo.cura_pocao(p[-1], hp_max) / hp_max))
	Audio.efeito("beber_pocao", 0.0)
	Sistema.mensagem("%s levanta-se!" % d.get("nome_pt", id))


# ------------------------------------------------------------------ animação ------------------------------------------------------------------

func _nome_direcao() -> String:
	if absf(direcao.x) > absf(direcao.y) * 1.1:
		return "lado"
	return "cima" if direcao.y < 0.0 else "baixo"


func _tocar(nome: String, vel: float = 1.0, recomecar: bool = false) -> void:
	var dn := _nome_direcao()
	boneco.flip = direcao.x < 0.0 and dn == "lado"
	var a := "%s_%s" % [nome, dn]
	if not boneco.tem(a):
		return
	if recomecar:
		boneco.recomecar(a, vel)
	else:
		boneco.tocar(a, vel)
