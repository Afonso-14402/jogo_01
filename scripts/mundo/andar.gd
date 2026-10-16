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
var _tons: Dictionary = {}             # caminho do .glb -> [Color] (tom de cada instância, só no chão)
var _cache_mesh: Dictionary = {}       # caminho -> [[Mesh, Transform3D local]]
var _rng := RandomNumberGenerator.new()
var _corpo_estatico: StaticBody3D


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
	grelha = dados.get("grelha", [])
	altura_cel = grelha.size()
	largura = grelha[0].size() if altura_cel > 0 else 0
	_rng.seed = numero * 7919 + int(Time.get_unix_time_from_system()) % 100000   # cada visita é diferente
	var amb: Dictionary = dados.get("ambiente", {})
	Ambiente.criar(self, Color(amb.get("ceu", "#7fa0c8")), Color(amb.get("nevoeiro", "#c8e0d0")),
			float(amb.get("densidade_nevoeiro", 0.01)), float(amb.get("luz_ambiente", 0.6)), regiao, regiao == 2)
	_corpo_estatico = StaticBody3D.new()
	add_child(_corpo_estatico)
	_calcular_alturas()
	_construir_chao()
	_construir_celulas()
	_pontos()
	_decorar()
	_criar_instancias()
	_colisao_chao()
	_monstros()
	_baus_madeira()
	_nos_recolha()
	_pagina()
	_sitios_pesca()
	_jogador()
	Audio.tocar_musica(amb.get("musica", ""))
	Sistema.mensagem("Andar %d — %s" % [numero, dados.get("nome_pt", "")], "andar")
	if Jogo.tem_flag("prologo_p2") and numero == 1:
		_prologo_p2.call_deferred()
	elif numero > 1 and Opcoes.v("gravacao_automatica"):
		Gravar.gravar(Jogo.espaco_gravacao)   # gravação automática ao entrar num andar (Zona Segura)
	Eventos.andar_entrou.emit(numero)
	if numero > Jogo.andar_maximo:
		Jogo.andar_maximo = numero


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
	if jogador and jogador.global_position.y < -12.0:
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

func _altura_codigo(c: String) -> float:
	match c:
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
	# suavizar as colinas (rampas) sem mexer no vazio nem na água
	for _passo in 3:
		var nova := _alturas.duplicate()
		for bz in bh:
			for bx in bw:
				var h := _alturas[bz * bw + bx]
				if h < -10.0 or h < 0.0:
					continue
				var soma := 0.0
				var n := 0
				for dz in range(-1, 2):
					for dx in range(-1, 2):
						var x := bx + dx
						var z := bz + dz
						if x >= 0 and z >= 0 and x < bw and z < bh:
							var v := _alturas[z * bw + x]
							if v >= 0.0:
								soma += v
								n += 1
				nova[bz * bw + bx] = snappedf(soma / max(1, n), 0.25)
		_alturas = nova
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
	for bz in altura_cel * POR_CEL:
		for bx in bw:
			var c := codigo(bx / POR_CEL, bz / POR_CEL)
			var h := _alturas[bz * bw + bx]
			if c == "  ":
				continue
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
				",,":
					peca = kit.get("agua_rasa", kit.get("agua", ""))
				"cc":
					peca = kit.get("nuvem_fraca", chao)[0]
				_:
					peca = variante
			if peca.begins_with("res://"):
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
			# os lados das colinas (para não se ver o "vazio" por baixo dos blocos altos)
			if h > 0.4:
				_bloco_cor(kit.get("borda_cor", "#45293f"), Vector3(x, h - 0.2, z), Vector3(BLOCO, h, BLOCO))


var _cores: Dictionary = {}


## Água animada em pixel art: faixas de brilho que se mexem e uma ondulação suave (docs/ARTE.md).
static func agua_material(cor: Color) -> ShaderMaterial:
	var sh := Shader.new()
	sh.code = """
shader_type spatial;
render_mode blend_mix, cull_back, specular_schlick_ggx;
uniform vec4 cor : source_color;
uniform vec4 brilho : source_color;
varying vec3 mundo;
void vertex() {
	mundo = (MODEL_MATRIX * vec4(VERTEX, 1.0)).xyz;
	VERTEX.y += sin(mundo.x * 0.7 + TIME * 1.3) * 0.04 + cos(mundo.z * 0.6 + TIME) * 0.04;
}
void fragment() {
	vec2 p = floor(mundo.xz * 4.0) / 4.0;   // pixels de 25 cm
	float o = sin(p.x * 0.9 + TIME * 1.2) + sin(p.y * 1.1 - TIME * 0.9) + sin((p.x + p.y) * 0.5 + TIME * 0.6);
	float faixa = step(2.1, o) + step(2.6, o) * 0.6;
	ALBEDO = mix(cor.rgb, brilho.rgb, clamp(faixa, 0.0, 1.0) * 0.55);
	ALPHA = 0.85;
	ROUGHNESS = 0.15;
	SPECULAR = 0.7;
}
"""
	var m := ShaderMaterial.new()
	m.shader = sh
	m.set_shader_parameter("cor", cor)
	m.set_shader_parameter("brilho", cor.lightened(0.5))
	return m


## Bloco de uma só cor (água, lama, lados das colinas) quando a região não tem peça própria.
func _bloco_cor(cor: String, p: Vector3, tamanho := Vector3(BLOCO, 0.2, BLOCO)) -> void:
	var chave := "%s|%s" % [cor, tamanho]
	if not _cores.has(chave):
		var m := BoxMesh.new()
		m.size = tamanho
		if cor == kit.get("agua", "") and tamanho.y < 0.5:
			m.material = agua_material(Color(cor))
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
	var rochas: Array = kit.get("rocha", [])
	var mato: Array = kit.get("mato", [])
	var arvores: Array = kit.get("arvore", [])
	var grandes: Array = kit.get("gigante", [])
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
					if p != Vector3.INF:
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
				if p != Vector3.INF and p.distance_to(ponto_seguro) > 8.0:
					var e := _rng.randf_range(0.8, 1.2)
					_por(arvores[_rng.randi() % arvores.size()], p, _rng.randf() * TAU, e)
					_cilindro(p, 0.6 * e)
			# coisas grandes raras (troncos caídos, cogumelos gigantes) no meio do prado
			if c == ".." and _rng.randf() < 0.035 and not grandes.is_empty():
				var p := _ponto_livre(cx, cy, c)
				if p != Vector3.INF and p.distance_to(ponto_seguro) > 10.0:
					_por(grandes[_rng.randi() % grandes.size()], p, _rng.randf() * TAU, _rng.randf_range(0.6, 0.9))
					_cilindro(p, 1.0)


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
	return p


func _construir_celulas() -> void:
	for cy in altura_cel:
		for cx in largura:
			var c := codigo(cx, cy)
			match c:
				"TT":
					_encher(cx, cy, kit.get("limite", []), 3, 1.3, 1.7)
					_parede(cx, cy)
				"tt", "▒▒":
					_espalhar(cx, cy, kit.get("arvore", []), _rng.randi_range(2, 4), 0.8, 1.4, 0.7)
					_espalhar(cx, cy, kit.get("mato", []), _rng.randi_range(1, 3), 0.7, 1.1, 0.0)
				"##":
					_encher(cx, cy, kit.get("rocha", []), 4, 1.4, 2.2)
					_parede(cx, cy)
				"\"\"":
					_espalhar(cx, cy, kit.get("erva_alta", []), 45, 1.0, 1.6, 0.0)
				"**":
					_espalhar(cx, cy, kit.get("flores", []), 8, 0.9, 1.2, 0.0)
				"()":
					_espalhar(cx, cy, kit.get("gigante", []), 1, 1.6, 2.0, 1.6)
				"CC":
					_espalhar(cx, cy, kit.get("casa", []), 1, 1.0, 1.0, 2.6, true)
				"mm":
					_espalhar(cx, cy, kit.get("mato", []), 4, 1.0, 1.3, 0.8)
				"rr":
					_no_recolha(_ponto_aleatorio(cx, cy, 2.0), "picareta")
				"~~", "ww":
					_parede(cx, cy, 2.0)
				"==":
					_ponte(cx, cy)


func _encher(cx: int, cy: int, pecas: Array, n: int, e0: float, e1: float) -> void:
	if pecas.is_empty():
		return
	for i in n:
		var p := _ponto_aleatorio(cx, cy, 1.5)
		_por(pecas[_rng.randi() % pecas.size()], p, _rng.randf() * TAU, _rng.randf_range(e0, e1))


func _espalhar(cx: int, cy: int, pecas: Array, n: int, e0: float, e1: float, raio_colisao: float, centro: bool = false) -> void:
	if pecas.is_empty():
		return
	for i in n:
		var p := centro_celula(cx, cy) if centro else _ponto_aleatorio(cx, cy, 1.2)
		var e := _rng.randf_range(e0, e1)
		_por(pecas[_rng.randi() % pecas.size()], p, (_rng.randi() % 4) * PI / 2.0 if centro else _rng.randf() * TAU, e)
		if raio_colisao > 0.0:
			_cilindro(p, raio_colisao * e)


func _parede(cx: int, cy: int, altura: float = 8.0) -> void:
	var f := CollisionShape3D.new()
	var b := BoxShape3D.new()
	b.size = Vector3(CEL, altura, CEL)
	f.shape = b
	f.position = centro_celula(cx, cy) + Vector3(0, altura / 2.0 - 1.0, 0)
	_corpo_estatico.add_child(f)


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
					_bau(p, "ouro" if "ouro" in _texto_ponto(cx, cy) else "prata")
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
	var dir := DirAccess.open(pasta)
	if dir == null:
		return
	for f in dir.get_files():
		if f.begins_with(prefixo) and f.ends_with(".glb"):
			pecas.append(pasta + f)
	pecas.sort()
	var sitios: Array[Vector2i] = []
	for marca in ["??", "!!", "<>", "[]", "AA", "@@", "vv", "ii", "FF", "HH", "JJ", "MM", "CC", "()"]:
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
		_por(peca, p, (_rng.randi() % 4) * PI / 2.0)
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
		else:
			malhas = _malhas_de(chave)
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
			if mm.use_colors and (par[0] as Mesh).get_surface_count() == 1:
				# o tom de cada bloco multiplica a textura (manchas mais claras e mais escuras no chão)
				var base = (par[0] as Mesh).surface_get_material(0)
				if base is StandardMaterial3D:
					var m: StandardMaterial3D = base.duplicate()
					m.vertex_color_use_as_albedo = true
					mi.material_override = m
			add_child(mi)
	_instancias.clear()
	_tons.clear()


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
