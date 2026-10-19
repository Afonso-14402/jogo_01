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
uniform float topo_altura = 99.0;     // altura das paredes de rocha (o topo marca-se no alfa do mapa)
uniform float topo_escuro = 0.0;      // nas grutas o topo das paredes fica quase preto (é o teto da gruta)
uniform float corta = 0.0;            // paredes altas à frente do herói ficam transparentes (aos quadradinhos)
uniform sampler2D alturas : filter_nearest;   // altura de cada bloco de 2 m (para as bordas e as sombras das colinas)
uniform float usa_alturas = 0.0;
uniform float bloco = 2.0;
global uniform vec3 jogador_pos;
global uniform sampler2D luzes_tex : filter_nearest;
global uniform int n_luzes;
global uniform float escuro;
global uniform float raio_jogador;
varying vec3 mundo;
varying float de_lado;
varying vec3 normal_mundo;

float aleat(float x) {
	return fract(sin(x * 12.9898) * 43758.5453);
}

float altura_em(vec2 p) {
	return texture(alturas, (p - origem) / tamanho).r;
}

float bayer(vec2 p) {
	ivec2 i = ivec2(mod(p, 4.0));
	int m[16] = int[](0, 8, 2, 10, 12, 4, 14, 6, 3, 11, 1, 9, 15, 7, 13, 5);
	return float(m[i.y * 4 + i.x]) / 16.0;
}

// Luzes da gruta (tochas, cristais, cogumelos, a luz do herói): manchas de luz em degraus, como em pixel art.
vec3 luz_local(vec3 p, vec2 px) {
	vec3 acc = vec3(0.0);
	float b = 0.3 + bayer(px) * 0.35;
	for (int i = 0; i < n_luzes; i++) {
		vec4 a = texelFetch(luzes_tex, ivec2(i, 0), 0);
		vec4 c = texelFetch(luzes_tex, ivec2(i, 1), 0);
		float d = length(p - a.xyz);
		if (d < a.w) {
			float k = 1.0 - d / a.w;
			acc += c.rgb * c.a * floor(k * 4.0 + b) / 4.0;
		}
	}
	float dj = length(p.xz - jogador_pos.xz);
	if (dj < raio_jogador + 1.0) {
		float k = clamp(1.0 - dj / (raio_jogador + 1.0), 0.0, 1.0);
		acc += vec3(1.0, 0.72, 0.42) * 1.1 * floor(k * 4.0 + b) / 4.0;
	}
	return acc;
}

void vertex() {
	mundo = (MODEL_MATRIX * vec4(VERTEX, 1.0)).xyz;
	normal_mundo = normalize((MODEL_MATRIX * vec4(NORMAL, 0.0)).xyz);
	de_lado = 1.0 - clamp(normal_mundo.y, 0.0, 1.0);
	// paredes altas entre a câmara e o herói: os blocos à frente dele "baixam" (corte, como numa maqueta)
	if (corta > 0.5 && mundo.y > jogador_pos.y + 1.0) {
		vec3 centro = MODEL_MATRIX[3].xyz;
		float dz = centro.z - jogador_pos.z;
		if (dz > -1.5 && dz < 9.0 && abs(centro.x - jogador_pos.x) < 3.2 + dz * 0.45) {
			float novo = jogador_pos.y + 0.7;
			VERTEX.y += novo - mundo.y;
			mundo.y = novo;
		}
	}
}

void fragment() {
	vec3 c;
	bool topo = false;
	vec2 px;
	if (de_lado > 0.5) {
		// lados dos degraus e das colinas: terra/rocha com a textura de pé (não esticada), um pouco mais escura
		px = floor(vec2(mundo.x + mundo.z, mundo.y) * 16.0);
		c = texture(t_terra, (px + 0.5) / 64.0).rgb * 0.78;
		// nas paredes altas: mais escuro em cima (a rocha sobe para a escuridão)
		if (topo_escuro > 0.0) c *= 1.0 - topo_escuro * 0.75 * clamp((mundo.y - 0.6) / max(0.5, topo_altura), 0.0, 1.0);
		if (usa_alturas > 0.5 && abs(normal_mundo.y) < 0.5) {
			// a borda da colina: a erva de cima "cai" uns píxeis pelo lado (com uma linha escura por baixo) e
			// o fundo do lado fica mais escuro (sombra junto ao chão), em degraus como em pixel art
			float ht = altura_em(mundo.xz - normal_mundo.xz * 0.3);
			float hv = altura_em(mundo.xz + normal_mundo.xz * 0.3);
			float yq = (floor(mundo.y * 16.0) + 0.5) / 16.0;
			float desce = ht - yq;
			float aba = (2.0 + floor(aleat(px.x) * 2.5)) / 16.0;
			if (topo_altura > 90.0) {
				if (desce < aba) c = texture(t_base, (px + 0.5) / 64.0).rgb * (desce < 1.0 / 16.0 ? 1.12 : 0.95);
				else if (desce < aba + 1.0 / 16.0) c *= 0.52;
			} else {
				// paredes de rocha: camadas (estratos) com uma racha escura entre elas e a aresta de cima clara
				float off = aleat(floor(px.x / 11.0) + 7.0) * 0.22;
				float camada = floor((yq + off) / 0.62);
				c *= mod(camada, 2.0) < 0.5 ? 1.0 : 0.88;
				if (fract((yq + off) / 0.62) < 0.1) c *= 0.72;
				if (desce < 2.0 / 16.0) c = texture(t_terra, (px + 0.5) / 64.0).rgb * 1.22;
				else if (desce < 3.0 / 16.0) c *= 0.8;
			}
			float t = clamp((yq - hv) / max(0.4, ht - hv), 0.0, 1.0);
			c *= 0.58 + 0.42 * floor(t * 3.0 + 0.8) / 3.0;
		}
	} else {
	px = floor(mundo.xz * 16.0);          // o píxel da textura (16 por metro)
	vec2 w = (px + 0.5) / 16.0;
	vec2 uv = w / 4.0;                          // texturas de 64 px = 4 m
	vec2 su = (w - origem) / tamanho;
	vec4 sa = texture(splat, su);
	vec3 s = sa.rgb;
	float n = texture(ruido, w * 0.09).r - 0.5;
	float d = (bayer(px) - 0.5) * 0.12;
	c = texture(t_base, uv).rgb;
	if (s.b + n * 0.9 + d > 0.5) c = texture(t_var, uv).rgb;
	if (s.g + n * 0.8 + d > 0.5) c = texture(t_terra, uv).rgb;
	if (s.r + n * 0.45 + d > 0.5) c = texture(t_caminho, uv).rgb;
	if (usa_alturas > 0.5) {
		// junto a uma descida: uma linha clara na borda; junto a uma subida: sombra no chão ao pé da parede
		vec2 g = (w - origem) / bloco;
		vec2 cel = floor(g);
		vec2 f = g - cel;
		vec2 b0 = origem + (cel + 0.5) * bloco;
		float h0 = altura_em(b0);
		float hw = altura_em(b0 - vec2(bloco, 0.0));
		float he = altura_em(b0 + vec2(bloco, 0.0));
		float hn = altura_em(b0 - vec2(0.0, bloco));
		float hs = altura_em(b0 + vec2(0.0, bloco));
		float um = 1.0 / (bloco * 16.0);
		if ((hw < h0 - 0.3 && f.x < um) || (he < h0 - 0.3 && f.x > 1.0 - um) || (hn < h0 - 0.3 && f.y < um) || (hs < h0 - 0.3 && f.y > 1.0 - um))
			c *= 1.22;
		float ao = 1.0;
		float k = 7.0 * um;
		if (hw > h0 + 0.3) ao = min(ao, f.x / k);
		if (he > h0 + 0.3) ao = min(ao, (1.0 - f.x) / k);
		if (hn > h0 + 0.3) ao = min(ao, f.y / k);
		if (hs > h0 + 0.3) ao = min(ao, (1.0 - f.y) / k);
		if (ao < 1.0) c *= 0.7 + 0.3 * floor(clamp(ao, 0.0, 1.0) * 3.0 + bayer(px) * 0.95) / 3.0;
	}
	// manchas grandes: mais claro ao sol, mais frio e escuro nas zonas húmidas (em degraus, pixel art)
	float m = texture(ruido, w * 0.018 + 0.31).r;
	c *= 0.86 + floor(clamp(m * 1.6 - 0.3, 0.0, 1.0) * 3.0 + bayer(px + 2.0) * 0.9) * 0.07;
	// sombras das nuvens a passar
	float nv = texture(ruido, w * 0.012 + TIME * vec2(0.0035, 0.0016)).r;
	c *= 1.0 - nuvens * 0.2 * step(0.6 + bayer(px) * 0.05, nv);
	// fora do mapa: mais escuro (a floresta à volta fica em segundo plano)
	if (su.x < 0.0 || su.y < 0.0 || su.x > 1.0 || su.y > 1.0) c *= fora_escuro;
	// topo das paredes de rocha
	if (sa.a > 0.5 && topo_altura < 90.0) {
		c = texture(t_terra, uv).rgb * (1.0 - topo_escuro);
		topo = true;
	}
	}
	ALBEDO = c;
	if (escuro > 0.0 && !topo) EMISSION = c * luz_local(mundo, px) * escuro;
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
	var rocha := float(Andar.ALTURA_ROCHA.get(regiao, 0.0))
	if rocha > 0.0:
		m.set_shader_parameter("topo_altura", rocha)
		m.set_shader_parameter("topo_escuro", 0.82 if regiao == 2 else 0.12)
		m.set_shader_parameter("corta", 1.0)
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
uniform float brilha = 0.0;   // cogumelos que brilham, cristais, lanternas: veem-se no escuro
global uniform vec3 jogador_pos;
global uniform sampler2D luzes_tex : filter_nearest;
global uniform int n_luzes;
global uniform float escuro;
global uniform float raio_jogador;
varying vec3 base_mundo;

float bayer(vec2 p) {
	ivec2 i = ivec2(mod(p, 4.0));
	int m[16] = int[](0, 8, 2, 10, 12, 4, 14, 6, 3, 11, 1, 9, 15, 7, 13, 5);
	return float(m[i.y * 4 + i.x]) / 16.0;
}

void vertex() {
	vec3 o = MODEL_MATRIX[3].xyz;
	base_mundo = o;
	float fase = o.x * 0.37 + o.z * 0.23;
	float h = clamp(VERTEX.y / tamanho.y, 0.0, 1.0);
	float s = sin(TIME * 1.5 + fase) * 0.65 + sin(TIME * 2.6 + fase * 1.7) * 0.25 + sin(TIME * 0.4 + fase * 0.3) * 0.5;
	// o vento dobra mais a parte de cima; o deslocamento anda aos píxeis (fica pixel art)
	VERTEX.x += round(s * vento * h * h * 0.06 * tamanho.y * 16.0) / 16.0;
	NORMAL = normalize(vec3(0.0, 1.0, 0.55));
}

void fragment() {
	vec4 c = texture(tex, UV);
	if (c.a < 0.5) discard;
	// o herói está escondido atrás desta planta: abre-se uma "janela" redonda à volta dele (só nessa parte,
	// com a borda aos quadradinhos do tamanho dos píxeis do desenho); o resto da árvore fica inteiro
	if (tapa > 0.5) {
		vec3 pv = (VIEW_MATRIX * vec4(jogador_pos + vec3(0.0, 0.85, 0.0), 1.0)).xyz;
		if (VERTEX.z > pv.z + 0.4) {
			vec2 a = (VERTEX.xy / -VERTEX.z - pv.xy / -pv.z) * -pv.z;   // em metros, à distância do herói
			float k = clamp((length(a * vec2(1.0, 0.85)) - 1.3) / 1.4, 0.0, 1.0);
			if (bayer(floor(UV * vec2(textureSize(tex, 0)))) >= k) discard;
		}
	}
	ALBEDO = c.rgb;
	if (escuro > 0.0) {   // luzes da gruta (ver o chão): a planta inteira apanha a luz que há no pé dela
		vec3 acc = vec3(0.0);
		for (int i = 0; i < n_luzes; i++) {
			vec4 a = texelFetch(luzes_tex, ivec2(i, 0), 0);
			vec4 l = texelFetch(luzes_tex, ivec2(i, 1), 0);
			float d = length(base_mundo - a.xyz);
			if (d < a.w) acc += l.rgb * l.a * floor((1.0 - d / a.w) * 4.0 + 0.5) / 4.0;
		}
		float dj = length(base_mundo.xz - jogador_pos.xz);
		if (dj < raio_jogador + 1.0) acc += vec3(1.0, 0.72, 0.42) * floor((1.0 - dj / (raio_jogador + 1.0)) * 4.0 + 0.5) / 4.0;
		EMISSION = c.rgb * (acc * escuro + brilha * 0.9);
	} else if (brilha > 0.0) {
		EMISSION = c.rgb * brilha * 0.35;
	}
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
	for k in ["cogumelo_luz", "cristais", "cristal", "lanterna", "cogumelo_gigante_luz", "chama", "brasa"]:
		if nome.begins_with(k):
			m.set_shader_parameter("brilha", 1.0)
	m.set_shader_parameter("tapa", 1.0 if tam.y > 1.6 else 0.0)
	return m
