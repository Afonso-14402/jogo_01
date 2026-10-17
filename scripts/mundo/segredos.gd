class_name Segredos
extends Node3D
## Os segredos e puzzles de cada andar (docs/regioes/rXX, linhas "Segredo" e "Puzzle"; os sítios são os pontos ?? e !!
## do mapa, dados/andares/aNNN.json). Cada um faz-se uma vez (flag "seg_aNNN_<nome>"). Para já: a Região 1.

const NAT := "res://arte/regioes/r01_floresta/natureza/"
const CORES := {"vermelho": Color("ea4f36"), "laranja": Color("f79617"), "amarelo": Color("f9c22b"), "verde": Color("1ebc73"), "azul": Color("4d9be6")}

## As peças 3D especiais (arte/regioes/<região>/andares/aNN_<nome>.glb) que os puzzles usam: o andar não as espalha.
const USADAS := {1: ["moinho"], 2: ["arvore_oca", "arvore_sussurrante"], 3: ["comporta", "cascata"], 4: ["cogumelo_oco", "anel_cogumelos"],
		5: ["toca"], 6: ["estatua_jardim", "colmeia_gigante", "favo"], 7: ["poco_luz"], 8: ["estatua_cavaleiro", "torre_vigia"],
		9: ["sino_barco"], 11: ["vagoneta", "elevador_de_mina"], 12: ["porta_de_madeira_de_mina", "mesa_de_mineiro"],
		13: ["cristal_interruptor", "ponte_de_quartzo"], 14: ["boia_de_luz", "cascata_escura"], 15: ["casulos"],
		16: ["lago_luminoso"], 17: ["ponto_de_eco", "ninho_de_morcego"],
		18: ["fornalha_ana", "portao_com_aneis_de_runas"], 19: ["estalagmite_espelhada", "altar_do_reflexo"],
		21: ["passadico", "caixotes"], 22: ["caldeirao", "casa_torta_da_bruxa", "lirio_branco"], 23: ["pedras_com_animais", "mural"],
		24: ["canoa"], 25: ["alavanca_de_agua"], 26: ["barco_afundado", "comporta_de_raizes"], 27: ["pedra_flutuante", "gruta_atras_de_cascata"],
		28: ["plataforma_giratoria", "ninho_gigante"], 29: ["regador", "flor_armadilha"],
		33: ["ponte_de_pedra_natural"], 34: ["porta_soterrada", "trono"], 35: ["ovos", "carapaca_gigante"],
		36: ["torre_de_pedra_com_vela"], 37: ["costela_gigante"], 38: ["obelisco_com_espelho"], 39: ["painel_de_hieroglifos"],
		41: ["fogueira_de_pedra", "iglu"], 42: ["pinheiro_com_neve"], 43: ["farol"], 44: ["cristal_azul_gigante", "parede_de_gelo_transparente"],
		46: ["torre_do_sino", "armadilhas"], 47: ["pico_com_bandeira"], 48: ["pedra_cantante", "lago_espelho"], 49: ["portao_de_gelo", "trono_de_gelo"],
		51: ["concha_gigante", "barco_destruido", "garrafa"], 52: ["farol"], 53: ["leme", "lanterna_fantasma"], 54: ["ostra_gigante", "comporta_de_coral"],
		56: ["lontras", "naufragio_antigo"], 57: ["coluna_de_corrente"], 58: ["coral_luminoso"], 59: ["concha_alavanca", "concha_falante"]}
## Andares em que os baús "$$" são prémios (só aparecem quando se resolve o segredo ou o puzzle).
const BAUS_PREMIO := [11, 12, 14, 15, 18, 21, 25, 39, 41, 47]

var andar: Node                    # o Andar
var _ordem: Array = []             # puzzles de ordem: o que já se carregou
var _t_sinos: float = 0.0
var _sinos: Dictionary = {}


func _ready() -> void:
	var f := "_andar_%d" % int(andar.numero)
	if has_method(f):
		call(f)
	_corridas()
	_enigmas()


## O sítio de partida das corridas deste andar (docs/ATIVIDADES.md 4.5): ao pé da povoação (ou da Zona Segura).
func _corridas() -> void:
	for c in Dados.tabela("minijogos").get("corridas", {}).values():
		if int(c.andar) != int(andar.numero):
			continue
		var pov: Array = pontos("@@")
		var p: Vector3 = (pov[0].p if not pov.is_empty() else andar.ponto_seguro) + Vector3(5.0, 0, 3.0)
		var veiculo: String = {"vagonetas": "vagoneta", "canoas": "canoa", "treno": "treno"}.get(c.id, "")
		if veiculo != "" and ResourceLoader.exists("%s/andares/a%02d_%s.glb" % [pasta(), int(andar.numero), veiculo]):
			peca(veiculo, p)
		letreiro(p, "Corrida de %s" % c.nome_pt, Color("fbff86"))
		var cid: String = c.id
		usar(p + Vector3(0, 0, 1.2), "Corrida de %s" % c.nome_pt, func():
			var r = get_tree().get_first_node_in_group("corrida_ui")
			if r:
				r.correr(cid))


func _process(delta: float) -> void:
	if _t_sinos > 0.0:
		_t_sinos -= delta
		if _t_sinos <= 0.0 and _sinos.size() < 3:
			_sinos.clear()
			Sistema.mensagem("Os sinos calaram-se. Tens de tocar os três no mesmo minuto!", "aviso")


# ------------------------------------------------------------------ ajudas ------------------------------------------------------------------

## Os pontos do mapa com esta marca (pela ordem dos dados): [{p: Vector3, texto: String}]
func pontos(marca: String) -> Array:
	var r := []
	for p in andar.dados.get("pontos", []):
		if p.marca == marca:
			r.append({"p": andar.centro_celula(int(p.x), int(p.y)), "texto": String(p.texto)})
	return r


func feito(nome: String) -> bool:
	return Jogo.tem_flag("seg_a%03d_%s" % [int(andar.numero), nome])


func marcar(nome: String) -> void:
	Jogo.por_flag("seg_a%03d_%s" % [int(andar.numero), nome])


func chao(p: Vector3) -> Vector3:
	p.y = andar.altura_em(p.x, p.z)
	return p


## A pasta da região (res://arte/regioes/rNN_xxx).
func pasta() -> String:
	return String(andar.kit.get("chao", [""])[0]).get_base_dir().get_base_dir()


## Um sprite de natureza (primeiro o da região, senão o da floresta).
func sprite(nome: String, p: Vector3, cor := Color.WHITE) -> Sprite3D:
	var c := pasta() + "/natureza/" + nome + ".png"
	if not ResourceLoader.exists(c):
		c = NAT + nome + ".png"
	if not ResourceLoader.exists(c):
		return null
	var s := Sprite3D.new()
	s.texture = load(c)
	s.pixel_size = 1.0 / Natureza.PPM
	s.billboard = BaseMaterial3D.BILLBOARD_FIXED_Y
	s.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
	s.alpha_cut = SpriteBase3D.ALPHA_CUT_DISCARD
	s.offset.y = s.texture.get_height() / 2.0
	s.modulate = cor
	add_child(s)
	s.global_position = chao(p)
	return s


## Uma peça 3D especial deste andar (aNN_<nome>.glb): grande -> fica transparente quando tapa o herói.
func peca(nome: String, p: Vector3, rot: float = 0.0) -> Node3D:
	var c := "%s/andares/a%02d_%s.glb" % [pasta(), int(andar.numero), nome]
	if not ResourceLoader.exists(c):
		return sprite("menir", p)
	var no: Node3D = (load(c) as PackedScene).instantiate()
	add_child(no)
	no.global_position = chao(p)
	if andar.escuro:
		LuzesGruta.registar(c, no.global_position)
	no.rotation.y = rot
	var a := Pecas.caixa(c)
	if a.size.y > 2.5:
		no.add_to_group("tapa_vista")
		no.set_meta("raio", maxf(a.size.x, a.size.z) * 0.55)
		no.set_meta("altura", a.size.y * 0.5)
	var corpo := StaticBody3D.new()
	var f := CollisionShape3D.new()
	var cil := CylinderShape3D.new()
	cil.radius = clampf(minf(a.size.x, a.size.z) * 0.4, 0.3, 3.0)
	cil.height = maxf(1.0, a.size.y)
	f.shape = cil
	f.position.y = cil.height / 2.0
	corpo.add_child(f)
	no.add_child(corpo)
	return no


## Escolher numa lista (caixa de diálogo); devolve o índice (ou -1).
func escolher(opcoes: Array) -> int:
	var ui = get_tree().get_first_node_in_group("dialogo_ui")
	if ui == null or ui.ocupado:
		return -1
	ui.ocupado = true
	var i: int = await ui.escolher(opcoes)
	ui.fechar()
	return i


func arma_tipo() -> String:
	return String(Dados.arma(Jogo.arma_equipada).get("tipo", ""))


func usar(p: Vector3, texto: String, cb: Callable) -> Interagivel:
	var i := Interagivel.new()
	i.texto = texto
	add_child(i)
	i.global_position = chao(p)
	i.usado.connect(func(_j): cb.call())
	return i


func letreiro(p: Vector3, texto: String, cor := Color("fbff86")) -> Label3D:
	var l := Label3D.new()
	l.text = texto
	l.font_size = 40
	l.pixel_size = 0.012
	l.outline_size = 10
	l.modulate = cor
	l.billboard = BaseMaterial3D.BILLBOARD_ENABLED
	add_child(l)
	l.global_position = chao(p) + Vector3(0, 2.2, 0)
	return l


func dar(item: String, qtd: int = 1) -> void:
	if Inventario._dados(item).is_empty():
		return
	Jogo.inventario.adicionar(item, qtd)
	Sistema.mensagem("Recebeste: %s ×%d" % [Inventario._dados(item).get("nome_pt", item), qtd], "item")


func luz(p: Vector3, cor: Color, energia: float = 0.0) -> OmniLight3D:
	var l := OmniLight3D.new()
	l.light_color = cor
	l.omni_range = 4.0
	l.light_energy = energia
	add_child(l)
	l.global_position = chao(p) + Vector3(0, 1.2, 0)
	return l


func resolvido(nome: String, texto: String, bau: String = "", onde := Vector3.INF) -> void:
	marcar(nome)
	Sistema.mensagem(texto, "nivel")
	Colecoes.contar("puzzles")
	if bau != "":
		var b: Array = pontos("$$")
		var p: Vector3 = onde if onde != Vector3.INF else (b[0].p if not b.is_empty() else andar.ponto_seguro + Vector3(2, 0, 2))
		andar.bau_em(chao(p), bau)


## Puzzle de ordem: carregar nas coisas pela ordem certa (se errares, volta ao início).
func carregar_ordem(qual: int, certa: Array, nome: String, ao_acertar: Callable, ao_errar: Callable = Callable()) -> void:
	if feito(nome):
		return
	_ordem.append(qual)
	var k := _ordem.size() - 1
	if _ordem[k] != certa[k]:
		_ordem.clear()
		Sistema.mensagem("Não era essa… Volta ao princípio.", "aviso")
		if ao_errar.is_valid():
			ao_errar.call()
		return
	if _ordem.size() == certa.size():
		_ordem.clear()
		ao_acertar.call()


# ------------------------------------------------------------------ Região 1 ------------------------------------------------------------------

## Andar 1 — Moinho Abandonado (puxar a corda abre um alçapão com um baú de prata) e o puzzle tutorial da pedra.
func _andar_1() -> void:
	for s in pontos("??"):
		peca("moinho", s.p + Vector3(0, 0, -3.0))
		usar(s.p, "Puxar a corda do moinho", func():
			if feito("moinho"):
				Sistema.mensagem("As pás já rodam ao vento.")
				return
			resolvido("moinho", "As pás do moinho começam a rodar… e abre-se um alçapão no chão!", "prata", s.p + Vector3(2, 0, 1)))
	for s in pontos("!!"):
		var buraco := MeshInstance3D.new()   # o buraco no chão
		var q := CylinderMesh.new()
		q.top_radius = 1.0
		q.bottom_radius = 1.0
		q.height = 0.05
		buraco.mesh = q
		var m := StandardMaterial3D.new()
		m.albedo_color = Color("2e222f")
		buraco.material_override = m
		add_child(buraco)
		buraco.global_position = chao(s.p) + Vector3(0, 0.03, 0)
		if feito("pedra"):
			buraco.visible = false
			continue
		var pedra := sprite("rocha_2", s.p + Vector3(-2.2, 0, 0))
		letreiro(s.p + Vector3(-2.2, 0, 0), "Empurra-me!", Color("c7dcd0"))
		usar(s.p + Vector3(-2.2, 0, 0), "Empurrar a pedra", func():
			if feito("pedra"):
				return
			var tw := create_tween()
			tw.tween_property(pedra, "global_position", chao(s.p), 0.6)
			tw.tween_callback(func():
				buraco.visible = false
				pedra.offset.y = 4
				resolvido("pedra", "A pedra tapou o buraco! Assim já se passa. (Há pedras que se empurram: experimenta!)", "madeira", s.p + Vector3(2.5, 0, 0))))


## Andar 2 — a árvore oca (Anel do Sussurro) e Os 3 Sussurros (três árvores dizem uma ordem; tocar 3 pedras assim).
func _andar_2() -> void:
	for s in pontos("??"):
		peca("arvore_oca", s.p + Vector3(0, 0, -1.5))
		usar(s.p + Vector3(0, 0, 0.6), "Procurar na árvore oca", func():
			if feito("arvore_oca"):
				Sistema.mensagem("A árvore está vazia. Só ecoa.")
				return
			marcar("arvore_oca")
			dar("anel_sussurro"))
	for s in pontos("!!"):
		var cores := ["azul", "vermelho", "amarelo"]
		var certa := [0, 1, 2]
		certa.shuffle()
		var nomes := ["primeira", "segunda", "terceira"]
		for k in 3:   # as árvores: cada uma diz uma parte da ordem
			var pa: Vector3 = s.p + Vector3((k - 1) * 3.5, 0, -3.0)
			peca("arvore_sussurrante", pa)
			var qual: int = certa[k]
			usar(pa + Vector3(0, 0, 1.0), "Ouvir a árvore", func():
				Sistema.mensagem("A árvore sussurra: «A pedra %s é a %s.»" % [cores[qual], nomes[k]]))
		for k in 3:   # as pedras
			var pp: Vector3 = s.p + Vector3((k - 1) * 2.5, 0, 2.0)
			var pedra := sprite("menir", pp, CORES[cores[k]].lightened(0.3))
			var l := luz(pp, CORES[cores[k]])
			var kk := k
			usar(pp + Vector3(0, 0, 0.8), "Tocar na pedra %s" % cores[k], func():
				l.light_energy = 2.0
				carregar_ordem(kk, certa, "sussurros", func():
					resolvido("sussurros", "As três pedras brilham ao mesmo tempo… Ouve-se um «clic»: apareceu um baú!", "prata"),
					func():
						for n in get_children():
							if n is OmniLight3D:
								n.light_energy = 0.0))
			if pedra == null:
				continue


## Andar 3 — as comportas (3 rodas pela ordem 2 → 3 → 1 baixam a água), o ninho com a chave e a gruta com o baú de ouro.
func _andar_3() -> void:
	var rodas: Array = pontos("!!")
	var certa := [1, 2, 0]   # "Ordem certa: 2 → 3 → 1"
	for k in rodas.size():
		var r: Dictionary = rodas[k]
		peca("comporta", r.p)
		letreiro(r.p, "Roda %d" % (k + 1), Color("c7dcd0"))
		if k == 0:
			sprite("placa", r.p + Vector3(2.0, 0, 1.0))
			usar(r.p + Vector3(2.0, 0, 1.6), "Ler a placa", func(): Sistema.mensagem("A placa diz: «Primeiro a do meio do vale, depois a do nascente, por fim a da cascata.»"))
		var kk := k
		usar(r.p + Vector3(0, 0, 1.2), "Rodar a roda %d" % (k + 1), func():
			if feito("comportas"):
				Sistema.mensagem("As comportas já estão abertas.")
				return
			Sistema.mensagem("Crrrr… a roda %d range." % (kk + 1))
			carregar_ordem(kk, certa, "comportas", func():
				resolvido("comportas", "As comportas abrem-se e a água do rio baixa! Já se chega à Ilhota a pé.")
				andar.baixar_agua()))
	if feito("comportas"):
		andar.baixar_agua.call_deferred()
	var seg: Array = pontos("??")
	for s in seg:
		if "ninho" in s.texto.to_lower():
			sprite("arbusto_bagas", s.p)
			usar(s.p + Vector3(0, 0, 0.8), "Procurar no ninho", func():
				if feito("ninho"):
					Sistema.mensagem("Só penas e cascas de ovo.")
					return
				marcar("ninho")
				dar("chave_bau_ouro_ilhota"))
		elif "gruta" in s.texto.to_lower():
			peca("cascata", s.p + Vector3(0, 0, -3.0))
			usar(s.p, "Entrar na gruta atrás da cascata", func():
				if feito("gruta"):
					Sistema.mensagem("A gruta está vazia (e molhada).")
					return
				if not Jogo.inventario.tem("chave_bau_ouro_ilhota"):
					Sistema.mensagem("Há um baú de ouro lá ao fundo, preso com um cadeado esquisito. A chave deve estar perto… num ninho?", "aviso")
					return
				Jogo.inventario.retirar("chave_bau_ouro_ilhota")
				Jogo.inventario.adicionar("chave_bau_ouro")   # a chave da Ilhota serve neste baú
				resolvido("gruta", "A chave da Ilhota abre o cadeado da gruta!", "ouro", s.p + Vector3(1.5, 0, 0)))


## Andar 4 — Luzes dos cogumelos (bater em 5 cogumelos-lanterna pela ordem do arco-íris), a sala do Cogumelo Oco
## (Livro de Receitas: Sopas) e o Anel de Fadas à meia-noite.
func _andar_4() -> void:
	var ordem := ["vermelho", "laranja", "amarelo", "verde", "azul"]
	for s in pontos("!!"):
		var lugares := [0, 1, 2, 3, 4]
		lugares.shuffle()   # os cogumelos não estão pela ordem (é esse o puzzle)
		var luzes := []
		for k in 5:
			var cor: String = ordem[lugares[k]]
			var ang := k * TAU / 5.0
			var pc: Vector3 = s.p + Vector3(cos(ang) * 3.2, 0, sin(ang) * 3.2)
			sprite("cogumelos", pc, CORES[cor].lightened(0.35))
			var l := luz(pc, CORES[cor], 0.3)
			letreiro(pc, cor, CORES[cor].lightened(0.2))
			luzes.append(l)
			var idx: int = lugares[k]
			usar(pc + Vector3(0, 0, 0.7), "Bater no cogumelo %s" % cor, func():
				l.light_energy = 2.5
				carregar_ordem(idx, [0, 1, 2, 3, 4], "luzes", func():
					resolvido("luzes", "Os cinco cogumelos acendem-se como um arco-íris! Apareceu um baú.", "prata"),
					func():
						for x in luzes:
							x.light_energy = 0.0))
		letreiro(s.p, "Como o arco-íris…", Color("eaaded"))
	for s in pontos("??"):
		var t: String = s.texto.to_lower()
		if "oco" in t:
			peca("cogumelo_oco", s.p + Vector3(0, 0, -2.5))
			usar(s.p + Vector3(0, 0, 0.5), "Entrar no Cogumelo Oco", func():
				if feito("cogumelo_oco"):
					Sistema.mensagem("A mesa redonda continua lá. As cadeiras também.")
					return
				marcar("cogumelo_oco")
				var n := 0
				for r in Dados.tabela("receitas").values():
					if "sopa" in String(r.id) and not r.id in Jogo.receitas:
						Jogo.aprender_receita(r.id, false)
						n += 1
				Sistema.mensagem("Encontraste o Livro de Receitas: Sopas! (%d receitas novas)" % n, "nivel"))
		elif "fadas" in t:
			peca("anel_cogumelos", s.p)
			usar(s.p, "Centro do Anel de Fadas", func():
				var h := Tempo.hora
				if h >= 0.0 and h < 1.0:
					if not feito("fadas"):
						marcar("fadas")
						Sistema.mensagem("À meia-noite, as fadas riem-se à tua volta e deixam-te um presente.", "nivel")
						dar("po_de_fada", 3)
					else:
						Sistema.mensagem("Ouves risinhos no escuro…")
				else:
					Sistema.mensagem("É só um círculo de cogumelos… Dizem que à meia-noite é diferente."))


## Andar 5 — a toca pequena (só com a Poção de Encolher) com o Ovo de Ouro do Javali.
func _andar_5() -> void:
	for s in pontos("??"):
		peca("toca", s.p + Vector3(0, 0, -1.0))
		usar(s.p + Vector3(0, 0, 0.7), "Toca pequena", func():
			if feito("toca"):
				Sistema.mensagem("A toca está vazia. Ainda cheira a javali.")
				return
			if not Jogo.inventario.tem("pocao_encolher"):
				Sistema.mensagem(Sistema.genero("É pequena demais. Se ao menos fosses mais pequen{o/a}…"), "aviso")
				return
			Jogo.inventario.retirar("pocao_encolher")
			marcar("toca")
			Sistema.mensagem("Bebes a Poção de Encolher e rastejas lá para dentro…", "nivel")
			dar("ovo_ouro_javali"))


## Andar 6 — a estátua com o vaso vazio (Flor de Mel abre a passagem com baú de ouro) e a colmeia labirinto (Mel Real).
func _andar_6() -> void:
	for s in pontos("??"):
		peca("estatua_jardim", s.p + Vector3(0, 0, -0.8))
		letreiro(s.p, "um vaso vazio…", Color("c7dcd0"))
		usar(s.p + Vector3(0, 0, 0.8), "Pôr uma flor no vaso", func():
			if feito("vaso"):
				Sistema.mensagem("A Flor de Mel continua no vaso, a cheirar bem.")
				return
			if not Jogo.inventario.tem("flor_de_mel"):
				Sistema.mensagem("O vaso está vazio. Que flor ficaria bem aqui? Uma doce…", "aviso")
				return
			Jogo.inventario.retirar("flor_de_mel")
			resolvido("vaso", "Pões a Flor de Mel no vaso… e a estátua desliza para o lado! Uma passagem secreta!", "ouro"))
	for s in pontos("!!"):
		peca("colmeia_gigante", s.p + Vector3(0, 0, -5.0))
		var favos := []
		for k in 3:
			var pf: Vector3 = s.p + Vector3((k - 1) * 2.0, 0, -1.5)
			var f := peca("favo", pf)
			favos.append(f)
			usar(pf + Vector3(0, 0, 0.8), "Empurrar o favo", func():
				if feito("colmeia") or f == null or not f.visible:
					return
				var tw := create_tween()
				tw.tween_property(f, "global_position", f.global_position + Vector3(0, 0, -2.0), 0.4)
				tw.tween_callback(func():
					f.visible = false
					if favos.all(func(x): return x == null or not x.visible):
						resolvido("colmeia", "Abriste caminho até ao fundo da colmeia: o Mel Real!")
						dar("mel", 5)))


## Andar 7 — o Poço da Lua (de noite mostra o caminho para a Raiz Oca) e os 4 Cristais de Seiva nos 4 altares.
func _andar_7() -> void:
	for s in pontos("??"):
		peca("poco_luz", s.p)
		usar(s.p, "Olhar para o Poço da Lua", func():
			if Tempo.hora >= 20.0 or Tempo.hora < 5.0:
				marcar("poco_lua")
				Sistema.mensagem("A lua reflete-se na água e desenha um caminho de luz… até à Raiz Oca, rodeada de quatro altares.", "nivel")
			else:
				Sistema.mensagem("Água parada. De noite, com a lua, deve ser diferente."))
	var altares: Array = pontos("!!")
	# os 4 Cristais de Seiva escondidos pelo andar (um por canto)
	if not feito("altares"):
		var abertas: Array = andar.celulas_abertas()
		for k in 4:
			if abertas.is_empty():
				break
			var c: Vector2i = abertas[(k * 7919 + int(andar.numero)) % abertas.size()]
			var pc: Vector3 = andar.centro_celula(c.x, c.y) + Vector3(1.5, 0, 1.5)
			var brilho := luz(pc, Color("cddf6c"), 1.5)
			sprite("cristais_verdes" if ResourceLoader.exists(NAT + "cristais_verdes.png") else "cogumelos", pc, Color("cddf6c"))
			var kk := k
			var ref := [null]   # (a função anónima guarda o valor de agora: o Interagivel vai numa lista)
			ref[0] = usar(pc, "Apanhar o Cristal de Seiva", func():
				if Jogo.tem_flag("seg_a007_cristal_%d" % kk):
					return
				Jogo.por_flag("seg_a007_cristal_%d" % kk)
				dar("cristal_seiva")
				brilho.light_energy = 0.0
				ref[0].ativo = false)
	var postos := [0]
	for a in altares:
		sprite("menir", a.p, Color("cddf6c"))
		var la := luz(a.p, Color("cddf6c"))
		usar(a.p + Vector3(0, 0, 0.8), "Pôr um Cristal de Seiva no altar", func():
			if feito("altares") or la.light_energy > 0.0:
				return
			if not Jogo.inventario.tem("cristal_seiva"):
				Sistema.mensagem("O altar tem uma cavidade com a forma de um cristal verde.", "aviso")
				return
			Jogo.inventario.retirar("cristal_seiva")
			la.light_energy = 2.0
			postos[0] += 1
			if postos[0] >= altares.size():
				resolvido("altares", "Os quatro altares brilham e a Raiz Oca abre-se! Lá dentro há um baú.", "prata", a.p + Vector3(2, 0, 0)))


## Andar 8 — a Torre de Vigia (de dia mostra onde está a Chave das Ruínas), a chave no telhado, o baú de ouro do
## Templo e o puzzle das estátuas (levar as 4 aos pedestais à volta da praça).
func _andar_8() -> void:
	for s in pontos("??"):
		peca("torre_vigia", s.p + Vector3(0, 0, -3.0))
		usar(s.p, "Subir à Torre de Vigia", func():
			if Tempo.hora >= 7.0 and Tempo.hora < 18.0:
				Sistema.mensagem("Lá de cima vês um brilho dourado num telhado, para os lados do nascente…", "nivel")
			else:
				Sistema.mensagem("Está escuro demais para ver alguma coisa lá em baixo."))
	for s in pontos("ii"):
		if feito("chave"):
			continue
		var l := luz(s.p, Color("f9c22b"), 1.2)
		var ref := [null]
		ref[0] = usar(s.p, "Apanhar o que brilha", func():
			if feito("chave"):
				return
			marcar("chave")
			l.light_energy = 0.0
			ref[0].ativo = false
			dar("chave_ruinas"))
	for s in pontos("$$"):
		if feito("templo"):
			continue
		sprite("pilar_partido", s.p + Vector3(-1.5, 0, -1))
		sprite("pilar_partido", s.p + Vector3(1.5, 0, -1))
		usar(s.p, "Porta do Templo Enterrado", func():
			if feito("templo"):
				return
			if not Jogo.inventario.tem("chave_ruinas"):
				Sistema.mensagem("Uma porta de pedra com uma fechadura antiga. Precisa da Chave das Ruínas.", "aviso")
				return
			Jogo.inventario.retirar("chave_ruinas")
			Jogo.inventario.adicionar("chave_bau_ouro")
			resolvido("templo", "A Chave das Ruínas abre a porta do Templo!", "ouro", s.p + Vector3(0, 0, -1.5)))
	var centro: Array = pontos("!!")
	var estatuas: Array = pontos("MM")
	if centro.is_empty() or estatuas.is_empty():
		return
	var c: Vector3 = centro[0].p
	var pedestais := [c + Vector3(-4, 0, -4), c + Vector3(4, 0, -4), c + Vector3(-4, 0, 4), c + Vector3(4, 0, 4)]
	var chegaram := [0]
	for k in pedestais.size():
		sprite("pedra_3", pedestais[k])
	for k in mini(4, estatuas.size()):
		var e := peca("estatua_cavaleiro", estatuas[k].p)
		var alvo: Vector3 = chao(pedestais[k])
		var ref := [null]
		ref[0] = usar(estatuas[k].p, "Empurrar a estátua", func():
			if feito("estatuas") or e == null:
				return
			# a estátua anda 3 m para o pedestal dela (e o botão vai com ela)
			var d := alvo - e.global_position
			d.y = 0
			var passo := d.normalized() * minf(3.0, d.length())
			var novo := chao(e.global_position + passo)
			create_tween().tween_property(e, "global_position", novo, 0.4)
			ref[0].global_position = novo
			if novo.distance_to(alvo) < 0.5:
				ref[0].ativo = false
				chegaram[0] += 1
				Sistema.mensagem("A estátua encaixa no pedestal com um «clonc».")
				if chegaram[0] >= mini(4, estatuas.size()):
					resolvido("estatuas", "As quatro estátuas estão nos pedestais! O chão da praça abre-se: um baú!", "prata", c)
			)


## Andar 9 — a ilha que só aparece às 3:00 (Altar do Reflexo) e os 3 sinos de barco (tocá-los no mesmo minuto).
func _andar_9() -> void:
	for s in pontos("??"):
		usar(s.p, "Altar do Reflexo", func():
			if not (Tempo.hora >= 2.5 and Tempo.hora < 3.5):
				Sistema.mensagem("Só nevoeiro e água… Os fogos-fátuos dançam aqui de madrugada, por volta das 3:00.")
				return
			if feito("ilha"):
				Sistema.mensagem("O altar reflete o teu rosto. Ou quase.")
				return
			marcar("ilha")
			Sistema.mensagem("Às 3:00 a ilha aparece, e o Altar do Reflexo mostra-te uma memória que não é tua…", "nivel")
			dar("amuleto_nevoa"))
	var sinos: Array = pontos("!!")
	for k in sinos.size():
		var s: Dictionary = sinos[k]
		peca("sino_barco", s.p)
		letreiro(s.p, "Sino %d" % (k + 1), Color("c7dcd0"))
		var kk := k
		usar(s.p + Vector3(0, 0, 0.7), "Tocar o sino", func():
			if feito("sinos"):
				Sistema.mensagem("Dlim… O templo já está aberto.")
				return
			Sistema.mensagem("DLIM! (sino %d)" % (kk + 1))
			if _sinos.is_empty():
				_t_sinos = 60.0
			_sinos[kk] = true
			if _sinos.size() >= sinos.size():
				_t_sinos = 0.0
				resolvido("sinos", "Os três sinos ecoam juntos sobre o lago… O templo da Ilha Central abre-se!", "prata", s.p + Vector3(2, 0, 0)))


# ------------------------------------------------------------------ Região 2 — Cavernas ------------------------------------------------------------------

## Andar 11 — o carril tapado com tábuas (martelo ou machado) e o vagão perdido; as Agulhas dos carris (4 alavancas).
func _andar_11() -> void:
	for s in pontos("??"):
		var tabuas := sprite("cerca", s.p, Color("966c6c"))
		usar(s.p + Vector3(0, 0, 0.8), "Tábuas pregadas no carril", func():
			if feito("tabuas"):
				return
			if not arma_tipo() in ["martelo", "machado"] and not Jogo.inventario.tem("machado_lenhador_cobre"):
				Sistema.mensagem("As tábuas estão bem pregadas. Com um martelo ou um machado partiam-se…", "aviso")
				return
			if tabuas:
				tabuas.visible = false
			resolvido("tabuas", "CRAC! As tábuas partem-se e o carril leva a um vagão perdido.", "prata"))
	for s in pontos("!!"):
		var certa := []
		for k in 4:
			certa.append(randi() % 2)
		var setas := ["⇐", "⇒"]
		sprite("placa", s.p + Vector3(-3.0, 0, 1.0))
		usar(s.p + Vector3(-3.0, 0, 1.6), "Ler o mapa dos carris", func():
			var t := ""
			for k in 4:
				t += "%s " % setas[certa[k]]
			Sistema.mensagem("Mapa riscado a giz: «Agulhas para o elevador: %s»" % t.strip_edges()))
		peca("elevador_de_mina", s.p + Vector3(4.0, 0, -2.0))
		var vag := peca("vagoneta", s.p + Vector3(-4.0, 0, -2.0), PI / 2.0)
		if feito("agulhas") and vag:
			vag.global_position = chao(s.p + Vector3(4.0, 0, 0))
		var estado := [0, 0, 0, 0]
		for k in 4:
			var pa: Vector3 = s.p + Vector3((k - 1.5) * 2.0, 0, 0)
			var l := letreiro(pa, "Alavanca %d: %s" % [k + 1, setas[0]], Color("c7dcd0"))
			sprite("pilar_partido", pa, Color("9babb2"))
			var kk := k
			usar(pa + Vector3(0, 0, 0.8), "Puxar a alavanca %d" % (k + 1), func():
				if feito("agulhas"):
					return
				estado[kk] = 1 - estado[kk]
				l.text = "Alavanca %d: %s" % [kk + 1, setas[estado[kk]]]
				if estado == certa:
					if vag:
						create_tween().tween_property(vag, "global_position", chao(s.p + Vector3(4.0, 0, 0)), 2.5).set_trans(Tween.TRANS_SINE)
					resolvido("agulhas", "As agulhas estalam e a vagoneta de minério desce até ao elevador! Lá está a carga dela.", "prata", s.p + Vector3(4.0, 0, 0)))


## Andar 12 — as portas que os goblins abrem e fecham, os 3 diários (cada um com um número) e o cofre do capataz.
func _andar_12() -> void:
	for d in pontos("[]"):   # portas de madeira: abrem e fecham sozinhas (o labirinto muda)
		var porta := peca("porta_de_madeira_de_mina", d.p)
		var t := create_tween().set_loops()
		t.tween_interval(randf_range(8.0, 14.0))
		t.tween_callback(func():
			if is_instance_valid(porta):
				porta.visible = not porta.visible
				for c in porta.find_children("*", "CollisionShape3D", true, false):
					c.disabled = not porta.visible)
	var codigo := [randi() % 10, randi() % 10, randi() % 10]
	var abertas: Array = andar.celulas_abertas()
	for k in 3:
		if abertas.is_empty():
			break
		var c: Vector2i = abertas[(k * 104729 + 7) % abertas.size()]
		var pd: Vector3 = andar.centro_celula(c.x, c.y) + Vector3(-1.5, 0, 1.0)
		peca("mesa_de_mineiro", pd)
		var kk := k
		usar(pd + Vector3(0, 0, 1.0), "Ler o diário do mineiro", func():
			Sistema.mensagem("Diário de mineiro nº %d: «…e o número que me calhou para o cofre foi o %d. Não contem a ninguém.»" % [kk + 1, codigo[kk]]))
	for s in pontos("$$"):
		sprite("caixote", s.p, Color("7f708a"))
		usar(s.p + Vector3(0, 0, 0.8), "Cofre do capataz", func():
			if feito("cofre"):
				Sistema.mensagem("O cofre está vazio.")
				return
			var escolha := []
			for k in 3:
				var i: int = await escolher(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
				if i < 0:
					return
				escolha.append(i)
			if escolha == codigo:
				dar("picareta_ferro")
				resolvido("cofre", "Clic-clic-clic… O cofre abre-se! Uma Picareta de Ferro e um baú do capataz.", "ouro", s.p + Vector3(1.5, 0, 0))
				Jogo.inventario.adicionar("chave_bau_ouro")
			else:
				Sistema.mensagem("O cofre não se mexe. Os números estão nos diários dos mineiros…", "aviso"))


## Andar 13 — os cristais de cor (a luz da sala muda), a luz violeta (vermelho + azul) e a Ponte de Quartzo.
func _andar_13() -> void:
	var cores := {"vermelho": Color("ea4f36"), "azul": Color("4d9be6"), "amarelo": Color("f9c22b"), "violeta": Color("a884f3")}
	var luz_sala := luz(andar.ponto_seguro, Color.WHITE, 0.0)
	luz_sala.omni_range = 60.0
	var atual := [""]
	for s in pontos("??"):   # dois cristais lado a lado
		var ultimo := {"vermelho": -10.0, "azul": -10.0}
		for k in 2:
			var cor: String = ["vermelho", "azul"][k]
			var pc: Vector3 = s.p + Vector3((k - 0.5) * 2.4, 0, 0)
			peca("cristal_interruptor", pc)
			letreiro(pc, cor, cores[cor])
			usar(pc + Vector3(0, 0, 0.8), "Bater no cristal %s" % cor, func():
				ultimo[cor] = Time.get_ticks_msec() / 1000.0
				atual[0] = cor
				luz_sala.light_color = cores[cor]
				luz_sala.light_energy = 1.5
				if absf(ultimo["vermelho"] - ultimo["azul"]) < 1.5:   # os dois quase ao mesmo tempo
					atual[0] = "violeta"
					luz_sala.light_color = cores["violeta"]
					if not feito("violeta"):
						marcar("violeta")
						Sistema.mensagem("Vermelho e azul juntos… luz violeta! Na parede aparece a Sala Violeta.", "nivel")
						dar("ametista_grande"))
	for s in pontos("!!"):   # a ponte: cada parte só existe com a cor certa
		peca("ponte_de_quartzo", s.p)
		var partes := ["amarelo", "vermelho", "azul"]
		var passo := [0]
		var amarelo: Vector3 = s.p + Vector3(-3.0, 0, 2.0)
		peca("cristal_interruptor", amarelo)
		letreiro(amarelo, "amarelo", cores["amarelo"])
		usar(amarelo + Vector3(0, 0, 0.8), "Bater no cristal amarelo", func():
			atual[0] = "amarelo"
			luz_sala.light_color = cores["amarelo"]
			luz_sala.light_energy = 1.5)
		usar(s.p + Vector3(0, 0, 1.2), "Pisar a Ponte de Quartzo", func():
			if feito("ponte"):
				Sistema.mensagem("Já atravessaste a ponte.")
				return
			var precisa: String = partes[passo[0]]
			if atual[0] != precisa:
				passo[0] = 0
				Sistema.mensagem("A parte seguinte da ponte é %s e não se vê com esta luz! Voltas ao princípio." % precisa, "aviso")
				return
			passo[0] += 1
			if passo[0] >= partes.size():
				resolvido("ponte", "Atravessaste a Ponte de Quartzo a mudar a luz no momento certo!", "prata", s.p + Vector3(0, 0, -3.0))
			else:
				Sistema.mensagem("Passaste a parte %s. A seguinte é %s." % [precisa, partes[passo[0]]]))


## Andar 14 — as 3 boias de luz (1-2-3 abre a eclusa para a Ilha dos Ossos) e a gruta atrás da Cascata Escura.
func _andar_14() -> void:
	var boias: Array = pontos("!!")
	var ordem := []
	for k in boias.size():   # o número vem do texto ("Boia de luz nº 2")
		var m := RegEx.create_from_string("nº (\\d)").search(boias[k].texto)
		ordem.append(int(m.get_string(1)) - 1 if m else k)
	var luzes := []
	for k in boias.size():
		var b: Dictionary = boias[k]
		peca("boia_de_luz", b.p)
		var l := luz(b.p, Color("8fd3ff"))
		luzes.append(l)
		var n: int = ordem[k]
		usar(b.p + Vector3(0, 0, 1.0), "Acender a boia nº %d" % (n + 1), func():
			l.light_energy = 2.0
			carregar_ordem(n, [0, 1, 2], "boias", func():
				resolvido("boias", "As três boias brilham e a eclusa abre-se! A água desce até à Ilha dos Ossos.")
				andar.baixar_agua(),
				func():
					for x in luzes:
						x.light_energy = 0.0))
	if feito("boias"):
		andar.baixar_agua.call_deferred()
	for s in pontos("??"):
		peca("cascata_escura", s.p + Vector3(0, 0, -3.0))
		usar(s.p, "Entrar atrás da Cascata Escura", func():
			if feito("cascata"):
				Sistema.mensagem("Só água e o eco dos teus passos.")
				return
			dar("remo_dourado")
			var b: Array = pontos("$$")
			resolvido("cascata", "Atrás da cascata há uma gruta seca, com um Remo Dourado e um baú!", "prata", s.p + Vector3(1.5, 0, -1.0)))


## Andar 15 — o casulo dourado (ovo de Aranha de Seda) e 3 casulos com aventureiros presos para resgatar.
func _andar_15() -> void:
	for s in pontos("$$"):
		sprite("cogumelo_gigante", s.p, Color("f9c22b"))
		usar(s.p + Vector3(0, 0, 0.8), "Abrir o casulo dourado", func():
			if feito("casulo"):
				return
			marcar("casulo")
			Sistema.mensagem("Dentro do casulo dourado há um ovo a brilhar. O Zed sabia chocá-lo…", "nivel")
			dar("ovo_aranha_dourado"))
	var abertas: Array = andar.celulas_abertas()
	for k in 3:
		if abertas.is_empty() or feito("resgate_%d" % k):
			continue
		var c: Vector2i = abertas[(k * 7907 + 3) % abertas.size()]
		var pc: Vector3 = andar.centro_celula(c.x, c.y)
		var casulo := peca("casulos", pc)
		var kk := k
		var ref := [null]
		ref[0] = usar(pc + Vector3(0, 0, 1.0), "Cortar o casulo", func():
			if feito("resgate_%d" % kk):
				return
			marcar("resgate_%d" % kk)
			ref[0].ativo = false
			if casulo:
				casulo.visible = false
			Jogo.ganhar_ouro(150)
			Sistema.mensagem(["«Obrigado! Pensei que ia virar jantar de aranha!» (+150 ouro)", "«Estou livre! Conta à Guilda que a Rosa do rank E está viva!» (+150 ouro)",
					"«Ufa… Há horas que estava a contar teias.» (+150 ouro)"][kk], "nivel"))


## Andar 16 — a Pérola Azul no fundo do lago (Poção de Respirar) e o Coro dos fungos (repetir a melodia do Ancião).
func _andar_16() -> void:
	for s in pontos("??"):
		peca("lago_luminoso", s.p)
		usar(s.p + Vector3(0, 0, 2.0), "Mergulhar no Lago Bioluminescente", func():
			if feito("perola"):
				Sistema.mensagem("A água brilha, mas lá em baixo já não há nada.")
				return
			if not Jogo.inventario.tem("pocao_respirar"):
				Sistema.mensagem("É fundo demais para ires sem respirar. Uma Poção de Respirar ajudava.", "aviso")
				return
			Jogo.inventario.retirar("pocao_respirar")
			marcar("perola")
			dar("perola"))
	var notas := ["Dó", "Ré", "Mi", "Fá", "Sol"]
	for s in pontos("!!"):
		var melodia := []
		for k in 5:
			melodia.append(randi() % 5)
		sprite("cogumelo_luz_3", s.p + Vector3(0, 0, -3.0), Color("fbff86"))
		usar(s.p + Vector3(0, 0, -2.2), "Ouvir o Ancião do coro", func():
			var t := []
			for n in melodia:
				t.append(notas[n])
			Sistema.mensagem("O fungo ancião canta: «%s»" % " – ".join(t)))
		for k in 5:
			var ang := PI + k * PI / 4.0
			var pf: Vector3 = s.p + Vector3(cos(ang) * 3.5, 0, sin(ang) * 3.5 + 1.0)
			sprite("cogumelo_luz_%d" % (k % 3 + 1), pf, Color.from_hsv(k / 5.0, 0.5, 1.0))
			letreiro(pf, notas[k], Color.from_hsv(k / 5.0, 0.4, 1.0))
			var kk := k
			usar(pf + Vector3(0, 0, 0.7), "Tocar no fungo (%s)" % notas[k], func():
				Sistema.mensagem("♪ %s" % notas[kk])
				carregar_ordem(kk, melodia, "coro", func():
					resolvido("coro", "Os cinco fungos cantam a melodia inteira! O ancião ri-se e oferece-te um baú.", "prata", s.p + Vector3(0, 0, 2.5))))


## Andar 17 — os pontos de eco (gritar mostra as plataformas; os dois pela ordem levam à sala do Gancho) e o ninho
## na parede (só com o Gancho): ovo do Morceguinho.
func _andar_17() -> void:
	var ecos: Array = pontos("!!")
	for k in ecos.size():
		var e: Dictionary = ecos[k]
		peca("ponto_de_eco", e.p)
		var kk := k
		usar(e.p + Vector3(0, 0, 0.9), "Gritar no ponto de eco", func():
			Sistema.mensagem("«ÔÔÔ!» … ÔÔÔ… ôôô… (por uns segundos vês plataformas no ar)")
			carregar_ordem(kk, range(ecos.size()), "ecos", func():
				dar("gancho")
				resolvido("ecos", "Seguiste as plataformas invisíveis pela parede norte até à sala do Gancho!")))
	for s in pontos("??"):
		peca("ninho_de_morcego", s.p)
		usar(s.p + Vector3(0, 0, 0.8), "Ninho na parede", func():
			if feito("ninho"):
				return
			if not Jogo.inventario.tem("gancho"):
				Sistema.mensagem("O ninho está alto demais na parede. Com um gancho chegavas lá.", "aviso")
				return
			marcar("ninho")
			Sistema.mensagem("Atiras o Gancho, sobes… e lá está um ovo pequenino e quente.", "nivel")
			dar("ovo_morceguinho"))


## Andar 18 — reacender as 3 fornalhas (Carvão: aparecem os fantasmas anões) e as Runas do portão (formar B·R·O·M):
## abre o portão com o Livro de Runas Anãs.
func _andar_18() -> void:
	var fornalhas: Array = pontos("FF").slice(0, 3)
	var acesas := [0]
	for k in fornalhas.size():
		var f: Dictionary = fornalhas[k]
		peca("fornalha_ana", f.p)
		var l := luz(f.p, Color("f79617"), 2.0 if feito("fornalhas") else 0.0)
		var kk := k
		usar(f.p + Vector3(0, 0, 1.2), "Acender a fornalha", func():
			if feito("fornalhas") or Jogo.tem_flag("seg_a018_forno_%d" % kk):
				return
			if not Jogo.inventario.tem("carvao"):
				Sistema.mensagem("A fornalha está fria. Precisa de Carvão.", "aviso")
				return
			Jogo.inventario.retirar("carvao")
			Jogo.por_flag("seg_a018_forno_%d" % kk)
			l.light_energy = 2.0
			acesas[0] += 1
			if acesas[0] >= fornalhas.size():
				resolvido("fornalhas", "As três fornalhas rugem! O salão ilumina-se… e aparecem os fantasmas dos anões, a trabalhar."))
	var letras := ["A", "B", "M", "O", "R", "T", "U"]
	for s in pontos("!!"):
		peca("portao_com_aneis_de_runas", s.p + Vector3(0, 0, -2.5))
		var aneis := [0, 0, 0, 0]
		var placas := []
		for k in 4:
			var pa: Vector3 = s.p + Vector3((k - 1.5) * 1.6, 0, 0.5)
			placas.append(letreiro(pa, letras[0], Color("f9c22b")))
			var kk := k
			usar(pa + Vector3(0, 0, 0.6), "Rodar o anel %d" % (k + 1), func():
				if feito("runas"):
					return
				aneis[kk] = (aneis[kk] + 1) % letras.size()
				placas[kk].text = letras[aneis[kk]]
				var palavra := ""
				for a in aneis:
					palavra += letras[a]
				if palavra == "BROM":
					Historia.acontecer("Grande Portão Anão")   # cena C2-07 (docs/guiao/cap02_cavernas.md)
					resolvido("runas", "B·R·O·M… O Grande Portão Anão abre-se com um rugido de pedra!", "ouro", s.p + Vector3(0, 0, -1.0))
					dar("livro_runas_anas")
					Jogo.inventario.adicionar("chave_bau_ouro"))
	for s in pontos("??"):
		usar(s.p, "Escadas por baixo do Salão das Forjas", func():
			if feito("runas"):
				Sistema.mensagem("Uma escada desce para a escuridão: a Mina do Rei Anão. (Masmorra: em breve)")
			else:
				Sistema.mensagem("Uma grade de ferro tapa a escada. Do outro lado do portão das runas deve haver forma de a abrir."))


## Andar 19 — as 3 fendas que o reflexo aponta (baús de prata) e os Espelhos (rodar 4 estalagmites até ao altar).
func _andar_19() -> void:
	for k in pontos("??").size():
		var s: Dictionary = pontos("??")[k]
		var kk := k
		usar(s.p, "Olhar para o reflexo no cristal", func():
			if feito("fenda_%d" % kk):
				Sistema.mensagem("O teu reflexo imita-te direitinho.")
				return
			resolvido("fenda_%d" % kk, "O teu reflexo aponta para o chão… e ali há uma fenda com um baú!", "prata", s.p + Vector3(1.2, 0, 0)))
	var espelhos: Array = pontos("()")
	var altar: Array = pontos("!!")
	if altar.is_empty():
		return
	peca("altar_do_reflexo", altar[0].p)
	var certa := []
	var estado := []
	var nomes := ["norte", "este", "sul", "oeste"]
	for k in espelhos.size():
		certa.append(randi() % 4)
		estado.append(0)
	for k in espelhos.size():
		var e: Dictionary = espelhos[k]
		var est := peca("estalagmite_espelhada", e.p)
		var kk := k
		usar(e.p + Vector3(0, 0, 0.9), "Rodar a estalagmite espelhada", func():
			if feito("espelhos"):
				return
			estado[kk] = (estado[kk] + 1) % 4
			if est:
				create_tween().tween_property(est, "rotation:y", est.rotation.y + PI / 2.0, 0.3)
			if estado[kk] == certa[kk]:
				Sistema.mensagem("A luz bate no espelho e salta para o seguinte!")
			if estado == certa:
				resolvido("espelhos", "A luz do teu cristal salta de espelho em espelho até ao Altar do Reflexo!", "prata", altar[0].p + Vector3(2.0, 0, 0)))
	usar(altar[0].p + Vector3(0, 0, 1.2), "Altar do Reflexo", func():
		if feito("espelhos"):
			Sistema.mensagem("O altar brilha com a tua luz.")
			return
		var dicas := []
		for k in espelhos.size():
			dicas.append("%d: %s" % [k + 1, nomes[certa[k]]])
		Sistema.mensagem("Gravado no altar: «Os espelhos olham para… %s»" % " · ".join(dicas)))


# ------------------------------------------------------------------ Região 3 — Pântano e Selva ------------------------------------------------------------------

## Uma célula aberta ao acaso (sempre a mesma para o mesmo k neste andar).
func aberta(k: int) -> Vector3:
	var a: Array = andar.celulas_abertas()
	if a.is_empty():
		return andar.ponto_seguro
	var c: Vector2i = a[(k * 7919 + int(andar.numero) * 31) % a.size()]
	return andar.centro_celula(c.x, c.y)


## Andar 21 — o alçapão da cabana (Cana de Mangue e o diário do pescador) e o passadiço partido (5 tábuas dos caixotes).
func _andar_21() -> void:
	for s in pontos("??"):
		usar(s.p, "Alçapão da cabana do pescador", func():
			if feito("alcapao"):
				Sistema.mensagem("O alçapão já está aberto. Só cheira a peixe.")
				return
			marcar("alcapao")
			Sistema.mensagem("Debaixo das tábuas do chão: uma cana de pesca boa e um caderno molhado.", "nivel")
			dar("cana_mangue")
			dar("diario_pescador"))
	var tabuas := [int(Jogo.contadores.get("a021_tabuas", 0))]
	for k in 5:
		if Jogo.tem_flag("seg_a021_caixote_%d" % k):
			continue
		var pc := aberta(k + 3)
		var cx := peca("caixotes", pc)
		var kk := k
		var ref := [null]
		ref[0] = usar(pc + Vector3(0, 0, 1.0), "Partir o caixote", func():
			Jogo.por_flag("seg_a021_caixote_%d" % kk)
			ref[0].ativo = false
			if cx:
				cx.visible = false
			tabuas[0] += 1
			Jogo.contadores["a021_tabuas"] = tabuas[0]
			Sistema.mensagem("CRAC! Apanhaste uma tábua (%d/5)." % tabuas[0]))
	var pontes: Array = pontos("!!")
	if pontes.is_empty():
		return
	var ponte := peca("passadico", pontes[0].p)
	if ponte and not feito("passadico"):
		ponte.visible = false
	usar(pontes[0].p + Vector3(0, 0, 1.2), "Passadiço partido", func():
		if feito("passadico"):
			Sistema.mensagem("O passadiço aguenta-se. Mais ou menos.")
			return
		if tabuas[0] < 5:
			Sistema.mensagem("Faltam tábuas: tens %d de 5. Os caixotes velhos do pântano têm madeira boa." % tabuas[0], "aviso")
			return
		if ponte:
			ponte.visible = true
		resolvido("passadico", "Pregaste as 5 tábuas: o passadiço chega à ilhota de lama!", "prata"))


## Andar 22 — o livro da bruxa (receita da Poção Purificadora e a rima do caldeirão), o caldeirão e os lírios brancos.
func _andar_22() -> void:
	var ingredientes := ["Olho de Sapo", "Raiz Torta", "Pó de Lírio", "Escama de Lagarto", "Lodo Verde"]
	var ordem := [1, 4, 0]
	var rima := "«Primeiro a raiz que nunca se endireita, / depois o lodo que no fundo se deita, / e no fim o olho que tudo espreita.»"
	for s in pontos("??"):
		peca("casa_torta_da_bruxa", s.p + Vector3(0, 0, -3.0))
		usar(s.p, "Livro da bruxa", func():
			if not feito("livro"):
				marcar("livro")
				Jogo.aprender_receita("pocao_purificadora")
			Sistema.mensagem("Receita da Poção Purificadora. Na última página, uma rima: " + rima))
	for s in pontos("!!"):
		peca("caldeirao", s.p)
		usar(s.p + Vector3(0, 0, 1.2), "Mexer o caldeirão", func():
			if feito("caldeirao"):
				Sistema.mensagem("O caldeirão borbulha, contente.")
				return
			var feitas := []
			for k in 3:
				var i: int = await escolher(ingredientes)
				if i < 0:
					return
				feitas.append(i)
			if feitas == ordem:
				resolvido("caldeirao", "PUF! Um fumo verde… e o chão ao lado do caldeirão abre-se: a cave da bruxa!", "ouro", s.p + Vector3(1.8, 0, 0))
				Jogo.inventario.adicionar("chave_bau_ouro")
			else:
				Sistema.mensagem("BLURP. Sai um cheiro horrível. A ordem não era essa (o livro da bruxa tem uma rima).", "aviso"))
	for s in pontos("FF"):
		var lirio := peca("lirio_branco", s.p)
		var l := luz(s.p, Color("c7dcd0"))
		usar(s.p + Vector3(0, 0, 0.8), "Bater no Lírio Branco", func():
			l.light_energy = 1.5
			Jogo.buffs["agua_limpa"] = [1.0, 20.0]
			Sistema.mensagem("O lírio abre-se e a água à volta fica limpa durante 20 s.")
			if lirio:
				create_tween().tween_property(lirio, "scale", Vector3.ONE * 1.15, 0.2).set_trans(Tween.TRANS_BACK)
			get_tree().create_timer(20.0).timeout.connect(func():
				l.light_energy = 0.0
				if is_instance_valid(lirio):
					lirio.scale = Vector3.ONE))


## Andar 23 — o mural e as 4 pedras dos animais (pela ordem do mural abre a escadaria escondida: Ídolo de Jade).
func _andar_23() -> void:
	var pedras: Array = pontos("!!")
	if pedras.is_empty():
		return
	var animais := []
	for p in pedras:
		var t: String = String(p.texto).to_lower()
		animais.append(t.trim_prefix("pedra do ").trim_prefix("pedra da "))
	var certa := range(pedras.size())
	certa.shuffle()
	var mural: Vector3 = pedras[0].p + Vector3(-4.0, 0, -3.0)
	peca("mural", mural)
	usar(mural + Vector3(0, 0, 1.2), "Olhar para o mural", func():
		var t := []
		for i in certa:
			t.append(animais[i])
		Sistema.mensagem("O mural mostra animais em fila, a caminhar: %s." % " → ".join(t)))
	for k in pedras.size():
		peca("pedras_com_animais", pedras[k].p)
		var kk := k
		usar(pedras[k].p + Vector3(0, 0, 1.0), "Carregar na pedra do %s" % animais[k], func():
			carregar_ordem(kk, certa, "animais", func():
				resolvido("animais", "As quatro pedras afundam-se e as vinhas abrem-se: uma escadaria escondida!")))
	for s in pontos("??"):
		usar(s.p, "Escadaria atrás das vinhas", func():
			if not feito("animais"):
				Sistema.mensagem("Só vinhas grossas. Há uma pedra solta por trás… mas não se mexe.")
				return
			if feito("idolo"):
				Sistema.mensagem("A escadaria desce para o Santuário do Jaguar.")
				return
			marcar("idolo")
			Sistema.mensagem("No fundo da escadaria, num pedestal: um ídolo verde que brilha.", "nivel")
			dar("idolo_jade"))


## Andar 24 — a Escama do Primeiro Rei no fundo da Lagoa Sagrada e as 3 canoas que fazem a ponte.
func _andar_24() -> void:
	for s in pontos("??"):
		usar(s.p, "Mergulhar na Lagoa Sagrada", func():
			if feito("escama"):
				Sistema.mensagem("A lagoa está calma. Os peixes olham para ti.")
				return
			if not Jogo.inventario.tem("pocao_respirar"):
				Sistema.mensagem("É funda demais. Com uma Poção de Respirar chegavas ao fundo.", "aviso")
				return
			Jogo.inventario.retirar("pocao_respirar")
			marcar("escama")
			Sistema.mensagem("No fundo, entre ossos antigos, uma escama enorme e dourada.", "nivel")
			dar("escama_primeiro_rei"))
	var postas := [0]
	for k in 3:
		var pc := aberta(k + 11)
		var c := peca("canoa", pc)
		var kk := k
		var ref := [null]
		ref[0] = usar(pc + Vector3(0, 0, 1.2), "Empurrar a canoa para a margem", func():
			if feito("canoa_%d" % kk):
				return
			if Missoes.estado("H_08") == "ativa" and Jogo.tem_flag("lagartos_inimigos"):
				Sistema.mensagem("Os Homens-Lagarto não te deixam mexer nas canoas deles.", "aviso")
				return
			marcar("canoa_%d" % kk)
			ref[0].ativo = false
			postas[0] += 1
			if c:
				create_tween().tween_property(c, "global_position", c.global_position + Vector3(0, 0, -4.0), 1.5)
			if postas[0] >= 3:
				resolvido("canoas", "As três canoas lado a lado fazem uma ponte até ao outro lado da lagoa!", "prata", pc + Vector3(2.0, 0, -5.0))
			else:
				Sistema.mensagem("Canoa na margem (%d/3)." % postas[0]))
		if feito("canoa_%d" % k):
			postas[0] += 1
			ref[0].ativo = false


## Andar 25 — as 4 alavancas da água do Templo Afundado: a da sala norte baixa a água e mostra a porta do Anel da Serpente.
func _andar_25() -> void:
	var alavancas: Array = pontos("!!")
	for k in alavancas.size():
		var a: Dictionary = alavancas[k]
		var no := peca("alavanca_de_agua", a.p)
		var norte: bool = "norte" in String(a.texto)
		var kk := k
		usar(a.p + Vector3(0, 0, 0.9), "Puxar a alavanca da água", func():
			if no:
				create_tween().tween_property(no, "rotation:z", 0.6 if no.rotation.z < 0.3 else 0.0, 0.3)
			if norte:
				if feito("agua_norte"):
					Sistema.mensagem("A água da sala norte já está em baixo.")
					return
				andar.baixar_agua()
				resolvido("agua_norte", "Um ronco nos canos… a água da sala norte desce e aparece uma porta na parede!", "prata")
			else:
				Sistema.mensagem(["A água sobe na sala este.", "A água desce na sala oeste… e volta a subir.", "Ouves água a correr no corredor."][kk % 3]))
	if feito("agua_norte"):
		andar.baixar_agua.call_deferred()
	for s in pontos("??"):
		usar(s.p, "Porta escondida da sala norte", func():
			if not feito("agua_norte"):
				Sistema.mensagem("Só se vê água turva. Há qualquer coisa lá no fundo…")
				return
			if feito("anel"):
				return
			marcar("anel")
			Sistema.mensagem("Atrás da porta, numa estátua de serpente: um anel enrolado como uma cobra.", "nivel")
			dar("anel_serpente"))


## Andar 26 — o barco afundado (só na maré baixa da madrugada: baú de ouro) e as 3 comportas de raízes.
func _andar_26() -> void:
	for s in pontos("??"):
		var barco := peca("barco_afundado", s.p)
		usar(s.p + Vector3(0, 0, 1.4), "Barco afundado", func():
			if feito("barco"):
				Sistema.mensagem("O barco está vazio. Um caranguejo mudou-se para lá.")
				return
			if not (Tempo.hora >= 3.0 and Tempo.hora < 6.0):
				Sistema.mensagem("A maré está alta: só se vê a ponta do mastro. Na maré baixa da madrugada (3:00–6:00) chegava-se lá.", "aviso")
				return
			resolvido("barco", "Maré baixa! Entras no barco afundado: um baú de ouro, ainda fechado!", "ouro", s.p + Vector3(1.5, 0, 0))
			Jogo.inventario.adicionar("chave_bau_ouro"))
	var comportas: Array = pontos("!!")
	for k in comportas.size():
		var c: Dictionary = comportas[k]
		peca("comporta_de_raizes", c.p)
		var kk := k
		usar(c.p + Vector3(0, 0, 1.0), "Abrir a comporta de raízes %d" % (k + 1), func():
			carregar_ordem(kk, range(comportas.size()), "comportas", func():
				resolvido("comportas", "A água entra pelas três comportas e o canal seco enche-se: já se passa de barco!", "prata")))


## Andar 27 — o arco-íris do meio-dia (12:00–14:00 com sol) mostra o símbolo da 6.ª gruta: a Fonte Esmeralda (+5% HP
## máximo, uma vez); e as pedras flutuantes que afundam ao ritmo das cascatas.
func _andar_27() -> void:
	var grutas: Array = pontos("HH")
	var g := 1 + int(andar.numero) % 5
	for s in pontos("??"):
		var arco := letreiro(s.p + Vector3(0, 1.5, -2.0), "", Color("fbff86"))
		var ver := func():
			var sol: bool = String(Tempo.clima(0).get("efeito", "sol")) == "sol"
			arco.text = ("☀ o arco-íris desenha o número %d na rocha" % g) if (Tempo.hora >= 12.0 and Tempo.hora < 14.0 and sol) else ""
		ver.call()
		var t := create_tween().set_loops()
		t.tween_interval(5.0)
		t.tween_callback(ver)
		peca("gruta_atras_de_cascata", s.p + Vector3(0, 0, -2.5))
		usar(s.p, "Entrar atrás da cascata", func():
			if feito("fonte"):
				Sistema.mensagem("A Fonte Esmeralda já não brilha para ti. Bebeste a tua parte.")
				return
			if not arco.text.is_empty() or Jogo.tem_flag("seg_a027_simbolo"):
				Jogo.por_flag("seg_a027_simbolo")
				marcar("fonte")
				Jogo.hp = Jogo.hp_maximo()
				Sistema.mensagem("A 6.ª gruta! A Fonte Esmeralda: bebes e sentes-te mais forte. (+5% HP máximo para sempre)", "nivel")
				Eventos.stats_mudaram.emit()
			else:
				Sistema.mensagem("Atrás da água só há rocha molhada. Dizem que o arco-íris do meio-dia mostra o caminho.", "aviso"))
	var pedras: Array = pontos("!!")
	for k in pedras.size():
		var pd := peca("pedra_flutuante", pedras[k].p)
		if pd:   # afundam e voltam ao ritmo das cascatas
			var t := create_tween().set_loops()
			t.tween_interval(1.0 + k * 0.4)
			t.tween_property(pd, "position:y", pd.position.y - 0.6, 0.6)
			t.tween_interval(1.2)
			t.tween_property(pd, "position:y", pd.position.y, 0.6)
		var kk := k
		usar(pedras[k].p + Vector3(0, 0, 0.9), "Saltar para a pedra %d" % (k + 1), func():
			if pd and pd.position.y < pedras[kk].p.y - 0.2:
				_ordem.clear()
				Sistema.mensagem("SPLASH! A pedra estava afundada. Volta ao princípio e espera que suba.", "aviso")
				return
			carregar_ordem(kk, range(pedras.size()), "pedras", func():
				resolvido("pedras", "Saltaste as pedras todas ao ritmo das cascatas!", "prata", pedras[pedras.size() - 1].p + Vector3(1.5, 0, 0))))
	for k in grutas.size():
		var h: Dictionary = grutas[k]
		usar(h.p, "Gruta atrás da cascata %d" % (k + 1), func():
			Sistema.mensagem(String(h.texto)))


## Andar 28 — as 3 plataformas giratórias (ligar as pontes até ao ninho) e o ovo de pássaro gigante (devolver ao ninho certo).
func _andar_28() -> void:
	var plats: Array = pontos("!!")
	var certa := []
	var estado := []
	for k in plats.size():
		certa.append((k * 3 + 1) % 4)
		estado.append(0)
	for k in plats.size():
		var no := peca("plataforma_giratoria", plats[k].p)
		var kk := k
		usar(plats[k].p + Vector3(0, 0, 1.0), "Rodar a plataforma %d" % (k + 1), func():
			if feito("pontes"):
				return
			estado[kk] = (estado[kk] + 1) % 4
			if no:
				create_tween().tween_property(no, "rotation:y", no.rotation.y + PI / 2.0, 0.4)
			Sistema.mensagem("A ponte da plataforma %d aponta para %s." % [kk + 1, ["norte", "este", "sul", "oeste"][estado[kk]]])
			if estado == certa:
				resolvido("pontes", "As três pontes ligam-se! Chega-se ao Ninho Gigante pelas copas.", "prata"))
	var ninhos := []
	for k in 3:
		var pn := aberta(k + 21)
		peca("ninho_gigante", pn)
		ninhos.append(pn)
		var kk := k
		usar(pn + Vector3(0, 0, 1.5), "Ninho gigante %d" % (k + 1), func():
			if feito("ovo"):
				Sistema.mensagem("A mãe pássaro olha para ti com carinho.")
				return
			if not Jogo.inventario.tem("ovo_passaro_gigante"):
				Sistema.mensagem(["Penas azuis no ninho… e nenhum ovo.", "Um ninho vazio, com penas castanhas.", "Restos de cascas e penas verdes."][kk])
				return
			if kk != 0:
				Sistema.mensagem("A mãe deste ninho não quer o ovo. As penas não são da mesma cor…", "aviso")
				return
			Jogo.inventario.retirar("ovo_passaro_gigante")
			marcar("ovo")
			Sistema.mensagem("A mãe pássaro aconchega o ovo e larga uma pena com todas as cores.", "nivel")
			dar("pena_arco_iris"))
	for s in pontos("ii"):
		var ref := [null]
		var spr := sprite("pedra_1", s.p, Color("8fd3ff"))   # (o ovo azul, pousado no chão)
		ref[0] = usar(s.p + Vector3(0, 0, 0.6), "Apanhar o ovo azul", func():
			if feito("ovo") or Jogo.inventario.tem("ovo_passaro_gigante"):
				return
			dar("ovo_passaro_gigante")
			Sistema.mensagem("Um ovo azul enorme, com pintas. Caiu de algum ninho…")
			ref[0].ativo = false
			if spr:
				spr.visible = false)


## Andar 29 — os 3 regadores e as 3 flores-porta (regar abre-as).
func _andar_29() -> void:
	var cheio := [false]
	for s in pontos("ii"):
		peca("regador", s.p)
		usar(s.p + Vector3(0, 0, 0.8), "Encher o regador", func():
			cheio[0] = true
			Sistema.mensagem("Regador cheio de água do pântano. Agora, à flor-porta!"))
	var portas: Array = pontos("[]").filter(func(x): return "Flor-porta" in String(x.texto))
	for k in portas.size():
		var fp: Dictionary = portas[k]
		var nome := "flor_%d" % k
		if feito(nome):
			continue
		var flor := peca("flor_armadilha", fp.p)
		var ref := [null]
		ref[0] = usar(fp.p + Vector3(0, 0, 1.4), "Regar a flor-porta", func():
			if not cheio[0]:
				Sistema.mensagem("A flor-porta está seca e fechada. Precisa de água (há regadores pelo ninho).", "aviso")
				return
			cheio[0] = false
			marcar(nome)
			ref[0].ativo = false
			if flor:
				var t := create_tween()
				t.tween_property(flor, "scale", Vector3(1.3, 0.2, 1.3), 0.8)
				t.tween_callback(flor.queue_free)
			Sistema.mensagem("A flor bebe a água, abre as pétalas e deixa-te passar!", "nivel")
			if portas.all(func(x): return feito("flor_%d" % portas.find(x))):
				resolvido("flores", "As três flores-porta estão abertas: o caminho para o Coração do Ninho está livre!"))


# ------------------------------------------------------------------ Região 4 — Deserto ------------------------------------------------------------------

func tem_pa() -> bool:
	for id in ["pa", "pa_prata", "pa_dourada"]:
		if Jogo.inventario.tem(id):
			return true
	return Jogo.arma_equipada == "pa_machado_coveiro"


## As pedras-enigma da Anciã Sahra (R4_09; dados/minijogos.json "enigmas_sahra"): uma em cada um de 5 andares.
func _enigmas() -> void:
	var lista: Array = Dados.tabela("minijogos").get("enigmas_sahra", [])
	var respostas := lista.map(func(e): return String(e.resposta_pt))
	for e in lista:
		if int(e.andar) != int(andar.numero):
			continue
		var ii: Array = pontos("ii").filter(func(x): return "enigma" in String(x.texto).to_lower())
		var p: Vector3 = ii[0].p if not ii.is_empty() else aberta(40 + int(e.pedra))
		sprite("pedra_enigma", p)
		var nome := "enigma_%d" % int(e.pedra)
		usar(p + Vector3(0, 0, 0.8), "Pedra-enigma", func():
			if Jogo.tem_flag("sahra_" + nome):
				Sistema.mensagem("A pedra já ouviu a tua resposta. Está calada, satisfeita.")
				return
			if int(Jogo.contadores.get("sahra_mudo_" + nome, -1)) == Amizade.dia_absoluto():
				Sistema.mensagem("A pedra está muda. Hoje já não te ouve.", "aviso")
				return
			Sistema.mensagem("Gravado na pedra: «%s»" % e.enigma_pt)
			var opcoes: Array = [e.resposta_pt]
			for r in respostas:
				if opcoes.size() < 4 and r != e.resposta_pt:
					opcoes.append(r)
			opcoes.shuffle()
			var i: int = await escolher(opcoes)
			if i < 0:
				return
			if opcoes[i] == e.resposta_pt:
				Jogo.por_flag("sahra_" + nome)
				Colecoes.contar("enigmas_sahra")
				var n := lista.filter(func(x): return Jogo.tem_flag("sahra_enigma_%d" % int(x.pedra))).size()
				Sistema.mensagem("«%s.» A pedra brilha a azul. (%d/5 enigmas da Sahra)" % [e.resposta_pt, n], "nivel")
				if n >= lista.size() and Missoes.estado("R4_09") == "ativa":
					Missoes.marcar("R4_09", 0)
			else:
				Jogo.contadores["sahra_mudo_" + nome] = Amizade.dia_absoluto()
				Sistema.mensagem("«%s»… A pedra fica fria e muda. Até amanhã." % opcoes[i], "aviso"))


## Andar 31 — o tesouro do mapa do bandido (cavar com a Pá) e os 3 camelos perdidos da caravana (R4_02).
func _andar_31() -> void:
	for s in pontos("??"):
		sprite("pedra_1", s.p, Color("fbb954"))
		letreiro(s.p, "✕", Color("ea4f36"))
		usar(s.p + Vector3(0, 0, 0.6), "Cavar no X", func():
			if feito("tesouro"):
				Sistema.mensagem("Só areia. Já cavaste aqui.")
				return
			if not tem_pa():
				Sistema.mensagem("A areia tem um X desenhado… Com uma Pá podias cavar.", "aviso")
				return
			resolvido("tesouro", "Cavas, cavas… TOC! Um baú de ouro enterrado!", "ouro", s.p + Vector3(1.2, 0, 0))
			Jogo.inventario.adicionar("chave_bau_ouro"))
	var camelos: Array = pontos("!!")
	var salvos := [0]
	for k in camelos.size():
		var c: Dictionary = camelos[k]
		var nome: String = String(c.texto).get_slice('"', 1)
		if feito("camelo_%d" % k):
			salvos[0] += 1
			continue
		var spr := sprite("camelo", c.p)
		var kk := k
		var ref := [null]
		ref[0] = usar(c.p + Vector3(0, 0, 1.0), "Acalmar o camelo «%s»" % nome, func():
			marcar("camelo_%d" % kk)
			ref[0].ativo = false
			salvos[0] += 1
			if spr:
				create_tween().tween_property(spr, "modulate:a", 0.0, 1.0)
			Sistema.mensagem("«%s» acalma-se e trota de volta para a caravana. (%d/3)" % [nome, salvos[0]], "nivel")
			if salvos[0] >= camelos.size() and Missoes.estado("R4_02") == "ativa":
				Missoes.marcar("R4_02", 0))


## Andar 32 — o Oásis Verdadeiro: a única "miragem" com sombra ao meio-dia (Cantil Infinito).
func _andar_32() -> void:
	for s in pontos("??"):
		usar(s.p, "Miragem de um oásis", func():
			if feito("oasis"):
				Sistema.mensagem("O Oásis Verdadeiro. A água é fresca e não acaba.")
				return
			if not (Tempo.hora >= 11.0 and Tempo.hora < 13.0):
				Sistema.mensagem("A miragem tremeluz e desaparece quando lhe tocas. Só uma das miragens tem sombra… ao meio-dia.", "aviso")
				return
			marcar("oasis")
			Sistema.mensagem("Ao meio-dia, esta miragem tem sombra! A água é verdadeira: enches o cantil e ele nunca mais esvazia.", "nivel")
			dar("cantil_infinito"))


## Andar 33 — a ponte levadiça (3 alavancas puxadas no mesmo minuto) e o esconderijo do Sultão Kasim (R4_04).
func _andar_33() -> void:
	var alavancas: Array = pontos("!!")
	var puxadas := {}
	var portas: Array = pontos("[]")
	var ponte: Node3D = peca("ponte_de_pedra_natural", portas[0].p) if not portas.is_empty() else null
	if ponte and not feito("ponte"):
		ponte.visible = false
	for k in alavancas.size():
		var a: Dictionary = alavancas[k]
		sprite("pilar_areia", a.p)
		var kk := k
		usar(a.p + Vector3(0, 0, 0.8), "Puxar a alavanca %d" % (k + 1), func():
			if feito("ponte"):
				return
			var agora := Time.get_ticks_msec() / 1000.0
			puxadas[kk] = agora
			for x in puxadas.keys():
				if agora - float(puxadas[x]) > 60.0:   # mais de um minuto: a alavanca voltou para trás
					puxadas.erase(x)
			if puxadas.size() >= alavancas.size():
				if ponte:
					ponte.visible = true
				resolvido("ponte", "As três alavancas no mesmo minuto: a ponte levadiça desce com estrondo!", "prata")
			else:
				Sistema.mensagem("Clanc! A alavanca fica presa… durante um minuto. (%d/%d)" % [puxadas.size(), alavancas.size()]))
	for h in pontos("HH"):
		usar(h.p, "Cascata de areia", func():
			if feito("kasim"):
				Sistema.mensagem("O esconderijo do Sultão Kasim, vazio e cheio de pó dourado.")
				return
			marcar("kasim")
			Sistema.mensagem("Atrás da cascata de areia há uma gruta com tapetes e almofadas: o esconderijo do Sultão Kasim!", "nivel"))


## Andar 34 — as 5 portas soterradas (escavar com a Pá pela ordem I a V do mapa da Íris; R4_05) e a Coroa atrás do trono.
func _andar_34() -> void:
	var portas: Array = pontos("[]")
	var romanos := ["I", "II", "III", "IV", "V"]
	for k in portas.size():
		var d: Dictionary = portas[k]
		var m := RegEx.create_from_string("soterrada (I{1,3}|IV|V)\\b").search(String(d.texto))
		var n: int = romanos.find(m.get_string(1)) if m else k
		var no := peca("porta_soterrada", d.p)
		usar(d.p + Vector3(0, 0, 1.2), "Escavar a porta %s" % romanos[n], func():
			if not tem_pa():
				Sistema.mensagem("A porta está cheia de areia. Precisas de uma Pá.", "aviso")
				return
			carregar_ordem(n, [0, 1, 2, 3, 4], "portas", func():
				resolvido("portas", "As cinco portas da Cidade Enterrada estão abertas, pela ordem do mapa da Íris!", "prata", d.p + Vector3(1.5, 0, 0))
				if Missoes.estado("R4_05") == "ativa":
					Missoes.marcar("R4_05", 0))
			if no and _ordem.size() > 0:
				create_tween().tween_property(no, "position:y", no.position.y - 0.3, 0.4))
	for s in pontos("??"):
		peca("trono", s.p + Vector3(0, 0, -1.5))
		usar(s.p, "Empurrar o trono", func():
			if feito("coroa"):
				Sistema.mensagem("A passagem atrás do trono está vazia.")
				return
			if not feito("portas"):
				Sistema.mensagem("O trono não se mexe. Talvez quando a cidade estiver toda aberta…")
				return
			marcar("coroa")
			Sistema.mensagem("O trono desliza e mostra uma passagem: lá dentro, uma coroa de ouro coberta de areia.", "nivel")
			dar("coroa_cidade_enterrada"))


## Andar 35 — os 6 ovos de escorpião (destruí-los fecha os buracos) e o Escudo de Carapaça debaixo da carapaça gigante.
func _andar_35() -> void:
	var ovos: Array = pontos("ii")
	var partidos := [0]
	for k in ovos.size():
		if feito("ovo_%d" % k):
			partidos[0] += 1
			continue
		var o := peca("ovos", ovos[k].p)
		var kk := k
		var ref := [null]
		ref[0] = usar(ovos[k].p + Vector3(0, 0, 0.8), "Partir os ovos de escorpião", func():
			marcar("ovo_%d" % kk)
			ref[0].ativo = false
			if o:
				o.queue_free()
			partidos[0] += 1
			if partidos[0] >= ovos.size():
				resolvido("ovos", "Partiste todos os ovos! Os buracos dos escorpiões ficam em silêncio.")
			else:
				Sistema.mensagem("Ovos partidos: %d/%d." % [partidos[0], ovos.size()]))
	for s in pontos("??"):
		peca("carapaca_gigante", s.p)
		usar(s.p + Vector3(0, 0, 2.0), "Levantar a carapaça gigante", func():
			if feito("escudo"):
				return
			if Jogo.a("for") < 12:
				Sistema.mensagem("É pesadíssima. Com mais Força (12) conseguias levantá-la.", "aviso")
				return
			marcar("escudo")
			Sistema.mensagem("Levantas a carapaça… e por baixo há um pedaço perfeito: dá um escudo!", "nivel")
			dar("escudo_carapaca"))


## Andar 36 — as 4 torres com velas de pano (rodar até desviar o vento) e a Caravana Perdida com o mercador preso.
func _andar_36() -> void:
	var torres: Array = pontos("!!")
	var estado := []
	var certa := []
	for k in torres.size():
		estado.append(0)
		certa.append((k + 2) % 4)
	var lados := ["norte", "este", "sul", "oeste"]
	for k in torres.size():
		var no := peca("torre_de_pedra_com_vela", torres[k].p)
		var kk := k
		usar(torres[k].p + Vector3(0, 0, 1.2), "Rodar a vela da torre %d" % (k + 1), func():
			if feito("velas"):
				return
			estado[kk] = (estado[kk] + 1) % 4
			if no:
				create_tween().tween_property(no, "rotation:y", no.rotation.y + PI / 2.0, 0.4)
			var certas := 0
			for i in estado.size():
				certas += 1 if estado[i] == certa[i] else 0
			Sistema.mensagem("A vela vira-se para %s. O vento acalma um pouco… (%d/%d torres certas)" % [lados[estado[kk]], certas, estado.size()])
			if estado == certa:
				resolvido("velas", "As quatro velas desviam o vento: abre-se um caminho calmo pela tempestade!", "prata"))


## Andar 37 — as 4 costelas ocas (tocar a canção dos nómadas) e a asa de osso enterrada (baú de ouro).
func _andar_37() -> void:
	var costelas: Array = pontos("!!")
	var notas := ["Bum", "Bom", "Bim", "Bam"]
	var cancao := [2, 0, 3, 1]
	for k in costelas.size():
		peca("costela_gigante", costelas[k].p)
		var kk := k
		usar(costelas[k].p + Vector3(0, 0, 1.0), "Bater na costela oca (%s)" % notas[k % 4], func():
			Sistema.mensagem("♪ %s…" % notas[kk % 4])
			carregar_ordem(kk, cancao.slice(0, costelas.size()), "costelas", func():
				resolvido("costelas", "Bim-Bum-Bam-Bom! A canção dos nómadas ecoa nos ossos… e a areia mexe-se ali ao lado.")))
	for s in pontos("??"):
		usar(s.p, "Asa de osso enterrada", func():
			if feito("asa"):
				return
			if not feito("costelas"):
				Sistema.mensagem("Uma asa de osso enorme, meio enterrada. Os nómadas cantam uma canção sobre ela: «Bim, Bum, Bam, Bom».")
				return
			if not tem_pa():
				Sistema.mensagem("Há qualquer coisa debaixo da asa. Com uma Pá…", "aviso")
				return
			resolvido("asa", "Debaixo da asa de osso: um baú de ouro!", "ouro", s.p + Vector3(1.5, 0, 0))
			Jogo.inventario.adicionar("chave_bau_ouro"))


## Andar 38 — os espelhos solares (rodar os obeliscos até a luz do sol chegar ao portão; só de dia) e o Olho Solar
## no topo de um obelisco (subir de noite, por cima das estátuas).
func _andar_38() -> void:
	var obel: Array = pontos("!!")
	var estado := []
	var certa := []
	for k in obel.size():
		estado.append(0)
		certa.append((k * 3 + 2) % 4)
	for k in obel.size():
		var no := peca("obelisco_com_espelho", obel[k].p)
		var kk := k
		usar(obel[k].p + Vector3(0, 0, 1.2), "Rodar o espelho do obelisco", func():
			if feito("espelhos"):
				return
			if Tempo.hora < 7.0 or Tempo.hora >= 18.0:
				Sistema.mensagem("De noite não há sol para os espelhos. (E as estátuas estão a olhar para ti…)", "aviso")
				return
			estado[kk] = (estado[kk] + 1) % 4
			if no:
				create_tween().tween_property(no, "rotation:y", no.rotation.y + PI / 2.0, 0.4)
			if estado[kk] == certa[kk]:
				Sistema.mensagem("O raio de sol salta deste espelho para o seguinte!")
			if estado == certa:
				Historia.acontecer("portão da pirâmide")
				resolvido("espelhos", "A luz chega ao portão de ouro e a pirâmide abre-se!", "prata"))
	for s in pontos("??"):
		usar(s.p, "Subir ao obelisco", func():
			if feito("olho"):
				return
			if not (Tempo.hora >= 21.0 or Tempo.hora < 5.0):
				Sistema.mensagem("É liso demais para trepar. De noite, quando as estátuas se mexem, dava para subir por cima delas…", "aviso")
				return
			marcar("olho")
			Sistema.mensagem("Saltas de cabeça de estátua em cabeça de estátua até ao topo: um olho de ouro a brilhar!", "nivel")
			dar("olho_solar"))


## Andar 39 — os 6 painéis de hieróglifos (H_10), as 4 placas das paredes que fecham e os 9 baús (8 mímicos).
func _andar_39() -> void:
	var paineis := [0]
	for k in 6:
		var pp := aberta(60 + k)
		peca("painel_de_hieroglifos", pp)
		var kk := k
		var ref := [null]
		ref[0] = usar(pp + Vector3(0, 0, 1.0), "Copiar o painel de hieróglifos", func():
			if feito("painel_%d" % kk):
				return
			marcar("painel_%d" % kk)
			ref[0].ativo = false
			paineis[0] += 1
			Sistema.mensagem("Copiaste o painel %d de 6 para o caderno." % paineis[0])
			if paineis[0] >= 6:
				Historia.acontecer("6 painéis")
				if Missoes.estado("H_10") == "ativa":
					Missoes.marcar("H_10", 0))
		if feito("painel_%d" % k):
			paineis[0] += 1
			ref[0].ativo = false
	var placas: Array = pontos("!!")
	var simbolos := ["olho", "ave", "serpente", "sol"]
	var certa := [3, 0, 2, 1]
	for k in placas.size():
		letreiro(placas[k].p, simbolos[k % 4], Color("f9c22b"))
		var kk := k
		usar(placas[k].p + Vector3(0, 0, 0.7), "Carregar na placa (%s)" % simbolos[k % 4], func():
			carregar_ordem(kk, certa.slice(0, placas.size()), "placas", func():
				resolvido("placas", "As paredes param a centímetros de ti… e voltam para trás. Sol, olho, serpente, ave!")))
	# a Sala dos Tesouros Falsos: o baú verdadeiro é o único sem pó (os outros são mímicos)
	var baus: Array = pontos("$$")
	if baus.is_empty() or feito("verdadeiro"):
		return
	var certo := int(andar.numero * 7) % baus.size()
	for k in baus.size():
		var b: Dictionary = baus[k]
		var spr := sprite("caixote", b.p, Color("c7dcd0") if k != certo else Color("fbb954"))
		var kk := k
		var ref := [null]
		ref[0] = usar(b.p + Vector3(0, 0, 0.8), "Abrir o baú (%s)" % ("sem pó, a brilhar" if k == certo else "cheio de pó"), func():
			ref[0].ativo = false
			if spr:
				spr.visible = false
			if kk == certo:
				resolvido("verdadeiro", "O baú sem pó era o verdadeiro!", "ouro", b.p)
				Jogo.inventario.adicionar("chave_bau_ouro")
			else:
				var m := Monstro.new().configurar("mimico", int(andar.dados.get("nivel", andar.numero)))
				andar.add_child(m)
				m.global_position = b.p + Vector3(0, 0.5, 0)
				Sistema.mensagem("O baú abre a boca… é um MÍMICO!", "aviso"))


# ------------------------------------------------------------------ Região 5 — Gelo ------------------------------------------------------------------

func tem_fogo() -> bool:
	return Jogo.inventario.tem("tocha") or Jogo.buffs.has("luz") or str(Dados.arma(Jogo.arma_equipada).get("elemento", "")) == "fogo"


## Andar 41 — a Porta de Gelo (acender 4 fogueiras de pedra à volta) e o iglu escondido com o baú de ouro.
func _andar_41() -> void:
	for d in pontos("[]"):
		var porta := sprite("cristais_gelo", d.p, Color("c7dcd0"))
		if porta:
			porta.scale = Vector3.ONE * 2.2
		if feito("porta_gelo") and porta:
			porta.visible = false
		var acesas := [0]
		for k in 4:
			var ang := k * TAU / 4.0 + PI / 4.0
			var pf: Vector3 = d.p + Vector3(cos(ang) * 4.5, 0, sin(ang) * 4.5 + 2.0)
			peca("fogueira_de_pedra", pf)
			var l := luz(pf, Color("f79617"), 2.0 if feito("porta_gelo") else 0.0)
			var kk := k
			usar(pf + Vector3(0, 0, 0.9), "Acender a fogueira de pedra", func():
				if feito("porta_gelo") or Jogo.tem_flag("seg_a041_fogo_%d" % kk):
					return
				if not tem_fogo():
					Sistema.mensagem("A lenha está seca mas precisas de fogo: uma Tocha, por exemplo.", "aviso")
					return
				Jogo.por_flag("seg_a041_fogo_%d" % kk)
				l.light_energy = 2.0
				acesas[0] += 1
				if acesas[0] >= 4:
					if porta:
						create_tween().tween_property(porta, "scale", Vector3(2.2, 0.05, 2.2), 2.0)
					resolvido("porta_gelo", "As quatro fogueiras ardem e a Porta de Gelo derrete-se em água!", "prata", d.p + Vector3(0, 0, -2.0))
				else:
					Sistema.mensagem("A fogueira pega. (%d/4)" % acesas[0]))
	for s in pontos("??"):
		peca("iglu", s.p + Vector3(0, 0, -1.5))
		usar(s.p + Vector3(0, 0, 1.2), "Entrar no iglu", func():
			if feito("iglu"):
				Sistema.mensagem("A fogueira do iglu nunca se apaga. Sabe bem aquecer as mãos.")
				Jogo.hp = minf(Jogo.hp_maximo(), Jogo.hp + Jogo.hp_maximo() * 0.2)
				return
			resolvido("iglu", "Um iglu escondido entre as Pedras de Vento! Lá dentro, uma fogueira que não se apaga… e um baú de ouro.", "ouro", s.p)
			Jogo.inventario.adicionar("chave_bau_ouro"))


## Andar 42 — o pinheiro dourado (o Ninho de Gaio cai com uma gema) e os 3 troncos no rio (a ponte até à serração).
func _andar_42() -> void:
	for s in pontos("??"):
		peca("pinheiro_com_neve", s.p)
		letreiro(s.p + Vector3(0, 2.5, 0), "✦", Color("f9c22b"))
		usar(s.p + Vector3(0, 0, 1.2), "Bater no pinheiro dourado", func():
			if feito("gaio"):
				Sistema.mensagem("Cai um bocado de neve na tua cabeça. Mais nada.")
				return
			marcar("gaio")
			Sistema.mensagem("PLOF! A neve cai… e com ela um ninho de gaio com uma pedra a brilhar.", "nivel")
			dar("gema_prismatica"))
	var troncos: Array = pontos("ii")
	var feitos := [0]
	for k in troncos.size():
		if feito("tronco_%d" % k):
			feitos[0] += 1
			continue
		var t := sprite("tronco_nevado", troncos[k].p)
		var kk := k
		var ref := [null]
		ref[0] = usar(troncos[k].p + Vector3(0, 0, 0.8), "Empurrar o tronco para o rio", func():
			marcar("tronco_%d" % kk)
			ref[0].ativo = false
			feitos[0] += 1
			if t:
				create_tween().tween_property(t, "global_position", t.global_position + Vector3(0, -0.3, -2.5), 1.0)
			if feitos[0] >= troncos.size():
				resolvido("troncos", "Os três troncos encaixam-se: há uma ponte até à ilha da serração!", "prata")
			else:
				Sistema.mensagem("O tronco rola para a água. (%d/%d)" % [feitos[0], troncos.size()]))


## Andar 43 — o farol (acendê-lo mostra o caminho seguro pelo gelo fino).
func _andar_43() -> void:
	for f in pontos("<>"):
		peca("farol", f.p)
		var l := luz(f.p + Vector3(0, 6.0, 0), Color("fbff86"), 0.0)
		l.omni_range = 30.0
		if feito("farol"):
			l.light_energy = 3.0
		usar(f.p + Vector3(0, 0, 1.6), "Subir a escada do farol", func():
			if feito("farol"):
				Sistema.mensagem("A luz do farol varre o lago. Os caminhos seguros brilham no gelo.")
				return
			l.light_energy = 3.0
			resolvido("farol", "Acendes o farol: a luz mostra no gelo os caminhos seguros (onde o gelo não racha)!"))


## Andar 44 — o Benedito congelado (derreter com fogo: vai viver para Ascendia) e os 3 cristais da Câmara Prismática.
func _andar_44() -> void:
	for a in pontos("AA"):
		var bloco := peca("parede_de_gelo_transparente", a.p)
		usar(a.p + Vector3(0, 0, 1.2), "Aventureiro congelado", func():
			if feito("benedito"):
				Sistema.mensagem("Só sobra uma poça de água onde estava o Benedito.")
				return
			if not tem_fogo():
				Sistema.mensagem("Há um homem dentro do gelo… e os olhos dele mexem-se! Com fogo podias derreter o gelo.", "aviso")
				return
			marcar("benedito")
			if bloco:
				create_tween().tween_property(bloco, "scale", Vector3(1.0, 0.05, 1.0), 2.0)
			Jogo.ganhar_ouro(300)
			Sistema.mensagem("«Doze anos… doze anos a olhar para a mesma estalactite!» O Benedito agradece e vai para Ascendia. (+300 ouro)", "nivel"))
	var cristais: Array = pontos("!!")
	var acesos := [0]
	for k in cristais.size():
		var no := peca("cristal_azul_gigante", cristais[k].p)
		var l := luz(cristais[k].p, Color("8fd3ff"), 2.0 if feito("prisma") else 0.0)
		var kk := k
		usar(cristais[k].p + Vector3(0, 0, 1.4), "Derreter a parede à frente do cristal", func():
			if feito("prisma") or Jogo.tem_flag("seg_a044_cristal_%d" % kk):
				return
			if not tem_fogo():
				Sistema.mensagem("Uma parede de gelo tapa a luz deste cristal. Com fogo derretia-se.", "aviso")
				return
			Jogo.por_flag("seg_a044_cristal_%d" % kk)
			l.light_energy = 2.0
			acesos[0] += 1
			if acesos[0] >= cristais.size():
				resolvido("prisma", "A luz salta de cristal em cristal e enche a câmara de arco-íris!", "prata")
			else:
				Sistema.mensagem("A luz chega ao cristal %d. (%d/%d)" % [kk + 1, acesos[0], cristais.size()]))


## Andar 45 — os brinquedos que o Yeti guardava na gruta (depois de o vencer): uma boneca de um Jogador antigo.
func _andar_45() -> void:
	for d in pontos("[]"):
		usar(d.p + Vector3(0, 0, -1.0), "Fundo da gruta do Yeti", func():
			if feito("brinquedos"):
				return
			if not Jogo.tem_flag("boss_yeti_anciao"):
				Sistema.mensagem("Ouves roncos enormes lá dentro. Melhor não…", "aviso")
				return
			marcar("brinquedos")
			Sistema.mensagem("Atrás da cama de peles, o Yeti guardava brinquedos: piões, ossos pintados… e uma boneca de pano antiga.", "nivel")
			dar("boneca_pano"))


## Andar 46 — a armadilha velha dos caçadores (baú de prata) e o sino da torre (3 vezes à meia-noite: o Diário da
## Equipa de Gorvan, cena C5-04, H_12).
func _andar_46() -> void:
	for s in pontos("??"):
		peca("armadilhas", s.p)
		usar(s.p + Vector3(0, 0, 1.0), "Armadilha velha dos caçadores", func():
			if feito("armadilha"):
				return
			if not Jogo.tem_flag("seg_a046_mordido"):
				Jogo.por_flag("seg_a046_mordido")
				Jogo.hp = maxf(1.0, Jogo.hp - Jogo.hp_maximo() * 0.1)
				Sistema.mensagem("CLAC! A armadilha ainda funciona! (−10% HP) Mas agora está desarmada…", "aviso")
				return
			resolvido("armadilha", "Debaixo da armadilha desarmada, um baú de prata dos caçadores.", "prata", s.p + Vector3(1.2, 0, 0)))
	var toques := []
	for t in pontos("<>"):
		peca("torre_do_sino", t.p + Vector3(0, 0, -2.0))
		usar(t.p + Vector3(0, 0, 0.6), "Tocar o sino", func():
			Sistema.mensagem("DONG!")
			if not (Tempo.hora < 1.0):
				toques.clear()
				return
			var agora := Time.get_ticks_msec() / 1000.0
			toques.append(agora)
			toques.assign(toques.filter(func(x): return agora - float(x) < 60.0))
			if toques.size() >= 3 and not feito("sino"):
				marcar("sino")
				Historia.acontecer("tocar o sino")
				Sistema.mensagem("Ao terceiro toque, à meia-noite, os Caçadores Congelados param… e cai do sino um caderno velho.", "nivel")
				dar("diario_equipa_gorvan")
				if Missoes.estado("H_12") == "ativa":
					Missoes.marcar("H_12", 0))


## Andar 47 — o baú do Pico (subir pelas paredes de escalada com a Picareta) e o selo da Cripta do Rei do Inverno.
func _andar_47() -> void:
	for s in pontos("??"):
		peca("pico_com_bandeira", s.p + Vector3(0, 0, -2.0))
		usar(s.p, "Chegar ao Pico", func():
			if feito("pico"):
				Sistema.mensagem("Do pico vê-se o glaciar todo. E está um frio de morrer.")
				return
			var picareta := false
			for e in Jogo.inventario.espacos:
				if e != null and String(e.id).begins_with("picareta"):
					picareta = true
			if not picareta and not String(Jogo.arma_equipada).begins_with("picareta"):
				Sistema.mensagem("A parede de gelo é a pique. Com uma Picareta dava para escalar.", "aviso")
				return
			resolvido("pico", "Escalaste até ao Pico! Ao pé da bandeira, um baú de ouro.", "ouro", s.p)
			Jogo.inventario.adicionar("chave_bau_ouro"))
	for h in pontos("HH"):
		usar(h.p, "Selo da Cripta do Rei do Inverno", func():
			if Jogo.inventario.tem("brasa_eterna", 3):
				Sistema.mensagem("As três Brasas Eternas derretem o selo… A cripta está aberta. (Masmorra: em breve)", "nivel")
				marcar("selo")
			else:
				Sistema.mensagem("Um selo de gelo azul com três buracos redondos. Diz-se que só Brasas Eternas o derretem. (%d/3)" % Jogo.inventario.contar("brasa_eterna")))


## Andar 48 — a aurora muda de cor a cada 2 minutos; as 4 Pedras Cantantes tocam-se quando a aurora tem a cor delas (R5_08).
## Rara: a aurora dourada abre o reflexo do Lago-Espelho (baú de ouro).
const AURORA := ["verde", "azul", "branca", "roxa"]
const COR_AURORA := {"verde": Color("1ebc73"), "azul": Color("4d9be6"), "branca": Color("c7dcd0"), "roxa": Color("a884f3"), "dourada": Color("f9c22b")}


func aurora() -> String:
	var ciclo := int(Time.get_ticks_msec() / 120000.0)
	if hash([ciclo, int(andar.numero)]) % 20 == 0:
		return "dourada"
	return AURORA[ciclo % AURORA.size()]


func _andar_48() -> void:
	var ceu := luz(andar.ponto_seguro + Vector3(0, 14.0, 0), COR_AURORA[aurora()], 0.6)
	ceu.omni_range = 120.0
	var t := create_tween().set_loops()
	t.tween_interval(3.0)
	t.tween_callback(func(): ceu.light_color = COR_AURORA[aurora()])
	var pedras: Array = pontos("!!")
	for k in pedras.size():
		var cor: String = ""
		for c in AURORA:
			if c in String(pedras[k].texto):
				cor = c
		if cor == "":
			continue
		peca("pedra_cantante", pedras[k].p)
		letreiro(pedras[k].p, cor, COR_AURORA[cor])
		var cc := cor
		usar(pedras[k].p + Vector3(0, 0, 0.9), "Tocar na Pedra Cantante %s" % cor, func():
			if feito("pedras"):
				Sistema.mensagem("A pedra canta baixinho, só para ti.")
				return
			if aurora() != cc:
				Sistema.mensagem("A pedra está calada. A aurora agora é %s; esta pedra só canta com a aurora %s." % [aurora(), cc], "aviso")
				return
			Jogo.por_flag("seg_a048_canta_" + cc)
			Sistema.mensagem("♪ A pedra %s canta com a aurora!" % cc)
			if AURORA.all(func(x): return Jogo.tem_flag("seg_a048_canta_" + x)):
				resolvido("pedras", "As quatro Pedras Cantantes cantam juntas. O Mestre Kael ia gostar de ouvir isto.", "prata")
				if Missoes.estado("R5_08") == "ativa":
					Missoes.marcar("R5_08", 0))
	for s in pontos("??"):
		peca("lago_espelho", s.p)
		usar(s.p + Vector3(0, 0, 2.0), "Olhar para o Lago-Espelho", func():
			if feito("reflexo"):
				Sistema.mensagem("O teu reflexo acena-te. Tu não acenaste.")
				return
			if aurora() != "dourada":
				Sistema.mensagem("O lago reflete a aurora %s. Dizem que com uma aurora dourada se pode entrar no reflexo…" % aurora())
				return
			resolvido("reflexo", "A aurora fica dourada e o reflexo abre-se: entras num andar ao contrário… e lá está um baú de ouro!", "ouro", s.p + Vector3(2.0, 0, 1.0))
			Jogo.inventario.adicionar("chave_bau_ouro"))


## Andar 49 — os portões em cadeia (3 alavancas: cada uma abre um portão e fecha outro) e a coroa de gelo do trono
## vazio (título "Rei por Um Minuto").
func _andar_49() -> void:
	var portoes: Array = pontos("[]")
	var nos := []
	var aberto := []
	for k in portoes.size():
		nos.append(peca("portao_de_gelo", portoes[k].p))
		aberto.append("principal" in String(portoes[k].texto))
	var trono := portoes.map(func(x): return "Trono" in String(x.texto)).find(true)
	var mostrar := func():
		for k in nos.size():
			if nos[k]:
				nos[k].visible = not aberto[k] and not feito("portoes")
				for c in (nos[k] as Node).find_children("*", "CollisionShape3D", true, false):
					c.disabled = aberto[k] or feito("portoes")
	mostrar.call()
	var alavancas: Array = pontos("!!")
	for k in alavancas.size():
		sprite("placa", alavancas[k].p)
		var kk := k
		usar(alavancas[k].p + Vector3(0, 0, 0.8), "Puxar a alavanca da torre", func():
			if feito("portoes") or nos.is_empty():
				return
			var abre := (kk + 1) % nos.size()   # cada alavanca abre um portão e fecha outro
			var fecha := (kk + 3) % nos.size()
			aberto[abre] = not aberto[abre]
			aberto[fecha] = not aberto[fecha] if fecha != abre else aberto[fecha]
			mostrar.call()
			var abertos := []
			for i in nos.size():
				if aberto[i]:
					abertos.append(String(portoes[i].texto))
			Sistema.mensagem("Ouve-se gelo a ranger. Abertos: %s." % (", ".join(abertos) if not abertos.is_empty() else "nenhum"))
			if trono >= 0 and aberto[trono]:
				resolvido("portoes", "O Portão do Salão do Trono abre-se!", "prata")
				mostrar.call())
	for s in pontos("??"):
		peca("trono_de_gelo", s.p + Vector3(0, 0, -1.5))
		usar(s.p, "Pôr a coroa de gelo", func():
			Sistema.mensagem("Pões a coroa de gelo… e a corte de fantasmas aparece a dançar à tua volta, durante um minuto.", "nivel")
			if not Jogo.tem_flag("titulo_rei_por_um_minuto"):
				Jogo.por_flag("titulo_rei_por_um_minuto")
				Sistema.mensagem("Título novo: Rei por Um Minuto", "nivel"))


# ------------------------------------------------------------------ Região 6 — Oceano ------------------------------------------------------------------

## Andar 51 — as 5 conchas-sino (a ordem está desenhada no barco destruído) e a garrafa com a mensagem (R6_08).
func _andar_51() -> void:
	var conchas: Array = pontos("!!")
	var certa := range(conchas.size())
	certa.shuffle()
	var sons := ["Dlim", "Dlom", "Dlum", "Dlem", "Dlam"]
	if not conchas.is_empty():
		var barco: Vector3 = conchas[0].p + Vector3(-5.0, 0, -3.0)
		peca("barco_destruido", barco)
		usar(barco + Vector3(0, 0, 2.0), "Olhar para o casco do barco", func():
			var t := []
			for i in certa:
				t.append(str(i + 1))
			Sistema.mensagem("Riscado no casco, com uma faca: conchas numeradas e setas… %s." % " → ".join(t)))
	for k in conchas.size():
		peca("concha_gigante", conchas[k].p)
		letreiro(conchas[k].p, str(k + 1), Color("fdcbb0"))
		var kk := k
		usar(conchas[k].p + Vector3(0, 0, 1.0), "Tocar na concha-sino %d" % (k + 1), func():
			Sistema.mensagem("♪ %s…" % sons[kk % 5])
			carregar_ordem(kk, certa, "conchas", func():
				resolvido("conchas", "As cinco conchas-sino cantam juntas e a areia abre-se: um baú de prata!", "prata", conchas[kk].p + Vector3(1.5, 0, 0))))
	for g in pontos("ii"):
		peca("garrafa", g.p)
		var ref := [null]
		ref[0] = usar(g.p + Vector3(0, 0, 0.6), "Apanhar a garrafa", func():
			if feito("garrafa"):
				return
			marcar("garrafa")
			ref[0].ativo = false
			dar("garrafa_mensagem")
			Sistema.mensagem("Dentro da garrafa: um mapa! «Ao pé do Farol da Caveira, onde cai a sombra do meio-dia.» (andar 52)", "nivel"))
		if feito("garrafa"):
			ref[0].ativo = false


## Andar 52 — o tesouro da garrafa (cavar ao pé do Farol da Caveira), os 5 marcos das ilhas (R6_02) e o farol que
## mostra a ilha da névoa.
func _andar_52() -> void:
	for s in pontos("??"):
		letreiro(s.p, "✕", Color("ea4f36"))
		usar(s.p, "Cavar ao pé do farol", func():
			if feito("tesouro"):
				return
			if not Jogo.inventario.tem("garrafa_mensagem"):
				Sistema.mensagem("Areia e conchas. Sem um mapa, era cavar ao calhas.")
				return
			if not tem_pa():
				Sistema.mensagem("É aqui, como no mapa da garrafa! Precisas de uma Pá.", "aviso")
				return
			resolvido("tesouro", "TOC! O tesouro da garrafa: um baú de ouro enterrado!", "ouro", s.p + Vector3(1.2, 0, 0))
			Jogo.inventario.adicionar("chave_bau_ouro")
			if Missoes.estado("R6_08") == "ativa":
				Missoes.marcar("R6_08", 0))
	var marcos: Array = pontos("ii")
	for k in marcos.size():
		sprite("menir", marcos[k].p)
		var kk := k
		usar(marcos[k].p + Vector3(0, 0, 0.8), "Tocar no marco de pedra da ilha", func():
			if Jogo.tem_flag("seg_a052_marco_%d" % kk):
				Sistema.mensagem("Já tocaste neste marco.")
				return
			Jogo.por_flag("seg_a052_marco_%d" % kk)
			var n := range(marcos.size()).filter(func(i): return Jogo.tem_flag("seg_a052_marco_%d" % i)).size()
			Sistema.mensagem("Marco da ilha registado na carta náutica. (%d/%d)" % [n, marcos.size()])
			if n >= marcos.size() and Missoes.estado("R6_02") == "ativa":
				Missoes.marcar("R6_02", 0))
	for f in pontos("<>"):
		peca("farol", f.p)
		var l := luz(f.p + Vector3(0, 6.0, 0), Color("fbff86"), 3.0 if feito("farol") else 0.0)
		l.omni_range = 30.0
		usar(f.p + Vector3(0, 0, 1.6), "Acender o Farol da Caveira", func():
			if feito("farol"):
				Sistema.mensagem("A luz do farol aponta para a ilha da névoa.")
				return
			l.light_energy = 3.0
			resolvido("farol", "Acendes o farol e rodas o espelho: no meio da névoa aparece uma ilha que não estava lá!", "prata", f.p + Vector3(3.0, 0, 2.0)))


## Andar 53 — os 5 fantasmas de Jogadores antigos (H_14) e o leme (inclinar o navio para um barril partir a porta).
func _andar_53() -> void:
	var fantasmas: Array = pontos("AA")
	var falas := {"1 450": "«Tenho uma carta para a minha mãe… Lês-ma? Obrigado. Já posso ir.»",
		"312": "«Lá-lá-lá… Não me lembro do fim da canção. Ah, é assim! Obrigado.»",
		"8 820": "«Não consigo parar de correr! …Parei? Parei. Que descanso.»",
		"3 377": "«Daqui da proa via-se o topo da torre. Ou eu achava que sim.»",
		"6 001": "«Guardei esta porta tanto tempo… Podes entrar. Lê o diário do capitão.»"}
	for k in fantasmas.size():
		var f: Dictionary = fantasmas[k]
		var num := ""
		for n in falas:
			if n in String(f.texto):
				num = n
		var spr := sprite("menir", f.p, Color(0.7, 0.85, 1.0, 0.6))   # (a figura do fantasma)
		peca("lanterna_fantasma", f.p + Vector3(1.0, 0, 0))
		letreiro(f.p, "Nº %s" % num, Color("8fd3ff"))
		var kk := k
		var nn := num
		usar(f.p + Vector3(0, 0, 0.8), "Falar com o fantasma nº %s" % num, func():
			if Jogo.tem_flag("seg_a053_fantasma_%d" % kk):
				Sistema.mensagem("Já só se vê uma luzinha onde estava o fantasma.")
				return
			Jogo.por_flag("seg_a053_fantasma_%d" % kk)
			Sistema.mensagem(falas.get(nn, "«Obrigado…»"))
			if spr:
				create_tween().tween_property(spr, "modulate:a", 0.0, 2.0)
			var n := range(fantasmas.size()).filter(func(i): return Jogo.tem_flag("seg_a053_fantasma_%d" % i)).size()
			if n >= fantasmas.size():
				marcar("fantasmas")
				Sistema.mensagem("Os cinco fantasmas estão livres. A porta da Cabine do Capitão abre-se sozinha.", "nivel")
				if Missoes.estado("H_14") == "ativa":
					Missoes.marcar("H_14", 0))
	for l in pontos("!!"):
		peca("leme", l.p)
		usar(l.p + Vector3(0, 0, 1.0), "Rodar o leme", func():
			if feito("barril"):
				Sistema.mensagem("O navio range. O barril já partiu a porta.")
				return
			var cam := get_viewport().get_camera_3d()
			if cam and cam.has_method("tremer"):
				cam.tremer(0.4)
			resolvido("barril", "O navio inclina-se… um barril rola pelo convés e CRASH! parte a porta dos porões!", "prata", l.p + Vector3(2.0, 0, 2.0)))


## Andar 54 — as ostras (Faca de Mergulho: pérolas), a ostra gigante (só abre com a canção da Concha do Mar: Pérola
## Negra) e as 3 comportas de coral.
func _andar_54() -> void:
	var ostras: Array = pontos("ii")
	for k in ostras.size():
		var kk := k
		sprite("concha_rosa", ostras[k].p)
		usar(ostras[k].p + Vector3(0, 0, 0.6), "Abrir a ostra", func():
			if Jogo.tem_flag("seg_a054_ostra_%d" % kk):
				Sistema.mensagem("Esta ostra já está vazia.")
				return
			if not Jogo.inventario.tem("faca_mergulho"):
				Sistema.mensagem("A ostra está bem fechada. Com uma Faca de Mergulho abria-se.", "aviso")
				return
			Jogo.por_flag("seg_a054_ostra_%d" % kk)
			dar("perola"))
	for s in pontos("??"):
		peca("ostra_gigante", s.p)
		usar(s.p + Vector3(0, 0, 1.4), "Ostra gigante", func():
			if feito("perola_negra"):
				return
			if not Jogo.inventario.tem("concha_mar"):
				Sistema.mensagem("Uma ostra do tamanho de uma cama. Dizem que só se abre a ouvir uma canção.", "aviso")
				return
			marcar("perola_negra")
			Sistema.mensagem("Tocas a Concha do Mar. A ostra gigante abre-se devagar, a ouvir… e lá dentro brilha uma pérola negra.", "nivel")
			dar("perola_negra"))
	var comportas: Array = pontos("!!")
	var abertas := [0]
	for k in comportas.size():
		var no := peca("comporta_de_coral", comportas[k].p)
		var kk := k
		var ref := [null]
		ref[0] = usar(comportas[k].p + Vector3(0, 0, 1.0), "Abrir a comporta de coral", func():
			if Jogo.tem_flag("seg_a054_comporta_%d" % kk):
				return
			Jogo.por_flag("seg_a054_comporta_%d" % kk)
			ref[0].ativo = false
			if no:
				create_tween().tween_property(no, "position:y", no.position.y - 1.5, 1.0)
			abertas[0] += 1
			if abertas[0] >= comportas.size():
				resolvido("correntes", "As três comportas abertas mudam a corrente: ela leva-te até à gruta da lagoa!", "prata")
			else:
				Sistema.mensagem("A comporta abre-se e a água muda de direção. (%d/%d)" % [abertas[0], comportas.size()]))


## Andar 55 — o cofre do Capitão pirata (Chave do Almirante).
func _andar_55() -> void:
	for s in pontos("??"):
		sprite("caixote", s.p, Color("fbb954"))
		usar(s.p + Vector3(0, 0, 0.8), "Cofre do Capitão", func():
			if feito("chave"):
				Sistema.mensagem("O cofre está vazio. Os piratas não vão gostar.")
				return
			marcar("chave")
			Sistema.mensagem("No fundo do cofre, embrulhada num lenço: uma chave grande com uma âncora.", "nivel")
			dar("chave_almirante"))


## Andar 56 — as 4 lontras (dar-lhes as conchas por ordem de tamanho abre a gruta do ovo de polvo, R6_15) e a porta
## do cofre do Naufrágio Antigo (Chave do Almirante).
func _andar_56() -> void:
	var lontras: Array = pontos("ii")
	var tamanhos := ["pequenina", "pequena", "grande", "enorme"]
	for k in lontras.size():
		peca("lontras", lontras[k].p)
		var kk := k
		usar(lontras[k].p + Vector3(0, 0, 1.0), "Dar uma concha à lontra", func():
			if feito("lontras"):
				Sistema.mensagem("A lontra rebola de barriga para o ar, contente.")
				return
			Sistema.mensagem("A lontra %d olha para as conchas que trazes. Qual lhe dás?" % (kk + 1))
			var i: int = await escolher(tamanhos)
			if i < 0:
				return
			if i != kk:
				_ordem.clear()
				Sistema.mensagem("A lontra devolve-te a concha e amua. As conchas vão por ordem de tamanho, lontra a lontra.", "aviso")
				return
			carregar_ordem(kk, range(lontras.size()), "lontras", func():
				resolvido("lontras", "As lontras empilham as conchas por tamanho… e uma rocha rola: abre-se a gruta do polvo!")))
	for h in pontos("HH"):
		usar(h.p, "Gruta do polvo", func():
			if not feito("lontras"):
				Sistema.mensagem("Uma rocha redonda tapa a entrada. As lontras olham para ela com interesse…")
				return
			if feito("ovo"):
				return
			marcar("ovo")
			Sistema.mensagem("Ao fundo da gruta, num ninho de algas: um ovo mole, com oito manchinhas.", "nivel")
			dar("ovo_polvo")
			if Missoes.estado("R6_15") == "ativa":
				Missoes.marcar("R6_15", 0))
	for d in pontos("[]"):
		peca("naufragio_antigo", d.p + Vector3(0, 0, -3.0))
		usar(d.p, "Porta do cofre do Naufrágio Antigo", func():
			if Jogo.inventario.tem("chave_almirante"):
				Sistema.mensagem("A Chave do Almirante roda… a porta abre-se para o fundo do mar. (Masmorra: em breve)", "nivel")
			else:
				Sistema.mensagem("Uma fechadura com a forma de uma âncora.", "aviso"))


## Andar 57 — ligar as 4 correntes-elevador até ao topo do Palácio.
func _andar_57() -> void:
	var correntes: Array = pontos("<>")
	var ligadas := [0]
	for k in correntes.size():
		var no := peca("coluna_de_corrente", correntes[k].p)
		if no and not Jogo.tem_flag("seg_a057_corrente_%d" % k):
			no.visible = false
		var kk := k
		usar(correntes[k].p + Vector3(0, 0, 1.0), "Ligar a corrente-elevador", func():
			if Jogo.tem_flag("seg_a057_corrente_%d" % kk):
				Sistema.mensagem("A coluna de água sobe com força. Wheee!")
				return
			Jogo.por_flag("seg_a057_corrente_%d" % kk)
			if no:
				no.visible = true
			ligadas[0] = range(correntes.size()).filter(func(i): return Jogo.tem_flag("seg_a057_corrente_%d" % i)).size()
			if ligadas[0] >= correntes.size():
				resolvido("correntes", "As quatro correntes-elevador estão ligadas: sobes até ao topo do Palácio de Pérola!", "prata")
			else:
				Sistema.mensagem("Uma coluna de água começa a subir. (%d/%d)" % [ligadas[0], correntes.size()]))


## Andar 58 — a caixa de lata do Tomás (fecho 2-8-0: a Carta do Tomás) e os 5 corais luminosos da constelação.
func _andar_58() -> void:
	for s in pontos("??"):
		sprite("caixote", s.p, Color("9babb2"))
		usar(s.p + Vector3(0, 0, 0.8), "Caixa de lata do barco «Gaivota»", func():
			if feito("carta"):
				Sistema.mensagem("A caixa está vazia. A carta está contigo.")
				return
			var feitos := []
			for k in 3:
				var i: int = await escolher(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
				if i < 0:
					return
				feitos.append(i)
			if feitos == [2, 8, 0]:
				marcar("carta")
				Sistema.mensagem("Clic. Dentro da caixa, seca, uma carta: «Mãe…». É do Tomás, o filho da Dona Marta.", "nivel")
				dar("carta_tomas")
			else:
				Sistema.mensagem("O fecho não abre. Três números… o barco chamava-se Gaivota e era de 280… quê?", "aviso"))
	var corais: Array = pontos("!!")
	var constelacao := [0, 2, 4, 1, 3].slice(0, corais.size())
	for k in corais.size():
		var no := peca("coral_luminoso", corais[k].p)
		var l := luz(corais[k].p, Color("30e1b9"), 2.0 if feito("constelacao") else 0.0)
		var kk := k
		usar(corais[k].p + Vector3(0, 0, 0.9), "Acender o coral luminoso %d" % (k + 1), func():
			l.light_energy = 2.0
			carregar_ordem(kk, constelacao, "constelacao", func():
				resolvido("constelacao", "Os cinco corais desenham a constelação do Palácio de Pérola no fundo do mar!", "prata"),
				func():
					for c in get_children():
						if c is OmniLight3D and c.light_color == Color("30e1b9"):
							c.light_energy = 0.0))
	if not corais.is_empty():
		usar(corais[0].p + Vector3(-2.0, 0, 0), "Desenho na rocha", func():
			Sistema.mensagem("Riscadas na rocha, estrelas ligadas por linhas: 1 → 3 → 5 → 2 → 4. Como no teto do Palácio de Pérola."))


## Andar 59 — as 4 conchas-alavanca (cada uma enche uma sala e esvazia a do lado) e a concha falante do Santuário
## (bênção: +10% HP máximo enquanto estiveres no oceano).
func _andar_59() -> void:
	var conchas: Array = pontos("!!")
	var cheia := []
	var certa := []
	for k in conchas.size():
		cheia.append(k % 2 == 0)
		certa.append(k % 2 == 1)
	for k in conchas.size():
		peca("concha_alavanca", conchas[k].p)
		var kk := k
		usar(conchas[k].p + Vector3(0, 0, 0.9), "Rodar a concha-alavanca %d" % (k + 1), func():
			if feito("mares"):
				return
			cheia[kk] = not cheia[kk]
			var outra := (kk + 1) % cheia.size()
			cheia[outra] = not cheia[outra]
			var t := []
			for i in cheia.size():
				t.append("%d %s" % [i + 1, "cheia" if cheia[i] else "vazia"])
			Sistema.mensagem("A água corre entre as salas: %s." % " · ".join(t))
			if cheia == certa:
				resolvido("mares", "As salas certas cheias e as outras vazias: o caminho para o Santuário está aberto!"))
	var santuario: Vector3 = conchas[conchas.size() - 1].p + Vector3(4.0, 0, -4.0) if not conchas.is_empty() else andar.ponto_seguro + Vector3(6, 0, 0)
	peca("concha_falante", santuario)
	usar(santuario + Vector3(0, 0, 1.4), "Concha falante do Santuário", func():
		if not feito("mares"):
			Sistema.mensagem("Ouves uma voz muito longe, abafada pela água.")
			return
		if not Jogo.tem_flag("bencao_templo_mar"):
			Jogo.por_flag("bencao_templo_mar")
			Eventos.stats_mudaram.emit()
		Sistema.mensagem("«Filho da escada… o mar abençoa-te.» (+10% HP máximo enquanto estiveres no oceano)", "nivel"))
