class_name Boss
extends Monstro
## Boss e mini-boss (docs/SISTEMAS.md, secção 7; docs/BOSSES.md): arena fechada, barra de vida grande, fases pelos
## limiares de HP (ataques novos, mais rápido, 1,5 s invencível com uma pequena cena), fúria aos 5 minutos.
## Os ataques vêm de dados/bosses.json; a forma de cada um sai do texto: carga, área, projéteis, chamar, golpe.

var fases: Array = []          # [{limite (0–1), ataques: [...]}]
var fase: int = 0
var arena_centro := Vector3.INF
var arena_raio: float = 15.0
var ativo := false
var _tempo_luta: float = 0.0
var _invencivel: float = 0.0
var _furia := false
var _paredes: StaticBody3D
var _carga_dir := Vector3.ZERO
var _carga_t: float = 0.0
var _atordoado: float = 0.0
var _chamou: Dictionary = {}
var _pausa: float = 0.0        # depois de cada ataque o boss respira um bocado (a janela para lhe bater)


func configurar(id_: String, nivel_: int, tipo_extra: String = "") -> Monstro:
	super.configurar(id_, nivel_, tipo_extra)
	anims = ANIMS.duplicate()
	for i in range(1, 5):
		anims["especial_%d" % i] = [10, false]
	for f in dados.get("fases", []):
		var lim := 1.0
		var m := RegEx.create_from_string("(\\d+)\\s*[–-]").search(String(f.get("vida", "100–0%")))
		if m:
			lim = float(m.get_string(1)) / 100.0
		var ataques := []
		for a in f.get("ataques", []):
			var x: Dictionary = a.duplicate()
			x["forma"] = _forma(String(a.get("texto", "")) + " " + String(a.get("nome_pt", "")))
			ataques.append(x)
		fases.append({"limite": lim, "ataques": ataques})
	return self


static func _forma(t: String) -> String:
	var a := t.to_lower()
	if "chama" in a or "invoca" in a:
		return "chamar"
	if "carga" in a or "corre em linha" in a or "investida" in a:
		return "carga"
	if "projét" in a or "chuva de" in a or "atira" in a or "cospe" in a:
		return "projeteis"
	if "área" in a or "anel" in a or "salta e cai" in a or "pisão" in a or "onda" in a or "grito" in a or "à volta" in a:
		return "area"
	return "golpe"


func _ready() -> void:
	super._ready()
	add_to_group("bosses")
	if arena_centro == Vector3.INF:
		arena_centro = global_position
	arena_raio = float(Dados.c("boss_arena_raio", 15.0))


func _physics_process(delta: float) -> void:
	_invencivel = maxf(0.0, _invencivel - delta)
	_pausa = maxf(0.0, _pausa - delta)
	if estado == "morto":
		super._physics_process(delta)
		return
	if not ativo:
		var j := get_tree().get_first_node_in_group("jogador")
		if j and j.global_position.distance_to(arena_centro) < arena_raio - 2.0:
			_comecar_luta()
		else:
			velocity = Vector3.ZERO
			_anim("parado")
			move_and_slide()
			return
	_tempo_luta += delta
	if not _furia and _tempo_luta > float(Dados.c("boss_furia_segundos", 300)):
		_furia = true
		vel *= float(Dados.c("boss_furia_mult", 1.3))
		Sistema.mensagem("%s está furios%s!" % [dados.get("nome_pt", id), "o"], "aviso")
	if _atordoado > 0.0:
		_atordoado -= delta
		velocity.x = 0.0
		velocity.z = 0.0
		move_and_slide()
		return
	if estado == "carga":
		_carregar(delta)
		return
	super._physics_process(delta)


func _comecar_luta() -> void:
	ativo = true
	_mudar("perseguir")
	_fechar_arena()
	Eventos.boss_comecou.emit(self)
	var cam := get_viewport().get_camera_3d()
	if cam is Camara:   # bosses grandes: a câmara afasta-se para se ver o boss inteiro
		cam.distancia = maxf(cam.distancia, 12.0 + _tamanho_px / 8.0)
	Audio.tocar_musica(String(id))
	Sistema.mensagem("%s — %s" % [dados.get("nome_pt", id), dados.get("epiteto", "")], "aviso")


## A arena fecha: um anel de paredes invisíveis (sai-se a ganhar ou a morrer).
func _fechar_arena() -> void:
	_paredes = StaticBody3D.new()
	_paredes.collision_layer = 1
	get_parent().add_child(_paredes)
	for i in 24:
		var a := i * TAU / 24.0
		var f := CollisionShape3D.new()
		var b := BoxShape3D.new()
		b.size = Vector3(arena_raio * TAU / 24.0 + 0.5, 6, 1.0)
		f.shape = b
		f.position = arena_centro + Vector3(cos(a) * arena_raio, 3, sin(a) * arena_raio)
		f.rotation.y = -a + PI / 2
		_paredes.add_child(f)


func _escolher_ataque() -> Dictionary:
	if _pausa > 0.0:
		return {}
	var lista: Array = fases[fase].ataques if fase < fases.size() else dados.get("ataques", [ATAQUE_PADRAO])
	var possiveis := []
	for a in lista:
		if _recargas.get(a.id, 0.0) > 0.0:
			continue
		if a.get("forma", "") == "chamar" and _chamou.get(a.id, false) and "uma vez" in String(a.get("texto", "")):
			continue
		possiveis.append(a)
	if possiveis.is_empty():
		return {}
	var a: Dictionary = possiveis[randi() % possiveis.size()].duplicate()
	match a.get("forma", "golpe"):   # os bosses atacam de mais longe que os monstros
		"carga":
			a.alcance = 10.0
		"projeteis", "chamar":
			a.alcance = 14.0
		"area":
			a.alcance = float(Dados.c("boss_area_raio", 4.5)) + 0.5
		_:
			a.alcance = maxf(float(a.get("alcance", 1.6)), _tamanho_px / 32.0 + 1.0)
	a.recarga = maxf(float(a.get("recarga", 1.5)), 2.5)
	return a


func _comecar_aviso(d: Vector3) -> void:
	var forma: String = _ataque.get("forma", "golpe")
	if forma == "golpe":
		super._comecar_aviso(d)
		return
	olhar_x = sign(d.x) if abs(d.x) > 0.05 else olhar_x
	_mira.rotation.y = atan2(-d.x, -d.z)
	var plano := _marca.mesh as PlaneMesh
	match forma:
		"carga":
			var comp := float(Dados.c("boss_carga_distancia", 9.0))
			plano.size = Vector2(_tamanho_px / 32.0 + 0.6, comp)
			_marca.position = Vector3(0, 0.03, -comp / 2.0)
		"area":
			var r := float(Dados.c("boss_area_raio", 4.5))
			plano.size = Vector2(r * 2, r * 2)
			_marca.position = Vector3(0, 0.03, 0)
		_:
			plano.size = Vector2(0.01, 0.01)
	_marca.visible = forma in ["carga", "area"]
	_mudar("aviso")
	var i := clampi(fases[fase].ataques.find(_ataque) + 1 if fase < fases.size() else 1, 1, 4)
	sprite.play("especial_%d_lado" % i if sprite.sprite_frames.has_animation("especial_%d_lado" % i) else "atacar_lado")
	sprite.speed_scale = 0.4


func _golpear() -> void:
	var forma: String = _ataque.get("forma", "golpe")
	_recargas[_ataque.id] = float(_ataque.get("recarga", 2.5))
	_marca.visible = false
	sprite.speed_scale = 1.4
	match forma:
		"golpe":
			super._golpear()
			return
		"carga":
			_carga_dir = (_mira.global_transform.basis * Vector3.FORWARD).normalized()
			_carga_t = float(Dados.c("boss_carga_tempo", 0.55))
			for f in hitbox.get_children():
				f.queue_free()
			hitbox.add_child(Hitbox.caixa(_tamanho_px / 32.0 + 0.6, _tamanho_px / 32.0 + 0.8))
			hitbox.ligar()
			_mudar("carga")
			return
		"area":
			var r := float(Dados.c("boss_area_raio", 4.5))
			var j := get_tree().get_first_node_in_group("jogador")
			if j and j.global_position.distance_to(global_position) < r:
				j.receber_golpe(_golpe_para(j))
			for k in 8:
				var a := TAU * k / 8.0
				EfeitosCombate.animado(get_tree(), "poeira", global_position + Vector3(cos(a) * r * 0.8, 0.3, sin(a) * r * 0.8))
			var cam := get_viewport().get_camera_3d()
			if cam and cam.has_method("tremer"):
				cam.tremer(0.25, 0.3)
		"projeteis":
			var j := get_tree().get_first_node_in_group("jogador")
			var n := int(Dados.c("boss_projeteis", 5))
			for k in n:
				var p := Projetil.new()
				p.textura = "res://arte/efeitos/projetil_pedra.png"
				p.dono = self
				p.mascara = 1 << 1
				p.alcance = 18.0
				p.velocidade = 10.0
				var alvo: Vector3 = j.global_position if j else global_position + Vector3.FORWARD
				var dir := (alvo - global_position)
				dir.y = 0.0
				p.direcao = dir.normalized().rotated(Vector3.UP, (k - (n - 1) / 2.0) * 0.22)
				p.calcular_golpe = func(alvo_n): return _golpe_para(alvo_n)
				get_parent().add_child(p)
				p.global_position = global_position + Vector3(0, 1.2, 0) + p.direcao * 1.5
		"chamar":
			_chamou[_ataque.id] = true
			_chamar(String(_ataque.get("texto", "")))
	_mudar("atacar")


func _golpe_para(alvo: Node) -> Dictionary:
	var info: Dictionary = alvo.info_dano() if alvo.has_method("info_dano") else {}
	var g := Dano.calcular(atq * estados.mult("dano_mult"), float(_ataque.get("mult", 1.2)), info.get("def", 0.0), info, _elemento_ataque(), 0.05, 1.5)
	g["empurrao"] = 1.5
	g["origem"] = global_position
	g["estados"] = _ataque.get("estados", [])
	return g


## Carga: corre a direito; se bater numa árvore ou parede fica atordoado (o momento de atacar).
func _carregar(delta: float) -> void:
	_carga_t -= delta
	var v := float(Dados.c("boss_carga_distancia", 9.0)) / float(Dados.c("boss_carga_tempo", 0.55))
	velocity.x = _carga_dir.x * v
	velocity.z = _carga_dir.z * v
	move_and_slide()
	if is_on_wall():
		hitbox.desligar()
		_atordoado = float(Dados.c("boss_atordoado_arvore", 3.0))
		estados.aplicar("atordoado", _atordoado)
		Sistema.mensagem("%s bateu e ficou atordoado!" % dados.get("nome_pt", id))
		var cam := get_viewport().get_camera_3d()
		if cam and cam.has_method("tremer"):
			cam.tremer(0.3, 0.3)
		_fim_ataque()
	elif _carga_t <= 0.0:
		_fim_ataque()


## "Chamar Javalis: 2 javalis normais" -> 2 monstros desse tipo à volta do boss.
func _chamar(texto: String) -> void:
	var n := 2
	var m := RegEx.create_from_string("(\\d+)\\s+(.+?)(?:\\s+normais)?(?:\\s*\\(|$)").search(texto)
	var quem := ""
	if m:
		n = int(m.get_string(1))
		var nome := m.get_string(2).strip_edges().to_lower()
		for mo in Dados.tabela("monstros").values():
			var nm: String = String(mo.nome_pt).to_lower()
			if nome.begins_with(nm.substr(0, maxi(4, nm.length() - 2))) or nm.begins_with(nome.substr(0, maxi(4, nome.length() - 2))):
				quem = mo.id
				break
	if quem == "":
		return
	for k in n:
		var mo: Monstro = Monstro.new().configurar(quem, maxi(1, nivel - 3))
		get_parent().add_child(mo)
		mo.global_position = global_position + Vector3(cos(k * 2.0) * 3.0, 0.3, sin(k * 2.0) * 3.0)
		EfeitosCombate.animado(get_tree(), "poeira", mo.global_position + Vector3(0, 0.4, 0))


func _fim_ataque() -> void:
	super._fim_ataque()
	_pausa = float(Dados.c("boss_pausa_ataques", 1.8))


func _mudar(novo: String) -> void:
	if estado == "carga" and novo != "carga":
		hitbox.desligar()
	super._mudar(novo)


func receber_golpe(golpe: Dictionary) -> void:
	if _invencivel > 0.0 or not ativo or estado == "morto":
		if not ativo and estado != "morto":
			_comecar_luta()
		else:
			return
	if _atordoado > 0.0:
		golpe = golpe.duplicate()
		golpe.valor = int(golpe.get("valor", 0) * float(Dados.c("atordoado_mult", 1.2)))
	var antes := hp
	super.receber_golpe(golpe)
	_ver_fase(antes)


## Mudar de fase ao passar o limiar de HP: 1,5 s invencível, um pouco mais rápido, ataques novos.
func _ver_fase(_antes: float) -> void:
	if estado == "morto":
		return
	var pct := hp / hp_max
	while fase + 1 < fases.size() and pct <= float(fases[fase + 1].limite):
		fase += 1
		_invencivel = float(Dados.c("boss_fase_invencivel", 1.5))
		vel *= 1.0 + float(Dados.c("boss_fase_vel", 0.1))
		_recargas.clear()
		_mudar("dano")
		if sprite.sprite_frames.has_animation("mudar_fase_lado"):   # a pose de fúria desenhada
			sprite.play("mudar_fase_lado")
		EfeitosCombate.piscar(sprite, 0.25)
		EfeitosCombate.hitstop(get_tree(), 0.12)
		EfeitosCombate.animado(get_tree(), "explosao_fisico", global_position + Vector3(0, _tamanho_px / 32.0, 0))
		EfeitosCombate.animado(get_tree(), "explosao_luz", global_position + Vector3(0, _tamanho_px / 20.0, 0.4))
		var cam := get_viewport().get_camera_3d()
		if cam and cam.has_method("tremer"):
			cam.tremer(0.4, 0.6)
		Sistema.mensagem("%s — fase %d!" % [dados.get("nome_pt", id), fase + 1], "aviso")


func morrer() -> void:
	super.morrer()
	# o fim de um boss: o ecrã treme e o corpo rebenta aos bocados antes de se desfazer
	EfeitosCombate.hitstop(get_tree(), 0.2)
	var cam := get_viewport().get_camera_3d()
	if cam and cam.has_method("tremer"):
		cam.tremer(0.5, 1.0)
	var metros := _tamanho_px / 16.0
	for i in 5:
		get_tree().create_timer(0.12 + i * 0.16).timeout.connect(func():
			if is_inside_tree():
				EfeitosCombate.animado(get_tree(), ["explosao_fisico", "explosao_luz", "explosao_fogo"][i % 3],
						global_position + Vector3(randf_range(-0.4, 0.4) * metros, randf_range(0.2, 0.8) * metros, 0.4)))
	if _paredes:
		_paredes.queue_free()
	Eventos.boss_acabou.emit(self)
	_recompensas()


## 1.ª vez: arma única garantida, troféu, título, muita XP e ouro, materiais (docs/SISTEMAS.md, secção 7).
func _recompensas() -> void:
	var primeira := not Jogo.tem_flag("boss_recompensa_" + id)
	if not primeira:
		return
	Jogo.por_flag("boss_recompensa_" + id)
	var c := Dados.constantes
	Jogo.ganhar_xp(Formulas.xp_monstro(c, nivel, float(c.tipos_monstro.get(tipo, c.tipos_monstro.normal).xp)) * 2)
	Jogo.ganhar_ouro(Formulas.monstro_ouro(nivel, RandomNumberGenerator.new()) * int(c.get("boss_ouro_mult", 8)), true)
	var arma_txt: String = String(dados.get("arma_unica", "")).split("(")[0].strip_edges()
	for a in Dados.tabela("armas").values():
		if arma_txt != "" and String(a.nome_pt) == arma_txt:
			Jogo.apanhar(a.id, 1, {"raridade": "lendario"})
	var trofeu: String = String(dados.get("trofeu", "")).split("(")[0].strip_edges()
	for it in Dados.tabela("itens").values():
		if trofeu != "" and String(it.nome_pt) == trofeu:
			Jogo.apanhar(it.id, 1)
	if dados.get("titulo", "") != "":
		Jogo.por_flag("titulo_" + String(dados.titulo).to_snake_case())
		Sistema.mensagem("Título novo: %s" % dados.titulo, "nivel")
	if tipo == "boss":   # boss de região: Dia da Subida em Ascendia
		Jogo.por_flag("dia_da_subida_pendente")
		Sistema.mensagem("Em Ascendia vão festejar o Dia da Subida!", "nivel")
