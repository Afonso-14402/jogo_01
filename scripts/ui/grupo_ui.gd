extends JanelaUI
## Janela Grupo (tecla G; docs/INTERFACE.md, secção 4): os companheiros que tens, quem vai na equipa (até 3),
## dar arma, armadura e poções, ensinar uma skill e dar ordens. Também abre noutros modos: "contratar" (a Lyra, na
## Guilda), "boatos" (os escondidos) e o cartão de um escondido quando o encontras ("recrutar").

const NOMES_ESPACOS := {"cabeca": "Cabeça", "corpo": "Corpo", "maos": "Mãos", "pes": "Pés"}

var _modo: String = "grupo"
var _sel: String = ""
var _recrutar: String = ""
var _modo_fixo: bool = false
var _esq: VBoxContainer
var _dir: VBoxContainer
var _titulo: Label


func _ready() -> void:
	acao = "grupo"
	add_to_group("janelas")
	add_to_group("grupo_ui")
	_criar_janela(Vector2(140, 60), Vector2(1000, 600))
	_titulo = _texto(_janela, Vector2(20, 12), 18, Color("8fd3ff"))
	var se := ScrollContainer.new()
	se.position = Vector2(16, 48)
	se.size = Vector2(300, 536)
	se.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED
	_janela.add_child(se)
	_esq = VBoxContainer.new()
	_esq.custom_minimum_size = Vector2(286, 0)
	_esq.add_theme_constant_override("separation", 6)
	se.add_child(_esq)
	var sd := ScrollContainer.new()
	sd.position = Vector2(332, 48)
	sd.size = Vector2(652, 536)
	sd.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED
	_janela.add_child(sd)
	_dir = VBoxContainer.new()
	_dir.custom_minimum_size = Vector2(636, 0)
	_dir.add_theme_constant_override("separation", 8)
	sd.add_child(_dir)


## Aberta pela tecla G ou pela pausa: sempre no modo Grupo. Os outros modos vêm de abrir_modo / abrir_recrutar.
func abrir(sim: bool) -> void:
	if sim and not _modo_fixo:
		_modo = "grupo"
	_modo_fixo = false
	super(sim)


func abrir_modo(modo: String) -> void:
	_modo = modo
	_sel = ""
	_modo_fixo = true
	abrir(true)


func abrir_recrutar(id: String) -> void:
	_modo = "recrutar"
	_recrutar = id
	_modo_fixo = true
	abrir(true)


func _mostrar() -> void:
	_limpar(_esq)
	_limpar(_dir)
	match _modo:
		"contratar":
			_mostrar_contratar()
		"boatos":
			_mostrar_boatos()
		"recrutar":
			_mostrar_recrutar()
		_:
			_mostrar_grupo()


func _refazer() -> void:
	_mostrar()


# ------------------------------------------------------------------ peças da janela ------------------------------------------------------------------

func _linha(pai: Node) -> HBoxContainer:
	var h := HBoxContainer.new()
	h.add_theme_constant_override("separation", 8)
	h.alignment = BoxContainer.ALIGNMENT_BEGIN
	h.child_entered_tree.connect(func(n): if n is Control: n.size_flags_vertical = Control.SIZE_SHRINK_CENTER)
	pai.add_child(h)
	return h


func _rotulo(pai: Node, texto: String, cor := Color.WHITE, tam: int = 14, largura: float = 0.0) -> Label:
	var l := Label.new()
	l.text = texto
	l.add_theme_font_size_override("font_size", tam)
	l.add_theme_color_override("font_color", cor)
	l.add_theme_color_override("font_outline_color", Color("2e222f"))
	l.add_theme_constant_override("outline_size", 4)
	if largura > 0.0:
		l.custom_minimum_size = Vector2(largura, 0)
		l.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	pai.add_child(l)
	return l


func _retrato(id: String, tam: float) -> TextureRect:
	var d := Grupo.dados(id)
	return _icone(String(d.get("retrato", "res://arte/retratos/" + id + "_")) + "normal.png", tam)


const ESTADOS_TXT := {"preso": "prende", "atordoado": "atordoa", "queimadura": "queima", "sangrar": "faz sangrar",
	"lentidao": "abranda", "parado": "para o tempo"}


func _descricao_skill(s: Dictionary) -> String:
	var t := _descricao_base(s)
	var efeitos := []
	for e in s.get("estados", []):
		efeitos.append(ESTADOS_TXT.get(e.estado, e.estado))
	return t + (", " + ", ".join(efeitos) if not efeitos.is_empty() else "")


func _descricao_base(s: Dictionary) -> String:
	var m := String.num(float(s.get("mult", 1.0)), 2).trim_suffix("0").trim_suffix("0").trim_suffix(".").replace(".", ",")
	var el := (" de " + String(s.elemento)) if s.get("elemento") else ""
	match String(s.get("forma", "golpe")):
		"multi": return "%d golpes ×%s%s" % [int(s.get("golpes", 2)), m, el]
		"area": return "área de %s m ×%s%s" % [String.num(float(s.get("dist", 3.0)), 1).replace(".", ","), m, el]
		"area_alvo": return "%d× área no alvo ×%s%s" % [int(s.get("golpes", 1)), m, el]
		"linha": return "em linha ×%s%s" % [m, el]
		"investida": return "corre %d m e acerta ×%s" % [int(s.get("dist", 4)), m]
		"projetil":
			var n := int(s.get("golpes", 1))
			return ("%d disparos ×%s%s" % [n, m, el]) if n > 1 else ("disparo ×%s%s" % [m, el])
		"provocar": return "os monstros a %d m vão a ele (%d s) e +%d%% DEF" % [int(s.get("dist", 6)), int(s.get("dura", 5)), int(100 * float(s.get("buff", {}).get("valor", 0.3)))]
		"cura_grupo": return "cura %d%% do HP a ti e ao grupo" % int(100 * float(s.get("cura", 0.25)))
		"cura": return "cura 30% do HP"
		"golpe_estado": return "golpe ×%s" % m
	return "golpe ×%s%s" % [m, el]


# ------------------------------------------------------------------ modo Grupo ------------------------------------------------------------------

func _mostrar_grupo() -> void:
	var cs := Grupo.conhecidos()
	_titulo.text = "Grupo — na equipa %d/%d · [T] muda as ordens" % [Jogo.companheiros.size(), int(Grupo.c("maximo", 3))]
	if cs.is_empty():
		_rotulo(_esq, "Ainda não tens companheiros.", Color("c7dcd0"), 14, 280)
		_rotulo(_dir, "Fala com a Lyra, na Guilda, para contratar aventureiros. Há também companheiros escondidos na torre, cada um com uma habilidade especial (a Lyra conta os boatos).", Color.WHITE, 14, 620)
		return
	if _sel == "" or not _sel in cs:
		_sel = Jogo.companheiros[0] if not Jogo.companheiros.is_empty() else cs[0]
	for id in cs:
		var d := Grupo.dados(id)
		var h := _linha(_esq)
		h.add_child(_retrato(id, 40))
		var b := _botao(("★ " if Grupo.na_equipa(id) else "") + String(d.get("nome_pt", id)), func():
			_sel = id
			_refazer(), h)
		b.custom_minimum_size = Vector2(230, 36)
		if id == _sel:
			b.add_theme_color_override("font_color", Color("f9c22b"))
	var achados := 0
	var total := 0
	for d in Grupo.todos():
		if d.get("origem", "") == "escondido":
			total += 1
			achados += 1 if Grupo.conhecido(d.id) else 0
	_rotulo(_esq, "Escondidos encontrados: %d/%d" % [achados, total], Color("8fd3ff"))
	_cartao(_sel)


func _cartao(id: String) -> void:
	var d := Grupo.dados(id)
	var e := Grupo.estado(id)
	var topo := _linha(_dir)
	topo.add_child(_retrato(id, 96))
	var info := VBoxContainer.new()
	topo.add_child(info)
	_rotulo(info, String(d.get("nome_pt", id)), Color("f9c22b"), 18)
	var orig: String = {"guilda": "aventureiro da Guilda", "historia": "companheiro", "escondido": "escondido"}.get(d.get("origem", ""), "")
	_rotulo(info, "%s · %s · Nível %d" % [d.get("estilo_pt", ""), orig, Grupo.nivel(id)], Color("c7dcd0"))
	var dr := Grupo.defesa(id)
	_rotulo(info, "HP %d · ATQ %d · DEF %d · RES %d · ❤ %d" % [int(Grupo.hp_max(id)), int(Grupo.atq(id)), int(dr[0]), int(dr[1]), Amizade.coracoes(id)])
	var s: Dictionary = d.get("skill", {})
	_rotulo(_dir, "Skill: %s — %s (de 15 em 15 s)" % [s.get("nome_pt", ""), _descricao_skill(s)], Color("8fd3ff"), 14, 620)
	var es: Dictionary = d.get("especial", {})
	if not es.is_empty():
		_rotulo(_dir, "Habilidade especial: %s — %s" % [es.nome_pt, es.texto_pt], Color("f79617"), 14, 620)
	# equipa
	var l := _linha(_dir)
	if Grupo.na_equipa(id):
		_botao("Sair da equipa", func():
			Grupo.sair(id)
			_refazer(), l)
	else:
		var b := _botao("Entrar na equipa", func():
			if not Grupo.juntar(id):
				Sistema.mensagem("A equipa está cheia (até %d)." % int(Grupo.c("maximo", 3)), "aviso")
			_refazer(), l)
		b.disabled = Jogo.companheiros.size() >= int(Grupo.c("maximo", 3))
	# ordens
	var o := _linha(_dir)
	_rotulo(o, "Ordem:", Color("c7dcd0"))
	for k in Grupo.ORDENS:
		var b := _botao(Grupo.NOMES_ORDENS[k], func():
			Grupo.mudar_ordem(id, k)
			_refazer(), o)
		if Grupo.ordem(id) == k:
			b.add_theme_color_override("font_color", Color("f9c22b"))
	# arma
	var w := Grupo.arma(id)
	var la := _linha(_dir)
	_rotulo(la, "Arma: %s%s" % [w.get("nome_pt", "?"), "" if not e.arma.is_empty() else " (dele, gasta)"], Color.WHITE, 14, 330)
	_botao("Dar arma", func(): _escolher_item(id, "arma"), la)
	if not e.arma.is_empty():
		_botao("Tirar", func():
			Grupo.tirar_arma(id)
			_refazer(), la)
	_rotulo(_dir, "Sabe usar: " + ", ".join(Array(d.get("armas", [])).map(func(t): return String(t).replace("_", " "))), Color("9babb2"))
	# armadura
	for esp in Grupo.ESPACOS:
		var p: Dictionary = e.pecas.get(esp, {})
		var lp := _linha(_dir)
		var nome: String = Inventario._dados(String(p.get("id", ""))).get("nome_pt", "") if not p.is_empty() else "— (armadura leve dele)"
		_rotulo(lp, "%s: %s" % [NOMES_ESPACOS[esp], nome], Color.WHITE, 14, 330)
		_botao("Dar", func(): _escolher_item(id, esp), lp)
		if not p.is_empty():
			_botao("Tirar", func():
				Grupo.tirar_peca(id, esp)
				_refazer(), lp)
	# poções
	var lpo := _linha(_dir)
	_rotulo(lpo, "Poções: %d/%d (bebe abaixo de %d%% de HP)" % [e.pocoes.size(), int(Grupo.c("pocoes_max", 5)), int(100 * float(Grupo.c("pocao_hp", 0.35)))], Color.WHITE, 14, 330)
	var bp := _botao("Dar poção", func():
		if not Grupo.dar_pocao(id):
			Sistema.mensagem("Não tens poções de vida (ou já leva %d)." % int(Grupo.c("pocoes_max", 5)), "aviso")
		_refazer(), lpo)
	bp.disabled = Grupo.pocoes_na_mochila().is_empty()
	if not e.pocoes.is_empty():
		_botao("Tirar", func():
			Grupo.tirar_pocoes(id)
			_refazer(), lpo)
	# skill ensinada
	var ens := String(e.ensinada)
	var le := _linha(_dir)
	_rotulo(le, "Skill ensinada: %s" % (Jogo.skill(ens).get("nome_pt", ens) if ens != "" else "nenhuma"), Color.WHITE, 14, 330)
	var podes := Grupo.skills_para_ensinar(id)
	var be := _botao("Ensinar", func(): _escolher_item(id, "skill"), le)
	be.disabled = podes.is_empty()
	if podes.is_empty():
		_rotulo(_dir, "Para ensinar, aprende primeiro uma skill com uma arma que ele saiba usar.", Color("9babb2"), 14, 620)


## Lista para escolher o que dar (arma, peça de um espaço) ou que skill ensinar.
func _escolher_item(id: String, o_que: String) -> void:
	_limpar(_dir)
	var d := Grupo.dados(id)
	_rotulo(_dir, "%s — escolhe:" % d.get("nome_pt", id), Color("f9c22b"), 18)
	var algum := false
	if o_que == "skill":
		for s in Grupo.skills_para_ensinar(id):
			algum = true
			_botao("%s — %s" % [s.nome_pt, s.get("efeito_pt", "")], func():
				Grupo.ensinar(id, s.id)
				_refazer(), _dir)
	else:
		for i in Jogo.inventario.espacos.size():
			var e = Jogo.inventario.espacos[i]
			if e == null:
				continue
			var it := Inventario._dados(e.id)
			var serve := false
			if o_que == "arma":
				serve = it.get("categoria", "") == "arma" and Grupo.pode_usar_arma(id, e.id)
			else:
				serve = it.get("categoria", "") == "armadura" and it.get("espaco", "") == o_que
			if not serve:
				continue
			algum = true
			var extra := (" +%d" % int(e.melhoria)) if int(e.get("melhoria", 0)) > 0 else ""
			var valor := ("ATQ %d" % int(it.get("atq", it.get("atq_magico", 0)))) if o_que == "arma" else ("DEF %d · RES %d" % [int(it.get("def", 0)), int(it.get("res", 0))])
			_botao("%s%s (%s)" % [it.get("nome_pt", e.id), extra, valor], func():
				if o_que == "arma":
					Grupo.dar_arma(id, i)
				else:
					Grupo.dar_peca(id, i)
				_refazer(), _dir)
	if not algum:
		_rotulo(_dir, "Não tens nada que sirva na mochila.", Color("c7dcd0"))
	_botao("Voltar", _refazer, _dir)


# ------------------------------------------------------------------ modo Contratar (Lyra) ------------------------------------------------------------------

func _mostrar_contratar() -> void:
	_titulo.text = "Aventureiros à procura de grupo — tens %d de ouro" % Jogo.ouro
	_rotulo(_esq, "\"Estes aventureiros procuram grupo. Pagas uma vez à Guilda e ficam contigo.\" — Lyra", Color("c7dcd0"), 14, 280)
	for d in Grupo.todos():
		if d.get("origem", "") != "guilda":
			continue
		var h := _linha(_dir)
		h.add_child(_retrato(d.id, 56))
		var v := VBoxContainer.new()
		h.add_child(v)
		_rotulo(v, "%s — %s" % [d.nome_pt, d.estilo_pt], Color("f9c22b"))
		_rotulo(v, "%s: %s" % [d.skill.nome_pt, _descricao_skill(d.skill)], Color("8fd3ff"), 14, 420)
		if Grupo.conhecido(d.id):
			_rotulo(h, "Já está contigo", Color("9cdb43"))
		elif not Grupo.disponivel(d.id):
			_rotulo(h, "Chega depois do andar %s" % String(d.condicao).split(">=")[-1].strip_edges(), Color("9babb2"))
		else:
			var b := _botao("Contratar (%d)" % int(d.preco), func():
				Grupo.recrutar(d.id)
				_refazer(), h)
			b.disabled = Jogo.ouro < int(d.preco)


# ------------------------------------------------------------------ modo Boatos ------------------------------------------------------------------

func _mostrar_boatos() -> void:
	_titulo.text = "Boatos — companheiros escondidos na torre"
	_rotulo(_esq, "\"Os aventureiros contam coisas... algumas até são verdade.\" — Lyra", Color("c7dcd0"), 14, 280)
	for d in Grupo.todos():
		if d.get("origem", "") != "escondido":
			continue
		var h := _linha(_dir)
		if Grupo.conhecido(d.id):
			h.add_child(_retrato(d.id, 48))
			_rotulo(h, "%s — %s: %s" % [d.nome_pt, d.especial.nome_pt, d.especial.texto_pt], Color("9cdb43"), 14, 560)
		elif int(d.andar) <= Jogo.andar_maximo + 10:
			_rotulo(h, "??? — " + String(d.pista_pt), Color.WHITE, 14, 620)
		else:
			_rotulo(h, "??? — ainda ninguém fala disso (andar %d+)." % (int(d.andar) / 10 * 10), Color("9babb2"), 14, 620)


# ------------------------------------------------------------------ modo Recrutar (um escondido) ------------------------------------------------------------------

func _mostrar_recrutar() -> void:
	var d := Grupo.dados(_recrutar)
	_titulo.text = String(d.get("nome_pt", ""))
	_esq.add_child(_retrato(_recrutar, 160))
	_rotulo(_dir, "\"%s\"" % d.get("fala_pt", ""), Color.WHITE, 16, 620)
	_rotulo(_dir, "%s · %s: %s" % [d.estilo_pt, d.skill.nome_pt, _descricao_skill(d.skill)], Color("8fd3ff"), 14, 620)
	_rotulo(_dir, "Habilidade especial: %s — %s" % [d.especial.nome_pt, d.especial.texto_pt], Color("f79617"), 14, 620)
	var pede := []
	var cond := String(d.get("condicao", ""))
	if cond != "":
		pede.append("nível %s" % cond.split(">=")[-1].strip_edges())
	if int(d.get("preco", 0)) > 0:
		pede.append("%d de ouro" % int(d.preco))
	if not pede.is_empty():
		_rotulo(_dir, "Pede: " + " e ".join(pede), Color("c7dcd0"))
	var l := _linha(_dir)
	var b := _botao("Vem comigo!", func():
		if Grupo.recrutar(_recrutar):
			abrir(false)
		else:
			_refazer(), l)
	b.disabled = not Grupo.disponivel(_recrutar) or Jogo.ouro < int(d.get("preco", 0))
	_botao("Agora não", func(): abrir(false), l)
	if not Grupo.disponivel(_recrutar):
		_rotulo(_dir, "Volta quando estiveres pronto.", Color("e83b3b"))
