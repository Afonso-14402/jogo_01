extends JanelaUI
## Menu de pausa (docs/INTERFACE.md, secção 4): Esc abre. Continuar · Mochila · Status · Diário · Opções ·
## Gravar (só em camas e cristais) · Sair para o menu.

var _corpo: VBoxContainer


func _ready() -> void:
	acao = "pausa"
	add_to_group("janelas")
	add_to_group("pausa_ui")
	_criar_janela(Vector2(490, 150), Vector2(300, 420))
	_texto(_janela, Vector2(20, 12), 18, Color("8fd3ff")).text = "Pausa"
	_corpo = VBoxContainer.new()
	_corpo.position = Vector2(24, 52)
	_corpo.custom_minimum_size = Vector2(252, 0)
	_corpo.add_theme_constant_override("separation", 8)
	_janela.add_child(_corpo)


func _unhandled_input(e: InputEvent) -> void:
	# Esc fecha a janela que estiver aberta; só abre a pausa se não houver nenhuma
	if e.is_action_pressed("pausa"):
		for j in get_tree().get_nodes_in_group("janelas"):
			if j != self and j.visible:
				return
		var d = get_tree().get_first_node_in_group("dialogo_ui")
		if d and d.visible:
			return
		abrir(not visible)
		get_viewport().set_input_as_handled()


func _mostrar() -> void:
	_limpar(_corpo)
	_botao("Continuar", func(): abrir(false), _corpo)
	for par in [["Mochila", "inventario_ui"], ["Diário", "diario_ui"], ["Mapa", "mapa_ui"], ["Opções", "opcoes_ui"]]:
		_botao(par[0], func():
			abrir(false)
			var j = get_tree().get_first_node_in_group(par[1])
			if j:
				j.abrir(true), _corpo)
	_botao("Status", func():
		abrir(false)
		for j in get_tree().get_nodes_in_group("janelas"):
			if j.acao == "status":
				j.abrir(true), _corpo)
	var g := _botao("Gravar", Callable(), _corpo)
	g.disabled = true
	g.tooltip_text = "Grava-se nas camas e nos cristais das Zonas Seguras."
	_botao("Sair para o menu", func():
		abrir(false)
		Cenas.mudar("res://cenas/ui/menu_inicial.tscn"), _corpo)
	(_corpo.get_child(0) as Button).grab_focus.call_deferred()
