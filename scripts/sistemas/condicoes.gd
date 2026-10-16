class_name Condicoes
extends RefCounted
## Avalia as condições dos diálogos e das missões (docs/dialogos/README.md, secção 3).
## Ex.: "clima == chuva && hora entre 20 e 23" · "coracoes(lyra) >= 4" · "!flag(kai_salvo)" · "missao(N_LYRA_1) == concluida"
## Uma condição que o jogo não sabe ler conta como falsa (para não dizer falas fora de sítio).

const RANKS := ["F", "E", "D", "C", "B", "A", "S", "SS", "SSS"]
static var _re: RegEx


static func avaliar(expr: String) -> bool:
	var e := expr.strip_edges().trim_prefix("`").trim_suffix("`")
	if e == "" or e == "—" or e == "-":
		return true
	for ou in e.split("||"):
		var todas := true
		for a in ou.split("&&"):
			if not _atomo(a.strip_edges()):
				todas = false
				break
		if todas:
			return true
	return false


static func _atomo(a: String) -> bool:
	if _re == null:
		_re = RegEx.new()
		_re.compile("^(!)?\\s*(\\w+)(?:\\(([^)]*)\\))?\\s*(?:(==|!=|>=|<=|>|<)\\s*(\\S+)|entre\\s+(\\d+)\\s+e\\s+(\\d+))?$")
	var m := _re.search(a)
	if m == null:
		return false
	var nao := m.get_string(1) == "!"
	var nome := m.get_string(2)
	var arg := m.get_string(3)
	var op := m.get_string(4)
	var alvo := m.get_string(5)
	var r: bool
	if m.get_string(6) != "":   # "hora entre 6 e 10" (inclui as duas pontas, até ao fim da última hora)
		var v := float(valor(nome, arg))
		r = v >= float(m.get_string(6)) and v < float(m.get_string(7)) + 1.0
	elif op == "":
		r = bool(valor(nome, arg))
	else:
		r = comparar(valor(nome, arg), op, alvo, nome)
	return r != nao


static func comparar(v: Variant, op: String, alvo: String, nome: String) -> bool:
	if nome == "rank":
		var a := RANKS.find(str(v))
		var b := RANKS.find(alvo)
		v = a
		alvo = str(b)
	if v is String or v is StringName:
		match op:
			"==": return str(v) == alvo
			"!=": return str(v) != alvo
		return false
	var x := float(v)
	var y := float(alvo)
	match op:
		"==": return is_equal_approx(x, y)
		"!=": return not is_equal_approx(x, y)
		">=": return x >= y
		"<=": return x <= y
		">": return x > y
		"<": return x < y
	return false


## O valor de uma variável do jogo.
static func valor(nome: String, arg: String = "") -> Variant:
	match nome:
		"estacao": return Tempo.nome_estacao()
		"dia_semana": return Tempo.dia_semana().to_lower().replace("ç", "c")
		"clima": return String(Tempo.clima(0).get("efeito", "sol")).replace("nevao", "neve")
		"hora": return Tempo.hora
		"dia": return Tempo.dia
		"coracoes": return Amizade.coracoes(arg)
		"amizade": return Amizade.pontos(arg)
		"andar_maximo": return Jogo.andar_maximo
		"andar": return Jogo.andar_atual
		"boss_derrotado": return Jogo.tem_flag("boss_" + arg)
		"missao": return Jogo.estado_missao(arg)
		"flag": return Jogo.tem_flag(arg)
		"origem": return Jogo.origem
		"skill_unica": return Jogo.skill_unica
		"classe":
			var linha := Progressao.linha_classes(Jogo.classe)
			return linha[0].id if not linha.is_empty() else "aventureiro"
		"arma_tipo": return Dados.arma(Jogo.arma_equipada).get("tipo", "")
		"vida_pct": return 100.0 * Jogo.hp / max(1.0, float(Jogo.hp_maximo()))
		"estado":
			if arg == "cansado":
				return Tempo.cansado
			var est: String = {"amaldicoado": "maldicao", "encharcado": "encharcado", "molhado": "encharcado"}.get(arg, arg)
			return Jogo.estados != null and is_instance_valid(Jogo.estados) and Jogo.estados.tem(est)
		"companheiro": return arg in Jogo.companheiros
		"animal": return Jogo.animal if Jogo.animal != "" else "nenhum"
		"rank": return Jogo.rank()
		"nivel": return Jogo.nivel
		"capitulo": return Jogo.capitulo()
		"tratamento": return Jogo.tratamento
	return null
