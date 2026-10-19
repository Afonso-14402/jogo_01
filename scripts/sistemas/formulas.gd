class_name Formulas
extends RefCounted
## Todas as fórmulas de docs/SISTEMAS.md, sem estado (fáceis de testar).
## "c" é o dicionário das constantes (Dados.constantes).


# ---------------- jogador (secção 2) ----------------

static func hp_maximo(c: Dictionary, vit: int, nivel: int, bonus: int = 0) -> int:
	return int(c.hp_base + vit * c.hp_por_vit + nivel * c.hp_por_nivel + bonus)


static func mp_maximo(c: Dictionary, intel: int, nivel: int) -> int:
	return int(c.mp_base + intel * c.mp_por_int + nivel * c.mp_por_nivel)


static func estamina_maxima(c: Dictionary, agi: int) -> int:
	return int(min(c.estamina_base + agi * c.estamina_por_agi, c.estamina_maxima))


static func velocidade(c: Dictionary, agi: int) -> float:
	return min(c.velocidade_base * (1.0 + agi * c.velocidade_por_agi), c.velocidade_maxima)


static func critico(c: Dictionary, des: int, sor: int, arma: float = 0.0) -> float:
	return min(c.critico_base + des * c.critico_por_des + sor * c.critico_por_sor + arma, c.critico_maximo)


static func defesa(c: Dictionary, armaduras: float, vit: int) -> float:
	return armaduras + vit * c.def_por_vit


static func resistencia(c: Dictionary, armaduras: float, vit: int, intel: int) -> float:
	return armaduras + vit * c.res_por_vit + intel * c.res_por_int


static func carga_maxima(c: Dictionary, forca: int) -> float:
	return c.carga_base + forca * c.carga_por_for


# ---------------- níveis e XP (secção 3) ----------------

static func xp_para_subir(c: Dictionary, nivel: int) -> int:
	return int(round(c.xp_base * pow(nivel, c.xp_expoente) + c.xp_soma))


static func xp_monstro(c: Dictionary, nivel: int, mult_tipo: float = 1.0) -> int:
	return int(round((c.xp_monstro_base + c.xp_monstro_mult * pow(nivel, c.xp_monstro_expoente)) * mult_tipo))


## XP que o jogador recebe (só 20% se o monstro tiver 5+ níveis abaixo).
static func xp_recebida(c: Dictionary, nivel_jogador: int, nivel_monstro: int, mult_tipo: float = 1.0) -> int:
	var xp := xp_monstro(c, nivel_monstro, mult_tipo)
	if nivel_jogador - nivel_monstro >= c.xp_nivel_baixo_diferenca:
		xp = int(xp * c.xp_nivel_baixo_mult)
	return max(1, xp)


# ---------------- combate (secção 4) ----------------

static func atq_fisico(c: Dictionary, atq_arma: float, melhoria: int, raridade: float, forca: int, des: int, distancia: bool) -> float:
	var base: float = atq_arma * (1.0 + melhoria * c.melhoria_bonus) * raridade
	return base + (des * c.atq_por_des if distancia else forca * c.atq_por_for)


static func atq_magico(c: Dictionary, atq_arma: float, melhoria: int, raridade: float, intel: int) -> float:
	return atq_arma * (1.0 + melhoria * c.melhoria_bonus) * raridade + intel * c.atq_magico_por_int


## Multiplicador do elemento contra um alvo: "fraco" ×1,5, "resiste" ×0,5, "imune" ×0.
static func mult_elemento(c: Dictionary, elemento: String, fraquezas: Array, resistencias: Array, imunidades: Array) -> float:
	if elemento == "" or elemento == "fisico":
		return 1.0
	if elemento in imunidades:
		return 0.0
	if elemento in fraquezas:
		return c.elemento_fraco
	if elemento in resistencias:
		return c.elemento_resiste
	return 1.0


## Dano final. defesa_alvo é a DEF (físico) ou a RES (mágico). variacao vem de fora para os testes serem certos.
static func dano(atq: float, mult_golpe: float, defesa_alvo: float, mult_elem: float, mult_critico: float, variacao: float) -> int:
	if mult_elem <= 0.0:
		return 0
	var d := atq * mult_golpe * 100.0 / (100.0 + defesa_alvo) * mult_elem * mult_critico * variacao
	return max(1, int(floor(d)))


# ---------------- monstros (secção 6) ----------------

static func monstro_hp(c: Dictionary, nivel: int, mult: float = 1.0) -> int:
	var k: Array = c.monstro_hp
	return int((k[0] + k[1] * nivel + k[2] * nivel * nivel) * mult)


static func monstro_atq(c: Dictionary, nivel: int, mult: float = 1.0) -> float:
	var k: Array = c.monstro_atq   # [base, por nível, por nível²] (o termo ao quadrado aperta os andares altos)
	return (k[0] + k[1] * nivel + (float(k[2]) * nivel * nivel if k.size() > 2 else 0.0)) * mult


static func monstro_def(c: Dictionary, nivel: int, mult: float = 1.0) -> float:
	return nivel * c.monstro_def * mult


static func monstro_res(c: Dictionary, nivel: int, mult: float = 1.0) -> float:
	return nivel * c.monstro_res * mult


static func monstro_ouro(nivel: int, rng: RandomNumberGenerator) -> int:
	return rng.randi_range(2 * nivel, 3 * nivel)
