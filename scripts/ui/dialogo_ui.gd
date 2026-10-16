extends CanvasLayer
## Caixa de diálogo (docs/INTERFACE.md, secção 5; docs/NPCS.md, secção 1): retrato com a emoção à esquerda, nome,
## texto letra a letra com "bips" de voz, escolhas em lista. Carregar acaba a frase; carregar outra vez passa à seguinte.
## O jogo fica em pausa enquanto fala. Uso: await dialogo.falar(falas, "lyra") · var i = await dialogo.escolher([...])

signal _avancar
signal _escolheu(i: int)

const UI := "res://arte/ui/"

var _caixa: NinePatchRect
var _retrato: TextureRect
var _nome: Label
var _texto: RichTextLabel
var _escolhas: VBoxContainer
var _narracao: Label
var _a_escrever := false
var _npc := ""
var _bip: AudioStreamPlayer
var ocupado := false


func _ready() -> void:
	add_to_group("dialogo_ui")
	layer = 6
	process_mode = Node.PROCESS_MODE_ALWAYS
	_caixa = NinePatchRect.new()
	_caixa.texture = load(UI + "janela_dialogo.png")
	for m in ["patch_margin_left", "patch_margin_right", "patch_margin_top", "patch_margin_bottom"]:
		_caixa.set(m, 8)
	_caixa.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	_caixa.position = Vector2(140, 530)
	_caixa.size = Vector2(1000, 170)
	add_child(_caixa)
	var fundo := ColorRect.new()   # fundo escuro para o HUD não se ver por trás
	fundo.color = Color(0.13, 0.1, 0.16, 0.9)
	fundo.position = Vector2(4, 4)
	fundo.size = _caixa.size - Vector2(8, 8)
	fundo.mouse_filter = Control.MOUSE_FILTER_IGNORE
	_caixa.add_child(fundo)
	_retrato = TextureRect.new()
	_retrato.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	_retrato.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	_retrato.position = Vector2(14, 14)
	_retrato.size = Vector2(142, 142)
	_caixa.add_child(_retrato)
	_nome = Label.new()
	_nome.position = Vector2(172, 10)
	_nome.add_theme_font_size_override("font_size", 18)
	_nome.add_theme_color_override("font_color", Color("fbff86"))
	_nome.add_theme_color_override("font_outline_color", Color("2e222f"))
	_nome.add_theme_constant_override("outline_size", 4)
	_caixa.add_child(_nome)
	_texto = RichTextLabel.new()
	_texto.bbcode_enabled = true
	_texto.position = Vector2(172, 40)
	_texto.size = Vector2(810, 120)
	_texto.add_theme_font_size_override("normal_font_size", 18)
	_texto.add_theme_font_size_override("bold_font_size", 19)
	_texto.add_theme_color_override("default_color", Color.WHITE)
	_texto.add_theme_color_override("font_outline_color", Color("2e222f"))
	_texto.add_theme_constant_override("outline_size", 3)
	_texto.mouse_filter = Control.MOUSE_FILTER_IGNORE
	_caixa.add_child(_texto)
	_narracao = Label.new()
	_narracao.position = Vector2(140, 486)
	_narracao.size = Vector2(1000, 40)
	_narracao.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	_narracao.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	_narracao.add_theme_font_size_override("font_size", 14)
	_narracao.add_theme_color_override("font_color", Color("c7dcd0"))
	_narracao.add_theme_color_override("font_outline_color", Color("2e222f"))
	_narracao.add_theme_constant_override("outline_size", 4)
	add_child(_narracao)
	_escolhas = VBoxContainer.new()
	_escolhas.position = Vector2(760, 330)
	_escolhas.custom_minimum_size = Vector2(380, 0)
	_escolhas.alignment = BoxContainer.ALIGNMENT_END
	add_child(_escolhas)
	_bip = AudioStreamPlayer.new()
	_bip.stream = _gerar_bip()
	_bip.volume_db = -14.0 + linear_to_db(maxf(0.01, float(Opcoes.v("volume_bips"))))
	add_child(_bip)
	visible = false


## "Voz" do NPC: um bip curto (onda quadrada); o tom muda de NPC para NPC.
func _gerar_bip() -> AudioStreamWAV:
	var w := AudioStreamWAV.new()
	w.format = AudioStreamWAV.FORMAT_8_BITS
	w.mix_rate = 22050
	var dados := PackedByteArray()
	var n := 900
	for i in n:
		var env := 1.0 - float(i) / n
		dados.append(int((64 if (i / 20) % 2 == 0 else -64) * env) & 0xFF)
	w.data = dados
	return w


func _unhandled_input(e: InputEvent) -> void:
	if not visible or _escolhas.get_child_count() > 0:
		return
	if e.is_action_pressed("interagir") or e.is_action_pressed("atacar") or (e is InputEventMouseButton and e.pressed):
		get_viewport().set_input_as_handled()
		if _a_escrever:
			_a_escrever = false
			_texto.visible_ratio = 1.0
		else:
			_avancar.emit()


## Mostra uma lista de falas (ver ferramentas/dados/dialogos.py). Devolve a última escolha feita (ou -1).
func falar(falas: Array, npc: String = "") -> int:
	_npc = npc
	var abriu := not ocupado
	ocupado = true
	visible = true
	get_tree().paused = true
	var escolha := -1
	for f in falas:
		if f.has("ramo") and int(f.ramo) != escolha:
			continue
		if f.has("escolhas"):
			escolha = await escolher(f.escolhas)
		elif f.has("texto"):
			await _mostrar_fala(f)
		elif f.has("acao") or f.has("camara"):
			_narracao.text = f.get("acao", f.get("camara", ""))
		if f.has("efeito"):
			_efeito(f)
	if abriu:
		fechar()
	return escolha


func fechar() -> void:
	ocupado = false
	visible = false
	_narracao.text = ""
	get_tree().paused = false


func _mostrar_fala(f: Dictionary) -> void:
	var quem: String = f.get("quem", "")
	var npc_id := _id_de(quem)
	var emo: String = f.get("emocao", "normal")
	var caminho := "res://arte/retratos/%s_%s.png" % [npc_id, emo]
	if not ResourceLoader.exists(caminho):
		caminho = "res://arte/retratos/%s_normal.png" % npc_id
	_retrato.texture = load(caminho) if ResourceLoader.exists(caminho) else null
	_retrato.visible = _retrato.texture != null
	_nome.text = quem
	_texto.position.x = 172 if _retrato.visible else 24
	_nome.position.x = _texto.position.x
	_texto.text = _preparar(f.texto)
	_texto.visible_ratio = 0.0
	_a_escrever = true
	var total := _texto.get_total_character_count()
	var vel := float(Dados.c("dialogo_letras_por_segundo", 45)) * float(Opcoes.v("velocidade_texto"))
	var tom := 0.8 + float(hash(npc_id) % 60) / 100.0
	var limpo := _texto.get_parsed_text()
	var i := 0
	var t := 0.0
	while _a_escrever and i < total:
		await get_tree().process_frame
		t += get_process_delta_time()
		var antes := i
		while i < total and t >= 1.0 / vel:   # letras pelo tempo que passou (não depende dos FPS)
			t -= 1.0 / vel
			i += 1
			if limpo.substr(i - 1, 1) in ".!?…":
				t -= 5.0 / vel   # pausa depois de um ponto
		_texto.visible_characters = i
		if i / 3 != antes / 3:
			_bip.pitch_scale = tom * randf_range(0.95, 1.05)
			_bip.play()
	_a_escrever = false
	_texto.visible_ratio = 1.0
	await _avancar


## {nome}, {o/a} e **negrito**.
func _preparar(t: String) -> String:
	t = t.replace("{nome}", Jogo.nome)
	t = Sistema.genero(t)
	var re := RegEx.new()
	re.compile("\\*\\*(.+?)\\*\\*")
	return re.sub(t, "[b]$1[/b]", true)


func _id_de(quem: String) -> String:
	if _npc != "" and Dados.obter("npcs", _npc).get("nome_pt", "") == quem:
		return _npc
	for n in Dados.tabela("npcs").values():
		if n.nome_pt == quem or quem in n.nome_pt:
			return n.id
	return quem.to_lower().replace(" ", "_")


## Escolhas: botões em lista, por cima da caixa. Devolve o índice.
func escolher(opcoes: Array) -> int:
	var abriu := not visible
	if abriu:
		visible = true
		get_tree().paused = true
	for c in _escolhas.get_children():
		c.queue_free()
	for i in opcoes.size():
		var b := Button.new()
		b.text = "▶ " + _preparar(str(opcoes[i])).replace("[b]", "").replace("[/b]", "")
		b.add_theme_font_size_override("font_size", 16)
		b.alignment = HORIZONTAL_ALIGNMENT_LEFT
		b.pressed.connect(func(): _escolheu.emit(i))
		_escolhas.add_child(b)
	(_escolhas.get_child(0) as Button).grab_focus.call_deferred()
	var i: int = await _escolheu
	for c in _escolhas.get_children():
		c.queue_free()
	if abriu and not ocupado:
		fechar()
	return i


## ⚙ efeitos que o jogo já sabe fazer: amizade (+30); o resto fica escrito no registo.
func _efeito(f: Dictionary) -> void:
	if f.has("amizade") and _npc != "":
		Amizade.mudar(_npc, int(f.amizade))
