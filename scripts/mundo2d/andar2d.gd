class_name Andar2D
extends Node2D
## Um andar da torre em 2D (Fase D do OBJETIVO.md; docs/PROGRAMACAO.md, secção 4A), feito com os mesmos dados
## da versão 3D: dados/andares/aNNN.json (a grelha do mapa), dados/natureza.json (texturas do chão e plantas
## em pixel art). Cada célula tem 10×10 m e o chão faz-se em blocos de 2×2 m (5×5 por célula); 1 m = 16 px.
## (Fase D1: chão, colinas, água, plantas, herói e câmara. Monstros, segredos e o resto vêm a seguir.)

const CEL := 10.0
const BLOCO := 2.0
const POR_CEL := 5
const PX := Chao2D.PX
const ALTURA_ROCHA := {2: 4.5, 4: 3.0, 5: 3.0, 6: 2.5, 7: 3.5, 8: 3.0, 10: 3.0}
const RELEVO := ["..", "tt", "\"\"", "**", "▒▒", "^^", "mm"]
const PAREDE := ["TT", "~~", "ww"]   # células onde não se entra (o "##" é parede quando tem altura)

var numero: int = 1
var regiao: int = 1
var dados: Dictionary = {}
var grelha: Array = []
var largura: int = 0
var altura_cel: int = 0
var heroi: Heroi2D
var mundo: Node2D                      # o nó com y-sort onde fica tudo o que se desenha no mundo
var ponto_chegada := Vector2.ZERO      # em metros (x, z)
var ponto_seguro := Vector2.ZERO

var _alturas := PackedFloat32Array()
var _agua := PackedByteArray()
var _rng := RandomNumberGenerator.new()
var _parede: StaticBody2D
var _clareiras: Array[Vector2] = []
var _planta_shader: Shader


func _ready() -> void:
	numero = Jogo.andar_atual
	dados = Dados.tabela("andares/a%03d" % numero)
	if dados.is_empty():
		push_error("Andar %d sem dados" % numero)
		return
	regiao = int(dados.get("regiao", 1))
	grelha = dados.get("grelha", [])
	altura_cel = grelha.size()
	largura = grelha[0].size() if altura_cel > 0 else 0
	_rng.seed = numero * 7919
	RenderingServer.set_default_clear_color(Color(dados.get("ambiente", {}).get("fundo_2d", "#1c2a2a")))
	mundo = Node2D.new()
	mundo.name = "Mundo"
	mundo.y_sort_enabled = true
	add_child(mundo)
	_parede = StaticBody2D.new()
	_parede.collision_layer = 1
	add_child(_parede)
	_calcular_alturas()
	_construir_chao()
	_pontos()
	_construir_celulas()
	_decorar()
	_heroi()
	_luz()
	Sistema.mensagem("Andar %d — %s (2D)" % [numero, dados.get("nome_pt", "")], "andar")


# ------------------------------------------------------------------ mapa ------------------------------------------------------------------

func codigo(cx: int, cy: int) -> String:
	if cy < 0 or cy >= altura_cel or cx < 0 or cx >= largura:
		return "TT"
	return grelha[cy][cx]


func origem() -> Vector2:
	return Vector2(-largura * CEL / 2.0, -altura_cel * CEL / 2.0)


func centro_celula(cx: int, cy: int) -> Vector2:
	return origem() + Vector2((cx + 0.5) * CEL, (cy + 0.5) * CEL)


## A célula do mapa onde está um ponto (em píxeis do mundo), para o mapa e o minimapa.
func celula_de(p_px: Vector2) -> Vector2i:
	var m := (p_px / PX - origem()) / CEL
	return Vector2i(int(floor(m.x)), int(floor(m.y)))


func pos_metros(p_px: Vector2) -> Vector2:
	return p_px / PX


## Altura do chão (m) no bloco de 2 m onde está o ponto (em metros).
func altura_m(p: Vector2) -> float:
	var bw := largura * POR_CEL
	var b := ((p - origem()) / BLOCO).floor()
	if b.x < 0 or b.y < 0 or b.x >= bw or b.y >= altura_cel * POR_CEL:
		return -60.0
	return _alturas[int(b.y) * bw + int(b.x)]


## Quanto sobe no ecrã (px) um boneco que está neste ponto (em píxeis do mundo).
func altura_px(p_px: Vector2) -> float:
	return maxf(altura_m(p_px / PX), -1.0) * Chao2D.SOBE * PX


## Pode-se ir de a para b (em píxeis)? Não se sobe nem se desce a pique, nem se cai no vazio.
func pode_passar(a_px: Vector2, b_px: Vector2) -> bool:
	var ha := altura_m(a_px / PX)
	var hb := altura_m(b_px / PX)
	if hb < -10.0:
		return false
	return absf(hb - ha) <= 0.6


func para_px(m: Vector2) -> Vector2:
	return m * PX


func altura_rocha() -> float:
	return float(ALTURA_ROCHA.get(regiao, 0.0))


func _altura_codigo(c: String) -> float:
	match c:
		"##": return altura_rocha()
		"^^": return 3.0
		"~~", "ww": return -0.8
		",,": return -0.25
		"  ": return -60.0
	return 0.0


## As mesmas alturas da versão 3D (Andar._calcular_alturas): colinas suavizadas em rampas, paredes de rocha com a
## beira comida aos bocados e pequenas ondulações no chão aberto.
func _calcular_alturas() -> void:
	var bw := largura * POR_CEL
	var bh := altura_cel * POR_CEL
	_alturas.resize(bw * bh)
	_agua.resize(bw * bh)
	for bz in bh:
		for bx in bw:
			var c := codigo(bx / POR_CEL, bz / POR_CEL)
			_alturas[bz * bw + bx] = _altura_codigo(c)
			_agua[bz * bw + bx] = 1 if c in ["~~", "ww", ",,"] else 0
	var rocha := func(bx: int, bz: int) -> bool: return codigo(bx / POR_CEL, bz / POR_CEL) == "##" and altura_rocha() > 0.0
	for _passo in 3:
		var nova := _alturas.duplicate()
		for bz in bh:
			for bx in bw:
				var h := _alturas[bz * bw + bx]
				if h < 0.0 or rocha.call(bx, bz):
					continue
				var soma := 0.0
				var n := 0
				for dz in range(-1, 2):
					for dx in range(-1, 2):
						var x := bx + dx
						var z := bz + dz
						if x >= 0 and z >= 0 and x < bw and z < bh and not rocha.call(x, z):
							var v := _alturas[z * bw + x]
							if v >= 0.0:
								soma += v
								n += 1
				nova[bz * bw + bx] = snappedf(soma / max(1, n), 0.25)
		_alturas = nova
	if altura_rocha() > 0.0:
		var bordo := FastNoiseLite.new()
		bordo.seed = numero * 17 + 5
		bordo.frequency = 0.35
		for passo in 2:
			var nova := _alturas.duplicate()
			for bz in bh:
				for bx in bw:
					if _alturas[bz * bw + bx] < altura_rocha() - 0.01 or not rocha.call(bx, bz):
						continue
					var chao := INF
					for d: Vector2i in [Vector2i(1, 0), Vector2i(-1, 0), Vector2i(0, 1), Vector2i(0, -1)]:
						var x: int = bx + d.x
						var z: int = bz + d.y
						if x >= 0 and z >= 0 and x < bw and z < bh and _alturas[z * bw + x] >= 0.0 and _alturas[z * bw + x] < altura_rocha() - 0.01:
							chao = minf(chao, _alturas[z * bw + x])
					if chao != INF and bordo.get_noise_2d(bx * 3.0, bz * 3.0 + passo * 50.0) > (0.05 if passo == 0 else 0.3):
						nova[bz * bw + bx] = chao
			_alturas = nova
		for bz in bh:
			for bx in bw:
				if _alturas[bz * bw + bx] >= altura_rocha() - 0.01:
					_alturas[bz * bw + bx] = altura_rocha() + snappedf(bordo.get_noise_2d(bx * 1.7, bz * 1.7) * 1.6, 0.5)
	# (as pequenas ondulações de 0,25 m da versão 3D não se põem: em 2D viravam riscas no chão)


func _bloco_de_caminho(c: String, cx: int, cy: int, lx: int, lz: int) -> bool:
	if c == "==":
		return true
	if c != "::":
		return false
	if lx >= 1 and lx <= 3 and lz >= 1 and lz <= 3:
		return true
	var liga := func(dx: int, dy: int) -> bool: return codigo(cx + dx, cy + dy) in ["::", "==", "SS", "EE", ">>", "GG", "@@", "BB", "CC"]
	if lx >= 1 and lx <= 3:
		if lz < 1 and liga.call(0, -1):
			return true
		if lz > 3 and liga.call(0, 1):
			return true
	if lz >= 1 and lz <= 3:
		if lx < 1 and liga.call(-1, 0):
			return true
		if lx > 3 and liga.call(1, 0):
			return true
	return false


# ------------------------------------------------------------------ chão ------------------------------------------------------------------

func _construir_chao() -> void:
	var bw := largura * POR_CEL
	var bh := altura_cel * POR_CEL
	var ruido := FastNoiseLite.new()
	ruido.seed = numero
	ruido.frequency = 0.09
	var splat := Image.create(bw, bh, false, Image.FORMAT_RGBA8)
	var alt_img := Image.create(bw, bh, false, Image.FORMAT_RF)
	var masc := Image.create(bw, bh, false, Image.FORMAT_L8)
	for bz in bh:
		for bx in bw:
			var c := codigo(bx / POR_CEL, bz / POR_CEL)
			var h := _alturas[bz * bw + bx]
			alt_img.set_pixel(bx, bz, Color(h, 0, 0))
			if c in ["~~", "ww"]:
				masc.set_pixel(bx, bz, Color(1, 1, 1))
			elif c == ",,":
				masc.set_pixel(bx, bz, Color(0.62, 0.62, 0.62))
			var sp := Color(0, 0, 0, 0)
			var n := ruido.get_noise_2d(bx, bz)
			if c == "##" and altura_rocha() > 0.0 and h > altura_rocha() * 0.6:
				sp.a = 1.0
			if _bloco_de_caminho(c, bx / POR_CEL, bz / POR_CEL, bx % POR_CEL, bz % POR_CEL):
				sp.r = 1.0
			elif c in ["..", "\"\"", "**"] and n < -0.55:
				sp.g = 1.0
			elif n > 0.3 and not c in ["tt", "▒▒"]:
				sp.b = 1.0
			splat.set_pixel(bx, bz, sp)
	var kit: Dictionary = Dados.tabela("kits").get(str(regiao), {})
	var agua := Color(kit.get("agua", "#0b8a8f")) if String(kit.get("agua", "#")).begins_with("#") else Color("0b8a8f")
	var mat := Chao2D.material(regiao, splat, alt_img, masc, origem(), Vector2(largura * CEL, altura_cel * CEL), agua, altura_rocha())
	for fila in Chao2D.filas(_alturas, _agua, bw, bh, origem(), BLOCO, mat):
		mundo.add_child(fila)
	# as paredes do mapa (bordas, água funda e, sem altura, as rochas "##") e a beira do mundo
	for cy in altura_cel:
		for cx in largura:
			var c := codigo(cx, cy)
			if c in PAREDE or (c == "##" and altura_rocha() <= 0.0):
				_caixa(centro_celula(cx, cy), Vector2(CEL, CEL))
	var o := origem()
	var t := Vector2(largura * CEL, altura_cel * CEL)
	for lado in [[o + Vector2(t.x / 2, -1), Vector2(t.x, 2)], [o + Vector2(t.x / 2, t.y + 1), Vector2(t.x, 2)],
			[o + Vector2(-1, t.y / 2), Vector2(2, t.y)], [o + Vector2(t.x + 1, t.y / 2), Vector2(2, t.y)]]:
		_caixa(lado[0], lado[1])


func _caixa(centro_m: Vector2, tam_m: Vector2) -> void:
	var f := CollisionShape2D.new()
	var r := RectangleShape2D.new()
	r.size = tam_m * PX
	f.shape = r
	f.position = centro_m * PX
	_parede.add_child(f)


func _circulo(p_m: Vector2, raio_m: float) -> void:
	var f := CollisionShape2D.new()
	var c := CircleShape2D.new()
	c.radius = raio_m * PX
	f.shape = c
	f.position = p_m * PX
	_parede.add_child(f)


# ------------------------------------------------------------------ pontos ------------------------------------------------------------------

func _pontos() -> void:
	for cy in altura_cel:
		for cx in largura:
			match codigo(cx, cy):
				"EE":
					ponto_chegada = centro_celula(cx, cy) + Vector2(0, 3)
					_clareiras.append(centro_celula(cx, cy))
				"SS":
					ponto_seguro = centro_celula(cx, cy)
					_clareiras.append(ponto_seguro)
					_planta_em(_kit_sprite("fogueira"), ponto_seguro, 1.0)
	if ponto_chegada == Vector2.ZERO:
		ponto_chegada = ponto_seguro + Vector2(0, 3.5) if ponto_seguro != Vector2.ZERO else _primeira_livre()
	for pt in dados.get("pontos", []):   # o sítio onde o herói acorda (andar 1)
		if pt.marca == "AA" and numero == 1:
			_clareiras.append(centro_celula(int(pt.x), int(pt.y)))


func _primeira_livre() -> Vector2:
	for cy in range(altura_cel - 1, -1, -1):
		for cx in largura:
			if codigo(cx, cy) == "..":
				return centro_celula(cx, cy)
	return Vector2.ZERO


func _kit_sprite(nome: String) -> String:
	for grupo in ["objetos", "detalhes", "povoacao"]:
		for p in Natureza.plantas(regiao, grupo):
			if String(p).get_file().begins_with(nome):
				return p
	return ""


## Uma árvore aqui taparia a chegada / a Zona Segura?
func _na_clareira(p: Vector2) -> bool:
	for k in _clareiras:
		var d := p - k
		if d.length() < 5.5 or (d.y > 0.0 and d.y < 7.0 and absf(d.x) < 4.5):
			return true
	return false


# ------------------------------------------------------------------ plantas ------------------------------------------------------------------

func _ponto(cx: int, cy: int, margem: float = 1.2) -> Vector2:
	return centro_celula(cx, cy) + Vector2(_rng.randf_range(-CEL / 2 + margem, CEL / 2 - margem), _rng.randf_range(-CEL / 2 + margem, CEL / 2 - margem))


func _construir_celulas() -> void:
	var arvores := Natureza.plantas(regiao, "arvore")
	var limite := Natureza.plantas(regiao, "limite")
	if limite.is_empty():
		limite = arvores
	var mato := Natureza.plantas(regiao, "mato")
	var rochas := Natureza.plantas(regiao, "rocha")
	var erva := Natureza.plantas(regiao, "erva")
	var flores := Natureza.plantas(regiao, "flores")
	for cy in altura_cel:
		for cx in largura:
			match codigo(cx, cy):
				"TT":
					for i in 7:
						var p := _ponto(cx, cy, 0.6)
						if _na_clareira(p):
							_plantar(mato, p, 1.0, 1.3)
						else:
							_plantar(limite, p, 1.0, 1.4)
				"tt", "▒▒":
					for i in _rng.randi_range(4, 6):
						var p := _ponto(cx, cy)
						if _na_clareira(p):
							_plantar(mato, p, 0.9, 1.2)
						elif _plantar(arvores, p, 0.85, 1.25):
							_circulo(p, 0.55)
					for i in _rng.randi_range(1, 3):
						_plantar(mato, _ponto(cx, cy), 0.8, 1.1)
				"##":
					if altura_rocha() > 0.0:
						for i in 3:
							_plantar(rochas, _ponto(cx, cy), 0.9, 1.4)
					else:
						for i in 6:
							_plantar(rochas, _ponto(cx, cy, 0.8), 1.0, 1.8)
				"\"\"":
					for i in 40:
						_plantar(erva, _ponto(cx, cy, 0.4), 1.0, 1.5)
				"**":
					for i in 10:
						_plantar(flores, _ponto(cx, cy, 0.6), 0.9, 1.2)
				"mm":
					for i in 4:
						var p := _ponto(cx, cy)
						if _plantar(mato, p, 1.0, 1.3):
							_circulo(p, 0.45)


## A erva, as flores, as pedrinhas, os arbustos e uma árvore solta de vez em quando no chão aberto.
func _decorar() -> void:
	var erva := Natureza.plantas(regiao, "erva")
	var flores := Natureza.plantas(regiao, "flores")
	var pedras := Natureza.plantas(regiao, "pedras")
	var mato := Natureza.plantas(regiao, "mato")
	var arvores := Natureza.plantas(regiao, "arvore")
	var ruido := FastNoiseLite.new()
	ruido.seed = numero * 3 + 1
	ruido.frequency = 0.18
	for cy in altura_cel:
		for cx in largura:
			var c := codigo(cx, cy)
			if not c in ["..", "::", "\"\"", "**", "SS", "EE", "GG", "$$", "??", "!!", "PP"]:
				continue
			var n := ruido.get_noise_2d(cx, cy)
			for i in (14 if n > 0.2 else 7):
				_plantar(erva, _ponto(cx, cy, 0.3), 0.6, 1.1)
			if n > -0.1:
				for i in 5:
					_plantar(flores, _ponto(cx, cy, 0.4), 0.7, 1.0)
			for i in 2:
				_plantar(pedras, _ponto(cx, cy, 0.4), 0.6, 1.0)
			if c == ".." and _rng.randf() < 0.35:
				var p := _ponto(cx, cy)
				if _plantar(mato, p, 0.8, 1.2):
					_circulo(p, 0.45)
			if c == ".." and _rng.randf() < 0.1:
				var p := _ponto(cx, cy)
				if not _na_clareira(p) and _plantar(arvores, p, 0.8, 1.1):
					_circulo(p, 0.55)


## Põe uma planta de uma lista (sprites de dados/natureza.json) em p (metros); devolve se pôs.
func _plantar(lista: Array, p: Vector2, e0: float, e1: float) -> bool:
	if lista.is_empty() or altura_m(p) < -0.5:
		return false
	var caminho: String = lista[_rng.randi() % lista.size()]
	_planta_em(caminho, p, _rng.randf_range(e0, e1))
	return true


func _planta_em(caminho: String, p: Vector2, escala: float) -> void:
	if caminho == "" or not ResourceLoader.exists(caminho):
		return
	var tex: Texture2D = load(caminho)
	var no := Node2D.new()
	no.position = p * PX
	var s := Sprite2D.new()
	s.texture = tex
	s.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	s.offset = Vector2(0, -tex.get_height() / 2.0)
	s.position.y = -maxf(altura_m(p), -1.0) * Chao2D.SOBE * PX
	s.scale = Vector2(escala * (-1.0 if _rng.randf() < 0.5 else 1.0), escala)
	s.material = _material_planta(caminho, tex)
	no.add_child(s)
	mundo.add_child(no)


var _mats_planta: Dictionary = {}


## Abanar ao vento (só as plantas) e, se tapar o herói, abrir uma janela redonda à volta dele.
func _material_planta(caminho: String, tex: Texture2D) -> ShaderMaterial:
	if _mats_planta.has(caminho):
		return _mats_planta[caminho]
	if _planta_shader == null:
		_planta_shader = Shader.new()
		_planta_shader.code = """
shader_type canvas_item;
uniform float vento = 1.0;
uniform float alto = 32.0;
uniform float tapa = 0.0;
global uniform vec2 jogador2d;
varying vec2 base;
varying vec2 mundo_px;
float bayer(vec2 p) {
	ivec2 i = ivec2(mod(p, 4.0));
	int m[16] = int[](0, 8, 2, 10, 12, 4, 14, 6, 3, 11, 1, 9, 15, 7, 13, 5);
	return float(m[i.y * 4 + i.x]) / 16.0;
}
void vertex() {
	base = (MODEL_MATRIX * vec4(0.0, 0.0, 0.0, 1.0)).xy;
	float fase = base.x * 0.023 + base.y * 0.014;
	float h = clamp(1.0 - UV.y, 0.0, 1.0);
	float s = sin(TIME * 1.5 + fase) * 0.65 + sin(TIME * 2.6 + fase * 1.7) * 0.25 + sin(TIME * 0.4 + fase * 0.3) * 0.5;
	VERTEX.x += round(s * vento * h * h * 0.06 * alto);
	mundo_px = (MODEL_MATRIX * vec4(VERTEX, 0.0, 1.0)).xy;
}
void fragment() {
	vec4 c = texture(TEXTURE, UV);
	if (tapa > 0.5 && base.y > jogador2d.y + 10.0) {
		float d = length((mundo_px - jogador2d) * vec2(1.0, 0.8));
		float k = clamp((d - 18.0) / 16.0, 0.0, 1.0);
		if (bayer(floor(UV * vec2(textureSize(TEXTURE, 0)))) >= k) c.a = 0.0;
	}
	COLOR = c;
}
"""
	var m := ShaderMaterial.new()
	m.shader = _planta_shader
	var nome := caminho.get_file().get_basename()
	var vento := 0.0
	for k in ["tufo", "flor", "junco", "erva", "alga", "feto"]:
		if nome.begins_with(k):
			vento = 1.6
	for k in ["carvalho", "pinheiro", "betula", "selva", "palmeira", "mangue", "acacia", "arvore_nuvem", "arbusto"]:
		if nome.begins_with(k):
			vento = 1.0
	m.set_shader_parameter("vento", vento)
	m.set_shader_parameter("alto", float(tex.get_height()))
	m.set_shader_parameter("tapa", 1.0 if tex.get_height() > 26 else 0.0)
	_mats_planta[caminho] = m
	return m


# ------------------------------------------------------------------ herói e luz ------------------------------------------------------------------

func _heroi() -> void:
	heroi = Heroi2D.new()
	heroi.mundo = self
	heroi.position = ponto_chegada * PX
	mundo.add_child(heroi)
	add_child(preload("res://cenas/ui/hud.tscn").instantiate())


## A cor da hora do dia (por cima de tudo): manhã quente, meio-dia claro, noite azul.
func _luz() -> void:
	var cm := CanvasModulate.new()
	cm.name = "LuzDoDia"
	add_child(cm)
	set_process(true)


func _process(_delta: float) -> void:
	var cm := get_node_or_null("LuzDoDia") as CanvasModulate
	if cm == null:
		return
	var h := Tempo.hora
	var f := CicloDia.fator_dia(h)
	var por := clampf(1.0 - absf(h - 19.0), 0.0, 1.0) + clampf(1.0 - absf(h - 5.8) * 1.5, 0.0, 1.0)
	var c := Color("5a6aa8").lerp(Color.WHITE, f).lerp(Color("ffd2b0"), por * 0.35)
	if regiao == 2:
		c = Color("5c5a78")
	cm.color = c
	if heroi:
		RenderingServer.global_shader_parameter_set("jogador2d", heroi.global_position + Vector2(0, -heroi.altura_vista() - 14.0))
