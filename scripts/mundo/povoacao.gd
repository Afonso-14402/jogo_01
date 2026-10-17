class_name Povoacao
extends Node3D
## Uma povoação dentro da torre (dados/povoacoes.json, docs/CIDADES.md secção 4): as pessoas (NPCs com falas,
## loja, quarto e forja), a fogueira do meio, as luzes das casas à noite, a placa com o nome e a mensagem ao chegar.
## Os edifícios e a decoração põem-se no andar (andar.gd, _construir_povoacao), porque vão nos MultiMesh.

var dados: Dictionary = {}
var mundo: Node
var centro := Vector3.ZERO
var casas: Array[Vector3] = []      # onde ficam os edifícios (as pessoas vivem à porta)
var casas_info: Array = []          # [{pos, raio, peca}] dos edifícios (para as portas)

var _npcs: Array[NPC] = []
var _casa_de: Dictionary = {}        # NPC -> Vector3
var _luzes: Array[OmniLight3D] = []
var _gente: Array[Transeunte] = []
var _fogo: CPUParticles3D
var _t: float = 0.0
var _chegou: bool = false
var _por_aparecer: Array[int] = []


func _por_npc(i: int) -> NPC:
	var n: Dictionary = dados.get("npcs", [])[i]
	var npc := NPC.new().configurar(n.id)
	add_child(npc)
	var casa: Vector3 = casas[i % casas.size()] if not casas.is_empty() else centro
	var porta := casa + Vector3(randf_range(-1.5, 1.5), 0, 3.2)
	npc.global_position = _no_chao(porta + Vector3(0, 0.5, 0))
	_npcs.append(npc)
	_casa_de[npc] = porta
	if "fantasma" in String(dados.get("id", "")):   # fantasmas: azulados
		for sp in npc.find_children("*", "SpriteBase3D", true, false):
			(sp as SpriteBase3D).modulate = Color(0.7, 0.85, 1.0)
	return npc


func _ready() -> void:
	var lista: Array = dados.get("npcs", [])
	for i in lista.size():
		var n: Dictionary = lista[i]
		if not Condicoes.avaliar(String(Dados.obter("npcs_povoacoes", n.id).get("cond", ""))):
			_por_aparecer.append(i)   # ex.: os fantasmas da forja só aparecem com as fornalhas acesas
			continue
		_por_npc(i)
	_portas()
	_fogueira()
	_placa()
	for i in int(dados.get("transeuntes", 3)):   # gente na rua (docs/CIDADES.md 4.1)
		var t := Transeunte.new()
		t.lugar = "r%02d" % int(dados.get("regiao", 1))
		t.pontos = _ponto_rua
		add_child(t)
		t.global_position = _no_chao(_ponto_rua() + Vector3(0, 0.5, 0))
		_gente.append(t)
	for c in casas:   # uma luz quente à porta de cada casa (acende ao fim do dia)
		var l := OmniLight3D.new()
		l.light_color = Color("fbb954")
		l.omni_range = 6.0
		l.shadow_enabled = false
		add_child(l)
		l.global_position = _no_chao(c + Vector3(0, 1.8, 2.6))
		_luzes.append(l)
	_atualizar(true)


func _no_chao(p: Vector3) -> Vector3:
	if mundo and mundo.has_method("altura_em"):
		p.y = maxf(p.y, mundo.altura_em(p.x, p.z) + 0.05)
	return p


func _noite() -> bool:
	return Tempo.hora >= 19.0 or Tempo.hora < 6.5


## O Mercado Fantasma só existe à noite (docs/regioes/r08, secção 7.1).
func _so_noite() -> bool:
	return dados.get("id", "") == "mercado_fantasma"


func _process(delta: float) -> void:
	_t -= delta
	if _t <= 0.0:
		_t = 1.0
		_atualizar(false)
		for i in _por_aparecer.duplicate():
			var n: Dictionary = dados.get("npcs", [])[i]
			if Condicoes.avaliar(String(Dados.obter("npcs_povoacoes", n.id).get("cond", ""))):
				_por_aparecer.erase(i)
				var npc := _por_npc(i)
				npc.scale = Vector3.ONE * 0.01
				create_tween().tween_property(npc, "scale", Vector3.ONE, 1.2).set_trans(Tween.TRANS_BACK)
	var j := get_tree().get_first_node_in_group("jogador") as Node3D
	if j and not _chegou and Vector2(j.global_position.x - centro.x, j.global_position.z - centro.z).length() < 18.0:
		_chegou = true
		Sistema.mensagem("Chegaste a %s." % dados.get("nome_pt", ""), "andar")


## De segundo a segundo: luzes, quem está na rua e passeios curtos à volta de casa.
func _atualizar(inicio: bool) -> void:
	var noite := _noite()
	for l in _luzes:
		l.light_energy = 1.4 if noite else 0.0
	if _fogo:
		_fogo.get_parent().get_node("Luz").light_energy = 2.2 if noite else 0.6
	for npc in _npcs:
		if not is_instance_valid(npc):
			continue
		var ve := (noite if _so_noite() else true)
		for t in _gente:
			t.visible = ve and (not noite or t.get_index() % 2 == 0)   # à noite há menos gente na rua
			t.process_mode = Node.PROCESS_MODE_INHERIT if t.visible else Node.PROCESS_MODE_DISABLED
		npc.visible = ve
		npc.process_mode = Node.PROCESS_MODE_INHERIT if ve else Node.PROCESS_MODE_DISABLED
		if not ve or inicio:
			continue
		var casa: Vector3 = _casa_de[npc]
		var ui := get_tree().get_first_node_in_group("dialogo_ui")
		if ui and ui.get("ocupado"):
			continue
		# de noite ficam à porta; de dia dão uma volta pela povoação (às vezes até à fogueira)
		if randf() < 0.12:
			var alvo := casa
			if not noite:
				alvo = (centro + Vector3(randf_range(-2.5, 2.5), 0, randf_range(1.5, 3.5))) if randf() < 0.3 else \
						casa + Vector3(randf_range(-4.0, 4.0), 0, randf_range(-1.0, 4.0))
			npc.ir_para(_no_chao(alvo))


## [E] Entrar em cada edifício (docs/CIDADES.md 1.6): cada casa é de um NPC da povoação (que está lá dentro);
## as estalagens, tabernas e forjas têm o seu tipo de divisão e os móveis são os da região.
func _portas() -> void:
	var lista: Array = dados.get("npcs", [])
	var regras: Array = Dados.tabela("interiores").get("povoacao", [])
	for k in casas_info.size():
		var c: Dictionary = casas_info[k]
		var peca: String = String(c.peca).get_file().get_basename()
		var tipo := "casa"
		for r in regras:
			if String(r[0]) in peca:
				tipo = r[1]
		var donos: Array = []
		for i in lista.size():
			if i % casas_info.size() == k:
				donos.append(lista[i].id)
		var nome := "%s de %s" % [{"estalagem": "Estalagem", "taberna": "Taberna", "forja": "Forja", "igreja": "Templo",
				"biblioteca": "Observatório", "camara": "Palácio"}.get(tipo, "Casa"), dados.get("nome_pt", "")]
		if tipo == "casa" and not donos.is_empty():
			nome = "Casa de %s" % Dados.obter("npcs_povoacoes", donos[0]).get("nome_pt", donos[0])
		var porta := _no_chao(c.pos + Vector3(0, 0, float(c.raio) + 0.5))
		var i := Interagivel.new()
		i.texto = "Entrar: %s" % nome
		add_child(i)
		i.global_position = porta
		var regiao := int(dados.get("regiao", 1))
		i.usado.connect(func(_j): Interior.entrar(mundo, tipo, regiao, nome, porta + Vector3(0, 0, 1.0), donos))


## Um sítio para a gente na rua ir: perto da fogueira ou à porta de uma casa.
func _ponto_rua() -> Vector3:
	var base: Vector3 = centro if casas.is_empty() or randf() < 0.35 else casas.pick_random() + Vector3(0, 0, 3.0)
	return _no_chao(base + Vector3(randf_range(-3.5, 3.5), 0, randf_range(-2.0, 3.5)))


## A fogueira no meio da povoação: lume aceso, fumo e luz (mais forte à noite).
func _fogueira() -> void:
	var base := Node3D.new()
	add_child(base)
	base.global_position = _no_chao(centro)
	var pedras := "res://arte/regioes/r01_floresta/natureza/fogueira_apagada.png"
	if ResourceLoader.exists(pedras):
		var s := Sprite3D.new()
		s.texture = load(pedras)
		s.pixel_size = 1.0 / Natureza.PPM
		s.billboard = BaseMaterial3D.BILLBOARD_FIXED_Y
		s.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
		s.alpha_cut = SpriteBase3D.ALPHA_CUT_DISCARD
		s.offset.y = s.texture.get_height() / 2.0
		base.add_child(s)
	# a chama: desenho animado (arte/efeitos/fogueira_chama.png, 6 frames) que não apanha sombra nem escuro
	var tira: Texture2D = load("res://arte/efeitos/fogueira_chama.png")
	var sf := SpriteFrames.new()
	sf.set_animation_speed("default", 10)
	for i in 6:
		var at := AtlasTexture.new()
		at.atlas = tira
		at.region = Rect2(i * 20, 0, 20, 26)
		sf.add_frame("default", at)
	var ch := AnimatedSprite3D.new()
	ch.sprite_frames = sf
	ch.pixel_size = 1.0 / Natureza.PPM
	ch.billboard = BaseMaterial3D.BILLBOARD_FIXED_Y
	ch.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
	ch.alpha_cut = SpriteBase3D.ALPHA_CUT_DISCARD
	ch.shaded = false
	ch.offset.y = 13
	ch.position.y = 0.1
	base.add_child(ch)
	ch.play()
	_fogo = _chamas(Color("fbb954"), Color("ea4f36", 0.0), 8, 1.2, Vector3(0, 1.4, 0), 0.07)   # faúlhas
	base.add_child(_fogo)
	_fogo.position.y = 1.0
	var fumo := _chamas(Color(0.62, 0.6, 0.66, 0.5), Color(0.62, 0.6, 0.66, 0.0), 10, 3.5, Vector3(0.25, 0.9, 0), 0.3)
	base.add_child(fumo)
	fumo.position.y = 1.2
	var luz := OmniLight3D.new()
	luz.name = "Luz"
	luz.light_color = Color("f79617")
	luz.omni_range = 9.0
	luz.position.y = 1.0
	base.add_child(luz)
	var col := StaticBody3D.new()
	var f := CollisionShape3D.new()
	var c := CylinderShape3D.new()
	c.radius = 0.8
	c.height = 1.0
	f.shape = c
	col.add_child(f)
	base.add_child(col)


func _chamas(c0: Color, c1: Color, n: int, vida: float, gravidade: Vector3, tamanho: float) -> CPUParticles3D:
	var p := CPUParticles3D.new()
	p.amount = n
	p.lifetime = vida
	p.emission_shape = CPUParticles3D.EMISSION_SHAPE_SPHERE
	p.emission_sphere_radius = 0.25
	p.gravity = gravidade
	p.direction = Vector3.UP
	p.spread = 15.0
	p.initial_velocity_min = 0.2
	p.initial_velocity_max = 0.6
	var q := QuadMesh.new()
	q.size = Vector2(tamanho, tamanho)
	var m := StandardMaterial3D.new()
	m.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	m.billboard_mode = BaseMaterial3D.BILLBOARD_PARTICLES
	m.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
	m.vertex_color_use_as_albedo = true
	m.albedo_color = Color.WHITE
	q.material = m
	p.mesh = q
	var g := Gradient.new()
	g.set_color(0, c0)
	g.set_color(1, c1)
	p.color_ramp = g
	return p


## Placa de madeira à entrada, com o nome da povoação escrito.
func _placa() -> void:
	var caminho := "res://arte/regioes/r01_floresta/natureza/placa.png"
	var p := _no_chao(centro + Vector3(4.5, 0, 5.0))
	if ResourceLoader.exists(caminho):
		var s := Sprite3D.new()
		s.texture = load(caminho)
		s.pixel_size = 1.0 / Natureza.PPM
		s.billboard = BaseMaterial3D.BILLBOARD_FIXED_Y
		s.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
		s.alpha_cut = SpriteBase3D.ALPHA_CUT_DISCARD
		s.offset.y = s.texture.get_height() / 2.0
		add_child(s)
		s.global_position = p
	var l := Label3D.new()
	l.text = dados.get("nome_pt", "")
	l.font_size = 48
	l.pixel_size = 0.0075
	l.outline_size = 12
	l.modulate = Color("fbff86")
	l.billboard = BaseMaterial3D.BILLBOARD_FIXED_Y
	l.no_depth_test = false
	add_child(l)
	l.global_position = p + Vector3(0, 2.1, 0)
