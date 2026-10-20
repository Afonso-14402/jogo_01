class_name SalaMasmorra
extends Node3D
## As salas especiais das masmorras escondidas (docs/regioes/rNN, secção 9; dados/masmorras.json, "mecanica" de cada
## sala; números em docs/TORRE.md 3.1). Fica dentro da Masmorra (mesmas coordenadas) e abre o portão da sala
## (Masmorra._abrir) quando a sala está resolvida. Tipos: linhas, ponte, agua, pedra, labirinto, vento, ar,
## despertar, espelhos, cavidades, balanca, lore.

var m: Masmorra
var i: int = 0
var mec: Dictionary = {}
var c := Vector3.ZERO              # centro da sala (local, como na Masmorra)
var _t: float = 0.0
var _rng := RandomNumberGenerator.new()
var _feita := false

# linhas
var _linhas: Array = []            # [{z, fase, faixa: MeshInstance3D, visual: Node3D, feriu, armada}]
var _placas: Array = []
# ponte
var _pedras: Array = []            # [{corpo, malha, p, t_pisada, caida}]
# agua
var _agua: MeshInstance3D
var _agua_h: float = -0.2
var _agua_a_subir := false
# pedra
var _pedra: MeshInstance3D
var _pedra_feriu := false
# labirinto
var _muros: Array = []             # [{malha, colisao, grupo}]
# vento
var _abrigos: Array = []
var _particulas: CPUParticles3D
# ar
var _ar: float = 100.0
var _ar_rotulo: Label3D
var _bolhas: Array = []            # [{malha, p, volta}]
# despertar
var _dormentes: Array = []         # [Monstro]
var _vivos: int = 0
# espelhos
var _raios: Array = []             # segmentos do raio (MeshInstance3D)
var _estado_esp: Array = []
var _certo_esp: Array = []
var _pontos_esp: Array = []
# lore (núcleo)
var _nucleo: MeshInstance3D
var _toques: int = 0
var _lidos: Dictionary = {}


func _ready() -> void:
	_rng.randomize()
	c = m.centro(i)
	match String(mec.get("tipo", "")):
		"linhas": _fazer_linhas()
		"ponte": _fazer_ponte()
		"agua": _fazer_agua()
		"pedra": _fazer_pedra()
		"labirinto": _fazer_labirinto()
		"vento": _fazer_vento()
		"ar": _fazer_ar()
		"despertar": _fazer_despertar()
		"espelhos": _fazer_espelhos()
		"cavidades": _fazer_cavidades()
		"balanca": _fazer_balanca()
		"lore": _fazer_lore()


# ------------------------------------------------------------------ ajudas ------------------------------------------------------------------

func resolver(texto := "") -> void:
	if _feita:
		return
	_feita = true
	if texto != "":
		Sistema.mensagem(texto, "nivel")
	Colecoes.contar("puzzles")
	m._abrir(i)


func jogador() -> Node3D:
	return get_tree().get_first_node_in_group("jogador") as Node3D


## Posição do herói nas coordenadas da masmorra.
func local_jogador() -> Vector3:
	var j := jogador()
	return j.global_position - m.global_position if j else Vector3(0, -999, 0)


func na_sala(p: Vector3) -> bool:
	return absf(p.z - c.z) < Masmorra.FUNDO / 2.0 and absf(p.x - c.x) < Masmorra.LARGURA / 2.0 and p.y > -2.0


func ferir(fracao: float, origem: Vector3) -> void:
	var j := jogador()
	if j and j.has_method("receber_golpe"):
		j.receber_golpe({"valor": maxi(1, int(Jogo.hp_maximo() * fracao)), "origem": m.global_position + origem})


## Pedra com a textura das paredes, pintada de uma cor (blocos, pedras, colunas).
func pedra(cor: Color) -> StandardMaterial3D:
	return m._material("res://arte/interiores/parede_pedra.png", cor)


func mat(cor: Color, transparente := false, brilha := false) -> StandardMaterial3D:
	var x := StandardMaterial3D.new()
	x.albedo_color = cor
	if transparente:
		x.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
	if brilha:
		x.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	return x


func caixa(p: Vector3, tam: Vector3, material: Material) -> MeshInstance3D:
	var mi := MeshInstance3D.new()
	var b := BoxMesh.new()
	b.size = tam
	mi.mesh = b
	mi.material_override = material
	mi.position = p
	add_child(mi)
	return mi


## Um corpo sólido próprio (para se poder desligar ou mexer sozinho).
func corpo(p: Vector3, tam: Vector3, material: Material, animavel := false) -> Array:
	var b: PhysicsBody3D = AnimatableBody3D.new() if animavel else StaticBody3D.new()
	b.position = p
	add_child(b)
	var f := CollisionShape3D.new()
	var s := BoxShape3D.new()
	s.size = tam
	f.shape = s
	b.add_child(f)
	var mi := MeshInstance3D.new()
	var bm := BoxMesh.new()
	bm.size = tam
	mi.mesh = bm
	mi.material_override = material
	b.add_child(mi)
	return [b, f, mi]


func rotulo(p: Vector3, texto: String, cor := Color("fbff86"), tam := 32) -> Label3D:
	var l := Label3D.new()
	l.text = texto
	l.font_size = tam
	l.pixel_size = 0.01
	l.outline_size = 10
	l.modulate = cor
	l.billboard = BaseMaterial3D.BILLBOARD_ENABLED
	l.position = p
	add_child(l)
	return l


func alavanca(texto := "Puxar a alavanca do portão") -> void:
	var p := c + Vector3(2.5, 0, -Masmorra.FUNDO / 2.0 + 1.4)
	caixa(p + Vector3(0, 0.5, 0), Vector3(0.3, 1.0, 0.3), mat(Color("694f62")))
	caixa(p + Vector3(0, 1.1, 0), Vector3(0.5, 0.3, 0.5), mat(Color("ea4f36")))
	m._usar(p + Vector3(0, 0, 0.7), texto, func(): resolver())


func escolher(opcoes: Array) -> int:
	var ui = get_tree().get_first_node_in_group("dialogo_ui")
	if ui == null or ui.ocupado:
		return -1
	ui.ocupado = true
	var k: int = await ui.escolher(opcoes)
	ui.fechar()
	return k


# ------------------------------------------------------------------ linhas (raízes, lâminas, dardos, fogo, retratos, canhões) ------------------------------------------------------------------

const AVISO := 0.8
const FERE := 0.4
const CICLO := 2.4
const QUADROS := {"raiz": 4, "osso": 4, "lamina": 4, "dardo": 2, "bala": 2, "fogo": 4, "olhos": 2}


func _fazer_linhas() -> void:
	var visual: String = mec.get("visual", "raiz")
	for k in 6:
		var z := c.z + Masmorra.FUNDO / 2.0 - 3.5 - k * 2.2
		var faixa := caixa(Vector3(c.x, 0.03, z), Vector3(Masmorra.LARGURA - 1.0, 0.04, 1.6), mat(Color(0.92, 0.31, 0.21, 0.0), true, true))
		var v := Node3D.new()
		v.position = Vector3(c.x, 0, z)
		add_child(v)
		var sprites: Array = []
		for x in range(-9, 10, 2):   # o que aparece quando a linha fere (arte/masmorras/armadilha_*.png)
			var nome: String = visual if visual in QUADROS else "raiz"
			var sp := Sprite3D.new()
			sp.texture = load("res://arte/masmorras/armadilha_%s.png" % nome)
			sp.hframes = int(QUADROS[nome])
			sp.pixel_size = 1.0 / 16.0
			sp.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
			sp.alpha_cut = SpriteBase3D.ALPHA_CUT_DISCARD
			sp.shaded = not visual in ["fogo", "olhos"]
			if visual in ["raiz", "osso"]:   # saem do chão: de pé, virados para a câmara
				sp.billboard = BaseMaterial3D.BILLBOARD_FIXED_Y
				sp.offset = Vector2(0, 12)
				sp.position = Vector3(x + _rng.randf_range(-0.4, 0.4), 0.0, _rng.randf_range(-0.4, 0.4))
				sp.scale = Vector3.ONE * _rng.randf_range(1.2, 1.6)
			else:
				sp.billboard = BaseMaterial3D.BILLBOARD_ENABLED
				sp.position = Vector3(x, 0.8 if visual != "lamina" else 0.75, 0)
				if visual == "lamina":
					sp.scale = Vector3.ONE * 1.6
			v.add_child(sp)
			sprites.append(sp)
		v.visible = false
		var fase := 0.0
		match String(mec.get("padrao", "onda")):
			"onda", "canhoes": fase = k * 0.4
			"ritmo": fase = (k % 2) * CICLO / 2.0
			"aleatorio", "retratos": fase = _rng.randf() * CICLO
		_linhas.append({"z": z, "fase": fase, "faixa": faixa, "visual": v, "sprites": sprites, "feriu": false, "armada": -1.0})
		if mec.get("padrao") in ["retratos", "canhoes"]:   # quem dispara: retratos ou canhões nas paredes
			for lado in [-1, 1]:
				caixa(Vector3(c.x + lado * (Masmorra.LARGURA / 2.0 - 0.45), 1.6, z), Vector3(0.2, 1.2, 1.0),
						mat(Color("966c6c") if mec.padrao == "retratos" else Color("3e3546")))
	if mec.get("padrao") == "placas":   # placas no chão: pisar uma arma a linha dela
		for k in 8:
			var lin: Dictionary = _linhas[k % _linhas.size()]
			var p := Vector3(c.x + _rng.randf_range(-8.0, 8.0), 0.04, lin.z + _rng.randf_range(-0.5, 0.5))
			caixa(p, Vector3(0.9, 0.06, 0.9), mat(Color("625565")))
			_placas.append({"p": p, "linha": lin})
	alavanca()


func _linhas_process(delta: float, lj: Vector3) -> void:
	var dentro := na_sala(lj)
	for lin in _linhas:
		var f: float
		if mec.get("padrao") == "placas":
			if float(lin.armada) < 0.0:
				f = -1.0
			else:
				lin.armada = float(lin.armada) + delta
				f = 1.2 + float(lin.armada)   # aviso logo e fere a seguir
				if float(lin.armada) > AVISO + FERE:
					lin.armada = -1.0
		else:
			f = fmod(_t + float(lin.fase), CICLO)
		var faixa: MeshInstance3D = lin.faixa
		var m_: StandardMaterial3D = faixa.material_override
		if f < 1.2:
			m_.albedo_color.a = 0.0
			lin.visual.visible = false
			lin.feriu = false
		elif f < 1.2 + AVISO:
			m_.albedo_color = Color(0.92, 0.31, 0.21, 0.12 + (f - 1.2) * 0.5)
			lin.visual.visible = false
		else:
			m_.albedo_color = Color(1.0, 0.5, 0.25, 0.7)
			lin.visual.visible = true
			var desde := f - 1.2 - AVISO
			for sp: Sprite3D in lin.sprites:   # os espinhos saem do chão e tremem; o resto anda em ciclo
				if mec.get("visual") in ["raiz", "osso"]:
					sp.frame = mini(2, int(desde * 16.0)) if desde < 0.2 else 2 + int(_t * 12.0) % 2
				else:
					sp.frame = int(_t * 10.0) % sp.hframes
			if mec.get("visual") in ["dardo", "bala", "olhos", "fogo"]:   # os projéteis atravessam a sala
				lin.visual.position.x = c.x + sin(_t * 9.0) * 1.5
			if dentro and not lin.feriu and absf(lj.z - float(lin.z)) < 0.9:
				lin.feriu = true
				ferir(0.1, Vector3(lj.x, 0, float(lin.z) + 2.0))
	if mec.get("padrao") == "placas" and dentro:
		for pl in _placas:
			if Vector2(lj.x - pl.p.x, lj.z - pl.p.z).length() < 0.6 and float(pl.linha.armada) < 0.0:
				pl.linha.armada = 0.0
				Audio.efeito("clique")


# ------------------------------------------------------------------ ponte (cai, baloiça, gravidade invertida) ------------------------------------------------------------------

func _fazer_ponte() -> void:
	var lava := int(m.d.get("regiao", 1)) == 7
	var cor_pedra := Color("c7dcd0") if mec.get("invertido", false) else (Color("7f708a") if lava else Color("9babb2"))
	# (o fundo só se vê: fica logo abaixo das pedras para no 2D não descer para lá da parede de baixo; cair conta-se
	# pela altura do herói, em _process)
	var fundo := caixa(Vector3(c.x, -0.8, c.z), Vector3(Masmorra.LARGURA, 0.2, Masmorra.FUNDO - 6.0),
			mat(Color("f79617") if lava else (Color("8fd3ff") if mec.get("invertido", false) else Color("120e16")), false, true))
	fundo.name = "Vazio"
	# um caminho de pedras, fila a fila, sempre com uma pedra a menos de 2,5 m da da fila de trás
	var x := 0.0
	var z := c.z + Masmorra.FUNDO / 2.0 - 4.0
	while z > c.z - Masmorra.FUNDO / 2.0 + 3.5:
		x = clampf(x + _rng.randf_range(-2.2, 2.2), -7.0, 7.0)
		for extra in [0.0, _rng.randf_range(3.0, 5.0) * (1 if _rng.randf() < 0.5 else -1)]:
			var p := Vector3(c.x + clampf(x + extra, -8.5, 8.5), -0.25, z)
			var b := corpo(p, Vector3(1.8, 0.5, 1.8), pedra(cor_pedra), bool(mec.get("baloica", false)))
			_pedras.append({"corpo": b[0], "forma": b[1], "malha": b[2], "p": p, "t": -1.0, "caida": 0.0, "fase": _rng.randf() * TAU})
			if mec.get("invertido", false):   # coisas penduradas ao contrário por baixo (o "teto" é o chão)
				var pend := caixa(p + Vector3(0, -1.2, 0), Vector3(0.4, 1.8, 0.4), mat(Color("9babb2")))
				pend.reparent(b[0], true)
		z -= 2.2
	if mec.get("invertido", false):
		rotulo(c + Vector3(0, 3.0, 2.0), "↓ céu ↓   (cair é para cima)", Color("8fd3ff"), 28)
	alavanca()


func _ponte_process(delta: float, lj: Vector3) -> void:
	for pd in _pedras:
		var b: Node3D = pd.corpo
		if mec.get("baloica", false):   # correntes: as pedras baloiçam de um lado para o outro
			b.position.x = pd.p.x + sin(_t * 1.3 + float(pd.fase)) * 1.4
		if float(mec.get("cai", 0)) <= 0.0:
			continue
		if float(pd.caida) > 0.0:   # caída: volta ao sítio 4 s depois
			pd.caida = float(pd.caida) - delta
			if float(pd.caida) <= 0.0:
				b.position = pd.p
				(pd.forma as CollisionShape3D).disabled = false
				(pd.malha as MeshInstance3D).visible = true
			continue
		var em_cima: bool = Vector2(lj.x - b.position.x, lj.z - b.position.z).length() < 1.1 and absf(lj.y - b.position.y) < 1.2
		if em_cima and float(pd.t) < 0.0:
			pd.t = 0.0
		if float(pd.t) >= 0.0:
			pd.t = float(pd.t) + delta
			(pd.malha as MeshInstance3D).position.x = sin(_t * 60.0) * 0.05   # treme antes de cair
			if float(pd.t) >= float(mec.cai):
				pd.t = -1.0
				pd.caida = 4.0
				(pd.forma as CollisionShape3D).disabled = true
				(pd.malha as MeshInstance3D).visible = false
	# caíste ao vazio: voltas ao princípio da sala e perdes 10% do HP
	if absf(lj.z - c.z) < Masmorra.FUNDO / 2.0 and lj.y < -3.0:
		var j := jogador()
		j.global_position = m.global_position + c + Vector3(0, 0.6, Masmorra.FUNDO / 2.0 - 1.5)
		if "velocity" in j:
			j.velocity = Vector3.ZERO
		ferir(0.1, c)
		Sistema.mensagem("Caíste! Voltas ao princípio da sala.", "aviso")


# ------------------------------------------------------------------ água que sobe ------------------------------------------------------------------

const AGUA_MAX := 3.0
const AGUA_TEMPO := 40.0


func _fazer_agua() -> void:
	# rampa ao longo da parede oeste até uma plataforma alta com a alavanca
	var comp := Masmorra.FUNDO - 6.0
	var alto := 2.6
	var ang := atan2(alto, comp)
	var rampa := corpo(Vector3(c.x - 8.5, alto / 2.0 - 0.15, c.z), Vector3(3.0, 0.3, sqrt(comp * comp + alto * alto)), m._mat_parede)
	(rampa[0] as Node3D).rotation.x = ang
	corpo(Vector3(c.x - 6.5, alto - 0.15, c.z - Masmorra.FUNDO / 2.0 + 2.0), Vector3(7.0, 0.3, 3.4), m._mat_parede)
	var p := c + Vector3(-5.0, alto, -Masmorra.FUNDO / 2.0 + 2.0)
	caixa(p + Vector3(0, 0.5, 0), Vector3(0.3, 1.0, 0.3), mat(Color("694f62")))
	caixa(p + Vector3(0, 1.1, 0), Vector3(0.5, 0.3, 0.5), mat(Color("ea4f36")))
	m._usar(p + Vector3(0, 0, 0.7), "Puxar a alavanca (lá em cima)", func():
		_agua_a_subir = false
		create_tween().tween_method(func(h: float): _agua_h = h, _agua_h, -0.2, 3.0)
		resolver("A alavanca abre um ralo: a água escoa-se e o portão abre!"))
	_agua = MeshInstance3D.new()
	var pm := PlaneMesh.new()
	pm.size = Vector2(Masmorra.LARGURA - 0.6, Masmorra.FUNDO - 0.6)
	pm.subdivide_width = 22
	pm.subdivide_depth = 18
	_agua.mesh = pm
	_agua.material_override = Andar.agua_material(Color("0b8a8f"))
	_agua.position = c + Vector3(0, _agua_h, 0)
	add_child(_agua)


func _agua_process(delta: float, lj: Vector3) -> void:
	if not _agua_a_subir and not _feita and na_sala(lj) and _agua_h < 0.0:
		_agua_a_subir = true
		Sistema.mensagem("Ouve-se água a jorrar! A sala está a encher-se: sobe pela rampa!", "aviso")
	if _agua_a_subir:
		_agua_h = minf(AGUA_MAX, _agua_h + AGUA_MAX / AGUA_TEMPO * delta)
	_agua.position.y = _agua_h
	if na_sala(lj) and lj.y + 1.2 < _agua_h and fmod(_t, 1.0) < delta:   # debaixo de água: 5% por segundo
		ferir(0.05, lj + Vector3(0, 0, 1))


# ------------------------------------------------------------------ pedra que rola ------------------------------------------------------------------

func _fazer_pedra() -> void:
	var p := c + Vector3(0, 0, -Masmorra.FUNDO / 2.0 + 2.5)
	caixa(p + Vector3(0, 0.5, 0), Vector3(1.2, 1.0, 1.2), m._mat_parede)
	var idolo := caixa(p + Vector3(0, 1.3, 0), Vector3(0.5, 0.6, 0.5), mat(Color("f9c22b"), false, true))
	var ref := [null]
	ref[0] = m._usar(p + Vector3(0, 0, 1.0), "Apanhar o ídolo", func():
		if _feita:
			return
		idolo.visible = false
		ref[0].ativo = false
		resolver()
		Sistema.mensagem("Apanhas o ídolo… CLONC. Atrás de ti, uma pedra GIGANTE começa a rolar. FOGE pelo portão!", "aviso")
		_pedra = MeshInstance3D.new()
		var sm := SphereMesh.new()
		sm.radius = 1.7
		sm.height = 3.4
		_pedra.mesh = sm
		_pedra.material_override = m._mat_parede
		_pedra.position = c + Vector3(0, 1.7, Masmorra.FUNDO / 2.0 - 1.0)
		add_child(_pedra))


func _pedra_process(delta: float, lj: Vector3) -> void:
	if _pedra == null:
		return
	if _pedra.position.z > c.z - Masmorra.FUNDO / 2.0 + 2.0:
		_pedra.position.z -= 4.6 * delta
		_pedra.rotation.x -= 4.6 * delta / 1.7
	if not _pedra_feriu and (lj - _pedra.position).length() < 2.2:
		_pedra_feriu = true
		ferir(0.25, _pedra.position + Vector3(0, 0, 2))


# ------------------------------------------------------------------ labirinto de paredes que se mexem ------------------------------------------------------------------

func _fazer_labirinto() -> void:
	var cor := Color(1.0, 0.95, 0.82) if mec.get("visual") == "osso" else Color(0.8, 0.75, 0.85)
	for fila in 4:
		for col in 3:
			var p := c + Vector3(-6.0 + col * 6.0 + (3.0 if fila % 2 else 0.0), 1.0, Masmorra.FUNDO / 2.0 - 4.0 - fila * 3.2)
			var b := corpo(p, Vector3(4.2, 2.0, 0.5), pedra(cor))
			_muros.append({"corpo": b[0], "forma": b[1], "malha": b[2], "grupo": (fila + col) % 2, "base": p.y})
	alavanca()


func _labirinto_process(_delta: float, _lj: Vector3) -> void:
	var grupo_em_cima := int(_t / 3.0) % 2   # de 3 em 3 s, metade das paredes desce e a outra sobe
	for w in _muros:
		var cima: bool = int(w.grupo) == grupo_em_cima
		var b: Node3D = w.corpo
		b.position.y = move_toward(b.position.y, float(w.base) if cima else -1.1, 4.0 * _delta)
		(w.forma as CollisionShape3D).disabled = b.position.y < 0.0


# ------------------------------------------------------------------ vento ------------------------------------------------------------------

func _fazer_vento() -> void:
	for k in 4:   # colunas que servem de abrigo
		var p := c + Vector3(-6.0 + (k % 2) * 12.0 + (k / 2) * 3.0 - 1.5, 1.5, Masmorra.FUNDO / 2.0 - 5.0 - (k / 2) * 6.0)
		corpo(p, Vector3(1.2, 3.0, 1.2), m._mat_parede)
		_abrigos.append(p)
	_particulas = CPUParticles3D.new()
	_particulas.amount = 140
	_particulas.lifetime = 1.2
	_particulas.emission_shape = CPUParticles3D.EMISSION_SHAPE_BOX
	_particulas.emission_box_extents = Vector3(Masmorra.LARGURA / 2.0, 1.5, 0.5)
	_particulas.direction = Vector3(1, 0, 0) if mec.get("lado", false) else Vector3(0, 0, 1)
	_particulas.spread = 4.0
	_particulas.gravity = Vector3.ZERO
	_particulas.initial_velocity_min = 14.0
	_particulas.initial_velocity_max = 18.0
	var q := QuadMesh.new()
	q.size = Vector2(0.6, 0.05)
	q.material = mat(Color(1, 1, 1, 0.5), true, true)
	_particulas.mesh = q
	_particulas.position = c + (Vector3(-Masmorra.LARGURA / 2.0 + 1.0, 1.0, 0) if mec.get("lado", false) else Vector3(0, 1.0, -Masmorra.FUNDO / 2.0 + 1.0))
	if mec.get("lado", false):
		_particulas.emission_box_extents = Vector3(0.5, 1.5, Masmorra.FUNDO / 2.0)
	add_child(_particulas)
	alavanca()


func _vento_process(delta: float, lj: Vector3) -> void:
	var sopra := true
	if mec.get("rajadas", false):
		sopra = fmod(_t, 4.5) < 2.5   # 2,5 s a soprar, 2 s parado
	_particulas.emitting = sopra and not _feita
	if not sopra or _feita or not na_sala(lj):
		return
	var dir := Vector3(1, 0, 0) if mec.get("lado", false) else Vector3(0, 0, 1)
	for a in _abrigos:   # atrás de uma coluna (do lado de onde não vem o vento) não empurra
		var rel: Vector3 = lj - a
		if dir.z > 0.0 and rel.z > 0.0 and rel.z < 3.5 and absf(rel.x) < 1.0:
			return
		if dir.x > 0.0 and rel.x > 0.0 and rel.x < 3.5 and absf(rel.z) < 1.0:
			return
	var j := jogador() as CharacterBody3D
	if j:
		j.move_and_collide(dir * 4.2 * delta)


# ------------------------------------------------------------------ sala inundada (Ar) ------------------------------------------------------------------

func _fazer_ar() -> void:
	var tinta := caixa(c + Vector3(0, 0.02, 0), Vector3(Masmorra.LARGURA - 0.6, 0.02, Masmorra.FUNDO - 0.6), mat(Color(0.05, 0.4, 0.55, 0.35), true, true))
	tinta.name = "Agua"
	for k in 5:
		var p := c + Vector3(_rng.randf_range(-8.0, 8.0), 0.9, _rng.randf_range(-6.0, 6.0))
		var b := MeshInstance3D.new()
		var sm := SphereMesh.new()
		sm.radius = 0.45
		sm.height = 0.9
		b.mesh = sm
		b.material_override = mat(Color(0.56, 0.83, 1.0, 0.6), true, true)
		b.position = p
		add_child(b)
		_bolhas.append({"malha": b, "p": p, "volta": 0.0})
	_ar_rotulo = rotulo(Vector3.ZERO, "", Color("8fd3ff"), 28)
	_ar_rotulo.visible = false
	alavanca()


func _ar_process(delta: float, lj: Vector3) -> void:
	var dentro := na_sala(lj) and not _feita
	_ar_rotulo.visible = dentro
	if not dentro:
		_ar = 100.0
		return
	_ar = maxf(0.0, _ar - 6.0 * delta)   # 6% por segundo
	_ar_rotulo.position = lj + Vector3(0, 2.4, 0)
	_ar_rotulo.text = "Ar %d%%" % int(_ar)
	_ar_rotulo.modulate = Color("8fd3ff") if _ar > 30.0 else Color("ea4f36")
	for b in _bolhas:
		var mi: MeshInstance3D = b.malha
		if float(b.volta) > 0.0:
			b.volta = float(b.volta) - delta
			mi.visible = float(b.volta) <= 0.0
			continue
		mi.position.y = b.p.y + sin(_t * 3.0 + b.p.x) * 0.15
		if Vector2(lj.x - b.p.x, lj.z - b.p.z).length() < 1.0:
			_ar = 100.0
			b.volta = 6.0
			mi.visible = false
			Audio.efeito("bolha")
	if _ar <= 0.0 and fmod(_t, 1.0) < delta:   # sem ar: 8% por segundo
		ferir(0.08, lj + Vector3(0, 0, 1))


# ------------------------------------------------------------------ despertar (guerreiros congelados, golens do ouro) ------------------------------------------------------------------

func _fazer_despertar() -> void:
	var regiao := int(m.d.get("regiao", 1))
	var pool: Array = []
	var filtro: Array = mec.get("filtro", [])
	for x in Dados.tabela("monstros").values():
		if int(x.get("regiao", 0)) == regiao and x.get("tipo", "") in ["normal", "tanque", "rapido", "mago", "fraco"]:
			if filtro.is_empty() or filtro.any(func(f): return f in String(x.id)):
				pool.append(x.id)
	if pool.is_empty():
		for x in Dados.tabela("monstros").values():
			if int(x.get("regiao", 0)) == regiao and x.get("tipo", "") in ["normal", "tanque"]:
				pool.append(x.id)
	var n := int(mec.get("n", 6))
	var nivel := int(m.d.get("andar", 1)) + 3
	for k in n:
		var col := k % 4
		var fila := k / 4
		var p := c + Vector3(-7.5 + col * 5.0, 0.5, Masmorra.FUNDO / 2.0 - 5.0 - fila * 4.0)
		var mo := Monstro.new().configurar(pool[k % pool.size()], nivel)
		mo.position = p
		mo.process_mode = Node.PROCESS_MODE_DISABLED   # parado (congelado / de pedra) até passares perto
		add_child(mo)
		if mo.sprite:   # parados: azulados (gelo) ou cinzentos (pedra)
			mo.sprite.modulate = Color(0.6, 0.8, 1.3) if regiao == 5 else Color(0.65, 0.65, 0.7)
		_dormentes.append(mo)
		mo.morreu.connect(func(_x):
			_vivos -= 1
			if _vivos <= 0 and _dormentes.is_empty():
				resolver("Venceste-os a todos!"))
	if mec.get("ouro", false):
		for k in 4:
			var p := c + Vector3(-6.0 + k * 4.0, 0, -Masmorra.FUNDO / 2.0 + 2.5)
			var monte := caixa(p + Vector3(0, 0.3, 0), Vector3(1.4, 0.6, 1.0), mat(Color("f9c22b")))
			var ref := [null]
			ref[0] = m._usar(p + Vector3(0, 0, 1.0), "Apanhar o ouro", func():
				if not _feita:
					Sistema.mensagem("Os golens não te deixam tocar no ouro!", "aviso")
					return
				ref[0].ativo = false
				monte.visible = false
				Jogo.ganhar_ouro(250))


func _despertar_process(_delta: float, lj: Vector3) -> void:
	for mo in _dormentes.duplicate():
		if not is_instance_valid(mo):
			_dormentes.erase(mo)
			continue
		if Vector2(lj.x - mo.position.x, lj.z - mo.position.z).length() < 4.5:
			mo.process_mode = Node.PROCESS_MODE_INHERIT
			if mo.sprite:
				mo.sprite.modulate = Color.WHITE
			_dormentes.erase(mo)
			_vivos += 1
			Sistema.mensagem("Uma das estátuas mexe-se!", "aviso")


# ------------------------------------------------------------------ espelhos (luz ou sombra até ao selo) ------------------------------------------------------------------

func _fazer_espelhos() -> void:
	var n := int(mec.get("n", 3))
	var cor := Color(String(mec.get("cor", "f79617")))
	var sombras: bool = mec.get("sombras", false)
	var fonte := c + Vector3(-Masmorra.LARGURA / 2.0 + 1.2, 1.2, Masmorra.FUNDO / 2.0 - 3.0)
	caixa(fonte, Vector3(0.8, 0.8, 0.8), mat(cor if not sombras else Color("fbff86"), false, true))
	rotulo(fonte + Vector3(0, 1.2, 0), "luz" if not sombras else "sol", Color("fbff86"), 24)
	_pontos_esp = [fonte]
	for k in n:   # zigue-zague até ao selo
		_pontos_esp.append(c + Vector3((-1 if k % 2 == 0 else 1) * 5.0 + k, 1.2, Masmorra.FUNDO / 2.0 - 3.0 - (k + 1) * 3.6))
	var selo := c + Vector3(0, 1.2, -Masmorra.FUNDO / 2.0 + 1.5)
	_pontos_esp.append(selo)
	caixa(selo, Vector3(1.6, 1.6, 0.3), mat(Color("625565")))
	var setas := ["↑", "→", "↓", "←"]
	for k in n:
		_estado_esp.append(0)
		_certo_esp.append(1 + _rng.randi() % 3)
		var p: Vector3 = _pontos_esp[k + 1]
		var esp := caixa(p, Vector3(1.0, 1.6, 0.2) if not sombras else Vector3(0.9, 2.0, 0.9), mat(Color("c7dcd0") if not sombras else Color("625565")))
		var seta := rotulo(p + Vector3(0, 1.4, 0), setas[0], Color("8fd3ff"), 40)
		var kk := k
		m._usar(p + Vector3(0, -1.2, 1.0), ("Rodar a estátua %d" if sombras else "Rodar o espelho %d") % (k + 1), func():
			if _feita:
				return
			_estado_esp[kk] = (_estado_esp[kk] + 1) % 4
			seta.text = setas[_estado_esp[kk]]
			create_tween().tween_property(esp, "rotation:y", esp.rotation.y + PI / 2.0, 0.3)
			_raio(cor if not sombras else Color("2e222f"))
			if _estado_esp == _certo_esp:
				resolver("A %s chega ao selo… e o portão abre-se!" % ("sombra faz uma ponte e a luz" if sombras else "luz")))
	var dica := ""
	for k in n:
		dica += setas[_certo_esp[k]] + " "
	rotulo(c + Vector3(Masmorra.LARGURA / 4.0, 2.4, Masmorra.FUNDO / 2.0 - 1.2), "«%s»" % dica.strip_edges(), Color("c7dcd0"), 28)
	_raio(cor if not sombras else Color("2e222f"))


## Desenha o raio de luz: da fonte até ao primeiro espelho que esteja mal virado.
func _raio(cor: Color) -> void:
	for r in _raios:
		r.queue_free()
	_raios.clear()
	for k in _pontos_esp.size() - 1:
		var a: Vector3 = _pontos_esp[k]
		var b: Vector3 = _pontos_esp[k + 1]
		var seg := MeshInstance3D.new()
		var bm := BoxMesh.new()
		bm.size = Vector3(0.12, 0.12, a.distance_to(b))
		seg.mesh = bm
		seg.material_override = mat(cor, false, true)
		add_child(seg)
		seg.position = (a + b) / 2.0
		seg.look_at_from_position(seg.position, b, Vector3.UP)
		_raios.append(seg)
		if k < _estado_esp.size() and _estado_esp[k] != _certo_esp[k]:
			break


# ------------------------------------------------------------------ cavidades (pedras-coração, moldes, código) ------------------------------------------------------------------

const CONJUNTOS := {
	"coracao": {"pergunta": "Que pedra-coração pões aqui?", "coisas": ["Pedra fria", "Pedra morna", "Pedra quente", "Pedra a escaldar"],
		"pistas": ["há geada à volta", "está morno, como uma mão", "sai um fio de fumo", "a pedra à volta derreteu"], "acabou": "As quatro pedras-coração batem ao mesmo tempo: TUM… TUM…"},
	"moldes": {"pergunta": "Que metal vertes neste molde?", "coisas": ["Espada", "Machado", "Lança", "Martelo"],
		"pistas": ["comprido, fino e com guarda", "curto, com uma lâmina larga", "muito comprido e com bico", "uma cabeça pesada e quadrada"], "acabou": "O metal arrefece nos moldes: as armas dos primeiros Jogadores!"},
	"codigo": {"pergunta": "Que símbolo está fora do sítio?", "coisas": ["o 1.º", "o 2.º", "o 3.º", "o 4.º", "o 5.º"],
		"linhas": ["▲ ▲ ▼ ▲ ▲", "1 2 3 5 5", "A B C D D"], "certas": [2, 3, 4], "acabou": "Três erros corrigidos. O código do Sistema brilha, arrumado."},
}


func _fazer_cavidades() -> void:
	var cj: Dictionary = CONJUNTOS.get(String(mec.get("conjunto", "coracao")), CONJUNTOS.coracao)
	var feitas := {}
	if cj.has("linhas"):   # código: cada linha tem um símbolo errado
		var linhas: Array = cj.linhas
		for k in linhas.size():
			var p := c + Vector3((k - 1) * 6.0, 0, -2.0)
			caixa(p + Vector3(0, 1.0, -0.4), Vector3(4.6, 2.0, 0.2), mat(Color("323353"), false, true))
			var l := rotulo(p + Vector3(0, 1.2, -0.2), linhas[k], Color("30e1b9"), 44)
			var kk := k
			m._usar(p + Vector3(0, 0, 0.8), "Corrigir a linha de código %d" % (k + 1), func():
				if feitas.has(kk):
					return
				var e: int = await escolher(cj.coisas)
				if e < 0:
					return
				if e == int(cj.certas[kk]):
					feitas[kk] = true
					l.modulate = Color("1ebc73")
					if feitas.size() >= cj.linhas.size():
						resolver(cj.acabou)
				else:
					ferir(0.05, p)
					Sistema.mensagem("ERRO. O Sistema dá-te um choque.", "aviso"))
		return
	var ordem := range(cj.coisas.size())
	ordem.shuffle()
	for k in ordem.size():   # cavidade k quer a coisa ordem[k]; a pista diz qual
		var p := c + Vector3(-7.5 + k * 5.0, 0, -2.0)
		caixa(p + Vector3(0, 0.4, 0), Vector3(1.4, 0.8, 1.4), m._mat_parede)
		rotulo(p + Vector3(0, 1.6, 0), cj.pistas[ordem[k]], Color("c7dcd0"), 22)
		var marca := rotulo(p + Vector3(0, 0.9, 0.8), "?", Color("fbff86"), 36)
		var kk := k
		m._usar(p + Vector3(0, 0, 1.1), "Cavidade %d" % (k + 1), func():
			if _feita:
				return
			Sistema.mensagem(cj.pergunta)
			var e: int = await escolher(cj.coisas)
			if e < 0:
				return
			marca.text = String(cj.coisas[e]).get_slice(" ", 1) if " " in cj.coisas[e] else cj.coisas[e]
			if e == ordem[kk]:
				feitas[kk] = true
				marca.modulate = Color("1ebc73")
			else:
				feitas.erase(kk)
				marca.modulate = Color("ea4f36")
			if feitas.size() >= ordem.size():
				resolver(cj.acabou))


# ------------------------------------------------------------------ balança ------------------------------------------------------------------

func _fazer_balanca() -> void:
	var alvo := 20 + _rng.randi_range(0, 30)
	var peso := [0]
	rotulo(c + Vector3(0, 3.4, -Masmorra.FUNDO / 2.0 + 0.6), "PESO: %d" % alvo, Color("f9c22b"), 44)
	var p := c + Vector3(0, 0, -2.0)
	caixa(p + Vector3(0, 0.6, 0), Vector3(0.3, 1.2, 0.3), mat(Color("f9c22b")))
	caixa(p + Vector3(0, 1.25, 0), Vector3(4.0, 0.12, 0.2), mat(Color("f9c22b")))
	var prato := caixa(p + Vector3(-1.8, 1.0, 0), Vector3(1.2, 0.1, 1.2), mat(Color("f79617")))
	var mostra := rotulo(p + Vector3(0, 2.2, 0), "0 / %d" % alvo, Color("fbff86"), 36)
	m._usar(p + Vector3(0, 0, 1.2), "Pôr peso na balança", func():
		if _feita:
			return
		var e: int = await escolher(["Uma moeda (1)", "Um lingote pequeno (5)", "Um lingote (10)", "Tirar tudo"])
		match e:
			0: peso[0] += 1
			1: peso[0] += 5
			2: peso[0] += 10
			3: peso[0] = 0
			_: return
		mostra.text = "%d / %d" % [peso[0], alvo]
		prato.position.y = p.y + 1.0 - clampf(float(peso[0] - alvo) / 20.0, -0.4, 0.4)
		if peso[0] == alvo:
			resolver("A balança fica direitinha. CLIC: a porta do cofre abre-se!")
		elif peso[0] > alvo:
			Sistema.mensagem("Pesado demais! A balança tomba para o teu lado.", "aviso"))


# ------------------------------------------------------------------ lore (espelhos da rainha, estátuas dos Jogadores, o Núcleo) ------------------------------------------------------------------

func _fazer_lore() -> void:
	match String(mec.get("conjunto", "")):
		"rainha":
			var textos := ["No espelho: um reino verde, com um rio e um castelo branco. Não há torre nenhuma no céu.",
				"No espelho: o rei e a rainha a dançar numa praça cheia de gente.",
				"No espelho: o céu a rasgar-se, e uma torre a descer devagar sobre o reino."]
			_ler(textos, "Espelho da Câmara da Rainha", "Os espelhos escurecem. O reino de antes ficou lá dentro.")
		"jogadores":
			var nums := ["Nº 1", "Nº 312", "Nº 1 450", "Nº 6 001", "Nº 8 820", "Nº 9 961", "Nº 9 999", "Nº 10 000"]
			for k in nums.size():
				var p := c + Vector3(-8.0 + (k % 4) * 5.3, 0, 2.0 - (k / 4) * 5.0)
				caixa(p + Vector3(0, 0.6, 0), Vector3(0.6, 1.2, 0.6), mat(Color("9babb2")))
				rotulo(p + Vector3(0, 1.6, 0), nums[k], Color("c7dcd0"), 24)
				var tua: bool = nums[k] == "Nº 10 000"
				m._usar(p + Vector3(0, 0, 0.8), "Olhar para a estátua %s" % nums[k], func():
					if tua:
						resolver("A estátua Nº 10 000 tem o teu corpo… mas ainda não tem cara. O portão abre-se.")
					else:
						Sistema.mensagem("Uma estatueta de um Jogador antigo, com o número gravado. Tem uma cara cansada."))
		_:   # o Núcleo: tocar na esfera quando ela brilha, três vezes
			_nucleo = MeshInstance3D.new()
			var sm := SphereMesh.new()
			sm.radius = 1.4
			sm.height = 2.8
			_nucleo.mesh = sm
			_nucleo.material_override = mat(Color("4d9be6"), false, true)
			_nucleo.position = c + Vector3(0, 1.8, -1.5)
			add_child(_nucleo)
			m._usar(c + Vector3(0, 0, 0.5), "Tocar no Núcleo", func():
				if _feita:
					return
				if fmod(_t, 2.0) > 1.4:   # está a brilhar
					_toques += 1
					Sistema.mensagem("O Núcleo responde ao teu toque. (%d/3)" % _toques)
					if _toques >= 3:
						resolver("O Núcleo pulsa ao teu ritmo… e abre-se um caminho.")
				else:
					ferir(0.06, c)
					Sistema.mensagem("Choque! Toca-lhe quando ele brilha.", "aviso"))


func _ler(textos: Array, nome: String, acabou: String) -> void:
	for k in textos.size():
		var p := c + Vector3((k - 1) * 6.0, 0, -3.0)
		caixa(p + Vector3(0, 1.2, -0.3), Vector3(1.6, 2.4, 0.15), mat(Color("8fd3ff"), false, true))
		var kk := k
		m._usar(p + Vector3(0, 0, 0.8), "%s %d" % [nome, k + 1], func():
			Sistema.mensagem(textos[kk])
			_lidos[kk] = true
			if _lidos.size() >= textos.size():
				resolver(acabou))


# ------------------------------------------------------------------ cada frame ------------------------------------------------------------------

func _process(delta: float) -> void:
	_t += delta
	var lj := local_jogador()
	match String(mec.get("tipo", "")):
		"linhas": _linhas_process(delta, lj)
		"ponte": _ponte_process(delta, lj)
		"agua": _agua_process(delta, lj)
		"pedra": _pedra_process(delta, lj)
		"labirinto": _labirinto_process(delta, lj)
		"vento": _vento_process(delta, lj)
		"ar": _ar_process(delta, lj)
		"despertar": _despertar_process(delta, lj)
		"lore":
			if _nucleo:
				var brilho := fmod(_t, 2.0) > 1.4
				_nucleo.scale = Vector3.ONE * (1.15 if brilho else 1.0)
				(_nucleo.material_override as StandardMaterial3D).albedo_color = Color("8fd3ff") if brilho else Color("4d65b4")
