extends JanelaUI
## O jogo de ritmo (docs/ATIVIDADES.md 4.7 e 4.9; dados/minijogos.json "ritmo"): setas que descem pelas 4 pistas
## (as direções de andar) até à linha; carrega na hora certa. Também há botões no ecrã (telemóvel).

signal acabou(nota: String)   # quando a música acaba (as masmorras esperam por isto)

const ACOES := ["mover_esquerda", "mover_baixo", "mover_cima", "mover_direita"]
const SIMBOLOS := ["◀", "▼", "▲", "▶"]
const CORES := ["ea4f36", "4d9be6", "1ebc73", "f9c22b"]
const LINHA := 330.0           # y da linha de acertar (na janela)
const VELOCIDADE := 260.0      # píxeis por segundo

var _cfg: Dictionary = {}
var _pista: Control
var _texto_estado: Label
var _notas: Array = []         # [{tempo, pista, feita}]
var _t: float = -1.0
var _pontos: int = 0
var _combo: int = 0
var _a_tocar: bool = false
var _flash: Array = [0.0, 0.0, 0.0, 0.0]
var _ultimo: String = ""
var _ultimo_t: float = 0.0
var _quem: String = ""


func _ready() -> void:
	add_to_group("janelas")
	add_to_group("ritmo_ui")
	_cfg = Dados.tabela("minijogos").get("ritmo", {})
	_criar_janela(Vector2(390, 60), Vector2(500, 600))
	_texto(_janela, Vector2(20, 12), 20, Color("fbff86")).text = "Ritmo!"
	_texto_estado = _texto(_janela, Vector2(20, 40), 14, Color("c7dcd0"))
	_pista = Control.new()
	_pista.position = Vector2(50, 70)
	_pista.size = Vector2(400, 420)
	_pista.clip_contents = true
	_pista.draw.connect(_desenhar)
	_janela.add_child(_pista)
	for k in 4:   # botões para o telemóvel
		var b := _botao(SIMBOLOS[k], func(): _carregar(k), _janela)
		b.position = Vector2(62 + k * 100, 500)
		b.custom_minimum_size = Vector2(76, 44)
	_botao("Sair", func(): abrir(false), _janela).position = Vector2(420, 560)


## Começar uma música (com quem se dança: para o prémio e para a mensagem).
func dancar(com: String = "") -> void:
	_quem = com
	abrir(true)
	var bpm := float(_cfg.get("bpm", 110))
	var n := int(_cfg.get("setas", 40))
	var rng := RandomNumberGenerator.new()
	rng.randomize()
	_notas.clear()
	var t := 2.0
	for i in n:
		_notas.append({"tempo": t, "pista": rng.randi() % 4, "feita": false})
		t += 60.0 / bpm * (0.5 if rng.randf() < 0.25 else 1.0)
	_t = 0.0
	_pontos = 0
	_combo = 0
	_a_tocar = true
	_ultimo = ""


func _process(delta: float) -> void:
	if not visible or not _a_tocar:
		return
	_t += delta
	for k in 4:
		_flash[k] = maxf(0.0, _flash[k] - delta * 4.0)
	_ultimo_t = maxf(0.0, _ultimo_t - delta)
	# as que passaram da linha sem se carregar contam como falhadas
	for n in _notas:
		if not n.feita and _t - n.tempo > float(_cfg.get("bom", 0.16)):
			n.feita = true
			_combo = 0
			_ultimo = "Falhou"
			_ultimo_t = 0.5
	if _notas.all(func(n): return n.feita):
		_fim()
	_texto_estado.text = "Pontos: %d   Combo: %d   %s" % [_pontos, _combo, _ultimo if _ultimo_t > 0.0 else ""]
	_pista.queue_redraw()


func _unhandled_input(e: InputEvent) -> void:
	if visible and _a_tocar:
		for k in 4:
			if e.is_action_pressed(ACOES[k]):
				_carregar(k)
				get_viewport().set_input_as_handled()
				return
	super._unhandled_input(e)


func _carregar(pista: int) -> void:
	if not _a_tocar:
		return
	_flash[pista] = 1.0
	var melhor: Dictionary = {}
	for n in _notas:
		if not n.feita and n.pista == pista and absf(n.tempo - _t) <= float(_cfg.get("bom", 0.16)):
			if melhor.is_empty() or absf(n.tempo - _t) < absf(melhor.tempo - _t):
				melhor = n
	if melhor.is_empty():
		return
	melhor.feita = true
	_combo += 1
	if absf(melhor.tempo - _t) <= float(_cfg.get("perfeito", 0.08)):
		_pontos += int(_cfg.get("pontos_perfeito", 100)) + _combo
		_ultimo = "Perfeito!"
	else:
		_pontos += int(_cfg.get("pontos_bom", 50))
		_ultimo = "Bom"
	_ultimo_t = 0.5


func _desenhar() -> void:
	var c := _pista
	c.draw_rect(Rect2(Vector2.ZERO, c.size), Color("2e222f"))
	for k in 4:
		var x := k * 100.0
		c.draw_rect(Rect2(x + 4, 0, 92, c.size.y), Color(CORES[k]).darkened(0.8))
		# a linha de acertar
		var alvo := Rect2(x + 14, LINHA - 22, 72, 44)
		c.draw_rect(alvo, Color(CORES[k]).lerp(Color.WHITE, _flash[k] * 0.6), false, 3.0)
		c.draw_string(ThemeDB.fallback_font, Vector2(x + 38, LINHA + 9), SIMBOLOS[k], HORIZONTAL_ALIGNMENT_LEFT, -1, 24, Color(CORES[k]).darkened(0.3))
	for n in _notas:
		if n.feita:
			continue
		var y: float = LINHA - (float(n.tempo) - _t) * VELOCIDADE
		if y < -40 or y > c.size.y + 40:
			continue
		var x := int(n.pista) * 100.0
		c.draw_rect(Rect2(x + 18, y - 18, 64, 36), Color(CORES[n.pista]))
		c.draw_rect(Rect2(x + 18, y - 18, 64, 6), Color(CORES[n.pista]).lightened(0.4))
		c.draw_string(ThemeDB.fallback_font, Vector2(x + 38, y + 9), SIMBOLOS[n.pista], HORIZONTAL_ALIGNMENT_LEFT, -1, 24, Color("2e222f"))


func _fim() -> void:
	_a_tocar = false
	var maximo := float(_notas.size() * int(_cfg.get("pontos_perfeito", 100)))
	var pct := 100.0 * _pontos / maxf(1.0, maximo)
	var nota := "C"
	var notas: Dictionary = _cfg.get("notas", {})
	for k in ["S", "A", "B"]:
		if pct >= float(notas.get(k, 101)):
			nota = k
			break
	var ouro := _pontos / int(_cfg.get("ouro_por", 20))
	Jogo.ganhar_ouro(ouro)
	Colecoes.maximo("ritmo_melhor", _pontos)
	if _quem != "" and nota in ["S", "A"]:
		Amizade.mudar(_quem, 10)
	_texto_estado.text = "Nota %s! %d pontos (+%d ouro)" % [nota, _pontos, ouro]
	Sistema.mensagem("Dança acabada: nota %s, %d pontos, +%d ouro." % [nota, _pontos, ouro], "nivel")
	acabou.emit(nota)
