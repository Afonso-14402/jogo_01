extends JanelaUI
## Janela de loja (docs/LOJAS.md; docs/INTERFACE.md, secção 5): Comprar / Vender, com o retrato do dono.
## Vende-se tudo a 30%. Descontos de amizade: 5% com 2 corações, 15% com 8. O stock renova-se às 6:00.

var loja: Dictionary = {}
var _lista: VBoxContainer
var _titulo: Label
var _retrato: TextureRect
var _aba := "comprar"


func _ready() -> void:
	add_to_group("janelas")
	add_to_group("loja_ui")
	_criar_janela(Vector2(200, 60), Vector2(880, 600))
	_retrato = _icone("", 72)
	_retrato.position = Vector2(16, 12)
	_janela.add_child(_retrato)
	_titulo = _texto(_janela, Vector2(100, 16), 18, Color("8fd3ff"))
	var abas := HBoxContainer.new()
	abas.position = Vector2(100, 50)
	_janela.add_child(abas)
	_botao("Comprar", func(): _aba = "comprar"; _mostrar(), abas)
	_botao("Vender", func(): _aba = "vender"; _mostrar(), abas)
	_botao("Sair", func(): abrir(false), abas)
	var rolar := ScrollContainer.new()
	rolar.position = Vector2(20, 96)
	rolar.size = Vector2(840, 490)
	_janela.add_child(rolar)
	_lista = VBoxContainer.new()
	_lista.custom_minimum_size = Vector2(820, 0)
	rolar.add_child(_lista)


func abrir_loja(dono: String) -> void:
	loja = {}
	for l in Dados.tabela("lojas").values() + Dados.tabela("lojas_povoacoes").values():
		if l.dono == dono:
			loja = l
	if loja.is_empty():
		return
	var h: Array = loja.get("horario", [0, 24])
	if not _aberta(h):
		Sistema.mensagem("Está fechado. Abre às %d:00." % int(h[0]), "aviso")
		return
	_aba = "comprar"
	abrir(true)


static func _aberta(h: Array) -> bool:
	var a := int(h[0])
	var f := int(h[1])
	var hora := Tempo.hora
	return (hora >= a and hora < f) if a < f else (hora >= a or hora < f)


## Desconto de amizade com o dono da loja.
static func desconto(dono: String) -> float:
	var c := Amizade.coracoes(dono)
	if c >= 8:
		return float(Dados.c("desconto_8_coracoes", 0.15))
	if c >= 2:
		return float(Dados.c("desconto_2_coracoes", 0.05))
	return 0.0


## O que está à venda hoje: [{item, preco, stock}] (as linhas "auto" da forja dão as armas e armaduras do tier).
static func a_venda(l: Dictionary) -> Array:
	var r := []
	for it in l.get("itens", []):
		if Condicoes.avaliar(it.get("cond", "")):
			r.append(it)
	var tier := clampi((Jogo.andar_maximo - 1) / 10 + 1, 1, 10)
	var metais := Crafting.METAIS
	for a in l.get("auto", []):
		match a:
			"armas":
				for arma in Dados.tabela("armas").values():
					if int(arma.get("tier", 99)) <= tier and arma.get("categoria", "normal") in ["normal", ""] and not arma.get("unica", false):
						r.append({"item": arma.id, "preco": int(arma.get("preco", 100)), "stock": -1})
			"armaduras":
				for it in Dados.tabela("itens").values():
					if it.has("espaco") and int(it.get("tier", 99)) <= tier:
						r.append({"item": it.id, "preco": int(it.get("preco", 60)), "stock": -1})
			"ferramentas":
				for t in tier:
					for f in ["picareta_", "machado_lenhador_"]:
						if not Dados.item(f + metais[t]).is_empty():
							r.append({"item": f + metais[t], "preco": int(Dados.item(f + metais[t]).get("preco", 90)) if int(Dados.item(f + metais[t]).get("preco", 0)) > 0 else 90 * (t + 1) * (t + 1), "stock": -1})
			"lingotes":
				for t in tier:
					var mt: Dictionary = Dados.lista_simples("materiais_tier")[t]
					r.append({"item": mt.lingote, "preco": int(Dados.c("preco_lingote_tier", 30)) * (t + 1) * (t + 1), "stock": int(Dados.c("loja_lingotes_por_dia", 10))})
	return r


func _stock(id: String, base: int) -> int:
	if base < 0:
		return -1
	var dia := Amizade.dia_absoluto()
	var chave := "%s:%s" % [loja.id, id]
	var reg: Dictionary = Jogo.stock_lojas.get(chave, {})
	if int(reg.get("dia", -1)) != dia:
		reg = {"dia": dia, "resta": base}
		Jogo.stock_lojas[chave] = reg
	return int(reg.resta)


func _mostrar() -> void:
	_limpar(_lista)
	var dono: String = loja.get("dono", "")
	_retrato.texture = load("res://arte/retratos/%s_feliz.png" % dono) if ResourceLoader.exists("res://arte/retratos/%s_feliz.png" % dono) else null
	var d := desconto(dono)
	_titulo.text = "%s   ·   %d ouro%s" % [loja.get("nome_pt", ""), Jogo.ouro, ("   ·   desconto %d%%" % int(d * 100)) if d > 0 else ""]
	if _aba == "comprar":
		for it in a_venda(loja):
			var st := _stock(it.item, int(it.get("stock", -1)))
			var preco := int(round(int(it.preco) * (1.0 - d)))
			var dd := Inventario._dados(it.item)
			var h := HBoxContainer.new()
			_lista.add_child(h)
			h.add_child(_icone(dd.get("icone", ""), 28))
			var l := _texto(h, Vector2.ZERO, 14)
			l.text = "  %s" % dd.get("nome_pt", it.item)
			l.custom_minimum_size = Vector2(420, 0)
			var p := _texto(h, Vector2.ZERO, 14, Color("f9c22b"))
			p.text = "%d ouro" % preco
			p.custom_minimum_size = Vector2(110, 0)
			var s := _texto(h, Vector2.ZERO, 12, Color("9babb2"))
			s.text = "∞" if st < 0 else "×%d" % st
			s.custom_minimum_size = Vector2(50, 0)
			var b := _botao("Comprar", func(): _comprar(it, preco), h)
			b.disabled = Jogo.ouro < preco or st == 0
	else:
		if not loja.get("compra", true):
			_texto(_lista, Vector2.ZERO, 14, Color("9babb2")).text = "Esta loja não compra nada."
			return
		var vistos := []
		for e in Jogo.inventario.espacos:
			if e == null or e.id in vistos or Inventario._dados(e.id).get("categoria", "") == "missao":
				continue
			vistos.append(e.id)
			var dd := Inventario._dados(e.id)
			var valor := preco_venda(e.id)
			var h := HBoxContainer.new()
			_lista.add_child(h)
			h.add_child(_icone(dd.get("icone", ""), 28))
			var l := _texto(h, Vector2.ZERO, 14)
			l.text = "  %s ×%d" % [dd.get("nome_pt", e.id), Jogo.inventario.contar(e.id)]
			l.custom_minimum_size = Vector2(470, 0)
			var p := _texto(h, Vector2.ZERO, 14, Color("f9c22b"))
			p.text = "%d ouro" % valor
			p.custom_minimum_size = Vector2(110, 0)
			var b := _botao("Vender", func(): _vender(e.id, valor), h)
			b.disabled = valor <= 0


static func preco_venda(id: String) -> int:
	var d := Inventario._dados(id)
	var p := int(d.get("preco", 0))
	if p <= 0 and d.get("categoria", "") == "material":
		p = 8 * Crafting.tier(id) * Crafting.tier(id)
	return int(p * float(Dados.c("venda_percent", 0.3)))


func _comprar(it: Dictionary, preco: int) -> void:
	if Jogo.ouro < preco:
		Audio.efeito("sem_dinheiro", 0.0)
		return
	Audio.efeito("comprar", 0.0)
	if not Jogo.apanhar(it.item, 1):
		return
	Jogo.ouro -= preco
	var chave := "%s:%s" % [loja.id, it.item]
	if Jogo.stock_lojas.has(chave) and int(Jogo.stock_lojas[chave].resta) > 0:
		Jogo.stock_lojas[chave].resta = int(Jogo.stock_lojas[chave].resta) - 1
	Eventos.ouro_mudou.emit(Jogo.ouro)
	_mostrar()


func _vender(id: String, valor: int) -> void:
	if Jogo.inventario.retirar(id, 1) == 1:
		Audio.efeito("vender", 0.0)
		Jogo.ganhar_ouro(valor)
	_mostrar()
