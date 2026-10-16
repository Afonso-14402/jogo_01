class_name NoRecolha
extends Node3D
## Nó de recolha (docs/SISTEMAS.md, secção 12): minério (picareta), árvore (machado) ou erva/flor (à mão).
## Dá 1–3 itens (+1% de hipótese de item extra por nível da skill de vida), às vezes um item raro, e desaparece
## (volta ao sair e voltar ao andar). As ferramentas têm tier: uma Picareta de Cobre não parte minério de Prata.

const SKILL := {"picareta": "mineracao", "machado": "lenhador", "mao": "herbalismo"}
const TEXTO := {"picareta": "Partir", "machado": "Cortar", "mao": "Apanhar"}
const METAL := ["Cobre", "Ferro", "Aço", "Prata", "Gelo Eterno", "Coral Abissal", "Obsidiana", "Mitril", "Oricalco", "Estelar"]

var item: String = ""
var ferramenta: String = "mao"
var tier: int = 1
var modelo: String = ""
var raros: Array = []          # [item] que podem sair às vezes (ex.: Rubi pequeno no minério de cobre)
var _golpes: int = 0
var _visual: Node3D
var _corpo: StaticBody3D
var _inter: Interagivel


func _ready() -> void:
	add_to_group("recolha")
	if modelo != "" and ResourceLoader.exists(modelo):
		_visual = load(modelo).instantiate()
	else:   # erva/flor: o ícone do item de pé, a brilhar um pouco
		var s := Sprite3D.new()
		s.texture = load(Inventario._dados(item).get("icone", "res://arte/icones/erva_verde.png"))
		s.billboard = BaseMaterial3D.BILLBOARD_FIXED_Y
		s.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
		s.pixel_size = 0.045
		s.position.y = 0.36
		s.alpha_cut = SpriteBase3D.ALPHA_CUT_DISCARD
		_visual = s
	add_child(_visual)
	if ferramenta != "mao":
		_corpo = StaticBody3D.new()
		var f := CollisionShape3D.new()
		var c := CylinderShape3D.new()
		c.radius = 0.6 if ferramenta == "picareta" else 0.5
		c.height = 2.0
		f.shape = c
		f.position.y = 1.0
		_corpo.add_child(f)
		add_child(_corpo)
	_inter = Interagivel.new()
	_inter.texto = "%s (%s)" % [TEXTO[ferramenta], Inventario._dados(item).get("nome_pt", item)]
	add_child(_inter)
	if ferramenta != "mao":   # a área de interação um pouco maior que o corpo
		var f := CollisionShape3D.new()
		var s := SphereShape3D.new()
		s.radius = 1.3
		f.shape = s
		f.position.y = 0.6
		_inter.add_child(f)
	_inter.usado.connect(_usar)


func _usar(jogador: Node) -> void:
	if ferramenta != "mao":
		var t := Jogo.tier_ferramenta(ferramenta)
		var nome_f := "Picareta" if ferramenta == "picareta" else "Machado de Lenhador"
		if t == 0:
			Sistema.mensagem("Precisas de uma %s." % nome_f, "aviso")
			return
		if t < tier:
			Sistema.mensagem("É preciso uma %s de %s ou melhor." % [nome_f, METAL[clampi(tier, 1, 10) - 1]], "aviso")
			return
	if jogador.has_method("animar_acao"):
		jogador.animar_acao(global_position, ferramenta)
	var nivel := Jogo.nivel_vida(SKILL[ferramenta])
	var precisa := 1 if ferramenta == "mao" or nivel >= 30 else int(Dados.c("recolha_golpes", 3))
	_golpes += 1
	if _visual and ferramenta != "mao":
		var tw := create_tween()
		tw.tween_property(_visual, "position:x", 0.08, 0.05)
		tw.tween_property(_visual, "position:x", -0.08, 0.05)
		tw.tween_property(_visual, "position:x", 0.0, 0.05)
		EfeitosCombate.animado(get_tree(), "poeira", global_position + Vector3(0, 0.8, 0.4))
	if _golpes < precisa:
		return
	var rng := RandomNumberGenerator.new()
	rng.randomize()
	var lim: Array = Dados.c("recolha_qtd", [1, 3])
	var qtd := rng.randi_range(int(lim[0]), int(lim[1]))
	if rng.randf() < nivel * float(Dados.c("recolha_extra_por_nivel", 0.01)):
		qtd += 1
	Jogo.apanhar(item, qtd)
	for r in raros:
		if rng.randf() < 0.05:
			Jogo.apanhar(r, 1)
	Jogo.treinar_vida(SKILL[ferramenta], 1)
	_inter.ativo = false
	_inter.queue_free()
	if _corpo:
		_corpo.queue_free()
	var tw := create_tween()
	tw.tween_property(self, "scale", Vector3(1.2, 0.05, 1.2), 0.25)
	tw.tween_callback(queue_free)
