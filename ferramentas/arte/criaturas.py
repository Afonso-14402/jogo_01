"""Moldes de criaturas reutilizáveis (regiões 2–10): cada criatura é um MOLDE + uma configuração.

Moldes: quadrupede, voador, bipede, serpente, amorfo, aracnideo, aquatico, planta, objeto.
Configuração (cfg): k (escala; 1 = 32 px), W (tamanho do quadro), cores (rampas do motor), e opções do molde
(chifres, orelhas, cauda, asas, arma, armadura, olhos...).
Poses (p): dx, dy, a (fase das patas/asas), at (0..1 força do ataque), cara ('normal', 'x', 'furia'), fx (efeito).

As animações-padrão (parado, mover, atacar, dano, morrer) e os ataques especiais saem de anims(molde, cfg, especiais).
"""
import math
import os
import random
import sys
sys.path.insert(0, os.path.dirname(__file__))
from motor import Parte, elipse, retangulo, capsula, poligono, desenhar, deitar, dissolver, guardar, RAMPAS

OUT = '#2e222f'
BRANCO = '#ffffff'


def R(n):
    return RAMPAS[n] if isinstance(n, str) else n


def escurecer(r):
    r = R(r)
    return [OUT, r[0], r[1], r[2], r[2]]


class Tela:
    """Ajuda a desenhar num espaço de 32 unidades escalado por k, com a base em baixo ao centro."""

    def __init__(self, cfg, p):
        self.k = cfg.get('k', 1.0)
        self.W = cfg.get('W', 32)
        self.ox = (self.W - 32 * self.k) / 2 + p.get('dx', 0) * self.k
        self.oy = self.W - 32 * self.k + p.get('dy', 0) * self.k
        self.P = []
        self.p = p

    def cristais(self, pontos, cores, tam=1.0, z=7):
        """Cristais a sair do corpo: pontos = [(x, y, inclinação)], cores = rampas que vão alternando."""
        for i, (x, y, inc) in enumerate(pontos):
            h = (4 + (i % 3) * 1.5) * tam
            w = 1.6 * tam
            topo = (x + inc * h * 0.5, y - h)
            cor = cores[i % len(cores)]
            self.pol([(x - w, y + 1), topo, (x + w, y + 1)], cor, z + i * 0.01)
            self.px([self.S(topo[0] - inc * 0.6, topo[1] + 1.4)], BRANCO, z + 0.5)

    def S(self, x, y):
        return self.ox + x * self.k, self.oy + y * self.k

    def r(self, v):
        return v * self.k

    def add(self, mascara, rampa, z, **kw):
        self.P.append(Parte(mascara, R(rampa) if rampa is not None else None, z=z, **kw))

    def el(self, x, y, rx, ry, rampa, z, **kw):
        self.add(elipse(*self.S(x, y), self.r(rx), self.r(ry)), rampa, z, **kw)

    def cap(self, x1, y1, x2, y2, rad, rampa, z, **kw):
        self.add(capsula(*self.S(x1, y1), *self.S(x2, y2), self.r(rad)), rampa, z, **kw)

    def pol(self, pts, rampa, z, **kw):
        self.add(poligono([self.S(x, y) for x, y in pts]), rampa, z, **kw)

    def ret(self, x1, y1, x2, y2, rampa, z, **kw):
        a, b = self.S(x1, y1)
        c, d = self.S(x2, y2)
        self.add(retangulo(int(a), int(b), int(c), int(d), canto=1), rampa, z, **kw)

    def px(self, pts, cor, z=60):
        self.P.append(Parte({(int(x), int(y)) for x, y in pts}, None, z=z, separar=False, cor=cor))

    def olho(self, x, y, cara, cor=OUT, grande=False):
        X, Y = self.S(x, y)
        X, Y = int(X), int(Y)
        if cara == 'x':
            self.px([(X - 1, Y - 1), (X + 1, Y - 1), (X, Y), (X - 1, Y + 1), (X + 1, Y + 1)], OUT)
            return
        c = '#e83b3b' if cara == 'furia' else cor
        if cara == 'fechado':
            tam = max(2, round(self.k * 1.5))
            self.px([(X + i, Y + 1) for i in range(tam)], OUT, 61)
            return
        tam = max(1, round(self.k * (2.2 if grande else 1.5)))
        self.px([(X + i, Y + j) for i in range(tam) for j in range(tam + 1)], c, 60)
        if c == OUT:   # brilho do olho (luz de cima à esquerda), como no herói
            self.px([(X, Y)], BRANCO, 61)

    def imagem(self):
        if self.p.get('_estrelas') is not None:
            from motor import estrelas
            topo = min((q[1] for pt in self.P for q in pt.m), default=4)
            estrelas(self.P, self.W // 2, max(3, topo - 2), self.p['_estrelas'], z=90)
        return desenhar(self.P, self.W, self.W)


# ---------------- efeitos ----------------

def efeito(t, cfg, p, cx, cy):
    fx = p.get('fx')
    if not fx:
        return
    cor = cfg.get('fx_cor', 'amarelo')
    n = p.get('fn', 1)
    rnd = random.Random(n * 7 + hash(fx) % 100)
    if fx == 'impacto':        # o golpe a acertar: arco branco + estrela amarela
        r = t.r(4 if n == 1 else 6)
        X, Y = t.S(cx + 3, cy + 1)
        X = min(X, t.W - r - 2)   # o impacto não pode sair do quadro
        arco = {(int(X + r * math.cos(u * 0.18 - 1.3)), int(Y + r * math.sin(u * 0.18 - 1.3))) for u in range(15)}
        t.px(arco, '#ffffff', 70)
        if n == 1:
            t.px({(int(X + r) + i, int(Y)) for i in (-1, 0, 1)} | {(int(X + r), int(Y) + j) for j in (-1, 1)}, '#fbff86', 71)
        else:
            t.px({(int(X + r * 0.7 * math.cos(u * 0.18 - 1.3)), int(Y + r * 0.7 * math.sin(u * 0.18 - 1.3))) for u in range(0, 15, 2)},
                 '#fbff86', 70)
        return
    if fx == 'projeteis':      # sopro / cuspe / disparo em linha para a frente
        for i in range(n):
            t.el(cx + 5 + i * 5, cy + (i % 2) * 1.5, 2.0, 1.5, cor, 70)
    elif fx == 'onda':         # onda de choque no chão
        X, Y = t.S(16, 31)
        R1 = t.r(5 + n * 5)
        m = {q for q in elipse(X, Y, R1, max(1.5, R1 * 0.18)) if q not in elipse(X, Y, R1 - 2, max(0.8, R1 * 0.18 - 1))}
        t.add(m, cor, 1, plano=True)
    elif fx in ('magia', 'invocar'):
        pts = {(int(t.S(cx, cy)[0] + rnd.uniform(-1, 1) * t.r(6 + n * 2)), int(t.S(cx, cy)[1] + rnd.uniform(-1, 1) * t.r(5 + n * 2)))
               for _ in range(6 + n * 4)}
        t.P.append(Parte(pts, None, z=72, separar=False, cor=R(cor)[3]))
        if fx == 'invocar':
            t.el(cx, cy, 2 + n, 2 + n, cor, 0.1, plano=True)
    elif fx == 'escudo':
        X, Y = t.S(16, 20)
        rr = t.r(13)
        t.add({q for q in elipse(X, Y, rr, rr) if q not in elipse(X, Y, rr - 1.5, rr - 1.5)}, cor, 71, plano=True)
    elif fx == 'rugido':
        for i in range(n + 1):
            x0 = cx + 4 + i * 3
            t.px([t.S(x0, cy - 3 + j) for j in range(0, 7, 2)], R(cor)[3], 72)
    elif fx == 'area':
        pts = {(int(t.S(16, 16)[0] + rnd.uniform(-1, 1) * t.r(14)), int(t.S(16, 16)[1] + rnd.uniform(-1, 1) * t.r(14))) for _ in range(10 + n * 8)}
        t.P.append(Parte(pts, None, z=72, separar=False, cor=R(cor)[3]))


# ================= molde 1: quadrúpede =================

def quadrupede(cfg, p):
    t = Tela(cfg, p)
    c = cfg.get('cor', 'cinza')
    c2 = cfg.get('cor2', c)
    a = p.get('a', 0)
    at = p.get('at', 0)
    baixo = p.get('baixo', 0)
    corpo_l = cfg.get('comprimento', 1.0)
    alto = cfg.get('altura', 1.0)
    pata = cfg.get('pata', 1.3)
    yb = 21 - (alto - 1) * 4 + baixo
    x0, x1 = 16 - 6 * corpo_l, 16 + 4 * corpo_l
    pe_y = 29
    longe = escurecer(c)

    def perna(xa, dxp, rampa, z):
        # coxa grossa + canela fina + pata: dá articulação em vez de "pau"
        jy = (yb + pe_y) / 2 + 0.5
        jx = xa + dxp * 0.5 - 0.6
        t.cap(xa, yb + 1, jx, jy, pata * 1.35, rampa, z, volume='cilindro_v', separar=z < 1)
        sobe = max(0.0, dxp) * 0.8
        t.cap(jx, jy - sobe * 0.4, xa + dxp, pe_y - 0.5 - sobe, pata * 0.85, rampa, z + 0.05, volume='cilindro_v', separar=False)
        t.el(xa + dxp + 0.8, pe_y - 0.2 - sobe, pata * 1.1, pata * 0.75, rampa, z + 0.1, separar=False)

    perna(x0 + 1, a, longe, 0)
    perna(x1 - 1, -a, longe, 0.2)
    cauda = cfg.get('cauda', 'normal')
    if cauda == 'normal':
        t.cap(x0 - 1, yb - 2, x0 - 5, yb - 5 + p.get('t', 0), 1.4, c, 1)
    elif cauda == 'grossa':
        t.cap(x0 - 1, yb, x0 - 7, yb + 3 + p.get('t', 0), 2.2, c, 1)
    elif cauda == 'curta':
        t.el(x0 - 1.5, yb - 2, 1.5, 1.5, c2, 1)
    corpo_r = cfg.get('grossura', 4.4)
    t.cap(x0, yb, x1, yb - 0.5, corpo_r, c, 2)
    t.el(x0 + 0.5, yb - 0.3, corpo_r + 0.6, corpo_r + 0.3, c, 2.05, separar=False)
    if cfg.get('barriga'):
        t.add({q for q in capsula(*t.S(x0, yb), *t.S(x1, yb - 0.5), t.r(corpo_r)) if q[1] > t.S(0, yb + 1.5)[1]}, cfg['barriga'], 2.1, separar=False)
    if cfg.get('manchas'):
        for i, (mx, my) in enumerate(((x0 + 2, yb - 1), (x0 + 6, yb), (x1 - 2, yb - 2))):
            t.el(mx, my, 1.4, 1.0, cfg['manchas'], 2.2, separar=False, plano=True)
    if cfg.get('espinhos'):
        pts = []
        for i in range(5):
            xx = x0 + i * (x1 - x0) / 4
            pts += [(xx - 1, yb - corpo_r + 1), (xx, yb - corpo_r - 2.5)]
        pts += [(x1 + 1, yb - corpo_r + 1), (x0 - 1, yb - corpo_r + 1)]
        t.pol(pts, cfg['espinhos'], 1.5)
    perna(x0 + 2, -a, c, 3)
    perna(x1, a, c, 3.3)
    if cfg.get('cristais'):
        t.cristais([(x0 + i * (x1 - x0) / 3, yb - corpo_r + 1, -0.3 + i * 0.2) for i in range(4)], cfg['cristais'], 0.9, 2.6)
    # cabeça
    cab = cfg.get('cabeca', 'lobo')
    hx, hy = x1 + 4 + at * 2, yb - 4 + baixo * 0.5 + (2 if p.get('cab') == 'baixa' else -3 if p.get('cab') == 'alta' else 0)
    hr = cfg.get('cabeca_r', 3.6)
    t.cap(x1 - 1, yb - 1, hx - 1, hy + 0.5, 2.6, c, 3.5)
    if cfg.get('juba'):
        t.el(hx - 1.5, hy, hr + 2.2, hr + 2.2, cfg['juba'], 3.8)
    orelhas = cfg.get('orelhas', 'pontiagudas')
    if orelhas == 'pontiagudas':
        t.pol([(hx - 2, hy - 2), (hx - 1, hy - 6.5), (hx + 1, hy - 2.5)], c, 4)
        t.pol([(hx + 0.5, hy - 2.5), (hx + 2, hy - 6.5), (hx + 2.8, hy - 1.5)], c, 6)
    elif orelhas == 'redondas':
        t.el(hx - 1.5, hy - 3.2, 1.4, 1.4, c, 4)
    t.el(hx, hy, hr, hr * 0.95, c, 5)
    focinho = {'lobo': (4, 1.2, 2.6, 1.8), 'felino': (3, 1.0, 2.0, 1.6), 'urso': (3.5, 1.0, 2.4, 2.0), 'reptil': (5, 1.4, 3.6, 1.6),
               'touro': (3.5, 1.4, 2.6, 2.2), 'cavalo': (4.5, 2.0, 2.4, 2.0), 'toupeira': (4, 1.0, 2.4, 1.4)}.get(cab, (4, 1.2, 2.6, 1.8))
    fx_, fy_ = hx + focinho[0], hy + focinho[1]
    t.el(fx_, fy_, focinho[2], focinho[3], cfg.get('cor_focinho', c), 6)
    if cfg.get('bico'):
        t.pol([(fx_ - 1, fy_ - 1.5), (fx_ + 4.5, fy_ + 0.5), (fx_ + 1, fy_ + 2), (fx_ - 1, fy_ + 1.5)], cfg['bico'], 6.2)
    nx, ny = t.S(fx_ + focinho[2] - 0.6, fy_ - 0.8)
    t.px([(nx, ny)], OUT)
    if at > 0.5 or p.get('boca'):
        t.cap(fx_ - 2, fy_ + focinho[3] + 0.6, fx_ + 1.5, fy_ + focinho[3] + 1.5, 0.9, c, 6.5)
        t.px([(nx - 1, ny + t.r(2.2)), (nx - 3, ny + t.r(2.2))], BRANCO)
    chifres = cfg.get('chifres')
    if chifres:
        t.pol([(hx - 1, hy - 2), (hx - 3, hy - 9), (hx + 1, hy - 3)], chifres, 7)
        t.pol([(hx + 1.5, hy - 2.5), (hx + 1, hy - 9.5), (hx + 3, hy - 2.5)], chifres, 7.1)
    if cfg.get('presas'):
        t.cap(fx_ - 0.5, fy_ + 1.5, fx_ + 1, fy_ - 1.5, 0.7, cfg['presas'], 7)
    if cfg.get('cabecas', 1) > 1:
        cores = cfg.get('cores_cabecas', [c] * 4)
        for i in range(cfg['cabecas'] - 1):
            # as outras cabeças em leque, para cima e para trás, cada uma no seu pescoço comprido e curvo
            balanco = (p.get('a', 0) % 2) * (1 if i else -1)
            longo = cab == 'reptil'   # (hidra: pescoços compridos; um cão de 3 cabeças tem-nas juntas aos ombros)
            if longo:
                ex, ey = hx - 3.5 - i * 5, hy - 8 - i * 5.5 + balanco
            else:
                ex, ey = hx - 4.5 - i * 4.5, hy - 5.5 - i * 2.5 + balanco * 0.5
            cc = cores[(i + 1) % len(cores)]
            zc = 3.0 - i * 0.2
            bx, by = x1 - 2 - i * 2.5, yb - 2
            if longo:
                mx, my = (bx + ex) / 2 - 2.5, (by + ey) / 2 + 1.5
                t.cap(bx, by, mx, my, 1.7, cc, zc)
                t.cap(mx, my, ex - 0.5, ey + 1, 1.5, cc, zc + 0.01)
            else:
                t.cap(bx, by, ex - 1, ey + 1, 2.3, cc, zc)
            zh = 3.6 + i * 0.05   # (as cabeças à frente de todos os pescoços)
            if not longo and orelhas == 'pontiagudas':
                t.pol([(ex - 2, ey - 1.5), (ex - 1, ey - 5.5), (ex + 0.8, ey - 2)], cc, zh - 0.01)
                t.pol([(ex + 0.3, ey - 2), (ex + 1.8, ey - 5.5), (ex + 2.4, ey - 1.2)], cc, zh - 0.005)
            t.el(ex, ey, hr * 0.8, hr * 0.75, cc, zh)
            t.el(ex + focinho[0] * 0.75, ey + 0.8, focinho[2] * 0.75, focinho[3] * 0.75, cc, zh + 0.01)
            ox, oy = t.S(ex + focinho[0] * 0.75 + focinho[2] * 0.75 - 0.6, ey + 0.2)
            t.px([(ox, oy)], OUT)
            olho = cfg.get('olho', '#f9c22b')
            if cc in ('amarelo', 'laranja', 'ouro') and olho in ('#f9c22b', '#fbff86', '#f79617'):
                olho = '#e83b3b'   # (olho amarelo numa cabeça amarela não se via)
            t.olho(ex + 1.0, ey - 0.8, p.get('cara', 'normal'), olho)
    t.olho(hx + 1.2, hy - 1, p.get('cara', 'normal'), cfg.get('olho', '#f9c22b'))
    if cfg.get('asas'):
        up = p.get('asa', 0)
        t.pol([(x0 + 3, yb - 3), (x0 - 3, yb - 14 + up * 6), (x0 + 6, yb - 10 + up * 4), (x1, yb - 3)], cfg['asas'], 8)
    efeito(t, cfg, p, fx_, fy_)
    return t.imagem()


# ================= molde 2: voador =================

def voador(cfg, p):
    t = Tela(cfg, p)
    c = cfg.get('cor', 'preto')
    asa_c = cfg.get('asa_cor', c)
    tipo = cfg.get('asa', 'penas')   # penas, membrana, inseto
    fase = p.get('a', 0) % 3
    cx, cy = 15, 15 + (1 if fase == 2 else 0)
    up = [(-9, -10), (-11, 0), (-8, 7)][fase]
    alfa = {'inseto': dict(plano=True)}.get(tipo, {})
    if tipo == 'membrana':
        t.pol([(cx - 1, cy - 2), (cx + up[0], cy + up[1]), (cx + up[0] + 2, cy + up[1] + 5), (cx - 4, cy + 3), (cx - 2, cy + 4)], asa_c, 1, **alfa)
    else:
        t.pol([(cx - 1, cy - 2), (cx + up[0], cy + up[1]), (cx - 5, cy + 4)], asa_c, 1, **alfa)
    if cfg.get('cauda_penas'):
        t.pol([(cx - 4, cy + 1), (cx - 10, cy + 3), (cx - 9, cy + 6), (cx - 4, cy + 3)], cfg['cauda_penas'], 1.5)
    t.el(cx, cy, cfg.get('corpo_rx', 5), cfg.get('corpo_ry', 4), c, 2)
    if cfg.get('riscas'):
        corpo = elipse(*t.S(cx, cy), t.r(cfg.get('corpo_rx', 5)), t.r(cfg.get('corpo_ry', 4)))
        for sx in (-2, 1):
            X = int(t.S(cx + sx, 0)[0])
            t.add({q for q in corpo if q[0] in (X, X + 1)}, cfg['riscas'], 2.5, separar=False, plano=True)
    hx, hy = cx + 5 + p.get('at', 0) * 2, cy - 2
    t.el(hx, hy, cfg.get('cabeca_r', 3), cfg.get('cabeca_r', 3) * 0.95, cfg.get('cabeca_cor', c), 3)
    bico = cfg.get('bico')
    if bico:
        t.pol([(hx + 2, hy - 0.5), (hx + 6, hy + 0.5), (hx + 2, hy + 1.8)], bico, 4)
    if cfg.get('orelhas'):
        t.pol([(hx - 1.5, hy - 2), (hx - 1, hy - 5.5), (hx + 0.5, hy - 2.5)], c, 2.8)
        t.pol([(hx + 0.5, hy - 2.5), (hx + 2, hy - 5.5), (hx + 2.2, hy - 1.5)], c, 3.2)
    if cfg.get('crista'):
        t.pol([(hx - 2, hy - 2), (hx - 1, hy - 6), (hx + 1, hy - 3), (hx + 2, hy - 6), (hx + 2.5, hy - 2)], cfg['crista'], 3.5)
    if cfg.get('ferrao'):
        t.pol([(cx - 4, cy), (cx - 9, cy + 2 + p.get('at', 0) * 2), (cx - 4, cy + 2)], cfg['ferrao'], 1.8)
    for lx in (-1, 2):
        t.cap(cx + lx, cy + 3, cx + lx - 0.5, cy + 6, 0.6, cfg.get('pernas', 'laranja' if bico else c), 1.2)
    up2 = [(-6, -11), (-8, 0), (-5, 7)][fase]
    if tipo == 'membrana':
        t.pol([(cx + 1, cy - 2), (cx + up2[0] + 4, cy + up2[1]), (cx + up2[0] + 6, cy + up2[1] + 5), (cx, cy + 3)], asa_c, 5, **alfa)
    else:
        t.pol([(cx + 1, cy - 2), (cx + up2[0] + 3, cy + up2[1]), (cx - 1, cy + 4)], asa_c, 5, **alfa)
    t.olho(hx + 1, hy - 1, p.get('cara', 'normal'), cfg.get('olho', OUT))
    efeito(t, cfg, p, hx + 3, hy)
    return t.imagem()


# ================= molde 3: bípede (humanoides, golems, mortos-vivos) =================

def bipede(cfg, p):
    t = Tela(cfg, p)
    c = cfg.get('cor', 'verde')          # pele / corpo
    roupa = cfg.get('roupa', c)
    a = p.get('a', 0)
    at = p.get('at', 0)
    corp = cfg.get('corpulento', 0)      # 0..3
    dy = p.get('baixo', 0)
    cx = 15
    perna_c = cfg.get('pernas', roupa)
    if cfg.get('cauda'):
        t.cap(cx - 3, 22 + dy, cx - 9, 25 + p.get('t', 0), 1.5, cfg.get('cauda_cor', c), 0.5)
    if cfg.get('cauda_peixe'):
        t.cap(cx, 22, cx - 2, 29, 3.2, cfg['cauda_peixe'], 1)
        t.pol([(cx - 3, 28), (cx - 8, 31), (cx + 1, 31)], cfg['cauda_peixe'], 1.2)
    else:
        t.cap(cx - 1.5, 23 + dy, cx - 1.5 - a, 29.5, 1.6 + corp * 0.4, escurecer(perna_c), 0, volume='cilindro_v')
        t.cap(cx + 2, 23 + dy, cx + 2 + a, 29.5, 1.6 + corp * 0.4, perna_c, 2, volume='cilindro_v')
        if cfg.get('pes'):
            t.el(cx + 2.8 + a, 30, 2.2, 1.4, cfg['pes'], 2.2)
    # braço de trás
    t.cap(cx - 1, 16 + dy, cx - 3 + a * 0.5, 22 + dy, 1.3 + corp * 0.4, escurecer(cfg.get('braco_cor', roupa)), 0.8)
    # tronco
    tw = 3.8 + corp * 1.2
    t.ret(cx - tw, 14 + dy, cx + tw, 24 + dy, roupa, 3, volume='cilindro_v')
    if cfg.get('armadura'):
        t.ret(cx - tw + 0.5, 15 + dy, cx + tw - 0.5, 19 + dy, cfg['armadura'], 3.2)
    if cfg.get('costelas'):
        for yy in (16, 18, 20):
            X1, Y = t.S(cx - tw + 1.5, yy + dy)
            X2, _ = t.S(cx + tw - 1.5, yy + dy)
            t.px([(x, Y) for x in range(int(X1), int(X2))], OUT, 3.5)
    if cfg.get('cristais'):
        t.cristais([(cx - tw + 0.5, 14.5 + dy, -0.6), (cx - tw + 2.5, 14 + dy, -0.2), (cx + tw - 1, 14.5 + dy, 0.4),
                    (cx + 0.5, 19 + dy, 0.0)], cfg['cristais'], 0.9, 5.9)
    if cfg.get('capa'):
        t.pol([(cx - tw, 14 + dy), (cx - tw - 4, 27 + dy), (cx - tw + 2, 27 + dy)], cfg['capa'], 0.4)
    if cfg.get('asas'):
        up = p.get('asa', 0)
        t.pol([(cx - 2, 15 + dy), (cx - 13, 4 + dy + up * 4), (cx - 11, 16 + dy), (cx - 3, 20 + dy)], cfg['asas'], 0.3)
    # cabeça
    cab = cfg.get('cabeca', 'redonda')
    hx, hy = cx + 1 + at, 9 + dy
    hr = cfg.get('cabeca_r', 5.0)
    if cab == 'focinho':
        t.el(hx, hy, hr, hr * 0.9, c, 5)
        t.el(hx + 3.5, hy + 1.2, 2.8, 1.8, c, 5.5)
    elif cab == 'caveira':
        t.el(hx, hy, hr, hr, cfg.get('osso', 'branco'), 5)
        t.el(hx + 2, hy + hr * 0.75, hr * 0.6, hr * 0.35, cfg.get('osso', 'branco'), 5.1)   # maxilar
        olho_c = cfg.get('olho', OUT)
        for ox in (0.2, 3.0):   # órbitas fundas, com um ponto de luz se o olho brilhar
            X, Y = t.S(hx + ox, hy - 0.8)
            q = max(2, round(t.k * 2))
            t.px([(int(X) + i, int(Y) + j) for i in range(q) for j in range(q)], OUT, 60)
            if olho_c != OUT:
                t.px([(int(X) + q // 2, int(Y) + q // 2)], olho_c, 61)
        X, Y = t.S(hx + 2.3, hy + 1.6)
        t.px([(int(X), int(Y))], OUT, 60)   # nariz
        X1, Y = t.S(hx + 0.5, hy + hr * 0.75)
        X2, _ = t.S(hx + 4.0, hy + hr * 0.75)
        t.px([(x, int(Y)) for x in range(int(X1), int(X2) + 1) if (x - int(X1)) % 2 == 0], OUT, 60)   # dentes
    elif cab == 'bloco':
        t.ret(hx - hr, hy - hr, hx + hr, hy + hr * 0.8, c, 5)
    elif cab == 'tubarao':
        t.pol([(hx - 3, hy - 3), (hx + 7, hy + 1), (hx - 3, hy + 4)], c, 5)
        t.pol([(hx - 2, hy - 3), (hx, hy - 8), (hx + 2, hy - 3)], c, 5.2)
    elif cab == 'capuz':
        t.el(hx, hy, hr + 1, hr + 1, cfg.get('capuz', roupa), 5)
        t.el(hx + 1.5, hy + 1, hr * 0.6, hr * 0.6, ['#2e222f'] * 5, 5.5, separar=False)
    else:
        t.el(hx, hy, hr, hr, c, 5, luz=cfg.get('luz_cara', 0.5))
    if cfg.get('cabelo'):
        t.add({q for q in elipse(*t.S(hx - 0.5, hy - 1), t.r(hr + 0.8), t.r(hr + 0.6)) if q[1] <= t.S(0, hy - 1.5)[1] or q[0] <= t.S(hx - 2, 0)[0]},
              cfg['cabelo'], 5.8)
    if cfg.get('chapeu'):
        t.ret(hx - hr - 1.5, hy - hr, hx + hr + 1.5, hy - hr + 1, cfg['chapeu'], 6)
        t.ret(hx - hr * 0.6, hy - hr - 4, hx + hr * 0.6, hy - hr, cfg['chapeu'], 6.1)
    if cfg.get('coroa'):
        t.pol([(hx - 3, hy - hr + 1), (hx - 3, hy - hr - 3), (hx - 1, hy - hr - 1), (hx, hy - hr - 4), (hx + 1, hy - hr - 1),
               (hx + 3, hy - hr - 3), (hx + 3, hy - hr + 1)], cfg['coroa'], 6.2)
    if cfg.get('chifres'):
        t.pol([(hx - 2, hy - 2), (hx - 4, hy - 8), (hx, hy - 3)], cfg['chifres'], 6.3)
        t.pol([(hx + 1, hy - 3), (hx + 2, hy - 8.5), (hx + 3, hy - 2)], cfg['chifres'], 6.3)
    if cfg.get('orelhas_longas'):
        t.pol([(hx - 2, hy - 1.5), (hx - 8, hy - 4.5), (hx - 2, hy + 1.5)], c, 5.6)
    if cfg.get('ligaduras'):
        for yy in range(-3, 4, 2):
            X1, Y = t.S(hx - hr + 0.5, hy + yy)
            X2, _ = t.S(hx + hr - 0.5, hy + yy)
            t.px([(x, Y) for x in range(int(X1), int(X2))], R('branco')[1], 5.6)
    if cab != 'caveira':
        t.olho(hx + 0.2, hy - 0.3, p.get('cara', 'normal'), cfg.get('olho', OUT))
        if cab not in ('tubarao', 'bloco', 'capuz'):
            t.olho(hx + 2.9, hy - 0.3, p.get('cara', 'normal'), cfg.get('olho', OUT))
    # braço da frente + arma
    arma = cfg.get('arma')
    ang = [(-3, -10), (8, -2), (9, 3), (3, 6)][int(round(at * 3))] if at else (2 + a * -0.5, 6)
    mx, my = cx + 2 + ang[0], 16 + dy + ang[1] + (0 if at else 0)
    if not at:
        mx, my = cx + 3.5 - a * 0.6, 21 + dy
    t.cap(cx + 1.5, 16 + dy, mx, my, 1.4 + corp * 0.45, cfg.get('braco_cor', roupa), 8)
    t.el(mx, my, 1.4 + corp * 0.3, 1.3 + corp * 0.3, cfg.get('mao', c), 8.5)
    if arma:
        cor_arma = cfg.get('arma_cor', 'ferro')
        dxv, dyv = (mx - (cx + 1.5)), (my - (16 + dy))
        nrm = math.hypot(dxv, dyv) or 1
        ux, uy = dxv / nrm, dyv / nrm
        if at == 0:   # parado: arma para a frente, longe da cara
            ux, uy = 0.88, -0.48
        L = {'espada': 10, 'lanca': 15, 'clava': 8, 'cajado': 13, 'machado': 9, 'picareta': 8, 'foice': 12, 'arco': 0, 'adaga': 5, 'tridente': 14}[arma]
        if arma == 'arco':
            t.cap(mx + 1, my - 6, mx + 3, my, 0.8, cor_arma, 9)
            t.cap(mx + 3, my, mx + 1, my + 6, 0.8, cor_arma, 9)
        else:
            ex, ey = mx + ux * L, my + uy * L
            larg = {'espada': 1.2, 'lanca': 0.7, 'clava': 1.0, 'cajado': 0.8, 'machado': 0.8, 'picareta': 0.8, 'foice': 0.8, 'adaga': 1.0, 'tridente': 0.7}[arma]
            t.cap(mx, my, ex, ey, larg, cor_arma if arma in ('espada', 'adaga') else 'madeira', 9)
            if arma == 'clava':
                t.el(ex, ey, 2.4, 2.4, cor_arma, 9.2)
            elif arma in ('machado', 'picareta'):
                t.pol([(ex - 2, ey - 2), (ex + 3, ey - 1), (ex - 2, ey + 3)], cor_arma, 9.2)
            elif arma == 'cajado':
                t.el(ex, ey, 1.8, 1.8, cfg.get('fx_cor', 'agua'), 9.2)
            elif arma == 'lanca':
                t.pol([(ex - 1.2, ey + 1), (ex + ux * 3.5, ey + uy * 3.5), (ex + 1.2, ey + 1)], cor_arma, 9.2)
            elif arma == 'tridente':
                for o in (-1.5, 0, 1.5):
                    t.cap(ex + o, ey, ex + o + ux * 3, ey + uy * 3, 0.4, cor_arma, 9.2)
            elif arma == 'foice':
                t.pol([(ex, ey), (ex + 6, ey + 1), (ex + 8, ey + 4), (ex + 2, ey + 2)], cor_arma, 9.2)
    if cfg.get('escudo'):
        t.pol([(cx - 6, 15 + dy), (cx - 1, 15 + dy), (cx - 1, 22 + dy), (cx - 3.5, 25 + dy), (cx - 6, 22 + dy)], cfg['escudo'], 7)
    efeito(t, cfg, p, hx + 3, hy + 2)
    return t.imagem()


# ================= molde 4: serpente / verme =================

def serpente(cfg, p):
    t = Tela(cfg, p)
    c = cfg.get('cor', 'verde')
    sobe = p.get('sobe', 0)
    ond = p.get('a', 0)
    n = cfg.get('segmentos', 6)
    pts = []
    for i in range(n):
        u = i / (n - 1)
        x = 4 + u * 20
        y = 27 - u * (8 + sobe) + math.sin(u * 6 + ond) * 2.2
        pts.append((x, y))
    for i in range(n - 1):
        rr = cfg.get('grossura', 3.2) * (0.75 + 0.25 * (i / n))
        t.cap(*pts[i], *pts[i + 1], rr, c, 1 + i * 0.1)
        if cfg.get('barriga'):
            pass
        if cfg.get('aneis'):
            X, Y = t.S(*pts[i])
            t.px([(X, Y - t.r(rr) + 1), (X, Y - t.r(rr) + 2)], R(cfg['aneis'])[1], 2 + i * 0.1)
    if cfg.get('cristais'):
        t.cristais([(pts[i][0], pts[i][1] - cfg.get('grossura', 3.2) * 0.7, -0.2) for i in range(n - 1)], cfg['cristais'], 0.8, 2.5)
    hx, hy = pts[-1][0] + 3 + p.get('at', 0) * 3, pts[-1][1] - 1
    if cfg.get('asas'):
        up = ond % 2
        t.pol([(hx - 8, hy + 2), (hx - 14, hy - 8 + up * 6), (hx - 4, hy - 1)], cfg['asas'], 0.5)
    t.el(hx, hy, cfg.get('cabeca_r', 3.6), cfg.get('cabeca_r', 3.6) * 0.8, cfg.get('cabeca_cor', c), 3)
    if cfg.get('boca_redonda'):
        t.el(hx + 2.5, hy, 1.6, 1.8, ['#45293f'] * 5, 3.5, separar=False)
    elif p.get('at', 0) > 0.5 or p.get('boca'):
        t.pol([(hx + 1, hy + 1), (hx + 7, hy + 3), (hx + 1, hy + 2.5)], c, 3.4)
    if cfg.get('chifres'):
        t.pol([(hx - 2, hy - 2), (hx - 4, hy - 7), (hx, hy - 2.5)], cfg['chifres'], 4)
    if not cfg.get('cego'):
        t.olho(hx + 1, hy - 1.2, p.get('cara', 'normal'), cfg.get('olho', '#f9c22b'))
    if cfg.get('buraco'):
        t.el(5, 30.5, 9, 2.0, ['#2e222f'] * 5, 0.2, plano=True)
    if cfg.get('agua'):
        X, Y = t.S(6, 30)
        t.add({q for q in elipse(X, Y, t.r(11), t.r(2.5)) if q not in elipse(X, Y, t.r(9), t.r(1.5))}, 'agua', 20, plano=True)
    efeito(t, cfg, p, hx + 2, hy)
    return t.imagem()


# ================= molde 5: amorfo (fantasmas, elementais, nuvens, lodos) =================

def amorfo(cfg, p):
    t = Tela(cfg, p)
    c = cfg.get('cor', 'branco')
    tipo = cfg.get('tipo', 'fantasma')
    fase = p.get('a', 0)
    cy = 15 + math.sin(fase * 1.6) * 1.2 + p.get('baixo', 0)
    if tipo == 'fantasma':
        t.el(16, cy, 7, 7, c, 1, luz=0.2)
        t.pol([(9, cy), (23, cy), (22, cy + 9), (19, cy + 7 + (fase % 2) * 2), (16, cy + 10), (13, cy + 7 + ((fase + 1) % 2) * 2), (10, cy + 9)], c, 1.1)
        if cfg.get('bracos', True):
            t.cap(20, cy + 3, 25 + p.get('at', 0) * 3, cy + 1 - p.get('at', 0) * 2, 1.4, c, 2)
    elif tipo == 'elemental':
        t.el(16, cy + 1, 6.5, 8, c, 1)
        for i in range(4):
            ang = fase * 0.8 + i * math.pi / 2
            t.el(16 + math.cos(ang) * 8, cy + math.sin(ang) * 6, 1.8, 1.8, cfg.get('cor2', c), 2)
        t.pol([(12, cy - 5), (14, cy - 13 - (fase % 2) * 2), (16, cy - 7), (18, cy - 14 + (fase % 2) * 2), (20, cy - 5)], cfg.get('cor2', c), 0.8)
    elif tipo == 'nuvem':
        for (x, y, r) in ((11, cy + 2, 5), (16, cy - 1, 6), (21, cy + 2, 5)):
            t.el(x, y, r, r * 0.85, c, 1)
    elif tipo == 'lodo':
        t.add({q for q in elipse(*t.S(16, 30 - 6), t.r(10 + (fase % 2)), t.r(7 - (fase % 2))) if q[1] <= t.S(0, 30)[1]}, c, 1)
        for (x, y) in ((11, 22), (19, 20), (15, 26)):
            t.el(x, y + (fase % 2), 1.3, 1.3, cfg.get('cor2', c), 2, separar=False)
    elif tipo == 'sombra':
        t.el(16, cy + 2, 6, 9, c, 1, brilho=False)
        t.pol([(10, cy + 6), (22, cy + 6), (24, 31), (8, 31)], c, 0.9, brilho=False)
    if cfg.get('coroa'):
        t.pol([(12, cy - 6), (12, cy - 10), (14, cy - 8), (16, cy - 11), (18, cy - 8), (20, cy - 10), (20, cy - 6)], cfg['coroa'], 3)
    olho = cfg.get('olho', OUT)
    t.olho(17, cy - 1, p.get('cara', 'normal'), olho, grande=True)
    t.olho(20, cy - 1, p.get('cara', 'normal'), olho, grande=True)
    if cfg.get('boca') or p.get('at', 0) > 0.5:
        t.el(18.5, cy + 3, 1.5, 1.8 + p.get('at', 0), ['#2e222f'] * 5, 3, separar=False)
    efeito(t, cfg, p, 21, cy + 2)
    return t.imagem()


# ================= molde 6: aracnídeo / inseto / crustáceo =================

def aracnideo(cfg, p):
    t = Tela(cfg, p)
    c = cfg.get('cor', 'preto')
    a = p.get('a', 0)
    at = p.get('at', 0)
    pernas = cfg.get('pernas', 8)
    cy = 22
    tipo0 = cfg.get('tipo', 'aranha')
    n2 = pernas // 2
    for i in range(n2):
        ox = 9 + i * (12 / max(1, n2 - 1))
        d = (i - (n2 - 1) / 2) / max(1, (n2 - 1) / 2)       # -1 (trás) .. 1 (frente)
        s = 2.0 if (i + int(a)) % 2 == 0 else -2.0
        sobe_p = 1.5 if (s > 0 and a) else 0
        alto_j = 7 if tipo0 == 'aranha' else 4
        for lado, rampa, z, desv in ((0, escurecer(c), 0, -1.5), (1, c, 1.5, 0)):
            kx, ky = ox + d * 4 + desv, cy - alto_j + lado
            fx2 = ox + d * 8 + desv + s * (1 if lado else -1)
            t.cap(ox, cy - 1, kx, ky, 0.9 + 0.2 * lado, rampa, z)
            t.cap(kx, ky - sobe_p * 0.5, fx2, 29.5 - sobe_p, 0.7 + 0.2 * lado, rampa, z + 0.1, separar=False)
    tipo = cfg.get('tipo', 'aranha')
    if tipo == 'aranha':
        t.el(10, cy - 2, 7, 6, c, 2)
        if cfg.get('marca'):
            t.el(9, cy - 3, 2, 1.5, cfg['marca'], 2.5, separar=False)
        t.el(19, cy - 1, 4.5, 4, c, 3)
        hx, hy = 22, cy - 1
    elif tipo == 'escorpiao':
        t.el(12, cy - 1, 8, 4, c, 2)
        cauda = [(6, cy - 2), (3, cy - 7), (4, cy - 13), (9 + at * 4, cy - 16 + at * 3)]
        for i in range(3):
            t.cap(*cauda[i], *cauda[i + 1], 1.8 - i * 0.3, c, 3 + i * 0.1)
        t.pol([(cauda[-1][0], cauda[-1][1]), (cauda[-1][0] + 4, cauda[-1][1] + 1), (cauda[-1][0] + 1, cauda[-1][1] + 3)], cfg.get('ferrao', c), 3.4)
        hx, hy = 20, cy - 1
    elif tipo == 'caranguejo':
        t.el(15, cy - 2, 9, 6, c, 2)
        hx, hy = 20, cy - 5
        t.cap(hx - 2, hy, hx - 2, hy - 4, 0.6, c, 2.5)
        t.cap(hx + 1, hy, hx + 1, hy - 4, 0.6, c, 2.5)
    else:   # escaravelho / lagarta
        t.el(14, cy - 3, 9, 6, c, 2)
        X, Y = t.S(14, cy - 9)
        X2, Y2 = t.S(14, cy + 3)
        t.px([(int(X), y) for y in range(int(Y), int(Y2))], OUT, 2.5)
        hx, hy = 23, cy - 2
        t.el(hx, hy, 3, 2.8, cfg.get('cabeca_cor', c), 3)
        if cfg.get('chifre'):
            t.pol([(hx, hy - 1), (hx + 2, hy - 7), (hx + 3, hy - 1)], cfg['chifre'], 3.5)
    if cfg.get('pincas'):
        for s, z in ((0, 4), (2, 6)):
            px_, py_ = hx + 4 + s, hy + 2 - at * 2
            t.cap(hx + 1, hy + 2, px_, py_, 1.3, c, z)
            t.pol([(px_ - 1, py_ - 2), (px_ + 5, py_ - 4 - at * 2), (px_ + 4, py_ - 1), (px_ + 5, py_ + 2), (px_, py_ + 2)], cfg.get('pinca_cor', c), z + 0.5)
    for i in range(cfg.get('olhos', 2)):
        t.olho(hx + 1 + (i % 2) * 1.5, hy - 1.5 + (i // 2) * 1.5, p.get('cara', 'normal'), cfg.get('olho', '#e83b3b'))
    if tipo == 'aranha' and at > 0.5:
        t.pol([(hx + 2, hy + 2), (hx + 4, hy + 5), (hx + 3, hy + 2)], BRANCO if False else 'branco', 4)
    efeito(t, cfg, p, hx + 3, hy)
    return t.imagem()


# ================= molde 7: aquático (peixes, polvos, alforrecas, baleias) =================

def aquatico(cfg, p):
    t = Tela(cfg, p)
    c = cfg.get('cor', 'agua')
    tipo = cfg.get('tipo', 'peixe')
    fase = p.get('a', 0)
    cy = 16 + math.sin(fase * 1.5) * 1.0
    if tipo == 'peixe':
        cau = (fase % 2) * 2 - 1
        t.pol([(6, cy), (1, cy - 5 + cau), (2, cy + 5 + cau)], cfg.get('barbatana', c), 0.5)
        t.el(15, cy, 10 * cfg.get('comprido', 1), 6, c, 1)
        t.pol([(12, cy - 5), (16, cy - 10), (19, cy - 5)], cfg.get('barbatana', c), 0.8)
        if cfg.get('espinhos'):
            for i in range(5):
                t.cap(10 + i * 2.5, cy - 4, 8 + i * 3, cy - 12, 0.4, cfg['espinhos'], 0.6)
        if cfg.get('lanterna'):
            t.cap(22, cy - 4, 27, cy - 11, 0.5, c, 1.2)
            t.el(27.5, cy - 11.5, 1.6, 1.6, cfg['lanterna'], 1.3)
        if p.get('at', 0) > 0.5 or cfg.get('dentes'):
            t.pol([(20, cy + 1), (26, cy - 1), (26, cy + 4)], ['#2e222f'] * 5, 2, separar=False)
            t.px([t.S(22 + i * 1.5, cy + 1) for i in range(3)], BRANCO)
        t.olho(21, cy - 2, p.get('cara', 'normal'), cfg.get('olho', OUT), grande=True)
    elif tipo == 'polvo':
        for i in range(6):
            ang = math.pi * (0.1 + 0.8 * i / 5)
            x2 = 16 + math.cos(ang) * 11
            y2 = cy + 6 + math.sin(ang) * 8 + ((fase + i) % 2) * 2
            t.cap(16 + math.cos(ang) * 4, cy + 4, x2, y2, 1.4, c, 0.5 + (i % 2) * 2)
        t.el(16, cy - 2, 7, 7.5, c, 1)
        t.olho(18, cy, p.get('cara', 'normal'), cfg.get('olho', '#f9c22b'), grande=True)
        t.olho(14, cy, p.get('cara', 'normal'), cfg.get('olho', '#f9c22b'), grande=True)
    elif tipo == 'alforreca':
        t.add({q for q in elipse(*t.S(16, cy - 2), t.r(8), t.r(6)) if q[1] <= t.S(0, cy)[1]}, c, 1, plano=False)
        for i in range(5):
            x = 10 + i * 3
            t.cap(x, cy, x + ((fase + i) % 2) * 2 - 1, cy + 11, 0.5, c, 0.5)
        t.olho(17, cy - 3, p.get('cara', 'normal'), cfg.get('olho', OUT))
    elif tipo == 'baleia':
        cau = (fase % 2) * 3
        t.pol([(5, cy), (-1, cy - 6 + cau), (0, cy + 4 + cau)], c, 0.5)
        t.el(17, cy + 1, 13, 7, c, 1)
        t.add({q for q in elipse(*t.S(17, cy + 1), t.r(13), t.r(7)) if q[1] > t.S(0, cy + 3)[1]}, cfg.get('barriga', 'branco'), 1.1, separar=False)
        t.olho(25, cy - 1, p.get('cara', 'normal'), cfg.get('olho', OUT))
        if cfg.get('estrelas'):
            pts = [t.S(10 + i * 3, cy - 2 + (i % 3)) for i in range(6)]
            t.px(pts, '#fbff86')
    efeito(t, cfg, p, 26, cy)
    return t.imagem()


# ================= molde 8: planta =================

def planta(cfg, p):
    t = Tela(cfg, p)
    c = cfg.get('cor', 'verde')
    caule = cfg.get('caule', 'verde_esc')
    fase = p.get('a', 0)
    at = p.get('at', 0)
    tipo = cfg.get('tipo', 'carnivora')
    if tipo == 'carnivora':
        hx, hy = 18 + at * 6, 12 - at * 2 + (fase % 2)
        t.cap(14, 30, 15, 22, 1.5, caule, 0)
        t.cap(15, 22, hx - 3, hy + 3, 1.5, caule, 0.5)
        for s in (-1, 1):
            t.pol([(14, 28), (14 + s * 8, 24 - (fase % 2)), (14 + s * 3, 29)], caule, 0.6)
        ab = 2 + at * 3
        t.pol([(hx - 4, hy), (hx + 5, hy - ab), (hx + 2, hy - 1)], c, 2)
        t.pol([(hx - 4, hy + 1), (hx + 5, hy + 2 + ab), (hx + 2, hy + 2)], c, 2.1)
        t.px([t.S(hx + i * 1.5, hy - ab * 0.5) for i in range(3)], BRANCO)
        t.olho(hx - 1, hy - 3, p.get('cara', 'normal'), cfg.get('olho', '#f9c22b'))
    elif tipo == 'arvore':
        t.cap(13, 30, 12 - fase % 2, 27, 1.6, caule, 0)
        t.cap(19, 30, 20 + fase % 2, 27, 1.6, caule, 0)
        t.ret(11, 13, 21, 28, caule, 1, volume='cilindro_v')
        t.el(16, 9, 10, 7, c, 2)
        t.cap(20, 18, 26 + at * 4, 14 - at * 6, 1.4, caule, 3)
        t.olho(18, 18, p.get('cara', 'normal'), cfg.get('olho', '#d5e04b'), grande=True)
        t.olho(14, 18, p.get('cara', 'normal'), cfg.get('olho', '#d5e04b'), grande=True)
    elif tipo == 'cacto':
        t.ret(13, 10, 19, 29, c, 1, volume='cilindro_v')
        t.cap(13, 19, 9, 15 - (fase % 2), 1.5, c, 0.5)
        t.cap(19, 17, 23 + at * 3, 13 - at * 3, 1.5, c, 2)
        t.olho(17, 14, p.get('cara', 'normal'), OUT)
    elif tipo == 'driade':
        cfg2 = dict(cfg, cor=cfg.get('pele', 'verde'), roupa=c, cabelo=cfg.get('cabelo', 'verde_esc'), cabeca='redonda')
        return bipede(cfg2, p)
    efeito(t, cfg, p, 22, 12)
    return t.imagem()


# ================= molde 9: objeto vivo (vagonetas, livros, olhos, relógios, totens, prismas...) =================

def objeto(cfg, p):
    t = Tela(cfg, p)
    c = cfg.get('cor', 'madeira')
    tipo = cfg.get('tipo', 'livro')
    fase = p.get('a', 0)
    at = p.get('at', 0)
    cy = 16 + math.sin(fase * 1.5) * 1.2
    if tipo == 'livro':
        ab = 4 + (fase % 2) * 2 + at * 3
        t.pol([(16, cy + 4), (16 - 9, cy - ab + 4), (16 - 9, cy - ab - 4), (16, cy - 4)], c, 1)
        t.pol([(16, cy + 4), (16 + 9, cy - ab + 4), (16 + 9, cy - ab - 4), (16, cy - 4)], c, 1.1)
        t.pol([(16, cy + 3), (16 + 8, cy - ab + 3), (16 + 8, cy - ab - 3), (16, cy - 3)], 'branco', 1.2, separar=False)
        t.olho(19, cy - 3, p.get('cara', 'normal'), cfg.get('olho', '#e83b3b'), grande=True)
    elif tipo == 'olho':
        for i in range(5):
            ang = i * 1.25 + fase * 0.3
            t.cap(16, cy, 16 + math.cos(ang) * 12, cy + 6 + math.sin(ang) * 6, 1.0, cfg.get('cor2', c), 0.5)
        t.el(16, cy, 8, 8, 'branco', 1)
        t.el(17 + at * 2, cy, 3.5 - at, 3.5 - at, cfg.get('iris', c), 2, separar=False)
        t.px([t.S(17 + at * 2, cy)], OUT)
    elif tipo == 'vagoneta':
        t.pol([(5, 15), (27, 15), (25, 26), (7, 26)], c, 1)
        for x in (10, 22):
            t.el(x, 27 + (fase % 2) * 0, 2.6, 2.6, 'ferro', 2)
        t.el(16, 15, 9, 2, ['#2e222f'] * 5, 1.5, plano=True)
        t.olho(13, 20, p.get('cara', 'normal'), cfg.get('olho', '#30e1b9'))
        t.olho(19, 20, p.get('cara', 'normal'), cfg.get('olho', '#30e1b9'))
    elif tipo == 'prisma':
        t.pol([(16, cy - 12), (24, cy + 4), (16, cy + 12), (8, cy + 4)], c, 1)
        t.pol([(16, cy - 12), (24, cy + 4), (16, cy + 2)], cfg.get('cor2', c), 1.1, separar=False)
        t.olho(17, cy, p.get('cara', 'normal'), OUT, grande=True)
    elif tipo == 'totem':
        for i, cor in enumerate(cfg.get('blocos', ['madeira', 'verde', 'vermelho'])):
            y0 = 29 - (i + 1) * 8
            t.ret(9, y0, 23, y0 + 7, cor, 1 + i)
            t.olho(13, y0 + 3, p.get('cara', 'normal'), cfg.get('olho', '#f9c22b'))
            t.olho(19, y0 + 3, p.get('cara', 'normal'), cfg.get('olho', '#f9c22b'))
    elif tipo == 'relogio':
        t.ret(10, 6, 22, 30, c, 1, volume='cilindro_v')
        t.el(16, 11, 4.5, 4.5, 'branco', 2)
        ang = fase * 1.2
        t.px([t.S(16 + math.cos(ang) * k, 11 + math.sin(ang) * k) for k in (0, 1, 2, 3)], OUT)
        t.cap(16, 20, 16 + math.sin(fase) * 2, 26, 0.6, 'ouro', 2)
        t.cap(10, 14, 5 - at * 3, 18 - at * 4, 1.0, c, 3)
        t.cap(22, 14, 27 + at * 3, 18 - at * 4, 1.0, c, 3)
    elif tipo == 'armadura':
        cfg2 = dict(cfg, cor=c, roupa=c, cabeca='bloco', olho=cfg.get('olho', '#30e1b9'), arma=cfg.get('arma', 'espada'))
        return bipede(cfg2, p)
    elif tipo == 'coracao':
        t.el(16, cy, 9, 10, c, 1)
        t.el(16, cy, 4, 5, cfg.get('cor2', c), 2, separar=False)
        for i in range(6):
            ang = i * 1.05 + fase * 0.4
            t.el(16 + math.cos(ang) * 13, cy + math.sin(ang) * 11, 1.6, 1.6, c, 3)
    elif tipo == 'mimico':   # baú que morde: a tampa abre-se, dentes e língua
        abre = 1.5 + at * 6 + (fase % 2) * 1.2
        t.ret(6, 18, 26, 28, cfg.get('cor', 'madeira'), 1)
        t.ret(6, 22, 26, 23, 'ouro', 1.2)
        for x in range(8, 24, 3):
            t.pol([(x, 18), (x + 1.5, 15.8), (x + 3, 18)], 'branco', 1.5)
        t.cap(16, 17, 19 + at * 7, 16 - at * 2 + (fase % 2), 1.3, 'rosa', 1.4)
        t.ret(6, 18 - abre - 5, 26, 18 - abre, cfg.get('cor', 'madeira'), 3)
        t.ret(15, 18 - abre - 3, 17, 18 - abre - 1, 'ouro', 3.1)
        for x in range(8, 24, 3):
            t.pol([(x, 18 - abre), (x + 1.5, 20.2 - abre), (x + 3, 18 - abre)], 'branco', 3.2)
        t.olho(11, 18 - abre - 3.5, p.get('cara', 'normal'), '#e83b3b')
        t.olho(20, 18 - abre - 3.5, p.get('cara', 'normal'), '#e83b3b')
    elif tipo == 'carruagem':
        t.pol([(8, 12), (26, 12), (28, 24), (6, 24)], c, 2)
        for x in (10, 24):
            t.el(x, 26, 4, 4, 'ouro', 3)
        t.el(30, 18, 3, 4, cfg.get('cor2', 'laranja'), 1)
    efeito(t, cfg, p, 22, cy)
    return t.imagem()


MOLDES = {'quadrupede': quadrupede, 'voador': voador, 'bipede': bipede, 'serpente': serpente, 'amorfo': amorfo,
          'aracnideo': aracnideo, 'aquatico': aquatico, 'planta': planta, 'objeto': objeto}


# ---------------- animações ----------------

ESPECIAIS = {
    # nome: lista de poses (dicionários)
    'investida': [dict(cab='baixa', baixo=1, a=1), dict(cab='baixa', baixo=1, dx=-1), dict(dx=3, at=1, a=2), dict(dx=4, at=1, a=-2), dict(dx=2)],
    'golpe': [dict(at=0.34, dx=-1), dict(at=0.67), dict(at=1, dx=2), dict(at=1, dx=2), dict()],
    'sopro': [dict(cab='alta', boca=True), dict(boca=True, at=0.6, fx='projeteis', fn=1), dict(boca=True, at=0.8, fx='projeteis', fn=2),
              dict(boca=True, at=0.8, fx='projeteis', fn=3), dict()],
    'onda': [dict(baixo=2), dict(dy=-5, a=1), dict(dy=-7, a=2), dict(baixo=1, fx='onda', fn=1), dict(fx='onda', fn=2), dict(fx='onda', fn=3)],
    'magia': [dict(cara='furia', fx='magia', fn=1), dict(fx='magia', fn=2, at=0.5), dict(fx='magia', fn=3, at=0.7), dict(fx='projeteis', fn=2, at=1), dict()],
    'invocar': [dict(cab='alta', fx='invocar', fn=1), dict(cab='alta', fx='invocar', fn=2), dict(cab='alta', fx='invocar', fn=3, boca=True), dict()],
    'escudo': [dict(baixo=1), dict(baixo=1, fx='escudo'), dict(baixo=1, fx='escudo'), dict()],
    'rugido': [dict(cab='alta'), dict(cab='alta', boca=True, fx='rugido', fn=1), dict(cab='alta', boca=True, fx='rugido', fn=2), dict()],
    'area': [dict(cara='furia'), dict(fx='area', fn=1), dict(fx='area', fn=2, at=0.5), dict(fx='area', fn=3), dict()],
    'salto': [dict(baixo=2), dict(dy=-6, a=2), dict(dy=-8, a=-2, dx=2), dict(baixo=1, dx=3), dict(dx=3)],
    'desaparecer': [dict(), dict(_dissolver=0.4), dict(_dissolver=0.8), dict(_dissolver=0.97), dict(_dissolver=0.5), dict()],
    'enterrar': [dict(), dict(dy=4), dict(dy=8), dict(dy=12, _dissolver=0.5), dict(dy=12, _dissolver=0.9)],
    'levantar': [dict(dy=12, _dissolver=0.6), dict(dy=9, _dissolver=0.3), dict(dy=6), dict(dy=3), dict(dy=-1), dict()],
    'aparecer': [dict(_dissolver=0.95), dict(_dissolver=0.7), dict(_dissolver=0.4), dict()],
    'descer': [dict(dy=-14, _dissolver=0.3), dict(dy=-9), dict(dy=-4), dict(dy=1, baixo=1), dict()],
    'atirar': [dict(at=0.34, dx=-1), dict(at=0.67, dx=-1), dict(at=1, fx='projeteis', fn=1), dict(at=1, fx='projeteis', fn=2), dict()],
    'dormir': [dict(cara='x', baixo=1), dict(cara='x', baixo=1, dy=1)],
    'pancada_chao': [dict(at=0.67, dy=-2), dict(at=1, dy=-3), dict(at=1, baixo=1, fx='onda', fn=1), dict(baixo=1, fx='onda', fn=2), dict(fx='onda', fn=3)],
}


def virar(img):
    """De patas para o ar, assente no chão (morte de animais e bichos)."""
    from PIL import Image
    v = img.transpose(Image.FLIP_TOP_BOTTOM)
    bb = v.getbbox()
    if not bb:
        return v
    out = Image.new('RGBA', v.size, (0, 0, 0, 0))
    out.alpha_composite(v.crop(bb), (bb[0], v.height - 1 - (bb[3] - bb[1])))
    return out


def _img(molde, cfg, pose):
    pose = dict(pose)
    dis = pose.pop('_dissolver', 0)
    im = MOLDES[molde](cfg, pose)
    if cfg.get('invertido'):          # anda no teto / no "céu" de cabeça para baixo
        from PIL import Image
        im = im.transpose(Image.FLIP_TOP_BOTTOM)
    return dissolver(im, dis) if dis else im


def anims(molde, cfg, especiais=(), voa=False, chave='ataque'):
    """Devolve {animação: [frames]}. especiais: lista de nomes de ESPECIAIS (por ordem: ataque_1/especial_1, ...)."""
    if molde == 'bipede' and cfg.get('k', 1.0) >= 1.5:   # humanoides grandes (guardiões, bosses): proporções de adulto
        import heroico
        return heroico.anims(cfg, especiais, chave)
    if molde == 'bipede' and cfg.get('k', 1.0) >= 0.7:   # humanoides: corpo do herói (humanoide.py)
        import humanoide
        return humanoide.anims(cfg, especiais, chave)
    f = lambda **k: _img(molde, cfg, k)
    A = {}
    if voa or molde in ('voador', 'amorfo', 'aquatico') or (molde == 'objeto' and cfg.get('tipo') in ('livro', 'olho', 'prisma', 'coracao')):
        A['parado'] = [f(a=i, dy=[0, -1, -1, 0][i]) for i in range(4)]
        A['mover'] = [f(a=i, dx=i % 2, dy=[0, -1, -2, -1][i]) for i in range(4)]
    elif molde == 'serpente':
        A['parado'] = [f(a=i * 0.8) for i in range(4)]
        A['mover'] = [f(a=i * 1.2, dx=i % 2) for i in range(4)]
    else:
        A['parado'] = [f(), f(t=1), f(baixo=1, t=1), f(t=0)]
        A['mover'] = [f(a=3, t=1), f(a=1.5, dy=-1), f(a=0, dy=-2, t=-1), f(a=-3, t=1), f(a=-1.5, dy=-1), f(a=0, dy=-2, t=-1)]
    # antecipação (recua e agacha) -> investida com impacto -> recupera
    A['atacar'] = [f(at=0.34, dx=-2, baixo=1), f(at=1, dx=3, fx='impacto', fn=1), f(at=1, dx=3, fx='impacto', fn=2),
                   f(at=0.3, dx=1)]
    A['dano'] = [f(dx=-2, baixo=1, cara='x')]
    morto = f(cara='x')
    if molde in ('voador', 'amorfo', 'aquatico') or cfg.get('desfaz'):
        A['morrer'] = [f(cara='x'), dissolver(f(cara='x', dy=3), 0.3), dissolver(f(cara='x', dy=6), 0.6), dissolver(f(cara='x', dy=8), 0.9)]
    elif molde in ('quadrupede', 'aracnideo', 'serpente', 'objeto', 'planta') and molde != 'bipede':
        caido = virar(morto)
        A['morrer'] = [f(cara='x', dx=-1, baixo=1), caido, dissolver(caido, 0.45), dissolver(caido, 0.8)]
    else:
        A['morrer'] = [f(cara='x', dx=-1), deitar(morto), dissolver(deitar(morto), 0.45), dissolver(deitar(morto), 0.8)]
    for i, nome in enumerate(especiais):
        if isinstance(nome, tuple):           # ('nome_da_animação', 'tipo de ESPECIAIS')
            A[nome[0]] = [f(**pp) for pp in ESPECIAIS[nome[1]]]
        else:
            A[f'{chave}_{i + 1}'] = [f(**pp) for pp in ESPECIAIS[nome]]
    if chave == 'especial':
        A['mudar_fase'] = [f(), f(cara='furia', fx='magia', fn=2), f(cara='furia', fx='magia', fn=3, dy=-1), f(cara='furia')]
        A['atordoado'] = [f(cara='x', baixo=1, _estrelas=i) for i in range(4)]
    return A


def lote(pasta, lista, ver=None):
    """Gera e grava uma lista de criaturas: [(nome, molde, cfg, especiais, chave)]."""
    for item in lista:
        nome, molde, cfg, esp = item[:4]
        chave = item[4] if len(item) > 4 else 'ataque'
        if ver and nome not in ver:
            continue
        import referencias
        if nome in referencias.REFERENCIAS:   # há um desenho à mão: usa-se esse
            r = referencias.REFERENCIAS[nome]
            guardar(pasta, nome, referencias.anims(nome, r[1], r[2]))
        else:
            guardar(pasta, nome, anims(molde, cfg, esp, chave=chave))
        print('  ', nome)
