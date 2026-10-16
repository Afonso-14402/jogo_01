extends JanelaUI
## Mapa (docs/INTERFACE.md, secções 2 e 4): o minimapa redondo no canto (células à volta do herói, só as que já
## visitaste, com a escada, baús, NPCs e o guardião) e, com M, o mapa do andar inteiro (% explorado) e o mapa da torre.

const CORES := {
	"TT": Color("165a4c"), "##": Color("3e3546"), "tt": Color("239063"), "▒▒": Color("1a3d36"), "..": Color("5ac54f"),
	"\"\"": Color("91db69"), "**": Color("f5a097"), "^^": Color("8fcf5f"), "::": Color("c7b08b"), "==": Color("966c6c"),
	"~~": Color("4d65b4"), ",,": Color("4d9be6"), "ww": Color("30e1b9"), "%%": Color("694f62"), "xx": Color("a884f3"),
	"mm": Color("1ebc73"), "  ": Color(0, 0, 0, 0), "CC": Color("b33831"), "SS": Color("f9c22b"), "EE": Color("fbff86"),
	">>": Color("ffffff"), "GG": Color("e83b3b"), "BB": Color("e83b3b"), "()": Color("7a4841"),
}
const RAIO_MINI := 7      # células à volta do herói no minimapa

var _mini: Control
var _grande: Control
var _aba := "andar"
var _texto_info: Label


func _ready() -> void:
	acao = "mapa"
	add_to_group("janelas")
	add_to_group("mapa_ui")
	# minimapa: sempre visível (fora da janela), recortado em círculo
	var raiz := CanvasLayer.new()
	raiz.layer = 2
	add_child(raiz)
	_mini = Control.new()
	_mini.position = Vector2(1120, 64)
	_mini.size = Vector2(144, 144)
	_mini.clip_contents = true
	_mini.mouse_filter = Control.MOUSE_FILTER_IGNORE
	_mini.draw.connect(func(): _desenhar(_mini, true))
	raiz.add_child(_mini)
	var moldura := TextureRect.new()
	moldura.texture = load(UI + "minimapa_moldura.png")
	moldura.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	moldura.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	moldura.position = _mini.position - Vector2(8, 8)
	moldura.size = _mini.size + Vector2(16, 16)
	moldura.mouse_filter = Control.MOUSE_FILTER_IGNORE
	raiz.add_child(moldura)
	# o mapa grande
	_criar_janela(Vector2(120, 30), Vector2(1040, 660))
	var abas := HBoxContainer.new()
	abas.position = Vector2(20, 12)
	_janela.add_child(abas)
	_botao("Este andar", func(): _aba = "andar"; _mostrar(), abas)
	_botao("A torre", func(): _aba = "torre"; _mostrar(), abas)
	_texto_info = _texto(_janela, Vector2(300, 14), 15, Color("8fd3ff"))
	_grande = Control.new()
	_grande.position = Vector2(20, 52)
	_grande.size = Vector2(1000, 590)
	_grande.clip_contents = true
	_grande.draw.connect(func(): if _aba == "andar": _desenhar(_grande, false) else: _desenhar_torre(_grande))
	_janela.add_child(_grande)


## O sítio onde estamos: um Andar ou a cidade (os dois têm codigo(), largura e a célula do herói).
func _mundo() -> Node:
	var c := get_tree().current_scene
	for n in get_tree().root.get_children():
		if n.has_method("codigo") and "largura" in n:
			c = n
		for f in n.get_children():
			if f.has_method("codigo") and "largura" in f:
				c = f
	return c if c and c.has_method("codigo") else null


func _process(_d: float) -> void:
	_mini.visible = _mundo() != null and not get_tree().paused
	_mini.queue_redraw()


func _mostrar() -> void:
	_grande.queue_redraw()
	var m := _mundo()
	if _aba == "andar" and m:
		var pct: float = m.percent_explorado() * 100.0 if m.has_method("percent_explorado") else 100.0
		var nome: String = "Ascendia" if Jogo.andar_atual <= 0 else "Andar %d — %s" % [Jogo.andar_atual, m.dados.get("nome_pt", "")]
		_texto_info.text = "%s   ·   %d%% explorado" % [nome, int(pct)]
	else:
		_texto_info.text = "A torre   ·   andar mais alto: %d" % Jogo.andar_maximo


func _desenhar(c: Control, mini: bool) -> void:
	var m := _mundo()
	if m == null:
		return
	var larg: int = m.largura
	var alt: int = m.altura_cel if "altura_cel" in m else m.altura
	var j := get_tree().get_first_node_in_group("jogador")
	var cel_j := Vector2i(-99, -99)
	if j:
		cel_j = m.celula_de(j.global_position) if m.has_method("celula_de") else Vector2i.ZERO
	var vistas: Dictionary = Jogo.explorado.get(str(Jogo.andar_atual), {})
	var na_cidade := Jogo.andar_atual <= 0
	var tam: float
	var origem: Vector2
	var x0 := 0
	var y0 := 0
	var x1 := larg
	var y1 := alt
	if mini:
		tam = c.size.x / (RAIO_MINI * 2 + 1)
		x0 = cel_j.x - RAIO_MINI
		y0 = cel_j.y - RAIO_MINI
		x1 = cel_j.x + RAIO_MINI + 1
		y1 = cel_j.y + RAIO_MINI + 1
		origem = Vector2(-x0, -y0) * tam
		c.draw_circle(c.size / 2.0, c.size.x / 2.0, Color("2e222f"))
	else:
		tam = floorf(minf(c.size.x / larg, c.size.y / alt))
		origem = (c.size - Vector2(larg, alt) * tam) / 2.0
	for y in range(y0, y1):
		for x in range(x0, x1):
			if x < 0 or y < 0 or x >= larg or y >= alt:
				continue
			if mini and Vector2(x - cel_j.x, y - cel_j.y).length() > RAIO_MINI + 0.3:
				continue   # o minimapa é redondo
			var cod: String = m.codigo(x, y)
			var cor: Color = CORES.get(cod, Color("7f708a") if na_cidade else Color("5ac54f"))
			var visto := na_cidade or vistas.has("%d,%d" % [x, y]) or _perto_visto(vistas, x, y)
			if not visto:
				cor = cor.darkened(0.82)
			var r := Rect2(origem + Vector2(x, y) * tam, Vector2(tam, tam))
			c.draw_rect(r, cor)
	# marcas: escada, Zona Segura, guardião, NPCs, baús
	var marca := func(p: Vector3, icone: String):
		var cc: Vector2i = m.celula_de(p) if m.has_method("celula_de") else Vector2i.ZERO
		if not na_cidade and not vistas.has("%d,%d" % [cc.x, cc.y]) and not _perto_visto(vistas, cc.x, cc.y):
			return
		var pos := origem + (Vector2(cc) + Vector2(0.5, 0.5)) * tam - Vector2(6, 6)
		c.draw_texture_rect(load(UI + icone), Rect2(pos, Vector2(12, 12)), false)
	if "escada" in m and m.escada:
		marca.call(m.escada.global_position, "mapa_saida.png")
	if "guardiao" in m and m.guardiao and is_instance_valid(m.guardiao) and m.guardiao.estado != "morto":
		marca.call(m.guardiao.global_position, "mapa_boss.png")
	for n in get_tree().get_nodes_in_group("npcs"):
		if n.visible:
			marca.call(n.global_position, "mapa_npc.png")
	for b in m.get_children():
		if b is Bau and not b.aberto:
			marca.call(b.global_position, "mapa_bau.png")
	if j:
		var pj := origem + (Vector2(cel_j) + Vector2(0.5, 0.5)) * tam
		if m.has_method("centro_celula"):   # posição fina dentro da célula
			var cen: Vector3 = m.centro_celula(cel_j.x, cel_j.y)
			pj += Vector2(j.global_position.x - cen.x, j.global_position.z - cen.z) / 10.0 * tam
		c.draw_texture_rect(load(UI + "mapa_jogador.png"), Rect2(pj - Vector2(7, 7), Vector2(14, 14)), false)


## Uma célula conta como vista se uma vizinha foi visitada (vês um bocadinho à volta).
func _perto_visto(vistas: Dictionary, x: int, y: int) -> bool:
	for dy in range(-1, 2):
		for dx in range(-1, 2):
			if vistas.has("%d,%d" % [x + dx, y + dy]):
				return true
	return false


## O mapa da torre: 100 andares numa coluna (10 por região), os vencidos, onde estás.
func _desenhar_torre(c: Control) -> void:
	var cores := ["5ac54f", "7f708a", "1ebc73", "f9c22b", "c7dcd0", "4d9be6", "ea4f36", "6b3e75", "8fd3ff", "3e3546"]
	var fonte := ThemeDB.fallback_font
	for i in 100:
		var andar := i + 1
		var col := i / 10
		var lin := 9 - i % 10
		var r := Rect2(Vector2(40 + col * 96, 30 + lin * 52), Vector2(84, 44))
		var cor := Color(cores[col])
		if andar > Jogo.andar_maximo:
			cor = cor.darkened(0.75)
		c.draw_rect(r, cor)
		if andar == Jogo.andar_atual:
			c.draw_rect(r.grow(3), Color("fbff86"), false, 3.0)
		var txt := str(andar)
		if andar in Jogo.cristais:
			txt += " ◆"
		c.draw_string(fonte, r.position + Vector2(8, 28), txt, HORIZONTAL_ALIGNMENT_LEFT, -1, 16, Color("2e222f"))
	c.draw_string(fonte, Vector2(40, 575), "◆ = cristal ligado (podes voltar pelo Cristal Mestre)", HORIZONTAL_ALIGNMENT_LEFT, -1, 14, Color("c7dcd0"))
