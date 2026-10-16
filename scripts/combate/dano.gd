class_name Dano
extends RefCounted
## Calcula um golpe (docs/SISTEMAS.md, secção 4) e devolve um "golpe" (dicionário) para o alvo aplicar.
## golpe = {valor, critico, imune, elemento, magico, empurrao, origem (Vector3), atacante}

static var rng := RandomNumberGenerator.new()


## atq: ATQ já calculado do atacante · alvo_def: DEF ou RES do alvo · alvo: dicionário com fraquezas/resistências/imunidades
static func calcular(atq: float, mult_golpe: float, alvo_def: float, alvo: Dictionary, elemento: String = "",
		hipotese_critico: float = 0.0, dano_critico: float = 1.5, magico: bool = false) -> Dictionary:
	var c := Dados.constantes
	var mult_elem := Formulas.mult_elemento(c, elemento, alvo.get("fraquezas", []), alvo.get("resistencias", []),
			alvo.get("imunidades", []))
	if elemento != "":
		mult_elem *= float(alvo.get("elem_mult", {}).get(elemento, 1.0))   # ex.: Encharcado
	var critico := rng.randf() < hipotese_critico
	if alvo.get("atordoado", false):
		mult_golpe *= float(c.atordoado_mult)
	var valor := Formulas.dano(atq, mult_golpe, alvo_def, mult_elem, dano_critico if critico else 1.0,
			rng.randf_range(c.variacao_min, c.variacao_max))
	return {"valor": valor, "critico": critico, "imune": mult_elem <= 0.0, "elemento": elemento, "magico": magico,
			"fraco": mult_elem > 1.0}
