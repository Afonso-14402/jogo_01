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
