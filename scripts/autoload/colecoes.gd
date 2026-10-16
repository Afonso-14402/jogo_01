extends Node
## Coleções (docs/ATIVIDADES.md, secções 5–7): contadores, bestiário, páginas do diário do Aren, peixes, títulos e
## conquistas. Ouve os eventos do jogo, conta, e de segundo a segundo vê se ganhaste títulos ou conquistas novas.

var _pendente := false


func _ready() -> void:
	Eventos.monstro_morto.connect(func(id, _n):
		contar("monstros")
		Jogo.bestiario[id] = int(Jogo.bestiario.get(id, 0)) + 1
		_marcar())
	Eventos.item_apanhado.connect(func(_i, _q): _marcar())
	Eventos.andar_entrou.connect(func(_n): _marcar())
	Eventos.missao_mudou.connect(func(_m): _marcar())
	var t := Timer.new()
	t.wait_time = 1.0
	t.autostart = true
	t.timeout.connect(func():
		if _pendente:
			_pendente = false
			verificar())
	add_child(t)


func _marcar() -> void:
	_pendente = true


func contar(nome: String, n: int = 1) -> void:
	Jogo.contadores[nome] = int(Jogo.contadores.get(nome, 0)) + n
	_marcar()


func maximo(nome: String, valor: int) -> void:
	Jogo.contadores[nome] = maxi(int(Jogo.contadores.get(nome, 0)), valor)
	_marcar()


## Títulos e conquistas novos (as regras são condições: ver Condicoes).
func verificar() -> void:
	for t in Dados.tabela("titulos").values():
		if t.regra != "" and not t.id in Jogo.titulos and Condicoes.avaliar(t.regra if t.regra != "—" else ""):
			Jogo.titulos.append(t.id)
			Sistema.mensagem("Título novo: %s" % t.nome_pt, "nivel")
	for f in Jogo.flags:   # títulos dados pela história, missões e bosses (flag "titulo_<nome>")
		if f.begins_with("titulo_"):
			var tid := f.trim_prefix("titulo_")
			for t in Dados.tabela("titulos").values():
				if String(t.nome_pt).to_snake_case() == tid and not t.id in Jogo.titulos:
					Jogo.titulos.append(t.id)
	for c in Dados.tabela("conquistas").values():
		if c.regra != "" and not c.id in Jogo.conquistas and Condicoes.avaliar(c.regra):
			Jogo.conquistas.append(c.id)
			Sistema.mensagem("Conquista: %s! (%d/%d)" % [c.nome_pt, Jogo.conquistas.size(), Dados.tabela("conquistas").size()], "nivel")


## Página do diário do Aren encontrada.
func pagina(n: int) -> void:
	if n in Jogo.paginas:
		return
	Jogo.paginas.append(n)
	Jogo.paginas.sort()
	contar("paginas")
	Sistema.mensagem("Página do diário encontrada (%d/100)." % Jogo.paginas.size(), "nivel")


func peixe(id: String) -> void:
	if not Jogo.peixes.has(id):
		contar("especies_peixe")
	Jogo.peixes[id] = int(Jogo.peixes.get(id, 0)) + 1
	contar("peixes")
