extends GutTest
## Estados alterados e elementos (docs/SISTEMAS.md, secções 4.5 e 5).


class Boneco:
	extends Node3D
	var hp := 100.0

	func hp_maximo_estado() -> float:
		return 100.0

	func perder_hp_estado(v: float, _cor: String, minimo_1: bool) -> void:
		hp = max(1.0 if minimo_1 else 0.0, hp - v)


var boneco: Boneco
var e: Estados


func before_each() -> void:
	boneco = Boneco.new()
	add_child_autofree(boneco)
	e = Estados.new()
	boneco.add_child(e)


func _correr(segundos: float) -> void:
	var passo := 1.0 / 60.0
	var t := 0.0
	while t < segundos:
		e._physics_process(passo)
		t += passo


func test_tres_frios_congelam() -> void:
	e.aplicar("frio")
	e.aplicar("frio")
	assert_true(e.tem("frio"))
	assert_almost_eq(e.mult("vel_mult"), 0.7, 0.001)
	e.aplicar("frio")
	assert_false(e.tem("frio"))
	assert_true(e.tem("congelado"))
	assert_true(e.flag("parado"))


func test_congelado_parte_com_golpe() -> void:
	e.aplicar("congelado")
	assert_almost_eq(e.consumir_golpe_mult(), 1.5, 0.001)
	assert_false(e.tem("congelado"))


func test_veneno_tira_2_por_cento_e_nao_mata() -> void:
	e.aplicar("veneno")
	_correr(1.01)
	assert_almost_eq(boneco.hp, 98.0, 1.01)
	boneco.hp = 1.5
	_correr(3.0)
	assert_eq(boneco.hp, 1.0)


func test_estado_acaba() -> void:
	e.aplicar("lentidao")
	_correr(3.1)
	assert_false(e.tem("lentidao"))


func test_boss_dura_metade_e_fica_imune() -> void:
	e.e_boss = true
	e.aplicar("lentidao")
	_correr(1.6)
	assert_false(e.tem("lentidao"))
	assert_false(e.aplicar("lentidao"), "imune 10 s")
	_correr(10.1)
	assert_true(e.aplicar("lentidao"))


func test_encharcado_raio_e_fogo() -> void:
	e.aplicar("encharcado")
	assert_almost_eq(e.mult_elemento("raio"), 1.5, 0.001)
	assert_almost_eq(e.mult_elemento("fogo"), 0.5, 0.001)


func test_antidoto_e_imunidade() -> void:
	e.aplicar("veneno")
	e.tirar(["veneno"])
	assert_false(e.tem("veneno"))
	e.dar_imunidade("frio", 5.0)
	assert_false(e.aplicar("frio"))


func test_dano_com_fraqueza_e_encharcado() -> void:
	var c := Dados.constantes
	var normal := Formulas.mult_elemento(c, "raio", [], [], [])
	assert_eq(normal, 1.0)
	Dano.rng.seed = 1
	var a := Dano.calcular(100.0, 1.0, 0.0, {"elem_mult": {"raio": 1.5}}, "raio")
	Dano.rng.seed = 1
	var b := Dano.calcular(100.0, 1.0, 0.0, {}, "raio")
	assert_gt(a.valor, b.valor)


func test_hipotese_do_golpe() -> void:
	var rng := RandomNumberGenerator.new()
	rng.seed = 5
	var pegou := 0
	for i in 200:
		e.ativos.clear()
		if not e.do_golpe([{"estado": "veneno", "hipotese": 0.3}], rng).is_empty():
			pegou += 1
	assert_between(pegou, 40, 80)
