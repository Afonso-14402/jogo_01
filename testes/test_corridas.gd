extends GutTest
## As corridas (scripts/ui/corrida_ui.gd; docs/ATIVIDADES.md 4.5).

var ui


func before_each() -> void:
	Jogo.novo_jogo("Teste")
	ui = preload("res://scripts/ui/corrida_ui.gd").new()
	add_child_autofree(ui)


func after_each() -> void:
	get_tree().paused = false


func _ate_ao_fim(passo := 1.0 / 30.0, max_s := 300.0) -> void:
	var t := 0.0
	while ui._a_correr and t < max_s:
		ui._passo(passo)
		t += passo


func test_ha_quatro_corridas_com_os_numeros_dos_docs() -> void:
	var c: Dictionary = Dados.tabela("minijogos").corridas
	assert_eq(c.size(), 4)
	assert_eq(c.vagonetas.organizador, "hilda_fundo_rocha")
	assert_eq(int(c.vagonetas.tempo), 60)
	assert_eq(c.lagartos.rivais.size(), 3)


func test_vagoneta_sem_cristais_nem_pancadas_demora_64_s() -> void:
	ui.correr("vagonetas")
	ui._coisas.clear()
	_ate_ao_fim()
	assert_almost_eq(ui._t, 64.0, 0.2)
	assert_false(Jogo.contadores.has("corridas_vagonetas"))   # mais de 60 s: não ganhou


func test_vagoneta_rapida_cumpre_a_missao() -> void:
	Missoes.aceitar("R2_09")
	ui.correr("vagonetas")
	ui._coisas.clear()
	for k in 30:   # cristais pelo caminho, todos no carril do meio
		ui._coisas.append({"d": 20.0 + k * 10.0, "x": 1.0, "tipo": "cristal", "feita": false})
	_ate_ao_fim()
	assert_lt(ui._t, 60.0)
	assert_eq(ui._apanhadas, 30)
	assert_eq(Missoes.estado("R2_09"), "pronta")


func test_viga_sem_baixar_para_a_vagoneta() -> void:
	ui.correr("vagonetas")
	ui._coisas = [{"d": 5.0, "x": 1.0, "tipo": "viga", "feita": false}]
	for k in 15:
		ui._passo(1.0 / 30.0)
	assert_gt(ui._parado, 0.0)
	ui.correr("vagonetas")
	ui._coisas = [{"d": 5.0, "x": 1.0, "tipo": "viga", "feita": false}]
	ui._carregar(0)   # baixar
	for k in 15:
		ui._passo(1.0 / 30.0)
	assert_eq(ui._parado, 0.0)


func test_canoa_remar_a_vez_anda_e_mesmo_lado_vira() -> void:
	ui.correr("canoas")
	ui._carregar(-1)
	ui._carregar(1)
	assert_almost_eq(ui._vel, 2.4, 0.01)
	ui._carregar(1)   # outra vez à direita: vira para a esquerda
	assert_eq(ui._alvo, 0.0)


func test_lagarto_salta_pedras() -> void:
	ui.correr("lagartos")
	ui._coisas = [{"d": 3.0, "x": 1.0, "tipo": "pedra", "feita": false}]
	ui._carregar(0)
	for k in 6:
		ui._passo(1.0 / 30.0)
	assert_eq(ui._travado, 0.0)
