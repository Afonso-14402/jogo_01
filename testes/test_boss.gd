extends GutTest
## Bosses: fases pelos limiares de vida, formas dos ataques (docs/BOSSES.md; docs/SISTEMAS.md, secção 7).


func test_fases_do_javali_rei() -> void:
	var b: Boss = Boss.new().configurar("javali_rei", 7, "mini_boss")
	assert_eq(b.fases.size(), 2)
	assert_almost_eq(float(b.fases[1].limite), 0.6, 0.001)
	var formas: Array = b.fases[0].ataques.map(func(a): return a.forma)
	assert_true("carga" in formas, "Carga Real")
	assert_true("chamar" in formas, "Chamar Javalis")
	b.free()


func test_fases_do_ent() -> void:
	var b: Boss = Boss.new().configurar("ent_anciao", 13, "boss")
	assert_eq(b.fases.size(), 3)
	assert_almost_eq(float(b.fases[2].limite), 0.35, 0.001)
	b.free()


func test_formas_pelo_texto() -> void:
	assert_eq(Boss._forma("corre em linha reta (aviso 1 s"), "carga")
	assert_eq(Boss._forma("salta e cai, onda de choque em anel"), "area")
	assert_eq(Boss._forma("projéteis em área"), "projeteis")
	assert_eq(Boss._forma(": 2 javalis normais (uma vez"), "golpe")
	assert_eq(Boss._forma("Chamar Javalis"), "chamar")


func test_todos_os_bosses_tem_fases() -> void:
	for d in Dados.tabela("bosses").values():
		var b: Boss = Boss.new().configurar(d.id, int(d.nivel), d.tipo)
		assert_gt(b.fases.size(), 0, d.id)
		b.free()
