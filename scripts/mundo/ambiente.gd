class_name Ambiente
extends RefCounted
## Luz do sol e ambiente (céu, nevoeiro, glow) de um andar ou da cidade.


static func criar(pai: Node, ceu := Color("7fa0c8"), nevoeiro := Color("c8e0d0"), densidade: float = 0.01, luz_ambiente: float = 0.6,
		regiao: int = 0, fechado: bool = false) -> DirectionalLight3D:
	var env := Environment.new()
	env.background_mode = Environment.BG_COLOR
	env.background_color = ceu
	env.ambient_light_source = Environment.AMBIENT_SOURCE_COLOR
	env.ambient_light_color = ceu.lerp(Color.WHITE, 0.25)
	env.ambient_light_energy = luz_ambiente * 0.55
	env.fog_enabled = densidade > 0.0
	env.fog_light_color = nevoeiro.lerp(ceu, 0.5)
	env.fog_density = densidade * 0.35
	env.fog_sky_affect = 0.0
	env.glow_enabled = true
	env.glow_intensity = 0.35
	env.glow_hdr_threshold = 1.4
	env.tonemap_mode = Environment.TONE_MAPPER_LINEAR
	var we := WorldEnvironment.new()
	we.environment = env
	pai.add_child(we)
	var sol := DirectionalLight3D.new()
	sol.rotation_degrees = Vector3(-55, -30, 0)
	sol.light_energy = 0.75
	sol.light_color = Color("fff4e0")
	sol.shadow_enabled = true
	sol.directional_shadow_max_distance = 60.0
	pai.add_child(sol)
	var ciclo := CicloDia.new()   # dia e noite + clima
	ciclo.env = env
	ciclo.sol = sol
	ciclo.ceu = ceu
	ciclo.nevoeiro = nevoeiro
	ciclo.densidade = densidade
	ciclo.luz = luz_ambiente
	ciclo.regiao = regiao
	ciclo.fechado = fechado
	pai.add_child(ciclo)
	return sol
