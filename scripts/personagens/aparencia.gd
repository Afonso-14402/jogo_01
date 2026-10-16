class_name Aparencia
extends RefCounted
## Aspeto do herói (docs/INTERFACE.md, secção 6): 8 penteados (folhas próprias em arte/heroi/aparencia/) e trocas de
## cor de pele, cabelo, olhos e roupa (arte/heroi/paletas.json, cores-índice) feitas nas imagens ao carregar.

const PALETAS := "res://arte/heroi/paletas.json"
static var _paletas: Dictionary = {}
static var _cache: Dictionary = {}


static func paletas() -> Dictionary:
	if _paletas.is_empty():
		var d: Variant = Dados.ler_json(PALETAS)
		_paletas = d if d is Dictionary else {}
	return _paletas


static func opcoes(parte: String) -> Array:
	var p: Variant = paletas().get(parte, [])
	return p.keys() if p is Dictionary else p


## As animações do herói com este aspeto: as folhas do penteado (heroi_<anim>_<dir>_<penteado>.png) com as cores-índice
## trocadas na própria imagem (exato, sem shader). Fica em cache por aspeto.
static func frames(ap: Dictionary, anims: Dictionary, dirs: Array) -> SpriteFrames:
	var penteado: String = ap.get("penteado", "espetado")
	var chave := str(ap) + str(anims.keys())
	if _cache.has(chave):
		return _cache[chave]
	var troca := mapa_cores(ap)
	var sf := SpriteFrames.new()
	sf.remove_animation("default")
	for nome in anims:
		for d in dirs:
			var caminho := "res://arte/heroi/aparencia/heroi_%s_%s_%s.png" % [nome, d, penteado]
			if not ResourceLoader.exists(caminho):
				continue
			var img: Image = (load(caminho) as Texture2D).get_image()
			img.convert(Image.FORMAT_RGBA8)
			for y in img.get_height():
				for x in img.get_width():
					var c := img.get_pixel(x, y)
					if c.a > 0.0:
						var k := c.to_html(false)
						if troca.has(k):
							img.set_pixel(x, y, troca[k])
			var tex := ImageTexture.create_from_image(img)
			var lado := tex.get_height()
			var a := "%s_%s" % [nome, d]
			sf.add_animation(a)
			sf.set_animation_speed(a, anims[nome][0])
			sf.set_animation_loop(a, anims[nome][1])
			for i in range(tex.get_width() / lado):
				var at := AtlasTexture.new()
				at.atlas = tex
				at.region = Rect2(i * lado, 0, lado, lado)
				sf.add_frame(a, at)
	_cache[chave] = sf
	return sf


## Cor-índice (html) -> cor escolhida.
static func mapa_cores(ap: Dictionary) -> Dictionary:
	var p := paletas()
	var ind: Dictionary = p.get("indices", {})
	var m := {}
	var juntar := func(origem: Array, destino: Array):
		for i in mini(origem.size(), destino.size()):
			m[Color(origem[i]).to_html(false)] = Color(destino[i])
	juntar.call(ind.get("pele", []), p.get("pele", {}).get(ap.get("pele", "clara"), ind.get("pele", [])))
	juntar.call(ind.get("cabelo", []), p.get("cabelo", {}).get(ap.get("cabelo", "castanho_avermelhado"), []))
	juntar.call([ind.get("olhos", "#000000")], [p.get("olhos", {}).get(ap.get("olhos", "preto"), "#2e222f")])
	var roupa: Dictionary = p.get("roupa", {}).get(ap.get("roupa", "aventureiro"), {})
	for parte in ind.get("roupa", {}):
		juntar.call(ind.roupa[parte], roupa.get(parte, ind.roupa[parte]))
	return m


## Retrato do herói com o aspeto escolhido (arte/retratos/heroi/<penteado>_<emocao>.png com cores-índice).
static func retrato(ap: Dictionary, emocao: String = "normal") -> Texture2D:
	var chave := "retrato" + str(ap) + emocao
	if _cache.has(chave):
		return _cache[chave]
	var caminho := "res://arte/retratos/heroi/%s_%s.png" % [ap.get("penteado", "espetado"), emocao]
	if not ResourceLoader.exists(caminho):
		return load("res://arte/retratos/heroi_%s.png" % emocao)
	var ind: Variant = Dados.ler_json("res://arte/retratos/heroi/indices.json")
	var p := paletas()
	var troca := {}
	var pele: Array = p.get("pele", {}).get(ap.get("pele", "clara"), [])
	var cab: Array = p.get("cabelo", {}).get(ap.get("cabelo", "castanho_avermelhado"), [])
	for i in ind.pele.size():
		troca[Color(ind.pele[i]).to_html(false)] = Color(pele[int(ind.mapa_pele[i])])
	for i in ind.cabelo.size():
		troca[Color(ind.cabelo[i]).to_html(false)] = Color(cab[int(ind.mapa_cabelo[i])])
	troca[Color(ind.olhos).to_html(false)] = Color(p.get("olhos", {}).get(ap.get("olhos", "preto"), "#2e222f"))
	var img: Image = (load(caminho) as Texture2D).get_image()
	img.convert(Image.FORMAT_RGBA8)
	for y in img.get_height():
		for x in img.get_width():
			var c := img.get_pixel(x, y)
			if c.a > 0.0 and troca.has(c.to_html(false)):
				img.set_pixel(x, y, troca[c.to_html(false)])
	var t := ImageTexture.create_from_image(img)
	_cache[chave] = t
	return t
