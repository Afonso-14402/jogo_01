class_name Sombra2D
extends RefCounted
## Sombra redonda no chão, em pixel art (uma elipse escura meio transparente debaixo dos pés).

static var _cache: Dictionary = {}


static func criar(raio_m: float) -> Sprite2D:
	var r := maxi(3, int(round(raio_m * Chao2D.PX)))
	if not _cache.has(r):
		var ry := maxi(2, int(round(r * 0.45)))
		var img := Image.create(r * 2 + 1, ry * 2 + 1, false, Image.FORMAT_RGBA8)
		for y in ry * 2 + 1:
			for x in r * 2 + 1:
				var dx := float(x - r) / r
				var dy := float(y - ry) / ry
				if dx * dx + dy * dy <= 1.0:
					img.set_pixel(x, y, Color(0.18, 0.13, 0.18, 0.38))
		_cache[r] = ImageTexture.create_from_image(img)
	var s := Sprite2D.new()
	s.texture = _cache[r]
	s.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	return s
