"""Herói, versão 2: desenhado À MÃO, píxel a píxel (cada peça é uma grelha de letras).

Cada letra é uma cor da paleta Resurrect 64 (ver PAL). '.' é transparente.
O boneco divide-se em peças (cabeça, tronco, braços, pernas, lenço) para as animações
mexerem cada peça sozinha, como um boneco de papel.
Estilo da referência Aranha-Mãe: contorno #2e222f, luz de cima à esquerda, 4–5 tons por material.
"""
import os
from PIL import Image

T = 32
PAL = {
    'o': '#2e222f',
    # cabelo (castanho-avermelhado)
    'H': '#7a3045', 'h': '#9e4539', 'r': '#cd683d', 'R': '#e6904e', 'Y': '#fbb954',
    # pele
    'K': '#cd683d', 'D': '#e6904e', 'S': '#fca790', 'L': '#fdcbb0', 'P': '#f68181', 'w': '#ffffff',
    # túnica azul
    '1': '#323353', '2': '#484a77', '3': '#4d65b4', '4': '#4d9be6', '5': '#8fd3ff',
    # lenço vermelho
    'x': '#6e2727', 'X': '#b33831', 'c': '#ea4f36', 'C': '#f57d4a',
    # couro, botas, fivela
    'b': '#45293f', 'B': '#694f62', 'n': '#966c6c', 'N': '#ab947a', 'g': '#f9c22b', 'G': '#fbff86',
    # calças
    't': '#3e3546', 'T': '#625565', 'u': '#7f708a',
}


def _rgba(c):
    return tuple(int(c[i:i + 2], 16) for i in (1, 3, 5)) + (255,)


def grelha(txt):
    return [l.strip() for l in txt.strip('\n').split('\n')]


def carimbar(img, g, x0, y0):
    for y, linha in enumerate(g):
        for x, ch in enumerate(linha):
            if ch != '.' and 0 <= x0 + x < img.width and 0 <= y0 + y < img.height:
                img.putpixel((x0 + x, y0 + y), _rgba(PAL[ch]))


def cortar(g, x1, x2, y1=0, y2=None):
    """Um bocado (colunas x1..x2, linhas y1..y2) de uma grelha."""
    y2 = len(g) - 1 if y2 is None else y2
    return [l[x1:x2 + 1] for l in g[y1:y2 + 1]]


# ============================ DE FRENTE ============================
FRENTE = grelha("""
......o.ooo.....
....oooYoRRRo...
..ooRRRYYRrRro..
.oRRYYYRRrrrrho.
.oRYYRRhrhrrrrHo
ohRRRRhrrrhrrrHo
ohRRrhrrrrrhrhHo
ohrRrSrRrSrRrhHo
ohhLSSSSSSSSShHo
ohLSwoSSSSwoSDHo
ohLSooSSSSooSDHo
.oDSPSSSKSSSPDo.
..ooDDSSSSDDoo..
..oooXcCCXxooo..
.o44XcCCccXx21o.
.o542XcCX33121o.
.o442cCX433121o.
.o432XcX333121o.
.onB244x3321bbo.
.oLSbnBgGBBbDKo.
.ooo44333321ooo.
...o32222111o...
...ooTuooTtoo...
....oTuooTto....
...oNnBooNnbo...
..oBnBBooBnBbo..
..obbbboobbbbo..
...oooo..oooo...
""")

COSTAS = grelha("""
......o.ooo.....
....oooYoRRRo...
..ooRRRYYRrRro..
.oRRYYYRRRrrrho.
.oRYYRRRRRrrrrHo
ohRRRRRhRRrrrrHo
ohRRRRhRRrhrrhHo
ohRRRhRRrrhrrhHo
ohRRhRRrrhrrhhHo
ohRrhRrrrhrrhhHo
ohrrhrrrhhrhhHHo
.ohhohrrhohhhHo.
..ooohhoohhooo..
..oooXcCCXxooo..
.o44XcCCccXx21o.
.o54233cX33121o.
.o44234cX33121o.
.o43234Xx33121o.
.onB2343x321bbo.
.oSSbnBBBBBbDKo.
.ooo44333321ooo.
...o32222111o...
...ooTuooTtoo...
....oTuooTto....
...oNnBooNnbo...
..oBnBBooBnBbo..
..obbbboobbbbo..
...oooo..oooo...
""")


def pecas_frente(g):
    return {
        'cabeca': cortar(g, 0, 15, 0, 12),
        'tronco': cortar(g, 4, 11, 13, 21),
        'braco_e': cortar(g, 0, 4, 13, 20),
        'braco_d': cortar(g, 11, 15, 13, 20),
        'pernas': cortar(g, 0, 15, 22, 27),
    }


def pernas_levanta(pernas, lado):
    """Levanta uma perna 1 píxel (lado 'e' = colunas 0–7, 'd' = 8–15)."""
    a, b = (0, 8) if lado == 'e' else (8, 16)
    novo = [list(l) for l in pernas]
    for y in range(len(pernas)):
        for x in range(a, b):
            novo[y][x] = pernas[y + 1][x] if y + 1 < len(pernas) else '.'
    return [''.join(l) for l in novo]


# ============================ DE LADO (virado para a direita) ============================
LADO_CABECA = grelha("""
.......o.oo......
....oooYoRRo.....
..ooRRYYRRRrooo..
.oRRRYYRRRRrrrro.
ooRRRRRRRRrrrrro.
oRRRRRRRRrrhrrrho
.ohRRRrrrhrrhrrho
ooRrRrhrrrSrSSrho
oRrrrhrSKSSSwoSo.
.ohrrhrKSSSSooSSo
.ohhhhrrSSSSPSKo.
..ohhhoDSSSSSSo..
...ooooDDDDDoo...
""")

LADO_TRONCO = grelha("""
.....ooXcCCoo...
....oxXcCCcXo...
....o4443332o...
....o4433322o...
....o4433222o...
...o44333222o...
...obnBBBBBbbo..
...o443333222o..
...o4322222211o.
""")

# braço do lado de cá: 'meio', 'frente', 'tras' (linhas 14–20 do boneco)
LADO_BRACO = {
    'meio': grelha("""
.......ooo...
......o544o..
......o443o..
......o432o..
......obnBo..
......oLSDo..
.......ooo...
"""),
    'frente': grelha("""
.......ooo...
......o544o..
.......o443o.
.......o432o.
........onBo.
........oSDo.
.........oo..
"""),
    'tras': grelha("""
.......ooo...
......o544o..
.....o443o...
.....o432o...
....obnBo....
....oLSDo....
.....oo......
"""),
}

# ponta do lenço que esvoaça atrás (linhas 13–17)
LADO_LENCO = [
    grelha("""
.....oxX
....oXxo
...oXco.
...oXxo.
....oo..
"""),
    grelha("""
.....oxX
..ooocXo
.oXcXxo.
oXxoo...
.oo.....
"""),
    grelha("""
.....oxX
.oooXcxo
oCcXXxo.
.ooxo...
...o....
"""),
    grelha("""
.....oxX
...ooXXo
.ooXcxo.
oXcxo...
.ooo....
"""),
]

# pernas (linhas 22–27): o 'parado' e as 6 poses de andar
LADO_PERNAS = {
    'parado': grelha("""
.....otTouTo....
.....otTouTo....
....obBoNnBo....
....obBBonnBBo..
....obbbobbbbbo.
.....ooo.ooooo..
"""),
    # 0: pé de cá à frente, pé de lá atrás
    'passo_a': grelha("""
.....otTouTo....
....otTo.ouTo...
...obBo...oNnBo.
..obBBo...onnBBo
..obbbo...obbbbo
...ooo.....oooo.
"""),
    # 1: a descer, pernas a juntar
    'desce_a': grelha("""
.....otTouTo....
....otToouTo....
...obBo.oNnBo...
...obBBoonnBBo..
...obbbbobbbbo..
....ooo..oooo...
"""),
    # 2: a passar, perna de lá no ar
    'passa_a': grelha("""
.....otTuTo.....
....obBouTo.....
....obBBNnBo....
.....ooonnBBo...
.......obbbbo...
........oooo....
"""),
    # 3: pé de lá à frente, pé de cá atrás
    'passo_b': grelha("""
.....ouTotTo....
....ouTo.otTo...
...oNnBo..obBBo.
..onnBBo..obBBBo
..obbbbo..obbbbo
...oooo....oooo.
"""),
    'desce_b': grelha("""
.....ouTotTo....
....ouTootTo....
...oNnBoobBBo...
...onnBBobBBBo..
...obbbbobbbbo..
....oooo.oooo...
"""),
    # 5: a passar, perna de cá no ar
    'passa_b': grelha("""
.....otuTTo.....
.....otoNnBo....
....obBonnBBo...
....obBBbbbbo...
....obbboooo....
.....ooo........
"""),
}


# ============================ montar os frames ============================
X0, Y0 = 8, 4   # canto do boneco no quadro 32×32 (os pés ficam na linha 31)


def frame_frente(P, cab=0, tronco=0, be=0, bd=0, pernas=None):
    im = Image.new('RGBA', (T, T))
    carimbar(im, pernas or P['pernas'], X0, Y0 + 22)
    carimbar(im, P['tronco'], X0 + 4, Y0 + 13 + tronco)
    carimbar(im, P['braco_e'], X0, Y0 + 13 + tronco + be)
    carimbar(im, P['braco_d'], X0 + 11, Y0 + 13 + tronco + bd)
    carimbar(im, P['cabeca'], X0, Y0 + cab)
    return im


def frame_lado(cab=0, tronco=0, braco='meio', lenco=0, pernas='parado'):
    im = Image.new('RGBA', (T, T))
    carimbar(im, LADO_LENCO[lenco], X0, Y0 + 13 + tronco)
    carimbar(im, LADO_PERNAS[pernas], X0, Y0 + 22)
    carimbar(im, LADO_TRONCO, X0, Y0 + 13 + tronco)
    carimbar(im, LADO_CABECA, X0, Y0 + cab)
    carimbar(im, LADO_BRACO[braco], X0, Y0 + 14 + tronco)
    return im


def anim_parado():
    out = {}
    for nome, g in (('baixo', FRENTE), ('cima', COSTAS)):
        P = pecas_frente(g)
        out[nome] = [frame_frente(P, cab=c, tronco=t, be=b, bd=b)
                     for c, t, b in ((0, 0, 0), (0, 0, 0), (1, 1, 0), (1, 1, 0))]
    out['lado'] = [frame_lado(cab=c, tronco=t, lenco=l)
                   for c, t, l in ((0, 0, 0), (0, 0, 1), (1, 1, 2), (1, 1, 1))]
    return out


def anim_andar():
    out = {}
    for nome, g in (('baixo', FRENTE), ('cima', COSTAS)):
        P = pecas_frente(g)
        pe = pernas_levanta(P['pernas'], 'e')
        pd = pernas_levanta(P['pernas'], 'd')
        seq = [  # (pernas, sobe, braço esq., braço dir.)
            (P['pernas'], 0, 0, 0), (pe, 0, 1, -1), (pe, -1, 1, -1),
            (P['pernas'], 0, 0, 0), (pd, 0, -1, 1), (pd, -1, -1, 1),
        ]
        out[nome] = [frame_frente(P, cab=s, tronco=s, be=e, bd=d, pernas=p) for p, s, e, d in seq]
    seq = [  # (pernas, sobe, braço, lenço)
        ('passo_a', 1, 'tras', 1), ('desce_a', 1, 'meio', 2), ('passa_a', 0, 'frente', 3),
        ('passo_b', 1, 'frente', 1), ('desce_b', 1, 'meio', 2), ('passa_b', 0, 'tras', 3),
    ]
    out['lado'] = [frame_lado(cab=s, tronco=s, braco=b, lenco=l, pernas=p) for p, s, b, l in seq]
    return out


ANIMS = {'parado': anim_parado, 'andar': anim_andar}


def tira(frames):
    im = Image.new('RGBA', (T * len(frames), T))
    for i, f in enumerate(frames):
        im.paste(f, (i * T, 0))
    return im


def gerar(destino):
    os.makedirs(destino, exist_ok=True)
    tudo = {}
    for nome, fn in ANIMS.items():
        for d, frames in fn().items():
            tira(frames).save(os.path.join(destino, f'heroi_{nome}_{d}.png'))
            tudo[(nome, d)] = frames
    return tudo


if __name__ == '__main__':
    import sys
    gerar(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), '../../arte/heroi'))
