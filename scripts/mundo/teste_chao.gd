extends Node3D
## Cena de teste (passos 1 e 2 de docs/PROGRAMACAO.md, secção 9): chão com o kit da Região 1,
## o herói a andar, a câmara a seguir e o HUD. Serve para ver o tamanho, as cores e o ângulo da câmara.

const KIT := "res://arte/regioes/r01_floresta/kit/r01_%s.glb"
const TAMANHO := 14   # células de 2×2 m para cada lado

var jogador: Jogador
var camara: Camara


func _ready() -> void:
	Ambiente.criar(self)
	_chao()
	_decoracao()
	jogador = preload("res://cenas/personagens/jogador.tscn").instantiate()
	add_child(jogador)
	camara = Camara.new()
	camara.alvo = jogador
	add_child(camara)
	add_child(preload("res://cenas/ui/hud.tscn").instantiate())
	_monstros()
	Sistema.mensagem("Bem-vindo à torre. (WASD para andar, Shift para correr, Espaço para esquivar)")


func _chao() -> void:
	var rng := RandomNumberGenerator.new()
	rng.seed = 7
	var pecas := ["chao_1", "chao_1", "chao_1", "chao_2", "chao_3"]
	for x in range(-TAMANHO, TAMANHO):
		for z in range(-TAMANHO, TAMANHO):
			var nome: String = "caminho" if x == 0 or z == 0 else pecas[rng.randi() % pecas.size()]
			_por(nome, Vector3(x * 2 + 1, -0.2, z * 2 + 1))
	# o chão tem colisão própria (uma caixa grande): as peças do kit são só visuais
	var corpo := StaticBody3D.new()
	var forma := CollisionShape3D.new()
	var caixa := BoxShape3D.new()
	caixa.size = Vector3(TAMANHO * 4, 1, TAMANHO * 4)
	forma.shape = caixa
	forma.position.y = -0.5
	corpo.add_child(forma)
	add_child(corpo)


func _decoracao() -> void:
	var rng := RandomNumberGenerator.new()
	rng.seed = 11
	var deco := {"arvore_1": 0.6, "arvore_2": 0.5, "arvore_3": 0.9, "rocha_1": 0.7, "rocha_2": 0.5, "arbusto_1": 0.0,
				 "erva": 0.0, "flores": 0.0, "cogumelo_gigante": 0.5}
	var nomes := deco.keys()
	for i in 70:
		var p := Vector3(rng.randf_range(-TAMANHO * 2 + 2, TAMANHO * 2 - 2), 0, rng.randf_range(-TAMANHO * 2 + 2, TAMANHO * 2 - 2))
		if p.length() < 5.0 or abs(p.x) < 1.5 or abs(p.z) < 1.5:
			continue
		var nome: String = nomes[rng.randi() % nomes.size()]
		var no := _por(nome, p)
		no.rotation.y = rng.randf() * TAU
		var raio: float = deco[nome]
		if raio > 0.0:
			_obstaculo(p, raio, no)
		if nome.begins_with("arvore") or nome == "cogumelo_gigante":
			no.add_to_group("tapa_vista")
			no.set_meta("raio", 2.6 if nome == "arvore_3" else 2.0)
			no.set_meta("altura", 3.4)
	_por("bau", Vector3(3, 0, -3))
	_por("fogueira", Vector3(-3, 0, 3))
	_por("cristal_teletransporte", Vector3(4, 0, 4))


func _monstros() -> void:
	var lista := [["slime_verde", Vector3(6, 0, -2)], ["slime_verde", Vector3(7, 0, 0)], ["lobo_cinzento", Vector3(-8, 0, -6)],
				  ["javali", Vector3(9, 0, 8)], ["cogumelo_andante", Vector3(-6, 0, 7)]]
	for m in lista:
		var mo := Monstro.new().configurar(m[0], 1)
		mo.position = m[1] + Vector3(0, 0.3, 0)
		add_child(mo)


func _por(nome: String, posicao: Vector3) -> Node3D:
	var cena: PackedScene = load(KIT % nome)
	var no: Node3D = cena.instantiate()
	no.position = posicao
	add_child(no)
	return no


func _obstaculo(p: Vector3, raio: float, visual: Node3D) -> void:
	var corpo := StaticBody3D.new()
	corpo.set_meta("visual", visual)
	var forma := CollisionShape3D.new()
	var cil := CylinderShape3D.new()
	cil.radius = raio
	cil.height = 6.0
	forma.shape = cil
	forma.position = p + Vector3(0, 3.0, 0)
	corpo.add_child(forma)
	add_child(corpo)
