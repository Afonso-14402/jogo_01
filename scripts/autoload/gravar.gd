extends Node
## Gravar e carregar (docs/PROGRAMACAO.md, secção 7): user://jogo_N.json, escrito primeiro para .tmp.

const VERSAO := 1


func caminho(espaco: int) -> String:
	return "user://jogo_%d.json" % espaco


func existe(espaco: int) -> bool:
	return FileAccess.file_exists(caminho(espaco))


func gravar(espaco: int) -> bool:
	var dados := Jogo.para_gravar()
	dados["versao"] = VERSAO
	dados["gravado"] = Time.get_datetime_string_from_system()
	dados["tempo"] = Tempo.para_gravar()
	var tmp := caminho(espaco) + ".tmp"
	var f := FileAccess.open(tmp, FileAccess.WRITE)
	if f == null:
		push_error("Gravar: não consegui escrever %s" % tmp)
		return false
	f.store_string(JSON.stringify(dados, "\t"))
	f.close()
	var dir := DirAccess.open("user://")
	if dir.file_exists(caminho(espaco).get_file()):
		dir.remove(caminho(espaco).get_file())
	return dir.rename(tmp.get_file(), caminho(espaco).get_file()) == OK


func carregar(espaco: int) -> bool:
	if not existe(espaco):
		return false
	var dados: Variant = JSON.parse_string(FileAccess.get_file_as_string(caminho(espaco)))
	if not dados is Dictionary:
		return false
	dados = _migrar(dados)
	Jogo.carregar(dados)
	Tempo.carregar(dados.get("tempo", {}))
	return true


## Gravações antigas passam para a versão atual.
func _migrar(dados: Dictionary) -> Dictionary:
	var v := int(dados.get("versao", 1))
	while v < VERSAO:
		v += 1
	dados["versao"] = VERSAO
	return dados
