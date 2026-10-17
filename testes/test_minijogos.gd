extends GutTest
## Jogos da Taberna (docs/ATIVIDADES.md 4.9).

var ui


func before_each() -> void:
	ui = load("res://scripts/ui/taberna_ui.gd").new()
	add_child_autofree(ui)


func test_carta_atq_pela_regiao_e_tipo() -> void:
	# Slime Verde: região 1, tipo fraco -> 2 + 1 × 1,2 + 0 = 3
	assert_eq(int(ui.carta("slime_verde").atq), 3)


func test_elemento_forte_da_mais_3() -> void:
	var a := {"atq": 5, "elemento": "fogo", "fraquezas": []}
	var b := {"atq": 6, "elemento": "fisico", "fraquezas": ["fogo"]}
	assert_eq(ui._valor(a, b), 8)
	assert_eq(ui._valor(b, a), 6)


func test_apostas_altas_depois_do_andar_30() -> void:
	Jogo.andar_maximo = 1
	assert_false(1000 in ui._apostas())
	Jogo.andar_maximo = 30
	assert_true(1000 in ui._apostas())
	Jogo.andar_maximo = 1


func test_zona_do_braco_cresce_com_a_for_ate_40() -> void:
	assert_true(ui._largura_zona() >= 0.16)
	assert_true(ui._largura_zona() <= 0.4)


func test_arena_so_abre_com_o_rank_e_perder_nao_mata() -> void:
	var mundo := Node3D.new()
	add_child_autofree(mundo)
	Jogo.novo_jogo("Teste")
	Arena.entrar(mundo, "bronze", Vector3.ZERO)
	assert_null(Arena.atual, "rank F: a Arena de Bronze ainda está fechada")
	Jogo.pontos_guilda = 100000
	Jogo.andar_maximo = 12
	Arena.entrar(mundo, "bronze", Vector3.ZERO)
	assert_not_null(Arena.atual)
	Arena.atual.perder()
	assert_eq(Jogo.hp, 1.0)
	assert_null(Arena.atual)
	assert_false(Jogo.dentro)
