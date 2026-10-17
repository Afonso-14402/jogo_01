class_name LuzHeroi
extends OmniLight3D
## A luz que o herói leva nas grutas (docs/regioes/r02_cavernas.md): sem nada vês 3 m; Tocha 5 m (3 min),
## Capacete de Mineiro 4 m, Poção de Luz 6 m (5 min), Morceguinho 6 m; Poção de Visão Noturna: vês tudo.

const SEM_LUZ := 3.0


static func raio() -> float:
	var r := SEM_LUZ
	if Jogo.buffs.has("luz"):
		r = maxf(r, float(Jogo.buffs.luz[0]))
	for e in Jogo.equipamento.values():
		if e is Dictionary and String(e.get("id", "")) == "capacete_mineiro":
			r = maxf(r, 4.0)
	if Jogo.animal == "morceguinho":
		r = maxf(r, 6.0)
	if Jogo.buffs.has("visao_noturna"):
		r = maxf(r, 10.0)
	return r


func _ready() -> void:
	light_color = Color("fbb954")
	light_energy = 1.3
	shadow_enabled = false
	position = Vector3(0, 1.6, 0)


func _process(_delta: float) -> void:
	var r := raio()
	omni_range = r + 2.0
	RenderingServer.global_shader_parameter_set("raio_jogador", r)
