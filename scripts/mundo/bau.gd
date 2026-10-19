class_name Bau
extends Node3D
## Baú (docs/SISTEMAS.md, secção 9.3): madeira, prata ou ouro (precisa de chave). 10% dos de madeira, a partir
## do andar 6, são Mímicos (um monstro Tanque de nível N+2 que deixa um baú de prata).

const CHAVE_OURO := "chave_bau_ouro"

var tipo: String = "madeira"
var andar: int = 1
var regiao: int = 1
var modelo: String = ""
var aberto: bool = false
var _visual: Node3D
var _inter: Interagivel


func _ready() -> void:
	if ResourceLoader.exists(modelo):
		_visual = load(modelo).instantiate()
		add_child(_visual)
		if tipo != "madeira":   # prata e ouro: mesmo modelo com outra cor
			_tingir(_visual, Color(0.85, 0.9, 1.25) if tipo == "prata" else Color(1.35, 1.1, 0.5))
	_inter = Interagivel.new()
	_inter.texto = "Abrir"
	add_child(_inter)
	_inter.usado.connect(_abrir)


func _tingir(no: Node, cor: Color) -> void:
	if no is MeshInstance3D and no.mesh:
		for i in no.mesh.get_surface_count():
			var m = no.mesh.surface_get_material(i)
			if m is StandardMaterial3D:
				var t: StandardMaterial3D = m.duplicate()
				t.albedo_color = cor
				no.set_surface_override_material(i, t)
	for f in no.get_children():
		_tingir(f, cor)


func _abrir(_jogador: Node) -> void:
	if aberto:
		return
	if tipo == "ouro":
		if not Jogo.inventario.tem(CHAVE_OURO):
			Sistema.mensagem("Este baú precisa de uma Chave de Baú de Ouro.", "aviso")
			return
		Jogo.inventario.retirar(CHAVE_OURO)
		Colecoes.contar("baus_ouro")
	aberto = true
	_inter.ativo = false
	var rng := RandomNumberGenerator.new()
	rng.randomize()
	var c := Dados.constantes
	if tipo == "madeira" and andar >= int(c.mimico_andar_minimo) and rng.randf() < float(c.mimico_hipotese):
		_mimico()
		return
	var conteudo := Loot.bau(c, tipo, andar, regiao, Jogo.a("sor"), rng, Jogo.azar_baus)
	if tipo != "madeira":
		var epico := false
		for it in conteudo.itens:
			if it[2].get("raridade", "") in ["epico", "lendario", "mitico"]:
				epico = true
		Jogo.azar_baus = 0 if epico else Jogo.azar_baus + 1
	_espalhar(conteudo)
	if _visual:
		var t := create_tween()
		t.tween_property(_visual, "scale", Vector3(1.15, 0.85, 1.15), 0.08)
		t.tween_property(_visual, "scale", Vector3.ONE, 0.15)
	EfeitosCombate.animado(get_tree(), "brilho_item", global_position + Vector3(0, 1, 0))


func _espalhar(conteudo: Dictionary) -> void:
	for it in conteudo.itens:
		var i := ItemChao.criar(it[0], it[1], it[2])
		get_parent().add_child(i)
		i.global_position = global_position + Vector3(0, 0.6, 0)
	if conteudo.ouro > 0:
		var m := ItemChao.moedas(conteudo.ouro)
		get_parent().add_child(m)
		m.global_position = global_position + Vector3(0, 0.6, 0)


func _mimico() -> void:
	Sistema.mensagem("O baú tinha dentes! É um Mímico!", "aviso")
	var m := Monstro.new().configurar("mimico", andar + 2, "tanque")
	m.position = position
	get_parent().add_child(m)
	m.morreu.connect(func(mo: Monstro):
		var rng := RandomNumberGenerator.new()
		rng.randomize()
		var cont := Loot.bau(Dados.constantes, "prata", andar, regiao, Jogo.a("sor"), rng, Jogo.azar_baus)
		for it in cont.itens:
			var i := ItemChao.criar(it[0], it[1], it[2])
			mo.get_parent().add_child(i)
			i.global_position = mo.global_position + Vector3(0, 0.6, 0))
	queue_free()
