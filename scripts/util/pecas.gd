class_name Pecas
extends RefCounted
## Peças repetidas (chão, árvores...) desenhadas com MultiMesh: uma MultiMeshInstance por malha.
## Uso: var p := Pecas.new(); p.por(caminho_glb, transform); ...; p.criar(pai)

static var _cache: Dictionary = {}
var _instancias: Dictionary = {}


func por(caminho: String, t: Transform3D) -> void:
	if caminho != "" and ResourceLoader.exists(caminho):
		_instancias.get_or_add(caminho, []).append(t)


func criar(pai: Node) -> void:
	for caminho in _instancias:
		var ts: Array = _instancias[caminho]
		for par in malhas(caminho):
			var mm := MultiMesh.new()
			mm.transform_format = MultiMesh.TRANSFORM_3D
			mm.mesh = par[0]
			mm.instance_count = ts.size()
			for i in ts.size():
				mm.set_instance_transform(i, ts[i] * par[1])
			var mi := MultiMeshInstance3D.new()
			mi.multimesh = mm
			pai.add_child(mi)
	_instancias.clear()


static func malhas(caminho: String) -> Array:
	if _cache.has(caminho):
		return _cache[caminho]
	var lista: Array = []
	var no: Node = (load(caminho) as PackedScene).instantiate()
	_recolher(no, Transform3D(), lista)
	no.free()
	_cache[caminho] = lista
	return lista


static func _recolher(no: Node, base: Transform3D, lista: Array) -> void:
	var t := base
	if no is Node3D:
		t = base * (no as Node3D).transform
	if no is MeshInstance3D and (no as MeshInstance3D).mesh:
		lista.append([(no as MeshInstance3D).mesh, t])
	for f in no.get_children():
		_recolher(f, t, lista)


## A caixa (AABB) de um modelo, para a colisão.
static func caixa(caminho: String) -> AABB:
	var a := AABB()
	var primeiro := true
	for par in malhas(caminho):
		var b: AABB = par[1] * (par[0] as Mesh).get_aabb()
		a = b if primeiro else a.merge(b)
		primeiro = false
	return a
