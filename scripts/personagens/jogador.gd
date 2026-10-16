class_name Jogador
extends CharacterBody3D
## O herói: andar, correr, esquivar (docs/SISTEMAS.md, secção 2.3) e combater com as 12 armas
## (docs/ARMAS.md, secção 1; dano em docs/SISTEMAS.md, secção 4).

signal estado_mudou(estado: String)

const ANIMS := {
	"parado": [5, true], "andar": [10, true], "esquiva": [16, false], "dano": [10, false], "morrer": [7, false],
	"recolher": [8, false], "ataque_corte": [14, false], "ataque_pesado": [10, false], "ataque_estocada": [14, false],
	"ataque_disparo": [12, false], "ataque_magia": [10, false], "ataque_soco": [16, false], "nadar": [8, true],
	"planar": [4, true], "montar": [4, true], "pescar": [6, false], "beber": [6, false], "celebrar": [8, false],
	"sentar": [1, true],
}
# tipo de arma -> [animação do herói, golpes do combo, largura da área (m), golpe em arco?]
const TIPOS := {
	"espada": ["ataque_corte", 3, 2.0, true], "espada_grande": ["ataque_pesado", 2, 3.2, true],
	"adaga": ["ataque_corte", 4, 1.4, true], "katana": ["ataque_corte", 3, 1.8, true],
	"machado": ["ataque_pesado", 2, 2.2, true], "martelo": ["ataque_pesado", 2, 2.4, true],
	"lanca": ["ataque_estocada", 3, 1.0, false], "foice": ["ataque_corte", 2, 3.4, true],
	"arco": ["ataque_disparo", 1, 0.0, false], "besta": ["ataque_disparo", 1, 0.0, false],
	"cajado": ["ataque_magia", 1, 0.0, false], "manoplas": ["ataque_soco", 6, 1.2, false],
}
const PROJETIL := {"arco": "flecha", "besta": "virote", "cajado": "projetil_luz"}

var estado: String = "normal"   # normal, esquiva, ataque, dano, morto
var direcao_olhar := Vector2(0, 1)   # x = direita, y = baixo no ecrã
var invencivel: float = 0.0
var correndo: bool = false
var arma: Dictionary = {}

var boneco: BonecoArma
var hitbox: Hitbox
var hurtbox: Hurtbox
var _mira: Node3D

var _esquiva_t: float = 0.0
var _esquiva_dir := Vector3.ZERO
var _espera_estamina: float = 0.0
var _ataque_t: float = 0.0
var _ataque_dur: float = 0.5
var _combo: int = 0
var _combo_pedido: bool = false
var _combo_janela: float = 0.0
var _mult_golpe: float = 1.0
var _carregar_t: float = 0.0
var _disparou: bool = false
var _gravidade: float = ProjectSettings.get_setting("physics/3d/default_gravity", 9.8)
var _ultimo_rato: float = -10.0
var _pocao_recarga: float = 0.0
var estados: Estados
var _carregado := false
var interagivel_perto: Interagivel = null


func _ready() -> void:
	add_to_group("jogador")
	collision_layer = 1 << 1
	collision_mask = 1
	var forma := CollisionShape3D.new()
	var capsula := CapsuleShape3D.new()
	capsula.radius = 0.3
	capsula.height = 1.4
	forma.shape = capsula
	forma.position.y = 0.7
	add_child(forma)
	boneco = BonecoArma.new(Folhas.criar("res://arte/heroi/heroi", ANIMS, ["baixo", "cima", "lado"]))
	add_child(boneco)
	add_child(Folhas.sombra(0.45))
	hurtbox = Hurtbox.criar(self, 1 << 1)
	add_child(hurtbox)
	_mira = Node3D.new()
	add_child(_mira)
	hitbox = Hitbox.new()
	hitbox.dono = self
	hitbox.collision_layer = 0
	hitbox.collision_mask = 1 << 2
	hitbox.calcular_golpe = _calcular_golpe
	hitbox.acertou.connect(_acertou)
	_mira.add_child(hitbox)
	estados = Estados.new()
	add_child(estados)
	Jogo.estados = estados
	estados.mudou.connect(func(): boneco.scale = Vector3.ONE * (0.5 if estados.tem("encolhido") else 1.0))
	equipar(Jogo.arma_equipada)
	Eventos.equipamento_mudou.connect(func(): equipar(Jogo.arma_equipada))
	tocar("parado")


func equipar(id: String) -> void:
	arma = Dados.arma(id)
	if arma.is_empty():
		arma = {"id": id, "tipo": "espada", "atq": 12, "velocidade": 1.6, "alcance": 1.8, "critico": 0.05}
	boneco.por_arma(load(arma.get("sprite", "")) if ResourceLoader.exists(arma.get("sprite", "")) else null)
	var t: Array = TIPOS.get(arma.tipo, TIPOS.espada)
	for f in hitbox.get_children():
		f.queue_free()
	if t[2] > 0.0:
		hitbox.add_child(Hitbox.caixa(t[2], float(arma.alcance) + 0.4))


# ------------------------------------------------------------------ ciclo ------------------------------------------------------------------

func _unhandled_input(evento: InputEvent) -> void:
	if evento is InputEventMouseMotion:
		_ultimo_rato = Time.get_ticks_msec() / 1000.0


func _physics_process(delta: float) -> void:
	invencivel = max(0.0, invencivel - delta)
	_combo_janela = max(0.0, _combo_janela - delta)
	_pocao_recarga = max(0.0, _pocao_recarga - delta)
	interagivel_perto = _procurar_interagivel()
	_regenerar(delta)
	if not is_on_floor():
		velocity.y -= _gravidade * delta
	else:
		velocity.y = 0.0
	if estado != "morto" and estados.flag("parado"):
		if Input.is_action_just_pressed("atacar") or Input.is_action_just_pressed("esquivar"):
			estados.sacudir()
		if estado in ["ataque", "esquiva"]:
			hitbox.desligar()
			boneco.esconder_arma()
			mudar_estado("normal")
		_travar(delta)
		move_and_slide()
		return
	if estados.tem("puxado") and estados.origem != Vector3.INF and estado != "morto":
		var p := estados.origem - global_position
		p.y = 0.0
		if p.length() > 1.0:
			global_position += p.normalized() * float(Estados.info("puxado").get("puxar", 1.5)) * delta
	match estado:
		"normal":
			_andar(delta)
			if not estados.flag("sem_atacar"):
				_entrada_ataque(delta)
		"esquiva":
			_esquivar(delta)
		"ataque":
			_atacar(delta)
		_:
			_travar(delta)
	move_and_slide()
	if invencivel > 0.0 and estado != "esquiva":
		boneco.visible = int(invencivel * 20.0) % 2 == 0
	else:
		boneco.visible = true


func _travar(delta: float) -> void:
	velocity.x = move_toward(velocity.x, 0.0, 25.0 * delta)
	velocity.z = move_toward(velocity.z, 0.0, 25.0 * delta)


func _andar(delta: float) -> void:
	var d := Entrada.direcao()
	if estados.flag("trocar_controlos"):
		d = -d
	correndo = Input.is_action_pressed("correr") and d != Vector2.ZERO and Jogo.estamina > 1.0
	var vel := Jogo.velocidade() * estados.mult("vel_mult")
	if correndo:
		vel *= float(Dados.c("correr_mult"))
		Jogo.estamina = max(0.0, Jogo.estamina - float(Dados.c("correr_custo")) * delta)
		_espera_estamina = float(Dados.c("regen_estamina_espera"))
	velocity.x = d.x * vel
	velocity.z = d.y * vel
	if d != Vector2.ZERO:
		direcao_olhar = d.normalized()
		tocar("andar", 1.4 if correndo else 1.0)
	else:
		tocar("parado")
	boneco.esconder_arma()
	if Input.is_action_just_pressed("esquivar"):
		comecar_esquiva()
	elif Input.is_action_just_pressed("interagir") and interagivel_perto:
		interagivel_perto.interagir(self)
	elif Input.is_action_just_pressed("pocao"):
		beber()
	elif Input.is_action_just_pressed("trocar_arma"):
		trocar_arma()


# ------------------------------------------------------------------ interagir, poções, armas ------------------------------------------------------------------

func _procurar_interagivel() -> Interagivel:
	var melhor: Interagivel = null
	var dist := float(Dados.c("interagir_distancia", 1.5)) + 0.6
	for i in get_tree().get_nodes_in_group("interagivel"):
		var it := i as Interagivel
		if it == null or not it.ativo:
			continue
		var d := it.global_position.distance_to(global_position)
		if d < dist:
			dist = d
			melhor = it
	return melhor


## Bebe a primeira poção da barra rápida (0,6 s a beber, recarga de 2 s; docs/SISTEMAS.md, secção 2.3).
func beber() -> void:
	if _pocao_recarga > 0.0:
		return
	for id in Jogo.inventario.barra_rapida:
		if id != "" and Jogo.inventario.tem(id) and not Inventario._dados(id).get("efeito", {}).is_empty():
			mudar_estado("ocupado")
			tocar("beber", 1.0, true)
			_pocao_recarga = float(Dados.c("pocao_recarga"))
			await get_tree().create_timer(float(Dados.c("pocao_tempo"))).timeout
			if estado == "ocupado":   # se levou dano a meio, foi interrompido
				Jogo.usar_consumivel(id)
				EfeitosCombate.animado(get_tree(), "cura", global_position + Vector3(0, 1, 0))
				mudar_estado("normal")
			return
	Sistema.mensagem("Não tens poções na barra rápida.", "aviso")


func trocar_arma() -> void:
	if Jogo.arma_2 == "":
		Sistema.mensagem("Não tens uma segunda arma equipada.", "aviso")
		return
	var a := Jogo.arma_equipada
	Jogo.arma_equipada = Jogo.arma_2
	Jogo.arma_2 = a
	Eventos.equipamento_mudou.emit()
	Sistema.mensagem("Arma: %s" % arma.get("nome_pt", arma.get("id", "")))


# ------------------------------------------------------------------ esquiva ------------------------------------------------------------------

func comecar_esquiva() -> void:
	if not Jogo.gastar_estamina(float(Dados.c("esquiva_custo"))):
		Sistema.mensagem("Estamina insuficiente.", "aviso")
		return
	_espera_estamina = float(Dados.c("regen_estamina_espera"))
	var d := Entrada.direcao()
	if d == Vector2.ZERO:
		d = direcao_olhar
	direcao_olhar = d.normalized()
	_esquiva_dir = Vector3(d.x, 0, d.y).normalized()
	_esquiva_t = float(Dados.c("esquiva_duracao"))
	invencivel = max(invencivel, float(Dados.c("esquiva_invencivel")))
	hitbox.desligar()
	boneco.esconder_arma()
	mudar_estado("esquiva")
	tocar("esquiva", 1.0, true)


func _esquivar(delta: float) -> void:
	var v := float(Dados.c("esquiva_distancia")) / float(Dados.c("esquiva_duracao"))
	velocity.x = _esquiva_dir.x * v
	velocity.z = _esquiva_dir.z * v
	_esquiva_t -= delta
	if _esquiva_t <= 0.0:
		mudar_estado("normal")


# ------------------------------------------------------------------ ataque ------------------------------------------------------------------

func _entrada_ataque(delta: float) -> void:
	if Input.is_action_pressed("ataque_forte"):
		_carregar_t += delta
		# a carregar: o herói brilha um pouco quando o golpe está pronto
		boneco.sprite.modulate = Color(1.6, 1.5, 1.0) if _carregar_t >= float(Dados.c("carregado_tempo")) else Color.WHITE
	elif _carregar_t > 0.0:
		var cheio := _carregar_t >= float(Dados.c("carregado_tempo"))
		_carregar_t = 0.0
		boneco.sprite.modulate = Color.WHITE
		if cheio and Jogo.gastar_estamina(float(Dados.c("carregado_custo"))):
			_espera_estamina = float(Dados.c("regen_estamina_espera"))
			comecar_ataque(float(Dados.c("carregado_mult")), true)
		else:
			comecar_ataque(_mult_combo())
	elif Input.is_action_just_pressed("atacar"):
		comecar_ataque(_mult_combo())


func _mult_combo() -> float:
	var n: int = TIPOS.get(arma.tipo, TIPOS.espada)[1]
	var mults: Array = Dados.c("combo_mult")
	if _combo_janela <= 0.0:
		_combo = 0
	if n == 1:
		return mults[0]
	if _combo >= n - 1:
		return mults[2]
	return mults[0] if _combo == 0 else mults[1]


func comecar_ataque(mult: float, carregado: bool = false) -> void:
	_virar_para_mira()
	_mult_golpe = mult
	_carregado = carregado
	_ataque_dur = 1.0 / max(0.3, float(arma.get("velocidade", 1.0)) * estados.mult("atq_vel_mult"))
	if carregado:
		_ataque_dur *= 1.3
	_ataque_t = 0.0
	_combo_pedido = false
	_disparou = false
	var t: Array = TIPOS.get(arma.tipo, TIPOS.espada)
	var anim: String = t[0]
	var frames := boneco.corpo.sprite_frames
	var nome := "%s_%s" % [anim, nome_direcao()]
	var n_frames := frames.get_frame_count(nome) if frames.has_animation(nome) else 4
	var fps := frames.get_animation_speed(nome) if frames.has_animation(nome) else 12.0
	tocar(anim, n_frames / fps / _ataque_dur, true)
	mudar_estado("ataque")
	_mira.rotation.y = atan2(-direcao_olhar.x, -direcao_olhar.y)
	velocity.x = direcao_olhar.x * 1.5
	velocity.z = direcao_olhar.y * 1.5
	if carregado:
		EfeitosCombate.animado(get_tree(), "critico", global_position + Vector3(0, 1, 0))


func _atacar(delta: float) -> void:
	_ataque_t += delta
	var p := _ataque_t / _ataque_dur
	_travar(delta)
	_pose_arma(p)
	var tipo: String = arma.get("tipo", "espada")
	if tipo in PROJETIL:
		if p >= 0.45 and not _disparou:
			_disparou = true
			_disparar()
	else:
		if p >= 0.3 and p < 0.65 and not hitbox.ligada:
			hitbox.ligar()
		elif p >= 0.65 and hitbox.ligada:
			hitbox.desligar()
	if Input.is_action_just_pressed("atacar") and p > 0.4:
		_combo_pedido = true
	if Input.is_action_just_pressed("esquivar") and p > 0.5:
		hitbox.desligar()
		mudar_estado("normal")
		comecar_esquiva()
		return
	if p >= 1.0:
		hitbox.desligar()
		var n: int = TIPOS.get(tipo, TIPOS.espada)[1]
		_combo = (_combo + 1) % max(1, n)
		_combo_janela = 0.45
		mudar_estado("normal")
		if _combo_pedido:
			comecar_ataque(_mult_combo())


## Pose da arma ao longo do golpe (p de 0 a 1), conforme a animação do tipo.
func _pose_arma(p: float) -> void:
	var anim: String = TIPOS.get(arma.get("tipo", "espada"), TIPOS.espada)[0]
	var atras := nome_direcao() == "cima"
	var e := ease(clamp((p - 0.15) / 0.5, 0.0, 1.0), 0.4)
	match anim:
		"ataque_corte":
			boneco.pose_arma(lerp(-110.0, 120.0, e), Vector2(0, -4), atras)
		"ataque_pesado":
			boneco.pose_arma(lerp(-170.0, 100.0, e), Vector2(-2, -6), atras)
		"ataque_estocada":
			boneco.pose_arma(90.0, Vector2(lerp(-8.0, 10.0, e), -6), atras)
		"ataque_disparo":
			boneco.pose_arma(90.0 if arma.tipo == "besta" else 0.0, Vector2(4, -8), atras)
		"ataque_magia":
			boneco.pose_arma(lerp(-30.0, 15.0, e), Vector2(2, -10), atras)
		_:
			boneco.esconder_arma()


func _disparar() -> void:
	var nome: String = PROJETIL.get(arma.tipo, "flecha")
	var p := Projetil.new()
	p.textura = "res://arte/efeitos/%s.png" % nome
	p.dono = self
	p.alcance = float(arma.get("alcance", 15.0))
	p.velocidade = 22.0 if arma.tipo != "cajado" else 14.0
	p.direcao = Vector3(direcao_olhar.x, 0, direcao_olhar.y).normalized()
	p.calcular_golpe = _calcular_golpe
	p.acertou.connect(_acertou)
	get_tree().current_scene.add_child(p)
	p.global_position = global_position + Vector3(0, 1.0, 0) + p.direcao * 0.6


func _calcular_golpe(alvo: Node) -> Dictionary:
	var c := Dados.constantes
	var magico: bool = arma.get("tipo", "") == "cajado"
	var distancia: bool = arma.get("distancia", false)
	var atq: float
	if magico:
		atq = Formulas.atq_magico(c, float(arma.get("atq_magico", 0)), 0, 1.0, Jogo.a("int"))
	else:
		atq = Formulas.atq_fisico(c, float(arma.get("atq", 0)), 0, 1.0, Jogo.a("for"), Jogo.a("des"), distancia)
	var info: Dictionary = alvo.info_dano() if alvo.has_method("info_dano") else {}
	var mult := _mult_golpe * estados.mult("dano_mult") * Jogo.buff("atq")
	if arma.get("tipo", "") == "adaga" and alvo is Node3D and _pelas_costas(alvo):
		mult *= float(c.costas_mult)
	var defesa: float = info.get("res", 0.0) if magico else info.get("def", 0.0)
	var g := Dano.calcular(atq, mult, defesa, info, arma.get("elemento", "") if arma.get("elemento") else "",
			Jogo.critico(float(arma.get("critico", 0.0))), float(c.critico_dano), magico)
	g["empurrao"] = float(c.empurrao_pesado) if arma.get("tipo", "") in ["espada_grande", "martelo", "machado"] else float(c.empurrao)
	g["estados"] = arma.get("efeitos", []).filter(func(e): return _carregado or not e.get("so_carregado", false))
	if arma.get("tipo", "") == "martelo" and _carregado:
		g.estados = g.estados + [{"estado": "atordoado", "hipotese": 1.0}]
	return g


func info_dano() -> Dictionary:
	var elem := {}
	for el in ["fogo", "gelo", "raio", "veneno", "luz", "sombra"]:
		elem[el] = estados.mult_elemento(el)
	return {"def": Jogo.defesa() * estados.mult("def_mult"), "res": Jogo.resistencia(), "fraquezas": [], "resistencias": [],
			"imunidades": [], "atordoado": estados.tem("atordoado"), "elem_mult": elem}


func hp_maximo_estado() -> float:
	return float(Jogo.hp_maximo())


func perder_hp_estado(valor: float, cor: String, minimo_1: bool) -> void:
	if estado == "morto":
		return
	Jogo.hp = max(1.0 if minimo_1 else 0.0, Jogo.hp - valor)
	Eventos.stats_mudaram.emit()
	EfeitosCombate.numero(get_tree(), global_position, str(int(valor)), cor)
	if Jogo.hp <= 0.0:
		morrer()


func _pelas_costas(alvo: Node3D) -> bool:
	if not "olhar_x" in alvo:
		return false
	return sign(alvo.global_position.x - global_position.x) == sign(alvo.olhar_x)


func _acertou(_alvo: Node, golpe: Dictionary) -> void:
	EfeitosCombate.hitstop(get_tree(), float(Dados.c("hitstop_critico" if golpe.critico else "hitstop")))
	var cam := get_viewport().get_camera_3d()
	if cam and cam.has_method("tremer"):
		cam.tremer(0.08 if not golpe.critico else 0.16, 0.12)


func _virar_para_mira() -> void:
	var agora := Time.get_ticks_msec() / 1000.0
	if Entrada.dispositivo == "teclado" and agora - _ultimo_rato < 3.0:
		var alvo := _ponto_do_rato()
		if alvo != Vector3.INF:
			var d := Vector2(alvo.x - global_position.x, alvo.z - global_position.z)
			if d.length() > 0.2:
				direcao_olhar = d.normalized()
				return
	var mov := Entrada.direcao()
	if mov != Vector2.ZERO:
		direcao_olhar = mov.normalized()


func _ponto_do_rato() -> Vector3:
	var cam := get_viewport().get_camera_3d()
	if cam == null:
		return Vector3.INF
	var m := get_viewport().get_mouse_position()
	var origem := cam.project_ray_origin(m)
	var dir := cam.project_ray_normal(m)
	if abs(dir.y) < 0.001:
		return Vector3.INF
	var t := (global_position.y - origem.y) / dir.y
	return origem + dir * t if t > 0.0 else Vector3.INF


# ------------------------------------------------------------------ levar dano ------------------------------------------------------------------

func receber_golpe(golpe: Dictionary) -> void:
	if estado == "morto" or invencivel > 0.0:
		return
	var valor: int = int(golpe.get("valor", 1) * estados.consumir_golpe_mult())
	estados.do_golpe(golpe.get("estados", []), null, golpe.get("origem", Vector3.INF))
	Jogo.receber_dano(valor)
	EfeitosCombate.numero(get_tree(), global_position, str(valor), "jogador")
	EfeitosCombate.piscar(boneco.sprite)
	invencivel = float(Dados.c("invencivel_dano"))
	var cam := get_viewport().get_camera_3d()
	if cam and cam.has_method("tremer"):
		cam.tremer(0.2, 0.2)
	hitbox.desligar()
	boneco.esconder_arma()
	if Jogo.hp <= 0.0:
		morrer()
		return
	var origem: Vector3 = golpe.get("origem", global_position)
	var fora := (global_position - origem)
	fora.y = 0.0
	if fora.length() > 0.01:
		velocity = fora.normalized() * 5.0
	mudar_estado("dano")
	tocar("dano", 1.0, true)
	await get_tree().create_timer(0.3).timeout
	if estado == "dano":
		mudar_estado("normal")


## Morrer (docs/SISTEMAS.md, secção 8): perdes 30% dos materiais apanhados neste andar, o dia avança para as 6:00
## e acordas na Zona Segura (na Estalagem, quando a cidade estiver pronta).
func morrer() -> void:
	mudar_estado("morto")
	velocity = Vector3.ZERO
	hitbox.desligar()
	tocar("morrer", 1.0, true)
	Sistema.mensagem("Os teus pontos de vida chegaram a zero.", "aviso")
	await get_tree().create_timer(2.5).timeout
	var rng := RandomNumberGenerator.new()
	rng.randomize()
	var perdidos := Jogo.perder_materiais_do_andar(rng)
	if not perdidos.is_empty():
		Sistema.mensagem("Perdeste alguns materiais pelo caminho.", "aviso")
	Tempo.dia += 1
	Tempo.hora = 6.0
	Jogo.encher()
	var andar := get_parent() as Andar
	global_position = (andar.ponto_seguro if andar else Vector3.ZERO) + Vector3(0, 0.5, 0)
	invencivel = 2.0
	mudar_estado("normal")


# ------------------------------------------------------------------ ajudas ------------------------------------------------------------------

func _regenerar(delta: float) -> void:
	if _espera_estamina > 0.0:
		_espera_estamina -= delta
	else:
		var maximo := float(Jogo.estamina_maxima())
		if Jogo.estamina < maximo:
			Jogo.estamina = min(maximo, Jogo.estamina + float(Dados.c("regen_estamina")) * delta)
	var mp_max := float(Jogo.mp_maximo())
	if Jogo.mp < mp_max:
		Jogo.mp = min(mp_max, Jogo.mp + mp_max * float(Dados.c("regen_mp")) * delta)


func mudar_estado(novo: String) -> void:
	if novo == estado:
		return
	estado = novo
	estado_mudou.emit(novo)


## Toca uma animação na direção para onde o herói está virado ("baixo", "cima" ou "lado" espelhado).
func tocar(nome: String, velocidade: float = 1.0, recomecar: bool = false) -> void:
	var d := nome_direcao()
	boneco.flip = direcao_olhar.x < 0.0 and d == "lado"
	var a := "%s_%s" % [nome, d]
	if not boneco.tem(a):
		return
	if recomecar:
		boneco.recomecar(a, velocidade)
	else:
		boneco.tocar(a, velocidade)


func nome_direcao() -> String:
	if abs(direcao_olhar.x) > abs(direcao_olhar.y) * 1.1:
		return "lado"
	return "cima" if direcao_olhar.y < 0.0 else "baixo"
