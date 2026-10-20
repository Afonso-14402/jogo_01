"""Ent Ancião (boss do andar 10, 128×128), desenhado de novo: um carvalho velho e torto que anda.
Ficha: docs/BOSSES.md, secção 2 (metade da copa seca, barba de musgo, olhos verdes que brilham, raízes por pernas).

- tronco nodoso, mais largo em baixo, com veios na casca, nós e manchas de musgo; dois cogumelos vermelhos;
- a cara entalhada do lado de quem olha (vira-se para a direita): sobrolho de casca, olhos fundos que brilham,
  nariz de nó, boca rachada e uma barba de musgo em fios que abanam;
- a copa em tufos de folhas (verde à direita, outono e ramos secos à esquerda), com a borda recortada em folhas;
- braços de ramos com cotovelo, mãos de três dedos-galho e um tufo de folhas; pernas de raízes com dedos.

Usado por ferramentas/arte/guardioes_r01.py (as mesmas animações e o mesmo número de quadros de antes).
"""
import math
import random

from motor import Parte, elipse, capsula, poligono, desenhar, dissolver

OUT = '#2e222f'
CASCA = ['#2e222f', '#45293f', '#694f62', '#966c6c', '#ab947a']
CASCA_ESC = ['#2e222f', '#2e222f', '#45293f', '#694f62', '#966c6c']
OUTONO = ['#6e2727', '#9e4539', '#cd683d', '#f79617', '#fbb954']
SECO = ['#2e222f', '#4c3e24', '#676633', '#a2a947', '#d5e04b']
FOLHA = ['#165a4c', '#239063', '#1ebc73', '#91db69', '#cddf6c']
MUSGO = ['#313638', '#374e4a', '#547e64', '#92a984', '#b2ba90']


def _px(P, pts, cor, z):
    P.append(Parte({(int(x), int(y)) for x, y in pts}, None, z=z, separar=False, cor=cor))


def _tufo(cx, cy, r, semente):
    """Um tufo de folhas: um círculo com a borda recortada (folhinhas a sair)."""
    rnd = random.Random(semente)
    m = elipse(cx, cy, r, r * 0.86)
    borda = [p for p in m if any((p[0] + dx, p[1] + dy) not in m for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))]
    for (x, y) in borda:
        k = rnd.random()
        if k < 0.28:
            m.discard((x, y))
        elif k < 0.5:   # uma folha a espreitar para fora
            dx, dy = (x - cx), (y - cy)
            n = math.hypot(dx, dy) or 1
            m.add((int(x + dx / n * 1.6), int(y + dy / n * 1.6)))
    return m


def _folhagem(P, m, rampa, z, semente):
    """Textura de folhas dentro de um tufo: pintas escuras (sombra entre folhas) e folhinhas claras em cima à esquerda."""
    rnd = random.Random(semente)
    xs = [p[0] for p in m]
    ys = [p[1] for p in m]
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    escuro, claro = [], []
    for (x, y) in m:
        h = (x * 7 + y * 13 + semente * 5) % 17
        lado = (x - cx) + (y - cy)
        if h == 0 or (h == 5 and lado > 2):
            escuro.append((x, y))
        elif h == 9 and lado < -3 and rnd.random() < 0.8:
            claro += [(x, y), (x + 1, y)]
    _px(P, escuro, rampa[0], z + 0.001)
    _px(P, [p for p in claro if p in m], rampa[4], z + 0.002)


def ent(dy=0, braco=(0, 0), braco2=(0, 0), perna=0, cara='normal', abanar=0, bolotas=0, raizes=0, folhas=0,
        seiva=False, grito=False):
    P = []
    cx = 58
    y0 = dy
    # ---------------- pernas de raízes (a de trás primeiro)
    joelho_t, pe_t = (cx - 12, 96 + y0), (cx - 17, 113)
    P.append(Parte(capsula(*joelho_t, *pe_t, 7), CASCA_ESC, z=0, volume='cilindro_v'))
    for (tx, ty, r) in ((-14, 124, 3.6), (-4, 125, 3.0), (4, 124, 2.6)):
        P.append(Parte(capsula(*pe_t, pe_t[0] + tx, ty, r), CASCA_ESC, z=0.1))
    joelho_f, pe_f = (cx + 13, 96 + y0), (cx + 18, 113 - perna)
    P.append(Parte(capsula(*joelho_f, *pe_f, 7.5), CASCA, z=4, volume='cilindro_v'))
    for (tx, ty, r) in ((-10, 125, 3.2), (2, 126, 3.4), (12, 124, 3.0)):
        P.append(Parte(capsula(*pe_f, pe_f[0] + tx, ty - perna, r), CASCA, z=4.1))
    _px(P, [(pe_f[0] - 3 + i, 112 - perna - (i % 3)) for i in range(7)], '#547e64', 4.2)   # musgo no pé
    # ---------------- braço de trás (longe)
    om2 = (cx - 14, 66 + y0)
    co2 = (cx - 32 + braco2[0] // 2, 76 + y0 + braco2[1] // 2)
    m2 = (cx - 44 + braco2[0], 84 + y0 + braco2[1])
    P.append(Parte(capsula(*om2, *co2, 6), CASCA_ESC, z=1, volume='cilindro_h'))
    P.append(Parte(capsula(*co2, *m2, 5), CASCA_ESC, z=1.1))
    for (fx, fy) in ((-7, 6), (-2, 9), (3, 8)):
        P.append(Parte(capsula(*m2, m2[0] + fx, m2[1] + fy, 1.6), CASCA_ESC, z=1.2))
    P.append(Parte(_tufo(m2[0] - 3, m2[1] - 6, 6, 21), ['#165a4c', '#165a4c', '#239063', '#1ebc73', '#91db69'], z=1.3))
    # ---------------- tronco
    contorno = [(cx - 25, 104), (cx - 21, 86), (cx - 23, 66), (cx - 20, 48), (cx - 13, 34), (cx + 13, 34),
                (cx + 20, 48), (cx + 23, 66), (cx + 22, 86), (cx + 27, 104)]
    tronco = poligono([(x, y + y0) for x, y in contorno])
    P.append(Parte(tronco, CASCA, z=2, volume='cilindro_v'))
    # veios da casca (riscos ondulados mais escuros e um fio claro ao lado)
    veio, luz = [], []
    for (x, y) in tronco:
        u = x + 2.2 * math.sin((y - y0) / 7.0 + x * 0.35)
        if int(u) % 7 == 0 and (y * 3 + x) % 11 != 0:
            veio.append((x, y))
        elif int(u) % 7 == 1 and x < cx and (x + y) % 3 == 0:
            luz.append((x, y))
    _px(P, veio, '#45293f', 2.1)
    _px(P, luz, '#ab947a', 2.1)
    # nós da casca
    for (nx, ny) in ((cx - 12, 82), (cx + 4, 96)):
        anel = elipse(nx, ny + y0, 3.5, 4.5) - elipse(nx, ny + y0, 2, 3)
        _px(P, anel, '#2e222f', 2.2)
        _px(P, elipse(nx, ny + y0, 2, 3), '#694f62', 2.15)
    # musgo no tronco (em cima à esquerda e em baixo)
    rnd = random.Random(7)
    for (mx, my, rx, ry) in ((cx - 18, 52, 5, 8), (cx - 16, 100, 8, 4), (cx + 18, 101, 6, 3)):
        mm = {p for p in elipse(mx, my + y0, rx, ry) if p in tronco and rnd.random() < 0.8}
        P.append(Parte(mm, MUSGO, z=2.3, separar=False))
    # cogumelos vermelhos ao pé do tronco
    for (kx, ky) in ((cx - 23, 92), (cx - 26, 98)):
        P.append(Parte(capsula(kx, ky + y0, kx, ky + 3 + y0, 1), ['#c7dcd0'] * 5, z=2.4))
        chapeu = {p for p in elipse(kx, ky + y0, 3.4, 2.4) if p[1] <= ky + y0}
        P.append(Parte(chapeu, ['#6e2727', '#ae2334', '#e83b3b', '#f57d4a', '#fca790'], z=2.5))
        _px(P, [(kx - 1, ky - 1 + y0), (kx + 1, ky - 2 + y0)], '#ffffff', 2.6)
    # ---------------- copa: tufos de folhas (outono e ramos secos à esquerda, verde à direita)
    a = abanar
    for i, (rx_, ry_) in enumerate(((-34, 6), (-40, -2), (-30, -8))):
        P.append(Parte(capsula(cx - 14 + a // 2, 30 + y0, cx + rx_ + a, 18 + ry_ + y0, 1.3), CASCA, z=2.8))
    for (tx, ty, r, s) in ((-26, 22, 12, 1), (-12, 10, 13, 2)):
        t = _tufo(cx + tx + a, ty + y0, r, s)
        P.append(Parte(t, OUTONO, z=3 + s * 0.01))
        _folhagem(P, t, OUTONO, 3 + s * 0.01, s)
    for (tx, ty, r, s) in ((4, 8, 15, 3), (22, 16, 13, 4), (34, 30, 10, 5), (12, 26, 13, 6), (-4, 26, 11, 7)):
        t = _tufo(cx + tx + a, ty + y0, r, s)
        P.append(Parte(t, FOLHA, z=3.2 + s * 0.01))
        _folhagem(P, t, FOLHA, 3.2 + s * 0.01, s)
    rnd = random.Random(11)
    for _ in range(14):   # folhinhas claras soltas na copa
        _px(P, [(cx + rnd.randint(-30, 40) + a, rnd.randint(2, 36) + y0)], '#cddf6c', 3.4)
    # ---------------- cara (virada para a direita)
    fx = cx + 9
    zang = cara == 'furia'
    if not grito:
        olho = '#d5e04b' if zang else '#91db69'
        for ex in (fx - 4, fx + 9):
            if cara == 'x':
                _px(P, [(ex - 1, 49 + y0), (ex + 1, 49 + y0), (ex, 50 + y0), (ex - 1, 51 + y0), (ex + 1, 51 + y0)], OUT, 40)
                continue
            _px(P, elipse(ex, 50 + y0, 4.2, 3.4), '#2e222f', 39)             # o buraco do olho
            _px(P, elipse(ex, 50.5 + y0, 2.6, 2), olho, 40)                  # o brilho
            _px(P, [(ex - 1, 49 + y0)], '#ffffff', 41)
        # sobrolho de casca (mais caído quando zangado)
        k = 2 if zang else 0   # zangado: as pontas de dentro descem
        P.append(Parte(capsula(fx - 9, 46 + y0 - k, fx - 1, 45 + y0 + k, 2.0), CASCA, z=42, volume='cilindro_h'))
        P.append(Parte(capsula(fx + 5, 45 + y0 + k, fx + 13, 46 + y0 - k, 2.0), CASCA, z=42, volume='cilindro_h'))
        # boca rachada
        _px(P, [(x, 64 + y0 + (1 if (x // 3) % 2 else 0)) for x in range(fx - 6, fx + 11)], '#2e222f', 40)
    else:   # o grito: olhos muito abertos e a boca aberta a brilhar por dentro
        for ex in (fx - 4, fx + 9):
            _px(P, elipse(ex, 50 + y0, 4.2, 4.2), '#2e222f', 39)
            _px(P, elipse(ex, 50 + y0, 2.8, 2.8), '#fbff86', 40)
        _px(P, elipse(fx + 2, 67 + y0, 6, 6.5), '#2e222f', 40)
        _px(P, elipse(fx + 2, 69 + y0, 3.5, 3.5), '#d5e04b', 41)
    # nariz de nó (sai para a direita)
    P.append(Parte(capsula(fx + 2, 51 + y0, fx + 10, 58 + y0, 2.8), CASCA, z=43))
    # barba de musgo em fios (abanam com o vento)
    for i, x in enumerate(range(fx - 7, fx + 14, 2)):
        comp = 10 + (i * 7) % 13
        ox = int(round(math.sin(i * 1.7 + a * 0.8) * 2))
        fio = capsula(x, 67 + y0, x + ox, 67 + comp + y0, 1.2 if i % 2 else 1.6)
        if grito:
            fio -= elipse(fx + 2, 67 + y0, 7, 7.5)
        P.append(Parte(fio, MUSGO, z=48 + (i % 2) * 0.01))
    if seiva:
        for (sx, sy) in ((-12, 58), (2, 90), (-16, 80), (18, 76)):
            P.append(Parte(capsula(cx + sx, sy + y0, cx + sx, sy + 4 + y0, 1.6), 'ouro', z=45))
    # ---------------- braço da frente (perto)
    om = (cx + 21, 76 + y0)
    co = (cx + 35 + braco[0] // 2, 82 + y0 + braco[1] // 2)
    m = (cx + 48 + braco[0], 88 + y0 + braco[1])
    P.append(Parte(capsula(*om, *co, 6.5), CASCA, z=46, volume='cilindro_h'))
    P.append(Parte(capsula(*co, *m, 5.5), CASCA, z=46.1))
    for (fx2, fy2) in ((8, 5), (4, 10), (-2, 10)):
        P.append(Parte(capsula(*m, m[0] + fx2, m[1] + fy2, 1.8), CASCA, z=46.2))
    P.append(Parte(_tufo(m[0] + 2, m[1] - 7, 7, 31), FOLHA, z=46.3))
    _px(P, [(co[0] - 2, co[1] - 5), (co[0] - 1, co[1] - 6), (co[0], co[1] - 6)], '#547e64', 46.4)   # musgo no cotovelo
    # ---------------- efeitos dos ataques
    for i in range(bolotas):
        bx, by = 18 + i * 22, 40 + (i % 2) * 14
        P.append(Parte(elipse(bx, by, 3, 3.5), ['#4c3e24', '#694f62', '#966c6c', '#ab947a', '#c7dcd0'], z=60))
        P.append(Parte({p for p in elipse(bx, by - 2, 3.4, 2) if p[1] <= by - 2}, ['#4c3e24', '#4c3e24', '#676633', '#a2a947', '#a2a947'], z=61))
    for i in range(raizes):
        for lx in (26, 62, 100):
            P.append(Parte(capsula(lx + i * 2, 127, lx + i * 3, 116 - i * 3, 2.6), CASCA, z=60))
            _px(P, [(lx + i * 3 - 1, 116 - i * 3)], '#91db69', 61)
    if folhas:
        rnd = random.Random(folhas)
        for _ in range(26):
            x, y = 64 + rnd.uniform(-46, 46), 70 + rnd.uniform(-34, 34)
            c = rnd.choice(['#91db69', '#cddf6c', '#f79617'])
            _px(P, [(x, y), (x + 1, y), (x + 1, y - 1)], c, 62)
    return desenhar(P, 128, 128)


def anims_ent():
    f = ent
    A = {'parado': [f(), f(abanar=1), f(dy=1, abanar=1), f(abanar=-1)],
         'mover': [f(perna=6), f(perna=3, dy=-1), f(perna=0), f(perna=3, dy=-1)],
         'dano': [f(cara='x', abanar=-3)]}
    # fase 1
    A['especial_1'] = [f(braco=(-10, -40)), f(braco=(-8, -46), dy=-1), f(braco=(8, 30)), f(braco=(10, 36), dy=1), f()]       # Varrer com o Braço
    A['especial_2'] = [f(braco=(-6, 20), dy=2), f(braco=(-6, 26), dy=2, raizes=1), f(braco=(-6, 26), dy=2, raizes=2),
                       f(braco=(-6, 26), dy=2, raizes=3), f()]                                                                  # Raízes em Linha
    A['especial_3'] = [f(abanar=3), f(abanar=-3), f(abanar=3, bolotas=2), f(abanar=-3, bolotas=4), f(bolotas=5)]           # Chuva de Bolotas
    # fase 2
    A['especial_4'] = [f(braco=(-10, -30), braco2=(10, -30), cara='furia'), f(braco=(-12, -40), braco2=(12, -40), cara='furia'),
                       f(braco=(0, 30), braco2=(0, 30), dy=2, cara='furia'), f()]                                                 # Chamar Treants
    A['especial_5'] = [f(braco=(-20, 10), braco2=(20, 10)), f(braco=(-26, 20), braco2=(26, 20), raizes=2),
                       f(braco=(-26, 20), braco2=(26, 20), raizes=4), f()]                                                      # Prisão de Raízes
    A['especial_6'] = [f(folhas=1, abanar=2), f(folhas=2, abanar=-2), f(folhas=3, abanar=2), f(folhas=4, abanar=-2)]       # Folhas Cortantes
    # fase 3
    A['especial_7'] = [f(cara='furia', raizes=1), f(cara='furia', raizes=3, dy=1), f(cara='furia', raizes=4, dy=1), f(cara='furia', raizes=4)]
    A['especial_8'] = [f(perna=14), f(perna=20, dy=-2), f(perna=0, dy=2, cara='furia'), f(perna=0, dy=1)]                     # Pisão Gigante
    A['especial_9'] = [f(), f(grito=True), f(grito=True, abanar=3), f(grito=True, abanar=-3), f()]                            # Grito da Árvore
    A['mudar_fase'] = [f(), f(seiva=True, cara='furia'), f(seiva=True, cara='furia', abanar=2), f(seiva=True, cara='furia', abanar=-2), f(seiva=True)]
    caida = [dict(dy=2, braco=(0, 20), braco2=(0, 20)), dict(dy=4, braco=(0, 30), braco2=(0, 30))]
    fim = dict(cara='x', dy=8, braco=(0, 36), braco2=(0, 36))
    A['morrer'] = [f(cara='x'), f(cara='x', **caida[0]), f(cara='x', **caida[1]),
                   dissolver(f(cara='x', dy=6, braco=(0, 34), braco2=(0, 34)), 0.25), dissolver(f(**fim), 0.5),
                   dissolver(f(**fim), 0.75), dissolver(f(**fim), 0.92)]
    return A
