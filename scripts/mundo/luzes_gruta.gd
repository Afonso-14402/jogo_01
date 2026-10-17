class_name LuzesGruta
extends RefCounted
## A escuridão das grutas (docs/regioes/r02_cavernas.md: "sem luz vês 3 m"): as coisas que brilham (cogumelos,
## cristais, lanternas, fogueiras, a Zona Segura) fazem manchas de luz no chão e nas plantas. Não são luzes
## "a sério" (no telemóvel só cabem 8 por objeto): vão numa textura pequena que os shaders do chão e das plantas
## leem (shader globals luzes_tex, n_luzes, escuro). O herói tem a luz dele (raio_jogador; ver LuzHeroi).

const MAX := 48

## Cor e raio (m) de cada coisa que brilha, pelo começo do nome do ficheiro.
const FONTES := {
	"cogumelo_luz_1": [Color("8fd3ff"), 3.5, 0.9], "cogumelo_luz_2": [Color("ed8099"), 3.5, 0.9],
	"cogumelo_luz_3": [Color("30e1b9"), 3.5, 0.9], "cogumelo_gigante_luz": [Color("30e1b9"), 9.0, 1.1],
	"cristais_azuis": [Color("4d9be6"), 5.0, 1.0], "cristais_rosa": [Color("f04f78"), 5.0, 1.0],
	"cristais_verdes": [Color("1ebc73"), 5.0, 1.0], "cristais": [Color("8fd3ff"), 5.0, 0.9], "cristal": [Color("8fd3ff"), 6.0, 1.0],
	"lanterna": [Color("f79617"), 7.0, 1.2], "escora_mina": [Color("f79617"), 7.0, 1.2], "fogueira": [Color("f79617"), 8.0, 1.3],
	"fornalha": [Color("f79617"), 9.0, 1.3], "lago_luminoso": [Color("30e1b9"), 12.0, 1.0],
	"minerio": [Color("c7dcd0"), 2.0, 0.4], "coral_luminoso": [Color("30e1b9"), 6.0, 1.1], "fonte_hidrotermal": [Color("f79617"), 7.0, 1.0],
	"anemona": [Color("ed8099"), 3.0, 0.7], "coral_1": [Color("f04f78"), 3.0, 0.6], "ovo_gigante": [Color("a884f3"), 8.0, 1.0],
}

static var _fontes: Array = []   # [Vector3, Color, raio, força]
static var ligada := false       # este andar está às escuras (a luz do dia fica fraca: ver CicloDia)


static func limpar() -> void:
	_fontes.clear()


## Se este ficheiro brilha, guarda a luz no sítio dele.
static func registar(caminho: String, p: Vector3) -> void:
	var nome := caminho.get_file().get_basename()
	if nome.begins_with("a") and nome.length() > 4 and nome[3] == "_":   # peças especiais: a13_cristal_interruptor
		nome = nome.substr(4)
	if "apagad" in nome:
		return
	for k in FONTES:
		if nome.begins_with(k):
			_fontes.append([p + Vector3(0, 0.4, 0), FONTES[k][0], float(FONTES[k][1]), float(FONTES[k][2])])
			return


static func adicionar(p: Vector3, cor: Color, raio: float, forca: float = 1.0) -> void:
	_fontes.append([p + Vector3(0, 0.4, 0), cor, raio, forca])


## Escolhe até 48 luzes (as maiores primeiro, sem duas quase no mesmo sítio) e liga a escuridão.
static func aplicar(ligar: bool) -> void:
	ligada = ligar
	if not ligar:
		RenderingServer.global_shader_parameter_set("escuro", 0.0)
		RenderingServer.global_shader_parameter_set("n_luzes", 0)
		return
	var lista := _fontes.duplicate()
	lista.sort_custom(func(a, b): return a[2] * a[3] > b[2] * b[3])
	var escolhidas: Array = []
	for f in lista:
		if escolhidas.size() >= MAX:
			break
		var perto := false
		for e in escolhidas:
			if (e[0] as Vector3).distance_to(f[0]) < maxf(2.5, minf(e[2], f[2]) * 0.6):
				perto = true
				break
		if not perto:
			escolhidas.append(f)
	var img := Image.create(MAX, 2, false, Image.FORMAT_RGBAF)
	for i in escolhidas.size():
		var f: Array = escolhidas[i]
		var p: Vector3 = f[0]
		img.set_pixel(i, 0, Color(p.x, p.y, p.z, f[2]))
		var c: Color = f[1]
		img.set_pixel(i, 1, Color(c.r, c.g, c.b, f[3]))
	RenderingServer.global_shader_parameter_set("luzes_tex", ImageTexture.create_from_image(img))
	RenderingServer.global_shader_parameter_set("n_luzes", escolhidas.size())
	RenderingServer.global_shader_parameter_set("escuro", 1.0)
