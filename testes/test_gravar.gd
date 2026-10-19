extends GutTest
## Gravar e carregar tudo (docs/SISTEMAS.md, secção 18) e a dificuldade (secção 19).


func test_gravar_e_carregar_tudo() -> void:
	Jogo.novo_jogo("Mira")
	Jogo.tratamento = "ela"
	Jogo.aparencia = {"penteado": "rabo", "pele": "morena", "cabelo": "azul", "olhos": "verde", "roupa": "aventureiro"}
	Jogo.origem = "jogador"
	Jogo.skill_unica = "mao_de_midas"
	Jogo.dificuldade = "dificil"
	Jogo.treinar_arma("espada", 300)
	Jogo.inventario.adicionar("espada_ferro", 1, {"raridade": "raro"})
	Jogo.arma_extra = {"id": "espada_cobre", "melhoria": 3}
	Missoes.aceitar("G_F_01")
	Amizade.mudar("lyra", 230)
	Jogo.cristais = [5]
	Jogo.andar_atual = 7
	Tempo.hora = 15.5
	Tempo.dia = 9
	assert_true(Gravar.gravar(8))
	Jogo.novo_jogo("Outro")
	Tempo.dia = 1
	assert_true(Gravar.carregar(8))
	assert_eq(Jogo.nome, "Mira")
	assert_eq(Jogo.tratamento, "ela")
	assert_eq(Jogo.aparencia.cabelo, "azul")
	assert_eq(Jogo.origem, "jogador")
	assert_eq(Jogo.skill_unica, "mao_de_midas")
	assert_eq(Jogo.dificuldade, "dificil")
	assert_eq(Jogo.nivel_arma("espada"), 3)
	assert_true(Jogo.inventario.tem("espada_ferro"))
	assert_eq(int(Jogo.arma_extra.melhoria), 3)
	assert_eq(Missoes.estado("G_F_01"), "ativa")
	assert_eq(Amizade.coracoes("lyra"), 2)
	assert_eq(Jogo.cristais, [5])
	assert_eq(Jogo.andar_atual, 7)
	assert_eq(Tempo.dia, 9)
	DirAccess.remove_absolute(ProjectSettings.globalize_path(Gravar.caminho(8)))


func test_dificuldade() -> void:
	Jogo.dificuldade = "historia"
	assert_eq(Jogo.dif("recebido"), 0.5)
	assert_eq(Jogo.dif("perda"), 0.0)
	Jogo.dificuldade = "dificil"
	assert_eq(Jogo.dif("recebido"), 1.5)
	Jogo.dificuldade = "normal"
	assert_eq(Jogo.dif("feito"), 1.0)
