extends GutTest
## Condições dos diálogos, amizade e presentes (docs/dialogos/README.md; docs/SISTEMAS.md, secção 15).


func before_each() -> void:
	Jogo.novo_jogo("Teste")
	Jogo.amizade.clear()
	Tempo.hora = 9.0
	Tempo.dia = 1
	Tempo.estacao = 0
	Tempo.ano = 1


func test_condicoes_simples() -> void:
	assert_true(Condicoes.avaliar(""))
	assert_true(Condicoes.avaliar("—"))
	assert_true(Condicoes.avaliar("hora entre 8 e 10"))
	assert_false(Condicoes.avaliar("hora entre 12 e 14"))
	assert_true(Condicoes.avaliar("estacao == primavera"))
	assert_true(Condicoes.avaliar("dia_semana == segunda"))
	assert_true(Condicoes.avaliar("andar_maximo < 5"))
	assert_false(Condicoes.avaliar("andar_maximo >= 11"))


func test_condicoes_compostas() -> void:
	assert_true(Condicoes.avaliar("estacao == primavera && hora entre 8 e 12"))
	assert_false(Condicoes.avaliar("estacao == verao && hora entre 8 e 12"))
	assert_true(Condicoes.avaliar("estacao == verao || nivel >= 1"))
	assert_true(Condicoes.avaliar("!flag(kai_salvo)"))
	Jogo.por_flag("kai_salvo")
	assert_false(Condicoes.avaliar("!flag(kai_salvo)"))


func test_condicoes_coracoes_e_rank() -> void:
	assert_false(Condicoes.avaliar("coracoes(lyra) >= 2"))
	Amizade.mudar("lyra", 250)
	assert_true(Condicoes.avaliar("coracoes(lyra) >= 2"))
	assert_true(Condicoes.avaliar("rank >= F"))
	assert_false(Condicoes.avaliar("rank >= C"))
	Jogo.pontos_guilda = 1500
	assert_true(Condicoes.avaliar("rank >= C"))


func test_condicao_desconhecida_e_falsa() -> void:
	assert_false(Condicoes.avaliar("arma equipada pela 1.ª vez com raridade Épica"))


func test_falar_da_20_uma_vez_por_dia() -> void:
	assert_true(Amizade.falar("lyra"))
	assert_false(Amizade.falar("lyra"))
	assert_eq(Amizade.pontos("lyra"), 20)
	Tempo.dia = 2
	assert_true(Amizade.falar("lyra"))
	assert_eq(Amizade.pontos("lyra"), 40)


func test_presentes() -> void:
	Jogo.inventario.adicionar("flor_de_mel", 5)
	Jogo.inventario.adicionar("gel_slime", 5)
	assert_eq(Amizade.reacao("lyra", "flor_de_mel"), "adora")
	assert_eq(Amizade.reacao("lyra", "gel_slime"), "detesta")
	assert_eq(Amizade.dar("lyra", "flor_de_mel"), "adora")
	assert_eq(Amizade.pontos("lyra"), 80)
	assert_ne(Amizade.pode_dar("lyra"), "", "1 por dia")
	Tempo.dia = 2
	assert_eq(Amizade.dar("lyra", "gel_slime"), "detesta")
	assert_eq(Amizade.pontos("lyra"), 40)
	Tempo.dia = 3
	assert_ne(Amizade.pode_dar("lyra"), "", "2 por semana")


func test_aniversario_vale_8x() -> void:
	Tempo.dia = 5   # Lyra: Primavera, dia 5
	Jogo.inventario.adicionar("flor_de_mel", 1)
	assert_true(Amizade.e_aniversario("lyra"))
	Amizade.dar("lyra", "flor_de_mel")
	assert_eq(Amizade.pontos("lyra"), 640)


func test_dados_dos_dialogos() -> void:
	var lyra: Dictionary = Dados.tabela("dialogos/lyra")
	assert_false(lyra.is_empty())
	assert_gt(lyra.dia.size(), 30)
	assert_eq(lyra.cenas.size(), 5)
	var cena: Dictionary = lyra.cenas[0]
	var tem_escolhas: bool = cena.falas.any(func(f): return f.has("escolhas") and f.escolhas.size() == 3)
	assert_true(tem_escolhas, "as 3 escolhas da cena de 2 corações")


func test_escolher_fala_respeita_condicao() -> void:
	var n := NPC.new().configurar("lyra")
	n.dados = Dados.obter("npcs", "lyra")
	var lista := [{"id": "a", "cond": "hora entre 20 e 23", "texto": "noite"}, {"id": "b", "cond": "", "texto": "sempre"}]
	var rng := RandomNumberGenerator.new()
	for i in 20:
		rng.seed = i
		assert_eq(n.escolher_fala(lista, rng).id, "b")
	n.free()
