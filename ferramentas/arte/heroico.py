"""Molde HEROICO: os humanoides grandes (guardiões, mini-bosses e bosses de 48 px ou mais).

O molde "bipede" pequeno usa o corpo do herói (cabeça grande, estilo "chibi") e ampliava-o 2×–4×: os bosses
ficavam com píxeis gordos e pareciam meninos. Este molde desenha-os à resolução certa (sem ampliar) e com
proporções de adulto: cabeça pequena, ombros largos, peito, cinto, saiote, pernas com joelho e botas,
braços com cotovelo, capa, armadura com ombreiras, arma grande e olhos que brilham.

Usa a mesma configuração do molde "bipede" (criaturas.py) — cor, roupa, pernas, cabeca, corpulento, armadura,
capa, coroa, chifres, chapeu, cabelo, barba, asas, cauda, cauda_peixe, costelas, ligaduras, cristais, escudo,
arma, arma_cor, mao, olho, fx_cor — e as mesmas poses (a, at, baixo, dx, dy, cab, boca, cara, fx, fn).
As animações: parado (respirar, 4), mover (passo, 6), atacar (antecipação → golpe → impacto → volta, 5),
dano, morrer (cai e desfaz-se) e os especiais de criaturas.ESPECIAIS.
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from motor import deitar, dissolver
import criaturas as C
from criaturas import Tela, efeito, escurecer, OUT, BRANCO, R

ARMA_L = {'espada': 13, 'lanca': 18, 'clava': 10, 'cajado': 16, 'machado': 11, 'picareta': 10, 'foice': 14, 'arco': 0,
          'adaga': 6, 'tridente': 17}


def _brilho_olho(t, x, y, cor, cara):
    """Olho de lado: 1 olho; se a cor não for o contorno, brilha (2×2 com um píxel claro)."""
    if cara == 'x' or cor == OUT:
        t.olho(x, y, cara, cor)
        return
    X, Y = t.S(x, y)
    q = max(1, round(t.k * 0.9))
    c = '#e83b3b' if cara == 'furia' else cor
    t.px([(int(X) + i, int(Y) + j) for i in range(q + 1) for j in range(q)], c, 62)
    t.px([(int(X) + q, int(Y))], BRANCO, 63)


def frame(cfg, p):
    t = Tela(cfg, p)
    c = cfg.get('cor', 'verde')
    roupa = cfg.get('roupa', c)
    pernas = cfg.get('pernas', roupa)
    corp = cfg.get('corpulento', 0)
    cab = cfg.get('cabeca', 'redonda')
    golem = cab == 'bloco' and corp >= 1
    a = p.get('a', 0)                     # fase das pernas (−3..3)
    lev = p.get('l', 0)                   # pé no ar: >0 o da frente, <0 o de trás
    at = p.get('at', 0)
    b = p.get('baixo', 0) * 1.2           # agachar
    res = p.get('t', 0) * 0.45            # respirar
    cara = p.get('cara', 'normal')
    olho = cfg.get('olho', OUT)
    cx = 15.0
    tw = 4.0 + corp * 1.3                 # meia largura dos ombros
    sy = 11.2 + b - res                   # ombros
    hip = 20.5 + b * 0.6
    # cabeça (inclina para a frente a atacar; para cima a rugir)
    hx = cx + 1.2 + at * 0.9
    hy = 6.3 + b - res
    if p.get('cab') == 'alta':
        hx, hy = hx - 0.4, hy - 0.8
    elif p.get('cab') == 'baixa':
        hx, hy = hx + 1.2, hy + 1.2
    hr = 3.1 + (0.9 if golem else 0) + cfg.get('cabeca_r', 5.0) * 0

    # ---------- atrás: asas, capa, cauda ----------
    if cfg.get('asas'):
        up = p.get('asa', 0) + (1 if p.get('fx') else 0)
        for k, z in ((0, 0.25), (1, 0.3)):
            o = k * 3
            t.pol([(cx - 1, sy + 1), (cx - 9 - o, sy - 9 + up * 3 - o), (cx - 15 - o, sy - 4 + up * 2), (cx - 12 - o, sy + 6),
                   (cx - 4, sy + 7)], cfg['asas'] if k == 0 else escurecer(cfg['asas']), z)
    if cfg.get('capa'):
        vento = math.sin(a * 0.9) * 0.8 + (1.2 if at else 0)
        t.pol([(cx - tw * 0.7, sy), (cx + tw * 0.2, sy), (cx - 1.5 - vento, 29.6), (cx - tw - 3.5 - vento, 29.2),
               (cx - tw - 2 - vento * 0.5, 22)], cfg['capa'], 0.2)
        t.pol([(cx - tw - 3.5 - vento, 29.2), (cx - 1.5 - vento, 29.6), (cx - 2.5 - vento, 27.8)], escurecer(cfg['capa']), 0.21)
    if cfg.get('cauda'):
        t.cap(cx - 2, hip, cx - 9, 25 + math.sin(a) * 1.5, 1.6, cfg.get('cauda_cor', c), 0.5)
        t.cap(cx - 9, 25 + math.sin(a) * 1.5, cx - 12, 22 + math.sin(a), 1.0, cfg.get('cauda_cor', c), 0.5)

    # ---------- pernas ----------
    def perna(hx_, pe_x, pe_y, cor, z):
        kx = (hx_ + pe_x) / 2 + 1.0 + b * 0.4          # o joelho dobra para a frente
        ky = (hip + pe_y) / 2 - 0.2
        grossa = 1.8 + corp * 0.5
        t.cap(hx_, hip, kx, ky, grossa, cor, z, volume='cilindro_v')
        t.cap(kx, ky, pe_x, pe_y - 1.2, grossa * 0.85, cor, z + 0.05, volume='cilindro_v')
        t.el(pe_x + 0.9, pe_y, 2.2 + corp * 0.4, 1.3, cfg.get('pes', 'couro' if not golem else cor), z + 0.1)
    if cfg.get('cauda_peixe'):
        t.cap(cx, hip - 1, cx - 2, 28.5, 3.6, cfg['cauda_peixe'], 1)
        t.pol([(cx - 3, 28), (cx - 9, 31), (cx + 2, 31)], cfg['cauda_peixe'], 1.2)
    else:
        perna(cx - 1.4, cx - 1.6 - a * 1.2, 30.3 - max(0, -lev) * 1.6, escurecer(pernas), 1)
        perna(cx + 1.6, cx + 1.4 + a * 1.2, 30.3 - max(0, lev) * 1.6, pernas, 2)

    # ---------- braço de trás (ou escudo) ----------
    braco = cfg.get('braco_cor', roupa)
    ox_b, oy_b = cx - tw * 0.55, sy + 0.9
    mb = (ox_b - 0.8 - a * 0.5, sy + 8.2 - (2 if at else 0))
    t.cap(ox_b, oy_b, ox_b - 0.4 - a * 0.25, sy + 4.6, 1.5 + corp * 0.5, escurecer(braco), 0.8)
    t.cap(ox_b - 0.4 - a * 0.25, sy + 4.6, *mb, 1.3 + corp * 0.45, escurecer(braco), 0.82)
    t.el(*mb, 1.4 + corp * 0.45, 1.3 + corp * 0.4, escurecer(cfg.get('mao', c)), 0.84)
    if cfg.get('escudo'):
        ex, ey = mb[0] - 1, mb[1] - 4
        t.pol([(ex - 3.5, ey - 3), (ex + 3.5, ey - 3), (ex + 3.5, ey + 3), (ex, ey + 6.5), (ex - 3.5, ey + 3)], cfg['escudo'], 7)
        t.pol([(ex - 0.6, ey - 2), (ex + 0.6, ey - 2), (ex + 0.6, ey + 4), (ex - 0.6, ey + 4)], 'ouro', 7.1, separar=False)

    # ---------- tronco ----------
    cin = 19.6 + b * 0.6
    t.pol([(cx - tw, sy), (cx + tw, sy), (cx + tw * 0.72, cin), (cx - tw * 0.72, cin)], roupa, 3, volume='cilindro_v')
    # saiote / túnica até meio da coxa
    t.pol([(cx - tw * 0.75, cin), (cx + tw * 0.75, cin), (cx + tw * 0.85 + 0.6, 23 + b * 0.5), (cx - tw * 0.85 - 0.6, 23 + b * 0.5)],
          escurecer(roupa) if not cfg.get('saiote') else cfg['saiote'], 2.6, plano=True)
    t.ret(cx - tw * 0.74, cin - 0.6, cx + tw * 0.74, cin + 0.8, cfg.get('cinto', 'couro'), 3.4, plano=True)
    t.ret(cx + 0.3, cin - 0.6, cx + 1.6, cin + 0.8, 'ouro', 3.5, plano=True)    # fivela
    if cfg.get('armadura'):
        arm = cfg['armadura']
        t.pol([(cx - tw + 0.6, sy + 0.6), (cx + tw - 0.6, sy + 0.6), (cx + tw * 0.65, sy + 6.5), (cx, sy + 7.8), (cx - tw * 0.65, sy + 6.5)],
              arm, 3.2)
        t.el(cx + tw * 0.55, sy + 0.8, 2.4 + corp * 0.6, 1.8 + corp * 0.4, arm, 7.6)   # ombreira da frente (por cima do braço)
    if cfg.get('costelas'):
        for yy in (sy + 2.5, sy + 4.5, sy + 6.5):
            X1, Y = t.S(cx - tw * 0.6, yy)
            X2, _ = t.S(cx + tw * 0.6, yy)
            t.px([(x, int(Y)) for x in range(int(X1), int(X2))], OUT, 3.6)
    if cfg.get('ligaduras'):
        for yy in (sy + 2, sy + 5, sy + 8, 24, 27):
            X1, Y = t.S(cx - tw * 0.7, yy)
            X2, _ = t.S(cx + tw * 0.7, yy + 0.8)
            t.px([(x, int(Y + (x % 3 == 0))) for x in range(int(X1), int(X2))], R('branco')[1], 3.7)
    if cfg.get('cristais'):
        t.cristais([(cx - tw + 0.8, sy + 0.5, -0.6), (cx - tw + 3, sy, -0.2), (cx + tw - 1.5, sy + 0.5, 0.4), (cx - 1, sy + 5, 0.0)],
                   cfg['cristais'], 1.0 + corp * 0.15, 5.9)

    # ---------- cabeça ----------
    if not golem:
        t.cap(cx + 0.6, sy, hx - 0.6, hy + 2.5, 1.2, c, 4.5)    # pescoço
    if cab == 'focinho':
        t.el(hx, hy, hr, hr * 0.95, c, 5)
        t.el(hx + 3.0, hy + 1.1, 2.5, 1.7, cfg.get('cor_focinho', c), 5.5)
        t.px([t.S(hx + 5.0, hy + 0.6)], OUT, 61)                   # nariz
        if p.get('boca') or cara == 'furia':
            t.px([t.S(hx + 2.5 + i * 0.5, hy + 2.6) for i in range(5)], OUT, 61)
        if not cfg.get('chifres'):
            t.pol([(hx - 1.5, hy - 2), (hx - 2.5, hy - 5.5), (hx + 0.3, hy - 2.5)], c, 5.6)   # orelha
        _brilho_olho(t, hx + 1.4, hy - 0.8, olho, cara)
    elif cab == 'caveira':
        osso = cfg.get('osso', 'branco')
        t.el(hx, hy - 0.2, hr + 0.2, hr, osso, 5)
        t.el(hx + 1.5, hy + 2.4, 2.0, 1.1, osso, 5.1)               # maxilar
        X, Y = t.S(hx + 1.0, hy - 0.9)
        q = max(2, round(t.k * 1.6))
        t.px([(int(X) + i, int(Y) + j) for i in range(q) for j in range(q)], OUT, 60)   # órbita
        if olho != OUT and cara != 'x':
            t.px([(int(X) + q // 2, int(Y) + q // 2), (int(X) + q // 2 - 1, int(Y) + q // 2)], olho, 61)
        X1, Y = t.S(hx + 0.3, hy + 2.2)
        X2, _ = t.S(hx + 3.2, hy + 2.2)
        t.px([(x, int(Y)) for x in range(int(X1), int(X2) + 1) if (x - int(X1)) % 2 == 0], OUT, 61)   # dentes
        t.px([t.S(hx + 2.4, hy + 0.9)], OUT, 61)
    elif cab == 'bloco':
        t.ret(hx - hr, hy - hr + 0.5, hx + hr, hy + hr * 0.8, c, 5)
        X1, Y = t.S(hx - 0.5, hy - 0.2)
        X2, _ = t.S(hx + hr - 0.6, hy - 0.2)
        cor_o = '#e83b3b' if cara == 'furia' else (olho if olho != OUT else '#f9c22b')
        if cara != 'x':
            t.px([(x, int(Y) + j) for x in range(int(X1), int(X2)) for j in range(max(1, round(t.k * 0.8)))], cor_o, 62)   # fenda que brilha
        else:
            t.olho(hx + 1.5, hy - 0.2, 'x')
    elif cab == 'capuz':
        cz = cfg.get('capuz', roupa)
        t.el(hx - 0.3, hy - 0.2, hr + 1.2, hr + 1.3, cz, 5)
        t.pol([(hx - 1, hy - hr - 1), (hx - 4.5, hy - hr - 2.5), (hx - 3, hy - 1)], cz, 4.9)     # bico do capuz
        t.el(hx + 1.6, hy + 0.6, hr * 0.62, hr * 0.75, ['#2e222f'] * 5, 5.5, separar=False)
        _brilho_olho(t, hx + 2.1, hy - 0.1, olho if olho != OUT else '#f9c22b', cara)
    elif cab == 'tubarao':
        t.pol([(hx - 3, hy - 3), (hx + 7, hy + 1), (hx - 3, hy + 4)], c, 5)
        t.pol([(hx - 2, hy - 3), (hx, hy - 8), (hx + 2, hy - 3)], c, 5.2)
        _brilho_olho(t, hx + 2, hy - 0.5, olho, cara)
    else:   # cara de pessoa, de lado
        t.el(hx, hy, hr, hr * 1.1, c, 5, luz=cfg.get('luz_cara', 0.5))
        t.el(hx + hr - 0.2, hy + 0.6, 0.8, 0.9, c, 5.05, luz=0.6)    # nariz
        if cfg.get('barba'):
            t.pol([(hx - 1, hy + 1), (hx + hr + 0.3, hy + 1.2), (hx + hr - 0.5, hy + 4.5), (hx + 0.8, hy + 7.5), (hx - 1.5, hy + 4)],
                  cfg['barba'], 5.7)
        elif p.get('boca') or cara == 'furia':
            t.px([t.S(hx + 1.6 + i * 0.5, hy + 2.0) for i in range(3)], OUT, 61)
        if cfg.get('cabelo'):
            t.add({q for q in C.elipse(*t.S(hx - 0.7, hy - 0.9), t.r(hr + 0.6), t.r(hr + 0.5))
                   if q[1] <= t.S(0, hy - 1.6)[1] or q[0] <= t.S(hx - 1.2, 0)[0]}, cfg['cabelo'], 5.8)
            if cfg.get('cabelo_longo', cfg.get('desfaz')):
                t.cap(hx - 2.2, hy, hx - 3.4, hy + 6, 1.6, cfg['cabelo'], 4.8)
        _brilho_olho(t, hx + 1.2, hy - 0.4, olho, cara)
    # ---------- por cima da cabeça ----------
    topo = hy - hr - (0.5 if cab == 'capuz' else 0)
    if cfg.get('chapeu'):
        t.ret(hx - hr - 2, topo + 0.6, hx + hr + 2, topo + 1.6, cfg['chapeu'], 6)
        t.pol([(hx - hr + 0.5, topo + 0.8), (hx + hr - 0.5, topo + 0.8), (hx + hr - 1.2, topo - 3.5), (hx - hr + 0.8, topo - 3.2)], cfg['chapeu'], 6.1)
    if cfg.get('coroa'):
        cr = cfg['coroa']
        t.pol([(hx - 3, topo + 1.4), (hx - 3.2, topo - 2.6), (hx - 1.6, topo - 0.6), (hx - 0.2, topo - 3.4), (hx + 1.2, topo - 0.6),
               (hx + 2.8, topo - 2.6), (hx + 2.8, topo + 1.4)], cr, 6.2)
        t.px([t.S(hx - 0.2, topo)], '#e83b3b' if cr != 'vermelho' else '#4d9be6', 63)   # pedra preciosa
    if cfg.get('chifres'):
        ch = cfg['chifres']
        t.pol([(hx - 1.6, hy - 2.2), (hx - 5.5, hy - 5.5), (hx - 6, hy - 9.5), (hx - 3.5, hy - 6.5), (hx + 0.2, hy - 3)], ch, 6.3)
        t.pol([(hx + 0.8, hy - 2.8), (hx + 2.8, hy - 7), (hx + 5.5, hy - 9), (hx + 4, hy - 5.5), (hx + 2.4, hy - 2.4)], ch, 6.3)
    if cfg.get('orelhas_longas'):
        t.pol([(hx - 1.5, hy - 1), (hx - 7, hy - 4.5), (hx - 1.5, hy + 1.5)], c, 5.6)
    if cfg.get('ligaduras') and cab not in ('caveira', 'bloco'):
        for yy in (-2, 0, 2):
            X1, Y = t.S(hx - hr + 0.4, hy + yy)
            X2, _ = t.S(hx + hr - 0.4, hy + yy + 0.6)
            t.px([(x, int(Y)) for x in range(int(X1), int(X2))], R('branco')[1], 5.65)

    # ---------- braço da frente + arma ----------
    arma = cfg.get('arma')
    ox, oy = cx + tw * 0.55, sy + 0.9
    if p.get('fx') in ('magia', 'invocar') and not at:
        cot, mao, dirv = (ox + 2.5, sy + 1.5), (ox + 4.5, sy - 1.5), (0.15, -1)
    elif at <= 0:
        cot, mao, dirv = (ox + 0.6, sy + 4.6), (ox + 1.4 - a * 0.3, sy + 8.4), (0.5, -0.86)
        if arma == 'cajado':
            dirv = (0.08, -1)
    elif at < 0.5:     # antecipação: arma levantada atrás da cabeça
        cot, mao, dirv = (ox + 1.0, sy - 1.0), (cx - 0.5, sy - 3.5), (-0.82, -0.57)
    elif at < 0.9:     # a meio do golpe
        cot, mao, dirv = (ox + 2.4, sy - 0.2), (ox + 5.5, sy - 1.5), (0.75, -0.66)
    else:              # golpe dado
        cot, mao, dirv = (ox + 2.4, sy + 1.6), (ox + 6.0, sy + 4.2), (0.96, 0.28)
    t.cap(ox, oy, *cot, 1.6 + corp * 0.55, braco, 8)
    t.cap(*cot, *mao, 1.4 + corp * 0.5, braco, 8.05)
    mr = 1.4 + corp * 0.45 + (0.8 if golem else 0)
    t.el(*mao, mr, mr * 0.95, cfg.get('mao', c), 8.5)
    if arma:
        za = 4.4 if 0 < at < 0.5 else 9
        cor_arma = cfg.get('arma_cor', 'ferro')
        ux, uy = dirv
        n = math.hypot(ux, uy)
        ux, uy = ux / n, uy / n
        L = ARMA_L[arma] * (1 + corp * 0.08)
        mx, my = mao
        if arma == 'arco':
            t.cap(mx + 0.5, my - 7, mx + 3, my, 0.8, cor_arma if cor_arma != 'ferro' else 'madeira', za)
            t.cap(mx + 3, my, mx + 0.5, my + 7, 0.8, cor_arma if cor_arma != 'ferro' else 'madeira', za)
            t.px([t.S(mx + 0.5, my - 7 + i) for i in range(15)], '#c7dcd0', za + 0.1)
        elif arma == 'cajado':
            t.cap(mx - ux * 6, my - uy * 6, mx + ux * L * 0.6, my + uy * L * 0.6, 0.75, 'madeira', za)
            ex, ey = mx + ux * L * 0.6, my + uy * L * 0.6
            t.el(ex, ey, 2.0, 2.0, cfg.get('fx_cor', 'agua'), za + 0.2)
            t.px([t.S(ex - 0.6, ey - 0.6)], BRANCO, za + 0.3)
            t.pol([(ex - 2.2, ey + 1.5), (ex - 1.2, ey - 2.5), (ex, ey + 1.8)], 'ouro', za + 0.1)
        else:
            ex, ey = mx + ux * L, my + uy * L
            if arma in ('espada', 'adaga'):
                t.cap(mx - ux * 1.2, my - uy * 1.2, mx, my, 0.6, 'couro', za)                   # punho
                gx, gy = mx + ux * 1.0, my + uy * 1.0
                t.cap(gx - uy * 2.2, gy + ux * 2.2, gx + uy * 2.2, gy - ux * 2.2, 0.55, 'ouro', za + 0.1)   # guarda
                t.cap(gx, gy, ex, ey, 1.2 + corp * 0.15, cor_arma, za + 0.05)
                t.px([t.S(gx + ux * k + 0.3, gy + uy * k - 0.4) for k in range(2, int(L) - 1, 1)], BRANCO, za + 0.2)   # fio
            else:
                t.cap(mx - ux * 2, my - uy * 2, ex, ey, 0.75, 'madeira', za)
                if arma == 'clava':
                    t.el(ex, ey, 2.8 + corp * 0.4, 2.8 + corp * 0.4, cor_arma, za + 0.2)
                    for ang in range(0, 360, 72):
                        r = 3.2 + corp * 0.4
                        t.px([t.S(ex + math.cos(math.radians(ang)) * r, ey + math.sin(math.radians(ang)) * r)], '#c7dcd0', za + 0.3)
                elif arma in ('machado', 'picareta'):
                    px_, py_ = -uy, ux        # perpendicular
                    if arma == 'machado':
                        t.pol([(ex - ux * 4, ey - uy * 4), (ex + px_ * 4.5 - ux * 5, ey + py_ * 4.5 - uy * 5),
                               (ex + px_ * 5 + ux * 1, ey + py_ * 5 + uy * 1), (ex + ux * 0.5, ey + uy * 0.5)], cor_arma, za + 0.2)
                    else:
                        t.cap(ex - px_ * 4, ey - py_ * 4, ex + px_ * 4, ey + py_ * 4, 0.8, cor_arma, za + 0.2)
                elif arma == 'lanca':
                    t.pol([(ex - uy * 1.3, ey + ux * 1.3), (ex + ux * 4, ey + uy * 4), (ex + uy * 1.3, ey - ux * 1.3)], cor_arma, za + 0.2)
                elif arma == 'tridente':
                    t.cap(ex - uy * 2, ey + ux * 2, ex + uy * 2, ey - ux * 2, 0.5, cor_arma, za + 0.2)
                    for o in (-2, 0, 2):
                        t.cap(ex + o * -uy, ey + o * ux, ex + o * -uy + ux * 3.5, ey + o * ux + uy * 3.5, 0.45, cor_arma, za + 0.2)
                elif arma == 'foice':
                    t.pol([(ex, ey), (ex + 7, ey + 1), (ex + 9, ey + 4.5), (ex + 2, ey + 2)], cor_arma, za + 0.2)
    efeito(t, cfg, p, hx + 3, hy + 3)
    return t.imagem()


def _img(cfg, pose):
    pose = dict(pose)
    dis = pose.pop('_dissolver', 0)
    im = frame(cfg, pose)
    return dissolver(im, dis) if dis else im


def anims(cfg, especiais=(), chave='ataque'):
    f = lambda **k: _img(cfg, k)
    A = {}
    A['parado'] = [f(t=0), f(t=0.6), f(t=1), f(t=0.6)]
    passos = []
    for i in range(6):
        ph = i * math.pi / 3
        passos.append(f(a=2.6 * math.sin(ph), l=math.cos(ph) * 0.9, dy=-1 if i % 3 == 0 else 0))
    A['mover'] = passos
    A['atacar'] = [f(at=0.34, dx=-1, baixo=1), f(at=0.67), f(at=1, dx=2, fx='impacto', fn=1), f(at=1, dx=2, fx='impacto', fn=2),
                   f(at=0.3, dx=1)]
    A['dano'] = [f(dx=-2, baixo=1, cara='x', cab='baixa')]
    morto = f(cara='x')
    A['morrer'] = [f(cara='x', dx=-1, baixo=1, cab='alta'), f(cara='x', baixo=2, cab='baixa'), deitar(morto),
                   dissolver(deitar(morto), 0.45), dissolver(deitar(morto), 0.8)]
    for i, nome in enumerate(especiais):
        if isinstance(nome, tuple):
            A[nome[0]] = [f(**pp) for pp in C.ESPECIAIS[nome[1]]]
        else:
            A[f'{chave}_{i + 1}'] = [f(**pp) for pp in C.ESPECIAIS[nome]]
    if chave == 'especial':
        A['mudar_fase'] = [f(), f(cara='furia', fx='magia', fn=2, cab='alta'), f(cara='furia', fx='magia', fn=3, dy=-1, cab='alta'),
                           f(cara='furia')]
        A['atordoado'] = [f(cara='x', baixo=1, _estrelas=i) for i in range(4)]
    return A
