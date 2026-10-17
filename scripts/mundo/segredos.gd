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
		18: ["fornalha_ana", "portao_com_aneis_de_runas"], 19: ["estalagmite_espelhada", "altar_do_reflexo"]}
## Andares em que os baús "$$" são prémios (só aparecem quando se resolve o segredo ou o puzzle).
const BAUS_PREMIO := [11, 12, 14, 15, 18]

var andar: Node                    # o Andar
var _ordem: Array = []             # puzzles de ordem: o que já se carregou
var _t_sinos: float = 0.0
var _sinos: Dictionary = {}


func _ready() -> void:
	var f := "_andar_%d" % int(andar.numero)
	if has_method(f):
		call(f)
	_corridas()


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
