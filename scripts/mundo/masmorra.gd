class_name Masmorra
extends Node3D
## As masmorras escondidas (docs/regioes/rNN, secção 9; dados/masmorras.json): 3 salas e a sala do boss extra, em
## fila, construídas longe (como a Arena). Cada sala fecha o portão do fundo até ser resolvida:
##   combate     — vencer os monstros da região que aparecem quando entras;
##   armadilhas  — atravessar as armadilhas (círculos vermelhos que avisam e depois ferem) e puxar a alavanca do fundo;
##   puzzle      — rodar as peças até ficarem como diz a placa da entrada;
##   ritmo       — dançar com os fantasmas (o jogo de ritmo) sem tirar nota C.
## No fim: o boss, a arma secreta (Lendária), um baú de ouro e a página de lore extra (só da primeira vez).

const ORIGEM := Vector3(0, -1000, 0)
const LARGURA := 22.0
const FUNDO := 18.0
const CORREDOR := 6.0
const ALTURA := 4.0
const BAIXA := 0.8                 # as paredes do lado da câmara

static var atual: Masmorra

var d: Dictionary = {}
var porta_fora := Vector3.ZERO
var _portoes: Array = []           # [{malha, colisao}] (o portão do fundo de cada sala)
var _resolvida: Array = [false, false, false, false]
var _entrou: Array = [false, false, false, false]
var _vivos: Array = [0, 0, 0, 0]
var _armadilhas: Array = []        # [{p, fase}]
var _rng := RandomNumberGenerator.new()
var _mat_chao: StandardMaterial3D
var _mat_parede: StandardMaterial3D
var _corpo: StaticBody3D
var _t: float = 0.0


## Entrar na masmorra da região (do andar, pela entrada que o segredo abriu).
static func entrar(mundo: Node, regiao: int, porta: Vector3) -> void:
	if atual != null and is_instance_valid(atual):
		return
	var dados: Dictionary = Dados.tabela("masmorras").get("masmorras", {}).get(str(regiao), {})
	if dados.is_empty():
		return
	var m := Masmorra.new()
	m.d = dados
	m.porta_fora = porta
	m.position = ORIGEM   # antes de entrar na árvore: o _ready constrói tudo já no sítio
	mundo.add_child(m)
	atual = m
	Jogo.dentro = true
	var j := mundo.get_tree().get_first_node_in_group("jogador") as Node3D
	if j:
		j.global_position = ORIGEM + m.centro(0) + Vector3(0, 0.5, FUNDO / 2.0 - 2.0)
		if "velocity" in j:
			j.velocity = Vector3.ZERO
	var cam := mundo.get_viewport().get_camera_3d()
	if cam and cam.has_method("saltar"):
		cam.saltar()
	Sistema.mensagem("Masmorra escondida: %s" % dados.nome_pt, "andar")


func ja_vencida() -> bool:
	return Jogo.tem_flag("masmorra_" + String(d.get("id", "")))


## Centro (local) da sala i (0 a 3): as salas vão para o fundo (-Z), com corredores entre elas.
func centro(i: int) -> Vector3:
	return Vector3(0, 0, -i * (FUNDO + CORREDOR))


func _exit_tree() -> void:
	if atual == self:
		atual = null
		Jogo.dentro = false


func _ready() -> void:
	_rng.randomize()
	var regiao := int(d.get("regiao", 1))
	var nat: Dictionary = Dados.tabela("natureza").get(str(regiao), {}).get("chao", {})
	_mat_chao = _material(nat.get("terra", nat.get("base", "")), Color.WHITE)
	_mat_parede = _material("res://arte/interiores/parede_pedra.png", Color(0.75, 0.7, 0.8))
	_corpo = StaticBody3D.new()
	add_child(_corpo)
	var escuro := StandardMaterial3D.new()
	escuro.albedo_color = Color("2e222f")
	escuro.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	_caixa(Vector3(0, -0.5, -40), Vector3(140, 0.2, 180), escuro, false)
	for i in 4:
		_sala(i)
	if ja_vencida():
		for i in 4:
			_resolvida[i] = true
			_abrir(i, false)
	_saida(centro(0) + Vector3(0, 0, FUNDO / 2.0 - 1.0), "Sair da masmorra")


func _material(caminho: String, cor: Color) -> StandardMaterial3D:
	var m := StandardMaterial3D.new()
	if caminho != "" and ResourceLoader.exists(caminho):
		m.albedo_texture = load(caminho)
	m.albedo_color = cor
	m.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
	m.uv1_triplanar = true
	m.uv1_world_triplanar = true
	m.uv1_scale = Vector3(0.5, 0.5, 0.5)   # 32 px = 2 m (16 px por metro)
	return m


## Colisão sem desenho (por cima das paredes baixas); com "buraco" de largura porta no meio (0 = sem buraco).
func _colisao_invisivel(p: Vector3, tam: Vector3, porta: float) -> void:
	var partes := [[p, tam]] if porta <= 0.0 else [[p + Vector3(-(tam.x + porta) / 4.0, 0, 0), Vector3((tam.x - porta) / 2.0, tam.y, tam.z)],
			[p + Vector3((tam.x + porta) / 4.0, 0, 0), Vector3((tam.x - porta) / 2.0, tam.y, tam.z)]]
	for pt in partes:
		var c := CollisionShape3D.new()
		var s := BoxShape3D.new()
		s.size = pt[1]
		c.shape = s
		c.position = pt[0]
		_corpo.add_child(c)


func _caixa(p: Vector3, tam: Vector3, mat: Material, colide := true) -> MeshInstance3D:
	var mi := MeshInstance3D.new()
	var b := BoxMesh.new()
	b.size = tam
	mi.mesh = b
	mi.material_override = mat
	mi.position = p
	add_child(mi)
	if colide:
		var c := CollisionShape3D.new()
		var s := BoxShape3D.new()
		s.size = tam
		c.shape = s
		c.position = p
		_corpo.add_child(c)
		mi.set_meta("colisao", c)
	return mi


## Uma sala: chão, paredes (com uma abertura a sul e outra a norte), tochas, o portão do fundo e o que lá vive.
func _sala(i: int) -> void:
	var c := centro(i)
	var porta := 3.0
	_caixa(c + Vector3(0, -0.1, 0), Vector3(LARGURA, 0.2, FUNDO), _mat_chao)
	var lado := (LARGURA - porta) / 2.0
	# a parede de norte é alta; a de sul (do lado da câmara) é baixinha, para se ver lá dentro (como nas casas)
	for z in [-FUNDO / 2.0, FUNDO / 2.0]:
		var h := ALTURA if z < 0.0 else BAIXA
		_caixa(c + Vector3(-LARGURA / 2.0 + lado / 2.0, h / 2.0, z), Vector3(lado, h, 0.6), _mat_parede)
		_caixa(c + Vector3(LARGURA / 2.0 - lado / 2.0, h / 2.0, z), Vector3(lado, h, 0.6), _mat_parede)
		if z > 0.0:   # (por cima da parede baixa não se passa: colisão invisível)
			_colisao_invisivel(c + Vector3(0, ALTURA / 2.0, z), Vector3(LARGURA, ALTURA, 0.6), porta)
	for x in [-LARGURA / 2.0, LARGURA / 2.0]:
		_caixa(c + Vector3(x, ALTURA / 2.0, 0), Vector3(0.6, ALTURA, FUNDO), _mat_parede)
	if i == 0:   # a entrada: fechada atrás de ti (sai-se pela porta da saída)
		_caixa(c + Vector3(0, BAIXA / 2.0, FUNDO / 2.0 + 0.4), Vector3(porta, BAIXA, 0.6), _mat_parede)
		_colisao_invisivel(c + Vector3(0, ALTURA / 2.0, FUNDO / 2.0 + 0.4), Vector3(porta, ALTURA, 0.6), 0.0)
	if i < 3:   # o corredor até à sala seguinte (paredes baixas), e o portão
		var cz := c.z - FUNDO / 2.0 - CORREDOR / 2.0
		_caixa(Vector3(0, -0.1, cz), Vector3(porta + 0.6, 0.2, CORREDOR), _mat_chao)
		for x in [-porta / 2.0 - 0.3, porta / 2.0 + 0.3]:
			_caixa(Vector3(x, BAIXA / 2.0, cz), Vector3(0.6, BAIXA, CORREDOR), _mat_parede)
			_colisao_invisivel(Vector3(x, ALTURA / 2.0, cz), Vector3(0.6, ALTURA, CORREDOR), 0.0)
		var g := _caixa(c + Vector3(0, ALTURA / 2.0, -FUNDO / 2.0), Vector3(porta, ALTURA, 0.4), _material("res://arte/interiores/parede_madeira.png", Color(0.8, 0.6, 0.5)))
		_portoes.append(g)
	else:
		_caixa(c + Vector3(0, ALTURA / 2.0, -FUNDO / 2.0), Vector3(porta, ALTURA, 0.6), _mat_parede)
	for k in 4:   # tochas nas paredes
		var l := OmniLight3D.new()
		l.light_color = Color("f79617")
		l.light_energy = 1.4
		l.omni_range = 11.0
		l.position = c + Vector3((-1 if k < 2 else 1) * (LARGURA / 2.0 - 1.0), 2.6, (-1 if k % 2 == 0 else 1) * FUNDO / 4.0)
		add_child(l)
	var placa := Label3D.new()
	placa.text = String(d.salas[i].nome_pt) if i < 3 else String(Dados.tabela("masmorras").get("bosses", {}).get(d.boss, {}).get("nome_pt", "Boss"))
	placa.font_size = 32
	placa.pixel_size = 0.01
	placa.outline_size = 10
	placa.modulate = Color("fbff86")
	placa.billboard = BaseMaterial3D.BILLBOARD_ENABLED
	placa.position = c + Vector3(-LARGURA / 4.0, 2.8, FUNDO / 2.0 - 1.2)
	add_child(placa)
	_enfeitar(i)
	if i < 3 and not ja_vencida():
		match String(d.salas[i].tipo):
			"armadilhas":
				_sala_armadilhas(i)
			"puzzle":
				_sala_puzzle(i)
			"ritmo":
				_sala_ritmo(i)
			_:
				pass   # combate: os monstros aparecem quando entras (_process)


## Enfeites da região: colunas nos cantos e coisas pelo chão encostadas às paredes (sem tapar o meio da sala).
func _enfeitar(i: int) -> void:
	var c := centro(i)
	var plantas: Dictionary = Dados.tabela("natureza").get(str(int(d.get("regiao", 1))), {}).get("plantas", {})
	var colunas: Array = Array(plantas.get("objetos", [])).filter(func(x): return "pilar" in x or "menir" in x or "estalag" in x)
	var soltos: Array = Array(plantas.get("detalhes", [])) + Array(plantas.get("pedras", []))
	for cx in [-1, 1]:
		for cz in [-1, 1]:
			var p := c + Vector3(cx * (LARGURA / 2.0 - 1.6), 0, cz * (FUNDO / 2.0 - 1.8))
			if not colunas.is_empty():
				_sprite(colunas[(i + cx + cz + 4) % colunas.size()], p, 1.3)
				_colisao_invisivel(p + Vector3(0, 1.5, 0), Vector3(0.9, 3.0, 0.9), 0.0)
	for k in 8:
		if soltos.is_empty():
			break
		var lado := -1.0 if k % 2 == 0 else 1.0
		var p := c + Vector3(lado * _rng.randf_range(LARGURA / 2.0 - 3.5, LARGURA / 2.0 - 1.2), 0, _rng.randf_range(-FUNDO / 2.0 + 2.0, FUNDO / 2.0 - 2.5))
		_sprite(soltos[_rng.randi() % soltos.size()], p, 1.0)


func _sprite(caminho: String, p: Vector3, escala: float) -> void:
	if not ResourceLoader.exists(caminho):
		return
	var s := Sprite3D.new()
	s.texture = load(caminho)
	s.pixel_size = escala / Natureza.PPM
	s.billboard = BaseMaterial3D.BILLBOARD_FIXED_Y
	s.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
	s.alpha_cut = SpriteBase3D.ALPHA_CUT_DISCARD
	s.offset.y = s.texture.get_height() / 2.0
	s.position = p
	add_child(s)


func _usar(p: Vector3, texto: String, cb: Callable) -> Interagivel:
	var it := Interagivel.new()
	it.texto = texto
	it.position = p
	add_child(it)
	it.usado.connect(func(_j): cb.call())
	return it


func _saida(p: Vector3, texto: String) -> void:
	_usar(p, texto, func(): sair())


func sair() -> void:
	var j := get_tree().get_first_node_in_group("jogador") as Node3D
	if j:
		j.global_position = porta_fora + Vector3(0, 0.5, 0)
		if "velocity" in j:
			j.velocity = Vector3.ZERO
	var cam := get_viewport().get_camera_3d()
	if cam and cam.has_method("saltar"):
		cam.saltar()
	queue_free()


## Abre o portão do fundo da sala i.
func _abrir(i: int, avisar := true) -> void:
	_resolvida[i] = true
	if i < _portoes.size():
		var g: MeshInstance3D = _portoes[i]
		if is_instance_valid(g):
			var col: CollisionShape3D = g.get_meta("colisao")
			col.set_deferred("disabled", true)
			create_tween().tween_property(g, "position:y", g.position.y + ALTURA, 1.2)
	if avisar:
		Sistema.mensagem("O portão abre-se com um rangido.", "nivel")
		Audio.efeito("porta")


# ------------------------------------------------------------------ tipos de sala ------------------------------------------------------------------

func _sala_armadilhas(i: int) -> void:
	var c := centro(i)
	for k in 10:
		var p := c + Vector3(_rng.randf_range(-LARGURA / 2.0 + 2.0, LARGURA / 2.0 - 2.0), 0, _rng.randf_range(-FUNDO / 2.0 + 2.5, FUNDO / 2.0 - 3.0))
		var disco := MeshInstance3D.new()
		var cil := CylinderMesh.new()
		cil.top_radius = 1.4
		cil.bottom_radius = 1.4
		cil.height = 0.04
		disco.mesh = cil
		var m := StandardMaterial3D.new()
		m.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
		m.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
		m.albedo_color = Color(0.92, 0.31, 0.21, 0.0)
		disco.material_override = m
		disco.position = p + Vector3(0, 0.03, 0)
		add_child(disco)
		_armadilhas.append({"p": p, "fase": _rng.randf() * 2.4, "m": m, "feriu": false})
	var alavanca := c + Vector3(0, 0, -FUNDO / 2.0 + 1.5)
	_usar(alavanca, "Puxar a alavanca do portão", func():
		if not _resolvida[i]:
			_abrir(i))


func _sala_puzzle(i: int) -> void:
	var c := centro(i)
	var n := 3 + i % 2
	var certa := []
	var estado := []
	var setas := ["↑", "→", "↓", "←"]
	for k in n:
		certa.append(_rng.randi() % 4)
		estado.append(0)
	var dica := ""
	for k in n:
		dica += setas[certa[k]] + " "
	var placa := Label3D.new()
	placa.text = "« %s»" % dica
	placa.font_size = 40
	placa.pixel_size = 0.01
	placa.outline_size = 10
	placa.billboard = BaseMaterial3D.BILLBOARD_ENABLED
	placa.position = c + Vector3(0, 2.6, FUNDO / 2.0 - 1.5)
	add_child(placa)
	for k in n:
		var p := c + Vector3((k - (n - 1) / 2.0) * 4.0, 0, -1.0)
		var peca := _caixa(p + Vector3(0, 0.8, 0), Vector3(1.0, 1.6, 1.0), _mat_parede)
		var seta := Label3D.new()
		seta.text = setas[0]
		seta.font_size = 64
		seta.pixel_size = 0.01
		seta.outline_size = 10
		seta.modulate = Color("8fd3ff")
		seta.billboard = BaseMaterial3D.BILLBOARD_ENABLED
		seta.position = p + Vector3(0, 2.2, 0)
		add_child(seta)
		var kk := k
		_usar(p + Vector3(0, 0, 1.0), "Rodar a peça %d" % (k + 1), func():
			if _resolvida[i]:
				return
			estado[kk] = (estado[kk] + 1) % 4
			seta.text = setas[estado[kk]]
			create_tween().tween_property(peca, "rotation:y", peca.rotation.y + PI / 2.0, 0.3)
			if estado == certa:
				Colecoes.contar("puzzles")
				_abrir(i))


func _sala_ritmo(i: int) -> void:
	var c := centro(i)
	_usar(c + Vector3(0, 0, 2.0), "Dançar com os fantasmas", func():
		if _resolvida[i]:
			return
		var r = get_tree().get_first_node_in_group("ritmo_ui")
		if r == null:
			_abrir(i)
			return
		r.dancar("")
		var nota: String = await r.acabou
		if nota != "C":
			_abrir(i)
		else:
			Jogo.hp = maxf(1.0, Jogo.hp - Jogo.hp_maximo() * 0.15)
			Sistema.mensagem("Pisaste os pés aos fantasmas e eles não gostaram. Tenta outra vez!", "aviso"))


## Monstros da região (combate) e o boss (última sala).
func _encher(i: int) -> void:
	var regiao := int(d.get("regiao", 1))
	var nivel := int(d.get("andar", 1)) + 3
	var c := centro(i)
	if i == 3:
		if ja_vencida():
			Sistema.mensagem("A sala do boss está em silêncio. Já venceste aqui.")
			return
		var b := Boss.new().configurar(String(d.boss), nivel + 3, "boss")
		b.position = c + Vector3(0, 0.5, -3.0)
		b.arena_centro = global_position + c
		add_child(b)
		b.morreu.connect(func(_m): _vitoria())
		return
	var pool := []
	for m in Dados.tabela("monstros").values():
		if int(m.get("regiao", 0)) == regiao and m.get("tipo", "") in ["normal", "tanque", "rapido", "mago", "fraco"]:
			pool.append(m.id)
	if pool.is_empty():
		_abrir(i)
		return
	var n := 4 + regiao / 2
	_vivos[i] = n
	for k in n:
		var m := Monstro.new().configurar(pool[_rng.randi() % pool.size()], nivel)
		m.position = c + Vector3(_rng.randf_range(-7, 7), 0.5, _rng.randf_range(-6, 2))
		add_child(m)
		m.morreu.connect(func(_m):
			_vivos[i] -= 1
			if _vivos[i] <= 0 and not _resolvida[i]:
				_abrir(i))
	Sistema.mensagem("%s: os monstros acordam!" % d.salas[i].nome_pt, "aviso")


func _vitoria() -> void:
	if ja_vencida():
		return
	Jogo.por_flag("masmorra_" + String(d.id))
	Colecoes.contar("masmorras")
	var arma := String(d.get("arma", ""))
	if arma != "":
		Jogo.inventario.adicionar(arma, 1, {"raridade": "lendario"})
		Sistema.mensagem("Arma secreta: %s (Lendária)!" % d.get("arma_pt", arma), "nivel")
	var bau := Bau.new()
	bau.tipo = "ouro"
	bau.andar = int(d.get("andar", 1))
	bau.regiao = int(d.get("regiao", 1))
	bau.position = centro(3) + Vector3(2.0, 0, 0)
	add_child(bau)
	Jogo.inventario.adicionar("chave_bau_ouro")
	if String(d.get("lore_pt", "")) != "":
		Colecoes.contar("paginas_extra")
		Sistema.mensagem("Página de lore extra: «%s»" % d.lore_pt, "nivel")
	Sistema.mensagem("VENCESTE A MASMORRA: %s!" % String(d.nome_pt).to_upper(), "nivel")
	_saida(centro(3) + Vector3(-2.0, 0, 2.0), "Voltar à torre")


func _process(delta: float) -> void:
	_t += delta
	var j := get_tree().get_first_node_in_group("jogador") as Node3D
	if j == null:
		return
	var local := j.global_position - global_position
	if local.length() > 400.0:   # o herói saiu por outro lado (morreu, Pedra de Regresso)
		queue_free()
		return
	for i in 4:   # entrar numa sala: acorda o que lá está
		var c := centro(i)
		if not _entrou[i] and absf(local.z - c.z) < FUNDO / 2.0 - 1.0 and absf(local.x) < LARGURA / 2.0:
			_entrou[i] = true
			if i == 3 or (String(d.salas[i].tipo) == "combate" and not _resolvida[i]):
				_encher(i)
	for a in _armadilhas:   # armadilhas: avisam 0,8 s (vermelho a aparecer) e ferem 0,4 s
		var f := fmod(_t + float(a.fase), 2.4)
		var m: StandardMaterial3D = a.m
		if f < 1.2:
			m.albedo_color.a = 0.0
			a.feriu = false
		elif f < 2.0:
			m.albedo_color = Color(0.92, 0.31, 0.21, 0.15 + (f - 1.2) * 0.4)
		else:
			m.albedo_color = Color(1.0, 0.5, 0.25, 0.85)
			if not a.feriu and Vector2(local.x - a.p.x, local.z - a.p.z).length() < 1.4:
				a.feriu = true
				Jogo.hp = maxf(0.0, Jogo.hp - Jogo.hp_maximo() * 0.1)
				Eventos.jogador_dano.emit(int(Jogo.hp_maximo() * 0.1))
				if Jogo.hp <= 0.0 and j.has_method("morrer"):
					j.morrer()
