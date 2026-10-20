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
var recargas_skill: Dictionary = {}
var _skill_t: float = 0.0
var _skill_vel := Vector3.ZERO
var _sem_combate: float = 99.0
var _regen_hp_t: float = 0.0
var _golpes_dados: int = 0
var _esquivas_seguidas: int = 0
var _carregado := false
var interagivel_perto: Interagivel = null
var a_nadar: bool = false   # na água funda (docs/SISTEMAS.md 2.5)
var barco: Barco = null     # no barco: anda pela água funda sem gastar Ar
var _nadar_t: float = 0.0


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
	# o aspeto escolhido na criação de personagem (penteado + trocas de cor); sem ele, o herói base
	var sf := Aparencia.frames(Jogo.aparencia, ANIMS, ["baixo", "cima", "lado"]) if Jogo.aparencia.get("penteado", "") != "" else null
	if sf == null or sf.get_animation_names().is_empty():
		sf = Folhas.criar("res://arte/heroi/heroi", ANIMS, ["baixo", "cima", "lado"])
	boneco = BonecoArma.new(sf)
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
	RenderingServer.global_shader_parameter_set("jogador_pos", global_position)   # plantas à frente ficam transparentes
	invencivel = max(0.0, invencivel - delta)
	_combo_janela = max(0.0, _combo_janela - delta)
	_pocao_recarga = max(0.0, _pocao_recarga - delta)
	_sem_combate += delta
	for k in recargas_skill.keys():
		recargas_skill[k] -= delta
		if recargas_skill[k] <= 0.0:
			recargas_skill.erase(k)
	interagivel_perto = _procurar_interagivel()
	_regenerar(delta)
	_ver_agua(delta)
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
			if not estados.flag("sem_atacar") and not a_nadar and not barco:   # a nadar (ou no barco) não se ataca
				_entrada_ataque(delta)
		"esquiva":
			_esquivar(delta)
		"ataque":
			_atacar(delta)
		"skill":
			_skill_t -= delta
			velocity.x = _skill_vel.x
			velocity.z = _skill_vel.z
			if _skill_t <= 0.0:
				_skill_vel = Vector3.ZERO
				mudar_estado("normal")
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
	if Jogo.inventario.peso() > Jogo.peso_maximo():
		vel *= float(Dados.c("carga_lento"))
	if a_nadar:
		vel *= float(Dados.c("nadar", {}).get("vel", 0.6))
		correndo = false
	if barco:   # o barco só anda na água funda
		vel *= float(Dados.c("nadar", {}).get("barco_vel", 1.3))
		correndo = false
		var an := get_parent() as Andar
		if d != Vector2.ZERO and an:
			var cel := an.celula_de(global_position + Vector3(d.x, 0, d.y) * 1.2)
			if not an.codigo(cel.x, cel.y) in ["~~", "ww", "JJ", ",,"]:   # não sobe para terra
				d = Vector2.ZERO
	if correndo:
		vel *= float(Dados.c("correr_mult"))
		Jogo.estamina = max(0.0, Jogo.estamina - float(Dados.c("correr_custo")) * delta)
		_espera_estamina = float(Dados.c("regen_estamina_espera"))
	velocity.x = d.x * vel
	velocity.z = d.y * vel
	if d != Vector2.ZERO:
		direcao_olhar = d.normalized()
		tocar("montar" if barco else ("nadar" if a_nadar else "andar"), 1.4 if correndo else 1.0)
		if is_on_floor() and not a_nadar:
			Audio.passos(delta, correndo, (Jogo.andar_atual - 1) / 10 + 1 if Jogo.andar_atual > 0 else 2)
	else:
		tocar("montar" if barco else ("nadar" if a_nadar else "parado"), 0.5 if a_nadar else 1.0)
	boneco.esconder_arma()
	if barco and Input.is_action_just_pressed("interagir"):
		sair_barco()
		return
	if (a_nadar or barco) and (Input.is_action_just_pressed("esquivar") or _alguma_skill_carregada()):
		return   # a nadar não se esquiva nem se usam skills (as poções e o E continuam a funcionar)
	if Input.is_action_just_pressed("esquivar"):
		comecar_esquiva()
	elif Input.is_action_just_pressed("interagir") and interagivel_perto:
		interagivel_perto.interagir(self)
	elif Input.is_action_just_pressed("pocao"):
		beber()
	elif Input.is_action_just_pressed("trocar_arma"):
		trocar_arma()
	else:
		for i in 6:
			if Input.is_action_just_pressed("skill_%d" % (i + 1)):
				usar_skill(i)
				break


## Entrar no barco (Barco, E ao pé dele).
func entrar_barco(b: Barco) -> void:
	if barco or estado != "normal":
		return
	barco = b
	b.inter.ativo = false
	global_position = b.global_position + Vector3(0, 0.4, 0)
	velocity = Vector3.ZERO
	Audio.efeito("nadar", 0.1, 0.6)
	Sistema.mensagem("No barco: E junto à margem para sair.")


## Sair do barco para a margem mais perto (o barco fica ali).
func sair_barco() -> void:
	var a := get_parent() as Andar
	if barco == null or a == null:
		return
	for i in 16:
		var ang := TAU * i / 16.0
		var p := global_position + Vector3(cos(ang), 0, sin(ang)) * 2.2
		var c := a.celula_de(p)
		if not a.agua_funda_em(p) and not a.codigo(c.x, c.y) in ["TT", "##", "  ", "~~", "ww"]:
			barco.inter.ativo = true
			barco = null
			global_position = Vector3(p.x, global_position.y + 0.5, p.z)
			return
	Sistema.mensagem("Leva o barco até à margem para sair.", "aviso")


func _alguma_skill_carregada() -> bool:
	for i in 6:
		if Input.is_action_just_pressed("skill_%d" % (i + 1)):
			return true
	return false


## Água funda: nadar (mais devagar, sem atacar); no oceano, debaixo de água, com a barra de Ar (docs/SISTEMAS.md 2.5).
func _ver_agua(delta: float) -> void:
	var a := get_parent() as Andar
	var cfg: Dictionary = Dados.c("nadar", {})
	if barco:   # no barco: não se nada, não se gasta Ar; o barco vai com o herói
		a_nadar = false
		barco.global_position = global_position + Vector3(0, -0.1, 0.05)
		Jogo.ar = minf(float(cfg.get("ar_max", 30.0)), Jogo.ar + delta * 10.0)
		return
	var agua := a != null and estado != "morto" and a.agua_funda_em(global_position)
	if agua != a_nadar:
		a_nadar = agua
		EfeitosCombate.animado(get_tree(), "explosao_gelo" if agua else "poeira", global_position + Vector3(0, 0.4, 0.1), 20.0)
		Audio.efeito("nadar", 0.1, 0.7)
		if agua and estado in ["ataque", "esquiva"]:
			hitbox.desligar()
			mudar_estado("normal")
	var maximo := float(cfg.get("ar_max", 30.0))
	if a_nadar and a.regiao == int(cfg.get("regiao_ar", 6)):
		Jogo.ar = maxf(0.0, Jogo.ar - delta)
		_nadar_t += delta
		if _nadar_t >= 1.0:   # de segundo a segundo: Encharcado e, sem ar, perde 5% do HP
			_nadar_t = 0.0
			estados.aplicar("encharcado", 2.0)
			if Jogo.ar <= 0.0:
				perder_hp_estado(maxf(1.0, float(Jogo.hp_maximo()) * float(cfg.get("sem_ar_dano", 0.05))), "#4d9be6", false)
	elif Jogo.ar < maximo:
		Jogo.ar = minf(maximo, Jogo.ar + maximo / maxf(0.1, float(cfg.get("ar_encher_s", 3.0))) * delta)


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
			Audio.efeito("beber_pocao", 0.0)
			_pocao_recarga = float(Dados.c("pocao_recarga"))
			await get_tree().create_timer(float(Dados.c("pocao_tempo"))).timeout
			if estado == "ocupado":   # se levou dano a meio, foi interrompido
				Jogo.usar_consumivel(id)
				EfeitosCombate.animado(get_tree(), "cura", global_position + Vector3(0, 1, 0))
				mudar_estado("normal")
			return
	Sistema.mensagem("Não tens poções na barra rápida.", "aviso")


## Pequena animação para recolher (partir, cortar, apanhar) virado para o ponto.
func animar_acao(alvo: Vector3, ferramenta: String) -> void:
	var d := Vector2(alvo.x - global_position.x, alvo.z - global_position.z)
	if d.length() > 0.05:
		direcao_olhar = d.normalized()
	mudar_estado("ocupado")
	tocar("ataque_pesado" if ferramenta != "mao" else "recolher", 1.4, true)
	await get_tree().create_timer(0.35).timeout
	if estado == "ocupado":
		mudar_estado("normal")


func trocar_arma() -> void:
	if Jogo.arma_2 == "":
		Sistema.mensagem("Não tens uma segunda arma equipada.", "aviso")
		return
	var a := Jogo.arma_equipada
	var ax := Jogo.arma_extra
	Jogo.arma_equipada = Jogo.arma_2
	Jogo.arma_extra = Jogo.arma_2_extra
	Jogo.arma_2 = a
	Jogo.arma_2_extra = ax
	Eventos.equipamento_mudou.emit()
	Sistema.mensagem("Arma: %s" % arma.get("nome_pt", arma.get("id", "")))


# ------------------------------------------------------------------ skills ------------------------------------------------------------------

## Usa a skill do espaço i da barra (teclas 1–6): paga o custo, começa a recarga e faz a ação.
func usar_skill(i: int) -> void:
	var id: String = Jogo.skills_barra[i]
	if id == "" or estado != "normal":
		return
	var s := Jogo.skill(id)
	if s.is_empty():
		return
	if estados.flag("sem_skills"):
		Sistema.mensagem("Não podes usar skills agora.", "aviso")
		return
	if s.has("arma") and s.arma != arma.get("tipo", ""):
		Sistema.mensagem("%s precisa de %s." % [s.nome_pt, String(s.arma).replace("_", " ")], "aviso")
		return
	if recargas_skill.has(id):
		return
	var cu: Dictionary = s.get("custo", {})
	if cu.has("mp"):
		if Jogo.mp < float(cu.mp):
			Sistema.mensagem("MP insuficiente.", "aviso")
			return
		Jogo.mp -= float(cu.mp)
	elif cu.has("estamina"):
		if not Jogo.gastar_estamina(float(cu.estamina)):
			Sistema.mensagem("Estamina insuficiente.", "aviso")
			return
		_espera_estamina = float(Dados.c("regen_estamina_espera"))
	elif cu.has("hp_percent"):
		Jogo.hp = max(1.0, Jogo.hp - Jogo.hp_maximo() * float(cu.hp_percent))
	recargas_skill[id] = float(s.get("recarga", 5.0))
	Eventos.stats_mudaram.emit()
	EfeitosCombate.numero(get_tree(), global_position + Vector3(0, 0.6, 0), s.nome_pt, "texto")
	_executar_skill(s)


## Faz a ação de uma skill (forma: golpe, multi, area, linha, investida, projetil, buff, cura).
func _executar_skill(s: Dictionary) -> void:
	_virar_para_mira()
	var forma: String = s.get("forma", "golpe")
	var mult := float(s.get("mult", 1.5))
	var el: String = s.get("elemento", "") if s.get("elemento") else ""
	if s.get("elemento_da_gema", false):
		el = arma.get("elemento") if arma.get("elemento") else "fogo"
	var est: Array = s.get("estados", [])
	var dir := Vector3(direcao_olhar.x, 0, direcao_olhar.y).normalized()
	var n := int(s.get("golpes", 1))
	var t: Array = TIPOS.get(arma.get("tipo", "espada"), TIPOS.espada)
	tocar(t[0], 1.6, true)
	mudar_estado("skill")
	_skill_t = 0.35
	SkillFx.preparar(get_tree(), self, el, forma in ["area", "linha", "buff", "cura"] or arma.get("tipo", "") == "cajado")
	boneco.sprite.modulate = Color(1.5, 1.45, 1.2)   # o herói brilha um instante ao usar a skill
	get_tree().create_timer(0.15).timeout.connect(func(): if is_instance_valid(boneco): boneco.sprite.modulate = Color.WHITE)
	match forma:
		"multi":
			if not "×" in String(s.get("efeito_pt", "")):
				mult = 0.6 if n > 3 else 1.0
			_skill_t = 0.1 * n + 0.15
			for k in n:
				_atingir(global_position + dir * 1.2, 1.6, mult, el, est)
				SkillFx.corte_multi(get_tree(), global_position + dir * 1.2, dir, k)
				tocar(t[0], 2.2, true)
				boneco.pose_golpe(t[0], 0.5 if k % 2 == 0 else 0.0, nome_direcao() == "cima", String(arma.get("tipo", "")))
				await get_tree().create_timer(0.1).timeout
		"area":
			var raio := float(s.get("dist", 3.0))
			for k in n:
				_atingir(global_position, raio, mult, el, est)
				SkillFx.onda(get_tree(), global_position, raio, el)
				if n > 1:
					await get_tree().create_timer(0.25).timeout
			_skill_t = 0.25 * n + 0.1
		"linha":
			var comp := float(s.get("dist", 6.0))
			_atingir(global_position, comp, mult, el, est, dir)
			var nome := "explosao_" + el if el != "" else "estocada"
			EfeitosCombate.animado(get_tree(), "estocada", global_position + dir * 1.4 + Vector3(0, 0.9, 0.05), 24.0, dir.x < 0.0)
			for k in int(comp / 1.5):
				EfeitosCombate.animado(get_tree(), nome, global_position + dir * (1.0 + k * 1.5) + Vector3(0, 0.8, 0), 22.0, dir.x < 0.0)
				await get_tree().create_timer(0.03).timeout
			SkillFx.tremer(get_tree(), 0.12)
		"investida":
			var dist := float(s.get("dist", 4.0))
			if "teletransporte" in String(s.get("efeito_pt", "")):
				var alvo := _monstro_mais_perto(8.0)
				if alvo:
					var atras := Vector3(sign(alvo.olhar_x) if "olhar_x" in alvo else 1.0, 0, 0)
					global_position = alvo.global_position - atras * 1.2
					direcao_olhar = Vector2(atras.x, 0)
				EfeitosCombate.animado(get_tree(), "poeira", global_position + Vector3(0, 0.4, 0))
			else:
				_skill_t = 0.22
				_skill_vel = dir * dist / 0.22
				invencivel = max(invencivel, 0.25)
				for k in 4:   # fantasmas pelo caminho
					SkillFx.fantasma(boneco, el)
					await get_tree().create_timer(0.055).timeout
			_atingir(global_position + dir * 0.8, 2.0, mult, el, est)
			EfeitosCombate.animado(get_tree(), "explosao_" + (el if el != "" else "fisico"), global_position + dir + Vector3(0, 0.6, 0))
			EfeitosCombate.animado(get_tree(), "impacto", global_position + dir * 1.1 + Vector3(0, 0.9, 0.1), 24.0)
			SkillFx.tremer(get_tree(), 0.14)
		"projetil":
			EfeitosCombate.animado(get_tree(), "impacto", global_position + dir * 0.7 + Vector3(0, 1.0, 0.1), 30.0)
			for k in n:
				var p := Projetil.new()
				p.textura = "res://arte/efeitos/%s.png" % ("projetil_" + el if el != "" else PROJETIL.get(arma.get("tipo", ""), "projetil_pedra"))
				p.dono = self
				p.alcance = 16.0
				p.velocidade = 18.0
				p.direcao = dir.rotated(Vector3.UP, (k - (n - 1) / 2.0) * 0.15)
				p.calcular_golpe = func(alvo): return _golpe_skill(alvo, mult, el, est)
				p.acertou.connect(_acertou)
				get_tree().current_scene.add_child(p)
				p.global_position = global_position + Vector3(0, 1.0, 0) + p.direcao * 0.6
		"buff":
			var b: Dictionary = s.get("buff", {"stat": "atq", "valor": 0.2, "dura": 10})
			Jogo.buffs[String(b.stat)] = [float(b.valor), float(b.dura)]
			EfeitosCombate.animado(get_tree(), "subir_nivel", global_position + Vector3(0, 1, 0))
			SkillFx.onda(get_tree(), global_position, 1.5, "luz", 0)
			Eventos.stats_mudaram.emit()
		"cura":
			Jogo.curar(Jogo.hp_maximo() * 0.3)
			EfeitosCombate.animado(get_tree(), "cura", global_position + Vector3(0, 1, 0))
			SkillFx.onda(get_tree(), global_position, 2.0, "cura")
		_:
			_atingir(global_position + dir * 1.2, float(arma.get("alcance", 1.8)) + 0.6, mult, el, est)
			EfeitosCombate.animado(get_tree(), "corte_pesado", global_position + dir * 1.2 + Vector3(0, 1.0, 0.05), 26.0, dir.x < 0.0)
			SkillFx.tremer(get_tree(), 0.1)


func _golpe_skill(alvo: Node, mult: float, el: String, est: Array) -> Dictionary:
	var g := golpe_com(alvo, mult, el, est)
	g["skill"] = true
	return g


## Acerta em todos os monstros dentro de um círculo (ou de uma linha, se "linha" não for zero).
func _atingir(centro: Vector3, raio: float, mult: float, el: String, est: Array, linha := Vector3.ZERO) -> int:
	var n := 0
	for m in get_tree().get_nodes_in_group("monstros"):
		if not is_instance_valid(m) or m.estado == "morto":
			continue
		var d: Vector3 = m.global_position - centro
		d.y = 0.0
		var dentro := false
		if linha != Vector3.ZERO:
			var ao_longo := d.dot(linha)
			dentro = ao_longo >= -0.5 and ao_longo <= raio and (d - linha * ao_longo).length() < 1.3
		else:
			dentro = d.length() <= raio
		if dentro:
			var g := _golpe_skill(m, mult, el, est)
			m.receber_golpe(g)
			_acertou(m, g)
			n += 1
	return n


func _monstro_mais_perto(raio: float) -> Node3D:
	var melhor: Node3D = null
	var dist := raio
	for m in get_tree().get_nodes_in_group("monstros"):
		if is_instance_valid(m) and m.estado != "morto" and m.global_position.distance_to(global_position) < dist:
			dist = m.global_position.distance_to(global_position)
			melhor = m
	return melhor


# ------------------------------------------------------------------ esquiva ------------------------------------------------------------------

func comecar_esquiva() -> void:
	if Jogo.inventario.peso() > Jogo.peso_maximo():
		Sistema.mensagem("Levas peso a mais para esquivar.", "aviso")
		return
	# Passo Fantasma: a 2.ª esquiva seguida é grátis
	var gratis := Jogo.tem_unica("passo_fantasma") and _esquivas_seguidas == 1
	_esquivas_seguidas = 0 if gratis else 1
	if not gratis and not Jogo.gastar_estamina(float(Dados.c("esquiva_custo"))):
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
	Audio.efeito("esquiva")


func _esquivar(delta: float) -> void:
	var v := float(Dados.c("esquiva_distancia")) / float(Dados.c("esquiva_duracao"))
	velocity.x = _esquiva_dir.x * v
	velocity.z = _esquiva_dir.z * v
	_esquiva_t -= delta
	if _esquiva_t <= 0.0:
		mudar_estado("normal")
		get_tree().create_timer(0.8).timeout.connect(func(): _esquivas_seguidas = 0)


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
			_rasto_golpe()
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


## O rasto do golpe (risco branco do corte, onda do golpe pesado, estocada), à frente do herói.
const SOM_GOLPE := {"espada": "corte", "espada_grande": "corte_pesado", "adaga": "estocada", "katana": "katana_iai",
	"machado": "machado", "martelo": "corte_pesado", "lanca": "estocada", "foice": "corte", "manoplas": "soco"}


func _rasto_golpe() -> void:
	Audio.efeito(String(SOM_GOLPE.get(arma.get("tipo", "espada"), "corte")))
	var anim: String = TIPOS.get(arma.get("tipo", "espada"), TIPOS.espada)[0]
	var nome: String = {"ataque_corte": "corte", "ataque_pesado": "corte_pesado", "ataque_estocada": "estocada",
			"ataque_soco": "impacto"}.get(anim, "")
	if nome == "":
		return
	var dir := Vector3(direcao_olhar.x, 0, direcao_olhar.y).normalized()
	var alcance := float(arma.get("alcance", 1.8))
	EfeitosCombate.animado(get_tree(), nome, global_position + dir * alcance * 0.55 + Vector3(0, 0.75, 0.05), 24.0,
			direcao_olhar.x < -0.1)


## Pose da arma ao longo do golpe (p de 0 a 1): prepara, golpe rápido com rasto e acompanha (BonecoArma).
func _pose_arma(p: float) -> void:
	var anim: String = TIPOS.get(arma.get("tipo", "espada"), TIPOS.espada)[0]
	boneco.pose_golpe(anim, p, nome_direcao() == "cima", String(arma.get("tipo", "")))


func _disparar() -> void:
	var nome: String = PROJETIL.get(arma.tipo, "flecha")
	match String(arma.tipo):
		"arco":
			Audio.efeito("arco_disparar")
		"besta":
			Audio.efeito("besta_disparar")
		_:
			var el := String(arma.get("elemento", "luz"))
			Audio.efeito("feitico_" + (el if el in ["fogo", "gelo", "raio", "veneno", "luz", "sombra"] else "luz"))
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
	var est: Array = arma.get("efeitos", []).filter(func(e): return _carregado or not e.get("so_carregado", false))
	if arma.get("tipo", "") == "martelo" and _carregado:
		est = est + [{"estado": "atordoado", "hipotese": 1.0}]
	return golpe_com(alvo, _mult_golpe, arma.get("elemento", "") if arma.get("elemento") else "", est)


## Um golpe do herói contra um alvo (docs/SISTEMAS.md, secção 4), com o multiplicador, elemento e estados dados.
func golpe_com(alvo: Node, mult_golpe: float, elemento: String, lista_estados: Array) -> Dictionary:
	var c := Dados.constantes
	var tipo: String = arma.get("tipo", "")
	var magico: bool = tipo == "cajado"
	var distancia: bool = arma.get("distancia", false)
	var atq: float
	var m_arma := Jogo.mult_arma_equipada()   # melhoria, raridade e qualidade: só na arma (docs/SISTEMAS.md 4.1)
	if magico:
		atq = Formulas.atq_magico(c, float(arma.get("atq_magico", 0)) * m_arma, 0, 1.0, Jogo.a("int"))
	else:
		atq = Formulas.atq_fisico(c, float(arma.get("atq", 0)) * m_arma, 0, 1.0, Jogo.a("for"), Jogo.a("des"), distancia)
	var info: Dictionary = alvo.info_dano() if alvo.has_method("info_dano") else {}
	var mult := mult_golpe * estados.mult("dano_mult") * Jogo.buff("atq") * Jogo.mult_arma(tipo) * Jogo.dif("feito")
	if tipo == "adaga" and alvo is Node3D and _pelas_costas(alvo):
		mult *= float(c.costas_mult)
	var defesa: float = info.get("res", 0.0) if magico else info.get("def", 0.0)
	var g := Dano.calcular(atq, mult, defesa, info, elemento, Jogo.critico(float(arma.get("critico", 0.0))),
			float(c.critico_dano), magico)
	g["empurrao"] = float(c.empurrao_pesado) if tipo in ["espada_grande", "martelo", "machado"] else float(c.empurrao)
	g["estados"] = lista_estados
	g["origem"] = global_position
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
	_sem_combate = 0.0
	if golpe.get("critico", false):
		Colecoes.contar("criticos")
	Jogo.treinar_arma(arma.get("tipo", "espada"))
	# Lâmina Espiritual (Skill Única): a cada 4.º golpe sai uma onda de energia que atravessa inimigos
	if Jogo.tem_unica("lamina_espiritual") and not golpe.get("skill", false):
		_golpes_dados += 1
		if _golpes_dados % int(Dados.c("unica_lamina_cada")) == 0:
			_executar_skill({"forma": "linha", "mult": float(Dados.c("unica_lamina_mult")), "dist": 6.0, "elemento": "luz"})
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
	if Vista2D.atual:
		return Vista2D.atual.rato_no_mundo(global_position.y)
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
	_sem_combate = 0.0
	var valor: int = maxi(1, int(golpe.get("valor", 1) * estados.consumir_golpe_mult() * Jogo.dif("recebido")))
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
	if Jogo.hp <= 0.0 and Jogo.tem_unica("segunda_vida") and not Jogo.segunda_vida_usada:
		Jogo.segunda_vida_usada = true   # uma vez por andar
		Jogo.hp = Jogo.hp_maximo() * float(Dados.c("unica_segunda_vida_hp"))
		Sistema.mensagem("Segunda Vida! Levantas-te outra vez.", "nivel")
		EfeitosCombate.animado(get_tree(), "cura", global_position + Vector3(0, 1, 0))
		invencivel = 2.0
	if Jogo.hp <= 0.0 and Grupo.tentar_renascer():   # Renascer (companheira escondida): uma vez por andar
		EfeitosCombate.animado(get_tree(), "cura", global_position + Vector3(0, 1, 0))
		invencivel = 2.0
	if Jogo.hp <= 0.0 and Arena.atual != null and is_instance_valid(Arena.atual):   # na Arena não se morre
		Arena.atual.perder()
		return
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
	Eventos.jogador_morreu.emit()
	await get_tree().create_timer(1.8).timeout
	var rng := RandomNumberGenerator.new()
	rng.randomize()
	var perdidos := Jogo.perder_materiais_do_andar(rng)
	# ecrã de morte: escurece, lista do que perdeste e "Acordar" (docs/INTERFACE.md, secção 5)
	var ui = get_tree().get_first_node_in_group("morte_ui")
	if ui:
		await ui.mostrar(perdidos)
	if Jogo.dificuldade == "hardcore":   # o jogo acaba
		DirAccess.remove_absolute(ProjectSettings.globalize_path(Gravar.caminho(Jogo.espaco_gravacao)))
		Cenas.mudar("res://cenas/ui/menu_inicial.tscn")
		return
	# acordas na Estalagem, no dia seguinte às 6:00
	Tempo.dormir()
	Jogo.encher()
	Jogo.estados = null
	Jogo.por_flag("acordar_estalagem")
	Cenas.mudar("res://cenas/mundo/cidade.tscn")


# ------------------------------------------------------------------ ajudas ------------------------------------------------------------------

func _regenerar(delta: float) -> void:
	if _espera_estamina > 0.0:
		_espera_estamina -= delta
	else:
		var maximo := float(Jogo.estamina_maxima())
		if Jogo.estamina < maximo:
			Jogo.estamina = min(maximo, Jogo.estamina + float(Dados.c("regen_estamina")) * delta)
	# HP: 1% a cada 5 s fora de combate; Coração de Dragão: 1% por segundo sempre
	var hp_max := float(Jogo.hp_maximo())
	if Jogo.hp > 0.0 and Jogo.hp < hp_max:
		if Jogo.tem_unica("coracao_de_dragao"):
			Jogo.hp = min(hp_max, Jogo.hp + hp_max * float(Dados.c("unica_coracao_regen")) * delta)
		elif _sem_combate >= float(Dados.c("regen_hp_fora_combate")):
			_regen_hp_t += delta
			if _regen_hp_t >= float(Dados.c("regen_hp_intervalo")):
				_regen_hp_t = 0.0
				Jogo.curar(hp_max * float(Dados.c("regen_hp")))
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
