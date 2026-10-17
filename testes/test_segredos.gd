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


func test_passadico_precisa_de_5_tabuas() -> void:
	_abrir(21)
	var ponte: Interagivel = _usar("Passadiço partido")[0]
	ponte.usado.emit(andar.jogador)
	assert_false(Jogo.tem_flag("seg_a021_passadico"))
	var cx := _usar("Partir o caixote")
	assert_eq(cx.size(), 5)
	for c in cx:
		c.usado.emit(andar.jogador)
	ponte.usado.emit(andar.jogador)
	assert_true(Jogo.tem_flag("seg_a021_passadico"))


func test_pedras_dos_animais_pela_ordem_do_mural() -> void:
	_abrir(23)
	var seg := _seg()
	var pedras := _usar("Carregar na pedra")
	assert_eq(pedras.size(), 4)
	# a ordem certa está no segredo; tentar todas as ordens até abrir (como quem vai experimentando)
	var feito := false
	for a in 4:
		for b in 4:
			for c in 4:
				for d in 4:
					if feito or len({a: 1, b: 1, c: 1, d: 1}) < 4:
						continue
					seg._ordem.clear()
					for k in [a, b, c, d]:
						pedras[k].usado.emit(andar.jogador)
					feito = Jogo.tem_flag("seg_a023_animais")
	assert_true(feito)
	_usar("Escadaria atrás")[0].usado.emit(andar.jogador)
	assert_true(Jogo.inventario.tem("idolo_jade"))


func test_alavanca_norte_baixa_a_agua_e_mostra_o_anel() -> void:
	_abrir(25)
	for a in _usar("Puxar a alavanca"):
		a.usado.emit(andar.jogador)
	assert_true(Jogo.tem_flag("seg_a025_agua_norte"))
	_usar("Porta escondida")[0].usado.emit(andar.jogador)
	assert_true(Jogo.inventario.tem("anel_serpente"))


func test_fonte_esmeralda_da_mais_hp() -> void:
	_abrir(27)
	var antes := Jogo.hp_maximo()
	Jogo.por_flag("seg_a027_simbolo")
	_usar("Entrar atrás da cascata")[0].usado.emit(andar.jogador)
	assert_gt(Jogo.hp_maximo(), antes)


func test_regar_as_flores_porta() -> void:
	_abrir(29)
	var flores := _usar("Regar a flor-porta")
	assert_eq(flores.size(), 3)
	for f in flores:
		_usar("Encher o regador")[0].usado.emit(andar.jogador)
		f.usado.emit(andar.jogador)
	assert_true(Jogo.tem_flag("seg_a029_flores"))


func test_camelos_perdidos() -> void:
	_abrir(31)
	Missoes.aceitar("R4_02")
	for c in _usar("Acalmar o camelo"):
		c.usado.emit(andar.jogador)
	assert_true(Missoes.estado("R4_02") in ["pronta", "concluida"])   # (o Caravaneiro Yusuf não está no jogo: acaba logo)


func test_portas_soterradas_com_pa_pela_ordem() -> void:
	_abrir(34)
	var portas := {}
	for p in _usar("Escavar a porta"):
		portas[String(p.texto).get_slice(" ", 3)] = p
	assert_eq(portas.size(), 5)
	portas["I"].usado.emit(andar.jogador)
	assert_true(_seg()._ordem.is_empty())   # sem pá não conta
	Jogo.inventario.adicionar("pa")
	for n in ["I", "II", "III", "IV", "V"]:
		portas[n].usado.emit(andar.jogador)
	assert_true(Jogo.tem_flag("seg_a034_portas"))
	_usar("Empurrar o trono")[0].usado.emit(andar.jogador)
	assert_true(Jogo.inventario.tem("coroa_cidade_enterrada"))


func test_baus_mimicos_e_o_verdadeiro() -> void:
	_abrir(39)
	var baus := _usar("Abrir o baú")
	assert_eq(baus.size(), 8)
	var falso: Interagivel = baus.filter(func(b): return "pó," not in String(b.texto) and "cheio" in String(b.texto))[0]
	var monstros := andar.get_children().filter(func(x): return x is Monstro).size()
	falso.usado.emit(andar.jogador)
	assert_eq(andar.get_children().filter(func(x): return x is Monstro).size(), monstros + 1)
	baus.filter(func(b): return "brilhar" in String(b.texto))[0].usado.emit(andar.jogador)
	assert_true(Jogo.tem_flag("seg_a039_verdadeiro"))


func test_quatro_fogueiras_derretem_a_porta_de_gelo() -> void:
	_abrir(41)
	var f := _usar("Acender a fogueira")
	assert_eq(f.size(), 4)
	f[0].usado.emit(andar.jogador)
	assert_false(Jogo.tem_flag("seg_a041_fogo_0"))   # sem fogo
	Jogo.inventario.adicionar("tocha")
	for x in f:
		x.usado.emit(andar.jogador)
	assert_true(Jogo.tem_flag("seg_a041_porta_gelo"))


func test_sino_a_meia_noite_da_o_diario() -> void:
	_abrir(46)
	Tempo.hora = 0.2
	var sino: Interagivel = _usar("Tocar o sino")[0]
	for k in 3:
		sino.usado.emit(andar.jogador)
	assert_true(Jogo.inventario.tem("diario_equipa_gorvan"))


func test_pedra_cantante_so_com_a_aurora_dela() -> void:
	_abrir(48)
	var seg := _seg()
	var cor: String = seg.aurora()
	for p in _usar("Tocar na Pedra Cantante"):
		p.usado.emit(andar.jogador)
	for c in Segredos.AURORA:
		assert_eq(Jogo.tem_flag("seg_a048_canta_" + c), c == cor)


func test_cinco_fantasmas_do_navio() -> void:
	_abrir(53)
	var f := _usar("Falar com o fantasma")
	assert_eq(f.size(), 5)
	for x in f:
		x.usado.emit(andar.jogador)
	assert_true(Jogo.tem_flag("seg_a053_fantasmas"))


func test_mares_do_templo_e_a_bencao() -> void:
	_abrir(59)
	var antes := Jogo.hp_maximo()
	var c := _usar("Rodar a concha-alavanca")
	assert_eq(c.size(), 4)
	# a 1.ª muda as salas 1 e 2, a 3.ª muda as 3 e 4: fica vazia-cheia-vazia-cheia
	c.filter(func(x): return String(x.texto).ends_with("1"))[0].usado.emit(andar.jogador)
	c.filter(func(x): return String(x.texto).ends_with("3"))[0].usado.emit(andar.jogador)
	assert_true(Jogo.tem_flag("seg_a059_mares"))
	Jogo.andar_atual = 59
	_usar("Concha falante")[0].usado.emit(andar.jogador)
	assert_gt(Jogo.hp_maximo(), antes)


func test_quatro_sinos_de_cinza() -> void:
	_abrir(61)
	var antes := andar.get_children().filter(func(x): return x is Bau).size()
	for s in _usar("Limpar e tocar o sino"):
		s.usado.emit(andar.jogador)
	assert_true(Jogo.tem_flag("seg_a061_sinos"))
	assert_eq(andar.get_children().filter(func(x): return x is Bau).size(), antes + 1)


func test_arvore_verde_precisa_da_fonte_esmeralda() -> void:
	_abrir(63)
	_usar("Raízes vivas")[0].usado.emit(andar.jogador)
	assert_false(Jogo.tem_flag("seg_a063_arvore"))
	Jogo.por_flag("seg_a027_fonte")
	var hp := Jogo.hp_maximo()
	_usar("Raízes vivas")[0].usado.emit(andar.jogador)
	for f in _usar("Comer um fruto"):
		f.usado.emit(andar.jogador)
	assert_gt(Jogo.hp_maximo(), hp)


func test_geiseres_em_cadeia_e_a_pena_de_fenix() -> void:
	_abrir(66)
	var g := _usar("Tapar/destapar o géiser")
	for k in g.size() - 1:
		g[k].usado.emit(andar.jogador)
	assert_true(Jogo.tem_flag("seg_a066_geiseres"))
	_usar("Ninho de fénix")[0].usado.emit(andar.jogador)
	assert_true(Jogo.inventario.tem("pena_fenix"))


func test_velas_pela_ordem_de_marcha() -> void:
	_abrir(74)
	var velas := {}
	for v in _usar("Acender a vela de"):
		velas[String(v.texto).get_slice("de ", 1)] = v
	assert_eq(velas.size(), 5)
	for n in ["Edrik", "Gorvan", "Odília", "Teodoro", "Ilsa"]:
		velas[n].usado.emit(andar.jogador)
	assert_true(Jogo.tem_flag("seg_a074_velas"))


func test_sepulturas_precisam_de_agua_benta() -> void:
	_abrir(73)
	var s := _usar("Consagrar a sepultura")
	assert_eq(s.size(), 10)
	s[0].usado.emit(andar.jogador)
	assert_false(Jogo.tem_flag("seg_a073_sepultura_0"))
	Jogo.inventario.adicionar("agua_benta", 10)
	for x in s:
		x.usado.emit(andar.jogador)
	assert_true(Jogo.tem_flag("seg_a073_sepulturas"))


func test_celas_com_a_chave_mestra() -> void:
	_abrir(78)
	for p in _usar("Apanhar a parte"):
		p.usado.emit(andar.jogador)
	assert_true(Jogo.inventario.tem("chave_mestra"))
	var ouro := Jogo.ouro
	_usar("Abrir a cela")[0].usado.emit(andar.jogador)
	assert_eq(Jogo.ouro, ouro + 120)
