extends Node
## Música (com mistura suave entre faixas, sempre em ciclo) e efeitos sonoros. Os ficheiros vêm de res://musica e
## res://sons (feitos por ferramentas/som/musica.py e efeitos.py; docs/AUDIO.md).
## Muitos sons tocam sozinhos a partir dos sinais do jogo (Eventos) e de todos os botões da interface.

var _musica_a: AudioStreamPlayer
var _musica_b: AudioStreamPlayer
var _faixa_atual: String = ""
var _faixa_antes_do_boss: String = ""
var volume_musica: float = 0.8
var volume_efeitos: float = 1.0
var _ultimo: Dictionary = {}   # nome do efeito -> tempo em que tocou (para não tocar o mesmo 20 vezes seguidas)
var _passo_t := 0.0
var _passo_n := 0
const POR_REGIAO := {1: "relva", 2: "pedra", 3: "relva", 4: "areia", 5: "neve", 6: "areia", 7: "pedra", 8: "pedra", 9: "relva", 10: "pedra"}


func _ready() -> void:
	_musica_a = AudioStreamPlayer.new()
	_musica_b = AudioStreamPlayer.new()
	add_child(_musica_a)
	add_child(_musica_b)
	Eventos.jogador_dano.connect(func(_v): efeito("dano_heroi"))
	Eventos.jogador_morreu.connect(func(): efeito("morrer", 0.0))
	Eventos.jogador_subiu_nivel.connect(func(_n): efeito("subir_nivel", 0.0))
	Eventos.monstro_morto.connect(func(_id, _n): efeito("monstro_morre"))
	Eventos.boss_comecou.connect(func(_b):
		_faixa_antes_do_boss = _faixa_atual
		efeito("boss_rugido", 0.0))
	Eventos.boss_acabou.connect(func(_b):
		if _faixa_antes_do_boss != "":
			tocar_musica(_faixa_antes_do_boss, 2.5))
	Eventos.boss_derrotado.connect(func(_id): efeito("vitoria", 0.0))
	Eventos.peixe_apanhado.connect(func(_id): efeito("pesca_apanhado", 0.0))
	Eventos.ouro_mudou.connect(func(_t): efeito("moeda"))
	Eventos.equipamento_mudou.connect(func(): efeito("equipar"))
	Eventos.mensagem_sistema.connect(_mensagem)
	get_tree().node_added.connect(_no_novo)


func tocar_musica(nome: String, mistura: float = 1.5) -> void:
	if nome == _faixa_atual or nome == "":
		return
	var caminho := "res://musica/%s.ogg" % nome
	if not ResourceLoader.exists(caminho):
		return
	_faixa_atual = nome
	var nova := _musica_b if _musica_a.playing else _musica_a
	var velha := _musica_a if nova == _musica_b else _musica_b
	var s: AudioStream = load(caminho)
	if s is AudioStreamOggVorbis:
		(s as AudioStreamOggVorbis).loop = nome != "morte"
	nova.stream = s
	nova.volume_db = -40.0
	nova.play()
	var t := create_tween().set_parallel()
	t.tween_property(nova, "volume_db", linear_to_db(maxf(0.001, volume_musica)), mistura)
	t.tween_property(velha, "volume_db", -40.0, mistura)
	t.chain().tween_callback(func(): if velha.volume_db <= -39.0: velha.stop())


## Toca um efeito (sons/<nome>.ogg). variacao: quanto o tom muda ao calhas (0 = sempre igual).
func efeito(nome: String, variacao: float = 0.06, volume: float = 1.0) -> void:
	var agora := Time.get_ticks_msec() / 1000.0
	if agora - float(_ultimo.get(nome, -1.0)) < 0.045:
		return
	_ultimo[nome] = agora
	var caminho := "res://sons/%s.ogg" % nome
	if not ResourceLoader.exists(caminho):
		return
	var p := AudioStreamPlayer.new()
	p.stream = load(caminho)
	p.volume_db = linear_to_db(maxf(0.001, volume_efeitos * volume))
	if variacao > 0.0:
		p.pitch_scale = 1.0 + randf_range(-variacao, variacao)
	add_child(p)
	p.play()
	p.finished.connect(p.queue_free)


## Passos do herói (chamado pelo jogador enquanto anda): o chão depende da região, da cidade e de estar dentro de casa.
func passos(delta: float, a_correr: bool, regiao: int) -> void:
	_passo_t -= delta
	if _passo_t > 0.0:
		return
	_passo_t = 0.24 if a_correr else 0.33
	_passo_n += 1
	var chao: String = "madeira" if Jogo.dentro else String(POR_REGIAO.get(regiao, "pedra"))
	efeito("passo_%s_%d" % [chao, 1 + _passo_n % 2], 0.08, 0.55)


func _mensagem(texto: String, tipo: String) -> void:
	if "Missão concluída" in texto or "Conquista" in texto:
		efeito("missao_concluida", 0.0)
		return
	match tipo:
		"aviso":
			efeito("recusar", 0.0, 0.6)
		"nivel":
			efeito("notificacao", 0.0, 0.7)
		"andar":
			efeito("abrir_janela", 0.0)
		_:
			efeito("mensagem_sistema", 0.0, 0.5)


## Todos os botões da interface fazem som (passar por cima e carregar).
func _no_novo(n: Node) -> void:
	if n is BaseButton:
		var b := n as BaseButton
		b.pressed.connect(func(): efeito("aceitar", 0.0, 0.7))
		b.mouse_entered.connect(func(): efeito("cursor", 0.0, 0.5))
		b.focus_entered.connect(func(): efeito("cursor", 0.0, 0.5))
