extends JanelaUI
## Janela de Status do Sistema (docs/INTERFACE.md, secção 4; docs/PROGRESSAO.md): nome, Origem, nível, XP, rank,
## classe, Skill Única, atributos com "+", valores derivados; skills de armas, de vida e a barra de skills (1–6).

const ATRIB := [["for", "FOR", "dano corpo a corpo, carga"], ["agi", "AGI", "velocidade, Estamina"],
	["des", "DES", "arco, besta, críticos"], ["int", "INT", "magia, MP"], ["vit", "VIT", "HP, DEF, RES"],
	["sor", "SOR", "drops raros, ouro, críticos"]]
const NOMES_ARMAS := {"espada": "Espada", "espada_grande": "Espada Grande", "adaga": "Adaga", "katana": "Katana",
	"machado": "Machado", "martelo": "Martelo", "lanca": "Lança", "foice": "Foice", "arco": "Arco", "besta": "Besta",
	"cajado": "Cajado", "manoplas": "Manoplas"}

var _esq: VBoxContainer
var _dir: VBoxContainer
var _separador := "armas"


func _ready() -> void:
	acao = "status"
	add_to_group("janelas")
	_criar_janela(Vector2(140, 50), Vector2(1000, 620))
	var t := _texto(_janela, Vector2(20, 10), 18, Color("8fd3ff"))
	t.text = "[ STATUS ]"
	_esq = VBoxContainer.new()
	_esq.position = Vector2(20, 44)
	_esq.custom_minimum_size = Vector2(420, 0)
	_janela.add_child(_esq)
	var abas := HBoxContainer.new()
	abas.position = Vector2(470, 12)
	_janela.add_child(abas)
	for a in [["armas", "Skills de armas"], ["ativas", "Barra de skills"], ["vida", "Skills de vida"]]:
		_botao(a[1], func(): _separador = a[0]; _mostrar(), abas)
	var rolar := ScrollContainer.new()
	rolar.position = Vector2(470, 48)
	rolar.size = Vector2(510, 556)
	_janela.add_child(rolar)
	_dir = VBoxContainer.new()
	_dir.custom_minimum_size = Vector2(490, 0)
	rolar.add_child(_dir)
	Eventos.stats_mudaram.connect(func(): if visible: _mostrar())


func _linha(pai: Node, texto: String, tam := 14, cor := Color.WHITE) -> Label:
	var l := Label.new()
	l.text = texto
	l.add_theme_font_size_override("font_size", tam)
	l.add_theme_color_override("font_color", cor)
	l.add_theme_color_override("font_outline_color", Color("2e222f"))
	l.add_theme_constant_override("outline_size", 4)
	if pai is VBoxContainer:   # só quebra linhas em colunas (numa fila ficava com largura zero)
		l.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
		l.custom_minimum_size.x = (pai as Control).custom_minimum_size.x
	l.size_flags_vertical = Control.SIZE_SHRINK_CENTER
	pai.add_child(l)
	return l


func _mostrar() -> void:
	_limpar(_esq)
	_limpar(_dir)
	var origem: Dictionary = Dados.obter("origens", Jogo.origem)
	var unica: Dictionary = Dados.obter("skills_unicas", Jogo.skill_unica)
	var classe: Dictionary = Dados.obter("classes", Jogo.classe)
	_linha(_esq, Jogo.nome, 20)
	if Jogo.titulo != "":
		_linha(_esq, "«%s»" % Dados.obter("titulos", Jogo.titulo).get("nome_pt", ""), 13, Color("fbff86"))
	_linha(_esq, "Origem: %s" % origem.get("nome_pt", "—"), 13, Color("c7dcd0"))
	_linha(_esq, "Nível %d   ·   Rank %s   ·   %s" % [Jogo.nivel, Jogo.rank(), classe.get("nome_pt", "Aventureiro")], 15)
	var xp := HBoxContainer.new()
	_esq.add_child(xp)
	_linha(xp, "XP ", 13)
	xp.add_child(_barra_progresso(Jogo.xp, Jogo.xp_para_subir(), 300, Color("f9c22b")))
	_linha(xp, " %d / %d" % [Jogo.xp, Jogo.xp_para_subir()], 12)
	_linha(_esq, "Skill Única: %s" % unica.get("nome_pt", "??? (o Cristal de Avaliação ainda não te viu)"), 13, Color("fbff86"))
	if not unica.is_empty():
		_linha(_esq, unica.efeito_pt, 11, Color("c7dcd0"))
	_linha(_esq, "", 6)
	_linha(_esq, "Pontos para distribuir: %d" % Jogo.pontos_livres, 14, Color("91db69") if Jogo.pontos_livres > 0 else Color("9babb2"))
	for a in ATRIB:
		var h := HBoxContainer.new()
		_esq.add_child(h)
		var nome := _linha(h, "%s  %d" % [a[1], Jogo.a(a[0])], 15)
		nome.custom_minimum_size = Vector2(90, 0)
		var b := _botao("+", func(): Jogo.gastar_ponto(a[0]); _mostrar(), h)
		b.disabled = Jogo.pontos_livres <= 0
		_linha(h, "  " + a[2], 11, Color("9babb2"))
	_linha(_esq, "", 6)
	var arma: Dictionary = Dados.arma(Jogo.arma_equipada)
	var j := get_tree().get_first_node_in_group("jogador")
	var atq := Formulas.atq_fisico(Dados.constantes, float(arma.get("atq", 0)), 0, 1.0, Jogo.a("for"), Jogo.a("des"), arma.get("distancia", false))
	_linha(_esq, "HP %d / %d     MP %d / %d     Estamina %d" % [Jogo.hp, Jogo.hp_maximo(), Jogo.mp, Jogo.mp_maximo(), Jogo.estamina_maxima()], 13)
	_linha(_esq, "ATQ %d (×%.2f com %s)     DEF %d     RES %d" % [atq, Jogo.mult_arma(arma.get("tipo", "espada")),
			NOMES_ARMAS.get(arma.get("tipo", ""), "—"), Jogo.defesa(), Jogo.resistencia()], 13)
	_linha(_esq, "Crítico %.1f%%     Velocidade %.1f m/s     Carga %.1f / %s kg" % [Jogo.critico(float(arma.get("critico", 0))) * 100.0,
			Jogo.velocidade(), Jogo.inventario.peso(), "∞" if Jogo.peso_maximo() == INF else str(int(Jogo.peso_maximo()))], 13)
	if j and not j.estados.ativos.is_empty():
		_linha(_esq, "Estados: " + ", ".join(j.estados.ativos.keys().map(func(k): return Estados.info(k).get("nome_pt", k))), 13, Color("e83b3b"))
	match _separador:
		"armas":
			_mostrar_armas()
		"ativas":
			_mostrar_ativas()
		"vida":
			_mostrar_vida()


func _mostrar_armas() -> void:
	_linha(_dir, "Cada golpe que acerta dá 1 ponto. +2% de dano por nível; ataques especiais nos níveis 3, 6 e 10.", 11, Color("9babb2"))
	for tipo in NOMES_ARMAS:
		var info := Progressao.nivel_arma(Dados.constantes, float(Jogo.skills_arma.get(tipo, 0)))
		var h := HBoxContainer.new()
		_dir.add_child(h)
		var l := _linha(h, "Manejo de %s" % NOMES_ARMAS[tipo], 13)
		l.custom_minimum_size = Vector2(190, 0)
		_linha(h, "Nv %d " % info[0], 13, Color("fbff86"))
		h.add_child(_barra_progresso(info[1], info[2], 150, Color("4d9be6")))
		var esp := HBoxContainer.new()
		_dir.add_child(esp)
		for s in Dados.tabela("skills_armas").values():
			if s.arma == tipo:
				var ic := _icone(s.get("icone", ""), 24)
				ic.modulate = Color.WHITE if int(s.nivel) <= info[0] else Color(0.3, 0.3, 0.35)
				ic.tooltip_text = "%s (Nv %d): %s" % [s.nome_pt, s.nivel, s.efeito_pt]
				ic.mouse_filter = Control.MOUSE_FILTER_PASS
				esp.add_child(ic)


func _mostrar_ativas() -> void:
	_linha(_dir, "Barra (teclas 1–6):", 14, Color("8fd3ff"))
	var barra := HBoxContainer.new()
	_dir.add_child(barra)
	for i in 6:
		var id: String = Jogo.skills_barra[i]
		var s := Jogo.skill(id) if id != "" else {}
		var b := Button.new()
		b.custom_minimum_size = Vector2(70, 56)
		b.text = "%d\n%s" % [i + 1, String(s.get("nome_pt", "—")).left(9)]
		b.add_theme_font_size_override("font_size", 11)
		b.tooltip_text = "Clica para tirar da barra"
		b.pressed.connect(func(): Jogo.skills_barra[i] = ""; Eventos.stats_mudaram.emit())
		barra.add_child(b)
	_linha(_dir, "", 6)
	_linha(_dir, "Skills que já sabes:", 14, Color("8fd3ff"))
	var lista := Jogo.skills_ativas()
	if lista.is_empty():
		_linha(_dir, "Ainda nenhuma. Usa uma arma até ao nível 3 de Manejo, ou escolhe uma classe no nível 10.", 12, Color("9babb2"))
	for s in lista:
		var h := HBoxContainer.new()
		_dir.add_child(h)
		h.add_child(_icone(s.get("icone", ""), 28))
		var cu: Dictionary = s.get("custo", {})
		var custo := ("%d MP" % cu.mp) if cu.has("mp") else (("%d Est." % cu.estamina) if cu.has("estamina") else "")
		var l := _linha(h, "%s  (%s, %d s)\n%s" % [s.nome_pt, custo, s.get("recarga", 0), s.efeito_pt], 11)
		l.custom_minimum_size = Vector2(340, 0)
		if s.id in Jogo.skills_barra:
			_linha(h, "na barra", 11, Color("91db69"))
		else:
			_botao("Pôr na barra", func(): Jogo.por_na_barra(s.id), h)


func _mostrar_vida() -> void:
	_linha(_dir, "Sobem com o uso (nível 1 a 50). A cada 10 níveis ganhas uma vantagem.", 11, Color("9babb2"))
	for s in Dados.tabela("skills_vida").values():
		var info := Progressao.nivel_vida(Dados.constantes, float(Jogo.skills_vida.get(s.id, 0)))
		var h := HBoxContainer.new()
		_dir.add_child(h)
		h.add_child(_icone(s.get("icone", ""), 24))
		var l := _linha(h, s.nome_pt, 13)
		l.custom_minimum_size = Vector2(130, 0)
		_linha(h, "Nv %d " % info[0], 13, Color("fbff86"))
		h.add_child(_barra_progresso(info[1], info[2], 120, Color("91db69")))
		var prox := mini(4, int(info[0] / 10))
		_linha(_dir, "   Nv %d: %s" % [(prox + 1) * 10, s.vantagens_pt[prox]], 11, Color("9babb2"))
