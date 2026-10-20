extends Node
## Mensagens azuis do "Sistema" ([Sistema] ...). A interface (HUD) ouve Eventos.mensagem_sistema e mostra-as.

var historico: Array[String] = []


func mensagem(texto: String, tipo: String = "notificacao") -> void:
	var linha := "[Sistema] " + Entrada.teclas(genero(texto))
	historico.append(linha)
	if historico.size() > 100:
		historico.pop_front()
	Eventos.mensagem_sistema.emit(linha, tipo)
	print(linha)


## Palavras com género: "{o/a}" -> "o" (tratamento "ele") ou "a" ("ela") (docs/dialogos/README.md).
static func genero(texto: String) -> String:
	var re := RegEx.new()
	re.compile("\\{([^/{}]*)/([^/{}]*)\\}")
	var ela: bool = Jogo.tratamento == "ela"
	var out := texto
	for m in re.search_all(texto):
		out = out.replace(m.get_string(0), m.get_string(2) if ela else m.get_string(1))
	return out
