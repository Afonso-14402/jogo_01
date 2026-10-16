extends Node
## Relógio do jogo: 1 hora de jogo = "hora_em_segundos" segundos reais (docs/SISTEMAS.md, secção 14).

signal nova_hora(hora: int)
signal novo_dia(dia: int)
signal nova_estacao(estacao: String)

const ESTACOES := ["primavera", "verao", "outono", "inverno"]
const DIAS_POR_ESTACAO := 28

var hora: float = 6.0
var dia: int = 1
var estacao: int = 0
var ano: int = 1
var parado: bool = false


func _process(delta: float) -> void:
	if parado:
		return
	var antes := int(hora)
	hora += delta / float(Dados.c("hora_em_segundos", 50))
	if int(hora) != antes:
		if hora >= 24.0:
			hora -= 24.0
			_passar_dia()
		nova_hora.emit(int(hora))


func _passar_dia() -> void:
	dia += 1
	if dia > DIAS_POR_ESTACAO:
		dia = 1
		estacao = (estacao + 1) % ESTACOES.size()
		if estacao == 0:
			ano += 1
		nova_estacao.emit(nome_estacao())
	novo_dia.emit(dia)


func nome_estacao() -> String:
	return ESTACOES[estacao]


func e_noite() -> bool:
	return hora >= 20.0 or hora < 6.0


func texto_hora() -> String:
	return "%02d:%02d" % [int(hora), int((hora - int(hora)) * 60.0)]


func para_gravar() -> Dictionary:
	return {"hora": hora, "dia": dia, "estacao": nome_estacao(), "ano": ano}


func carregar(d: Dictionary) -> void:
	hora = d.get("hora", 6.0)
	dia = d.get("dia", 1)
	estacao = max(0, ESTACOES.find(d.get("estacao", "primavera")))
	ano = d.get("ano", 1)
