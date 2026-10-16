extends Node3D
## Ascendia (docs/CIDADES.md e docs/mapas/ascendia.md): montada a partir de dados/cidade.json.
## Chão por células de 10 m, muralha, rio, edifícios (com colisão), árvores, candeeiros, NPCs com rotinas,
## o Cristal Mestre (entrada da torre) e o quadro de avisos.

const CEL := 10.0
const POR_CEL := 5          # 5 ladrilhos de 2 m por célula
const ARTE := "res://arte/cidade/"
const CHAO_PEDRA := ["::", "][", "Fn", "Cr", "▓▓", "Qa"]
const CHAO_TERRA := ["..", "Pa", "Eb", "Tr", "Me", "Ar", "Ca", "Pi", "Mi"]
const ESCALA := {"guilda": 1.4, "base_torre": 1.0, "arena": 1.0, "estalagem": 1.3, "camara_governador": 1.3, "igreja": 1.3, "biblioteca": 1.2}

var dados: Dictionary = {}
var largura: int = 0
var altura: int = 0
var jogador: Node3D
var camara: Camara
var ponto_chegada := Vector3.ZERO
var npcs: Dictionary = {}           # id -> NPC
var locais: Dictionary = {}         # código do edifício -> ponto à porta
var _pecas := Pecas.new()
var _corpo: StaticBody3D
var _rng := RandomNumberGenerator.new()


func _ready() -> void:
	dados = Dados.tabela("cidade")
	largura = int(dados.largura)
	altura = int(dados.altura)
	Jogo.andar_atual = 0
	_rng.seed = 1977
	Ambiente.criar(self, Color("7fa0c8"), Color("c8e0d0"), 0.006, 0.7, 0, false)
	_corpo = StaticBody3D.new()
	add_child(_corpo)
	var chao := CollisionShape3D.new()
	var b := BoxShape3D.new()
	b.size = Vector3(largura * CEL, 1.0, altura * CEL)
	chao.shape = b
	chao.position.y = -0.5
	_corpo.add_child(chao)
	_construir_chao()
	_construir_edificios()
	_criar_jogador()
	_criar_npcs()
	_pecas.criar(self)
	var vida := Vida.new()
	vida.mundo = self
	vida.regiao = 1
	add_child(vida)
	_gente_na_rua()
	Tempo.nova_hora.connect(func(_h): _rotinas(false))
	Audio.tocar_musica("ascendia_dia")
	Sistema.mensagem("Ascendia — %s" % Tempo.texto_data())
	if Opcoes.v("gravacao_automatica"):
		Gravar.gravar(Jogo.espaco_gravacao)   # grava ao entrar na cidade (docs/SISTEMAS.md, secção 18)
	if Jogo.tem_flag("dia_da_subida_pendente"):
		Jogo.flags.erase("dia_da_subida_pendente")
		for id in Dados.tabela("npcs").keys():
			Amizade.mudar(id, 20)
		Sistema.mensagem("Dia da Subida! Toda a Ascendia festeja a tua vitória (+20 amizade com todos).", "nivel")


func codigo(cx: int, cy: int) -> String:
	if cy < 0 or cy >= altura or cx < 0 or cx >= largura:
		return "tt"
	return dados.grelha[cy][cx]


# ------------------------------------------------------------------ gente na rua ------------------------------------------------------------------

var _ruas: Array[Vector2i] = []
var _gente: Array[Transeunte] = []


## 12 pessoas sem nome a passear pelas ruas e praças (docs/CIDADES.md 4.1); à noite só ficam 5.
func _gente_na_rua() -> void:
	for cy in altura:
		for cx in largura:
			if codigo(cx, cy) in ["::", "▓▓", "Fn", "Cr", "Qa"]:
				_ruas.append(Vector2i(cx, cy))
	if _ruas.is_empty():
		return
	for i in 12:
		var t := Transeunte.new()
		t.lugar = "ascendia"
		t.pontos = _ponto_rua
		add_child(t)
		t.global_position = _ponto_rua() + Vector3(0, 0.5, 0)
		_gente.append(t)
	_gente_hora(Tempo.hora)
	Tempo.nova_hora.connect(_gente_hora)


func _ponto_rua() -> Vector3:
	var c: Vector2i = _ruas[randi() % _ruas.size()]
	return centro(c.x, c.y) + Vector3(randf_range(-3.5, 3.5), 0, randf_range(-3.5, 3.5))


func _gente_hora(_h: Variant) -> void:
	var noite: bool = Tempo.hora >= 21.0 or Tempo.hora < 6.0
	for i in _gente.size():
		var ve := not noite or i < 5
		_gente[i].visible = ve
		_gente[i].process_mode = Node.PROCESS_MODE_INHERIT if ve else Node.PROCESS_MODE_DISABLED


# para a vida (bichos): a relva e as ruas de terra
const CHAO_BICHOS := ["..", "^^", "tt"]
var _abertas: Array[Vector2i] = []


func altura_em(_x: float, _z: float) -> float:
	return 0.0


func celulas_abertas() -> Array[Vector2i]:
	if _abertas.is_empty():
		for cy in altura:
			for cx in largura:
				if codigo(cx, cy) in CHAO_BICHOS:
					_abertas.append(Vector2i(cx, cy))
	return _abertas


func ponto_bicho(longe_de: Vector3, distancia: float) -> Vector3:
	var lista := celulas_abertas()
	for i in 12:
		if lista.is_empty():
			break
		var c: Vector2i = lista[randi() % lista.size()]
		var p := centro(c.x, c.y) + Vector3(randf_range(-4, 4), 0, randf_range(-4, 4))
		if longe_de == Vector3.INF or Vector2(p.x - longe_de.x, p.z - longe_de.z).length() >= distancia:
			return p
	return Vector3.INF


func ponto_aberto(p: Vector3) -> bool:
	var c := celula_de(p)
	return codigo(c.x, c.y) in CHAO_BICHOS


func pontos_agua() -> Array[Vector3]:
	var r: Array[Vector3] = []
	for cy in altura:
		for cx in largura:
			if codigo(cx, cy) == "~~":
				r.append(centro(cx, cy) + Vector3(0, -0.4, 0))
	return r


func celula_de(p: Vector3) -> Vector2i:
	return Vector2i(int(floor((p.x + largura * CEL / 2.0) / CEL)), int(floor((p.z + altura * CEL / 2.0) / CEL)))


func centro_celula(cx: int, cy: int) -> Vector3:
	return centro(cx, cy)


func centro(cx: float, cy: float) -> Vector3:
	return Vector3((cx + 0.5) * CEL - largura * CEL / 2.0, 0.0, (cy + 0.5) * CEL - altura * CEL / 2.0)


func _construir_chao() -> void:
	var ladrilho := CEL / POR_CEL
	# o chão: ladrilhos de 2 m com o shader da natureza (relva, terra batida e calçada misturadas, docs/ARTE.md 6.1)
	var splat := Image.create(largura * POR_CEL, altura * POR_CEL, false, Image.FORMAT_RGB8)
	var ruido := FastNoiseLite.new()
	ruido.seed = 7
	ruido.frequency = 0.08
	var caixa := BoxMesh.new()
	caixa.size = Vector3(ladrilho, 0.2, ladrilho)
	var arvores := Natureza.plantas(1, "arvore")
	var mato := Natureza.plantas(1, "mato")
	var erva := Natureza.plantas(1, "erva")
	var flores := Natureza.plantas(1, "flores")
	for cy in altura:
		for cx in largura:
			var c := codigo(cx, cy)
			var base := centro(cx, cy)
			if c in ["~~"]:
				_agua(cx, cy)
				continue
			for i in POR_CEL:
				for j in POR_CEL:
					var p := base + Vector3((i - POR_CEL / 2.0 + 0.5) * ladrilho, -0.1, (j - POR_CEL / 2.0 + 0.5) * ladrilho)
					_pecas.por_malha(caixa, Transform3D(Basis(), p))
					var sp := Color(0, 0, 0)
					if c in CHAO_PEDRA or c == "==":
						sp.r = 1.0
					elif c in CHAO_TERRA and c != "..":
						sp.g = 1.0
					elif ruido.get_noise_2d(cx * POR_CEL + i, cy * POR_CEL + j) > 0.3:
						sp.b = 1.0
					splat.set_pixel(cx * POR_CEL + i, cy * POR_CEL + j, sp)
			match c:
				"tt":
					for k in 5:
						var p := base + Vector3(_rng.randf_range(-4.2, 4.2), 0, _rng.randf_range(-4.2, 4.2))
						_planta(arvores, p)
						_cilindro(p, 0.6)
					for k in 3:
						_planta(mato, base + Vector3(_rng.randf_range(-4.5, 4.5), 0, _rng.randf_range(-4.5, 4.5)))
				"^^":
					if _rng.randf() < 0.35:
						_planta(arvores, base)
						_cilindro(base, 0.6)
					_planta(mato, base + Vector3(_rng.randf_range(-4, 4), 0, _rng.randf_range(-4, 4)))
				"##":
					_muralha(cx, cy)
				"::":
					if (cx + cy) % 4 == 0:
						_pecas.por(ARTE + "candeeiro.glb", Transform3D(Basis(), base + Vector3(4.0, 0, 4.0)))
				"==":
					if Jogo.tem_flag("projeto_ponte_rio") or Jogo.tem_flag("missao_R1_02"):
						_pecas.por(ARTE + "cais.glb", Transform3D(Basis(), base + Vector3(0, 0.0, 0)).scaled_local(Vector3(1.2, 1, 1.3)))
					else:
						_agua(cx, cy)
				"][":
					_pecas.por(ARTE + "portao.glb", Transform3D(Basis(Vector3.UP, PI / 2 if codigo(cx, cy - 1) == "##" else 0.0), base))
			# erva e flores na relva
			if c in ["..", "^^", "tt"]:
				for k in (6 if c == ".." else 9):
					_planta(erva, base + Vector3(_rng.randf_range(-4.8, 4.8), 0, _rng.randf_range(-4.8, 4.8)))
				if ruido.get_noise_2d(cx * 7.0, cy * 7.0) > 0.1:
					for k in 4:
						_planta(flores, base + Vector3(_rng.randf_range(-4.8, 4.8), 0, _rng.randf_range(-4.8, 4.8)))
	caixa.material = Natureza.material_chao(1, ImageTexture.create_from_image(splat), Vector2(-largura * CEL / 2.0, -altura * CEL / 2.0),
			Vector2(largura * CEL, altura * CEL), {"caminho": "calcada"})


func _planta(lista: Array, p: Vector3) -> void:
	if not lista.is_empty():
		_pecas.por(lista[_rng.randi() % lista.size()], Transform3D(Basis.from_scale(Vector3(-1.0 if _rng.randf() < 0.5 else 1.0, 1, 1)), p))


func _agua(cx: int, cy: int) -> void:
	var m := MeshInstance3D.new()
	var q := PlaneMesh.new()
	q.size = Vector2(CEL, CEL)
	m.mesh = q
	m.material_override = Andar.agua_material(Color("0eaf9b"))
	m.position = centro(cx, cy) + Vector3(0, -0.4, 0)
	add_child(m)
	_parede(centro(cx, cy), Vector3(CEL, 4, CEL))


func _muralha(cx: int, cy: int) -> void:
	var base := centro(cx, cy)
	var vertical := codigo(cx, cy - 1) == "##" or codigo(cx, cy + 1) == "##"
	for k in 3:
		var off := (k - 1) * 3.4
		var p := base + (Vector3(0, 0, off) if vertical else Vector3(off, 0, 0))
		_pecas.por(ARTE + "muralha.glb", Transform3D(Basis(Vector3.UP, PI / 2 if vertical else 0.0), p))
	_parede(base + Vector3(0, 3, 0), Vector3(CEL if not vertical else 2.0, 6, CEL if vertical else 2.0))


func _parede(p: Vector3, tam: Vector3) -> void:
	var f := CollisionShape3D.new()
	var b := BoxShape3D.new()
	b.size = tam
	f.shape = b
	f.position = p
	_corpo.add_child(f)


func _cilindro(p: Vector3, r: float) -> void:
	var f := CollisionShape3D.new()
	var c := CylinderShape3D.new()
	c.radius = r
	c.height = 4.0
	f.shape = c
	f.position = p + Vector3(0, 2, 0)
	_corpo.add_child(f)


func _construir_edificios() -> void:
	for e in dados.edificios:
		var cx: float = e.centro[0]
		var cy: float = e.centro[1]
		var p := centro(cx, cy)
		var modelo: String = ARTE + e.modelo + ".glb"
		var cod: String = e.codigo
		if cod == "TC" and not Jogo.tem_flag("casa_heroi"):
			continue   # a tua casa só aparece depois do andar 20
		match cod:
			"Me":   # o mercado: várias bancas
				for k in e.celulas.size() * 2:
					var c: Array = e.celulas[k % e.celulas.size()]
					var q := centro(c[0], c[1]) + Vector3((k / e.celulas.size()) * 4.0 - 2.0, 0, 0)
					_pecas.por(ARTE + "banca_%d.glb" % (k % 3 + 1), Transform3D(Basis(), q))
					_parede(q + Vector3(0, 1, 0), Vector3(2.6, 2, 1.4))
				locais[cod] = p + Vector3(0, 0, 3)
				continue
			"Eb", "Tr", "ca", "cb":   # várias peças pequenas, uma por célula
				for c in e.celulas:
					var q := centro(c[0], c[1])
					var m: String = ARTE + ("casa_%d.glb" % (_rng.randi() % 3 + 1) if cod == "ca" else e.modelo + ".glb")
					_por_modelo(m, q, 1.0, cod in ["ca", "cb"])
				locais[cod] = centro(e.celulas[0][0], e.celulas[0][1]) + Vector3(0, 0, 5)
				continue
		# o edifício cresce para ocupar ~60% do terreno que tem no mapa (entre ×1 e ×2,4)
		var xs: Array = e.celulas.map(func(c): return c[0])
		var ys: Array = e.celulas.map(func(c): return c[1])
		var tam := Vector2((xs.max() - xs.min() + 1) * CEL, (ys.max() - ys.min() + 1) * CEL)
		var mc := Pecas.caixa(modelo)
		var esc: float = ESCALA.get(e.modelo, 1.0)
		if mc.size.x > 0.1 and not cod in ["Cr", "Fn", "Qa", "Pa", "Pi", "Ca", "Mi", "Qt"]:
			esc = clampf(minf(tam.x * 0.6 / mc.size.x, tam.y * 0.6 / mc.size.z), 1.0, 1.8)
		var caixa := _por_modelo(modelo, p, esc, true)
		locais[cod] = p + Vector3(0, 0, caixa.end.z * esc + 1.8)
		match cod:
			"Cr":
				ponto_chegada = p + Vector3(0, 0, 4)
				var i := Interagivel.new()
				i.texto = "Cristal Mestre (entrar na torre)"
				i.position = p
				add_child(i)
				i.usado.connect(func(_j): _cristal_mestre())
			"Qa":
				var i := Interagivel.new()
				i.texto = "Quadro de avisos"
				i.position = p
				add_child(i)
				i.usado.connect(func(_j):
					var q = get_tree().get_first_node_in_group("diario_ui")
					if q:
						q.abrir_quadro())
			"Gu":   # o Cristal de Avaliação, à porta da Guilda
				var cr := Interagivel.new()
				cr.texto = "Cristal de Avaliação"
				cr.position = locais[cod] + Vector3(4.0, 0, -0.6)
				add_child(cr)
				var vis: Node3D = (load(ARTE + "cristal_mestre.glb") as PackedScene).instantiate()
				vis.scale = Vector3.ONE * 0.45
				vis.position = cr.position
				add_child(vis)
				cr.usado.connect(func(_j): _cristal_avaliacao())
			"Pi", "Ca":   # o rio de Ascendia: pesca (o Pip está ao pé)
				var pi := Interagivel.new()
				pi.texto = "Pescar"
				pi.position = locais[cod] + Vector3(-3.0, 0, 0)
				add_child(pi)
				pi.usado.connect(func(_j):
					var ui = get_tree().get_first_node_in_group("pesca_ui")
					if ui:
						ui.pescar(0, true))
			"Fo":
				_estacao("forja", p + Vector3(3.0 * esc, 0, caixa.end.z * esc + 0.5))
			"Al":
				_estacao("alquimia", p + Vector3(-2.0, 0, caixa.end.z * esc + 0.5))
	if ponto_chegada == Vector3.ZERO:
		ponto_chegada = Vector3.ZERO


func _estacao(e: String, p: Vector3) -> void:
	var s := Estacao.new()
	s.estacao = e
	s.position = p
	add_child(s)


## Um edifício (instância própria, com colisão pela caixa do modelo). Devolve a caixa (sem escala).
func _por_modelo(caminho: String, p: Vector3, esc: float, colisao: bool) -> AABB:
	if not ResourceLoader.exists(caminho):
		return AABB()
	var cena: Node3D = (load(caminho) as PackedScene).instantiate()
	cena.position = p
	cena.scale = Vector3.ONE * esc
	add_child(cena)
	var a := Pecas.caixa(caminho)
	if a.size.length() > 0.1 and a.size.y > 2.5:   # edifícios altos ficam transparentes quando tapam o herói
		cena.add_to_group("tapa_vista")
		cena.set_meta("raio", maxf(a.size.x, a.size.z) * esc * 0.55)
		cena.set_meta("altura", a.size.y * esc * 0.5)
	if colisao and a.size.length() > 0.1:
		_parede(p + a.get_center() * esc, a.size * esc * Vector3(0.95, 1, 0.95))
	return a


func _criar_jogador() -> void:
	jogador = preload("res://cenas/personagens/jogador.tscn").instantiate()
	if Jogo.tem_flag("acordar_estalagem") and locais.has("Es"):   # depois de morrer, acordas na Estalagem
		Jogo.flags.erase("acordar_estalagem")
		ponto_chegada = locais["Es"]
	jogador.position = ponto_chegada + Vector3(0, 0.5, 0)
	add_child(jogador)
	camara = Camara.new()
	camara.alvo = jogador
	add_child(camara)
	add_child(preload("res://cenas/ui/hud.tscn").instantiate())


# ------------------------------------------------------------------ NPCs ------------------------------------------------------------------

func _criar_npcs() -> void:
	for id in dados.get("npcs", {}):
		if Dados.obter("npcs", id).is_empty():
			continue
		var n := NPC.new().configurar(id)
		add_child(n)
		npcs[id] = n
	_rotinas(true)


## Onde está cada NPC agora (docs/NPCS.md "Onde está"): vai a pé; se não está em lado nenhum, está em casa.
func onde(id: String) -> String:
	var r: Dictionary = dados.npcs.get(id, {})
	var h := int(Tempo.hora)
	var domingo := Tempo.e_domingo()
	var rotina: Array = r.get("rotina", [])
	for passo in rotina:
		if bool(passo.get("domingo", false)) != domingo and passo.get("domingo", false):
			continue
		var de := int(passo.de)
		var ate := int(passo.ate)
		var dentro := (h >= de and h < ate) if de < ate else (h >= de or h < ate)
		if dentro:
			return passo.local
	if rotina.is_empty():
		return r.get("balcao", "Fn")
	return "casa"


func _rotinas(logo: bool) -> void:
	var usados := {}
	for id in npcs:
		var n: NPC = npcs[id]
		var l := onde(id)
		var em_casa := l == "casa" or not locais.has(l)
		n.visible = not em_casa
		n.process_mode = Node.PROCESS_MODE_DISABLED if em_casa else Node.PROCESS_MODE_INHERIT
		n.collision_layer = 0 if em_casa else 1
		if em_casa:
			continue
		var k: int = usados.get(l, 0)
		usados[l] = k + 1
		var alvo: Vector3 = locais[l] + Vector3((k % 3 - 1) * 1.6, 0.3, (k / 3) * 1.4)
		if logo or n.global_position.distance_to(alvo) > 60.0:
			n.global_position = alvo
		else:
			n.ir_para(alvo)


## O Cristal de Avaliação sorteia a Skill Única (docs/PROGRESSAO.md, secção 2; missão H_02).
func _cristal_avaliacao() -> void:
	var ui = get_tree().get_first_node_in_group("dialogo_ui")
	if Jogo.skill_unica != "":
		var s := Dados.obter("skills_unicas", Jogo.skill_unica)
		await ui.falar([{"quem": "Sistema", "texto": "Skill Única: **%s**. %s" % [s.nome_pt, s.efeito_pt]}])
		return
	var lista := Dados.tabela("skills_unicas").keys()
	var rng := RandomNumberGenerator.new()
	rng.randomize()
	Jogo.skill_unica = lista[rng.randi() % lista.size()]
	var s := Dados.obter("skills_unicas", Jogo.skill_unica)
	EfeitosCombate.animado(get_tree(), "subir_nivel", jogador.global_position + Vector3(0, 1, 0))
	await ui.falar([{"acao": "O cristal acende-se. Uma janela azul aparece à tua frente."},
		{"quem": "Sistema", "texto": "Avaliação concluída. Skill Única: **%s**." % s.nome_pt},
		{"quem": "Sistema", "texto": s.efeito_pt}])
	Jogo.por_flag("cristal_avaliacao")
	if Jogo.skill_unica == "bolsa_infinita":
		Jogo.inventario.aumentar(int(Dados.c("unica_bolsa_espacos", 99)))
	Eventos.stats_mudaram.emit()


# ------------------------------------------------------------------ torre ------------------------------------------------------------------

## O Cristal Mestre leva a qualquer andar com Zona Segura que já visitaste (docs/INTERFACE.md, secção 5).
func _cristal_mestre() -> void:
	var ui = get_tree().get_first_node_in_group("dialogo_ui")
	var andares := [1]
	for a in Jogo.cristais:
		if not int(a) in andares:
			andares.append(int(a))
	andares.sort()
	var opcoes: Array = andares.map(func(a): return "Andar %d — %s" % [a, Dados.tabela("andares/a%03d" % a).get("nome_pt", "")])
	opcoes.append("Ficar em Ascendia")
	var i: int = await ui.escolher(opcoes)
	if i < andares.size():
		Jogo.andar_atual = andares[i]
		Cenas.mudar("res://cenas/mundo/andar.tscn")
