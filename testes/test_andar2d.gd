extends GutTest
## A versão 2D do andar (Fase D do OBJETIVO.md; scripts/mundo2d/; docs/PROGRAMACAO.md, secção 4A).

var andar: Andar2D


func before_each() -> void:
	get_tree().paused = false
	Jogo.novo_jogo("Teste")


func _montar(n: int) -> void:
	Jogo.andar_atual = n
	andar = load("res://cenas/mundo2d/andar2d.tscn").instantiate()
	add_child_autofree(andar)


func test_andar_1_tem_chao_plantas_e_heroi() -> void:
	_montar(1)
	var filas := andar.mundo.get_children().filter(func(n): return n is MeshInstance2D)
	assert_gt(filas.size(), 50, "uma fila de chão por cada 2 m")
	assert_gt(andar.mundo.get_child_count(), 500, "erva, flores, árvores...")
	assert_not_null(andar.heroi)
	assert_true(andar.pode_passar(andar.heroi.position, andar.heroi.position + Vector2(8, 0)))


func test_nao_se_sobe_paredes_de_rocha() -> void:
	_montar(33)   # deserto: paredes de rocha de 3 m
	var par := []
	for z in range(-200, 200, 2):
		for x in range(-200, 200, 2):
			var p := Vector2(x + 1, z + 1)
			if andar.altura_m(p) > 2.5 and absf(andar.altura_m(p + Vector2(0, 2))) < 0.3:
				par = [p + Vector2(0, 2), p]
				break
		if not par.is_empty():
			break
	assert_false(par.is_empty(), "há uma parede de rocha com chão à frente")
	if not par.is_empty():
		assert_false(andar.pode_passar(par[0] * 16.0, par[1] * 16.0))
