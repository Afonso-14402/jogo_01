"""Penteados do herói (criação de personagem: 8 penteados), desenhados à mão como a cabeça do herói.
Cada penteado tem a cabeça inteira nas 3 direções: (grelha, dx, dy) — dx/dy dizem quanto a grelha começa
antes da cabeça normal (ex.: o carrapito tem 3 linhas a mais por cima → dy = -3).
Letras: as de heroi.PAL (H h r R Y = cabelo · K D S L P = pele · w = brilho do olho · e = íris · o = contorno).
"""
from heroi import grelha, FRENTE, COSTAS, LADO_CABECA

_ROSTO_F = """
ohLSweSSSSweSDHo
ohLSeeSSSSeeSDHo
.oDSPSSSKSSSPDo.
..ooDDSSSSDDoo..
"""

CURTO_F = grelha("""
................
....oooooooo....
...oRRYYYRRro...
..oRYYRRRRrrro..
.oRRRRRRRrrrrho.
.oRRRRrrrrrrrhHo
ohRRrrrrrrrrrhHo
ohrrrSrrrSrrhhHo
ohhLSSSSSSSShhHo
""" + _ROSTO_F.lstrip("\n"))

CURTO_L = grelha("""
.................
.....oooooo......
...ooRYYYRRoo....
..oRRYYRRRRrroo..
.oRRRRRRRRrrrrro.
.oRRRRRRRrrrrrrho
ohRRRrrrrrrrrrrho
ohrRrrrrrrSrSSrho
ohrrrhrSKSSSweSo.
.ohrrhrKSSSSeeSSo
.ohhhhrSSSSSPSKo.
..ohhhoDSSSSSSo..
...ooooDDDDDoo...
""")

CURTO_B = grelha("""
................
....oooooooo....
...oRRYYYRRro...
..oRYYRRRRrrro..
.oRRRRRRRrrrrho.
.oRRRRrrrrrrrhHo
ohRRRrrrrrrrrhHo
ohRRrrrrrrrrhhHo
ohRrrrrrrrrhhhHo
ohrrrrrrrrrhhHHo
.ohhhhhhhhhhHHo.
..oDSSSSSSSSDo..
...ooDDDDDDoo...
""")

RAPADO_F = grelha("""
................
................
.....oooooo.....
...oohrrrrhoo...
..ohrrRRRrrrho..
.ohrRRrrrrrrhho.
.ohrrrrrrrrrhho.
ohLSSSSSSSSSSDDo
ohLSSSSSSSSSSDDo
oDLSweSSSSweSDDo
oDLSeeSSSSeeSDDo
.oDSPSSSKSSSPDo.
..ooDDSSSSDDoo..
""")

RAPADO_L = grelha("""
.................
.................
......oooooo.....
....oohrrrrhoo...
...ohrRRRRrrrho..
..ohrRRrrrrrrrho.
..ohrrrrrrrrrrDo.
.ohrrrrrSSSSSSSo.
.ohrrrrSKSSSweSo.
.ohrrrrKSSSSeeSSo
..ohhhhSSSSSPSKo.
...oDDDDSSSSSSo..
....oooDDDDDoo...
""")

RAPADO_B = grelha("""
................
................
.....oooooo.....
...oohrrrrhoo...
..ohrrRRRrrrho..
.ohrRRrrrrrrhho.
.ohrrrrrrrrrhho.
ohrrrrrrrrrrhhHo
ohrrrrrrrrrrhhHo
oDhhrrrrrrrhhhDo
oDSShhhhhhhhSSDo
.oDSSSSSSSSSSDo.
..ooDDDDDDDDoo..
""")

COMPRIDO_F = grelha("""
................
.....oooooo.....
...ooRYYRRroo...
..oRYYRRRRrrro..
.oRRRRRRRrrrrho.
oRRRRRrrrrrrrhHo
oRRRrrrrrrrrrhHo
oRrrrSrrrrSrrhHo
oRrhLSSSSSSShhHo
oRhSweSSSSweShHo
oRhSeeSSSSeeShHo
oRhDPSSSKSSSPhHo
oRhoDDSSSSDDohHo
oRho........ohHo
oRHo........oHHo
.oo..........oo.
""")

COMPRIDO_L = grelha("""
.......o.oo......
....oooYoRRo.....
..ooRRYYRRRrooo..
.oRRRYYRRRRrrrro.
ooRRRRRRRRrrrrro.
oRRRRRRRRrrhrrrho
oRhRRRrrrhrrhrrho
oRRrRrhrrrSrSSrho
oRrrrhrSKSSSweSo.
oRhrrhrKSSSSeeSSo
oRhhhhrrSSSSPSKo.
oRhhhhoDSSSSSSo..
oRhhhoooDDDDDoo..
oRhhho...........
ohHHo............
.ooo.............
""")

COMPRIDO_B = grelha("\n".join([l for l in COSTAS[:12]]) + """
ohrrhrrrhhrhhHHo
ohrhrrhrrhrhhHHo
.ohhohrhhohhhHo.
..ooo.oo.ooooo..
""")

# rabo de cavalo: de frente parece o curto; de lado e de costas vê-se o rabo
def _pad(g, n):
    return ['.' * n + l for l in g]


def _sobre(g, por_cima, ox, oy):
    """Desenha por cima de uma grelha (os '.' de por_cima não mudam nada)."""
    g = [list(l) for l in g]
    for y, l in enumerate(por_cima):
        for x, ch in enumerate(l):
            if ch != '.':
                g[oy + y][ox + x] = ch
    return [''.join(l) for l in g]


# rabo de cavalo de lado: preso com uma fita (c) e a cair para trás
RABO_L = _sobre(_pad(CURTO_L, 2), ["..o", ".oc", "oRc", "oRh", "oRh", "ohR", ".oh", "..o"], 0, 4)

CARRAPITO_TOPO = ["......oooo......", ".....oRYRro.....", ".....oRrrho.....", "......oooo......"]
CARRAPITO_F = CARRAPITO_TOPO[:3] + CURTO_F
CARRAPITO_B = CARRAPITO_TOPO[:3] + CURTO_B
CARRAPITO_L = [" " * 0 + "....oooo.........", "...oRYRro........", "...oRrrho........"] + CURTO_L

TRANCA_F = CURTO_F[:11] + grelha("""
oRhDPSSSKSSSPDo.
ohRoDDSSSSDDoo..
oRho............
ohRo............
oRho............
.oo.............
""")
TRANCA_B = CURTO_B[:10] + grelha("""
.ohhhhhhhhhhHHo.
..oDSSoRhoSSDo..
...ooDohRoDoo...
......oRho......
......ohRo......
......oRho......
.......oo.......
""")
TRANCA_L = CURTO_L[:10] + grelha("""
.oRhhhrSSSSSPSKo.
.ohRhhoDSSSSSSo..
.oRhoooDDDDDoo...
.ohRo............
.oRho............
..oo.............
""")

CARACOIS_F = grelha("""
....oooooooo....
..ooRYRRYRrRoo..
.oRYRrYRRrRrrho.
.oYRrRRrRRrrRho.
oRRrRRrrRrrRrhHo
oRrRrrRrrRrhrhHo
oRRrRrrrRrrrhrHo
ohrRrhrRrhrrhhHo
ohRLSSSSSSSShrHo
ohRSweSSSSweShHo
ohRSeeSSSSeeShHo
.ohDPSSSKSSSPho.
..ooDDSSSSDDoo..
""")
CARACOIS_L = grelha("""
...oooooooo......
.ooRYRRYRrRoo....
oRYRrYRRrRrrhoo..
oYRrRRrRRrrRrrho.
oRrRRrrRrrRrhrrho
oRRrRrRrrRrhrrrho
oRrRrrrRrrrhrrrho
ohRrRhrRrrSrSShho
oRrhrhrSKSSSweSo.
.oRhrhrKSSSSeeSSo
.ohhRhrrSSSSPSKo.
..ohhhoDSSSSSSo..
...ooooDDDDDoo...
""")
CARACOIS_B = grelha("""
....oooooooo....
..ooRYRRYRrRoo..
.oRYRrYRRrRrrho.
.oYRrRRrRRrrRho.
oRRrRRrrRrrRrhHo
oRrRrrRrrRrhrhHo
oRRrRrrrRrrrhrHo
ohrRrhrRrhrrhhHo
ohRrRrrRrhrRhrHo
ohrRrhrrRrhrhhHo
.ohrhrRrhrhrhho.
..ooDhhhhhhDoo..
...ooDDDDDDoo...
""")

RABO_B = CURTO_B[:8] + grelha("""
ohRrrrcccrrhhhHo
ohrrrroRhorhhHHo
.ohhhhoRhohhHHo.
..oDSSoRhoSSDo..
...ooDohHoDoo...
......oRho......
......ohHo......
.......oo.......
""")

# estilo: {direção: (grelha, dx, dy)}
PENTEADOS = {
    'espetado': {'baixo': (FRENTE[:13], 0, 0), 'cima': (COSTAS[:13], 0, 0), 'lado': (LADO_CABECA, 0, 0)},
    'curto': {'baixo': (CURTO_F, 0, 0), 'cima': (CURTO_B, 0, 0), 'lado': (CURTO_L, 0, 0)},
    'rapado': {'baixo': (RAPADO_F, 0, 0), 'cima': (RAPADO_B, 0, 0), 'lado': (RAPADO_L, 0, 0)},
    'comprido': {'baixo': (COMPRIDO_F, 0, 0), 'cima': (COMPRIDO_B, 0, 0), 'lado': (COMPRIDO_L, 0, 0)},
    'rabo': {'baixo': (CURTO_F, 0, 0), 'cima': (RABO_B, 0, 0), 'lado': (RABO_L, -2, 0)},
    'carrapito': {'baixo': (CARRAPITO_F, 0, -3), 'cima': (CARRAPITO_B, 0, -3), 'lado': (CARRAPITO_L, 0, -3)},
    'tranca': {'baixo': (TRANCA_F, 0, 0), 'cima': (TRANCA_B, 0, 0), 'lado': (TRANCA_L, 0, 0)},
    'caracois': {'baixo': (CARACOIS_F, 0, 0), 'cima': (CARACOIS_B, 0, 0), 'lado': (CARACOIS_L, 0, 0)},
}
