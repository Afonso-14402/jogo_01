class_name Interior
extends Node3D
## Por dentro dos edifícios (docs/CIDADES.md 1.6; dados/interiores.json): uma divisão sem teto, construída longe
## (por baixo do mapa) quando o herói entra, com chão e paredes em pixel art, os móveis, luzes, quem lá está e a
## porta para sair. Não muda de cena: o andar (ou a cidade) continua igual cá fora.

const ORIGEM := Vector3(0, -400, 0)
const ALTURA_PAREDE := 3.0

static var atual: Interior

var tipo: String = "casa"
var regiao: int = 0
var nome: String = ""
var porta_fora := Vector3.ZERO
var ocupantes: Array = []          # ids de NPCs que estão lá dentro
var _d: Dictionary = {}
var _luzes: Array[OmniLight3D] = []


## Entrar: constrói a divisão, leva o herói lá para dentro e esconde o tempo (chuva, neve) e os bichos do ar.
static func entrar(mundo: Node, tipo_: String, regiao_: int, nome_: String, porta: Vector3, quem: Array = []) -> void:
	if atual != null and is_instance_valid(atual):
		return
	var i := Interior.new()
	i.tipo = tipo_
	i.regiao = regiao_
	i.nome = nome_
	i.porta_fora = porta
	i.ocupantes = quem
	mundo.add_child(i)
	i.global_position = ORIGEM
	atual = i
	Jogo.dentro = true
	var j := mundo.get_tree().get_first_node_in_group("jogador") as Node3D
	if j:
		j.global_position = ORIGEM + Vector3(0, 0.4, i.fundo() / 2.0 - 1.4)
		if "velocity" in j:
			j.velocity = Vector3.ZERO
	var cam := mundo.get_viewport().get_camera_3d()
	if cam and cam.has_method("saltar"):
		cam.saltar()
	Sistema.mensagem(nome_, "andar")


func sair() -> void:
	var j := get_tree().get_first_node_in_group("jogador") as Node3D
	if j:
		j.global_position = porta_fora + Vector3(0, 0.4, 0)
		if "velocity" in j:
			j.velocity = Vector3.ZERO
	Jogo.dentro = false
	atual = null
	var cam := get_viewport().get_camera_3d()
	if cam and cam.has_method("saltar"):
		cam.saltar()
	queue_free()


func largura() -> float:
	return float(_dados().get("tamanho", [8, 6])[0])


func fundo() -> float:
	return float(_dados().get("tamanho", [8, 6])[1])


func _dados() -> Dictionary:
	if _d.is_empty():
		var tipos: Dictionary = Dados.tabela("interiores").get("tipos", {})
		_d = tipos.get(tipo, tipos.get("casa", {}))
	return _d


func _ready() -> void:
	var w := largura()
	var f := fundo()
	var d := _dados()
	var corpo := StaticBody3D.new()
	add_child(corpo)
	# à volta: escuro (não se vê o céu nem o vazio)
	var escuro := StandardMaterial3D.new()
	escuro.albedo_color = Color("2e222f")
	escuro.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
	_caixa(Vector3(0, -0.4, 0), Vector3(w + 80, 0.2, f + 80), escuro, null)
	_caixa(Vector3(0, 6, -f / 2.0 - 3.0), Vector3(w + 80, 14, 1), escuro, null)
	# chão e paredes
	var tipo_chao: String = d.get("chao", "madeira")
	var tipo_parede: String = d.get("parede", "reboco")
	var mr: Array = Dados.tabela("interiores").get("materiais_regiao", {}).get(str(regiao), [])
	if regiao >= 1 and tipo in ["casa", "estalagem"] and mr.size() == 2:   # povoações: os materiais da região
		tipo_chao = mr[0]
		tipo_parede = mr[1]
	var chao := _material("res://arte/interiores/chao_%s.png" % tipo_chao)
	var parede := _material("res://arte/interiores/parede_%s.png" % tipo_parede)
	_caixa(Vector3(0, -0.1, 0), Vector3(w, 0.2, f), chao, corpo)
	_caixa(Vector3(0, ALTURA_PAREDE / 2.0, -f / 2.0 - 0.15), Vector3(w + 0.6, ALTURA_PAREDE, 0.3), parede, corpo)
	_caixa(Vector3(-w / 2.0 - 0.15, ALTURA_PAREDE / 2.0, 0), Vector3(0.3, ALTURA_PAREDE, f), parede, corpo)
	_caixa(Vector3(w / 2.0 + 0.15, ALTURA_PAREDE / 2.0, 0), Vector3(0.3, ALTURA_PAREDE, f), parede, corpo)
	# a parede da frente é baixinha (para se ver lá dentro), com a porta no meio
	var lado := (w - 1.8) / 2.0
	_caixa(Vector3(-w / 2.0 + lado / 2.0, 0.3, f / 2.0 + 0.15), Vector3(lado, 0.6, 0.3), parede, corpo)
	_caixa(Vector3(w / 2.0 - lado / 2.0, 0.3, f / 2.0 + 0.15), Vector3(lado, 0.6, 0.3), parede, corpo)
	_caixa(Vector3(0, 0.3, f / 2.0 + 1.2), Vector3(1.8, 0.6, 0.3), escuro, corpo)   # não se sai pela porta a correr
	# a beira de cima das paredes (madeira escura)
	var beira := StandardMaterial3D.new()
	beira.albedo_color = Color("45293f")
	_caixa(Vector3(0, ALTURA_PAREDE + 0.05, -f / 2.0 - 0.15), Vector3(w + 0.6, 0.1, 0.36), beira, null)
	_moveis(d)
	_pessoas(d)
	_estacoes(d)
	_porta(f)
	# luzes quentes (velas e candeeiros): mais fortes à noite
	for k in 3:
		var l := OmniLight3D.new()
		l.light_color = Color("fbb954")
		l.omni_range = maxf(w, f) * 0.7
		l.position = Vector3((k - 1) * w * 0.3, 2.6, -f * 0.15)
		add_child(l)
		_luzes.append(l)
	_acender()


func _process(_delta: float) -> void:
	if Engine.get_process_frames() % 60 == 0:
		_acender()


func _acender() -> void:
	var noite := Tempo.hora >= 19.0 or Tempo.hora < 6.5
	for l in _luzes:
		l.light_energy = 1.6 if noite else 0.8


func _material(caminho: String) -> StandardMaterial3D:
	var m := StandardMaterial3D.new()
	if ResourceLoader.exists(caminho):
		m.albedo_texture = load(caminho)
	m.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
	m.uv1_triplanar = true
	m.uv1_world_triplanar = true
	m.uv1_scale = Vector3(0.5, 0.5, 0.5)   # 32 px = 2 m (16 px por metro, como o resto)
	return m


func _caixa(p: Vector3, tam: Vector3, mat: Material, corpo: StaticBody3D) -> void:
	var mi := MeshInstance3D.new()
	var b := BoxMesh.new()
	b.size = tam
	mi.mesh = b
	mi.material_override = mat
	mi.position = p
	add_child(mi)
	if corpo:
		var c := CollisionShape3D.new()
		var s := BoxShape3D.new()
		s.size = tam
		c.shape = s
		c.position = p
		corpo.add_child(c)


## Os móveis: os básicos trocam-se pelos da região (nas povoações), e os maiores têm colisão.
func _moveis(d: Dictionary) -> void:
	var regional: Dictionary = Dados.tabela("interiores").get("regional", {})
	var corpo := StaticBody3D.new()
	add_child(corpo)
	for m in d.get("moveis", []):
		var id: String = m[0]
		var p := Vector3(float(m[1]), 0, float(m[2]))
		if id.begins_with("res://"):   # sprite (barris, caixotes)
			if not ResourceLoader.exists(id):
				continue
			var s := Sprite3D.new()
			s.texture = load(id)
			s.pixel_size = 1.0 / Natureza.PPM
			s.billboard = BaseMaterial3D.BILLBOARD_FIXED_Y
			s.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
			s.alpha_cut = SpriteBase3D.ALPHA_CUT_DISCARD
			s.offset.y = s.texture.get_height() / 2.0
			s.position = p
			add_child(s)
			_colisao(corpo, p, Vector3(0.7, 1, 0.7))
			continue
		if regiao >= 1 and regional.has(id):
			var r := "movel_r%02d_%s" % [regiao, regional[id]]
			if ResourceLoader.exists("res://arte/moveis/%s.glb" % r):
				id = r
		var caminho := "res://arte/moveis/%s.glb" % id
		if not ResourceLoader.exists(caminho):
			continue
		var no: Node3D = (load(caminho) as PackedScene).instantiate()
		no.position = p
		no.rotation_degrees.y = float(m[3])
		add_child(no)
		var a := Pecas.caixa(caminho)
		if a.size.y > 0.15:
			var tam := a.size
			if absf(fmod(float(m[3]), 180.0)) > 45.0:
				tam = Vector3(tam.z, tam.y, tam.x)
			_colisao(corpo, p + Vector3(0, tam.y / 2.0, 0), tam * Vector3(0.9, 1, 0.9))


func _colisao(corpo: StaticBody3D, p: Vector3, tam: Vector3) -> void:
	var c := CollisionShape3D.new()
	var s := BoxShape3D.new()
	s.size = tam
	c.shape = s
	c.position = p
	corpo.add_child(c)


func _pessoas(d: Dictionary) -> void:
	var sitios: Array = d.get("pessoas", [])
	for k in ocupantes.size():
		var npc := NPC.new().configurar(ocupantes[k])
		add_child(npc)
		var s: Array = sitios[k % sitios.size()] if not sitios.is_empty() else [0.0, 0.0]
		npc.position = Vector3(float(s[0]) + (k / maxi(1, sitios.size())) * 1.2, 0.3, float(s[1]))


## A tua casa: a cama dorme e grava (grátis) e o fogão cozinha (docs/CIDADES.md, secção 2).
func _estacoes(d: Dictionary) -> void:
	var e: Dictionary = d.get("estacoes", {})
	if e.has("cama"):
		var i := Interagivel.new()
		i.texto = "Dormir (e gravar)"
		i.position = Vector3(float(e.cama[0]), 0, float(e.cama[1]) + 1.2)
		add_child(i)
		i.usado.connect(func(_j):
			Tempo.dormir()
			Jogo.encher()
			Gravar.gravar(Jogo.espaco_gravacao)
			Sistema.mensagem("Dormiste na tua cama. O jogo foi gravado.", "nivel"))
	if e.has("fogao"):
		var i := Interagivel.new()
		i.texto = "Cozinhar"
		i.position = Vector3(float(e.fogao[0]), 0, float(e.fogao[1]) + 1.0)
		add_child(i)
		i.usado.connect(func(_j):
			var ui = get_tree().get_first_node_in_group("crafting_ui")
			if ui:
				ui.abrir_estacao("fogao"))


func _porta(f: float) -> void:
	var tapete := MeshInstance3D.new()
	var q := BoxMesh.new()
	q.size = Vector3(1.6, 0.02, 0.9)
	tapete.mesh = q
	var m := StandardMaterial3D.new()
	m.albedo_color = Color("6e2727")
	tapete.material_override = m
	tapete.position = Vector3(0, 0.01, f / 2.0 - 0.3)
	add_child(tapete)
	var i := Interagivel.new()
	i.texto = "Sair"
	i.position = Vector3(0, 0, f / 2.0 - 0.3)
	add_child(i)
	i.usado.connect(func(_j): sair())
