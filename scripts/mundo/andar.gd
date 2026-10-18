class_name Andar
extends Node3D
## Um andar da torre montado a partir dos dados (docs/PROGRAMACAO.md, secção 9, passo 9):
## dados/andares/aNNN.json (grelha do mapa de docs/mapas, pontos e zonas) + dados/kits.json (peças de cada região).
## Cada célula do mapa tem 10×10 m; o chão faz-se em blocos de 2×2 m (5×5 por célula).

signal guardiao_vencido
signal escada_aberta

const CEL := 10.0
const BLOCO := 2.0
const POR_CEL := 5
# células onde se pode andar (e pôr monstros)
const PASSA := ["..", "\"\"", "**", "::", ",,", "%%", "xx", "nn", "^^", "tt", "==", "ww", "++", "cc", "↑↑", "░░", "◌◌",
	"EE", "SS", "GG", ">>", "BB", "$$", "??", "PP", "!!", "@@", "AA", "rr", "FF", "ii", "JJ", "HH", "vv", "<>", "[]", "▒▒"]
const SEM_MONSTROS := ["SS", "EE", "BB", "@@", ">>", "AA"]

var numero: int = 1
var dados: Dictionary = {}
var kit: Dictionary = {}
var grelha: Array = []
var largura: int = 0   # em células
var altura_cel: int = 0
var nivel: int = 1
var regiao: int = 1

var jogador: Jogador
var camara: Camara
var guardiao: Monstro
var escada: Area3D
var ponto_chegada := Vector3.ZERO
var ponto_seguro := Vector3.ZERO
var escada_livre: bool = false

var _alturas := PackedFloat32Array()   # uma por bloco de 2 m
var _instancias: Dictionary = {}       # caminho do .glb -> [Transform3D]
var escuro: bool = false               # andar às escuras (grutas): ver LuzesGruta e LuzHeroi
var _tons: Dictionary = {}             # caminho do .glb -> [Color] (tom de cada instância, só no chão)
var _cache_mesh: Dictionary = {}       # caminho -> [[Mesh, Transform3D local]]
var _rng := RandomNumberGenerator.new()
var _corpo_estatico: StaticBody3D
var _pov: Dictionary = {}              # a povoação deste andar (dados/povoacoes.json), se houver
var _casas: Array[Vector3] = []
var _casas_info: Array = []            # [{pos, raio, peca}] — para as portas (entrar nas casas)
var _centro_pov := Vector3.ZERO
var _ocupado: Array[Vector4] = []      # (x, 0, z, raio): sítios onde a decoração não entra
var _natureza: Dictionary = {}         # dados/natureza.json desta região (chão e plantas em pixel art)
var _splat: Image                      # 1 píxel por bloco: R = caminho, G = terra, B = variante
var _alturas_img: Image                 # altura de cada bloco (para as bordas das colinas no shader do chão)
var _chao_geo: String = ""             # a peça de chão que leva o shader da natureza


func _ready() -> void:
	numero = Jogo.andar_atual
	Jogo.segunda_vida_usada = false
	dados = Dados.tabela("andares/a%03d" % numero)
	if dados.is_empty():
		push_error("Andar %d sem dados" % numero)
		return
	regiao = int(dados.get("regiao", 1))
	nivel = int(dados.get("nivel", numero))
	kit = Dados.tabela("kits").get(str(regiao), Dados.tabela("kits").get("1"))
	kit = Natureza.aplicar(kit, regiao)
	_natureza = Dados.tabela("natureza").get(str(regiao), {})
	for p in Dados.tabela("povoacoes").values():
		if int(p.andar) == numero:
			_pov = p
	grelha = dados.get("grelha", [])
	altura_cel = grelha.size()
	largura = grelha[0].size() if altura_cel > 0 else 0
	_rng.seed = numero * 7919 + int(Time.get_unix_time_from_system()) % 100000   # cada visita é diferente
	var amb: Dictionary = dados.get("ambiente", {})
	Ambiente.criar(self, Color(amb.get("ceu", "#7fa0c8")), Color(amb.get("nevoeiro", "#c8e0d0")),
			float(amb.get("densidade_nevoeiro", 0.01)), float(amb.get("luz_ambiente", 0.6)), regiao, regiao == 2)
	escuro = regiao == 2 or numero in [58, 74] or bool(amb.get("escuro", false))   # 58: Fossa Abissal · 74: Catacumbas
	LuzesGruta.limpar()
	_corpo_estatico = StaticBody3D.new()
	add_child(_corpo_estatico)
	_calcular_alturas()
	_construir_chao()
	_construir_celulas()
	_pontos()
	_construir_povoacao()
	_decorar()
	_cenarios()
	_detalhes()
	_bordas()
	_criar_instancias()
	_colisao_chao()
	_monstros()
	_baus_madeira()
	_nos_recolha()
	_pagina()
	_sitios_pesca()
	_jogador()
	if not _pov.is_empty():
		var pv := Povoacao.new()
		pv.dados = _pov
		pv.mundo = self
		pv.centro = _centro_pov
		pv.casas = _casas
		pv.casas_info = _casas_info
		add_child(pv)
	# o Tibério na Zona Segura (docs/LOJAS.md 3.1): sempre nos andares 1, 5, 10, 15… e em 1 de cada 3 dos outros
	if ponto_seguro != Vector3.ZERO and (numero == 1 or numero % 5 == 0 or _rng.randf() < 1.0 / 3.0):
		var t := NPC.new().configurar("tiberio")
		add_child(t)
		t.global_position = ponto_seguro + Vector3(3.0, 0.6, 1.5)
	if escuro:   # a Zona Segura, a povoação e as escadas também dão luz
		if ponto_seguro != Vector3.ZERO:
			LuzesGruta.adicionar(ponto_seguro, Color("8fd3ff"), 9.0, 1.1)
		if not _casas.is_empty():
			LuzesGruta.adicionar(_centro_pov, Color("f79617"), 18.0, 1.2)
			var lp := OmniLight3D.new()   # uma luz a sério na povoação (para as pessoas também se verem)
			lp.light_color = Color("fbb954")
			lp.omni_range = 20.0
			lp.light_energy = 1.4
			add_child(lp)
			lp.global_position = _centro_pov + Vector3(0, 4.0, 0)
			for c in _casas:
				LuzesGruta.adicionar(c, Color("fbb954"), 8.0, 0.9)
		LuzesGruta.adicionar(ponto_chegada, Color("c7dcd0"), 6.0, 0.8)
		var luz := LuzHeroi.new()
		jogador.add_child(luz)
		LuzesGruta.aplicar.call_deferred(true)
	else:
		LuzesGruta.aplicar(false)
	var seg := Segredos.new()   # os segredos e puzzles do andar (docs/regioes, linhas Segredo e Puzzle)
	seg.andar = self
	add_child(seg)
	var vida := Vida.new()
	vida.mundo = self
	vida.regiao = regiao
	add_child(vida)
	Audio.tocar_musica(amb.get("musica", ""))
	Sistema.mensagem("Andar %d — %s" % [numero, dados.get("nome_pt", "")], "andar")
	if Jogo.tem_flag("prologo_p2") and numero == 1:
		_prologo_p2.call_deferred()
	elif numero > 1 and Opcoes.v("gravacao_automatica"):
		Gravar.gravar(Jogo.espaco_gravacao)   # gravação automática ao entrar num andar (Zona Segura)
	Eventos.andar_entrou.emit(numero)
	if numero > Jogo.andar_maximo:
		Jogo.andar_maximo = numero
	if Vista2D.ligada():   # tudo o que se vê passa a ser desenhado em 2D (scripts/mundo2d/vista2d.gd)
		add_child.call_deferred(Vista2D.new())


## P2 — Despertar (docs/guiao/prologo.md): as primeiras mensagens do Sistema e a missão H_00.
func _prologo_p2() -> void:
	Jogo.flags.erase("prologo_p2")
	await get_tree().create_timer(1.0).timeout
	for t in ["A verificar sinais vitais… ✓", "A verificar ligação ao Sistema… ✓", "Bem-vindo à Torre, Jogador nº 10 000.",
			"Missão principal: SOBE.", "Usa [mover] para andar. [atacar] com o rato, [esquivar] com o espaço."]:
		Sistema.mensagem(t, "nivel")
		await get_tree().create_timer(1.4).timeout
	Missoes.aceitar("H_00")
	Eventos.monstro_morto.connect(func(_i, _n):
		if Missoes.estado("H_00") == "ativa":
			for k in Missoes.dados("H_00").passos.size():
				Missoes.marcar("H_00", k), CONNECT_ONE_SHOT)


func _cristal() -> void:
	if not numero in Jogo.cristais:
		Jogo.cristais.append(numero)
		Sistema.mensagem("Cristal ligado: já podes voltar ao andar %d pelo Cristal Mestre." % numero, "nivel")
	var ui = get_tree().get_first_node_in_group("dialogo_ui")
	var i: int = await ui.escolher(["Voltar a Ascendia", "Gravar o jogo", "Ficar"])
	if i == 0:
		Cenas.mudar("res://cenas/mundo/cidade.tscn")
	elif i == 1:
		Gravar.gravar(Jogo.espaco_gravacao)
		Sistema.mensagem("Jogo gravado.", "nivel")


## Exploração: as células por onde já passaste (para o mapa e as missões "explorar 80% do andar").
func percent_explorado() -> float:
	var total := 0
	for cy in altura_cel:
		for cx in largura:
			if not codigo(cx, cy) in ["TT", "##", "~~", "  "]:
				total += 1
	var vistas: Dictionary = Jogo.explorado.get(str(numero), {})
	return float(vistas.size()) / maxf(1.0, float(total))


func _physics_process(_delta: float) -> void:
	if jogador:
		var c := celula_de(jogador.global_position)
		var vistas: Dictionary = Jogo.explorado.get_or_add(str(numero), {})
		var chave := "%d,%d" % [c.x, c.y]
		if not vistas.has(chave):
			vistas[chave] = true
			Missoes.explorou(numero, percent_explorado())
	# na Zona Segura os materiais ficam "guardados" (já não se perdem se morreres)
	if jogador and jogador.global_position.distance_to(ponto_seguro) < 6.0 and not Jogo.materiais_andar.is_empty():
		Jogo.materiais_andar.clear()
	# cair no vazio (regiões 9 e 10) ou para fora do mapa: volta à Zona Segura com −10% de HP
	if jogador and jogador.global_position.y < -12.0 and not Jogo.dentro:
		Jogo.receber_dano(int(Jogo.hp_maximo() * 0.1))
		jogador.global_position = ponto_seguro + Vector3(0, 1, 0)
		jogador.velocity = Vector3.ZERO
		Sistema.mensagem("Caíste! Voltaste à Zona Segura.", "aviso")


# ------------------------------------------------------------------ coordenadas ------------------------------------------------------------------

func codigo(cx: int, cy: int) -> String:
	if cy < 0 or cy >= altura_cel or cx < 0 or cx >= largura:
		return "TT"
	return grelha[cy][cx]


func centro_celula(cx: int, cy: int) -> Vector3:
	var x := (cx + 0.5) * CEL - largura * CEL / 2.0
	var z := (cy + 0.5) * CEL - altura_cel * CEL / 2.0
	return Vector3(x, altura_em(x, z), z)


func celula_de(p: Vector3) -> Vector2i:
	return Vector2i(int(floor((p.x + largura * CEL / 2.0) / CEL)), int(floor((p.z + altura_cel * CEL / 2.0) / CEL)))


func altura_em(x: float, z: float) -> float:
	var bw := largura * POR_CEL
	var bx := int(floor((x + largura * CEL / 2.0) / BLOCO))
	var bz := int(floor((z + altura_cel * CEL / 2.0) / BLOCO))
	if bx < 0 or bz < 0 or bx >= bw or bz >= altura_cel * POR_CEL:
		return 0.0
	return _alturas[bz * bw + bx]


func _ponto_aleatorio(cx: int, cy: int, margem: float = 1.0) -> Vector3:
	var c := centro_celula(cx, cy)
	var p := c + Vector3(_rng.randf_range(-CEL / 2 + margem, CEL / 2 - margem), 0, _rng.randf_range(-CEL / 2 + margem, CEL / 2 - margem))
	p.y = altura_em(p.x, p.z)
	return p


# ------------------------------------------------------------------ chão ------------------------------------------------------------------

## Altura das paredes de rocha "##" por região (0 = rochas soltas no chão, como antes).
const ALTURA_ROCHA := {2: 4.5, 4: 3.0, 5: 3.0, 6: 2.5, 7: 3.5, 8: 3.0, 10: 3.0}


func altura_rocha() -> float:
	return float(ALTURA_ROCHA.get(regiao, 0.0))


func _exit_tree() -> void:
	if escuro:
		LuzesGruta.aplicar(false)


func _altura_codigo(c: String) -> float:
	match c:
		"##": return altura_rocha()
		"^^": return 3.0
		"~~", "ww": return -0.8
		",,": return -0.25
		"  ": return -60.0
	return 0.0


const RELEVO := ["..", "tt", "\"\"", "**", "▒▒", "^^", "mm"]
const ABERTO := ["..", "\"\"", "**", "tt", "▒▒", "^^", "::", "mm", "%%", "xx", "??", "PP", "!!", "FF", "AA"]


func _calcular_alturas() -> void:
	var bw := largura * POR_CEL
	var bh := altura_cel * POR_CEL
	_alturas.resize(bw * bh)
	for bz in bh:
		for bx in bw:
			_alturas[bz * bw + bx] = _altura_codigo(codigo(bx / POR_CEL, bz / POR_CEL))
	var rocha := func(bx: int, bz: int) -> bool: return codigo(bx / POR_CEL, bz / POR_CEL) == "##" and altura_rocha() > 0.0
	# suavizar as colinas (rampas) sem mexer no vazio nem na água (nem nas paredes de rocha, que são a pique)
	for _passo in 3:
		var nova := _alturas.duplicate()
		for bz in bh:
			for bx in bw:
				var h := _alturas[bz * bw + bx]
				if h < -10.0 or h < 0.0 or rocha.call(bx, bz):
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
	# paredes de rocha: a beira come-se aos bocados (não fica uma linha reta de 10 m) e o topo fica irregular
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
	# pequeno relevo no chão aberto (ondulações de 0,25 m), para o mapa não ser uma mesa lisa
	var relevo := FastNoiseLite.new()
	relevo.seed = numero * 31 + 7
	relevo.frequency = 0.12
	for bz in bh:
		for bx in bw:
			var cx := bx / POR_CEL
			var cz := bz / POR_CEL
			if codigo(cx, cz) in RELEVO and not _bloco_de_caminho(codigo(cx, cz), cx, cz, bx % POR_CEL, bz % POR_CEL):
				var v := relevo.get_noise_2d(bx, bz)
				if v > 0.15:
					_alturas[bz * bw + bx] += snappedf((v - 0.15) * 1.2, 0.25)


## Liga um trilho "::" às células vizinhas: o caminho tem 3 blocos (6 m) e segue as ligações.
func _bloco_de_caminho(c: String, cx: int, cy: int, lx: int, lz: int) -> bool:
	if c == "==":
		return true
	var meio := lx >= 1 and lx <= 3 and lz >= 1 and lz <= 3
	if meio:
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


func _construir_chao() -> void:
	var bw := largura * POR_CEL
	var chao: Array = kit.get("chao", [])
	var ruido := FastNoiseLite.new()
	ruido.seed = numero
	ruido.frequency = 0.09
	var tons := FastNoiseLite.new()
	tons.seed = numero * 7 + 3
	tons.frequency = 0.05
	_mascara_agua = Image.create(bw, altura_cel * POR_CEL, false, Image.FORMAT_L8)
	var nat: bool = _natureza.has("chao") and not chao.is_empty()
	if nat:
		_splat = Image.create(bw, altura_cel * POR_CEL, false, Image.FORMAT_RGBA8)
		_alturas_img = Image.create(bw, altura_cel * POR_CEL, false, Image.FORMAT_RF)
		_chao_geo = chao[0]
	for bz in altura_cel * POR_CEL:
		for bx in bw:
			var c := codigo(bx / POR_CEL, bz / POR_CEL)
			var h := _alturas[bz * bw + bx]
			if c == "  ":
				continue
			if nat:
				_alturas_img.set_pixel(bx, bz, Color(h, 0, 0))
			var x := (bx + 0.5) * BLOCO - largura * CEL / 2.0
			var z := (bz + 0.5) * BLOCO - altura_cel * CEL / 2.0
			var peca: String
			var n := ruido.get_noise_2d(bx, bz)
			var variante: String = chao[0]
			if chao.size() > 1 and n > 0.35:
				variante = chao[1 + (bx + bz) % max(1, chao.size() - 2)]
			elif chao.size() > 2 and n < -0.45:
				variante = chao[chao.size() - 1]
			match c:
				"::", "==":
					peca = kit.get("caminho", chao)[0] if _bloco_de_caminho(c, bx / POR_CEL, bz / POR_CEL, bx % POR_CEL, bz % POR_CEL) else variante
				"%%":
					peca = kit.get("lama", "")
				"~~", "ww":
					peca = kit.get("agua", "")
					_mascara_agua.set_pixel(bx, bz, Color(1, 1, 1))
				",,":
					peca = kit.get("agua_rasa", kit.get("agua", ""))
					_mascara_agua.set_pixel(bx, bz, Color(0.62, 0.62, 0.62))
				"cc":
					peca = kit.get("nuvem_fraca", chao)[0]
				_:
					peca = variante
			if nat and peca.begins_with("res://") and not c in ["cc"]:
				# chão da natureza: uma só peça; o shader escolhe a textura pelo mapa (splat)
				var sp := Color(0, 0, 0, 0)
				if c == "##" and altura_rocha() > 0.0 and h > altura_rocha() * 0.6:
					sp.a = 1.0   # topo de parede de rocha
				if c in ["::", "=="] and peca == kit.get("caminho", chao)[0] and _bloco_de_caminho(c, bx / POR_CEL, bz / POR_CEL, bx % POR_CEL, bz % POR_CEL):
					sp.r = 1.0
				elif c in ["..", "\"\"", "**"] and n < -0.55:
					sp.g = 1.0   # clareiras de terra batida
				elif n > 0.3 and not c in ["tt", "▒▒"]:
					sp.b = 1.0
				_splat.set_pixel(bx, bz, sp)
				_por(_chao_geo, Vector3(x, h - 0.2, z))
			elif peca.begins_with("res://"):
				# tom do bloco: manchas grandes (mais claro/escuro) + um pouco de ruído por bloco
				var m := tons.get_noise_2d(bx * 0.6, bz * 0.6)
				# (as cores das instâncias não passam de 1,0: o tom vai de 0,6 a 1,0)
				# manchas: frio e escuro (zonas húmidas, sombra) <-> quente e claro (sol, erva seca)
				var t := clampf((m + 0.6) / 1.2 + _rng.randf_range(-0.06, 0.06), 0.0, 1.0)
				var tom := Color(0.62, 0.78, 0.84).lerp(Color(1.0, 1.0, 0.74), t)
				if c in ["tt", "▒▒"]:
					tom = tom.darkened(0.12)
				# clareiras de terra batida no meio da erva
				if c in ["..", "\"\""] and n < -0.62 and kit.has("caminho"):
					peca = kit.caminho[0]
				_por(peca, Vector3(x, h - 0.2, z), 0.0, 1.0, tom)
			else:
				_bloco_cor(peca if peca != "" else kit.get("agua", "#0eaf9b"), Vector3(x, h, z))
			# os lados das colinas e das margens (para não se ver o "vazio" por baixo dos blocos mais altos
			# do que o vizinho, por exemplo a terra ao pé da água)
			var baixo := -0.2
			for d: Vector2i in [Vector2i(1, 0), Vector2i(-1, 0), Vector2i(0, 1), Vector2i(0, -1)]:
				var vx: int = bx + d.x
				var vz: int = bz + d.y
				if vx >= 0 and vz >= 0 and vx < bw and vz < altura_cel * POR_CEL:
					var hv := _alturas[vz * bw + vx]
					if hv > -10.0:
						baixo = minf(baixo, hv - 0.2)
			var alto := h - 0.2
			if alto - baixo > 0.25 and (h > 0.4 or baixo < -0.25):
				var meio := Vector3(x, (alto + baixo) / 2.0, z)
				var tam := Vector3(BLOCO, alto - baixo, BLOCO)
				if nat:   # com a textura de terra/rocha do shader da natureza
					var chave := "lado|%.2f" % tam.y
					if not _cores.has(chave):
						var bm := BoxMesh.new()
						bm.size = tam
						bm.material = _material_chao()
						_cores[chave] = bm
					_instancias.get_or_add(_cores[chave], []).append(Transform3D(Basis(), meio))
				else:
					_bloco_cor(kit.get("borda_cor", "#45293f"), Vector3(x, alto, z), tam)
	if nat:   # o material pode ter sido criado a meio (lados das colinas): agora o mapa está completo
		var mc := _material_chao()
		mc.set_shader_parameter("splat", ImageTexture.create_from_image(_splat))
		mc.set_shader_parameter("alturas", ImageTexture.create_from_image(_alturas_img))
		mc.set_shader_parameter("usa_alturas", 1.0)
		mc.set_shader_parameter("bloco", BLOCO)
	if not _mats_agua.is_empty():
		var tex := ImageTexture.create_from_image(_mascara_agua)
		for m in _mats_agua:
			if regiao == 5 and _natureza.get("chao", {}).has("terra"):
				m.set_shader_parameter("gelo", 1.0)
				m.set_shader_parameter("t_gelo", load(_natureza.chao.terra))
			m.set_shader_parameter("mascara", tex)
			m.set_shader_parameter("m_origem", Vector2(-largura * CEL / 2.0, -altura_cel * CEL / 2.0))
			m.set_shader_parameter("m_tamanho", Vector2(largura * CEL, altura_cel * CEL))
			m.set_shader_parameter("usa_mascara", 1.0)


var _cores: Dictionary = {}
var _mats_agua: Array[ShaderMaterial] = []
var _mascara_agua: Image


## Água animada em pixel art: faixas de brilho que se mexem, ondulação suave e — com a máscara da água
## (1 píxel por bloco: 1 = fundo, ~0,5 = raso, 0 = terra) — água mais clara junto à margem, mais escura no
## fundo e uma linha de espuma a mexer-se encostada à terra.
static func agua_material(cor: Color, mascara: Texture2D = null, origem := Vector2.ZERO, tamanho := Vector2.ONE) -> ShaderMaterial:
	var sh := Shader.new()
	sh.code = """
shader_type spatial;
render_mode cull_back, specular_schlick_ggx;
uniform vec4 cor : source_color;
uniform vec4 brilho : source_color;
uniform sampler2D mascara : filter_linear;
uniform vec2 m_origem;
uniform vec2 m_tamanho = vec2(1.0);
uniform float usa_mascara = 0.0;
uniform float gelo = 0.0;
uniform float lava = 0.0;
uniform sampler2D t_gelo : source_color, filter_nearest, repeat_enable;
varying vec3 mundo;
float aleatorio(vec2 p) {
	return fract(sin(dot(p, vec2(12.9898, 78.233))) * 43758.5453);
}
float ruido(vec2 p) {
	vec2 i = floor(p);
	vec2 f = fract(p);
	f = f * f * (3.0 - 2.0 * f);
	return mix(mix(aleatorio(i), aleatorio(i + vec2(1.0, 0.0)), f.x), mix(aleatorio(i + vec2(0.0, 1.0)), aleatorio(i + vec2(1.0, 1.0)), f.x), f.y);
}
float bayer(vec2 p) {
	ivec2 i = ivec2(mod(p, 4.0));
	int b[16] = int[](0, 8, 2, 10, 12, 4, 14, 6, 3, 11, 1, 9, 15, 7, 13, 5);
	return float(b[i.y * 4 + i.x]) / 16.0;
}
void vertex() {
	mundo = (MODEL_MATRIX * vec4(VERTEX, 1.0)).xyz;
	VERTEX.y += (sin(mundo.x * 0.7 + TIME * 1.3) * 0.03 + cos(mundo.z * 0.6 + TIME) * 0.03) * (1.0 - gelo);
}
void fragment() {
	vec2 q = floor(mundo.xz * 16.0);   // o píxel (16 por metro, como o chão)
	float m = 0.75;
	if (usa_mascara > 0.5) {
		m = texture(mascara, ((q + 0.5) / 16.0 - m_origem) / m_tamanho).r;
	}
	// fundo mais escuro, margem mais clara, e manchas grandes que se mexem devagar: 3 tons, em degraus
	float t = clamp(smoothstep(0.35, 0.9, m) * 0.9 + (ruido(q / 40.0 + TIME * vec2(0.025, 0.012)) - 0.5) * 0.22, 0.0, 1.0);
	t = floor(t * 3.0 + 0.5) / 3.0;
	vec3 c = mix(cor.rgb * 1.1 + vec3(0.03, 0.06, 0.04), cor.rgb * 0.74, t);
	// ondinhas: tracinhos claros (com uma sombra por baixo) que vão andando e piscam
	float fila = floor(q.y / 6.0);
	float vel = 1.0 + floor(aleatorio(vec2(fila, 3.0)) * 3.0);
	float sx = q.x + floor(TIME * vel);
	float r = aleatorio(vec2(floor(sx / 12.0), fila));
	if (r < 0.4) {
		float lx = mod(sx, 12.0);
		float ly = mod(q.y, 6.0);
		float comp = 3.0 + floor(r * 10.0);
		float ligado = step(-0.2, sin(TIME * 1.4 + r * 31.0));
		if (ly == 2.0 && lx >= 2.0 && lx < 2.0 + comp) c = mix(c, brilho.rgb, 0.8 * ligado);
		else if (ly == 3.0 && lx >= 3.0 && lx < 1.0 + comp) c = mix(c, cor.rgb * 0.5, 0.45 * ligado);
	}
	// brilhos do sol que piscam
	float b = aleatorio(floor(q / 3.0) + 17.0);
	if (b > 0.995 && sin(TIME * 4.0 + b * 60.0) > 0.75) c = vec3(1.0);
	// espuma encostada à terra
	float onda = sin(TIME * 1.8 + q.x * 0.14 + q.y * 0.1) * 0.05 + sin(TIME * 0.7 - q.x * 0.06) * 0.03;
	float espuma = step(m + onda, 0.3) * usa_mascara;
	float espuma2 = step(m + onda * 1.4, 0.42) * (1.0 - espuma) * usa_mascara;
	c = mix(c, vec3(0.93, 1.0, 0.97), espuma * 0.9);
	c = mix(c, brilho.rgb, espuma2 * 0.6);
	if (gelo > 0.5) {
		// lago gelado: placas de gelo (a textura de gelo da região), neve na margem e brilhos que piscam
		c = texture(t_gelo, (q + 0.5) / 64.0).rgb;
		c = mix(c, vec3(1.0), step(m, 0.38) * usa_mascara);
		float bg = aleatorio(floor(q / 4.0));
		c = mix(c, vec3(1.0), step(0.994, bg) * step(0.6, sin(TIME * 3.0 + bg * 40.0)));
	}
	if (lava > 0.5) {
		// lava: crosta escura a boiar devagar, rachas a brilhar, lava amarela no meio e bolhas que rebentam
		float n1 = ruido(q / 22.0 + TIME * vec2(0.03, 0.018));
		float n2 = ruido(q / 7.0 - TIME * vec2(0.05, 0.03));
		float k = n1 * 0.72 + n2 * 0.28 - (1.0 - smoothstep(0.3, 0.6, m)) * 0.25 * usa_mascara;
		vec3 e = vec3(0.98, 0.76, 0.17);                    // o mais quente (amarelo)
		if (k > 0.56) e = vec3(0.18, 0.13, 0.18);           // crosta
		else if (k > 0.5) e = cor.rgb * 0.8;                // borda da crosta, ainda em brasa
		else if (k > 0.38) e = cor.rgb;
		else if (k > 0.27) e = vec3(0.98, 0.42, 0.11);
		else if (k > 0.2) e = vec3(0.97, 0.59, 0.09);
		vec2 cb = floor(q / 10.0);
		float rb = aleatorio(cb + 5.0);
		float fase = fract(TIME * 0.35 + rb * 7.0);
		if (rb < 0.12 && k < 0.5) {
			vec2 o = q - cb * 10.0 - vec2(5.0);
			float raio = fase * 3.5;
			if (abs(length(o) - raio) < 0.7 && fase < 0.85) e = vec3(0.97, 0.59, 0.09);
		}
		c = e;
		EMISSION = (k > 0.56 ? vec3(0.0) : e * 0.3);
		ROUGHNESS = 0.9;
		SPECULAR = 0.0;
	} else {
		ROUGHNESS = 0.2;
		SPECULAR = 0.6;
	}
	ALBEDO = c;
}
"""
	var m := ShaderMaterial.new()
	m.shader = sh
	m.set_shader_parameter("cor", cor)
	m.set_shader_parameter("brilho", cor.lightened(0.5))
	if cor.r > 0.7 and cor.g < 0.45 and cor.b < 0.4:   # vermelho-laranja: é lava (região 7)
		m.set_shader_parameter("lava", 1.0)
	if mascara:
		m.set_shader_parameter("mascara", mascara)
		m.set_shader_parameter("m_origem", origem)
		m.set_shader_parameter("m_tamanho", tamanho)
		m.set_shader_parameter("usa_mascara", 1.0)
	return m


## Bloco de uma só cor (água, lama, lados das colinas) quando a região não tem peça própria.
func _bloco_cor(cor: String, p: Vector3, tamanho := Vector3(BLOCO, 0.2, BLOCO)) -> void:
	var chave := "%s|%s" % [cor, tamanho]
	if not _cores.has(chave):
		var m := BoxMesh.new()
		m.size = tamanho
		if cor in [kit.get("agua", ""), kit.get("agua_rasa", "")] and tamanho.y < 0.5:
			m.material = agua_material(Color(cor))
			_mats_agua.append(m.material)
		else:
			var mat := StandardMaterial3D.new()
			mat.albedo_color = Color(cor)
			m.material = mat
		_cores[chave] = m
	# p é o topo do bloco
	_instancias.get_or_add(_cores[chave], []).append(Transform3D(Basis(), p - Vector3(0, tamanho.y / 2.0, 0)))


# ------------------------------------------------------------------ células ------------------------------------------------------------------

## Decoração por todo o chão aberto (docs/ARTE.md): tufos de erva, flores em manchas, pedrinhas, arbustos e árvores
## a fazer a passagem para as bordas, troncos e cogumelos raros. Sem colisão nas coisas pequenas.
func _decorar() -> void:
	var manchas := FastNoiseLite.new()
	manchas.seed = numero * 13 + 1
	manchas.frequency = 0.18
	var erva: Array = kit.get("erva_alta", [])
	var flores: Array = kit.get("flores", [])
	var rochas: Array = kit.get("pedras", kit.get("rocha", []))
	var mato: Array = kit.get("mato", [])
	var arvores: Array = kit.get("arvore", [])
	var grandes: Array = kit.get("gigante", [])
	var lanternas: Array = Array(_natureza.get("plantas", {}).get("objetos", [])).filter(func(x): return "lanterna" in x or "escora" in x)
	for cy in altura_cel:
		for cx in largura:
			var c := codigo(cx, cy)
			if not c in ABERTO:
				continue
			var borda := false
			for d in [Vector2i(1, 0), Vector2i(-1, 0), Vector2i(0, 1), Vector2i(0, -1)]:
				if codigo(cx + d.x, cy + d.y) in ["TT", "##"]:
					borda = true
			var n := manchas.get_noise_2d(cx * 3.0, cy * 3.0)
			# tufos de erva (mais nas manchas verdes, menos nos caminhos)
			var tufos := 3 if c == "::" else (9 if n > 0.1 else 5)
			if not erva.is_empty() and Natureza.e_sprite(erva[0]) and erva[0].get_file().begins_with("tufo"):
				tufos *= 3   # os tufos em pixel art são pequenos: mais deles
			for i in tufos:
				var p := _ponto_livre(cx, cy, c)
				if p != Vector3.INF and not erva.is_empty():
					_por(erva[_rng.randi() % erva.size()], p, _rng.randf() * TAU, _rng.randf_range(0.5, 0.95))
			# flores aos molhos
			if n > 0.35 and not flores.is_empty():
				for i in _rng.randi_range(2, 5):
					var p := _ponto_livre(cx, cy, c)
					if p != Vector3.INF:
						_por(flores[_rng.randi() % flores.size()], p, _rng.randf() * TAU, _rng.randf_range(0.6, 1.0))
			# nas grutas: lanternas ao longo dos caminhos (a luz que os mineiros deixaram)
			if escuro and c == "::" and _rng.randf() < 0.22 and not lanternas.is_empty():
				var p := _ponto_livre(cx, cy, c)   # fora do caminho, ao lado dele
				if p != Vector3.INF:
					_por(lanternas.pick_random(), p)
					_cilindro(p, 0.3)
			# pedrinhas soltas
			if _rng.randf() < 0.45 and not rochas.is_empty():
				var p := _ponto_livre(cx, cy, c)
				if p != Vector3.INF:
					_por(rochas[_rng.randi() % rochas.size()], p, _rng.randf() * TAU, _rng.randf_range(0.18, 0.35))
			# ao pé das bordas: arbustos e árvores (a floresta "entra" no mapa)
			if borda and c in ["..", "\"\"", "**", "tt", "^^"]:
				for i in 2:
					var p := _ponto_livre(cx, cy, c)
					if p != Vector3.INF and not mato.is_empty():
						_por(mato[_rng.randi() % mato.size()], p, _rng.randf() * TAU, _rng.randf_range(0.8, 1.2))
						_cilindro(p, 0.5)
				if _rng.randf() < 0.5 and not arvores.is_empty():
					var p := _ponto_livre(cx, cy, c)
					if p != Vector3.INF and not _na_clareira(p):
						var e := _rng.randf_range(0.9, 1.3)
						_por(arvores[_rng.randi() % arvores.size()], p, _rng.randf() * TAU, e)
						_cilindro(p, 0.6 * e)
			# erva alta em manchas e uma árvore solta de vez em quando
			if c == ".." and n > 0.45 and not erva.is_empty():
				for i in _rng.randi_range(6, 14):
					var p := _ponto_livre(cx, cy, c)
					if p != Vector3.INF:
						_por(erva[_rng.randi() % erva.size()], p, _rng.randf() * TAU, _rng.randf_range(1.0, 1.5))
			if c == ".." and _rng.randf() < 0.08 and not arvores.is_empty():
				var p := _ponto_livre(cx, cy, c)
				if p != Vector3.INF and p.distance_to(ponto_seguro) > 8.0 and not _na_clareira(p):
					var e := _rng.randf_range(0.8, 1.2)
					_por(arvores[_rng.randi() % arvores.size()], p, _rng.randf() * TAU, e)
					_cilindro(p, 0.6 * e)
			# coisas grandes raras (troncos caídos, cogumelos gigantes) no meio do prado
			if c == ".." and _rng.randf() < 0.035 and not grandes.is_empty():
				var p := _ponto_livre(cx, cy, c)
				if p != Vector3.INF and p.distance_to(ponto_seguro) > 10.0:
					_por(grandes[_rng.randi() % grandes.size()], p, _rng.randf() * TAU, _rng.randf_range(0.6, 0.9))
					_cilindro(p, 1.0)


## A povoação do andar (docs/CIDADES.md, secção 4): os edifícios nas células "CC" do mapa (ou, se o mapa não as
## tiver, à volta da Zona Segura), a decoração entre as casas e um largo livre no meio para a fogueira.
func _construir_povoacao() -> void:
	if _pov.is_empty():
		return
	var edificios: Array = _pov.get("edificios", [])
	var deco: Array = _pov.get("decoracao", [])
	var pontos: Array[Vector3] = []
	for c in _celulas("CC"):
		pontos.append(centro_celula(c.x, c.y))
	if pontos.is_empty():   # à volta da Zona Segura
		var base := ponto_seguro if ponto_seguro != Vector3.ZERO else centro_celula(largura / 2, altura_cel / 2)
		var sitio := celula_de(base)
		var quantos := clampi(maxi(edificios.size(), 3), 3, 6)
		var tent := 0
		while pontos.size() < quantos and tent < 200:
			tent += 1
			var c := sitio + Vector2i(_rng.randi_range(-3, 3), _rng.randi_range(-3, 3))
			if not codigo(c.x, c.y) in ["..", "\"\"", "**", "tt", "^^", "::"]:
				continue
			var p := centro_celula(c.x, c.y) + Vector3(_rng.randf_range(-2, 2), 0, _rng.randf_range(-2, 2))
			if p.distance_to(base) < 9.0 or pontos.any(func(q: Vector3): return q.distance_to(p) < 8.0):
				continue
			pontos.append(p)
	if pontos.is_empty():
		return
	var soma := Vector3.ZERO
	for p in pontos:
		soma += p
	_centro_pov = soma / pontos.size()
	# o largo do meio fica livre (fogueira e placa); se calhar em cima de uma casa, afasta-se um pouco
	if pontos.any(func(q: Vector3): return q.distance_to(_centro_pov) < 4.0):
		_centro_pov += Vector3(0, 0, 4.5)
	_centro_pov.y = altura_em(_centro_pov.x, _centro_pov.z)
	_ocupado.append(Vector4(_centro_pov.x, 0, _centro_pov.z, 3.5))
	for i in pontos.size():
		var p: Vector3 = pontos[i]
		p.y = altura_em(p.x, p.z)
		_casas.append(p)
		var raio := 2.5
		if not edificios.is_empty():
			var peca: String = edificios[i % edificios.size()]
			_por(peca, p, 0.0, 1.0)
			if Natureza.e_sprite(peca):
				raio = (load(peca) as Texture2D).get_width() / Natureza.PPM * 0.38
			else:
				var a := Pecas.caixa(peca)
				raio = clampf(maxf(a.size.x, a.size.z) * 0.45, 1.0, 5.0)
			_cilindro(p, raio)
			_casas_info.append({"pos": p, "raio": raio, "peca": peca})
		_ocupado.append(Vector4(p.x, 0, p.z, raio + 1.5))
	# decoração: cada peça ao lado de uma casa (repete-se se houver mais casas)
	for k in maxi(deco.size(), pontos.size()):
		if deco.is_empty():
			break
		var casa: Vector3 = _casas[k % _casas.size()]
		for t in 6:
			var ang := _rng.randf() * TAU
			var p := casa + Vector3(cos(ang), 0, sin(ang)) * _rng.randf_range(4.0, 6.5)
			if not codigo(celula_de(p).x, celula_de(p).y) in ABERTO + ["CC"]:
				continue
			if _ocupado.any(func(o: Vector4): return Vector2(p.x - o.x, p.z - o.z).length() < 1.6):
				continue
			p.y = altura_em(p.x, p.z)
			var peca: String = deco[k % deco.size()]
			_por(peca, p, 0.0 if Natureza.e_sprite(peca) else _rng.randf() * TAU, 1.0)
			_cilindro(p, 0.7)
			_ocupado.append(Vector4(p.x, 0, p.z, 1.6))
			break


## Por baixo das ilhas do Céu: um mar de nuvens a mexer-se; por baixo do Abismo: escuro com estrelas e névoa roxa.
func _fundo_vazio() -> void:
	var sh := Shader.new()
	sh.code = """
shader_type spatial;
render_mode unshaded, cull_disabled;
uniform sampler2D ruido : filter_linear, repeat_enable;
uniform float abismo = 0.0;
varying vec3 mundo;
float aleatorio(vec2 p) {
	return fract(sin(dot(p, vec2(12.9898, 78.233))) * 43758.5453);
}
void vertex() {
	mundo = (MODEL_MATRIX * vec4(VERTEX, 1.0)).xyz;
}
void fragment() {
	vec2 p = floor(mundo.xz * 2.0) / 2.0;   // píxeis grandes (está longe)
	float n1 = texture(ruido, p * 0.006 + TIME * vec2(0.004, 0.001)).r;
	float n2 = texture(ruido, p * 0.013 - TIME * vec2(0.002, 0.003) + 0.5).r;
	float n = n1 * 0.65 + n2 * 0.35;
	vec3 c;
	if (abismo < 0.5) {
		// nuvens: 4 tons, do azul do céu ao branco
		c = vec3(0.56, 0.83, 1.0);
		c = mix(c, vec3(0.78, 0.86, 0.82), step(0.42, n));
		c = mix(c, vec3(1.0), step(0.52, n));
		c = mix(c, vec3(0.61, 0.67, 0.70), step(0.52, n) * (1.0 - step(0.5, n2 + 0.08)) * 0.5);
	} else {
		c = vec3(0.18, 0.13, 0.18);
		c = mix(c, vec3(0.27, 0.16, 0.25), step(0.5, n));
		c = mix(c, vec3(0.42, 0.24, 0.46), step(0.62, n));
		float e = aleatorio(floor(p));
		c = mix(c, vec3(1.0), step(0.992, e) * (0.5 + 0.5 * sin(TIME * 2.0 + e * 60.0)));
		c = mix(c, vec3(0.66, 0.52, 0.95), step(0.985, e) * (1.0 - step(0.992, e)));
	}
	ALBEDO = c;
}
"""
	var m := ShaderMaterial.new()
	m.shader = sh
	m.set_shader_parameter("ruido", Natureza.ruido())
	m.set_shader_parameter("abismo", 1.0 if regiao == 10 else 0.0)
	var plano := PlaneMesh.new()
	plano.size = Vector2(largura * CEL + 400.0, altura_cel * CEL + 400.0)
	var mi := MeshInstance3D.new()
	mi.mesh = plano
	mi.material_override = m
	mi.position.y = -30.0
	mi.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
	add_child(mi)


## Mais coisas pelo chão (docs/ARTE.md 6.1): erva alta, troncos, tocos, cogumelos, objetos perdidos, arbustos,
## pequenos bosques nos prados e juncos à beira da água. Assim nenhum sítio do mapa fica vazio.
func _detalhes() -> void:
	var p_nat: Dictionary = _natureza.get("plantas", {})
	var det: Array = p_nat.get("detalhes", [])
	var obj: Array = p_nat.get("objetos", [])
	var erva_alta := det.filter(func(x: String): return "erva" in x.get_file() or "juncos" in x.get_file())
	var juncos := det.filter(func(x: String): return "juncos" in x.get_file())
	var soltos := det.filter(func(x: String): return not x in erva_alta)
	var pequenos := obj.filter(func(x: String): return x.get_file().get_basename() in ["barril", "caixote", "placa", "anfora", "cerca_partida", "abobora"])
	var mato: Array = kit.get("mato", [])
	var arvores: Array = kit.get("arvore", [])
	var bosque := FastNoiseLite.new()
	bosque.seed = numero * 31 + 5
	bosque.frequency = 0.22
	var tema: Array = _natureza.get("andares", {}).get(str(numero), [])   # o tema deste andar (cristais, teias, fungos...)
	for cy in altura_cel:
		for cx in largura:
			var c := codigo(cx, cy)
			if not tema.is_empty() and c in ABERTO and not c in ["??", "PP", "!!", "FF", "AA"]:
				var nt := bosque.get_noise_2d(cx * 1.3 + 40.0, cy * 1.3)
				if nt > -0.15:
					for t in tema:
						var quantos := float(t[1]) * (1.8 if nt > 0.3 else 0.9)
						var k := int(quantos) + (1 if _rng.randf() < fmod(quantos, 1.0) else 0)
						for i in k:
							var p := _ponto_livre(cx, cy, c)
							if p != Vector3.INF:
								_por(t[0], p)
								var nome: String = String(t[0]).get_file()
								if nome.begins_with("cristal_alto") or nome.begins_with("coluna") or nome.begins_with("estalagmites") \
										or nome.begins_with("cogumelo_gigante") or nome.begins_with("bigorna") or nome.begins_with("escora"):
									_cilindro(p, 0.5)
			var boiam: Array = p_nat.get("na_agua", [])
			if c in ["~~", ",,"] and not boiam.is_empty():   # nenúfares a boiar (em molhos)
				var nb := bosque.get_noise_2d(cx * 2.0, cy * 2.0 + 90.0)
				for i in (_rng.randi_range(3, 7) if nb > 0.0 else _rng.randi_range(0, 2)):
					var p := _ponto_aleatorio(cx, cy, 0.6)
					p.y = maxf(p.y, -0.8) + 0.02
					_por(boiam.pick_random(), p)
			if c in [",,"] and not juncos.is_empty():   # água rasa: juncos
				for i in 5:
					_por(juncos[_rng.randi() % juncos.size()], _ponto_aleatorio(cx, cy, 0.5))
				continue
			if not c in ABERTO or c in ["??", "PP", "!!", "FF", "AA"]:
				continue
			var junto_agua := false
			for d in [Vector2i(1, 0), Vector2i(-1, 0), Vector2i(0, 1), Vector2i(0, -1)]:
				if codigo(cx + d.x, cy + d.y) in ["~~", ",,", "ww"]:
					junto_agua = true
			var n := bosque.get_noise_2d(cx, cy)
			if not erva_alta.is_empty():
				for i in (_rng.randi_range(2, 5) if n > 0.0 or junto_agua else _rng.randi_range(0, 2)):
					var p := _ponto_livre(cx, cy, c)
					if p != Vector3.INF:
						_por((juncos if junto_agua and not juncos.is_empty() else erva_alta)[_rng.randi() % (juncos.size() if junto_agua and not juncos.is_empty() else erva_alta.size())], p)
			if not soltos.is_empty() and _rng.randf() < 0.35:
				var p := _ponto_livre(cx, cy, c)
				if p != Vector3.INF:
					var peca: String = soltos[_rng.randi() % soltos.size()]
					_por(peca, p)
					if "tronco" in peca.get_file():
						_cilindro(p, 0.9)
			if not pequenos.is_empty() and _rng.randf() < 0.06:
				var p := _ponto_livre(cx, cy, c)
				if p != Vector3.INF:
					_por(pequenos[_rng.randi() % pequenos.size()], p)
					_cilindro(p, 0.4)
			if not mato.is_empty() and _rng.randf() < 0.4:
				var p := _ponto_livre(cx, cy, c)
				if p != Vector3.INF:
					_por(mato[_rng.randi() % mato.size()], p)
			# pequenos bosques no meio dos prados (onde o ruído é alto)
			if c in ["..", "\"\""] and n > 0.45 and not arvores.is_empty() and Natureza.e_sprite(arvores[0]):
				var centro := centro_celula(cx, cy)
				if ponto_seguro == Vector3.ZERO or centro.distance_to(ponto_seguro) > 12.0:
					for i in _rng.randi_range(2, 4):
						var p := _ponto_livre(cx, cy, c)
						if p != Vector3.INF and not _na_clareira(p):
							_por(arvores[_rng.randi() % arvores.size()], p)
							_cilindro(p, 0.6)


## Cenários: pequenos grupos de objetos que contam uma história (acampamento abandonado, ruína, círculo de
## cogumelos, carroça partida...), em prados abertos, longe da Zona Segura e uns dos outros.
func _cenarios() -> void:
	var lista: Array = _natureza.get("cenarios", [])
	if lista.is_empty():
		return
	var candidatas: Array[Vector2i] = []
	for cy in range(1, altura_cel - 1):
		for cx in range(1, largura - 1):
			if not codigo(cx, cy) in ["..", "\"\"", "^^"]:
				continue
			var livre := true
			for dy in [-1, 0, 1]:
				for dx in [-1, 0, 1]:
					if not codigo(cx + dx, cy + dy) in ABERTO:
						livre = false
			if livre:
				candidatas.append(Vector2i(cx, cy))
	candidatas.shuffle()
	var postos: Array[Vector3] = []
	var maximo := clampi(celulas_abertas().size() / 14, 2, 9)
	for c in candidatas:
		if postos.size() >= maximo:
			break
		var centro := centro_celula(c.x, c.y) + Vector3(_rng.randf_range(-1.5, 1.5), 0, _rng.randf_range(-1.5, 1.5))
		if ponto_seguro != Vector3.ZERO and centro.distance_to(ponto_seguro) < 14.0:
			continue
		if postos.any(func(p: Vector3): return p.distance_to(centro) < 22.0):
			continue
		if _ocupado.any(func(o: Vector4): return Vector2(centro.x - o.x, centro.z - o.z).length() < o.w + 6.0):
			continue
		postos.append(centro)
		var cen: Dictionary = lista[_rng.randi() % lista.size()]
		var espelho := -1.0 if _rng.randf() < 0.5 else 1.0
		for peca in cen.get("pecas", []):
			var p := centro + Vector3(float(peca[1]) * espelho, 0, float(peca[2]))
			p.y = altura_em(p.x, p.z)
			_por(peca[0], p)
			if float(peca[3]) > 0.0:
				_cilindro(p, float(peca[3]))


## À volta do mapa: o chão continua (mais escuro) e há uma floresta (ou falésias) de várias filas,
## para nunca se ver o vazio. No Céu e no Abismo a borda é mesmo o vazio.
func _bordas() -> void:
	var fora: String = _natureza.get("fora", "chao")
	if fora == "nada":
		_fundo_vazio()
		return
	var meia := Vector2(largura * CEL / 2.0, altura_cel * CEL / 2.0)
	# 4 faixas à volta do mapa (não por baixo: senão tapava os rios, que ficam mais fundos)
	var margem := 45.0
	var faixas := [
		[Vector2(largura * CEL + margem * 2.0, margem), Vector2(0, -meia.y - margem / 2.0)],
		[Vector2(largura * CEL + margem * 2.0, margem), Vector2(0, meia.y + margem / 2.0)],
		[Vector2(margem, altura_cel * CEL), Vector2(-meia.x - margem / 2.0, 0)],
		[Vector2(margem, altura_cel * CEL), Vector2(meia.x + margem / 2.0, 0)],
	]
	var mat: Material
	var y := -0.06 if altura_rocha() <= 0.0 else altura_rocha() - 0.2
	if fora == "agua":
		y = -0.35
		mat = agua_material(Color(kit.get("agua", "#0b8a8f")))
	elif _splat:
		mat = _material_chao()
	else:
		var sm := StandardMaterial3D.new()
		sm.albedo_color = Color(kit.get("borda_cor", "#2e222f"))
		mat = sm
	for f in faixas:
		var plano := PlaneMesh.new()
		plano.size = f[0]
		var mi := MeshInstance3D.new()
		mi.mesh = plano
		mi.position = Vector3(f[1].x, y, f[1].y)
		mi.material_override = mat
		mi.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
		add_child(mi)
	var lim: Array = kit.get("limite", [])
	if lim.is_empty() or fora == "agua":
		return
	var sprite := Natureza.e_sprite(lim[0])
	var passo := 2.3 if sprite else 7.0
	for fila in (6 if sprite else 2):
		var d := 0.6 + fila * passo * 0.8
		var pontos: Array[Vector3] = []
		var x := -meia.x - d
		while x <= meia.x + d:
			pontos.append(Vector3(x, 0, -meia.y - d))
			pontos.append(Vector3(x, 0, meia.y + d))
			x += passo
		var z := -meia.y - d + passo
		while z < meia.y + d:
			pontos.append(Vector3(-meia.x - d, 0, z))
			pontos.append(Vector3(meia.x + d, 0, z))
			z += passo
		for p in pontos:
			p += Vector3(_rng.randf_range(-0.9, 0.9), 0, _rng.randf_range(-0.9, 0.9))
			_por(lim[_rng.randi() % lim.size()], p, _rng.randf() * TAU, _rng.randf_range(1.2, 1.8))


# ------------------------------------------------------------------ para a vida (bichos) ------------------------------------------------------------------

const CHAO_BICHOS := ["..", "\"\"", "**", "tt", "::", "^^", "mm", "%%", "▒▒"]
var _abertas: Array[Vector2i] = []


func celulas_abertas() -> Array[Vector2i]:
	if _abertas.is_empty():
		for c in CHAO_BICHOS:
			_abertas.append_array(_celulas(c))
	return _abertas


## Um ponto de chão aberto ao acaso (longe de "longe_de", se for dado). INF se não houver.
func ponto_bicho(longe_de: Vector3, distancia: float) -> Vector3:
	var lista := celulas_abertas()
	if lista.is_empty():
		return Vector3.INF
	for i in 12:
		var c: Vector2i = lista[randi() % lista.size()]
		var p := _ponto_aleatorio(c.x, c.y, 1.0)
		if longe_de == Vector3.INF or Vector2(p.x - longe_de.x, p.z - longe_de.z).length() >= distancia:
			return p
	return Vector3.INF


func ponto_aberto(p: Vector3) -> bool:
	var c := celula_de(p)
	return codigo(c.x, c.y) in CHAO_BICHOS


func pontos_agua() -> Array[Vector3]:
	var r: Array[Vector3] = []
	for marca in ["~~", "ww", ",,"]:
		for c in _celulas(marca):
			r.append(centro_celula(c.x, c.y))
	return r


## Um ponto ao acaso na célula que não fica em cima do caminho (devolve INF se calhar no caminho).
func _ponto_livre(cx: int, cy: int, c: String) -> Vector3:
	var p := _ponto_aleatorio(cx, cy, 0.4)
	var base := centro_celula(cx, cy)
	var lx := int(floor((p.x - base.x + CEL / 2.0) / BLOCO))
	var lz := int(floor((p.z - base.z + CEL / 2.0) / BLOCO))
	if c == "::" and _bloco_de_caminho(c, cx, cy, clampi(lx, 0, POR_CEL - 1), clampi(lz, 0, POR_CEL - 1)):
		return Vector3.INF
	if ponto_seguro != Vector3.ZERO and p.distance_to(ponto_seguro) < 4.0:
		return Vector3.INF
	for o in _ocupado:   # casas e fogueira das povoações
		if Vector2(p.x - o.x, p.z - o.z).length() < o.w:
			return Vector3.INF
	return p


func _construir_celulas() -> void:
	_clareiras.clear()   # à volta da chegada e da Zona Segura não nascem árvores (nem à frente delas, a tapar a vista)
	for cy in altura_cel:
		for cx in largura:
			if codigo(cx, cy) in ["EE", "SS"]:
				_clareiras.append(centro_celula(cx, cy))
	for cy in altura_cel:
		for cx in largura:
			var c := codigo(cx, cy)
			match c:
				"TT":
					var lim: Array = kit.get("limite", [])
					_encher(cx, cy, lim, 9 if not lim.is_empty() and Natureza.e_sprite(lim[0]) else 3, 1.3, 1.7, kit.get("mato", []))
					_parede(cx, cy)
				"tt", "▒▒":
					var arv: Array = kit.get("arvore", [])
					var mais := 3 if not arv.is_empty() and Natureza.e_sprite(arv[0]) else 0
					_espalhar(cx, cy, arv, _rng.randi_range(2, 4) + mais, 0.8, 1.4, 0.7, false, true)
					_espalhar(cx, cy, kit.get("mato", []), _rng.randi_range(1, 3), 0.7, 1.1, 0.0)
				"##":
					var roc: Array = kit.get("rocha", [])
					if altura_rocha() > 0.0:   # parede de rocha a sério: a colisão do chão já a tem
						if escuro:
							if _rng.randf() < 0.35:
								_encher(cx, cy, roc, 1, 0.8, 1.3)
						else:   # à luz do dia: rochas por cima (o topo não fica um bloco liso)
							_encher(cx, cy, roc, 4, 1.1, 1.8)
					else:
						_encher(cx, cy, roc, 7 if not roc.is_empty() and Natureza.e_sprite(roc[0]) else 4, 1.4, 2.2)
						_parede(cx, cy)
				"\"\"":
					_espalhar(cx, cy, kit.get("erva_alta", []), 45, 1.0, 1.6, 0.0)
				"**":
					_espalhar(cx, cy, kit.get("flores", []), 8, 0.9, 1.2, 0.0)
				"()":
					_espalhar(cx, cy, kit.get("gigante", []), 1, 1.6, 2.0, 1.6)
				"CC":
					if _pov.is_empty():   # com povoação, as casas são as dela (_construir_povoacao)
						_espalhar(cx, cy, kit.get("casa", []), 1, 1.0, 1.0, 2.6, true)
				"mm":
					_espalhar(cx, cy, kit.get("mato", []), 4, 1.0, 1.3, 0.8)
				"rr":
					_no_recolha(_ponto_aleatorio(cx, cy, 2.0), "picareta")
				"~~", "ww":
					_parede(cx, cy, 2.0)
				"==":
					_ponte(cx, cy)


## baixos: na clareira da chegada / Zona Segura (_na_clareira) põe-se isto (arbustos) em vez das árvores altas.
func _encher(cx: int, cy: int, pecas: Array, n: int, e0: float, e1: float, baixos: Array = []) -> void:
	if pecas.is_empty():
		return
	for i in n:
		var p := _ponto_aleatorio(cx, cy, 1.5)
		if not baixos.is_empty() and _na_clareira(p):
			_por(baixos[_rng.randi() % baixos.size()], p, _rng.randf() * TAU, _rng.randf_range(1.0, 1.4))
			continue
		_por(pecas[_rng.randi() % pecas.size()], p, _rng.randf() * TAU, _rng.randf_range(e0, e1))


var _clareiras: Array[Vector3] = []


## Uma árvore aqui taparia a chegada / a Zona Segura (perto, ou à frente delas, do lado da câmara)?
func _na_clareira(p: Vector3) -> bool:
	for k in _clareiras:
		var d := p - k
		if Vector2(d.x, d.z).length() < 5.5 or (d.z > 0.0 and d.z < 11.5 and absf(d.x) < 6.0):
			return true
	return false


func _espalhar(cx: int, cy: int, pecas: Array, n: int, e0: float, e1: float, raio_colisao: float, centro: bool = false,
		arvores: bool = false) -> void:
	if pecas.is_empty():
		return
	for i in n:
		var p := centro_celula(cx, cy) if centro else _ponto_aleatorio(cx, cy, 1.2)
		if arvores and _na_clareira(p):
			var baixos: Array = kit.get("mato", [])
			if not baixos.is_empty():
				_por(baixos[_rng.randi() % baixos.size()], p, _rng.randf() * TAU, _rng.randf_range(0.9, 1.2))
			continue
		var e := _rng.randf_range(e0, e1)
		_por(pecas[_rng.randi() % pecas.size()], p, (_rng.randi() % 4) * PI / 2.0 if centro else _rng.randf() * TAU, e)
		if raio_colisao > 0.0:
			_cilindro(p, raio_colisao * e)


var paredes_agua: Array[CollisionShape3D] = []   # as paredes da água funda (o puzzle das comportas tira-as)


func _parede(cx: int, cy: int, altura: float = 8.0) -> void:
	var f := CollisionShape3D.new()
	var b := BoxShape3D.new()
	b.size = Vector3(CEL, altura, CEL)
	f.shape = b
	f.position = centro_celula(cx, cy) + Vector3(0, altura / 2.0 - 1.0, 0)
	_corpo_estatico.add_child(f)
	if codigo(cx, cy) in ["~~", "ww"]:
		paredes_agua.append(f)


## A água "baixa" (puzzle das comportas): já se passa a pé e a água fica clara (rasa).
func baixar_agua() -> void:
	for f in paredes_agua:
		if is_instance_valid(f):
			f.queue_free()
	paredes_agua.clear()
	if _mascara_agua:
		for y in _mascara_agua.get_height():
			for x in _mascara_agua.get_width():
				if _mascara_agua.get_pixel(x, y).r > 0.9:
					_mascara_agua.set_pixel(x, y, Color(0.6, 0.6, 0.6))
		var tex := ImageTexture.create_from_image(_mascara_agua)
		for m in _mats_agua:
			m.set_shader_parameter("mascara", tex)


## Um baú posto mais tarde (prémio de um puzzle).
func bau_em(p: Vector3, tipo: String) -> void:
	_bau(p, tipo)


func _cilindro(p: Vector3, raio: float) -> void:
	var f := CollisionShape3D.new()
	var c := CylinderShape3D.new()
	c.radius = raio
	c.height = 6.0
	f.shape = c
	f.position = p + Vector3(0, 3.0, 0)
	_corpo_estatico.add_child(f)


func _ponte(cx: int, cy: int) -> void:
	# a ponte vai na direção das outras células "==" ou da terra à volta
	var horizontal := codigo(cx - 1, cy) in ["==", "..", "::"] or codigo(cx + 1, cy) in ["==", "..", "::"]
	var c := centro_celula(cx, cy)
	c.y = 0.0
	for i in range(-1, 2):
		var p := c + (Vector3(i * 3.4, 0, 0) if horizontal else Vector3(0, 0, i * 3.4))
		_por(kit.get("ponte", [""])[0], p, PI / 2.0 if horizontal else 0.0, 1.0)
	var f := CollisionShape3D.new()
	var b := BoxShape3D.new()
	b.size = Vector3(CEL, 0.4, 3.0) if horizontal else Vector3(3.0, 0.4, CEL)
	f.shape = b
	f.position = c + Vector3(0, 0.25, 0)
	_corpo_estatico.add_child(f)


# ------------------------------------------------------------------ pontos (zona segura, escada, guardião...) ------------------------------------------------------------------

func _pontos() -> void:
	var tem_chegada := false
	for cy in altura_cel:
		for cx in largura:
			var c := codigo(cx, cy)
			var p := centro_celula(cx, cy)
			match c:
				"EE":
					ponto_chegada = p + Vector3(0, 0, 3)
					tem_chegada = true
					_por(kit.get("escada", ""), p, PI, 1.0)
				"SS":
					ponto_seguro = p
					_por(kit.get("fogueira", ""), p)
					var fog := Estacao.new()   # na fogueira cozinham-se os pratos simples (🔥)
					fog.estacao = "fogueira"
					fog.position = p
					add_child(fog)
					_por(kit.get("cristal", ""), p + Vector3(3, 0, -2))
					var cr := Interagivel.new()   # o cristal: guarda o andar para o teletransporte e leva a Ascendia
					cr.texto = "Cristal de teletransporte"
					cr.position = p + Vector3(3, 0, -2)
					add_child(cr)
					cr.usado.connect(func(_j): _cristal())
				">>":
					_escada(p)
				"$$":
					var t := _texto_ponto(cx, cy)
					# os baús que são prémio de um puzzle ou segredo só aparecem quando se resolve (segredos.gd)
					if not ("puzzle" in t or "abre" in t or "precisa" in t or numero in Segredos.BAUS_PREMIO):
						_bau(p, "ouro" if "ouro" in t else "prata")
	_pecas_especiais()
	if not tem_chegada:
		ponto_chegada = ponto_seguro + Vector3(0, 0, 3.5) if ponto_seguro != Vector3.ZERO else _primeira_celula_livre()
	if ponto_seguro == Vector3.ZERO:
		ponto_seguro = ponto_chegada


## As peças especiais do andar (arte/regioes/<região>/andares/aNN_*.glb) vão para os pontos especiais
## do mapa (segredos, puzzles, sítios da história...); as que sobram ficam em células abertas.
func _pecas_especiais() -> void:
	var pasta := "res://arte/regioes/%s/andares/" % kit.get("chao", [""])[0].get_base_dir().get_base_dir().get_file()
	var prefixo := "a%02d_" % numero if numero < 100 else "a%d_" % numero
	var pecas: Array[String] = []
	if not DirAccess.dir_exists_absolute(pasta):
		return
	# ResourceLoader.list_directory também funciona nas builds (lá os .glb só existem como .import)
	var usadas: Array = Segredos.USADAS.get(numero, [])   # as dos puzzles põe-nas o segredos.gd
	for f in ResourceLoader.list_directory(pasta):
		if f.begins_with(prefixo) and f.ends_with(".glb") and not f.trim_prefix(prefixo).get_basename() in usadas:
			pecas.append(pasta + f)
	pecas.sort()
	var sitios: Array[Vector2i] = []
	for marca in ["<>", "[]", "AA", "@@", "vv", "FF", "HH", "JJ", "CC", "()", "??", "!!"]:   # os puzzles por último
		sitios.append_array(_celulas(marca))
	var i := 0
	for peca in pecas:
		var c: Vector2i
		if i < sitios.size():
			c = sitios[i]
		else:
			var abertas := _celulas("..")
			if abertas.is_empty():
				break
			c = abertas[_rng.randi() % abertas.size()]
		var p := centro_celula(c.x, c.y)
		var a := Pecas.caixa(peca)
		if a.size.y > 3.5:   # peças grandes: ficam transparentes quando tapam o herói (câmara)
			var no: Node3D = (load(peca) as PackedScene).instantiate()
			no.position = p
			no.rotation.y = (_rng.randi() % 4) * PI / 2.0
			add_child(no)
			no.add_to_group("tapa_vista")
			no.set_meta("raio", maxf(a.size.x, a.size.z) * 0.55)
			no.set_meta("altura", a.size.y * 0.5)
		else:
			_por(peca, p, (_rng.randi() % 4) * PI / 2.0)
		if escuro:
			LuzesGruta.registar(peca, p)
		_cilindro(p, 1.5)
		i += 1


func _texto_ponto(cx: int, cy: int) -> String:
	for p in dados.get("pontos", []):
		if int(p.x) == cx and int(p.y) == cy:
			return String(p.texto).to_lower()
	return ""


func _bau(p: Vector3, tipo: String) -> void:
	var b := Bau.new()
	b.tipo = tipo
	b.andar = numero
	b.regiao = regiao
	b.modelo = kit.get("bau", "")
	b.position = p
	b.rotation.y = PI
	add_child(b)


## Baús de madeira espalhados (6–10 por andar) em células abertas, longe da Zona Segura.
func _baus_madeira() -> void:
	var abertas := _celulas("..")
	abertas.append_array(_celulas("\"\""))
	if abertas.is_empty():
		return
	var lim: Array = Dados.c("baus_madeira", [6, 10])
	for i in _rng.randi_range(int(lim[0]), int(lim[1])):
		var c: Vector2i = abertas[_rng.randi() % abertas.size()]
		var p := _ponto_aleatorio(c.x, c.y, 2.0)
		if p.distance_to(ponto_seguro) > 12.0:
			_bau(p, "madeira")


## A página do diário do Aren deste andar (marca PP no mapa); a 1.ª só depois da missão H_03.
func _pagina() -> void:
	var pp := _celulas("PP")
	if pp.is_empty() or numero in Jogo.paginas or (numero == 1 and not Jogo.tem_flag("missao_H_03")):
		return
	var p := centro_celula(pp[0].x, pp[0].y)
	var s := Sprite3D.new()
	s.texture = load("res://arte/icones/pagina_diario.png")
	s.billboard = BaseMaterial3D.BILLBOARD_ENABLED
	s.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
	s.pixel_size = 0.04
	s.shaded = false
	s.position = p + Vector3(0, 0.6, 0)
	add_child(s)
	var luz := OmniLight3D.new()   # brilha com uma luz branca fraca
	luz.light_energy = 0.6
	luz.omni_range = 4.0
	luz.position = p + Vector3(0, 1.0, 0)
	add_child(luz)
	var t := s.create_tween().set_loops()
	t.tween_property(s, "position:y", p.y + 0.9, 1.2).set_trans(Tween.TRANS_SINE)
	t.tween_property(s, "position:y", p.y + 0.6, 1.2).set_trans(Tween.TRANS_SINE)
	var i := Interagivel.new()
	i.texto = "Apanhar a página"
	i.position = p
	add_child(i)
	i.usado.connect(func(_j):
		Colecoes.pagina(numero)
		s.queue_free()
		luz.queue_free()
		i.queue_free()
		var ui = get_tree().get_first_node_in_group("pagina_ui")
		if ui:
			ui.mostrar(numero))


## Sítios de pesca: bordas de água (~~, ,, e ww) ao pé de chão onde se anda (até 4 por andar).
func _sitios_pesca() -> void:
	var agua := _celulas("~~")
	agua.append_array(_celulas(",,"))
	agua.append_array(_celulas("ww"))
	var feitos := 0
	agua.shuffle()
	for c in agua:
		if feitos >= 4:
			break
		for d in [Vector2i(0, 1), Vector2i(1, 0), Vector2i(-1, 0), Vector2i(0, -1)]:
			var v: Vector2i = c + d
			if codigo(v.x, v.y) in ["..", "::", "\"\"", "**", "tt"]:
				var p := centro_celula(v.x, v.y) - Vector3(d.x, 0, d.y) * 3.5
				var i := Interagivel.new()
				i.texto = "Pescar"
				i.position = p
				add_child(i)
				i.usado.connect(func(_j):
					var ui = get_tree().get_first_node_in_group("pesca_ui")
					if ui:
						ui.pescar(numero, false))
				feitos += 1
				break


## Recursos deste andar (dados/recursos.json), por ferramenta. Os raros só às vezes.
func _recursos(ferramenta: String) -> Array:
	var r := []
	for x in Dados.lista_simples("recursos"):
		if x.ferramenta == ferramenta and float(numero) in x.andares:
			r.append(x)
	return r


## Os nós de recursos comuns não estão nos mapas: sorteiam-se ao entrar (docs/mapas/README.md).
func _nos_recolha() -> void:
	var livres := _celulas("..")
	livres.append_array(_celulas("tt"))
	livres.append_array(_celulas("\"\""))
	livres.append_array(_celulas("**"))
	if livres.is_empty():
		return
	var lim: Array = Dados.c("nos_por_andar", [10, 18])
	for i in _rng.randi_range(int(lim[0]), int(lim[1])):
		var c: Vector2i = livres[_rng.randi() % livres.size()]
		var p := _ponto_aleatorio(c.x, c.y, 2.0)
		if p.distance_to(ponto_seguro) < 8.0:
			continue
		var tipo: String = ["mao", "mao", "mao", "picareta", "machado"][_rng.randi() % 5]
		if codigo(c.x, c.y) == "tt":
			tipo = "machado"
		_no_recolha(p, tipo)


func _no_recolha(p: Vector3, ferramenta: String) -> void:
	var lista := _recursos(ferramenta)
	var comuns := lista.filter(func(x): return not x.raro)
	if comuns.is_empty():
		return
	var r: Dictionary = comuns[_rng.randi() % comuns.size()]
	var n := NoRecolha.new()
	n.item = r.item
	n.ferramenta = ferramenta
	n.tier = int(r.get("tier", regiao))
	n.raros = lista.filter(func(x): return x.raro).map(func(x): return x.item)
	match ferramenta:
		"picareta":
			var m: Array = kit.get("minerio", kit.get("rocha", []))
			n.modelo = m[_rng.randi() % m.size()] if not m.is_empty() else ""
		"machado":
			var a: Array = kit.get("arvore", [])
			n.modelo = a[0] if not a.is_empty() else ""
	n.position = p
	n.rotation.y = _rng.randf() * TAU
	add_child(n)


func _primeira_celula_livre() -> Vector3:
	for cy in range(altura_cel - 1, -1, -1):
		for cx in largura:
			if codigo(cx, cy) == "..":
				return centro_celula(cx, cy)
	return Vector3.ZERO


func _escada(p: Vector3) -> void:
	_por(kit.get("escada", ""), p, 0.0, 1.0)
	escada = Area3D.new()
	escada.collision_layer = 1 << 6
	escada.collision_mask = 1 << 1
	var f := CollisionShape3D.new()
	var b := BoxShape3D.new()
	b.size = Vector3(3, 3, 3)
	f.shape = b
	f.position.y = 1.5
	escada.add_child(f)
	escada.position = p
	add_child(escada)
	escada.body_entered.connect(_na_escada)


func _na_escada(corpo: Node) -> void:
	if not corpo is Jogador:
		return
	if not escada_livre:
		Sistema.mensagem("A escada está fechada. Derrota o guardião do andar.", "aviso")
		return
	if numero >= 100:
		Sistema.mensagem("Chegaste ao topo da torre.", "historia")
		return
	Jogo.andar_atual = numero + 1
	Jogo.andar_maximo = max(Jogo.andar_maximo, numero + 1)
	Cenas.mudar("res://cenas/mundo/andar.tscn")


# ------------------------------------------------------------------ monstros ------------------------------------------------------------------

func _monstros() -> void:
	var zonas: Array = dados.get("zonas", [])
	var usou := false
	for z in zonas:
		var lista: Array = z.get("monstros", [])
		var r = z.get("rect")
		if lista.is_empty() or r == null:
			continue
		var area := (int(r[2]) - int(r[0]) + 1) * (int(r[3]) - int(r[1]) + 1)
		var n: int = clamp(area / 3, 2, 10)
		var de_agora := lista.filter(func(m): return Tempo.e_noite() or not Dados.monstro(m).get("noturno", false))
		if de_agora.is_empty():
			continue
		for i in n:
			var id: String = de_agora[_rng.randi() % de_agora.size()]
			_por_monstro(id, int(r[0]), int(r[1]), int(r[2]), int(r[3]))
			usou = true
	if not usou:
		var lista: Array = dados.get("monstros", [])
		for i in min(30, largura * altura_cel / 6):
			if lista.is_empty():
				break
			_por_monstro(lista[_rng.randi() % lista.size()], 0, 0, largura - 1, altura_cel - 1)
	# o guardião guarda a escada; nos andares de boss, o boss está na arena (BB)
	var g = dados.get("guardiao")
	var b = dados.get("boss")
	var gg := _celulas("GG")
	var bb := _celulas("BB")
	if g and not (gg.is_empty() and bb.is_empty()):
		guardiao = Monstro.new().configurar(g, nivel + 1, "guardiao")
		guardiao.position = (centro_celula(gg[0].x, gg[0].y) if not gg.is_empty() else _meio(bb)) + Vector3(0, 0.5, 0)
	elif b and not bb.is_empty():
		var tipo_b: String = Dados.obter("bosses", b).get("tipo", "boss")
		var extra := 3 if tipo_b == "boss" else 2
		var boss: Boss = Boss.new().configurar(b, int(Dados.obter("bosses", b).get("nivel", nivel + extra)), tipo_b)
		boss.position = _meio(bb) + Vector3(0, 0.5, 0)
		boss.arena_centro = _meio(bb)
		guardiao = boss
	if guardiao:
		add_child(guardiao)
		guardiao.morreu.connect(_guardiao_morreu)
	escada_livre = guardiao == null
	# sem escada no mapa: abre-se no sítio do guardião (ex.: a escada de luz do andar 1)
	if escada == null and numero < 100:
		var sitio := gg if not gg.is_empty() else (bb if not bb.is_empty() else [])
		if not sitio.is_empty():
			_escada(centro_celula(sitio[0].x, sitio[0].y) + Vector3(0, 0, -3))


func _meio(celulas: Array[Vector2i]) -> Vector3:
	var soma := Vector3.ZERO
	for c in celulas:
		soma += centro_celula(c.x, c.y)
	return soma / max(1, celulas.size())


func _celulas(marca: String) -> Array[Vector2i]:
	var r: Array[Vector2i] = []
	for cy in altura_cel:
		for cx in largura:
			if codigo(cx, cy) == marca:
				r.append(Vector2i(cx, cy))
	return r


func _por_monstro(id: String, x0: int, y0: int, x1: int, y1: int) -> void:
	if Dados.monstro(id).is_empty():
		return
	for tentativa in 12:
		var cx := _rng.randi_range(x0, x1)
		var cy := _rng.randi_range(y0, y1)
		var c := codigo(cx, cy)
		if not c in PASSA or c in SEM_MONSTROS:
			continue
		var p := _ponto_aleatorio(cx, cy, 1.5)
		if p.distance_to(ponto_seguro) < 14.0 or p.distance_to(ponto_chegada) < 10.0:
			continue
		if not _casas.is_empty() and p.distance_to(_centro_pov) < 26.0:   # a povoação é um sítio seguro
			continue
		var extra := "elite" if _rng.randf() < float(Dados.c("elite_hipotese")) else ""
		var m := Monstro.new().configurar(id, nivel + _rng.randi_range(-1, 1), extra)
		m.position = p + Vector3(0, 0.5, 0)
		add_child(m)
		return


func _guardiao_morreu(_m: Monstro) -> void:
	escada_livre = true
	Sistema.mensagem("O guardião caiu. A escada para o andar %d está aberta!" % (numero + 1), "historia")
	guardiao_vencido.emit()
	escada_aberta.emit()


# ------------------------------------------------------------------ jogador ------------------------------------------------------------------

func _jogador() -> void:
	jogador = preload("res://cenas/personagens/jogador.tscn").instantiate()
	jogador.position = ponto_chegada + Vector3(0, 0.5, 0)
	add_child(jogador)
	camara = Camara.new()
	camara.alvo = jogador
	add_child(camara)
	add_child(preload("res://cenas/ui/hud.tscn").instantiate())


# ------------------------------------------------------------------ peças (MultiMesh) ------------------------------------------------------------------

func _por(caminho: String, p: Vector3, rot_y: float = 0.0, escala: float = 1.0, tom := Color(-1, 0, 0)) -> void:
	if caminho == "" or not ResourceLoader.exists(caminho):
		return
	if escuro:
		LuzesGruta.registar(caminho, p)
	if Natureza.e_sprite(caminho):
		# plantas em pixel art: de frente para a câmara, tamanho real (sem escalar os píxeis), às vezes ao espelho
		_instancias.get_or_add(caminho, []).append(Transform3D(Basis.from_scale(Vector3(-1.0 if _rng.randf() < 0.5 else 1.0, 1, 1)), p))
		return
	var t := Transform3D(Basis(Vector3.UP, rot_y).scaled(Vector3.ONE * escala), p)
	_instancias.get_or_add(caminho, []).append(t)
	if tom.r >= 0.0 or _tons.has(caminho):
		var lista: Array = _tons.get_or_add(caminho, [])
		while lista.size() < _instancias[caminho].size() - 1:
			lista.append(Color.WHITE)
		lista.append(tom if tom.r >= 0.0 else Color.WHITE)


## As peças repetidas (chão, árvores, erva...) desenham-se com MultiMesh: uma por malha.
func _criar_instancias() -> void:
	for chave in _instancias:
		var transformacoes: Array = _instancias[chave]
		var malhas: Array = []
		if chave is Mesh:
			malhas = [[chave, Transform3D()]]
		elif Natureza.e_sprite(chave):
			malhas = [[Natureza.malha_planta(chave), Transform3D()]]
		else:
			malhas = _malhas_de(chave)
		var parte := 0
		for par in malhas:
			var mm := MultiMesh.new()
			mm.transform_format = MultiMesh.TRANSFORM_3D
			mm.mesh = par[0]
			var tons: Array = _tons.get(chave, [])
			mm.use_colors = not tons.is_empty()
			mm.instance_count = transformacoes.size()
			for i in transformacoes.size():
				mm.set_instance_transform(i, transformacoes[i] * par[1])
				if mm.use_colors:
					mm.set_instance_color(i, tons[i] if i < tons.size() else Color.WHITE)
			var mi := MultiMeshInstance3D.new()
			mi.multimesh = mm
			if chave is String and not Natureza.e_sprite(chave):   # para a vista 2D saber de que peça é
				mi.set_meta("glb", chave)
				mi.set_meta("parte", parte)
				mi.set_meta("parte_t", par[1])
				if chave == _chao_geo:
					mi.set_meta("chao", true)
			elif chave is Mesh:
				mi.set_meta("chao", true)   # blocos de cor e lados das colinas: a vista 2D tem o chão dela
			parte += 1
			if chave is String and chave == _chao_geo and _splat:
				mi.material_override = _material_chao()
			elif mm.use_colors and (par[0] as Mesh).get_surface_count() == 1:
				# o tom de cada bloco multiplica a textura (manchas mais claras e mais escuras no chão)
				var base = (par[0] as Mesh).surface_get_material(0)
				if base is StandardMaterial3D:
					var m: StandardMaterial3D = base.duplicate()
					m.vertex_color_use_as_albedo = true
					mi.material_override = m
			add_child(mi)
	_instancias.clear()
	_tons.clear()


var _mat_chao: ShaderMaterial


func _material_chao() -> ShaderMaterial:
	if _mat_chao == null:
		_mat_chao = Natureza.material_chao(regiao, ImageTexture.create_from_image(_splat),
				Vector2(-largura * CEL / 2.0, -altura_cel * CEL / 2.0), Vector2(largura * CEL, altura_cel * CEL))
	return _mat_chao


func _malhas_de(caminho: String) -> Array:
	if _cache_mesh.has(caminho):
		return _cache_mesh[caminho]
	var lista: Array = []
	var cena: PackedScene = load(caminho)
	var no := cena.instantiate()
	_recolher_malhas(no, Transform3D(), lista)
	no.free()
	_cache_mesh[caminho] = lista
	return lista


func _recolher_malhas(no: Node, base: Transform3D, lista: Array) -> void:
	var t := base
	if no is Node3D:
		t = base * (no as Node3D).transform
	if no is MeshInstance3D and (no as MeshInstance3D).mesh:
		lista.append([(no as MeshInstance3D).mesh, t])
	for f in no.get_children():
		_recolher_malhas(f, t, lista)


# ------------------------------------------------------------------ colisão do chão ------------------------------------------------------------------

## Colisão do chão: um HeightMapShape3D com 1 ponto por metro (as rampas das colinas ficam suaves).
func _colisao_chao() -> void:
	var w := int(largura * CEL) + 1
	var d := int(altura_cel * CEL) + 1
	var mapa := PackedFloat32Array()
	mapa.resize(w * d)
	for z in d:
		for x in w:
			var wx := x - largura * CEL / 2.0
			var wz := z - altura_cel * CEL / 2.0
			mapa[z * w + x] = altura_em(clamp(wx, -largura * CEL / 2.0 + 0.5, largura * CEL / 2.0 - 0.5),
					clamp(wz, -altura_cel * CEL / 2.0 + 0.5, altura_cel * CEL / 2.0 - 0.5))
	var hm := HeightMapShape3D.new()
	hm.map_width = w
	hm.map_depth = d
	hm.map_data = mapa
	var f := CollisionShape3D.new()
	f.shape = hm
	_corpo_estatico.add_child(f)
