extends Node3D
## Menu inicial (docs/INTERFACE.md, secção 6): a torre à noite com nuvens a passar, o logótipo, e
## Continuar · Novo Jogo · Carregar · Opções · Créditos. Novo jogo: espaço (1–3) → dificuldade → cena P1 (a Origem,
## docs/guiao/prologo.md) → criar personagem → andar 1.

const VERSAO := "Demo 0.1"
const DIFICULDADES := [["historia", "História", "Dano recebido ×0,5 · não perdes nada ao morrer"],
	["normal", "Normal", "A experiência pensada para o jogo"],
	["dificil", "Difícil", "Dano recebido ×1,5 · perdes 50% dos materiais · drops ×1,2"],
	["hardcore", "Hardcore", "Como o Difícil, mas se morreres o jogo acaba"]]
const ORIGENS := [["atrasado", "A caminho da escola, a correr porque estava atrasad{o/a}."],
	["jogador", "A jogar até tarde, só mais um nível."], ["ajudante", "A ajudar alguém que precisava."],
	["dormir", "A dormir. Só a dormir."]]
const PARTES := [["penteado", "Penteado"], ["pele", "Pele"], ["cabelo", "Cabelo"], ["olhos", "Olhos"], ["roupa", "Roupa"]]

var _ui: Control
var _painel: VBoxContainer
var _nuvens: Array = []
var _logo: TextureRect
var _logo_t := 0.0
var _escolhas := {"espaco": 1, "dificuldade": "normal", "origem": "", "nome": "", "tratamento": "ele",
	"aparencia": {"penteado": "espetado", "pele": "clara", "cabelo": "castanho_avermelhado", "olhos": "preto", "roupa": "camisola_capuz"}}
var _previa: AnimatedSprite2D
var _dir := 0


func _ready() -> void:
	_cenario()
	var camada := CanvasLayer.new()
	add_child(camada)
	_ui = Control.new()
	_ui.set_anchors_preset(Control.PRESET_FULL_RECT)
	camada.add_child(_ui)
	for i in 5:
		var n := TextureRect.new()
		n.texture = load("res://arte/ui/nuvem_%d.png" % (i % 3 + 1))
		n.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
		n.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
		n.size = Vector2(48, 16) * (4 + i % 3)
		n.position = Vector2(randf_range(-200, 1280), 40 + i * 70)
		n.modulate.a = 0.75
		_ui.add_child(n)
		_nuvens.append([n, 12.0 + i * 6.0])
	_logo = TextureRect.new()
	_logo.texture = AtlasTexture.new()
	(_logo.texture as AtlasTexture).atlas = load("res://arte/ui/logo.png")
	(_logo.texture as AtlasTexture).region = Rect2(0, 0, 160, 64)
	_logo.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	_logo.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	_logo.size = Vector2(640, 256)
	_logo.position = Vector2(320, 10)
	_ui.add_child(_logo)
	var v := Label.new()
	v.text = VERSAO
	v.position = Vector2(1180, 690)
	v.add_theme_color_override("font_color", Color("9babb2"))
	_ui.add_child(v)
	var opc := preload("res://scripts/ui/opcoes_ui.gd").new()
	add_child(opc)
	_painel = VBoxContainer.new()
	_painel.position = Vector2(490, 300)
	_painel.custom_minimum_size = Vector2(300, 0)
	_painel.add_theme_constant_override("separation", 10)
	_ui.add_child(_painel)
	Audio.tocar_musica("menu")
	_menu_principal()


var _fundo_2d: TextureRect
var _fundo_t := 0.0


## A torre à noite em pixel art 2D (ferramentas/arte/menu_fundo.py): as estrelas piscam e as janelas tremeluzem.
func _cenario() -> void:
	var fundo := CanvasLayer.new()
	fundo.layer = -1
	add_child(fundo)
	_fundo_2d = TextureRect.new()
	var at := AtlasTexture.new()
	at.atlas = load("res://arte/ui/menu_fundo.png")
	at.region = Rect2(0, 0, 426, 240)
	_fundo_2d.texture = at
	_fundo_2d.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	_fundo_2d.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	_fundo_2d.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_COVERED
	_fundo_2d.set_anchors_preset(Control.PRESET_FULL_RECT)
	fundo.add_child(_fundo_2d)


func _process(delta: float) -> void:
	for n in _nuvens:
		n[0].position.x += n[1] * delta
		if n[0].position.x > 1300:
			n[0].position.x = -n[0].size.x
	_logo_t += delta
	(_logo.texture as AtlasTexture).region = Rect2(int(_logo_t * 9.0) % 8 * 160, 0, 160, 64)
	if _fundo_2d:   # as estrelas piscam e as janelas tremeluzem (4 quadros)
		_fundo_t += delta
		(_fundo_2d.texture as AtlasTexture).region = Rect2(int(_fundo_t * 3.0) % 4 * 426, 0, 426, 240)
	if _previa and is_instance_valid(_previa):
		_previa.flip_h = _dir == 3


# ------------------------------------------------------------------ ecrãs ------------------------------------------------------------------

func _limpar() -> void:
	for c in _painel.get_children():
		c.queue_free()


func _b(texto: String, cb: Callable, ativo := true) -> Button:
	var b := Button.new()
	b.text = texto
	b.add_theme_font_size_override("font_size", 18)
	b.custom_minimum_size = Vector2(300, 40)
	b.disabled = not ativo
	b.pressed.connect(cb)
	_painel.add_child(b)
	return b


func _t(texto: String, tam := 16, cor := Color.WHITE) -> Label:
	var l := Label.new()
	l.text = Sistema.genero(texto) if "{" in texto else texto
	l.add_theme_font_size_override("font_size", tam)
	l.add_theme_color_override("font_color", cor)
	l.add_theme_color_override("font_outline_color", Color("2e222f"))
	l.add_theme_constant_override("outline_size", 4)
	l.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	l.custom_minimum_size = Vector2(300, 0)
	_painel.add_child(l)
	return l


func _menu_principal() -> void:
	_limpar()
	if _ui.has_node("fundo_criar"):
		_ui.get_node("fundo_criar").queue_free()
	if _previa and is_instance_valid(_previa):
		_previa.queue_free()
	_logo.visible = true
	_painel.position = Vector2(490, 300)
	var ultimo := _ultimo_espaco()
	var bc := _b("Continuar", func(): _carregar(ultimo), ultimo > 0)
	_b("Novo Jogo", _novo_espaco)
	_b("Carregar", _escolher_para_carregar)
	_b("Opções", func(): get_tree().get_first_node_in_group("opcoes_ui").abrir(true))
	_b("Créditos", _creditos)
	_b("Sair", func(): get_tree().quit())
	(bc if ultimo > 0 else _painel.get_child(1)).grab_focus.call_deferred()


func _ultimo_espaco() -> int:
	var melhor := 0
	var data := ""
	for i in range(1, 4):
		if Gravar.existe(i):
			var d: Variant = JSON.parse_string(FileAccess.get_file_as_string(Gravar.caminho(i)))
			if d is Dictionary and String(d.get("gravado", "")) > data:
				data = d.get("gravado", "")
				melhor = i
	return melhor


func _resumo(i: int) -> String:
	if not Gravar.existe(i):
		return "Espaço %d — vazio" % i
	var d: Variant = JSON.parse_string(FileAccess.get_file_as_string(Gravar.caminho(i)))
	if not d is Dictionary:
		return "Espaço %d — estragado" % i
	var j: Dictionary = d.get("jogador", {})
	var horas := int(float(d.get("tempo_jogado", 0)) / 3600.0)
	return "Espaço %d — %s · Nv %d · Andar %d · %dh" % [i, j.get("nome", "?"), int(j.get("nivel", 1)),
		int(d.get("andares", {}).get("desbloqueados", 1)), horas]


func _escolher_para_carregar() -> void:
	_limpar()
	_t("Carregar", 22, Color("8fd3ff"))
	for i in range(1, 4):
		_b(_resumo(i), func(): _carregar(i), Gravar.existe(i))
	_b("Voltar", _menu_principal)


func _carregar(i: int) -> void:
	if Gravar.carregar(i):
		Jogo.espaco_gravacao = i
		Cenas.mudar("res://cenas/mundo/cidade.tscn" if Jogo.andar_atual <= 0 else "res://cenas/mundo/andar.tscn")


func _novo_espaco() -> void:
	_limpar()
	_t("Novo Jogo — escolhe um espaço", 22, Color("8fd3ff"))
	for i in range(1, 4):
		_b(_resumo(i) + (" (vai ser apagado)" if Gravar.existe(i) else ""), func(): _escolhas.espaco = i; _dificuldade())
	_b("Voltar", _menu_principal)


func _dificuldade() -> void:
	_limpar()
	_t("Dificuldade", 22, Color("8fd3ff"))
	for d in DIFICULDADES:
		_b(d[1], func(): _escolhas.dificuldade = d[0]; _cena_p1())
		_t(d[2], 12, Color("9babb2"))
	_b("Voltar", _novo_espaco)


## P1 — Antes (docs/guiao/prologo.md): ecrã preto e a pergunta da Origem.
func _cena_p1() -> void:
	_limpar()
	_logo.visible = false
	_painel.position = Vector2(340, 160)
	_painel.custom_minimum_size = Vector2(600, 0)
	for linha in ["Lembras-te do último dia normal?", "Do cheiro da tua casa. Do barulho da rua.", "O que estavas a fazer antes de tudo ficar azul?"]:
		var l := _t(linha, 20, Color("c7dcd0"))
		l.custom_minimum_size.x = 600
		l.modulate.a = 0.0
		create_tween().tween_property(l, "modulate:a", 1.0, 1.0)
		await get_tree().create_timer(1.1).timeout
	for o in ORIGENS:
		var b := _b("▶ " + Sistema.genero(o[1]), func(): _escolhas.origem = o[0]; _depois_p1())
		b.custom_minimum_size.x = 600
		b.alignment = HORIZONTAL_ALIGNMENT_LEFT


func _depois_p1() -> void:
	_limpar()
	var l := _t("Então lembra-te disso. Vais precisar.", 20, Color("c7dcd0"))
	l.custom_minimum_size.x = 600
	await get_tree().create_timer(1.6).timeout
	_t("[Sistema] A criar o registo do Jogador…", 18, Color("8fd3ff"))
	await get_tree().create_timer(1.2).timeout
	_criar_personagem()


# ------------------------------------------------------------------ criar personagem ------------------------------------------------------------------

func _criar_personagem() -> void:
	_limpar()
	_logo.visible = false
	if not _ui.has_node("fundo_criar"):
		var f := NinePatchRect.new()
		f.name = "fundo_criar"
		f.texture = load("res://arte/ui/janela_sistema.png")
		for m in ["patch_margin_left", "patch_margin_right", "patch_margin_top", "patch_margin_bottom"]:
			f.set(m, 6)
		f.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
		f.position = Vector2(200, 70)
		f.size = Vector2(880, 560)
		_ui.add_child(f)
		_ui.move_child(f, _painel.get_index())
	_painel.position = Vector2(620, 90)
	_painel.custom_minimum_size = Vector2(420, 0)
	_t("Criar personagem", 22, Color("8fd3ff"))
	var nome := LineEdit.new()
	nome.placeholder_text = "Nome"
	nome.max_length = 14
	nome.text = _escolhas.nome
	nome.custom_minimum_size = Vector2(300, 36)
	nome.text_changed.connect(func(t): _escolhas.nome = t)
	_painel.add_child(nome)
	var trat := HBoxContainer.new()
	_painel.add_child(trat)
	var lt := Label.new()
	lt.text = "Tratamento: "
	trat.add_child(lt)
	for t in [["ele", "ele"], ["ela", "ela"]]:
		var b := Button.new()
		b.text = t[1]
		b.toggle_mode = true
		b.button_pressed = _escolhas.tratamento == t[0]
		b.pressed.connect(func(): _escolhas.tratamento = t[0]; Jogo.tratamento = t[0]; _criar_personagem())
		trat.add_child(b)
	for parte in PARTES:
		var h := HBoxContainer.new()
		_painel.add_child(h)
		var lb := Label.new()
		lb.text = parte[1]
		lb.custom_minimum_size = Vector2(110, 0)
		h.add_child(lb)
		var ops: Array = Aparencia.opcoes("penteados" if parte[0] == "penteado" else parte[0])
		if parte[0] == "roupa":
			ops = ops.filter(func(x): return x != "aventureiro")   # no prólogo trazes a roupa do teu mundo
		var atual: String = _escolhas.aparencia[parte[0]]
		var i := maxi(0, ops.find(atual))
		var menos := Button.new()
		menos.text = "◀"
		menos.pressed.connect(func(): _escolhas.aparencia[parte[0]] = ops[(i - 1 + ops.size()) % ops.size()]; _criar_personagem())
		h.add_child(menos)
		var v := Label.new()
		v.text = String(atual).replace("_", " ").capitalize()
		v.custom_minimum_size = Vector2(190, 0)
		v.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
		h.add_child(v)
		var mais := Button.new()
		mais.text = "▶"
		mais.pressed.connect(func(): _escolhas.aparencia[parte[0]] = ops[(i + 1) % ops.size()]; _criar_personagem())
		h.add_child(mais)
	_b("Rodar", func(): _dir = (_dir + 1) % 4; _criar_personagem())
	_b("Começar", _comecar, true)
	_b("Voltar", _dificuldade)
	# pré-visualização do herói, grande, a andar
	if _previa and is_instance_valid(_previa):
		_previa.queue_free()
	_previa = AnimatedSprite2D.new()
	_previa.sprite_frames = Aparencia.frames(_escolhas.aparencia, {"andar": [8, true], "parado": [5, true]}, ["baixo", "cima", "lado"])
	_previa.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	_previa.scale = Vector2(7, 7)
	_previa.position = Vector2(400, 430)
	_ui.add_child(_previa)
	_previa.play("andar_" + ["baixo", "lado", "cima", "lado"][_dir])
	if _ui.has_node("retrato_criar"):
		_ui.get_node("retrato_criar").free()
	var r := TextureRect.new()   # o retrato com as mesmas cores
	r.name = "retrato_criar"
	r.texture = Aparencia.retrato(_escolhas.aparencia, "feliz")
	r.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	r.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	r.size = Vector2(128, 128)
	r.position = Vector2(230, 90)
	_ui.add_child(r)


func _comecar() -> void:
	if String(_escolhas.nome).strip_edges() == "":
		_escolhas.nome = "Jogador"
	Jogo.novo_jogo(String(_escolhas.nome).strip_edges())
	Jogo.tratamento = _escolhas.tratamento
	Jogo.aparencia = _escolhas.aparencia.duplicate()
	Jogo.dificuldade = _escolhas.dificuldade
	Jogo.origem = _escolhas.origem
	Jogo.espaco_gravacao = int(_escolhas.espaco)
	Jogo.andar_atual = 1
	Jogo.por_flag("prologo_p2")
	Tempo.hora = 7.0
	Tempo.dia = 1
	Tempo.estacao = 0
	Tempo.ano = 1
	Gravar.gravar(Jogo.espaco_gravacao)
	Cenas.mudar("res://cenas/mundo/andar.tscn")


func _creditos() -> void:
	_limpar()
	_t("Ascendia", 22, Color("fbff86"))
	_t("Arte, textos e código feitos com o Claude, a partir da bíblia do jogo (docs/).", 15)
	_t("Motor: Godot 4 · Arte: pixel art feita por código · Música e sons: a caminho", 13, Color("9babb2"))
	_b("Voltar", _menu_principal)
