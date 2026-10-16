extends GutTest
## Missões: aceitar, contar, entregar, rank e o quadro da Guilda (docs/MISSOES.md; docs/SISTEMAS.md, secção 16).


func before_each() -> void:
	Jogo.novo_jogo("Teste")
	Tempo.dia = 1
	Tempo.estacao = 0
	Tempo.ano = 1


func test_matar_slimes() -> void:
	assert_true(Missoes.aceitar("G_F_01"))
	assert_eq(Missoes.estado("G_F_01"), "ativa")
	for i in 9:
		Eventos.monstro_morto.emit("slime_verde", 1)
	assert_eq(Missoes.progresso("G_F_01", 0), [9, 10])
	Eventos.monstro_morto.emit("lobo_cinzento", 1)
	assert_eq(Missoes.estado("G_F_01"), "ativa")
	Eventos.monstro_morto.emit("slime_verde", 1)
	assert_eq(Missoes.estado("G_F_01"), "pronta")
	var ouro := Jogo.ouro
	assert_true(Missoes.entregar("G_F_01"))
	assert_eq(Missoes.estado("G_F_01"), "concluida")
	assert_eq(Jogo.ouro, ouro + 50)
	assert_eq(Jogo.pontos_guilda, 10)


func test_trazer_itens_conta_a_mochila() -> void:
	Missoes.aceitar("G_F_02")
	Jogo.apanhar("erva_verde", 6)
	assert_eq(Missoes.progresso("G_F_02", 0), [6, 10])
	Jogo.apanhar("erva_verde", 4)
	assert_eq(Missoes.estado("G_F_02"), "pronta")
	Missoes.entregar("G_F_02")
	assert_eq(Jogo.inventario.contar("erva_verde"), 0, "os itens vão para quem pediu")


func test_rank_impede_missoes_altas() -> void:
	assert_ne(Missoes.pode_aceitar("G_D_01"), "")
	Jogo.pontos_guilda = 450
	assert_eq(Missoes.pode_aceitar("G_D_01"), "")


func test_maximo_de_10() -> void:
	var n := 0
	for m in Dados.tabela("missoes").values():
		if m.tipo == "regiao" and n < 10:
			assert_true(Missoes.aceitar(m.id))
			n += 1
	var outra := ""
	for m in Dados.tabela("missoes").values():
		if m.tipo == "regiao" and Missoes.estado(m.id) == "inativa":
			outra = m.id
			break
	assert_ne(Missoes.pode_aceitar(outra), "")


func test_historia_ir_a_andar() -> void:
	Missoes.aceitar("H_04")
	Eventos.andar_entrou.emit(5)
	assert_true(Missoes.passo_feito("H_04", 0))
	assert_eq(Missoes.estado("H_04"), "ativa")
	Eventos.monstro_morto.emit("javali_rei", 7)
	assert_eq(Missoes.estado("H_04"), "concluida", "sem ninguém a quem entregar, acaba logo")


func test_quadro_gera_3_missoes() -> void:
	Jogo.andar_maximo = 3
	var r := RandomNumberGenerator.new()
	r.seed = 4
	Missoes.gerar_quadro(r)
	assert_eq(Jogo.quadro.size(), 3)
	for g in Jogo.quadro:
		assert_true(g.passos[0].tipo in ["matar", "apanhar"])
		assert_gt(int(g.recompensas.ouro), 0)
	assert_true(Missoes.aceitar(Jogo.quadro[0].id))
