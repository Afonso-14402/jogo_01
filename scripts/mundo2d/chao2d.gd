class_name Chao2D
extends RefCounted
## O chão de um andar em 2D (docs/PROGRAMACAO.md, secção 4A): uma malha por fila de blocos de 2 m, com o topo
## de cada bloco e, quando o vizinho da frente é mais baixo, o lado de frente à vista. Cada fila é um nó do
## y-sort do mundo: o que está à frente desenha-se por cima (o herói passa por trás das paredes).
## O shader pinta com as mesmas texturas, o mesmo mapa de mistura e as mesmas bordas da versão 3D (natureza.gd).

const PX := 16.0          # píxeis por metro
const SOBE := 0.8         # 1 m de altura sobe 0,8 m no ecrã (vista de cima, um pouco de frente)

static var _shader: Shader


static func shader() -> Shader:
	if _shader:
		return _shader
	_shader = Shader.new()
	_shader.code = """
shader_type canvas_item;
uniform sampler2D t_base : source_color, filter_nearest, repeat_enable;
uniform sampler2D t_var : source_color, filter_nearest, repeat_enable;
uniform sampler2D t_terra : source_color, filter_nearest, repeat_enable;
uniform sampler2D t_caminho : source_color, filter_nearest, repeat_enable;
uniform sampler2D splat : filter_linear;
uniform sampler2D alturas : filter_nearest;
uniform sampler2D mascara : filter_linear;
uniform sampler2D ruido : filter_linear, repeat_enable;
uniform vec2 origem;
uniform vec2 tamanho;
uniform float bloco = 2.0;
uniform float nuvens = 1.0;
uniform float topo_altura = 99.0;
uniform float topo_escuro = 0.0;
uniform float teto = 0.0;   // quanto escurece o cimo das paredes de rocha (nas grutas, bem mais escuro que o chão)
uniform vec4 agua_cor : source_color = vec4(0.04, 0.54, 0.56, 1.0);
uniform float lava = 0.0;
uniform float gelo = 0.0;   // região 5: os lagos estão gelados
const float RAIO = 0.42;   // raio dos cantos redondos (fração do bloco de 2 m)
varying vec4 info;
varying vec2 tela;      // o sítio no ecrã (px do mundo 2D)
varying float fila_z;   // a beira de trás desta fila de blocos (m)
global uniform vec2 jogador2d;
global uniform vec2 jogador2d_chao;   // r: lado (1) · g: altura do topo · b: altura do vizinho · a: 1 chão, 0.5 água

float bayer(vec2 p) {
	ivec2 i = ivec2(mod(p, 4.0));
	int m[16] = int[](0, 8, 2, 10, 12, 4, 14, 6, 3, 11, 1, 9, 15, 7, 13, 5);
	return float(m[i.y * 4 + i.x]) / 16.0;
}
float aleat(vec2 p) {
	return fract(sin(dot(p, vec2(12.9898, 78.233))) * 43758.5453);
}
float ruido_v(vec2 p) {
	vec2 i = floor(p);
	vec2 f = fract(p);
	f = f * f * (3.0 - 2.0 * f);
	return mix(mix(aleat(i), aleat(i + vec2(1.0, 0.0)), f.x), mix(aleat(i + vec2(0.0, 1.0)), aleat(i + vec2(1.0, 1.0)), f.x), f.y);
}
float altura_em(vec2 p) {
	return texture(alturas, (p - origem) / tamanho).r;
}

void vertex() {
	info = COLOR;
	tela = (MODEL_MATRIX * vec4(VERTEX, 0.0, 1.0)).xy;
	fila_z = MODEL_MATRIX[3].y / 16.0;
}

vec3 agua(vec2 q, vec2 w) {
	float m = texture(mascara, ((q + 0.5) / 16.0 - origem) / tamanho).r;
	float t = clamp(smoothstep(0.35, 0.9, m) * 0.9 + (ruido_v(q / 40.0 + TIME * vec2(0.025, 0.012)) - 0.5) * 0.22, 0.0, 1.0);
	t = floor(t * 3.0 + 0.5) / 3.0;
	vec3 cor = agua_cor.rgb;
	vec3 brilho = mix(cor, vec3(1.0), 0.5);
	vec3 c = mix(cor * 1.1 + vec3(0.03, 0.06, 0.04), cor * 0.74, t);
	float fila = floor(q.y / 6.0);
	float vel = 1.0 + floor(aleat(vec2(fila, 3.0)) * 3.0);
	float sx = q.x + floor(TIME * vel);
	float r = aleat(vec2(floor(sx / 12.0), fila));
	if (r < 0.4) {
		float lx = mod(sx, 12.0);
		float ly = mod(q.y, 6.0);
		float comp = 3.0 + floor(r * 10.0);
		float ligado = step(-0.2, sin(TIME * 1.4 + r * 31.0));
		if (ly == 2.0 && lx >= 2.0 && lx < 2.0 + comp) c = mix(c, brilho, 0.8 * ligado);
		else if (ly == 3.0 && lx >= 3.0 && lx < 1.0 + comp) c = mix(c, cor * 0.5, 0.45 * ligado);
	}
	float b = aleat(floor(q / 3.0) + 17.0);
	if (b > 0.995 && sin(TIME * 4.0 + b * 60.0) > 0.75) c = vec3(1.0);
	float onda = sin(TIME * 1.8 + q.x * 0.14 + q.y * 0.1) * 0.05 + sin(TIME * 0.7 - q.x * 0.06) * 0.03;
	c = mix(c, vec3(0.93, 1.0, 0.97), step(m + onda, 0.3) * 0.9);
	c = mix(c, brilho, step(m + onda * 1.4, 0.42) * (1.0 - step(m + onda, 0.3)) * 0.6);
	if (gelo > 0.5) {
		// lago gelado: gelo liso em 3 tons (manchas grandes), rachas finas, riscos de reflexo, neve na margem
		// e brilhos que piscam (antes era a textura de lajes da região: parecia um chão de azulejos)
		float n = ruido_v(q / 110.0) * 0.75 + ruido_v(q / 34.0 + 7.3) * 0.25;
		c = n > 0.64 ? vec3(0.78, 0.92, 1.0) : (n > 0.4 ? vec3(0.56, 0.83, 1.0) : vec3(0.30, 0.61, 0.90));
		float rk = ruido_v(q / 30.0 + 3.1);
		if (abs(rk - 0.5) < 0.008 && ruido_v(q / 70.0 + 5.0) > 0.58) c = vec3(0.30, 0.40, 0.71);   // rachas (poucas)
		float rf = fract((q.x + q.y * 0.55) / 41.0);
		if (rf < 0.035 && ruido_v(q / 26.0 + 11.0) > 0.55) c = vec3(1.0);   // reflexo
		c = mix(c, vec3(1.0), step(m, 0.38));
		float bg = aleat(floor(q / 4.0));
		c = mix(c, vec3(1.0), step(0.994, bg) * step(0.6, sin(TIME * 3.0 + bg * 40.0)));
		return c;
	}
	if (lava > 0.5) {
		float n1 = ruido_v(q / 22.0 + TIME * vec2(0.03, 0.018));
		float n2 = ruido_v(q / 7.0 - TIME * vec2(0.05, 0.03));
		float k = n1 * 0.72 + n2 * 0.28 - (1.0 - smoothstep(0.3, 0.6, m)) * 0.25;
		c = vec3(0.98, 0.76, 0.17);
		if (k > 0.56) c = vec3(0.18, 0.13, 0.18);
		else if (k > 0.5) c = cor * 0.8;
		else if (k > 0.38) c = cor;
		else if (k > 0.27) c = vec3(0.98, 0.42, 0.11);
		else if (k > 0.2) c = vec3(0.97, 0.59, 0.09);
	}
	return c;
}

void fragment() {
	vec2 w = UV;   // metros: (x, z) no topo; (x, altura) nos lados
	vec3 c;
	// uma parede alta à frente do herói (mais a sul) que o tapa: abre-se uma janela redonda à volta dele
	if (info.g * 10.0 - 2.0 > 0.6 && fila_z > jogador2d_chao.y / 16.0 - 0.2) {
		float d = length((tela - jogador2d) * vec2(1.0, 0.85));
		float k = clamp((d - 20.0) / 14.0, 0.0, 1.0);
		if (bayer(floor(tela)) >= k) discard;
	}
	if (info.r > 0.5) {
		// lado de frente de uma colina / parede / margem
		vec2 px = floor(w * 16.0);
		float ht = info.g * 10.0 - 2.0;
		float hv = info.b * 10.0 - 2.0;
		float yq = (px.y + 0.5) / 16.0;
		float desce = ht - yq;
		c = texture(t_terra, (px + 0.5) / 64.0).rgb * 0.78;
		if (topo_escuro > 0.0) c *= 1.0 - topo_escuro * 0.75 * clamp((yq - 0.6) / max(0.5, topo_altura), 0.0, 1.0);
		if (topo_altura > 90.0) {
			float aba = (2.0 + floor(aleat(vec2(px.x, 1.0)) * 2.5)) / 16.0;
			if (desce < aba) c = texture(t_base, (px + 0.5) / 64.0).rgb * (desce < 1.0 / 16.0 ? 1.12 : 0.95);
			else if (desce < aba + 1.0 / 16.0) c *= 0.52;
		} else {
			float off = aleat(vec2(floor(px.x / 11.0), 7.0)) * 0.22;
			float camada = floor((yq + off) / 0.62);
			c *= mod(camada, 2.0) < 0.5 ? 1.0 : 0.88;
			if (fract((yq + off) / 0.62) < 0.1) c *= 0.72;
			if (desce < 2.0 / 16.0) c = texture(t_terra, (px + 0.5) / 64.0).rgb * 1.22;
			else if (desce < 3.0 / 16.0) c *= 0.8;
		}
		float t = clamp((yq - hv) / max(0.4, ht - hv), 0.0, 1.0);
		c *= 0.58 + 0.42 * floor(t * 3.0 + 0.8) / 3.0;
		// cantos redondos (vistos de cima, um pouco de frente): a coluna da ponta sobe com a curva do topo
		float flags = floor(info.a * 8.0 + 0.5) - 1.0;
		bool wl = mod(flags, 4.0) >= 2.0;
		bool el = flags >= 4.0;
		float fx = fract((w.x - origem.x) / bloco);
		float pxb = 1.0 / (bloco * 16.0);
		float dx = wl && fx < RAIO ? RAIO - fx : (el && fx > 1.0 - RAIO ? fx - (1.0 - RAIO) : 0.0);
		float dz = RAIO - sqrt(max(RAIO * RAIO - dx * dx, 0.0));   // quanto a curva recua (fração do bloco)
		float sobe_m = dz * bloco / 0.8;                               // em metros de altura
		if (yq - hv < sobe_m) discard;
		// contornos: em baixo e nas pontas de lado
		if (ht - hv < 0.6) {
			// degrau pequeno (ondulação do chão): só um pouco mais escuro, sem contornos (senão viravam riscas)
			c = (topo_altura > 90.0 ? texture(t_base, (px + 0.5) / 64.0).rgb : texture(t_terra, (px + 0.5) / 64.0).rgb) * 0.84;
		} else {
			if (yq - hv < sobe_m + 1.0 / 16.0) c *= 0.5;
			if ((wl && fx < pxb) || (el && fx > 1.0 - pxb)) c *= 0.55;
		}
	} else {
		vec2 px = floor(w * 16.0);
		vec2 wq = (px + 0.5) / 16.0;
		if (info.a < 0.9) {
			c = agua(px, wq);
		} else {
			vec2 uv = wq / 4.0;
			vec2 su = (wq - origem) / tamanho;
			vec4 sa = texture(splat, su);
			float n = texture(ruido, wq * 0.09).r - 0.5;
			float d = 0.0;   // (sem xadrez: as bordas entre a erva, a terra e o caminho seguem as manchas)
			c = texture(t_base, uv).rgb;
			if (sa.b + n * 0.9 + d > 0.5) c = texture(t_var, uv).rgb;
			if (sa.g + n * 0.8 + d > 0.5) c = texture(t_terra, uv).rgb;
			if (sa.r + n * 0.45 + d > 0.5) c = texture(t_caminho, uv).rgb;
			float m = texture(ruido, wq * 0.018 + 0.31).r;
			c *= 0.95 + floor(clamp(m * 1.6 - 0.3, 0.0, 1.0) * 2.0 + 0.5) * 0.035;   // manchas grandes e suaves (pouco contraste)
			float nv = texture(ruido, wq * 0.012 + TIME * vec2(0.0035, 0.0016)).r;
			c *= 1.0 - nuvens * 0.16 * step(0.6, nv);
			if (su.x < 0.0 || su.y < 0.0 || su.x > 1.0 || su.y > 1.0) c *= 0.78;   // fora do mapa: mais escuro
			if (sa.a > 0.5 && topo_altura < 90.0) {
				c = texture(t_terra, uv).rgb * (1.0 - teto);
				if (teto > 0.3) c = mix(c, vec3(0.18, 0.13, 0.18), 0.4);   // grutas: rocha escura e fria por cima
			}
			// bordas: linha clara junto a uma descida, sombra ao pé de uma subida
			vec2 g = (wq - origem) / bloco;
			vec2 cel = floor(g);
			vec2 f = g - cel;
			vec2 b0 = origem + (cel + 0.5) * bloco;
			float h0 = altura_em(b0);
			float hw = altura_em(b0 - vec2(bloco, 0.0));
			float he = altura_em(b0 + vec2(bloco, 0.0));
			float hn = altura_em(b0 - vec2(0.0, bloco));
			float hs = altura_em(b0 + vec2(0.0, bloco));
			float um = 1.0 / (bloco * 16.0);
			bool bw_ = hw < h0 - 0.3;
			bool be_ = he < h0 - 0.3;
			bool bn_ = hn < h0 - 0.3;
			bool bs_ = hs < h0 - 0.3;
			// cantos de fora redondos: atrás (norte) vê-se o chão de trás; à frente (sul) vê-se a parede a curvar
			vec2 q = vec2(-1.0);
			if (bn_ && bw_ && f.x < RAIO && f.y < RAIO) q = vec2(RAIO - f.x, RAIO - f.y);
			if (bn_ && be_ && f.x > 1.0 - RAIO && f.y < RAIO) q = vec2(f.x - (1.0 - RAIO), RAIO - f.y);
			bool frente = false;
			if (bs_ && bw_ && f.x < RAIO && f.y > 1.0 - RAIO) { q = vec2(RAIO - f.x, f.y - (1.0 - RAIO)); frente = true; }
			if (bs_ && be_ && f.x > 1.0 - RAIO && f.y > 1.0 - RAIO) { q = vec2(f.x - (1.0 - RAIO), f.y - (1.0 - RAIO)); frente = true; }
			float dq = q.x >= 0.0 ? length(q) : 0.0;
			if (dq > RAIO) {
				if (!frente) discard;
				c = texture(t_terra, (px + 0.5) / 64.0).rgb * 0.78;   // a parede que curva (como o cimo do lado)
				if (topo_altura < 90.0) c *= 1.0 - topo_escuro * 0.5;
				if (dq < RAIO + um) c *= 1.22;
			} else if (bw_ || be_ || bn_ || bs_) {
				// a beira: contorno escuro de 1 píxel nas pontas de trás e de lado, aresta clara a seguir (e à frente)
				float dw = bw_ ? f.x : 9.0;
				float de = be_ ? 1.0 - f.x : 9.0;
				float dn = bn_ ? f.y : 9.0;
				float ds = bs_ ? 1.0 - f.y : 9.0;
				float borda = min(min(dw, de), dn);
				if (q.x >= 0.0) borda = min(borda, RAIO - dq);
				if (q.x >= 0.0 && frente) ds = min(ds, RAIO - dq);
				if (borda < um) c *= 0.5;
				else if (borda < 2.0 * um || ds < 2.0 * um) c *= 1.22;
			}
			float ao = 1.0;
			float k = 7.0 * um;
			if (hw > h0 + 0.3) ao = min(ao, f.x / k);
			if (he > h0 + 0.3) ao = min(ao, (1.0 - f.x) / k);
			if (hn > h0 + 0.3) ao = min(ao, f.y / (k * 2.0));   // a parede de trás faz mais sombra (o sol vem de cima)
			if (ao < 1.0) c *= 0.7 + 0.3 * floor(clamp(ao, 0.0, 1.0) * 3.0 + 0.5) / 3.0;
		}
	}
	COLOR = vec4(c, 1.0);
}
"""
	return _shader


## O material do chão da região (as mesmas texturas da versão 3D).
static func material(regiao: int, splat: Image, alturas: Image, mascara: Image, origem: Vector2, tamanho: Vector2, agua: Color,
		rocha: float, trocar: Dictionary = {}) -> ShaderMaterial:
	var n: Dictionary = Dados.tabela("natureza").get(str(regiao), {})
	var ch: Dictionary = n.get("chao", {})
	var m := ShaderMaterial.new()
	m.shader = shader()
	for k in ["base", "variante", "terra", "caminho"]:
		var uni: String = {"base": "t_base", "variante": "t_var", "terra": "t_terra", "caminho": "t_caminho"}[k]
		var caminho: String = ch.get(trocar.get(k, k), ch.get("base", ""))
		if caminho != "":
			m.set_shader_parameter(uni, load(caminho))
	m.set_shader_parameter("splat", ImageTexture.create_from_image(splat))
	m.set_shader_parameter("alturas", ImageTexture.create_from_image(alturas))
	m.set_shader_parameter("mascara", ImageTexture.create_from_image(mascara))
	m.set_shader_parameter("ruido", Natureza.ruido())
	m.set_shader_parameter("origem", origem)
	m.set_shader_parameter("tamanho", tamanho)
	m.set_shader_parameter("nuvens", 0.0 if regiao in [2, 10] else 1.0)
	m.set_shader_parameter("agua_cor", agua)
	m.set_shader_parameter("lava", 1.0 if agua.r > 0.7 and agua.g < 0.45 and agua.b < 0.4 else 0.0)
	m.set_shader_parameter("gelo", 1.0 if regiao == 5 else 0.0)
	if rocha > 0.0:
		m.set_shader_parameter("topo_altura", rocha)
		m.set_shader_parameter("topo_escuro", 0.3 if regiao == 2 else 0.1)
		m.set_shader_parameter("teto", 0.55 if regiao == 2 else 0.1)
	return m


## As filas do chão. O chão plano (até 0,3 m de altura) fica todo por baixo (camada "baixo", sem ordem: nada se
## esconde atrás dele); os blocos mais altos (colinas, paredes de rocha) ficam numa malha por fila que entra no
## y-sort do mundo pela beira de trás da fila (o que está atrás deles fica escondido, o que está à frente ou por
## cima desenha-se depois). Devolve [[MeshInstance2D, alto?], ...].
## alturas: uma por bloco (−60 = vazio); agua: blocos com água; bw × bh blocos; origem em metros.
static func filas(alturas: PackedFloat32Array, agua: PackedByteArray, bw: int, bh: int, origem: Vector2, bloco: float,
		mat: ShaderMaterial) -> Array:
	var out: Array = []
	var bp := bloco * PX
	for bz in bh:
		var partes := [[PackedVector2Array(), PackedVector2Array(), PackedColorArray()],
				[PackedVector2Array(), PackedVector2Array(), PackedColorArray()]]
		var z0 := origem.y + bz * bloco
		for bx in bw:
			var h := alturas[bz * bw + bx]
			if h < -10.0:
				continue
			var k := 1 if h > 0.3 else 0
			var v: PackedVector2Array = partes[k][0]
			var uv: PackedVector2Array = partes[k][1]
			var cor: PackedColorArray = partes[k][2]
			var x0 := origem.x + bx * bloco
			var sobe := h * SOBE * PX
			var tipo := 0.5 if agua[bz * bw + bx] else 1.0
			var info := Color(0.0, (h + 2.0) / 10.0, 0.0, tipo)
			_quad(v, uv, cor, Vector2(x0 * PX, -sobe), Vector2(x0 * PX + bp, bp - sobe),
					Vector2(x0, z0), Vector2(x0 + bloco, z0 + bloco), info)
			# o lado de frente, se o bloco da frente for mais baixo (o vazio: uma parede de 3 m)
			var hs := alturas[(bz + 1) * bw + bx] if bz + 1 < bh else h - 3.0
			if hs < -10.0:
				hs = h - 3.0
			if hs < h - 0.05:
				# a: os vizinhos de lado também são mais baixos? (para arredondar os cantos e pôr contorno)
				var hw := alturas[bz * bw + bx - 1] if bx > 0 else -60.0
				var he := alturas[bz * bw + bx + 1] if bx + 1 < bw else -60.0
				var flags := (1.0 if hw < h - 0.3 else 0.0) * 2.0 + (1.0 if he < h - 0.3 else 0.0) * 4.0
				var info_l := Color(1.0, (h + 2.0) / 10.0, (hs + 2.0) / 10.0, (1.0 + flags) / 8.0)
				_quad(v, uv, cor, Vector2(x0 * PX, bp - sobe), Vector2(x0 * PX + bp, bp - hs * SOBE * PX),
						Vector2(x0, h), Vector2(x0 + bloco, hs), info_l)
			partes[k] = [v, uv, cor]
		for k in 2:
			var v: PackedVector2Array = partes[k][0]
			if v.is_empty():
				continue
			var arr := []
			arr.resize(Mesh.ARRAY_MAX)
			arr[Mesh.ARRAY_VERTEX] = v
			arr[Mesh.ARRAY_TEX_UV] = partes[k][1]
			arr[Mesh.ARRAY_COLOR] = partes[k][2]
			var am := ArrayMesh.new()
			am.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, arr)
			var mi := MeshInstance2D.new()
			mi.mesh = am
			mi.material = mat
			mi.position = Vector2(0, z0 * PX)
			mi.name = ("Alto%d" if k == 1 else "Baixo%d") % bz
			out.append([mi, k == 1])
	return out


## Um retângulo (2 triângulos): a..b no ecrã, ua..ub nas coordenadas do mundo (para as texturas).
static func _quad(v: PackedVector2Array, uv: PackedVector2Array, cor: PackedColorArray, a: Vector2, b: Vector2,
		ua: Vector2, ub: Vector2, info: Color) -> void:
	var p := [a, Vector2(b.x, a.y), b, Vector2(a.x, b.y)]
	var q := [ua, Vector2(ub.x, ua.y), ub, Vector2(ua.x, ub.y)]
	for i in [0, 1, 2, 0, 2, 3]:
		v.append(p[i])
		uv.append(q[i])
		cor.append(info)
