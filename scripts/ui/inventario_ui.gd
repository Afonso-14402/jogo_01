extends JanelaUI
## Janela da Mochila (docs/INTERFACE.md, secção 4): grelha de itens com filtros, detalhes, usar, equipar,
## pôr na barra rápida, deitar fora. Abre com I (ação "inventario"); o jogo fica em pausa enquanto está aberta.

const COLUNAS := 6
const FILTROS := [["tudo", "Tudo"], ["equip", "Equipamento"], ["consumivel", "Consumíveis"], ["material", "Materiais"], ["missao", "Missão"]]

var _grelha: GridContainer
var _info: Label
var _titulo: Label
var _botoes: HBoxContainer
var _filtro := "tudo"
var _escolhido := -1          # índice do espaço (ou -1)
var _missao_escolhida := ""


func _ready() -> void:
	acao = "inventario"
	add_to_group("inventario_ui")
	add_to_group("janelas")
	_criar_janela(Vector2(240, 90), Vector2(800, 520))
	_titulo = _texto(_janela, Vector2(20, 12), 18)
	var filtros := HBoxContainer.new()
	filtros.position = Vector2(20, 44)
	_janela.add_child(filtros)
	for f in FILTROS:
		var b := _botao(f[1])
		b.pressed.connect(func(): _filtro = f[0]; _escolhido = -1; _missao_escolhida = ""; _mostrar())
		filtros.add_child(b)
	_grelha = GridContainer.new()
	_grelha.columns = COLUNAS
	_grelha.position = Vector2(20, 90)
	_grelha.add_theme_constant_override("h_separation", 4)
	_grelha.add_theme_constant_override("v_separation", 4)
	_janela.add_child(_grelha)
	_info = _texto(_janela, Vector2(370, 90), 14)
	_info.size = Vector2(410, 300)
	_info.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	_botoes = HBoxContainer.new()
	_botoes.position = Vector2(370, 440)
	_janela.add_child(_botoes)
	Jogo.inventario.mudou.connect(func(): if visible: _mostrar())


func abrir(sim: bool) -> void:
	if sim != visible:
		Audio.efeito("abrir_janela" if sim else "fechar_janela", 0.0)
	_escolhido = -1
	_missao_escolhida = ""
	super.abrir(sim)


func _passa(e) -> bool:
	if e == null:
		return _filtro == "tudo"
	var cat: String = Inventario._dados(e.id).get("categoria", "")
	match _filtro:
		"equip":
			return Inventario.e_equipamento(e.id)
		"consumivel", "material":
			return cat == _filtro
		"missao":
			return false
	return true


func _mostrar() -> void:
	var inv: Inventario = Jogo.inventario
	_titulo.text = "Mochila   %d/%d   ·   %.1f kg   ·   %d ouro" % [inv.tamanho() - inv.livres(), inv.tamanho(), inv.peso(), Jogo.ouro]
	for c in _grelha.get_children():
		c.queue_free()
	if _filtro == "missao":
		for id in inv.missao:
			_grelha.add_child(_casa(id, int(inv.missao[id]), "comum", id == _missao_escolhida, func(): _missao_escolhida = id; _mostrar()))
	else:
		for i in inv.tamanho():
			var e = inv.espacos[i]
			if not _passa(e):
				continue
			var cb := func(): _escolhido = i; _mostrar()
			if e == null:
				_grelha.add_child(_casa("", 0, "", false, cb))
			else:
				_grelha.add_child(_casa(e.id, int(e.qtd), e.get("raridade", "comum"), i == _escolhido, cb))
	_detalhes()


func _casa(id: String, qtd: int, raridade: String, selecionada: bool, ao_clicar: Callable) -> Control:
	var b := TextureButton.new()
	var fundo := "casa_selecionada.png" if selecionada else ("casa_%s.png" % raridade if raridade != "" and raridade != "comum" else "casa.png")
	b.texture_normal = load(UI + fundo) if ResourceLoader.exists(UI + fundo) else load(UI + "casa.png")
	b.ignore_texture_size = true
	b.stretch_mode = TextureButton.STRETCH_SCALE
	b.custom_minimum_size = Vector2(52, 52)
	b.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	b.pressed.connect(ao_clicar)
	if id != "":
		var icone: String = Inventario._dados(id).get("icone", "")
		if icone != "" and ResourceLoader.exists(icone):
			var t := TextureRect.new()
			t.texture = load(icone)
			t.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
			t.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
			t.position = Vector2(10, 10)
			t.size = Vector2(32, 32)
			t.mouse_filter = Control.MOUSE_FILTER_IGNORE
			b.add_child(t)
		if qtd > 1:
			_texto(b, Vector2(30, 30), 12).text = str(qtd)
	return b


func _detalhes() -> void:
	for c in _botoes.get_children():
		c.queue_free()
	var inv: Inventario = Jogo.inventario
	var id := _missao_escolhida
	var e = null
	if _escolhido >= 0:
		e = inv.espacos[_escolhido]
		id = e.id if e else ""
	if id == "":
		var a: Dictionary = Dados.arma(Jogo.arma_equipada)
		var t := "Arma: %s +%d\nSegunda arma: %s\n" % [a.get("nome_pt", "—"), int(Jogo.arma_extra.get("melhoria", 0)),
			Dados.arma(Jogo.arma_2).get("nome_pt", "—") if Jogo.arma_2 != "" else "—"]
		for k in ["cabeca", "corpo", "maos", "pes", "capa"]:
			var p: Dictionary = Jogo.equipamento.get(k, {})
			t += "%s: %s\n" % [{"cabeca": "Cabeça", "corpo": "Corpo", "maos": "Mãos", "pes": "Pés", "capa": "Capa"}[k],
				("%s +%d" % [Inventario._dados(p.id).get("nome_pt", p.id), int(p.get("melhoria", 0))]) if not p.is_empty() else "—"]
		_info.text = t + "\nDEF %d · RES %d\n\nEscolhe um item para ver os detalhes." % [Jogo.defesa(), Jogo.resistencia()]
		for k in Jogo.equipamento.keys():
			_botoes.add_child(_botao("Tirar " + k, func(): Jogo.desequipar(k); _mostrar()))
		return
	var d := Inventario._dados(id)
	var linhas := [d.get("nome_pt", id)]
	if e and e.get("raridade", "comum") != "comum":
		linhas[0] += "  (%s)" % String(e.raridade).capitalize()
	if e and int(e.get("melhoria", 0)) > 0:
		linhas[0] += "  +%d" % e.melhoria
	if e and e.get("qualidade", "normal") != "normal":
		linhas[0] += "  [%s]" % String(e.qualidade).capitalize()
	if d.has("def"):
		linhas.append("DEF %d   RES %d   (%s · conjunto %s)" % [d.def, d.res, d.get("espaco", ""), String(d.get("conjunto", "")).replace("_", " ")])
	linhas.append(d.get("descricao_pt", ""))
	if d.get("categoria", "") == "arma":
		var atual: Dictionary = Dados.arma(Jogo.arma_equipada)
		var dif := int(d.get("atq", 0)) - int(atual.get("atq", 0))
		linhas.append("Tipo: %s   ATQ %d (%s%d)   Velocidade %.1f   Crítico %d%%" % [
			d.get("tipo", ""), d.get("atq", 0), "+" if dif >= 0 else "", dif, float(d.get("velocidade", 1)), int(float(d.get("critico", 0)) * 100)])
	if d.has("preco_venda"):
		linhas.append("Vende por %s ouro" % d.preco_venda)
	_info.text = "\n\n".join(linhas.filter(func(l): return str(l) != ""))
	if e == null:
		return
	var cat: String = d.get("categoria", "")
	if cat == "arma":
		_botoes.add_child(_botao("Equipar", func(): Jogo.equipar_do_espaco(_escolhido); _escolhido = -1))
		_botoes.add_child(_botao("Como 2.ª arma", func(): Jogo.equipar_do_espaco(_escolhido, true); _escolhido = -1))
	if cat == "armadura" and d.has("espaco"):
		_botoes.add_child(_botao("Vestir", func(): Jogo.equipar_do_espaco(_escolhido); _escolhido = -1))
	if not d.get("efeito", {}).is_empty():
		_botoes.add_child(_botao("Usar", func(): Jogo.usar_consumivel(id)))
		var na_barra := id in inv.barra_rapida
		_botoes.add_child(_botao("Tirar da barra" if na_barra else "Pôr na barra", func(): _barra(id)))
	_botoes.add_child(_botao("Deitar fora", func(): inv.retirar_espaco(_escolhido); _escolhido = -1))


func _barra(id: String) -> void:
	var b: Array = Jogo.inventario.barra_rapida
	var i := b.find(id)
	if i >= 0:
		b[i] = ""
	else:
		var livre := b.find("")
		if livre < 0:
			Sistema.mensagem("A barra rápida está cheia.", "aviso")
			return
		b[livre] = id
	Jogo.inventario.mudou.emit()
