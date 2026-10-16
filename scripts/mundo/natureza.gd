class_name Natureza
## A natureza dos andares em pixel art (ferramentas/arte/natureza.py → dados/natureza.json):
## - o chão: um shader que mistura 4 texturas (base, variante, terra, caminho) com bordas recortadas,
##   manchas grandes de cor e sombras de nuvens a passar;
## - as plantas: sprites de frente para a câmara (como os bonecos) que abanam com o vento e ficam
##   transparentes quando o jogador passa por trás delas.

const PPM := 16.0   # píxeis por metro

static var _shader_chao: Shader
static var _shader_planta: Shader
static var _ruido: NoiseTexture2D
static var _cache_planta: Dictionary = {}


## Os grupos do kit que a natureza em sprite substitui (natureza.json → kits.json).
static func aplicar(kit: Dictionary, regiao: int) -> Dictionary:
	var n: Dictionary = Dados.tabela("natureza").get(str(regiao), {})
	var plantas: Dictionary = n.get("plantas", {})
	if plantas.is_empty():
		return kit
	var k := kit.duplicate()
	for grupo in plantas:
		k[{"erva": "erva_alta"}.get(grupo, grupo)] = plantas[grupo]
	return k


static func e_sprite(caminho: Variant) -> bool:
	return caminho is String and (caminho as String).ends_with(".png")


## As plantas de um grupo (arvore, limite, mato, erva, flores, rocha, pedras) de uma região.
static func plantas(regiao: int, grupo: String) -> Array:
	return Dados.tabela("natureza").get(str(regiao), {}).get("plantas", {}).get(grupo, [])


static func ruido() -> NoiseTexture2D:
	if _ruido == null:
		var f := FastNoiseLite.new()
		f.frequency = 0.012
		f.fractal_octaves = 3
		_ruido = NoiseTexture2D.new()
		_ruido.width = 256
		_ruido.height = 256
		_ruido.seamless = true
		_ruido.noise = f
	return _ruido


## Material do chão de uma região. splat: 1 píxel por bloco de 2 m (R = caminho, G = terra, B = variante).
static func material_chao(regiao: int, splat: Texture2D, origem: Vector2, tamanho: Vector2, trocar: Dictionary = {}) -> ShaderMaterial:
	if _shader_chao == null:
		_shader_chao = Shader.new()
		_shader_chao.code = """
shader_type spatial;
render_mode cull_back, diffuse_lambert, specular_disabled;
uniform sampler2D t_base : source_color, filter_nearest, repeat_enable;
uniform sampler2D t_var : source_color, filter_nearest, repeat_enable;
uniform sampler2D t_terra : source_color, filter_nearest, repeat_enable;
uniform sampler2D t_caminho : source_color, filter_nearest, repeat_enable;
uniform sampler2D splat : filter_linear;
uniform sampler2D ruido : filter_linear, repeat_enable;
uniform vec2 origem;
uniform vec2 tamanho;
uniform float nuvens = 1.0;
uniform float fora_escuro = 0.78;
varying vec3 mundo;
varying float de_lado;

float bayer(vec2 p) {
	ivec2 i = ivec2(mod(p, 4.0));
	int m[16] = int[](0, 8, 2, 10, 12, 4, 14, 6, 3, 11, 1, 9, 15, 7, 13, 5);
	return float(m[i.y * 4 + i.x]) / 16.0;
}

void vertex() {
	mundo = (MODEL_MATRIX * vec4(VERTEX, 1.0)).xyz;
	de_lado = 1.0 - clamp((MODEL_MATRIX * vec4(NORMAL, 0.0)).y, 0.0, 1.0);
}

void fragment() {
	vec2 px = floor(mundo.xz * 16.0);          // o píxel da textura (16 por metro)
	vec2 w = (px + 0.5) / 16.0;
	vec2 uv = w / 4.0;                          // texturas de 64 px = 4 m
	vec2 su = (w - origem) / tamanho;
	vec3 s = texture(splat, su).rgb;
	float n = texture(ruido, w * 0.09).r - 0.5;
	float d = (bayer(px) - 0.5) * 0.12;
	vec3 c = texture(t_base, uv).rgb;
	if (s.b + n * 0.9 + d > 0.5) c = texture(t_var, uv).rgb;
	if (s.g + n * 0.8 + d > 0.5) c = texture(t_terra, uv).rgb;
	if (s.r + n * 0.45 + d > 0.5) c = texture(t_caminho, uv).rgb;
	// manchas grandes: mais claro ao sol, mais frio e escuro nas zonas húmidas (em degraus, pixel art)
	float m = texture(ruido, w * 0.018 + 0.31).r;
	c *= 0.86 + floor(clamp(m * 1.6 - 0.3, 0.0, 1.0) * 3.0 + bayer(px + 2.0) * 0.9) * 0.07;
	// sombras das nuvens a passar
	float nv = texture(ruido, w * 0.012 + TIME * vec2(0.0035, 0.0016)).r;
	c *= 1.0 - nuvens * 0.2 * step(0.6 + bayer(px) * 0.05, nv);
	// fora do mapa: mais escuro (a floresta à volta fica em segundo plano)
	if (su.x < 0.0 || su.y < 0.0 || su.x > 1.0 || su.y > 1.0) c *= fora_escuro;
	c *= 1.0 - de_lado * 0.35;   // os lados dos degraus mais escuros (sombra)
	ALBEDO = c;
}
"""
	var n: Dictionary = Dados.tabela("natureza").get(str(regiao), {})
	var ch: Dictionary = n.get("chao", {})
	var m := ShaderMaterial.new()
	m.shader = _shader_chao
	for k in ["base", "variante", "terra", "caminho"]:
		var uni: String = {"base": "t_base", "variante": "t_var", "terra": "t_terra", "caminho": "t_caminho"}[k]
		m.set_shader_parameter(uni, load(ch.get(trocar.get(k, k), ch.get("base", ""))))
	m.set_shader_parameter("splat", splat)
	m.set_shader_parameter("ruido", ruido())
	m.set_shader_parameter("origem", origem)
	m.set_shader_parameter("tamanho", tamanho)
	m.set_shader_parameter("nuvens", 0.0 if regiao in [2, 10] else 1.0)
	return m


## Malha (quad com a base na origem) + material de uma planta em sprite.
static func malha_planta(caminho: String) -> QuadMesh:
	if _cache_planta.has(caminho):
		return _cache_planta[caminho]
	var tex: Texture2D = load(caminho)
	var tam := Vector2(tex.get_width(), tex.get_height()) / PPM
	var q := QuadMesh.new()
	q.size = tam
	q.center_offset = Vector3(0, tam.y / 2.0, 0)
	q.material = _material_planta(tex, tam, caminho)
	_cache_planta[caminho] = q
	return q


static func _material_planta(tex: Texture2D, tam: Vector2, caminho: String) -> ShaderMaterial:
	if _shader_planta == null:
		_shader_planta = Shader.new()
		_shader_planta.code = """
shader_type spatial;
render_mode cull_disabled, diffuse_lambert, specular_disabled;
uniform sampler2D tex : source_color, filter_nearest;
uniform float vento = 1.0;
uniform vec2 tamanho = vec2(4.0, 5.0);
uniform float tapa = 1.0;
global uniform vec3 jogador_pos;
varying float transparente;

float bayer(vec2 p) {
	ivec2 i = ivec2(mod(p, 4.0));
	int m[16] = int[](0, 8, 2, 10, 12, 4, 14, 6, 3, 11, 1, 9, 15, 7, 13, 5);
	return float(m[i.y * 4 + i.x]) / 16.0;
}

void vertex() {
	vec3 o = MODEL_MATRIX[3].xyz;
	float fase = o.x * 0.37 + o.z * 0.23;
	float h = clamp(VERTEX.y / tamanho.y, 0.0, 1.0);
	float s = sin(TIME * 1.5 + fase) * 0.65 + sin(TIME * 2.6 + fase * 1.7) * 0.25 + sin(TIME * 0.4 + fase * 0.3) * 0.5;
	// o vento dobra mais a parte de cima; o deslocamento anda aos píxeis (fica pixel art)
	VERTEX.x += round(s * vento * h * h * 0.06 * tamanho.y * 16.0) / 16.0;
	NORMAL = normalize(vec3(0.0, 1.0, 0.55));
	// o jogador está escondido atrás desta planta? (ela fica mais perto da câmara, que olha para -Z)
	vec3 d = jogador_pos - o;
	transparente = (tapa > 0.5 && d.z < 0.2 && d.z > -tamanho.y * 1.45 && abs(d.x) < tamanho.x * 0.45 + 0.3 && d.y < tamanho.y) ? 1.0 : 0.0;
}

void fragment() {
	vec4 c = texture(tex, UV);
	if (c.a < 0.5) discard;
	if (transparente > 0.5 && bayer(FRAGCOORD.xy / 2.0) < 0.62) discard;
	ALBEDO = c.rgb;
}
"""
	var m := ShaderMaterial.new()
	m.shader = _shader_planta
	m.set_shader_parameter("tex", tex)
	m.set_shader_parameter("tamanho", tam)
	# só as plantas abanam: erva e flores mais, árvores e arbustos um pouco, árvores mortas e cactos quase nada;
	# objetos (pilares, campas, cercas, barris...) e rochas ficam quietos
	var nome := caminho.get_file().get_basename()
	var vento := 0.0
	for k in ["tufo", "flor", "junco", "erva", "alga", "feto"]:
		if nome.begins_with(k):
			vento = 1.6
	for k in ["carvalho", "pinheiro", "betula", "selva", "palmeira", "mangue", "acacia", "arvore_nuvem", "arbusto"]:
		if nome.begins_with(k):
			vento = 1.0
	for k in ["arvore_negra", "arvore_petrificada", "tronco_queimado", "cacto", "coral"]:
		if nome.begins_with(k):
			vento = 0.15
	m.set_shader_parameter("vento", vento)
	m.set_shader_parameter("tapa", 1.0 if tam.y > 1.6 else 0.0)
	return m
