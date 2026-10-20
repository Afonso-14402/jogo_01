extends JanelaUI
## Janela de Opções (docs/INTERFACE.md, secção 7): som, ecrã, jogo e acessibilidade.

var _corpo: VBoxContainer


func _ready() -> void:
	add_to_group("janelas")
	add_to_group("opcoes_ui")
	_criar_janela(Vector2(340, 30), Vector2(600, 660))
	_texto(_janela, Vector2(20, 12), 18, Color("8fd3ff")).text = "Opções"
	_corpo = VBoxContainer.new()
	_corpo.position = Vector2(24, 52)
	_corpo.custom_minimum_size = Vector2(550, 0)
	_corpo.add_theme_constant_override("separation", 8)
	_janela.add_child(_corpo)


func _mostrar() -> void:
	_limpar(_corpo)
	_titulo_grupo("Som")
	_deslizar("Volume geral", "volume_geral")
	_deslizar("Música", "volume_musica")
	_deslizar("Efeitos", "volume_efeitos")
	_deslizar("Vozes (bips)", "volume_bips")
	_titulo_grupo("Ecrã e jogo")
	_caixa("Ecrã inteiro", "ecra_inteiro")
	_caixa("Mostrar números de dano", "numeros_dano")
	_caixa("Gravação automática", "gravacao_automatica")
	_deslizar("Velocidade do texto", "velocidade_texto", 0.5, 2.0)
	_titulo_grupo("Telemóvel")
	_deslizar("Tamanho dos botões", "botoes_tamanho", 0.7, 1.4)
	_deslizar("Transparência dos botões", "botoes_alfa", 0.3, 1.0)
	_caixa("Modo canhoto", "canhoto")
	_titulo_grupo("Acessibilidade")
	_caixa("Tremor do ecrã", "tremor")
	_caixa("Flashes (relâmpagos, críticos)", "flashes")
	_botao("Fechar", func(): abrir(false), _corpo)


func _titulo_grupo(t: String) -> void:
	var l := Label.new()
	l.text = t
	l.add_theme_font_size_override("font_size", 15)
	l.add_theme_color_override("font_color", Color("fbff86"))
	_corpo.add_child(l)


func _deslizar(nome: String, chave: String, mn := 0.0, mx := 1.0) -> void:
	var h := HBoxContainer.new()
	_corpo.add_child(h)
	var l := Label.new()
	l.text = nome
	l.custom_minimum_size = Vector2(220, 0)
	h.add_child(l)
	var s := HSlider.new()
	s.min_value = mn
	s.max_value = mx
	s.step = 0.05
	s.value = float(Opcoes.v(chave))
	s.custom_minimum_size = Vector2(300, 20)
	s.value_changed.connect(func(x): Opcoes.mudar(chave, x))
	h.add_child(s)


func _caixa(nome: String, chave: String) -> void:
	var c := CheckBox.new()
	c.text = nome
	c.button_pressed = bool(Opcoes.v(chave))
	c.toggled.connect(func(x): Opcoes.mudar(chave, x))
	_corpo.add_child(c)
