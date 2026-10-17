extends GutTest
## Segredos e puzzles dos andares (scripts/mundo/segredos.gd), resolvidos a carregar nas coisas.

var andar: Node


func _abrir(n: int) -> void:
	Jogo.novo_jogo("Teste")
	Jogo.andar_atual = n
	andar = load("res://cenas/mundo/andar.tscn").instantiate()
	add_child_autofree(andar)


func _usar(texto: String) -> Array:
	var r := []
	for i in get_tree().get_nodes_in_group("interagivel"):
		if String(i.texto).begins_with(texto):
			r.append(i)
	return r


func test_moinho_abre_alcapao_com_bau() -> void:
	_abrir(1)
	var baus_antes := andar.get_children().filter(func(x): return x is Bau).size()
	_usar("Puxar a corda")[0].usado.emit(andar.jogador)
	assert_true(Jogo.tem_flag("seg_a001_moinho"))
	assert_eq(andar.get_children().filter(func(x): return x is Bau).size(), baus_antes + 1)


func test_comportas_pela_ordem_certa_baixam_a_agua() -> void:
	_abrir(3)
	assert_false(andar.paredes_agua.is_empty())
	var rodas := {}
	for i in _usar("Rodar a roda"):
		rodas[String(i.texto).right(1)] = i
	for n in ["1", "2"]:   # ordem errada: nada
		rodas[n].usado.emit(andar.jogador)
	assert_false(Jogo.tem_flag("seg_a003_comportas"))
	var seg: Segredos = andar.get_children().filter(func(x): return x is Segredos)[0]
	seg._ordem.clear()   # recomeçar (como quem se engana e tenta outra vez)
	for n in ["2", "3", "1"]:
		rodas[n].usado.emit(andar.jogador)
	assert_true(Jogo.tem_flag("seg_a003_comportas"))
	assert_true(andar.paredes_agua.is_empty())


func test_tres_sussurros() -> void:
	_abrir(2)
	var seg: Segredos = andar.get_children().filter(func(x): return x is Segredos)[0]
	var pedras := _usar("Tocar na pedra")
	assert_eq(pedras.size(), 3)
	# a ordem certa está guardada nas árvores; tentar todas as ordens até abrir
	var cores := ["azul", "vermelho", "amarelo"]
	for a in 3:
		for b in 3:
			for c in 3:
				if a == b or b == c or a == c or Jogo.tem_flag("seg_a002_sussurros"):
					continue
				seg._ordem.clear()
				for k in [a, b, c]:
					for p in pedras:
						if String(p.texto).ends_with(cores[k]):
							p.usado.emit(andar.jogador)
	assert_true(Jogo.tem_flag("seg_a002_sussurros"))


func _seg() -> Segredos:
	return andar.get_children().filter(func(x): return x is Segredos)[0]


func test_tabuas_do_carril_precisam_de_martelo_ou_machado() -> void:
	_abrir(11)
	var baus_antes := andar.get_children().filter(func(x): return x is Bau).size()
	var t: Interagivel = _usar("Tábuas pregadas")[0]
	t.usado.emit(andar.jogador)
	assert_false(Jogo.tem_flag("seg_a011_tabuas"))
	Jogo.inventario.adicionar("machado_lenhador_cobre")
	t.usado.emit(andar.jogador)
	assert_true(Jogo.tem_flag("seg_a011_tabuas"))
	assert_eq(andar.get_children().filter(func(x): return x is Bau).size(), baus_antes + 1)


func test_boias_pela_ordem_abrem_a_eclusa() -> void:
	_abrir(14)
	var boias := {}
	for i in _usar("Acender a boia"):
		boias[String(i.texto).right(1)] = i
	assert_eq(boias.size(), 3)
	for n in ["1", "2", "3"]:
		boias[n].usado.emit(andar.jogador)
	assert_true(Jogo.tem_flag("seg_a014_boias"))


func test_runas_brom_abrem_o_portao() -> void:
	_abrir(18)
	var aneis := _usar("Rodar o anel")
	assert_eq(aneis.size(), 4)
	# letras: A B M O R T U -> B=1, R=4, O=3, M=2
	for k in 4:
		for v in [1, 4, 3, 2][k]:
			aneis[k].usado.emit(andar.jogador)
	assert_true(Jogo.tem_flag("seg_a018_runas"))
	assert_true(Jogo.inventario.tem("livro_runas_anas"))


func test_fornalhas_com_carvao() -> void:
	_abrir(18)
	var f := _usar("Acender a fornalha")
	assert_eq(f.size(), 3)
	f[0].usado.emit(andar.jogador)
	assert_false(Jogo.tem_flag("seg_a018_forno_0"))
	Jogo.inventario.adicionar("carvao", 3)
	for x in f:
		x.usado.emit(andar.jogador)
	assert_true(Jogo.tem_flag("seg_a018_fornalhas"))


func test_resgatar_aventureiros_dos_casulos() -> void:
	_abrir(15)
	var ouro := Jogo.ouro
	var c := _usar("Cortar o casulo")
	assert_eq(c.size(), 3)
	for x in c:
		x.usado.emit(andar.jogador)
	assert_eq(Jogo.ouro, ouro + 450)
