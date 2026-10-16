class_name NPC
extends CharacterBody3D
## Um NPC (docs/NPCS.md): boneco animado, tecla E para falar, menu Conversar · Perguntar sobre… · Dar presente.
## A conversa escolhida segue a prioridade de docs/dialogos/README.md, secção 2.

const ANIMS := {"parado": [4, true], "andar": [8, true]}
const NOMES_REGIAO := ["", "Floresta", "Cavernas", "Pântano", "Deserto", "Gelo", "Oceano", "Vulcão", "Reino Assombrado", "Céu", "Abismo"]

var id: String = ""
var dados: Dictionary = {}
var dialogo: Dictionary = {}
var servicos: Array = []        # [["Loja", Callable]] — as lojas e serviços juntam-se aqui (cidade)
var sprite: AnimatedSprite3D
var _inter: Interagivel
var _destino := Vector3.INF
var _gravidade: float = ProjectSettings.get_setting("physics/3d/default_gravity", 9.8)


func configurar(id_: String) -> NPC:
	id = id_
	return self


func _ready() -> void:
	add_to_group("npcs")
	dados = Dados.obter("npcs", id)
	dialogo = Dados.tabela("dialogos/" + id)
	collision_layer = 1
	collision_mask = 1
	var f := CollisionShape3D.new()
	var c := CapsuleShape3D.new()
	c.radius = 0.3
	c.height = 1.4
	f.shape = c
	f.position.y = 0.7
	add_child(f)
	sprite = Folhas.boneco(Folhas.criar(dados.get("sprite", "res://arte/npcs/" + id), ANIMS, ["baixo", "cima", "lado"]), 32)
	add_child(sprite)
	add_child(Folhas.sombra(0.4))
	_inter = Interagivel.new()
	_inter.texto = "Falar com %s" % dados.get("nome_pt", id)
	add_child(_inter)
	_inter.usado.connect(func(j): conversar_menu(j))
	_anim("parado", "baixo")
	if id == "lyra":   # a Lyra tem o quadro de missões da Guilda
		servicos.append(["Quadro de missões", func():
			var q = get_tree().get_first_node_in_group("diario_ui")
			if q:
				q.abrir_quadro()])


func _anim(nome: String, dir: String) -> void:
	var a := "%s_%s" % [nome, dir]
	if sprite.sprite_frames.has_animation(a) and sprite.animation != a:
		sprite.play(a)


## Andar até um ponto (rotinas da cidade).
func ir_para(p: Vector3) -> void:
	_destino = p


func _physics_process(delta: float) -> void:
	velocity.y = 0.0 if is_on_floor() else velocity.y - _gravidade * delta
	if _destino != Vector3.INF:
		var d := _destino - global_position
		d.y = 0.0
		if d.length() < 0.3:
			_destino = Vector3.INF
			velocity.x = 0.0
			velocity.z = 0.0
			_anim("parado", "baixo")
		else:
			var v := d.normalized() * 2.2
			velocity.x = v.x
			velocity.z = v.z
			if absf(d.x) > absf(d.z):
				_anim("andar", "lado")
				sprite.flip_h = d.x < 0.0
			else:
				_anim("andar", "baixo" if d.z > 0.0 else "cima")
	move_and_slide()


func _olhar_para(j: Node3D) -> void:
	var d := j.global_position - global_position
	if absf(d.x) > absf(d.z):
		_anim("parado", "lado")
		sprite.flip_h = d.x < 0.0
	else:
		_anim("parado", "baixo" if d.z > 0.0 else "cima")


# ------------------------------------------------------------------ menu ------------------------------------------------------------------

func _ui() -> Node:
	return get_tree().get_first_node_in_group("dialogo_ui")


func conversar_menu(j: Node3D) -> void:
	var ui := _ui()
	if ui == null or ui.ocupado:
		return
	_destino = Vector3.INF
	_olhar_para(j)
	ui.ocupado = true
	await conversar()
	while true:
		var opcoes := ["Conversar", "Perguntar sobre…", "Dar presente"]
		for s in servicos:
			opcoes.append(s[0])
		opcoes.append("Adeus")
		var i: int = await ui.escolher(opcoes)
		if i == 0:
			await conversar()
		elif i == 1:
			await perguntar()
		elif i == 2:
			await dar_presente()
		elif i < 3 + servicos.size():
			ui.fechar()
			servicos[i - 3][1].call()
			return
		else:
			break
	ui.fechar()


func _fala(f: Dictionary) -> Dictionary:
	var r := f.duplicate()
	r["quem"] = dados.get("nome_pt", id)
	return r


## A conversa do dia (prioridade de docs/dialogos/README.md, secção 2).
func conversar() -> void:
	var ui := _ui()
	var primeira_hoje := Amizade.falar(id)
	# 0. a primeira conversa de sempre
	if not Amizade.vista(id, "primeira") and not dialogo.get("primeira", []).is_empty():
		Amizade.marcar_vista(id, "primeira")
		await ui.falar(dialogo.primeira, id)
		return
	# 1. cena de coração pendente
	for c in dialogo.get("cenas", []):
		if Amizade.coracoes(id) >= int(c.coracoes) and not Amizade.vista(id, c.id) and Condicoes.avaliar(c.get("cond", "")):
			Amizade.marcar_vista(id, c.id)
			await ui.falar(c.falas, id)
			return
	# 2. aniversário
	if Amizade.e_aniversario(id) and primeira_hoje and dialogo.get("aniversario", {}).has("sem"):
		await ui.falar([_fala(dialogo.aniversario.sem)], id)
		return
	# 4. depois de um boss (o mais recente que ainda não comentou)
	var bosses: Array = Dados.tabela("bosses").values()
	bosses.sort_custom(func(a, b): return int(a.andar) > int(b.andar))
	for b in bosses:
		if Jogo.tem_flag("boss_" + b.id) and dialogo.get("bosses", {}).has(b.id) and not Amizade.vista(id, "boss_" + b.id):
			for b2 in bosses:   # os anteriores ficam todos "vistos"
				if Jogo.tem_flag("boss_" + b2.id):
					Amizade.marcar_vista(id, "boss_" + b2.id)
			await ui.falar([_fala({"emocao": "feliz", "texto": dialogo.bosses[b.id]})], id)
			return
	# 5. missões deste NPC: entregar, pedir ou lembrar
	if await _missoes():
		return
	# 6. estado do herói (1 vez por dia)
	if primeira_hoje:
		for e in dialogo.get("estados", []):
			if e.cond != "" and Condicoes.avaliar(e.cond):
				await ui.falar([_fala(e)], id)
				return
	# 8. já falaste hoje: fala curta
	if not primeira_hoje and not dialogo.get("curtas", []).is_empty():
		await ui.falar([_fala(dialogo.curtas.pick_random())], id)
		return
	# 7. falas do dia a dia: ao acaso, sem repetir as últimas 5, as específicas valem ×3
	var f := escolher_fala(dialogo.get("dia", []))
	if not f.is_empty():
		Amizade.lembrar(id, f.id)
		await ui.falar([_fala(f)], id)


func escolher_fala(lista: Array, rng: RandomNumberGenerator = null) -> Dictionary:
	var recentes: Array = Amizade._reg(id).recentes
	var possiveis := []
	var total := 0.0
	for f in lista:
		if f.id in recentes or not Condicoes.avaliar(f.get("cond", "")):
			continue
		var peso := float(Dados.c("dialogo_peso_especifico", 3)) if f.get("cond", "") != "" else 1.0
		possiveis.append([f, peso])
		total += peso
	if possiveis.is_empty():
		return {}
	var x := (rng.randf() if rng else randf()) * total
	for p in possiveis:
		x -= p[1]
		if x <= 0.0:
			return p[0]
	return possiveis[-1][0]


## As missões deste NPC na conversa (prioridade 5): entregar as prontas, pedir uma nova, lembrar uma ativa.
func _missoes() -> bool:
	var ui := _ui()
	var falas_m := {}
	for m in dialogo.get("missoes", []):
		falas_m[m.id] = m
	for m in Dados.tabela("missoes").values() + Jogo.quadro:
		if m.get("dada_por", "") != id:
			continue
		var e := Missoes.estado(m.id)
		var partes: Dictionary = falas_m.get(m.id, {}).get("partes", {})
		if e == "pronta":
			var f: Array = partes.get("entregar", [])
			await ui.falar(f if not f.is_empty() else [_fala({"emocao": "feliz", "texto": "Conseguiste! Obrigad{o/a}, {nome}."})], id)
			Missoes.entregar(m.id)
			return true
	for m in Dados.tabela("missoes").values():
		if m.get("dada_por", "") != id or Missoes.estado(m.id) != "inativa" or not falas_m.has(m.id):
			continue
		if m.get("tipo", "") == "guilda":
			continue
		var cab: String = falas_m[m.id].get("cabecalho_pt", "")
		var cor := cab.find("❤")
		var precisa := int(cab.substr(maxi(0, cab.find("(") + 1), 2).strip_edges()) if cor > 0 else 0
		var conds := []
		var re := RegEx.new()
		re.compile("`([^`]+)`")
		for x in re.search_all(cab):
			conds.append(x.get_string(1))
		if Amizade.coracoes(id) < precisa or not Condicoes.avaliar(" && ".join(conds)):
			continue
		var pedir: Array = falas_m[m.id].get("partes", {}).get("pedir", [])
		if pedir.is_empty():
			continue
		var escolha: int = await ui.falar(pedir, id)
		if escolha <= 0:   # a 1.ª escolha é sempre "aceitar"
			Missoes.aceitar(m.id)
		return true
	for m in Dados.tabela("missoes").values():
		if m.get("dada_por", "") == id and Missoes.estado(m.id) == "ativa" and falas_m.has(m.id) and randf() < 0.5:
			var d: Array = falas_m[m.id].get("partes", {}).get("durante", [])
			if not d.is_empty():
				await ui.falar(d, id)
				return true
	return false


func perguntar() -> void:
	var ui := _ui()
	var p: Dictionary = dialogo.get("perguntar", {})
	var i: int = await ui.escolher(["A torre", "Este andar", "Rumores", "A tua vida", "Voltar"])
	match i:
		0:
			await ui.falar(p.get("torre", []), id)
		1:
			var regiao := clampi((Jogo.andar_maximo - 1) / 10 + 1, 1, 10)
			var t: String = p.get("andar", {}).get(str(regiao), "")
			if t != "":
				await ui.falar([_fala({"emocao": "normal", "texto": t})], id)
		2:
			var r := escolher_fala(p.get("rumores", []))
			if not r.is_empty():
				await ui.falar([_fala(r)], id)
		3:
			var vida: Dictionary = p.get("vida", {})
			var melhor := ""
			for k in vida:
				if int(k) <= Amizade.coracoes(id) and (melhor == "" or int(k) > int(melhor)):
					melhor = k
			if melhor != "":
				await ui.falar([_fala({"emocao": "normal", "texto": vida[melhor]})], id)


## Escolher um item da mochila (6 de cada vez) e dar.
func dar_presente() -> void:
	var ui := _ui()
	var motivo := Amizade.pode_dar(id)
	if motivo != "":
		Sistema.mensagem(motivo, "aviso")
		return
	var ids := []
	for e in Jogo.inventario.espacos:
		if e != null and not e.id in ids and not Inventario.e_equipamento(e.id):
			ids.append(e.id)
	if ids.is_empty():
		Sistema.mensagem("Não tens nada para dar.", "aviso")
		return
	var pagina := 0
	while true:
		var parte := ids.slice(pagina * 6, pagina * 6 + 6)
		var opcoes: Array = parte.map(func(x): return Inventario._dados(x).get("nome_pt", x))
		var mais := ids.size() > (pagina + 1) * 6
		if mais:
			opcoes.append("Mais…")
		opcoes.append("Não dar nada")
		var i: int = await ui.escolher(opcoes)
		if i < parte.size():
			await _reagir(parte[i])
			return
		if mais and i == parte.size():
			pagina += 1
			continue
		return


func _reagir(item: String) -> void:
	var ui := _ui()
	var aniv := Amizade.e_aniversario(id)
	var reac := Amizade.dar(id, item)
	if reac == "":
		return
	var pres: Dictionary = dialogo.get("presentes", {})
	var emo: String = {"adora": "feliz", "gosta": "feliz", "neutro": "normal", "nao_gosta": "triste", "detesta": "zangado"}.get(reac, "normal")
	var texto := ""
	if aniv and dialogo.get("aniversario", {}).has("adora" if reac == "adora" else "outro"):
		texto = dialogo.aniversario["adora" if reac == "adora" else "outro"].texto
	elif pres.get("especiais", {}).has(item):
		texto = pres.especiais[item]
	else:
		var lista: Array = pres.get("reacoes", {}).get(reac, [])
		if lista.is_empty():
			lista = pres.get("reacoes", {}).get("neutro", ["Obrigad{o/a}."])
		texto = lista.pick_random()
	await ui.falar([_fala({"emocao": emo, "texto": texto})], id)
