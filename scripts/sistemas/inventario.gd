class_name Inventario
extends RefCounted
## Mochila (docs/SISTEMAS.md, secção 13): N espaços, pilhas até "empilha" (99), barra rápida de 6,
## itens de missão à parte (não ocupam espaço). Armas e armaduras são "instâncias" com melhoria e raridade.

signal mudou

var espacos: Array = []          # cada um: null · {"id", "qtd"} · {"id", "qtd": 1, "inst", "melhoria", "raridade", "qualidade", "gema"}
var missao: Dictionary = {}       # id -> qtd
var barra_rapida: Array = ["", "", "", "", "", ""]   # ids de consumíveis
var _proxima_inst: int = 1


func _init(tamanho: int = 30) -> void:
	espacos.resize(tamanho)


func tamanho() -> int:
	return espacos.size()


func aumentar(novo_tamanho: int) -> void:
	if novo_tamanho > espacos.size():
		espacos.resize(novo_tamanho)
		mudou.emit()


static func _dados(id: String) -> Dictionary:
	var d := Dados.item(id)
	if d.is_empty():
		d = Dados.arma(id)
		if not d.is_empty():
			d = d.duplicate()
			d["categoria"] = "arma"
			d["empilha"] = 1
	return d


static func e_equipamento(id: String) -> bool:
	return _dados(id).get("categoria", "") in ["arma", "armadura", "acessorio", "ferramenta"]


## Junta itens; devolve quantos NÃO couberam (0 = coube tudo).
func adicionar(id: String, qtd: int = 1, extra: Dictionary = {}) -> int:
	var d := _dados(id)
	if d.get("categoria", "") == "missao":
		missao[id] = int(missao.get(id, 0)) + qtd
		mudou.emit()
		return 0
	if e_equipamento(id):
		var falta := qtd
		while falta > 0:
			var i := espacos.find(null)
			if i < 0:
				break
			var inst := {"id": id, "qtd": 1, "inst": "inst_%04d" % _proxima_inst, "melhoria": 0,
						 "raridade": extra.get("raridade", d.get("raridade", "comum") if d.get("raridade") else "comum"),
						 "qualidade": extra.get("qualidade", "normal"), "gema": null}
			_proxima_inst += 1
			espacos[i] = inst
			falta -= 1
		mudou.emit()
		return falta
	var maximo := int(d.get("empilha", 99))
	var falta := qtd
	for e in espacos:
		if falta <= 0:
			break
		if e != null and e.id == id and e.qtd < maximo:
			var cabe: int = min(maximo - int(e.qtd), falta)
			e.qtd += cabe
			falta -= cabe
	while falta > 0:
		var i := espacos.find(null)
		if i < 0:
			break
		var cabe: int = min(maximo, falta)
		espacos[i] = {"id": id, "qtd": cabe}
		falta -= cabe
	mudou.emit()
	return falta


func contar(id: String) -> int:
	if missao.has(id):
		return int(missao[id])
	var n := 0
	for e in espacos:
		if e != null and e.id == id:
			n += int(e.qtd)
	return n


func tem(id: String, qtd: int = 1) -> bool:
	return contar(id) >= qtd


## Tira itens (das últimas pilhas primeiro); devolve quantos tirou.
func retirar(id: String, qtd: int = 1) -> int:
	if missao.has(id):
		var t: int = min(qtd, int(missao[id]))
		missao[id] = int(missao[id]) - t
		if missao[id] <= 0:
			missao.erase(id)
		mudou.emit()
		return t
	var tirado := 0
	for i in range(espacos.size() - 1, -1, -1):
		var e = espacos[i]
		if tirado >= qtd:
			break
		if e != null and e.id == id:
			var t: int = min(qtd - tirado, int(e.qtd))
			e.qtd -= t
			tirado += t
			if e.qtd <= 0:
				espacos[i] = null
	mudou.emit()
	return tirado


func retirar_espaco(i: int) -> Dictionary:
	var e = espacos[i]
	espacos[i] = null
	mudou.emit()
	return e if e else {}


func instancia(inst: String) -> Dictionary:
	for e in espacos:
		if e != null and e.get("inst", "") == inst:
			return e
	return {}


func livres() -> int:
	return espacos.count(null)


func peso() -> float:
	var p := 0.0
	for e in espacos:
		if e != null:
			p += float(_dados(e.id).get("peso", 0.1)) * int(e.qtd)
	return p


## Os materiais desde a última Zona Segura (para a regra de morrer: perdes 30%).
func materiais() -> Array:
	var r := []
	for e in espacos:
		if e != null and _dados(e.id).get("categoria", "") == "material":
			r.append(e)
	return r


func para_gravar() -> Dictionary:
	return {"espacos": espacos, "missao": missao, "barra_rapida": barra_rapida, "proxima_inst": _proxima_inst}


func carregar(d: Dictionary) -> void:
	var lista: Array = d.get("espacos", [])
	espacos.resize(max(lista.size(), 30))
	for i in espacos.size():
		espacos[i] = lista[i] if i < lista.size() else null
	missao = d.get("missao", {})
	barra_rapida = d.get("barra_rapida", barra_rapida)
	_proxima_inst = int(d.get("proxima_inst", 1))
	mudou.emit()
