extends Node
## Mensagens azuis do "Sistema" ([Sistema] ...). A interface (HUD) ouve Eventos.mensagem_sistema e mostra-as.

var historico: Array[String] = []


func mensagem(texto: String, tipo: String = "notificacao") -> void:
	var linha := "[Sistema] " + texto
	historico.append(linha)
	if historico.size() > 100:
		historico.pop_front()
	Eventos.mensagem_sistema.emit(linha, tipo)
	print(linha)
