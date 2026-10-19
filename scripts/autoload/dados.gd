extends Node
## Lê todos os ficheiros JSON de res://dados/ no arranque e dá acesso a eles.
## Ex.: Dados.c("esquiva_custo"), Dados.arma("espada_cobre"), Dados.lista("monstros").

const PASTA := "res://dados/"

var constantes: Dictionary = {}
var _tabelas: Dictionary = {}   # nome do ficheiro -> {id: dados} (listas) ou o dicionário tal como está


func _ready() -> void:
	carregar()


func carregar() -> void:
	_tabelas.clear()
	_ler_pasta(PASTA, "")
	constantes = _tabelas.get("constantes", {})


func _ler_pasta(caminho: String, prefixo: String) -> void:
	var dir := DirAccess.open(caminho)
	if dir == null:
		push_error("Dados: não consegui abrir %s" % caminho)
		return
	for ficheiro in dir.get_files():
		if ficheiro.ends_with(".json"):
			var nome := prefixo + ficheiro.get_basename()
			_tabelas[nome] = _indexar(ler_json(caminho + ficheiro))
	for sub in dir.get_directories():
		_ler_pasta(caminho + sub + "/", prefixo + sub + "/")


static func ler_json(caminho: String) -> Variant:
	var texto := FileAccess.get_file_as_string(caminho)
	var dados: Variant = JSON.parse_string(texto)
	if dados == null:
		push_error("Dados: JSON inválido em %s" % caminho)
		return {}
	return dados


## Uma lista de objetos com "id" passa a dicionário {id: objeto}; o resto fica como está.
static func _indexar(dados: Variant) -> Variant:
	if dados is Array and not dados.is_empty() and not (dados[0] is Dictionary and dados[0].has("id")):
		return dados   # lista sem ids (ex.: materiais_tier): fica lista
	if dados is Array:
		var d := {}
		for item in dados:
			if item is Dictionary and item.has("id"):
				d[item["id"]] = item
		return d
	return dados


func c(chave: String, padrao: Variant = null) -> Variant:
	if not constantes.has(chave):
		if padrao == null:
			push_warning("Dados: constante em falta: %s" % chave)
		return padrao
	return constantes[chave]


func tabela(nome: String) -> Dictionary:
	var t: Variant = _tabelas.get(nome, {})
	return t if t is Dictionary else {}


## Uma tabela que é uma lista simples (sem ids).
func lista_simples(nome: String) -> Array:
	var t: Variant = _tabelas.get(nome, [])
	return t if t is Array else []


func obter(nome_tabela: String, id: String) -> Dictionary:
	return tabela(nome_tabela).get(id, {})


func arma(id: String) -> Dictionary:
	return obter("armas", id)


func monstro(id: String) -> Dictionary:
	return obter("monstros", id)


func item(id: String) -> Dictionary:
	return obter("itens", id)
