"""Herói: desenhado À MÃO, píxel a píxel (cada peça é uma grelha de letras).

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
    'e': '#2e222f',   # íris (cor-índice própria nas camadas)
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
ohLSweSSSSweSDHo
ohLSeeSSSSeeSDHo
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
oRrrrhrSKSSSweSo.
.ohrrhrKSSSSeeSSo
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


# ---------- pernas extra de lado ----------
LADO_PERNAS['sentado'] = grelha("""
....ooooooooo...
....otTTuuuuTo..
.....ooooooNnBo.
..........obnBo.
..........obbbo.
...........ooo..
""")

# ============================ braços extra ============================
# DE FRENTE: braço do lado esquerdo do ecrã, com a sua origem (x, y) no boneco.
# O braço do outro lado é o mesmo, espelhado e mais escuro (fica na sombra).
BRACOS_FRENTE = {
    'cima': (-2, 6, grelha("""
.oo....
oLSo...
oSDo...
.onBo..
.o54o..
..o54o.
..o44o.
...o4o.
..o44o.
""")),
    'frente': (1, 14, grelha("""
o54o...
o443o..
.o443o.
..o43o.
..onBBo
..oLSDo
...ooo.
""")),
    'fora': (-5, 14, grelha("""
.ooooooo.
oLSnB544o
oSDbB443o
.ooooooo.
""")),
    'boca': (1, 10, grelha("""
....oo..
...oLSo.
..onBDo.
.o44oo..
o544o...
o443o...
o43o....
.oo.....
""")),
}
POR_CIMA_DA_CABECA = {'cima', 'boca'}
SOMBRA = {'5': '3', '4': '2', '3': '1', 'L': 'S', 'S': 'D', 'D': 'K', 'N': 'n', 'n': 'B', 'B': 'b'}

# DE LADO: braço do lado de cá, (linha onde começa, grelha)
LADO_BRACO_EXTRA = {
    # levantado por trás da cabeça: só se vê a mão por cima do cabelo e a manga no ombro
    'cima': (-3, grelha("""
.......oo...
......oLSo..
......oSDo..
......onBo..
......o44o..
......o44o..
......o44o..
......o44o..
......o44o..
......o44o..
......o44o..
......o44o..
......o44o..
......o44o..
......o44o..
......o44o..
......o44o..
......o43o..
......o443o.
......o544o.
......o432o.
.......ooo..
""")),
    'horizontal': (14, grelha("""
.......ooo......
......o5444oooo.
......o443333nLSo
......o4322bBBDo
.......oooooooo.
""")),
    'atras_alto': (8, grelha("""
..oo.........
.oLSo........
.oSDo........
..onBo.......
...o44o......
....o443o....
.....o544o...
......o43o...
.......oo....
""")),
    'baixo_frente': (14, grelha("""
.......ooo...
......o544o..
.......o443o.
........o43o.
.........onBo
.........oLSo
..........oo.
""")),
    'boca': (9, grelha("""
...........oo.
..........oLSo
.........onBo.
........o44o..
.......o443o..
......o544o...
......o43o....
.......oo.....
""")),
}
for k, g in LADO_BRACO.items():
    LADO_BRACO_EXTRA[k] = (14, g)
LADO_BRACO_EXTRA['nenhum'] = (14, [])


# ============================ caras ============================
def _troca(g, pix):
    g = [list(l) for l in g]
    for (y, x), ch in pix.items():
        g[y][x] = ch
    return [''.join(l) for l in g]


def _cabeca(d, estilo):
    """(grelha, dx, dy) da cabeça com o penteado escolhido (heroi_cabelos.py)."""
    from heroi_cabelos import PENTEADOS
    return PENTEADOS[estilo][d]


def cara_frente(g, tipo, ox=0, oy=0):
    olhos = {
        'normal': None,
        'fechado': ('SS', 'oo', 'SS', 'oo'),
        'dor': ('oS', 'So', 'So', 'oS'),
        'feliz': ('oo', 'SS', 'oo', 'SS'),
    }[tipo]
    if not olhos:
        return g
    a, b, c, d = olhos
    return _troca(g, {(9 + oy, 4 + ox): a[0], (9 + oy, 5 + ox): a[1], (10 + oy, 4 + ox): b[0], (10 + oy, 5 + ox): b[1],
                      (9 + oy, 10 + ox): c[0], (9 + oy, 11 + ox): c[1], (10 + oy, 10 + ox): d[0], (10 + oy, 11 + ox): d[1]})


def cara_lado(g, tipo, ox=0, oy=0):
    olho = {'normal': None, 'fechado': ('SS', 'oo'), 'dor': ('oS', 'So'), 'feliz': ('oo', 'SS')}[tipo]
    if not olho:
        return g
    return _troca(g, {(8 + oy, 12 + ox): olho[0][0], (8 + oy, 13 + ox): olho[0][1], (9 + oy, 12 + ox): olho[1][0],
                      (9 + oy, 13 + ox): olho[1][1]})


# ============================ montar os frames ============================
X0, Y0 = 8, 4   # canto do boneco no quadro 32×32 (os pés ficam na linha 31)


def pecas_frente_todas(g):
    P = pecas_frente(g)
    # tronco com contorno dos dois lados (fica bem quando um braço sai do sítio)
    tr = ['.' + l + '.' for l in P['tronco']]
    for y in range(1, 8):
        tr[y] = 'o' + tr[y][1:-1] + 'o'
    tr[8] = 'o' + tr[8][1:-1] + 'o'
    P['tronco'] = tr
    pern = P['pernas']
    P['pernas_e'] = pernas_levanta(pern, 'e')
    P['pernas_d'] = pernas_levanta(pern, 'd')
    P['pernas_abre'] = [l[1:8] + '..' + l[8:15] for l in pern]
    P['pernas_senta'] = pern[:1] + pern[2:]
    return P


def _espelho(g):
    return [''.join(SOMBRA.get(c, c) for c in reversed(l)) for l in g]


def _braco_frente(P, lado, pose):
    """Devolve (x, y, grelha) de um braço de frente/costas."""
    if pose == 'nenhum':
        return 0, 0, []
    if pose == 'normal':
        return (0, 13, P['braco_e']) if lado == 'e' else (11, 13, P['braco_d'])
    ox, oy, g = BRACOS_FRENTE[pose]
    if lado == 'e':
        return ox, oy, g
    w = max(len(l) for l in g)
    return 15 - (ox + w - 1), oy, _espelho([l.ljust(w, '.') for l in g])


def _deslocar(im, dx, dy):
    if not dx and not dy:
        return im
    out = Image.new('RGBA', im.size)
    out.paste(im, (dx, dy), im)
    return out


POSE = dict(s='meio', f='normal', o='normal', cab=0, tr=0, dx=0, dy=0, pl='parado', pf='normal',
            cara='normal', l=0, cabeca=True, lenco=True, k=None, estilo='espetado')


def _agacha(p):
    """Quando o corpo desce 2 ou mais, as pernas encolhem (dobram os joelhos)."""
    return p['k'] if p['k'] is not None else min(max(p['tr'] - 1, 0), 2)


def compor(d, **k):
    p = dict(POSE, **k)
    im = Image.new('RGBA', (T, T))
    tr, cab = p['tr'], p['cab']
    if d == 'lado':
        if p['lenco']:
            carimbar(im, LADO_LENCO[p['l']], X0, Y0 + 13 + tr)
        k = _agacha(p) if p['pl'] != 'sentado' else 0
        carimbar(im, LADO_PERNAS[p['pl']][k:], X0, Y0 + 22 + k)
        carimbar(im, LADO_TRONCO, X0, Y0 + 13 + tr)
        y, g = LADO_BRACO_EXTRA[p['s']]
        if p['s'] == 'cima':
            carimbar(im, g, X0, Y0 + y + tr)
        if p['cabeca']:
            gc, ox, oy = _cabeca('lado', p['estilo'])
            carimbar(im, cara_lado(gc, p['cara'], -ox, -oy), X0 + ox, Y0 + cab + oy)
        if p['s'] != 'cima':
            carimbar(im, g, X0, Y0 + y + tr)
        return _deslocar(im, p['dx'], p['dy'])
    P = PECAS[d]
    pern = {'normal': P['pernas'], 'e': P['pernas_e'], 'd': P['pernas_d'],
            'abre': P['pernas_abre'], 'senta': P['pernas_senta']}[p['pf']]
    k = _agacha(p) if p['pf'] != 'senta' else 0
    carimbar(im, pern[k:], X0, Y0 + 22 + k + (1 if p['pf'] == 'senta' else 0))
    carimbar(im, P['tronco'], X0 + 3, Y0 + 13 + tr)
    # o braço da arma é o direito do herói: à esquerda do ecrã de frente, à direita de costas
    arma, outro = ('e', 'd') if d == 'baixo' else ('d', 'e')
    bracos = [(arma, p['f']), (outro, p['o'])]
    depois = []
    for lado, pose in bracos:
        x, y, g = _braco_frente(P, lado, pose)
        if pose in POR_CIMA_DA_CABECA:
            depois.append((x, y, g))
        else:
            carimbar(im, g, X0 + x, Y0 + y + tr)
    if p['cabeca']:
        g, ox, oy = _cabeca(d, p['estilo'])
        cabeca = cara_frente(g, p['cara'], -ox, -oy) if d == 'baixo' else g
        carimbar(im, cabeca, X0 + ox, Y0 + cab + oy)
    for x, y, g in depois:
        carimbar(im, g, X0 + x, Y0 + y + tr)
    return _deslocar(im, p['dx'] if d == 'lado' else 0, p['dy'])


PECAS = {'baixo': pecas_frente_todas(FRENTE), 'cima': pecas_frente_todas(COSTAS)}


def frame_lado(cab=0, tronco=0, braco='meio', lenco=0, pernas='parado'):
    return compor('lado', cab=cab, tr=tronco, s=braco, l=lenco, pl=pernas)


def _caixa(im):
    return im.crop(im.getbbox())


def deitar(im, sentido=1, sobe=0):
    """Roda o boneco 90° (deitado no chão), centrado e com o corpo no fundo do quadro."""
    b = _caixa(im).rotate(90 * sentido, expand=True)
    out = Image.new('RGBA', (T, T))
    out.paste(b, ((T - b.width) // 2, T - b.height - sobe), b)
    return out


def rodar(im, quartos):
    b = _caixa(im).rotate(-90 * quartos, expand=True)
    out = Image.new('RGBA', (T, T))
    out.paste(b, ((T - b.width) // 2, T - b.height), b)
    return out


DIRS = ('baixo', 'lado', 'cima')


def _anim(lista):
    """lista de poses (dicts) -> {direção: [frames]}"""
    return {d: [compor(d, **f) for f in lista] for d in DIRS}


def anim_parado():
    return _anim([dict(), dict(l=1), dict(cab=1, tr=1, l=2), dict(cab=1, tr=1, l=1)])


def anim_andar():
    out = {}
    lado = [('passo_a', 1, 'tras', 1), ('desce_a', 1, 'meio', 2), ('passa_a', 0, 'frente', 3),
            ('passo_b', 1, 'frente', 1), ('desce_b', 1, 'meio', 2), ('passa_b', 0, 'tras', 3)]
    out['lado'] = [compor('lado', pl=pl, cab=s, tr=s, s=b, l=l) for pl, s, b, l in lado]
    frente = [('normal', 0), ('e', 0), ('e', -1), ('normal', 0), ('d', 0), ('d', -1)]
    for d in ('baixo', 'cima'):
        out[d] = [compor(d, pf=pf, cab=s, tr=s) for pf, s in frente]
    return out


def anim_esquiva():
    out = {}
    for d in DIRS:
        bola = compor(d, cab=4, tr=4, pl='desce_a', s='baixo_frente', f='frente', o='frente', cara='fechado', l=2)
        out[d] = [bola, rodar(bola, 1), rodar(bola, 2), rodar(bola, 3)]
    return out


def anim_dano():
    return _anim([dict(cara='dor', dx=-1, s='tras', f='fora', o='fora', l=1),
                  dict(cara='dor', dx=-1, cab=1, tr=1, l=2)])


def anim_morrer():
    out = {}
    for d in DIRS:
        a = compor(d, cara='dor', dx=-1, s='tras', f='fora', o='fora', l=1)
        b = compor(d, cara='fechado', cab=3, tr=3, pl='desce_a', s='baixo_frente', f='frente', o='frente', l=2)
        c = compor(d, cara='fechado', cab=5, tr=5, pl='desce_a', s='baixo_frente', f='frente', o='frente')
        caido = compor(d, cara='fechado')
        out[d] = [a, b, c, deitar(caido, 1, sobe=2), deitar(caido, 1)]
    return out


def anim_recolher():
    return _anim([dict(cab=2, tr=2, pl='desce_a', s='baixo_frente', f='frente'),
                  dict(cab=3, tr=3, pl='desce_a', s='baixo_frente', f='frente', l=1),
                  dict(cab=3, tr=3, pl='desce_a', s='horizontal', f='frente', l=2),
                  dict(cab=1, tr=1, s='meio', l=1)])


def anim_ataque_corte():
    return _anim([dict(s='atras_alto', f='fora', cab=1, tr=1, l=1),
                  dict(s='horizontal', f='frente', dx=1, pl='passo_a', l=2),
                  dict(s='baixo_frente', f='frente', o='fora', dx=1, pl='passo_a', cab=1, tr=1, l=3),
                  dict(l=1)])


def anim_ataque_pesado():
    return _anim([dict(s='atras_alto', f='fora', cab=1, tr=1, l=1),
                  dict(s='cima', f='cima', o='cima', cab=-1, tr=-1, l=2),
                  dict(s='baixo_frente', f='frente', o='frente', cab=2, tr=2, dx=1, pl='passo_a', pf='abre', l=3),
                  dict(s='baixo_frente', f='frente', o='frente', cab=3, tr=3, dx=1, pl='passo_a', pf='abre', l=1),
                  dict(cab=1, tr=1, l=2)])


def anim_ataque_estocada():
    return _anim([dict(s='tras', dx=-1, cab=1, tr=1, f='fora', l=1),
                  dict(s='horizontal', f='frente', dx=2, pl='passo_a', pf='abre', l=2),
                  dict(s='horizontal', f='frente', dx=2, pl='passo_a', pf='abre', cab=1, tr=1, l=3),
                  dict(l=1)])


def anim_ataque_disparo():
    return _anim([dict(s='horizontal', f='frente', o='frente', l=0),
                  dict(s='horizontal', f='frente', o='boca', l=1),
                  dict(s='horizontal', f='frente', o='fora', dx=-1, cab=1, tr=1, l=2),
                  dict(l=1)])


def anim_ataque_magia():
    return _anim([dict(s='cima', f='cima', cab=-1, tr=-1, cara='fechado', l=1),
                  dict(s='cima', f='cima', cab=-1, tr=-1, l=2),
                  dict(s='horizontal', f='frente', dx=1, pl='passo_a', l=3),
                  dict(l=1)])


def anim_ataque_soco():
    return _anim([dict(s='tras', cab=1, tr=1, f='fora', l=1),
                  dict(s='horizontal', f='frente', dx=2, pl='passo_a', pf='abre', l=2),
                  dict(s='baixo_frente', f='frente', o='frente', dx=1, l=3),
                  dict(l=1)])


def anim_nadar():
    out = {}
    lado = [('cima', 'passo_a'), ('horizontal', 'desce_a'), ('tras', 'passa_a'),
            ('cima', 'passo_b'), ('horizontal', 'desce_b'), ('tras', 'passa_b')]
    out['lado'] = [rodar(compor('lado', s=b, pl=pl, l=i % 4), 1) for i, (b, pl) in enumerate(lado)]
    seq = [('cima', 'normal', 'e', 0), ('cima', 'normal', 'e', -1), ('normal', 'normal', 'normal', 0),
           ('normal', 'cima', 'd', 0), ('normal', 'cima', 'd', -1), ('normal', 'normal', 'normal', 0)]
    for d in ('baixo', 'cima'):
        out[d] = [compor(d, f=f, o=o, pf=pf, dy=dy) for f, o, pf, dy in seq]
    return out


def anim_planar():
    return _anim([dict(s='cima', f='cima', o='cima', pl='passa_a', pf='e', l=1),
                  dict(s='cima', f='cima', o='cima', pl='passa_a', pf='e', dy=-1, l=3)])


def anim_montar():
    return _anim([dict(pl='sentado', pf='senta', cab=1, tr=1, l=1),
                  dict(pl='sentado', pf='senta', cab=2, tr=2, l=2)])


def anim_pescar():
    return _anim([dict(s='atras_alto', f='cima', cab=1, tr=1, l=1),
                  dict(s='horizontal', f='frente', dx=1, l=2),
                  dict(s='baixo_frente', f='frente', l=1),
                  dict(s='cima', f='cima', cab=-1, tr=-1, l=3)])


def anim_beber():
    return _anim([dict(s='boca', f='boca'),
                  dict(s='boca', f='boca', cab=-1, cara='fechado', l=1),
                  dict(s='meio', cara='feliz', l=2)])


def anim_celebrar():
    return _anim([dict(cab=2, tr=2, pl='desce_a', cara='feliz'),
                  dict(s='cima', f='cima', dy=-3, pl='passa_a', pf='e', cara='feliz', l=2),
                  dict(s='cima', f='cima', dy=-2, cara='feliz', l=3),
                  dict(s='cima', f='cima', cab=1, tr=1, cara='feliz', l=1)])


def anim_sentar():
    return _anim([dict(pl='sentado', pf='senta', cab=1, tr=1)])


ANIMS = {n[5:]: f for n, f in list(globals().items()) if n.startswith('anim_')}


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
