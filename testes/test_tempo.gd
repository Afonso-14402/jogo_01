extends GutTest
## Tempo, calendário, clima e cansaço (docs/SISTEMAS.md, secção 14).


func before_each() -> void:
	Tempo.hora = 6.0
	Tempo.dia = 1
	Tempo.estacao = 0
	Tempo.ano = 1
	Tempo.cansado = false


func test_semana_comeca_a_segunda() -> void:
	assert_eq(Tempo.dia_semana(), "Segunda")
	Tempo.dia = 7
	assert_true(Tempo.e_domingo())
	Tempo.dia = 8
	assert_eq(Tempo.dia_semana(), "Segunda")


func test_periodos() -> void:
	for par in [[7.0, "dia"], [18.5, "entardecer"], [23.0, "noite"], [3.0, "noite"], [5.5, "madrugada"]]:
		Tempo.hora = par[0]
		assert_eq(Tempo.periodo(), par[1])


func test_dormir_vai_para_as_6_do_dia_seguinte() -> void:
	Tempo.hora = 23.0
	Tempo.cansado = true
	Tempo.dormir()
	assert_eq(Tempo.dia, 2)
	assert_eq(Tempo.hora, 6.0)
	assert_false(Tempo.cansado)


func test_dormir_de_madrugada_nao_salta_dia() -> void:
	Tempo.dia = 3
	Tempo.hora = 3.0
	Tempo.dormir()
	assert_eq(Tempo.dia, 3)


func test_mudar_de_estacao() -> void:
	Tempo.dia = 28
	Tempo._passar_dia()
	assert_eq(Tempo.dia, 1)
	assert_eq(Tempo.nome_estacao(), "verao")


func test_clima_e_sempre_o_mesmo_no_mesmo_dia() -> void:
	var a := Tempo.clima(1)
	var b := Tempo.clima(1)
	assert_eq(a, b)
	assert_eq(Tempo.clima(2).efeito, "nenhum", "as cavernas não têm céu")


func test_inverno_na_cidade_tem_neve_as_vezes() -> void:
	Tempo.estacao = 3
	var viu_neve := false
	for d in range(1, 29):
		Tempo.dia = d
		viu_neve = viu_neve or Tempo.clima(0).efeito == "neve"
	assert_true(viu_neve)


func test_cansado_tira_20_por_cento() -> void:
	Jogo.novo_jogo("Teste")
	var v := Jogo.velocidade()
	Tempo.cansado = true
	assert_almost_eq(Jogo.velocidade(), v * 0.8, 0.001)
	Tempo.cansado = false


func test_luz_do_dia() -> void:
	assert_eq(CicloDia.fator_dia(12.0), 1.0)
	assert_eq(CicloDia.fator_dia(23.0), 0.0)
	assert_between(CicloDia.fator_dia(19.0), 0.01, 0.99)


func test_genero_nas_mensagens() -> void:
	Jogo.tratamento = "ela"
	assert_eq(Sistema.genero("Estás cansad{o/a}."), "Estás cansada.")
	Jogo.tratamento = "ele"
	assert_eq(Sistema.genero("Estás cansad{o/a}."), "Estás cansado.")
