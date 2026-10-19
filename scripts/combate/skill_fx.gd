class_name SkillFx
extends RefCounted
## O que se vê nas skills (do herói e dos companheiros): o círculo mágico ao preparar, a onda no chão das skills
## de área, a chuva (de flechas ou de estrelas), os cortes alternados, os fantasmas da investida e o grito.
## Arte: ferramentas/arte/efeitos.py (onda_*, conjurar_*, queda_*, grito).

const ELEMENTOS := ["fogo", "gelo", "raio", "veneno", "luz", "sombra"]


static func _el(el: String) -> String:
	return el if el in ELEMENTOS else "fisico"


static func tremer(arvore: SceneTree, forca: float, duracao: float = 0.18) -> void:
	var cam := arvore.root.get_viewport().get_camera_3d()
	if cam and cam.has_method("tremer"):
		cam.tremer(forca, duracao)


## Ao começar a skill: círculo mágico aos pés (magia, área, cura) ou um levantar de pó (golpes).
static func preparar(arvore: SceneTree, quem: Node3D, el: String, magica: bool) -> void:
	if magica:
		EfeitosCombate.animado(arvore, "conjurar_" + (el if el != "" else "luz"), quem.global_position + Vector3(0, 0.75, 0.05), 22.0)
	else:
		EfeitosCombate.animado(arvore, "poeira", quem.global_position + Vector3(0, 0.3, 0.1), 16.0)


## Onda que se espalha pelo chão até ao raio da skill (+ algumas explosões dentro) e a câmara treme.
static func onda(arvore: SceneTree, centro: Vector3, raio: float, el: String, explosoes: int = 3) -> void:
	var e := _el(el) if el != "cura" else "cura"
	var esc := clampf(roundf(raio * 2.0 * 16.0 / 44.0), 1.0, 4.0)   # o anel do desenho tem ~44 px de largura
	EfeitosCombate.animado(arvore, "onda_" + e, centro + Vector3(0, 10.0 * esc / 16.0, 0.05), 16.0, false, esc)
	if e == "cura":
		return
	for k in explosoes:
		var a := randf() * TAU
		var d := randf_range(0.2, 0.8) * raio
		EfeitosCombate.animado(arvore, "explosao_" + e, centro + Vector3(cos(a) * d, 0.6, sin(a) * d * 0.6), 20.0)
	tremer(arvore, 0.12 + 0.03 * raio)


## Chuva sobre uma zona: flechas (físico) ou estrelas (magia), a cair umas atrás das outras.
static func chuva(arvore: SceneTree, centro: Vector3, raio: float, el: String, n: int = 6) -> void:
	var nome := "queda_flecha" if el == "" else "queda_estrela"
	for k in n:
		var a := randf() * TAU
		var d := sqrt(randf()) * raio
		EfeitosCombate.animado(arvore, nome, centro + Vector3(cos(a) * d, 1.0, sin(a) * d * 0.6), 14.0 + randf() * 6.0)
	if el != "":
		EfeitosCombate.animado(arvore, "explosao_" + _el(el), centro + Vector3(0, 0.6, 0), 18.0)


## Um dos cortes de uma skill de vários golpes: alternam de lado e de altura (parece uma sequência de golpes).
static func corte_multi(arvore: SceneTree, pos: Vector3, dir: Vector3, k: int) -> void:
	var alto := 1.15 if k % 2 == 0 else 0.75
	var esp := (dir.x < 0.0) != (k % 2 == 1)
	EfeitosCombate.animado(arvore, "corte" if k % 3 != 2 else "corte_pesado", pos + Vector3(randf_range(-0.3, 0.3), alto, 0.05), 32.0, esp)


## Investida: fantasmas do boneco pelo caminho (chamar várias vezes durante a corrida) e pó ao partir.
static func fantasma(boneco: BonecoArma, el: String = "") -> void:
	var cores := {"fogo": Color(1.0, 0.6, 0.3, 0.55), "gelo": Color(0.6, 0.85, 1.0, 0.55), "raio": Color(1.0, 0.95, 0.4, 0.55),
		"veneno": Color(0.6, 1.0, 0.5, 0.55), "luz": Color(1.0, 1.0, 0.7, 0.55), "sombra": Color(0.7, 0.5, 1.0, 0.55)}
	boneco.fantasma(cores.get(el, Color(0.75, 0.85, 1.0, 0.5)))


## Provocar: grito vermelho por cima da cabeça.
static func grito(arvore: SceneTree, quem: Node3D) -> void:
	EfeitosCombate.animado(arvore, "grito", quem.global_position + Vector3(0, 1.9, 0.1), 12.0)
	EfeitosCombate.animado(arvore, "onda_fogo", quem.global_position + Vector3(0, 0.62, 0.05), 16.0, false, 2.0)
	tremer(arvore, 0.1)
