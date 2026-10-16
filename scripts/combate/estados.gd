class_name Estados
extends Node
## Estados alterados de um jogador ou monstro (docs/SISTEMAS.md, secção 5; dados em dados/estados.json).
## O dono (pai) tem de ter: hp_maximo_estado() -> float e perder_hp_estado(valor: float, cor: String, minimo_1: bool).
## Bosses: cada estado dura 50% e depois ficam 10 s imunes a esse estado.

signal mudou

var ativos: Dictionary = {}     # id -> {"t": segundos que faltam, "n": acumulações}
var imunes: Dictionary = {}     # id -> segundos que faltam (-1 = sempre)
var e_boss := false
var _dano_guardado: Dictionary = {}
var _ultima_pos := Vector3.INF
var origem := Vector3.INF       # quem aplicou o último estado (para Puxado)
var altura := 1.9               # onde aparece o ícone por cima da cabeça
var _icone: AnimatedSprite3D
static var _folhas: Dictionary = {}


func _ready() -> void:
	mudou.connect(_mostrar_icone)


## Ícone animado do estado mais recente por cima da cabeça (arte/efeitos/estado_<id>.png, 4 frames de 9×11).
func _mostrar_icone() -> void:
	if ativos.is_empty():
		if _icone:
			_icone.visible = false
		return
	var id: String = ativos.keys()[ativos.size() - 1]
	if not _folhas.has(id):
		var caminho := "res://arte/efeitos/estado_%s.png" % id
		if not ResourceLoader.exists(caminho):
			return
		var tex: Texture2D = load(caminho)
		var sf := SpriteFrames.new()
		sf.set_animation_speed("default", 6)
		for i in tex.get_width() / 9:
			var at := AtlasTexture.new()
			at.atlas = tex
			at.region = Rect2(i * 9, 0, 9, tex.get_height())
			sf.add_frame("default", at)
		_folhas[id] = sf
	if _icone == null:
		_icone = AnimatedSprite3D.new()
		_icone.billboard = BaseMaterial3D.BILLBOARD_ENABLED
		_icone.texture_filter = BaseMaterial3D.TEXTURE_FILTER_NEAREST
		_icone.pixel_size = 1.0 / 16.0
		_icone.no_depth_test = true
		_icone.shaded = false
		get_parent().add_child.call_deferred(_icone)
	_icone.position.y = altura
	_icone.sprite_frames = _folhas[id]
	_icone.visible = true
	_icone.play("default")


static func info(id: String) -> Dictionary:
	return Dados.obter("estados", id)


## Aplica um estado. dura < 0 = a duração da tabela. Devolve true se pegou.
func aplicar(id: String, dura: float = -1.0) -> bool:
	var d := info(id)
	if d.is_empty() or imunes.has(id):
		return false
	if dura <= 0.0:
		dura = float(d.get("dura", 1.0))
	if e_boss:
		dura = float(d.get("dura_boss", dura * float(Dados.c("estado_boss_dura", 0.5))))
	if d.has("acumula"):
		var n := int(ativos.get(id, {}).get("n", 0)) + 1
		if n >= int(d.acumula):
			ativos.erase(id)
			mudou.emit()
			return aplicar(String(d.vira))
		ativos[id] = {"t": dura, "n": n}
	else:
		ativos[id] = {"t": max(dura, float(ativos.get(id, {}).get("t", 0.0))), "n": 1}
	if d.get("trocar_arma", false) and get_parent().has_method("trocar_arma"):
		get_parent().trocar_arma()
	mudou.emit()
	return true


func tem(id: String) -> bool:
	return ativos.has(id)


func tirar(lista: Array) -> void:
	if "todos" in lista:
		ativos.clear()
	for id in lista:
		ativos.erase(id)
	mudou.emit()


func dar_imunidade(id: String, segundos: float) -> void:
	imunes[id] = segundos
	ativos.erase(id)
	mudou.emit()


## Produto de um campo (vel_mult, atq_vel_mult, def_mult, cura_mult, dano_mult...) de todos os estados ativos.
func mult(campo: String) -> float:
	var m := 1.0
	for id in ativos:
		m *= float(info(id).get(campo, 1.0))
	return m


## Algum estado ativo tem este campo a true? (parado, sem_atacar, sem_skills, trocar_controlos)
func flag(campo: String) -> bool:
	for id in ativos:
		if info(id).get(campo, false):
			return true
	return false


## Multiplicador por elemento vindo dos estados (ex.: Encharcado: raio ×1,5, fogo ×0,5).
func mult_elemento(elemento: String) -> float:
	var m := 1.0
	for id in ativos:
		m *= float(info(id).get("elem_mult", {}).get(elemento, 1.0))
	return m


## Carregar nos botões depressa solta de Agarrado e parte o gelo de Congelado.
func sacudir() -> void:
	for id in ativos:
		if info(id).get("soltar", false) or id == "congelado":
			ativos[id].t -= 0.25


## O próximo golpe faz mais (Congelado ×1,5) e parte o gelo.
func consumir_golpe_mult() -> float:
	var m := 1.0
	for id in ativos.keys():
		var g := float(info(id).get("golpe_mult", 1.0))
		if g != 1.0:
			m *= g
			ativos.erase(id)
			mudou.emit()
	return m


## Aplica os estados de um golpe: [{estado, hipotese, dura}]
func do_golpe(lista: Array, rng: RandomNumberGenerator = null, de: Vector3 = Vector3.INF) -> Array:
	var pegou := []
	if de != Vector3.INF:
		origem = de
	for e in lista:
		var h := float(e.get("hipotese", 1.0))
		var x := rng.randf() if rng else randf()
		if x < h and aplicar(String(e.estado), float(e.get("dura", -1.0))):
			pegou.append(String(e.estado))
	return pegou


func _physics_process(delta: float) -> void:
	var dono := get_parent()
	if ativos.is_empty() and imunes.is_empty():
		_ultima_pos = dono.global_position if dono is Node3D else Vector3.INF
		return
	var mudou_algo := false
	for id in imunes.keys():
		if imunes[id] >= 0.0:
			imunes[id] -= delta
			if imunes[id] <= 0.0:
				imunes.erase(id)
	for id in ativos.keys():
		var d := info(id)
		var hp_max: float = dono.hp_maximo_estado()
		var dano := float(d.get("dano_hp_s", 0.0)) * hp_max * delta
		if d.has("dano_hp_m") and dono is Node3D and _ultima_pos != Vector3.INF:
			var andou := Vector2(dono.global_position.x - _ultima_pos.x, dono.global_position.z - _ultima_pos.z).length()
			dano += float(d.dano_hp_m) * hp_max * andou
		if dano > 0.0:
			_dano_guardado[id] = float(_dano_guardado.get(id, 0.0)) + dano
			if _dano_guardado[id] >= 1.0:
				var inteiro := floorf(_dano_guardado[id])
				_dano_guardado[id] -= inteiro
				dono.perder_hp_estado(inteiro, d.get("cor", "#ffffff"), id == "veneno")
		ativos[id].t -= delta
		if ativos[id].t <= 0.0:
			ativos.erase(id)
			_dano_guardado.erase(id)
			mudou_algo = true
			if e_boss:
				imunes[id] = float(Dados.c("estado_boss_imune", 10))
	if dono is Node3D:
		_ultima_pos = dono.global_position
	if mudou_algo:
		mudou.emit()


func para_gravar() -> Dictionary:
	return {"ativos": ativos, "imunes": imunes}
