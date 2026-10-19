extends GutTest
## A vista 2D (OBJETIVO.md, Fase D; scripts/mundo2d/vista2d.gd): monta-se nos andares e na cidade e desenha tudo em 2D.

var cena: Node


func before_each() -> void:
	get_tree().paused = false
	Jogo.novo_jogo("Teste")
	Opcoes.valores["vista_2d"] = true


func _montar(caminho: String, andar: int) -> Vista2D:
	Jogo.andar_atual = andar
	cena = load(caminho).instantiate()
	add_child_autofree(cena)
	await get_tree().process_frame
	await get_tree().process_frame
	for f in cena.get_children():
		if f is Vista2D:
			return f
	return null


func test_andares_de_varias_regioes() -> void:
	for n in [1, 15, 34, 64]:
		var v := await _montar("res://cenas/mundo/andar.tscn", n)
		assert_not_null(v, "andar %d tem vista 2D" % n)
		if v:
			assert_gt(v._proxies.size(), 20, "andar %d: espelhos 2D" % n)
			assert_gt(v.mundo.get_child_count(), 100, "andar %d: chão, plantas e peças" % n)
			assert_eq(get_viewport().get_camera_3d().cull_mask, 0, "a câmara 3D não desenha nada")
		cena.free()
		await get_tree().process_frame


func test_cidade() -> void:
	var v := await _montar("res://cenas/mundo/cidade.tscn", 0)
	assert_not_null(v)
	if v:
		var pecas := v._proxies.filter(func(p): return p.tipo == "peca")
		assert_gt(pecas.size(), 10, "os edifícios são fotografias em pixel art")


func test_projecao() -> void:
	assert_eq(Vista2D.ecra(Vector3(1, 0, 2)), Vector2(16, 32))
	assert_eq(Vista2D.ecra(Vector3(0, 1, 0)), Vector2(0, -12.8))
	assert_almost_eq(Vista2D.escala_px(1.25), 4.0 / 3.0, 0.001)
	assert_almost_eq(Vista2D.escala_px(-1.0), -1.0, 0.001)
