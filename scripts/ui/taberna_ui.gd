extends JanelaUI
## Os jogos da Taberna "O Primeiro Degrau" (docs/ATIVIDADES.md 4.2–4.4 e 4.9; números em dados/minijogos.json):
## - Maior ou Menor (dados): até 5 acertos seguidos, cada um duplica o prémio;
## - Torre de Cartas: cartas dos monstros que já venceste (ATQ + elemento), ganha quem vencer 3 rondas;
## - Braço de ferro: carregar quando o cursor está na zona verde (a FOR alarga-a).

const ELEMENTO_REGIAO := {1: "fisico", 2: "fisico", 3: "sombra", 4: "fogo", 5: "gelo", 6: "raio", 7: "fogo", 8: "sombra", 9: "raio", 10: "luz"}
const COR_ELEMENTO := {"fogo": "ea4f36", "gelo": "8fd3ff", "raio": "f9c22b", "luz": "fbff86", "sombra": "a884f3", "fisico": "9babb2"}
const TIPO := {"tanque": "forte", "com_nome": "elite", "rapido": "normal", "mago": "normal", "voador": "normal"}

var _cfg: Dictionary = {}
var _corpo: Control
var _titulo: Label
var _ouro: Label
var _jogo: String = ""
var _aposta: int = 0
var _adv: Dictionary = {}
var _rng := RandomNumberGenerator.new()
# dados
var _dado: int = 1
var _premio: int = 0
var _seguidas: int = 0
var _a_rolar: bool = false
var _rolar_t: float = 0.0
var _rolar_troca: float = 0.0
var _rolar_depois: Callable
# cartas
var _mao: Array = []
var _mao_adv: Array = []
var _pontos := Vector2i.ZERO
var _ronda: int = 0
var _escolhidas: Array = []
# braço de ferro
var _forca: float = 0.5
var _cursor: float = 0.0
var _sentido: float = 1.0
var _zona := Vector2(0.4, 0.56)
var _barra: Control
var _a_jogar: bool = false


func _ready() -> void:
	add_to_group("janelas")
	add_to_group("taberna_ui")
	_cfg = Dados.tabela("minijogos")
	_rng.randomize()
	_criar_janela(Vector2(300, 130), Vector2(680, 460))
	_titulo = _texto(_janela, Vector2(20, 12), 20, Color("fbff86"))
	_ouro = _texto(_janela, Vector2(520, 14), 15, Color("f9c22b"))
	_corpo = Control.new()
	_corpo.position = Vector2(16, 48)
	_corpo.size = Vector2(648, 400)
	_janela.add_child(_corpo)
	_botao("Sair", func(): abrir(false), _janela).position = Vector2(600, 420)


func _atualizar_ouro() -> void:
	_ouro.text = "%d ouro" % Jogo.ouro


func _apostas() -> Array:
	var a: Array = _cfg.get("apostas", [10, 50, 100, 500]).duplicate()
	if Jogo.andar_maximo >= int(_cfg.get("aposta_alta_andar", 30)):
		a.append(int(_cfg.get("aposta_alta", 1000)))
	return a


## A fila de botões das apostas; ao escolher, paga e chama cb.
func _escolher_aposta(y: float, cb: Callable) -> void:
	_texto(_corpo, Vector2(0, y), 15).text = "Quanto apostas?"
	var x := 150.0
	for v in _apostas():
		var b := _botao("%d" % v, func():
			if Jogo.ouro < v:
				Sistema.mensagem("Não tens ouro que chegue.", "aviso")
				return
			Jogo.ouro -= v
			_aposta = v
			_atualizar_ouro()
			cb.call(), _corpo)
		b.position = Vector2(x, y - 2)
		b.disabled = Jogo.ouro < v
		x += 70.0


func _ganhar(valor: int, texto: String) -> void:
	Jogo.ouro += valor
	_atualizar_ouro()
	Sistema.mensagem(texto, "nivel")


# ================================================================== MAIOR OU MENOR ==================================================================

func abrir_dados() -> void:
	_jogo = "dados"
	abrir(true)
	_limpar(_corpo)
	_titulo.text = "Maior ou Menor"
	_atualizar_ouro()
	_texto(_corpo, Vector2(0, 0), 13, Color("c7dcd0")).text = "Lança-se um dado. Diz se o próximo é maior ou menor. Cada acerto duplica o prémio (até %d seguidos)." % int(_cfg.get("dados_seguidas", 5))
	_escolher_aposta(40, _dados_comecar)


func _dados_comecar() -> void:
	_limpar(_corpo)
	_premio = _aposta
	_seguidas = 0
	var face := Control.new()
	face.name = "Dado"
	face.position = Vector2(270, 30)
	face.size = Vector2(110, 110)
	face.draw.connect(func(): _desenhar_dado(face))
	_corpo.add_child(face)
	var info := _texto(_corpo, Vector2(0, 160), 16)
	info.name = "Info"
	var maior := _botao("▲ Maior", func(): _dados_apostar(1), _corpo)
	maior.position = Vector2(170, 210)
	var menor := _botao("▼ Menor", func(): _dados_apostar(-1), _corpo)
	menor.position = Vector2(290, 210)
	var parar := _botao("Parar e levar o prémio", _dados_parar, _corpo)
	parar.name = "Parar"
	parar.position = Vector2(410, 210)
	_rolar(func(): _dados_info(""))


func _desenhar_dado(c: Control) -> void:
	var r := Rect2(Vector2.ZERO, c.size)
	c.draw_rect(r, Color("2e222f"))
	c.draw_rect(r.grow(-4), Color("ffffff"))
	c.draw_rect(Rect2(r.position + Vector2(4, r.size.y - 14), Vector2(r.size.x - 8, 10)), Color("c7dcd0"))
	var p := {1: [[1, 1]], 2: [[0, 0], [2, 2]], 3: [[0, 0], [1, 1], [2, 2]], 4: [[0, 0], [2, 0], [0, 2], [2, 2]],
			5: [[0, 0], [2, 0], [1, 1], [0, 2], [2, 2]], 6: [[0, 0], [2, 0], [0, 1], [2, 1], [0, 2], [2, 2]]}
	for q in p[_dado]:
		var centro := Vector2(22 + q[0] * 33, 22 + q[1] * 33)
		c.draw_rect(Rect2(centro - Vector2(8, 8), Vector2(16, 16)), Color("b33831") if _dado == 1 else Color("2e222f"))


## Lança o dado: salta e muda de face durante 0,6 s (no _process, que corre com o jogo em pausa) e depois chama depois.
func _rolar(depois: Callable) -> void:
	_a_rolar = true
	_rolar_t = 0.6
	_rolar_depois = depois


func _animar_dado(delta: float) -> void:
	var face: Control = _corpo.get_node_or_null("Dado")
	if face == null:
		_a_rolar = false
		return
	_rolar_t -= delta
	_rolar_troca -= delta
	if _rolar_troca <= 0.0:
		_rolar_troca = 0.06
		_dado = _rng.randi_range(1, 6)
		Audio.efeito("dado")
	face.position.y = 30 - absf(sin(_rolar_t * 15.0)) * 18.0
	face.queue_redraw()
	if _rolar_t <= 0.0:
		face.position.y = 30
		_dado = _rng.randi_range(1, 6)
		face.queue_redraw()
		_a_rolar = false
		if _rolar_depois.is_valid():
			_rolar_depois.call()


func _dados_info(extra: String) -> void:
	var info: Label = _corpo.get_node("Info")
	info.text = "%sDado: %d · Prémio: %d ouro · Seguidas: %d/%d" % [extra, _dado, _premio, _seguidas, int(_cfg.get("dados_seguidas", 5))]


func _dados_apostar(sentido: int) -> void:
	if _a_rolar or _premio <= 0:
		return
	var antes := _dado
	_rolar(func(): _dados_resultado(antes, sentido))


func _dados_resultado(antes: int, sentido: int) -> void:
	if _dado == antes:
		_dados_info("Igual! Ninguém ganha. ")
		return
	if (_dado > antes) == (sentido > 0):
		_seguidas += 1
		_premio *= 2
		if _seguidas >= int(_cfg.get("dados_seguidas", 5)):
			_ganhar(_premio, "Cinco seguidas! Ganhaste %d ouro na Taberna!" % _premio)
			_premio = 0
			_dados_fim("Cinco seguidas! Levas %d ouro." % (_aposta * int(pow(2, _seguidas))))
			return
		_dados_info("Acertaste! ")
	else:
		_premio = 0
		_dados_fim("Errado… Perdeste a aposta.")


func _dados_parar() -> void:
	if _premio <= 0 or _a_rolar:
		return
	_ganhar(_premio, "Levaste %d ouro dos dados." % _premio)
	_dados_fim("Paraste a tempo: %d ouro." % _premio)
	_premio = 0


func _dados_fim(texto: String) -> void:
	_dados_info("")
	var info: Label = _corpo.get_node("Info")
	info.text = texto
	var de_novo := _botao("Jogar outra vez", abrir_dados, _corpo)
	de_novo.position = Vector2(250, 270)


# ================================================================== TORRE DE CARTAS ==================================================================

## Uma carta de um monstro: ATQ (região e tipo) e elemento (resistência, ou o da região).
func carta(mid: String) -> Dictionary:
	var m := Dados.monstro(mid)
	var tipos: Dictionary = _cfg.get("cartas_tipo", {})
	var tipo: String = TIPO.get(m.get("tipo", "normal"), m.get("tipo", "normal"))
	var atq := roundi(float(_cfg.get("cartas_base", 2)) + int(m.get("regiao", 1)) * float(_cfg.get("cartas_por_regiao", 1.2)) + int(tipos.get(tipo, 1)))
	var el: String = ELEMENTO_REGIAO.get(int(m.get("regiao", 1)), "fisico")
	for r in m.get("resistencias", []):
		if r != "fisico":
			el = r
			break
	return {"id": mid, "nome_pt": m.get("nome_pt", mid), "atq": atq, "elemento": el, "fraquezas": m.get("fraquezas", []), "sprite": m.get("sprite", "")}


func _valor(a: Dictionary, contra: Dictionary) -> int:
	return int(a.atq) + (int(_cfg.get("cartas_elemento", 3)) if a.elemento in contra.fraquezas else 0)


func abrir_cartas(adversario: String) -> void:
	_jogo = "cartas"
	for a in _cfg.get("cartas_adversarios", []):
		if a.id == adversario:
			_adv = a
	abrir(true)
	_limpar(_corpo)
	_titulo.text = "Torre de Cartas — contra %s" % _adv.get("nome_pt", "?")
	_atualizar_ouro()
	var minhas: Array = []
	for mid in Jogo.bestiario.keys():
		if not Dados.monstro(mid).is_empty():
			minhas.append(carta(mid))
	if minhas.size() < int(_cfg.get("cartas_minimo", 5)):
		_texto(_corpo, Vector2(0, 20), 15).text = "Precisas de ter vencido pelo menos %d tipos de monstros (tens %d).\nO Bestiário é o teu baralho!" % [int(_cfg.get("cartas_minimo", 5)), minhas.size()]
		return
	minhas.sort_custom(func(a, b): return int(a.atq) > int(b.atq))
	_escolhidas = minhas.slice(0, 5)
	_texto(_corpo, Vector2(0, 0), 13, Color("c7dcd0")).text = "Escolhe 5 cartas (as mais fortes já estão escolhidas). Elemento forte contra o outro: +%d." % int(_cfg.get("cartas_elemento", 3))
	var grelha := GridContainer.new()
	grelha.columns = 8
	grelha.position = Vector2(0, 24)
	var scroll := ScrollContainer.new()
	scroll.position = Vector2(0, 24)
	scroll.size = Vector2(648, 290)
	scroll.add_child(grelha)
	_corpo.add_child(scroll)
	for c in minhas:
		var vista := _vista_carta(c, 0.62)
		vista.modulate = Color.WHITE if c in _escolhidas else Color(0.55, 0.55, 0.6)
		vista.gui_input.connect(func(e: InputEvent):
			if e is InputEventMouseButton and e.pressed:
				if c in _escolhidas:
					_escolhidas.erase(c)
				elif _escolhidas.size() < 5:
					_escolhidas.append(c)
				vista.modulate = Color.WHITE if c in _escolhidas else Color(0.55, 0.55, 0.6))
		grelha.add_child(vista)
	_escolher_aposta(330, _cartas_comecar)


func _vista_carta(c: Dictionary, esc: float = 1.0) -> Control:
	var tam := Vector2(96, 128) * esc
	var p := Control.new()
	p.custom_minimum_size = tam
	p.size = tam
	p.mouse_filter = Control.MOUSE_FILTER_STOP
	var fundo := NinePatchRect.new()
	fundo.texture = load(UI + "janela_sistema.png")
	for m in ["patch_margin_left", "patch_margin_right", "patch_margin_top", "patch_margin_bottom"]:
		fundo.set(m, 6)
	fundo.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	fundo.size = tam
	fundo.mouse_filter = Control.MOUSE_FILTER_IGNORE
	p.add_child(fundo)
	var faixa := ColorRect.new()
	faixa.color = Color(COR_ELEMENTO.get(c.elemento, "9babb2"))
	faixa.position = Vector2(4, 4)
	faixa.size = Vector2(tam.x - 8, 6 * esc)
	faixa.mouse_filter = Control.MOUSE_FILTER_IGNORE
	p.add_child(faixa)
	var caminho: String = c.sprite + "_parado_lado.png"
	if ResourceLoader.exists(caminho):
		var tex: Texture2D = load(caminho)
		var at := AtlasTexture.new()
		at.atlas = tex
		at.region = Rect2(0, 0, tex.get_height(), tex.get_height())
		var t := TextureRect.new()
		t.texture = at
		t.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
		t.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
		t.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
		t.position = Vector2(8, 14) * esc
		t.size = Vector2(80, 64) * esc
		t.mouse_filter = Control.MOUSE_FILTER_IGNORE
		p.add_child(t)
	var nome := _texto(p, Vector2(6, 78) * esc, maxi(9, int(11 * esc)))
	nome.text = c.nome_pt
	nome.size = Vector2(tam.x - 10, 20)
	nome.clip_text = true
	var el := _texto(p, Vector2(6, 92) * esc, maxi(8, int(10 * esc)), Color(COR_ELEMENTO.get(c.elemento, "9babb2")))
	el.text = c.elemento
	var atq := _texto(p, Vector2(6, 104) * esc, maxi(11, int(17 * esc)), Color("fbff86"))
	atq.text = "ATQ %d" % int(c.atq)
	return p


func _cartas_comecar() -> void:
	if _escolhidas.size() < 5:
		Jogo.ouro += _aposta
		Sistema.mensagem("Escolhe 5 cartas primeiro.", "aviso")
		return
	_mao = _escolhidas.duplicate()
	# o baralho do adversário: monstros das regiões dele (os difíceis escolhem os mais fortes)
	var todos: Array = []
	for m in Dados.tabela("monstros").values():
		if int(m.get("regiao", 1)) <= int(_adv.get("regioes", 3)):
			todos.append(carta(m.id))
	todos.shuffle()
	if _adv.get("dificuldade", "") != "fácil":
		todos.sort_custom(func(a, b): return int(a.atq) > int(b.atq))
		todos = todos.slice(0, mini(todos.size(), 12))
		todos.shuffle()
	_mao_adv = todos.slice(0, 5)
	_pontos = Vector2i.ZERO
	_ronda = 0
	_cartas_mesa("Escolhe uma carta para jogar.")


func _cartas_mesa(texto: String) -> void:
	_limpar(_corpo)
	_texto(_corpo, Vector2(0, 0), 15).text = "Tu %d — %d %s   (ronda %d)" % [_pontos.x, _pontos.y, _adv.get("nome_pt", ""), _ronda + 1]
	_texto(_corpo, Vector2(0, 22), 13, Color("c7dcd0")).text = texto
	for i in _mao_adv.size():   # as cartas do adversário, viradas para baixo
		var costas := ColorRect.new()
		costas.color = Color("484a77")
		costas.position = Vector2(170 + i * 64, 50)
		costas.size = Vector2(54, 72)
		_corpo.add_child(costas)
	for i in _mao.size():
		var c: Dictionary = _mao[i]
		var v := _vista_carta(c)
		v.position = Vector2(60 + i * 106, 250)
		v.gui_input.connect(func(e: InputEvent):
			if e is InputEventMouseButton and e.pressed:
				_cartas_jogar(c))
		_corpo.add_child(v)


func _cartas_jogar(minha: Dictionary) -> void:
	_mao.erase(minha)
	var dele: Dictionary = _mao_adv[0]
	var dif: String = _adv.get("dificuldade", "fácil")
	if dif == "difícil" or (dif == "médio" and _rng.randf() < 0.5):
		# a carta mais fraca que ainda ganha; senão, a mais fraca de todas (não a desperdiça)
		var melhor: Dictionary = {}
		for c in _mao_adv:
			if _valor(c, minha) > _valor(minha, c) and (melhor.is_empty() or int(c.atq) < int(melhor.atq)):
				melhor = c
		if melhor.is_empty():
			for c in _mao_adv:
				if melhor.is_empty() or int(c.atq) < int(melhor.atq):
					melhor = c
		dele = melhor
	else:
		dele = _mao_adv[_rng.randi() % _mao_adv.size()]
	_mao_adv.erase(dele)
	var a := _valor(minha, dele)
	var b := _valor(dele, minha)
	var texto := ""
	if a > b:
		_pontos.x += 1
		texto = "Ganhaste a ronda! %s (%d) contra %s (%d)." % [minha.nome_pt, a, dele.nome_pt, b]
	elif b > a:
		_pontos.y += 1
		texto = "Perdeste a ronda. %s (%d) contra %s (%d)." % [minha.nome_pt, a, dele.nome_pt, b]
	else:
		texto = "Empate! %d contra %d." % [a, b]
	_ronda += 1
	# mostrar as duas cartas viradas
	_cartas_mesa(texto)
	var vm := _vista_carta(minha)
	vm.position = Vector2(200, 120)
	_corpo.add_child(vm)
	var vd := _vista_carta(dele)
	vd.position = Vector2(350, 120)
	_corpo.add_child(vd)
	for v in [vm, vd]:   # entram a crescer
		v.pivot_offset = v.size / 2.0
		v.scale = Vector2(0.2, 0.2)
		var tw := create_tween()
		tw.tween_property(v, "scale", Vector2.ONE, 0.25).set_trans(Tween.TRANS_BACK)
	if _pontos.x >= 3 or _pontos.y >= 3 or _mao.is_empty():
		var fim := _botao("Ver o resultado", _cartas_fim, _corpo)
		fim.position = Vector2(270, 90)


func _cartas_fim() -> void:
	_limpar(_corpo)
	var t := _texto(_corpo, Vector2(0, 40), 18)
	if _pontos.x > _pontos.y:
		_ganhar(_aposta * 2, "Venceste o %s às cartas! +%d ouro." % [_adv.nome_pt, _aposta * 2])
		t.text = "Venceste %d–%d! Ganhaste %d ouro." % [_pontos.x, _pontos.y, _aposta * 2]
		Jogo.por_flag("cartas_venceu_" + _adv.id)
		var todos := true
		for a in _cfg.get("cartas_adversarios", []):
			if not Jogo.tem_flag("cartas_venceu_" + a.id):
				todos = false
		if todos and not "rei_das_cartas" in Jogo.titulos:
			Jogo.titulos.append("rei_das_cartas")
			Sistema.mensagem("Título novo: Rei das Cartas", "nivel")
	elif _pontos.y > _pontos.x:
		t.text = "Perdeste %d–%d. O %s fica com a aposta." % [_pontos.x, _pontos.y, _adv.nome_pt]
	else:
		Jogo.ouro += _aposta
		_atualizar_ouro()
		t.text = "Empate! Recebes a aposta de volta."
	_botao("Jogar outra vez", func(): abrir_cartas(_adv.id), _corpo).position = Vector2(250, 120)


# ================================================================== BRAÇO DE FERRO ==================================================================

func abrir_braco(adversario: String) -> void:
	_jogo = "braco"
	for a in _cfg.get("braco_adversarios", []):
		if a.id == adversario:
			_adv = a
	abrir(true)
	_limpar(_corpo)
	_a_jogar = false
	_titulo.text = "Braço de ferro — contra %s" % _adv.get("nome_pt", "?")
	_atualizar_ouro()
	_texto(_corpo, Vector2(0, 0), 13, Color("c7dcd0")).text = "Carrega (ATACAR ou o botão) quando o cursor estiver na zona verde. A tua FOR alarga a zona."
	_escolher_aposta(40, _braco_comecar)


func _largura_zona() -> float:
	return minf(float(_cfg.get("braco_zona_max", 0.4)), float(_cfg.get("braco_zona", 0.16)) + Jogo.a("for") * float(_cfg.get("braco_zona_for", 0.006)))


func _braco_comecar() -> void:
	_limpar(_corpo)
	_forca = 0.5
	_cursor = 0.0
	_nova_zona()
	_barra = Control.new()
	_barra.position = Vector2(24, 60)
	_barra.size = Vector2(600, 240)
	_barra.draw.connect(_desenhar_braco)
	_corpo.add_child(_barra)
	_botao("FORÇA!", _braco_carregar, _corpo).position = Vector2(290, 320)
	_a_jogar = true


func _nova_zona() -> void:
	var w := _largura_zona()
	var x := _rng.randf_range(0.0, 1.0 - w)
	_zona = Vector2(x, x + w)


func _desenhar_braco() -> void:
	var c := _barra
	# o medidor de força: a tua cor da esquerda, a dele da direita
	var r := Rect2(0, 0, c.size.x, 26)
	c.draw_rect(r, Color("2e222f"))
	c.draw_rect(Rect2(2, 2, (c.size.x - 4) * _forca, 22), Color("4d9be6"))
	c.draw_rect(Rect2(2 + (c.size.x - 4) * _forca, 2, (c.size.x - 4) * (1.0 - _forca), 22), Color("ea4f36"))
	c.draw_string(ThemeDB.fallback_font, Vector2(6, 46), "Tu", HORIZONTAL_ALIGNMENT_LEFT, -1, 15, Color("8fd3ff"))
	c.draw_string(ThemeDB.fallback_font, Vector2(c.size.x - 70, 46), _adv.get("nome_pt", ""), HORIZONTAL_ALIGNMENT_LEFT, -1, 15, Color("f57d4a"))
	# os dois braços: a mão encontra-se na posição da força
	var meio := Vector2(c.size.x * (0.25 + 0.5 * _forca), 130)
	c.draw_line(Vector2(80, 180), meio, Color("fca790"), 18.0)
	c.draw_line(Vector2(c.size.x - 80, 180), meio, Color("e6904e"), 18.0)
	c.draw_circle(meio, 16, Color("cd683d"))
	c.draw_rect(Rect2(40, 182, c.size.x - 80, 10), Color("694f62"))   # a mesa
	# a barra do ritmo
	var b := Rect2(0, 210, c.size.x, 22)
	c.draw_rect(b, Color("3e3546"))
	c.draw_rect(Rect2(b.position.x + b.size.x * _zona.x, b.position.y, b.size.x * (_zona.y - _zona.x), b.size.y), Color("1ebc73"))
	c.draw_rect(Rect2(b.position.x + b.size.x * _cursor - 3, b.position.y - 4, 6, b.size.y + 8), Color("fbff86"))


func _process(delta: float) -> void:
	if visible and _a_rolar:
		_animar_dado(delta)
	if not visible or _jogo != "braco" or not _a_jogar:
		return
	var v := float(_adv.get("velocidade", 1.0)) * 0.9
	_cursor += _sentido * v * delta
	if _cursor > 1.0 or _cursor < 0.0:
		_sentido = -_sentido
		_cursor = clampf(_cursor, 0.0, 1.0)
	_forca -= float(_adv.get("empurra", 0.03)) * delta
	if _forca <= 0.0:
		_braco_fim(false)
	_barra.queue_redraw()


func _unhandled_input(e: InputEvent) -> void:
	if visible and _jogo == "braco" and _a_jogar and (e.is_action_pressed("atacar") or e.is_action_pressed("interagir")):
		_braco_carregar()
		get_viewport().set_input_as_handled()
		return
	super._unhandled_input(e)


func _braco_carregar() -> void:
	if not _a_jogar:
		return
	if _cursor >= _zona.x and _cursor <= _zona.y:
		_forca += float(_cfg.get("braco_acerto", 0.12))
		_nova_zona()
	else:
		_forca -= float(_cfg.get("braco_erro", 0.1))
	if _forca >= 1.0:
		_braco_fim(true)
	elif _forca <= 0.0:
		_braco_fim(false)


func _braco_fim(ganhou: bool) -> void:
	_a_jogar = false
	_limpar(_corpo)
	var t := _texto(_corpo, Vector2(0, 40), 18)
	if ganhou:
		_ganhar(_aposta * 2, "Venceste o %s no braço de ferro! +%d ouro." % [_adv.nome_pt, _aposta * 2])
		t.text = "Ganhaste! O %s esfrega o braço. +%d ouro." % [_adv.nome_pt, _aposta * 2]
		Jogo.por_flag("braco_venceu_" + _adv.id)
	else:
		t.text = "O %s ganhou. Para a próxima come mais sopa." % _adv.nome_pt
	_botao("Outra vez", func(): abrir_braco(_adv.id), _corpo).position = Vector2(270, 120)
