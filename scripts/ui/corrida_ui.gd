extends JanelaUI
## As corridas (docs/ATIVIDADES.md 4.5; dados/minijogos.json "corridas"): vista de cima, a pista desce pelo ecrã.
## Vagonetas (mudar de carril, baixar nas vigas, apanhar cristais), canoas (remar à vez nos dois lados), lagartos
## (mudar de pista, saltar pedras, contra 3 rivais) e trenó (deslizar entre os pinheiros, apanhar bandeiras).
## Também há botões no ecrã (telemóvel).

const ARTE := "res://arte/minijogos/corrida_"
const ALTURA := 430.0
const LARGURA := 450.0
const HEROI_Y := 360.0
const ESCALA := 3.0

var _c: Dictionary = {}
var _id: String = ""
var _pista: Control
var _estado: Label
var _botao_meio: Button
var _botoes: Array[Button] = []
var _tex: Dictionary = {}
var _rng := RandomNumberGenerator.new()

var _a_correr: bool = false
var _dist: float = 0.0
var _vel: float = 0.0
var _t: float = 0.0
var _x: float = 1.0               # pista onde estás (0, 1, 2); no trenó é contínuo
var _alvo: float = 1.0
var _parado: float = 0.0
var _travado: float = 0.0
var _baixo: float = 0.0
var _ar: float = 0.0
var _lado: int = 0                # canoa: lado da última remada (-1 / 1)
var _remo: float = 0.0
var _segura: int = 0              # trenó: -1 / 0 / 1
var _coisas: Array = []           # [{d, x, tipo, feita}]
var _rivais: Array = []           # [{d, vel, x}]
var _apanhadas: int = 0
var _anim: float = 0.0
var _tremer: float = 0.0


func _ready() -> void:
	add_to_group("janelas")
	add_to_group("corrida_ui")
	_criar_janela(Vector2(390, 40), Vector2(500, 640))
	_texto(_janela, Vector2(20, 12), 20, Color("fbff86")).name = "Titulo"
	_estado = _texto(_janela, Vector2(20, 40), 14, Color("c7dcd0"))
	_pista = Control.new()
	_pista.position = Vector2(25, 66)
	_pista.size = Vector2(LARGURA, ALTURA)
	_pista.clip_contents = true
	_pista.draw.connect(_desenhar)
	_janela.add_child(_pista)
	var esq := _botao("◀", func(): _carregar(-1), _janela)
	var meio := _botao("", func(): _carregar(0), _janela)
	var dir := _botao("▶", func(): _carregar(1), _janela)
	_botao_meio = meio
	for k in 3:
		var b: Button = [esq, meio, dir][k]
		b.position = Vector2(40 + k * 150, 510)
		b.custom_minimum_size = Vector2(120, 52)
		b.add_theme_font_size_override("font_size", 20)
		_botoes.append(b)
	esq.button_down.connect(func(): _segura = -1)
	dir.button_down.connect(func(): _segura = 1)
	esq.button_up.connect(func(): _segura = 0)
	dir.button_up.connect(func(): _segura = 0)
	_botao("Outra vez", func(): correr(_id), _janela).position = Vector2(300, 590)
	_botao("Sair", func(): abrir(false), _janela).position = Vector2(420, 590)


func _textura(nome: String) -> Texture2D:
	if not _tex.has(nome):
		var c: String = ARTE + nome + ".png"
		_tex[nome] = load(c) if ResourceLoader.exists(c) else null
	return _tex[nome]


## Começar uma corrida (id: vagonetas, canoas, lagartos, treno).
func correr(id: String) -> void:
	_c = Dados.tabela("minijogos").get("corridas", {}).get(id, {})
	if _c.is_empty():
		return
	_id = id
	abrir(true)
	(_janela.get_node("Titulo") as Label).text = "Corrida de %s" % _c.nome_pt
	_botao_meio.text = {"vagonetas": "▼ Baixar", "lagartos": "▲ Saltar"}.get(id, "")
	_botao_meio.visible = _botao_meio.text != ""
	_rng.randomize()
	_dist = 0.0
	_t = 0.0
	_vel = float(_c.get("velocidade", 20))
	_x = 1.0
	_alvo = 1.0
	_parado = 0.0
	_travado = 0.0
	_baixo = 0.0
	_ar = 0.0
	_lado = 0
	_segura = 0
	_apanhadas = 0
	_coisas.clear()
	_rivais.clear()
	var pista := float(_c.get("pista", 1000))
	var d := 30.0
	var o: Array = _c.get("obstaculos", [40, 70])
	while d < pista - 20.0:
		_coisas.append({"d": d, "x": _lugar(), "tipo": _obstaculo(), "feita": false})
		var meio := d + _rng.randf_range(float(o[0]), float(o[1])) / 2.0
		if id in ["vagonetas", "treno"] and meio < pista - 20.0:
			_coisas.append({"d": meio, "x": _lugar(), "tipo": "cristal" if id == "vagonetas" else "bandeira", "feita": false})
		d += _rng.randf_range(float(o[0]), float(o[1]))
	var livres := [0.0, 2.0, 0.0]
	var rv: Array = _c.get("rivais", [])
	for k in rv.size():
		_rivais.append({"d": 0.0, "vel": float(rv[k]), "x": livres[k % 3] if rv.size() < 3 else float(k)})
	_a_correr = true


func _lugar() -> float:
	if _id == "treno":
		return _rng.randf_range(0.0, 2.0)
	return float(_rng.randi() % 3)


func _obstaculo() -> String:
	match _id:
		"vagonetas":
			return "viga" if _rng.randf() < 0.45 else "pedra"
		"canoas":
			return "pedra_rio" if _rng.randf() < 0.6 else "tronco"
		"lagartos":
			return "pedra" if _rng.randf() < 0.55 else "cacto"
	return "pinheiro"


func _carregar(lado: int) -> void:
	if not _a_correr:
		return
	match _id:
		"vagonetas", "lagartos":
			if lado == 0:
				if _id == "vagonetas":
					_baixo = float(_c.get("baixar", 0.7))
				elif _ar <= 0.0:
					_ar = float(_c.get("salto", 0.6))
			else:
				_alvo = clampf(_alvo + lado, 0.0, 2.0)
		"canoas":
			if lado == 0:
				return
			_remo = 0.25
			if lado == _lado:   # duas vezes do mesmo lado: a canoa vira para o outro
				_alvo = clampf(_alvo - lado, 0.0, 2.0)
				_lado = 0
			else:
				_vel = minf(float(_c.get("maximo", 9)), _vel + float(_c.get("por_remada", 1.2)))
				_lado = lado


func _unhandled_input(e: InputEvent) -> void:
	if visible and _a_correr:
		var mapa := {"mover_esquerda": -1, "mover_direita": 1, "mover_baixo": 0, "mover_cima": 0}
		for a in mapa:
			if e.is_action_pressed(a):
				if a == "mover_cima" and _id != "lagartos" or a == "mover_baixo" and _id != "vagonetas":
					continue
				_carregar(mapa[a])
				if _id == "treno" and mapa[a] != 0:
					_segura = mapa[a]
				get_viewport().set_input_as_handled()
				return
			if _id == "treno" and e.is_action_released(a) and mapa[a] == _segura:
				_segura = 0
	super._unhandled_input(e)


func _process(delta: float) -> void:
	if not visible:
		return
	_anim += delta
	_tremer = maxf(0.0, _tremer - delta)
	if _a_correr:
		_passo(delta)
	_pista.queue_redraw()


## Um bocadinho de corrida (também usado pelos testes).
func _passo(delta: float) -> void:
	_t += delta
	_baixo = maxf(0.0, _baixo - delta)
	_ar = maxf(0.0, _ar - delta)
	_remo = maxf(0.0, _remo - delta)
	_travado = maxf(0.0, _travado - delta)
	match _id:
		"canoas":
			_vel = maxf(0.0, _vel - float(_c.get("atrito", 1.5)) * delta)
		"treno":
			_vel = minf(float(_c.get("maximo", 28)), _vel + float(_c.get("aceleracao", 0.8)) * delta)
			_alvo = clampf(_alvo + _segura * delta * 2.6, 0.0, 2.0)
	_x = move_toward(_x, _alvo, delta * (12.0 if _id == "treno" else 7.0))
	var v := _vel
	if _parado > 0.0:
		_parado -= delta
		v = 0.0
	elif _travado > 0.0:
		v *= 1.0 - float(_c.get("travar", 0.4))
	var antes := _dist
	_dist += v * delta
	for r in _rivais:
		r.d = minf(float(_c.pista), r.d + r.vel * delta)
	for o in _coisas:
		if not o.feita and o.d > antes and o.d <= _dist:
			o.feita = true
			_tocar(o)
	if _dist >= float(_c.pista):
		_fim()


func _tocar(o: Dictionary) -> void:
	var perto: bool = absf(float(o.x) - _x) < (0.45 if _id == "treno" else 0.5)
	match o.tipo:
		"cristal", "bandeira":
			if perto:
				_apanhadas += 1
				if o.tipo == "cristal":
					_vel = minf(float(_c.get("maximo", 35)), _vel + float(_c.get("por_cristal", 0.5)))
				Audio.efeito("moeda")
		"viga":
			if _baixo <= 0.0:
				_bater()
		"pedra":
			if perto and (_id != "lagartos" or _ar <= 0.0):
				_bater()
		_:
			if perto:
				_bater()


func _bater() -> void:
	_tremer = 0.4
	Audio.efeito("pancada")
	if _c.has("parar"):
		_parado = float(_c.parar)
	if _c.has("travar"):
		_travado = float(_c.get("travar_s", 1.0))
	if _c.get("recomecar", false):
		_vel = float(_c.get("velocidade", 12))


func _fim() -> void:
	_a_correr = false
	var regiao := clampi((int(_c.get("andar", 1)) - 1) / 10 + 1, 1, 10)
	var lugar := 1
	for r in _rivais:
		if r.d >= float(_c.pista) - 0.01:
			lugar += 1
	var ganhou := lugar == 1
	if _c.has("tempo"):
		ganhou = _t < float(_c.tempo)
	var ouro := _apanhadas * int(_c.get("ouro_coisa", 0))
	if ganhou:
		ouro += int(_c.get("premio_regiao", 50)) * regiao
		Colecoes.contar("corridas_ganhas")
		Colecoes.contar("corridas_" + _id)
		if _c.get("missao", "") != "":
			var precisa := int(_c.get("vitorias_missao", 1))
			if int(Jogo.contadores.get("corridas_" + _id, 0)) >= precisa:
				Missoes.marcar(String(_c.missao), 0)
	var melhor := int(Jogo.contadores.get("corrida_%s_melhor" % _id, 0))   # décimos de segundo
	var agora := int(round(_t * 10.0))
	var recorde := melhor == 0 or agora < melhor
	if recorde:
		Jogo.contadores["corrida_%s_melhor" % _id] = agora
	if ouro > 0:
		Jogo.ganhar_ouro(ouro)
	var txt := "%s! %.1f s%s · +%d ouro" % ["Ganhaste" if ganhou else ("Chegaste em %dº" % lugar if _c.has("rivais") else "Demasiado lento"),
			_t, " (recorde!)" if recorde else "", ouro]
	_estado.text = txt
	Sistema.mensagem("Corrida de %s: %s" % [_c.nome_pt, txt], "nivel" if ganhou else "aviso")


# ------------------------------------------------------------------ desenho ------------------------------------------------------------------

func _esc() -> float:   # píxeis por metro (a pista desce mais ou menos depressa conforme a corrida)
	return 270.0 / maxf(6.0, float(_c.get("maximo", _c.get("velocidade", 20))) * (0.85 if _id != "canoas" else 0.9))


func _y(d: float) -> float:
	return HEROI_Y - (d - _dist) * _esc()


func _cx(x: float) -> float:
	return 75.0 + x * 150.0


func _quadro(nome: String, n: int, fps: float = 8.0) -> Array:
	var t := _textura(nome)
	if t == null:
		return [null, Rect2()]
	var w := t.get_width() / n
	var f := int(_anim * fps) % n
	return [t, Rect2(f * w, 0, w, t.get_height())]


func _sprite(nome: String, n: int, centro: Vector2, esc := ESCALA, f: int = -1, cor := Color.WHITE) -> void:
	var q := _quadro(nome, n)
	if q[0] == null:
		return
	var r: Rect2 = q[1]
	if f >= 0:
		r.position.x = f * r.size.x
	var tam: Vector2 = r.size * esc
	_pista.draw_texture_rect_region(q[0], Rect2(centro - tam / 2.0, tam), r, cor)


func _desenhar() -> void:
	if _c.is_empty():
		return
	var c := _pista
	var e := _esc()
	var sobe := fmod(_dist * e, 48.0)
	match _id:
		"vagonetas":
			c.draw_rect(Rect2(Vector2.ZERO, c.size), Color("3e3546"))
			for k in 3:
				var cx := _cx(k)
				var y := -48.0 + sobe
				while y < ALTURA + 48.0:
					c.draw_rect(Rect2(cx - 40, y, 80, 8), Color("694f62"))
					y += 48.0
				for lx in [-26.0, 22.0]:
					c.draw_rect(Rect2(cx + lx, 0, 4, ALTURA), Color("9babb2"))
			for k in 8:   # lanternas nas paredes
				var y := fmod(k * 120.0 + _dist * e * 0.999, ALTURA + 120.0) - 60.0
				c.draw_circle(Vector2(6, y), 5, Color("f9c22b"))
				c.draw_circle(Vector2(LARGURA - 6, y + 60), 5, Color("f9c22b"))
		"canoas":
			c.draw_rect(Rect2(Vector2.ZERO, c.size), Color("0b8a8f"))
			for k in 14:
				var y := fmod(k * 37.0 + _dist * e, ALTURA + 40.0) - 20.0
				c.draw_rect(Rect2(fmod(k * 97.0, LARGURA - 40) + 10, y, 22, 3), Color("30e1b9"))
			c.draw_rect(Rect2(0, 0, 12, ALTURA), Color("547e64"))
			c.draw_rect(Rect2(LARGURA - 12, 0, 12, ALTURA), Color("547e64"))
		"lagartos":
			c.draw_rect(Rect2(Vector2.ZERO, c.size), Color("fbb954"))
			for k in 18:
				var y := fmod(k * 29.0 + _dist * e, ALTURA + 30.0) - 15.0
				c.draw_rect(Rect2(fmod(k * 131.0, LARGURA - 20) + 6, y, 10, 4), Color("e6904e"))
			for k in [1, 2]:
				var y := -48.0 + sobe
				while y < ALTURA:
					c.draw_rect(Rect2(k * 150.0 - 2, y, 4, 24), Color("cd683d"))
					y += 48.0
		_:
			c.draw_rect(Rect2(Vector2.ZERO, c.size), Color("c7dcd0"))
			for k in 16:
				var y := fmod(k * 31.0 + _dist * e, ALTURA + 30.0) - 15.0
				c.draw_rect(Rect2(fmod(k * 113.0, LARGURA - 20) + 6, y, 14, 3), Color("ffffff"))
	# a meta
	var ym := _y(float(_c.pista))
	if ym > -20 and ym < ALTURA + 20:
		for k in 15:
			c.draw_rect(Rect2(k * 30.0, ym - 8, 15, 8), Color("2e222f") if k % 2 == 0 else Color("ffffff"))
			c.draw_rect(Rect2(k * 30.0 + 15, ym, 15, 8), Color("2e222f") if k % 2 == 0 else Color("ffffff"))
	# as coisas da pista
	for o in _coisas:
		var y := _y(o.d)
		if y < -60 or y > ALTURA + 60 or (o.feita and o.tipo in ["cristal", "bandeira"]):
			continue
		var p := Vector2(_cx(o.x), y)
		match o.tipo:
			"viga":
				for k in 3:
					_sprite("viga", 1, Vector2(_cx(k), y), 1.5)
			"cristal":
				_sprite("cristal", 4, p, 2.5)
			"bandeira":
				_sprite("bandeira", 2, p, 3.0)
			"pedra":
				_sprite("pedra", 1, p, 3.0, -1, Color("fca790") if _id == "lagartos" else Color.WHITE)
			"pedra_rio":
				_sprite("pedra_rio", 2, p)
			"tronco":
				_sprite("tronco", 2, p)
			"cacto":
				_sprite("cacto", 1, p)
			"pinheiro":
				_sprite("pinheiro", 1, p)
	# os rivais
	for r in _rivais:
		var p := Vector2(_cx(r.x), _y(r.d))
		if p.y > -60 and p.y < ALTURA + 60:
			if _id == "canoas":
				_sprite("canoa_rival", 4, p, ESCALA, int(_anim * 3.0) % 4)
			else:
				_sprite("lagarto", 4, p, ESCALA, -1, Color("91db69"))
	# tu
	var tremer := Vector2(randf_range(-3, 3), 0) if _tremer > 0.0 else Vector2.ZERO
	var eu := Vector2(_cx(_x), HEROI_Y) + tremer
	match _id:
		"vagonetas":
			_sprite("vagoneta_baixar" if _baixo > 0.0 else "vagoneta", 2, eu)
		"canoas":
			var f := (0 if _lado <= 0 else 2) + (1 if _remo > 0.0 else 0)
			_sprite("canoa", 4, eu, ESCALA, f)
		"lagartos":
			if _ar > 0.0:
				c.draw_circle(eu + Vector2(0, 30), 26, Color(0, 0, 0, 0.2))
				_sprite("lagarto_salto", 1, eu + Vector2(0, -16), ESCALA * 1.1)
			else:
				_sprite("lagarto", 4, eu)
		_:
			_sprite("treno", 2, eu)
	# a barra do progresso (à direita): tu a amarelo, os rivais a verde
	var bx := LARGURA - 10.0
	c.draw_rect(Rect2(bx - 2, 10, 4, ALTURA - 20), Color(0, 0, 0, 0.35))
	for r in _rivais:
		c.draw_circle(Vector2(bx, ALTURA - 10 - (ALTURA - 20) * r.d / float(_c.pista)), 5, Color("1ebc73"))
	c.draw_circle(Vector2(bx, ALTURA - 10 - (ALTURA - 20) * minf(1.0, _dist / float(_c.pista))), 6, Color("f9c22b"))
	# o estado
	var pos := ""
	if not _rivais.is_empty():
		var lugar := 1
		for r in _rivais:
			if r.d > _dist:
				lugar += 1
		pos = "   %dº lugar" % lugar
	if _a_correr:
		_estado.text = "%.1f s   %d m / %d m   %.0f m/s%s%s" % [_t, int(_dist), int(_c.pista), _vel, pos,
				("   %s: %d" % ["cristais" if _id == "vagonetas" else "bandeiras", _apanhadas]) if _id in ["vagonetas", "treno"] else ""]
