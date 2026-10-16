"""Molde HUMANOIDE dos monstros (goblins, esqueletos, piratas, cultistas, golems, reis...).

O corpo é o do herói (peças desenhadas à mão em heroi.py), com as cores de cada monstro, e as
cabeças são desenhadas à mão aqui (humana, focinho, caveira, bloco, capuz), com extras por cima
(chifres, orelhas, coroa, chapéu, ligaduras). Assim os monstros herdam as animações do herói:
respirar, andar de 6 frames, ataques com antecipação, dano e cair ao morrer.
Os monstros grandes são desenhados a 32 px e ampliados 2×, 3× ou 4× (píxeis inteiros, sem desfocar).
Só vista de lado (virado para a direita); a esquerda é espelhada no jogo.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image
import heroi as H
from motor import RAMPAS, deitar, dissolver
from criaturas import Tela, efeito, R, escurecer, OUT

T = 32

# ---------------- cabeças de lado (A..E = rampa da pele, do escuro para o claro) ----------------
# e = olho, g = brilho do olho, m = boca. A origem é a mesma da cabeça do herói.
CABECAS = {
    'redonda': """
.....oooooo.....
...ooDEEEDDoo...
..oCDEEEEDDDCo..
.oCDDEEDDDDDDCo.
.oCDDDDDDDDDDDo.
oBCDDDDDDDDDDDDo
oBCCoooDDDDDDDDo
oBCoCDCoDDDDgeDo
oBCoCCCoDDDDeeDDo
.oBCoooCDDDDDDCo
.oBCCCCCDDDDmmo.
..oBBCCCCDDDCo..
...oooBBBBBoo...
""",
    'focinho': """
...oo...............
..oDCo..............
..oDCCoooooo........
.oCDDDDDEEDDoo......
.oCDDDDDDEEDDDo.....
oBCDDDDDDDDDDDDo....
oBCCDDDDDDDDgeDDooo.
oBCCDDDDDDDDeeDDDDDo
oBBCCDDDDDDDDDDDDDoo
.oBCCCDDDDDDCCCmmmo.
.oBBCCCCDDDCCCoooo..
..ooBBCCCCCCoo......
....oooooooo........
""",
    'caveira': """
.....oooooo.....
...ooDEEEEDoo...
..oCDEEEEEEDDo..
.oCDDEEEDDDDDDo.
.oCDDDDDDDDDDDo.
oBCDDDDDDDDDDDDo
oBCCDDDDDDooooDo
oBCCDDDDDoegooDo
oBBCCDDDDDooooDo
.oBCCCDDDDDDDoDo
.oBBCCCCDoDoDoo.
..ooBBCCCDDDDo..
....oooooooooo..
""",
    'bloco': """
................
................
..oooooooooooo..
.oDEEEEEDDDDDCo.
.oDEEDDDDDDDDCo.
.oDDDDDDDDDDDCo.
.oCDDDDDDDDDCCo.
.oCDDDDDDgeeCCo.
.oCCDDDDDDDDCBo.
.oCCCDDDDDDCCBo.
.oBCCCCCCCCCBBo.
..oooooooooooo..
................
""",
    'capuz': """
.....ooooo......
...ooDEEEDoo....
..oCDEEEDDDDo...
.oCDDEDDDDDDDo..
.oCDDDDDDDDDDDo.
oBCDDDDDDooooDo.
oBCCDDDDoooooDDo
oBCCDDDooooegoDo
oBBCDDDoooooooDo
oBBCCDDooooooDo.
.oBBCCDDoooooDo.
.oBBBCCCDDDDDo..
..ooooooooooo...
""",
}
CABECAS = {k: H.grelha(v) for k, v in CABECAS.items()}
CABECAS['tubarao'] = CABECAS['focinho']

# extras por cima da cabeça: (x, y, grelha) com A..E = rampa do extra
EXTRAS = {
    'chifres': (5, -4, H.grelha("""
.o....o.
oDo..oDo
oCDooDCo
.oCooCo.
..o..o..
""")),
    'orelhas_longas': (-4, 4, H.grelha("""
oo.....
oDCoo..
.oDCCCo
..ooooo
""")),
    'coroa': (3, -3, H.grelha("""
.o..o..o..
oEooEooEo.
oDEDDEDDDo
oCCCCCCCCo
.oooooooo.
""")),
    'chapeu': (1, -4, H.grelha("""
....oooooo....
...oDEEEDCo...
...oDDDDDCo...
...oCCCCCBo...
.ooooooooooooo
oDDDDDDDDDCCBo
.ooooooooooooo
""")),
    'barbatana': (4, -4, H.grelha("""
...oo
..oDo
.oDCo
oDCCo
""")),
}

DIR_ARMA = {'meio': (0.88, -0.48), 'frente': (0.95, -0.3), 'tras': (0.3, -0.95), 'horizontal': (1, 0),
            'cima': (0.15, -1), 'atras_alto': (-0.7, -0.7), 'baixo_frente': (0.85, 0.5), 'boca': (0.5, -0.85)}


def _hex(c):
    return tuple(int(c[i:i + 2], 16) for i in (1, 3, 5)) + (255,)


def _pinta(img, g, x0, y0, cores):
    for y, l in enumerate(g):
        for x, ch in enumerate(l):
            if ch in cores and 0 <= x0 + x < img.width and 0 <= y0 + y < img.height:
                img.putpixel((x0 + x, y0 + y), cores[ch])


def _rampa_cores(rampa, olho=OUT):
    r = R(rampa)
    d = {'A': r[0], 'B': r[1], 'C': r[2], 'D': r[3], 'E': r[4], 'o': OUT, 'e': olho, 'g': '#ffffff', 'm': r[0]}
    if olho != OUT:
        d['g'] = olho
    return {k: _hex(v) for k, v in d.items()}


def _tabela(cfg):
    """cor do herói -> cor do monstro"""
    c = cfg.get('cor', 'verde')
    roupa = R(cfg.get('roupa', c))
    pernas = R(cfg.get('pernas', cfg.get('roupa', c)))
    pes = R(cfg['pes']) if cfg.get('pes') else escurecer(pernas)
    mao = R(cfg.get('mao', c))
    t = {}
    for i, h in enumerate(['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff']):
        t[h] = roupa[i]
    for h, i in (('#6e2727', 0), ('#b33831', 1), ('#ea4f36', 2), ('#f57d4a', 3)):
        t[h] = roupa[i]
    for h, i in (('#3e3546', 1), ('#625565', 2), ('#7f708a', 3)):
        t[h] = pernas[i]
    for h, i in (('#45293f', 0), ('#694f62', 1), ('#966c6c', 2), ('#ab947a', 3), ('#f9c22b', 3), ('#fbff86', 4)):
        t[h] = pes[i]
    for h, i in (('#cd683d', 1), ('#e6904e', 2), ('#fca790', 3), ('#fdcbb0', 4), ('#f68181', 2)):
        t[h] = mao[i]
    return {_hex(a): _hex(b) for a, b in t.items()}


def _recolorir(im, tab):
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            c = px[x, y]
            if c[3] and c in tab:
                px[x, y] = tab[c]
    return im


def _mao(s, tr):
    y0, g = H.LADO_BRACO_EXTRA[s]
    pts = [(x, y) for y, l in enumerate(g) for x, ch in enumerate(l) if ch in 'LS']
    if not pts:
        return None
    return (H.X0 + sum(p[0] for p in pts) / len(pts) + 0.5, H.Y0 + y0 + tr + sum(p[1] for p in pts) / len(pts) + 0.5)


def _arma(t, cfg, mx, my, ux, uy):
    arma = cfg.get('arma')
    cor_arma = cfg.get('arma_cor', 'ferro')
    L = {'espada': 10, 'lanca': 15, 'clava': 8, 'cajado': 13, 'machado': 9, 'picareta': 8, 'foice': 12, 'arco': 0,
         'adaga': 5, 'tridente': 14}[arma]
    if arma == 'arco':
        t.cap(mx + 1, my - 6, mx + 3, my, 0.8, cor_arma, 9)
        t.cap(mx + 3, my, mx + 1, my + 6, 0.8, cor_arma, 9)
        t.px([(int(mx + 1), int(y)) for y in range(int(my - 6), int(my + 7))], '#c7dcd0', 8.9)
        return
    ex, ey = mx + ux * L, my + uy * L
    larg = {'espada': 1.2, 'lanca': 0.7, 'clava': 1.0, 'cajado': 0.8, 'machado': 0.8, 'picareta': 0.8, 'foice': 0.8,
            'adaga': 1.0, 'tridente': 0.7}[arma]
    t.cap(mx - ux * 1.5, my - uy * 1.5, ex, ey, larg, cor_arma if arma in ('espada', 'adaga') else 'madeira', 9)
    if arma in ('espada', 'adaga'):   # guarda
        t.cap(mx + uy * 2, my - ux * 2, mx - uy * 2, my + ux * 2, 0.6, 'ouro', 9.1)
    if arma == 'clava':
        t.el(ex, ey, 2.4, 2.4, cor_arma, 9.2)
    elif arma in ('machado', 'picareta'):
        t.pol([(ex - uy * 3, ey + ux * 3), (ex + ux * 2, ey + uy * 2), (ex + uy * 3, ey - ux * 3)] if arma == 'picareta'
              else [(ex, ey), (ex - uy * 4 + ux, ey + ux * 4 + uy), (ex - uy * 4 - ux * 3, ey + ux * 4 - uy * 3)], cor_arma, 9.2)
    elif arma == 'cajado':
        t.el(ex, ey, 1.9, 1.9, cfg.get('fx_cor', 'agua'), 9.2)
    elif arma == 'lanca':
        t.pol([(ex - uy * 1.3, ey + ux * 1.3), (ex + ux * 3.5, ey + uy * 3.5), (ex + uy * 1.3, ey - ux * 1.3)], cor_arma, 9.2)
    elif arma == 'tridente':
        for o in (-1.6, 0, 1.6):
            t.cap(ex - uy * o, ey + ux * o, ex - uy * o + ux * 3, ey + ux * o + uy * 3, 0.45, cor_arma, 9.2)
    elif arma == 'foice':
        t.pol([(ex, ey), (ex - uy * 6 + ux, ey + ux * 6 + uy), (ex - uy * 7 - ux * 2, ey + ux * 7 - uy * 2)], cor_arma, 9.2)


def _converte(p):
    """Poses genéricas das criaturas (at, a, baixo, cab='alta'...) -> poses do corpo do herói."""
    q = dict(p)
    at, a, baixo = p.get('at', 0), p.get('a', 0), p.get('baixo', 0)
    s = p.get('s')
    if s is None:
        s = 'meio' if not at else 'atras_alto' if at <= 0.4 else 'cima' if at < 0.9 else 'horizontal'
    if p.get('cab') == 'alta':
        s, baixo = 'cima', baixo - 1
    elif p.get('cab') == 'baixa':
        baixo += 1
    q.update(s=s, cab=baixo + p.get('cb', 0), tr=baixo + p.get('cb', 0),
             pl=p.get('pl') or ('passo_a' if a > 0.5 else 'passo_b' if a < -0.5 else 'parado'))
    return q


def frame(cfg, p):
    """Um frame 32×32 (antes da ampliação)."""
    p = _converte(p)
    tr, cab, s = p['tr'], p['cab'], p['s']
    c = cfg.get('cor', 'verde')
    tab = _tabela(cfg)
    im = Image.new('RGBA', (T, T))
    # ---- atrás do corpo: asas, capa, cauda
    tras = Tela(dict(k=1, W=32), {})
    cx = 15
    if cfg.get('asas'):
        up = (p.get('l', 0) % 4 in (1, 2)) * 1 + p.get('asa', 0)
        tras.pol([(cx - 2, 15 + tr), (cx - 13, 4 + tr - up * 2), (cx - 11, 17 + tr), (cx - 3, 21 + tr)], cfg['asas'], 0.3)
    if cfg.get('capa'):
        bal = [0, 1, 2, 1][p.get('l', 0) % 4]
        tras.pol([(cx - 3, 15 + tr), (cx - 8 - bal, 28), (cx - 1, 28), (cx + 1, 16 + tr)], cfg['capa'], 0.4)
    if cfg.get('cauda'):
        tras.cap(cx - 3, 24 + tr, cx - 9, 27 + (p.get('l', 0) % 2), 1.5, cfg.get('cauda_cor', c), 0.5)
    if cfg.get('cauda_peixe'):
        tras.cap(cx, 23 + tr, cx - 2, 29, 3.2, cfg['cauda_peixe'], 1)
        tras.pol([(cx - 3, 28), (cx - 8, 31), (cx + 1, 31)], cfg['cauda_peixe'], 1.2)
    if tras.P:
        im.alpha_composite(tras.imagem())
    # ---- pernas, tronco, cabeça, braço
    corpo = Image.new('RGBA', (T, T))
    if not cfg.get('cauda_peixe'):
        k = min(max(tr - 1, 0), 2)
        H.carimbar(corpo, H.LADO_PERNAS[p['pl']][k:], H.X0, H.Y0 + 22 + k)
    H.carimbar(corpo, H.LADO_TRONCO, H.X0, H.Y0 + 13 + tr)
    _recolorir(corpo, tab)
    if cfg.get('armadura'):
        _recolorir(corpo, {v: _hex(R(cfg['armadura'])[i]) for i, v in
                           enumerate(_hex(R(cfg.get('roupa', c))[j]) for j in range(5))})
    if cfg.get('costelas'):
        for yy in (16, 18, 20):
            for x in range(13, 20):
                q = corpo.getpixel((x, yy + tr))
                if q[3] and q[:3] != _hex(OUT)[:3]:
                    corpo.putpixel((x, yy + tr), _hex(OUT))
    im.alpha_composite(corpo)
    braco_atras = s == 'cima'
    braco = Image.new('RGBA', (T, T))
    y0, g = H.LADO_BRACO_EXTRA[s]
    H.carimbar(braco, g, H.X0, H.Y0 + y0 + tr)
    _recolorir(braco, tab)
    if cfg.get('braco_cor'):
        _recolorir(braco, {_hex(R(cfg.get('roupa', c))[i]): _hex(R(cfg['braco_cor'])[i]) for i in range(5)})
    if braco_atras:
        im.alpha_composite(braco)
    # cabeça
    tipo = cfg.get('cabeca', 'redonda')
    cara = p.get('cara', 'normal')
    olho = '#e83b3b' if cara == 'furia' else cfg.get('olho', OUT)
    hx, hy = H.X0, H.Y0 + cab
    if tipo == 'redonda' and cfg.get('cabelo'):
        # a cabeça do herói, com o cabelo e a pele deste monstro
        cab_im = Image.new('RGBA', (T, T))
        H.carimbar(cab_im, H.cara_lado(H.LADO_CABECA, 'fechado' if cara in ('x', 'fechado') else 'normal'), hx, hy)
        cr, pe = R(cfg['cabelo']), R(c)
        mapa = {'#7a3045': cr[0], '#9e4539': cr[1], '#cd683d': cr[2], '#e6904e': cr[3], '#fbb954': cr[4],
                '#fca790': pe[3], '#fdcbb0': pe[4], '#f68181': pe[2]}
        _recolorir(cab_im, {_hex(a): _hex(b) for a, b in mapa.items()})
        # o 'K' (#cd683d) da pele também é cabelo-médio no herói: a boca fica com a cor do cabelo escuro
        if olho != OUT:
            px = cab_im.load()
            for (x, y) in ((12 + hx, 9 + hy), (13 + hx, 9 + hy)):
                if 0 <= x < T and 0 <= y < T and px[x, y][3]:
                    px[x, y] = _hex(olho)
        im.alpha_composite(cab_im)
    else:
        rampa = cfg.get('capuz', cfg.get('roupa', c)) if tipo == 'capuz' else ('cinza' if tipo == 'bloco' and 'cor' not in cfg else c)
        if tipo == 'caveira':
            rampa = cfg.get('osso', 'branco')
        g = CABECAS[tipo]
        cores = _rampa_cores(rampa, olho)
        if cara in ('x', 'fechado') and tipo != 'caveira':
            g = [l.replace('g', 'D').replace('e', 'D') if i in (6, 7) else l.replace('g', 'e') for i, l in enumerate(g)]
            g = [l.replace('e', 'o') for l in g]
        _pinta(im, g, hx, hy, cores)
        if cfg.get('cabelo'):
            cr = _rampa_cores(cfg['cabelo'])
            gcab = [l[:16] for l in H.LADO_CABECA[:6]]
            gcab = [''.join(ch if ch in 'oHhrRY' else '.' for ch in l) for l in gcab]
            _pinta(im, gcab, hx, hy, {'o': cr['o'], 'H': cr['A'], 'h': cr['B'], 'r': cr['C'], 'R': cr['D'], 'Y': cr['E']})
    if cfg.get('ligaduras'):
        claro = _hex(R('branco')[1])
        for yy in range(2, 12, 3):
            for x in range(0, 16):
                q = im.getpixel((min(T - 1, hx + x), hy + yy))
                if q[3] and q[:3] != _hex(OUT)[:3]:
                    im.putpixel((hx + x, hy + yy), claro)
    for nome in ('chifres', 'orelhas_longas', 'coroa', 'chapeu'):
        if cfg.get(nome):
            ox, oy, g = EXTRAS[nome]
            _pinta(im, g, hx + ox, hy + oy, _rampa_cores(c if nome == 'orelhas_longas' else cfg[nome]))
    if tipo == 'tubarao':
        ox, oy, g = EXTRAS['barbatana']
        _pinta(im, g, hx + ox, hy + oy, _rampa_cores(c))
    if not braco_atras:
        im.alpha_composite(braco)
    # ---- à frente: escudo, arma, cristais, efeitos
    frente = Tela(dict(k=1, W=32), {k: v for k, v in p.items() if k == '_estrelas'})
    if cfg.get('escudo'):
        frente.pol([(cx - 6, 15 + tr), (cx - 1, 15 + tr), (cx - 1, 22 + tr), (cx - 3.5, 25 + tr), (cx - 6, 22 + tr)],
                   cfg['escudo'], 7)
    if cfg.get('cristais'):
        frente.cristais([(cx - 4, 15 + tr, -0.6), (cx - 2.5, 14 + tr, -0.2), (cx - 4.5, 19 + tr, -0.7)],
                        cfg['cristais'], 0.8, 5.9)
    m = _mao(s, tr)
    if cfg.get('arma') and m and s != 'boca':
        ux, uy = DIR_ARMA[s]
        _arma(frente, cfg, m[0], m[1], ux, uy)
    efeito(frente, cfg, p, H.X0 + 13, hy + 7)
    if frente.P or p.get('_estrelas') is not None:
        im.alpha_composite(frente.imagem())
    dx, dy = p.get('dx', 0), p.get('dy', 0)
    if dx or dy:
        out = Image.new('RGBA', (T, T))
        out.paste(im, (dx, dy), im)
        im = out
    return im


def escala(cfg):
    k = cfg.get('k', 1.0)
    return 1 if k <= 1.25 else 2 if k <= 2.5 else int(round(k))


def _ampliar(im, n):
    return im if n == 1 else im.resize((im.width * n, im.height * n), Image.NEAREST)


def _ataque(cfg):
    arma = cfg.get('arma')
    if arma == 'arco':
        return [dict(s='horizontal'), dict(s='horizontal', l=1, cb=0), dict(s='horizontal', fx='projeteis', fn=1, dx=-1),
                dict(l=1)]
    if arma == 'cajado':
        return [dict(s='cima', cb=-1, fx='magia', fn=1), dict(s='cima', cb=-1, fx='magia', fn=2),
                dict(s='horizontal', dx=1, pl='passo_a', fx='projeteis', fn=2), dict(l=1)]
    if arma in ('lanca', 'tridente'):
        return [dict(s='tras', dx=-1, cb=1, l=1), dict(s='horizontal', dx=2, pl='passo_a', l=2),
                dict(s='horizontal', dx=2, pl='passo_a', cb=1, l=3), dict(l=1)]
    if not arma:
        return [dict(s='tras', cb=1, l=1), dict(s='horizontal', dx=2, pl='passo_a', l=2),
                dict(s='baixo_frente', dx=1, l=3), dict(l=1)]
    return [dict(s='atras_alto', cb=1, l=1), dict(s='horizontal', dx=1, pl='passo_a', l=2),
            dict(s='baixo_frente', dx=1, pl='passo_a', cb=1, l=3), dict(l=1)]


def anims(cfg, especiais=(), chave='ataque'):
    from criaturas import ESPECIAIS
    n = escala(cfg)
    f = lambda **p: _ampliar(_dis(frame(cfg, p), p), n)
    A = {}
    A['parado'] = [f(), f(l=1), f(cb=1, l=2), f(cb=1, l=1)]
    A['mover'] = [f(pl=pl, cb=sb, s=b, l=l) for pl, sb, b, l in
                  (('passo_a', 1, 'tras', 1), ('desce_a', 1, 'meio', 2), ('passa_a', 0, 'frente', 3),
                   ('passo_b', 1, 'frente', 1), ('desce_b', 1, 'meio', 2), ('passa_b', 0, 'tras', 3))]
    A['atacar'] = [f(**p) for p in _ataque(cfg)]
    A['dano'] = [f(cara='x', dx=-1, s='tras', l=1)]
    dor = f(cara='x', dx=-1, s='tras', l=1)
    joelhos = f(cara='x', cb=3, pl='desce_a', s='baixo_frente', l=2)
    caido = _ampliar(deitar(frame(cfg, dict(cara='x')), 1), n)
    A['morrer'] = [dor, joelhos, caido, dissolver(caido, 0.6)] if not cfg.get('desfaz') else \
        [dor, dissolver(joelhos, 0.3), dissolver(joelhos, 0.6), dissolver(joelhos, 0.9)]
    for i, nome in enumerate(especiais):
        if isinstance(nome, tuple):
            A[nome[0]] = [f(**pp) for pp in ESPECIAIS[nome[1]]]
        else:
            A[f'{chave}_{i + 1}'] = [f(**pp) for pp in ESPECIAIS[nome]]
    if chave == 'especial':
        A['mudar_fase'] = [f(), f(cara='furia', fx='magia', fn=2, s='cima'), f(cara='furia', fx='magia', fn=3, dy=-1, s='cima'),
                           f(cara='furia')]
        A['atordoado'] = [f(cara='x', cb=1, _estrelas=i) for i in range(4)]
    return A


def _dis(im, p):
    d = p.get('_dissolver', 0)
    return dissolver(im, d) if d else im
