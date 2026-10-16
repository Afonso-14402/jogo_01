extends Node
## Relógio do jogo: 1 hora de jogo = "hora_em_segundos" segundos reais (docs/SISTEMAS.md, secção 14).
## Calendário: 4 estações de 28 dias, semanas de Segunda a Domingo. Clima do dia (14.1 e o clima das regiões).

signal nova_hora(hora: int)
signal novo_dia(dia: int)
signal nova_estacao(estacao: String)

const ESTACOES := ["primavera", "verao", "outono", "inverno"]
const NOMES_ESTACOES := ["Primavera", "Verão", "Outono", "Inverno"]
const DIAS_SEMANA := ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
const DIAS_POR_ESTACAO := 28

var hora: float = 6.0
var dia: int = 1
var estacao: int = 0
var ano: int = 1
var parado: bool = false
var cansado: bool = false        # às 2:00 sem dormir: −20% em tudo até dormires


func _process(delta: float) -> void:
	if parado:
		return
	var antes := int(hora)
	hora += delta / float(Dados.c("hora_em_segundos", 50))
	if int(hora) != antes:
		if hora >= 24.0:
			hora -= 24.0
			_passar_dia()
		var h := int(hora)
		if h == int(Dados.c("hora_cansado", 2)) and not cansado:
			cansado = true
			Sistema.mensagem("Estás cansad{o/a}. Vai dormir: −20% em tudo até descansares.", "aviso")
			Eventos.stats_mudaram.emit()
		nova_hora.emit(h)


func _passar_dia() -> void:
	dia += 1
	if dia > DIAS_POR_ESTACAO:
		dia = 1
		estacao = (estacao + 1) % ESTACOES.size()
		if estacao == 0:
			ano += 1
		nova_estacao.emit(nome_estacao())
	novo_dia.emit(dia)


## Dormir: salta para as 6:00 do dia seguinte e tira o cansaço (gravar fica com quem chama: camas e cristais).
func dormir() -> void:
	if hora >= 6.0:
		_passar_dia()
	hora = 6.0
	cansado = false
	Eventos.stats_mudaram.emit()
	nova_hora.emit(6)


func nome_estacao() -> String:
	return ESTACOES[estacao]


func dia_semana() -> String:
	return DIAS_SEMANA[(dia - 1) % 7]


func e_domingo() -> bool:
	return (dia - 1) % 7 == 6


func e_noite() -> bool:
	return hora >= 20.0 or hora < 6.0


## dia · entardecer · noite · madrugada (secção 14)
func periodo() -> String:
	if hora >= 6.0 and hora < 18.0:
		return "dia"
	if hora >= 18.0 and hora < 20.0:
		return "entardecer"
	if hora >= 5.0 and hora < 6.0:
		return "madrugada"
	return "noite"


func texto_hora() -> String:
	return "%02d:%02d" % [int(hora), int((hora - int(hora)) * 60.0)]


func texto_data() -> String:
	return "%s, %d de %s" % [dia_semana(), dia, NOMES_ESTACOES[estacao]]


## O tempo atmosférico de hoje: regiao 0 = cidade (pela estação), 1–10 = o clima da região.
## É sempre o mesmo para o mesmo dia (semente pelo dia), para não mudar ao entrar e sair.
func clima(regiao: int = 0) -> Dictionary:
	var c: Dictionary = Dados.tabela("clima")
	var lista: Array = c.get("regioes", {}).get(str(regiao), []) if regiao > 0 else c.get("estacoes", {}).get(nome_estacao(), [])
	if lista.is_empty():
		return {"nome_pt": "Sol", "efeito": "sol"}
	var rng := RandomNumberGenerator.new()
	rng.seed = hash([ano, estacao, dia, regiao])
	var x := rng.randf()
	for t in lista:
		if t.get("so_noite", false) and not e_noite():
			continue
		x -= float(t.hipotese)
		if x <= 0.0:
			return t
	return lista[0]


func para_gravar() -> Dictionary:
	return {"hora": hora, "dia": dia, "estacao": nome_estacao(), "ano": ano, "cansado": cansado}


func carregar(d: Dictionary) -> void:
	hora = d.get("hora", 6.0)
	dia = d.get("dia", 1)
	estacao = max(0, ESTACOES.find(d.get("estacao", "primavera")))
	ano = d.get("ano", 1)
	cansado = d.get("cansado", false)
