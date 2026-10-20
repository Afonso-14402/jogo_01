"""Imagens para a página do jogo no itch.io (docs/PUBLICACAO.md, secção 3), em pixel art desenhada píxel a píxel
e ampliada sem desfocar (vizinho mais próximo), só com cores da Resurrect 64:

  capa     630×500  (315×250 ×2): o herói de costas, pequenino, na Praça de Ascendia, a olhar para a Torre ao pôr
                    do sol, com o logótipo. Também capa.gif (nuvens a passar, janelas e cristal a piscar, o herói a
                    respirar, o brilho do logótipo).
  banner   960×300  (480×150 ×2): a Torre a subir pelo meio, com as 10 regiões em faixas (de baixo para cima:
                    Floresta → Abismo), cada uma com a sua paisagem e cores, e o logótipo numa janela do Sistema.
  icone    512×512  (64×64 ×8): a janela azul do Sistema com uma torre pequenina dentro. Também os ícones do
                    projeto Godot e das exportações (arte/ui/icone_*.png e icone_jogo.ico).
  gif      640×360, 6 s: a partir das capturas seguidas do robô (testes/robo_captura.gd, modo esquiva), metade do
                    tamanho com o zoom 4 do jogo (cada píxel da arte fica com 2×2).
  capturas 1920×1080: copia as capturas escolhidas do robô para arte/publicacao/.

Saída: arte/publicacao/ (com .gdignore: o Godot não importa estas imagens, não vão para dentro do jogo).
Uso:   python3 ferramentas/arte/publicacao.py capa|banner|icone|tudo
       python3 ferramentas/arte/publicacao.py gif <pasta das capturas> <primeira> [n=120]
       python3 ferramentas/arte/publicacao.py capturas <nome>=<ficheiro.png> ...
"""
import math
import os
import random
import re
import shutil
import sys

from PIL import Image

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
ARTE = os.path.join(RAIZ, 'arte')
PASTA = os.path.join(ARTE, 'publicacao')
OUT = '#2e222f'

RESURRECT = ('2e222f 3e3546 625565 966c6c ab947a 694f62 7f708a 9babb2 c7dcd0 ffffff 6e2727 b33831 ea4f36 f57d4a '
             'ae2334 e83b3b fb6b1d f79617 f9c22b 7a3045 9e4539 cd683d e6904e fbb954 4c3e24 676633 a2a947 d5e04b '
             'fbff86 165a4c 239063 1ebc73 91db69 cddf6c 313638 374e4a 547e64 92a984 b2ba90 0b5e65 0b8a8f 0eaf9b '
             '30e1b9 8ff8e2 323353 484a77 4d65b4 4d9be6 8fd3ff 45293f 6b3e75 905ea9 a884f3 eaaded 753c54 a24b6f '
             'cf657f ed8099 831c5d c32454 f04f78 f68181 fca790 fdcbb0').split()


def hx(c):
    return tuple(int(c[i:i + 2], 16) for i in (1, 3, 5))


PAL = [hx('#' + c) for c in RESURRECT]


def mais_perto(rgb):
    return min(PAL, key=lambda p: (p[0] - rgb[0]) ** 2 + (p[1] - rgb[1]) ** 2 + (p[2] - rgb[2]) ** 2)


def imagem_paleta():
    """Imagem 'P' com as 64 cores (para gravar GIFs sem cores de fora)."""
    p = Image.new('P', (1, 1))
    flat = []
    for c in PAL:
        flat += list(c)
    p.putpalette(flat + [0, 0, 0] * (256 - len(PAL)))
    return p


def ampliar(im, k):
    return im.resize((im.width * k, im.height * k), Image.NEAREST)


def guardar_gif(quadros, caminho, ms):
    pal = imagem_paleta()
    q = [f.convert('RGB').quantize(palette=pal, dither=Image.Dither.NONE) for f in quadros]
    q[0].save(caminho, save_all=True, append_images=q[1:], duration=ms, loop=0, optimize=False, disposal=1)


def verificar_paleta(im, nome):
    fora = {c for c in im.convert('RGB').get_flattened_data() if c not in PAL}
    if fora:
        print('  AVISO: %s tem %d cores fora da paleta: %s' % (nome, len(fora), list(fora)[:5]))


class Tela:
    """Uma tela RGB com ajudas para desenhar (cores em '#rrggbb')."""

    def __init__(self, w, h, cor=OUT):
        self.w, self.h = w, h
        self.im = Image.new('RGB', (w, h), hx(cor))
        self.px = self.im.load()

    def p(self, x, y, cor):
        x, y = int(x), int(y)
        if 0 <= x < self.w and 0 <= y < self.h:
            self.px[x, y] = hx(cor) if isinstance(cor, str) else cor

    def get(self, x, y):
        return self.px[int(x), int(y)]

    def ret(self, x0, y0, x1, y1, cor):
        for y in range(int(y0), int(y1) + 1):
            for x in range(int(x0), int(x1) + 1):
                self.p(x, y, cor)

    def colar(self, spr, x, y):
        """Cola um sprite RGBA (só os píxeis opacos)."""
        sp = spr.load()
        for yy in range(spr.height):
            for xx in range(spr.width):
                c = sp[xx, yy]
                if c[3] > 128:
                    self.p(x + xx, y + yy, c[:3])


def faixas(t, y0, y1, cores, x0=0, x1=None, xadrez=2):
    """Céu em faixas de cor de y0 a y1, com 'xadrez' linhas de passagem em xadrez entre faixas."""
    x1 = t.w - 1 if x1 is None else x1
    n = len(cores)
    for y in range(y0, y1 + 1):
        u = (y - y0) / max(1, (y1 - y0 + 1)) * n
        k = min(n - 1, int(u))
        resto = (k + 1 - u) * (y1 - y0 + 1) / n   # linhas até à faixa seguinte
        for x in range(x0, x1 + 1):
            c = cores[k]
            if k < n - 1 and resto <= xadrez and (x + y) % 2 == 0:
                c = cores[k + 1]
            t.p(x, y, c)


# ------------------------------------------------------------------ sprites do jogo ------------------------------------
def logo_quadros():
    """Os 8 quadros do logótipo (arte/ui/logo.png), recortados à volta das letras."""
    im = Image.open(os.path.join(ARTE, 'ui', 'logo.png')).convert('RGBA')
    q = [im.crop((f * 160, 0, f * 160 + 160, 64)) for f in range(8)]
    caixa = q[0].getbbox()
    return [f.crop(caixa) for f in q]


def heroi_costas(caminho='heroi/heroi_parado_cima.png', espelhar=False):
    """O herói parado de costas (arte/heroi/heroi_parado_cima.png), 4 quadros 32×32, em contraluz: mais escuro (as
    costas estão na sombra, o sol está à frente dele) e com um contorno de luz laranja à esquerda e em cima.
    Serve também para os NPCs da praça (outro caminho)."""
    im = Image.open(os.path.join(ARTE, caminho)).convert('RGBA')
    sombra = hx('#45293f')
    quadros = []
    for f in range(im.width // 32):
        q = im.crop((f * 32, 0, f * 32 + 32, 32))
        if espelhar:
            q = q.transpose(Image.FLIP_LEFT_RIGHT)
        px = q.load()
        cheio = {(x, y) for y in range(32) for x in range(32) if px[x, y][3] > 128}
        novo = Image.new('RGBA', (32, 32))
        npx = novo.load()
        for (x, y) in cheio:
            r, g, b, _ = px[x, y]
            if (r, g, b) == hx(OUT):
                c = (r, g, b)
            else:
                c = mais_perto((r * 0.8 + sombra[0] * 0.2, g * 0.8 + sombra[1] * 0.2, b * 0.8 + sombra[2] * 0.2))
            npx[x, y] = c + (255,)
        # luz do pôr do sol: o 1.º píxel de dentro, do lado esquerdo e em cima
        for (x, y) in cheio:
            if px[x, y][:3] == hx(OUT):
                continue
            esq = (x - 1, y) in cheio and px[x - 1, y][:3] == hx(OUT) and (x - 2, y) not in cheio
            cima = (x, y - 1) in cheio and px[x, y - 1][:3] == hx(OUT) and (x, y - 2) not in cheio
            if esq:
                npx[x, y] = hx('#f57d4a') + (255,)
            elif cima and x < 18:
                npx[x, y] = hx('#fbb954') + (255,)
        quadros.append(novo)
    return quadros


# ------------------------------------------------------------------ capa ----------------------------------------------
CW, CH = 315, 250
N_CAPA = 96
CEU_CAPA = ['#323353', '#484a77', '#6b3e75', '#a24b6f', '#cf657f', '#f68181', '#fca790', '#fbb954']
TX = 188            # meio da Torre
BASE = 203          # o chão da praça (os pés da Torre)
HORIZONTE = 200


def meia_torre(y):
    return 19 + (y / BASE) * 10


def nuvens_mascara(periodo, altura, n, semente, rmin, rmax, esticar=1.7):
    """Máscara de nuvens que se repete na horizontal a cada 'periodo' píxeis: {(x, y): fração da altura}."""
    r = random.Random(semente)
    bolas = []
    for i in range(n):
        cx = (i + r.random() * 0.6) * periodo / n
        bolas.append((cx, r.uniform(altura * 0.4, altura * 0.6), r.uniform(rmin, rmax)))
        for k in range(4):
            bolas.append((cx + r.uniform(-rmax, rmax) * 1.4, r.uniform(altura * 0.6, altura * 0.85), r.uniform(rmin * 0.5, rmax * 0.65)))
    m = {}
    for y in range(altura):
        for x in range(periodo):
            for (bx, by, br) in bolas:
                dx = abs(x - bx) % periodo
                dx = min(dx, periodo - dx)
                if (dx / esticar) ** 2 + (y - by) ** 2 <= br * br and y <= altura - 2:
                    m[(x, y)] = True
                    break
    return m


_NUV = {}


def desenhar_nuvens(t, mascara, periodo, altura, y0, desvio, cores, so_x=None):
    """Nuvens iluminadas por baixo (pelo sol): em cima escuras, em baixo a orla quente."""
    topo_c, meio_c, baixo_c, orla_c = cores
    for (x, y) in mascara:
        pass
    for sx in range(t.w):
        if so_x and not so_x(sx):
            continue
        mx = (sx + desvio) % periodo
        for y in range(altura):
            if (mx, y) not in mascara:
                continue
            em_baixo = (mx, y + 1) not in mascara
            em_baixo2 = (mx, y + 2) not in mascara
            em_cima = (mx, y - 1) not in mascara
            c = meio_c
            if em_baixo:
                c = orla_c
            elif em_baixo2:
                c = baixo_c
            elif em_cima or (mx, y - 2) not in mascara:
                c = topo_c
            t.p(sx, y0 + y, c)


def capa_quadro(f, logo, heroi, gente):
    t = Tela(CW, CH)
    rnd = random.Random(11)
    # céu do pôr do sol
    faixas(t, 0, HORIZONTE, CEU_CAPA, xadrez=2)
    # estrelas lá em cima (piscam)
    for i in range(40):
        x, y = rnd.randrange(CW), rnd.randrange(52)
        fase = (f // 4 + i * 3) % 8
        if fase == 0:
            continue
        t.p(x, y, '#ffffff' if fase in (3, 4) and i % 3 == 0 else '#c7dcd0' if y < 30 else '#eaaded')
    # o sol a pôr-se (com riscas, ao estilo das capas antigas)
    sx, sy, sr = 112, 186, 24
    for y in range(sy - sr, sy + sr + 1):
        for x in range(sx - sr, sx + sr + 1):
            d = math.hypot(x - sx, y - sy)
            if d <= sr:
                risca = y > sy - 8 and (y - sy) % 5 == 0 and y < HORIZONTE
                if risca:
                    continue
                t.p(x, y, '#fbff86' if d < sr - 4 else ('#f9c22b' if d < sr - 1 else '#f79617'))
    # nuvens longe (finas, 1 px por quadro, repetem-se a cada 96)
    if 'longe' not in _NUV:
        _NUV['longe'] = nuvens_mascara(96, 14, 2, 5, 3, 5)
        _NUV['perto'] = nuvens_mascara(192, 34, 3, 9, 8, 12, esticar=1.35)
    desenhar_nuvens(t, _NUV['longe'], 96, 14, 124, f, ('#cf657f', '#f68181', '#fca790', '#fdcbb0'))
    # cidade ao longe (por trás da Torre), roxa da névoa, com janelas acesas
    rnd2 = random.Random(4)
    x = 80
    while x < CW:
        w = rnd2.randint(8, 16)
        h = rnd2.randint(6, 16)
        for yy in range(HORIZONTE - h, BASE + 1):
            for xx in range(x, x + w):
                t.p(xx, yy, '#753c54')
        if rnd2.random() < 0.5:   # telhado em bico
            for k in range(w // 2):
                for xx in range(x + k, x + w - k):
                    t.p(xx, HORIZONTE - h - 1 - k // 1, '#753c54')
        for k in range(2):
            if rnd2.random() < 0.6:
                t.p(x + 2 + k * (w - 5), HORIZONTE - h + 3, '#fbb954')
        x += w + rnd2.randint(0, 3)
    # a Torre
    torre(t, f)
    # nuvens perto (passam à frente do cimo da Torre: a Torre perde-se nelas)
    desenhar_nuvens(t, _NUV['perto'], 192, 34, 46, f * 2, ('#753c54', '#a24b6f', '#cf657f', '#f68181'))
    # casas da praça, à esquerda e à direita
    casas(t, f)
    # chão da praça (calçada em perspetiva)
    calcada(t)
    # candeeiros
    for (lx, ly) in ((90, 232), (250, 232)):
        candeeiro(t, lx, ly, f)
    # gente na praça (o Brom e o Kai a conversar à esquerda, a guarda Sami à direita), também em contraluz
    for (q, gx, gy) in gente:
        sombra_heroi(t, gx + 16, gy)
        t.colar(q[(f // 6 + gx) % len(q)], gx, gy - 31)
    # o herói, de costas, com a sombra comprida para a frente (o sol está atrás da Torre)
    hx0, hy0 = 140, 241
    sombra_heroi(t, hx0 + 16, hy0)
    t.colar(heroi[(f // 6) % len(heroi)], hx0, hy0 - 31)
    # o logótipo, com sombra
    lq = logo[(f - 48) if 48 <= f < 56 else 0]
    lx, ly = (CW - lq.width) // 2, 10
    sombra = Image.new('RGBA', lq.size)
    sp, lp = sombra.load(), lq.load()
    for yy in range(lq.height):
        for xx in range(lq.width):
            if lp[xx, yy][3] > 128:
                sp[xx, yy] = hx(OUT) + (255,)
    t.colar(sombra, lx + 1, ly + 2)
    t.colar(lq, lx, ly)
    return t.im


def torre(t, f):
    rnd = random.Random(2)
    for y in range(0, BASE):
        mw = meia_torre(y)
        x0, x1 = int(round(TX - mw)), int(round(TX + mw))
        fiada = y // 5
        for x in range(x0, x1 + 1):
            u = (x - x0) / max(1, x1 - x0)
            if x in (x0, x1):
                c = OUT
            elif u < 0.05:
                c = '#fbb954'           # a orla do sol (o sol está à esquerda, atrás)
            elif u < 0.13:
                c = '#cd683d'
            elif u < 0.38:
                c = '#694f62'
            elif u < 0.85:
                c = '#45293f'
            else:
                c = '#3e3546' if u < 0.93 else OUT
            junta = y % 5 == 0 or ((x - x0 + fiada * 4) % 9 == 0 and 0.1 < u < 0.9)
            if junta and c not in (OUT,):
                c = {'#fbb954': '#f57d4a', '#cd683d': '#9e4539', '#694f62': '#45293f', '#45293f': '#3e3546',
                     '#3e3546': '#2e222f'}[c] if y % 5 == 0 else ({'#694f62': '#45293f', '#45293f': '#3e3546'}.get(c, c))
            t.p(x, y, c)
    # anéis de pedra entre os andares
    for ry in (36, 82, 128, 172):
        mw = meia_torre(ry) + 3
        x0, x1 = int(TX - mw), int(TX + mw)
        for x in range(x0, x1 + 1):
            u = (x - x0) / max(1, x1 - x0)
            t.p(x, ry, '#fbb954' if u < 0.12 else ('#966c6c' if u < 0.4 else '#694f62'))
            t.p(x, ry + 1, '#45293f' if u < 0.6 else '#3e3546')
            t.p(x, ry + 2, OUT)
        t.p(x0, ry, OUT)
        t.p(x1, ry, OUT)
        t.p(x0, ry + 1, OUT)
        t.p(x1, ry + 1, OUT)
    # janelas (umas acesas, uma pisca)
    k = 0
    for wy in range(14, BASE - 30, 15):
        if any(abs(wy - ry) < 5 for ry in (36, 82, 128, 172)):
            continue
        mw = meia_torre(wy)
        for j, uu in enumerate((-0.45, 0.05, 0.5)):
            if (k + j) % 4 == 3:
                continue
            wx = int(TX + uu * mw)
            acesa = (k * 3 + j) % 5 != 0
            if k == 4 and j == 1:   # a janela que pisca
                acesa = (f // 8) % 2 == 0
            luz = '#fbff86' if acesa and (k + j) % 3 == 0 else ('#f9c22b' if acesa else '#2e222f')
            t.ret(wx, wy, wx + 2, wy + 4, OUT)
            t.ret(wx + 1, wy + 1, wx + 1, wy + 4, luz)
            t.p(wx + 1, wy + 1, '#f79617' if acesa else OUT)
        k += 1
    # o degrau da base
    for y in range(BASE - 6, BASE + 1):
        mw = meia_torre(BASE) + 4 + (2 if y >= BASE - 2 else 0)
        x0, x1 = int(TX - mw), int(TX + mw)
        for x in range(x0, x1 + 1):
            u = (x - x0) / max(1, x1 - x0)
            c = OUT if x in (x0, x1) else ('#fbb954' if u < 0.08 else ('#7f708a' if y in (BASE - 6, BASE - 2) else '#3e3546'))
            if y in (BASE - 3, BASE):
                c = OUT if y == BASE else '#2e222f'
            t.p(x, y, c)
    # a porta em arco e o Cristal Mestre a brilhar
    pw, ph = 8, 22
    topo = BASE - 6 - ph
    for y in range(topo, BASE - 6):
        for x in range(TX - pw, TX + pw + 1):
            dentro = (x - TX) ** 2 / (pw * pw) + max(0, (topo + pw - y)) ** 2 / (pw * pw) <= 1.0
            if dentro:
                borda = (x - TX) ** 2 / ((pw - 1.5) ** 2) + max(0, (topo + pw - y)) ** 2 / ((pw - 1.5) ** 2) > 1.0
                t.p(x, y, OUT if borda else '#45293f')
    brilho = ['#4d65b4', '#4d9be6', '#8fd3ff', '#4d9be6'][(f // 6) % 4]
    for i, y in enumerate(range(BASE - 22, BASE - 6)):
        meia = min(i // 2, (16 - i) // 2, 4)
        for x in range(TX - meia, TX + meia + 1):
            c = '#ffffff' if x == TX - meia + 1 and i < 9 else (brilho if x < TX + meia else '#4d65b4')
            t.p(x, y, c)
    # o brilho do cristal no chão
    for x in range(TX - 10, TX + 11):
        if (x + f // 6) % 2 == 0:
            t.p(x, BASE + 1, '#4d65b4')


def casas(t, f):
    """Casas da praça: em contraluz (fachadas na sombra), telhados vermelho-escuros com a orla do sol, janelas
    acesas e chaminés."""
    lista = [(-6, 150, 34, 'b'), (22, 162, 30, 'a'), (48, 172, 26, 'b'), (70, 182, 20, 'a'),
             (232, 178, 22, 'a'), (250, 164, 30, 'b'), (276, 150, 44, 'a')]
    for (x0, topo, w, tipo) in lista:
        tecto = w // 2 + 2 if tipo == 'a' else w // 3 + 3
        # paredes
        for y in range(topo, BASE + 3):
            for x in range(x0, x0 + w):
                c = '#3e3546' if x - x0 > 2 else '#694f62'
                if x in (x0, x0 + w - 1):
                    c = OUT
                if (y - topo) % 6 == 5 and x - x0 > 2:
                    c = '#45293f'   # vigas de madeira
                t.p(x, y, c)
        # telhado
        for k in range(tecto):
            y = topo - tecto + k
            meia = (k + 1) * (w / 2 + 2) / tecto
            cx = x0 + w / 2
            for x in range(int(cx - meia), int(cx + meia) + 1):
                borda = x in (int(cx - meia), int(cx + meia))
                c = OUT if borda else ('#6e2727' if x > cx - 1 else '#b33831')
                if not borda and x <= cx and (int(cx - meia) + 1 >= x or k == 0):
                    c = '#f57d4a'     # a orla do sol no telhado
                if not borda and (k % 3 == 2) and x > cx - 1:
                    c = '#45293f'
                t.p(x, y, c)
        for x in range(x0 - 2, x0 + w + 2):
            t.p(x, topo, OUT)
            t.p(x, topo + 1, '#45293f')
        # chaminé
        chx = x0 + (w * 2) // 3
        t.ret(chx, topo - tecto + 1, chx + 3, topo - tecto // 2, OUT)
        t.ret(chx + 1, topo - tecto + 2, chx + 2, topo - tecto // 2, '#6e2727')
        t.p(chx + 1, topo - tecto + 2, '#f57d4a')
        # fumo a subir (3 bolinhas que sobem e voltam)
        for i in range(3):
            fy = (f // 2 + i * 6) % 18
            fx = chx + 1 + fy // 5
            c = '#966c6c' if fy < 9 else '#753c54'
            t.p(fx, topo - tecto - fy, c)
            t.p(fx + 1, topo - tecto - fy, c)
        # janelas acesas
        # porta
        dx = x0 + w // 2 - 2 if w > 24 else x0 + 3
        if 0 <= dx < CW - 5:
            t.ret(dx, BASE - 7, dx + 4, BASE + 1, OUT)
            t.ret(dx + 1, BASE - 6, dx + 3, BASE + 1, '#45293f')
            t.p(dx + 3, BASE - 3, '#f9c22b')
        for jx in ([x0 + 4, x0 + w - 9] if w > 24 else [x0 + w - 9]):
            for jy in range(topo + 5, BASE - 12, 16):
                acesa = (jx + jy) % 3 != 0
                t.ret(jx, jy, jx + 4, jy + 5, OUT)
                t.ret(jx + 1, jy + 1, jx + 3, jy + 4, '#f9c22b' if acesa else '#45293f')
                if acesa:
                    t.ret(jx + 1, jy + 1, jx + 3, jy + 1, '#fbff86')
                    t.p(jx + 2, jy + 2, '#f79617')
                    t.p(jx + 2, jy + 3, '#f79617')


def calcada(t):
    """A calçada da praça em perspetiva: pedras pequenas lá ao fundo e maiores cá à frente, de cantos redondos,
    com o reflexo quente do pôr do sol (mais forte na direção do sol)."""
    r = random.Random(8)
    y = BASE + 2
    alturas = [2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7]
    fila = 0
    for x in range(CW):
        t.p(x, BASE + 1, '#3e3546')
    while y < CH:
        h = alturas[min(fila, len(alturas) - 1)]
        x = -r.randint(0, h * 3)
        while x < CW:
            w = max(3, int(h * r.uniform(1.8, 3.2)))
            for yy in range(y, min(CH, y + h)):
                for xx in range(x, x + w):
                    if not 0 <= xx < CW:
                        continue
                    a, b = xx - x, yy - y
                    canto = (a in (0, w - 1)) and (b in (0, h - 1)) and h > 2
                    if xx == x + w - 1 or yy == y + h - 1 and h <= 2:
                        c = '#3e3546'
                    elif canto:
                        c = '#3e3546'
                    elif b == 0 or (a == 0 and h > 2):
                        c = '#966c6c'
                        perto = abs(xx - 112) < 26 + fila * 6
                        if perto and fila < 8:
                            c = '#cd683d' if fila < 5 else '#966c6c'
                    elif b == h - 1:
                        c = '#45293f'
                    else:
                        c = '#694f62'
                    t.p(xx, yy, c)
            x += w
        y += h
        fila += 1


ESCURECER = {'#966c6c': '#694f62', '#cd683d': '#9e4539', '#3e3546': '#2e222f', '#694f62': '#45293f',
             '#45293f': '#3e3546'}


def sombra_heroi(t, px, py):
    """Sombra comprida do herói, para a frente e um pouco à direita (o sol está atrás, à esquerda)."""
    inv = {hx(k): v for k, v in ESCURECER.items()}
    for i in range(26):
        y = py + i // 2
        cx = px + i * 0.55
        meia = 4 - i / 10
        for x in range(int(cx - meia), int(cx + meia) + 1):
            c = t.get(x, y) if 0 <= x < CW and 0 <= y < CH else None
            if c in inv:
                t.p(x, y, inv[c])


def candeeiro(t, x, y, f):
    t.ret(x, y - 26, x, y, OUT)
    t.ret(x - 1, y - 1, x + 1, y, OUT)
    t.ret(x - 2, y - 32, x + 2, y - 26, OUT)
    luz = ['#f9c22b', '#fbff86', '#f9c22b', '#f79617'][(f // 3 + x) % 4]
    t.ret(x - 1, y - 31, x + 1, y - 27, luz)
    t.p(x, y - 33, OUT)
    # o halo da luz (píxeis soltos à volta)
    for a in range(0, 360, 30):
        r = 5 + ((f // 3) % 2)
        t.p(x + round(math.cos(math.radians(a)) * r), y - 29 + round(math.sin(math.radians(a)) * r), '#f79617')


def fazer_capa():
    logo = logo_quadros()
    heroi = heroi_costas()
    gente = [(heroi_costas('npcs/brom_parado_lado.png'), 22, 234), (heroi_costas('npcs/kai_parado_lado.png', True), 44, 236),
             (heroi_costas('npcs/guarda_sami_parado_baixo.png'), 268, 238)]
    quadros = [capa_quadro(f, logo, heroi, gente) for f in range(N_CAPA)]
    verificar_paleta(quadros[0], 'capa')
    ampliar(quadros[0], 2).save(os.path.join(PASTA, 'capa.png'))
    guardar_gif([ampliar(q, 2) for q in quadros], os.path.join(PASTA, 'capa.gif'), 100)
    print('capa: 630×500 + capa.gif (%d quadros)' % len(quadros))


# ------------------------------------------------------------------ banner --------------------------------------------
BW, BH = 480, 150
# (nome, escuro, médio, claro, destaque) — cores de docs/regioes/rNN_*.md ("Cores principais")
REGIOES = [
    ('floresta', '#165a4c', '#239063', '#1ebc73', '#91db69'),
    ('cavernas', '#2e222f', '#3e3546', '#625565', '#30e1b9'),
    ('pantano', '#374e4a', '#165a4c', '#676633', '#d5e04b'),
    ('deserto', '#9e4539', '#cd683d', '#e6904e', '#fbb954'),
    ('gelo', '#484a77', '#4d65b4', '#8fd3ff', '#ffffff'),
    ('oceano', '#0b5e65', '#0b8a8f', '#0eaf9b', '#8ff8e2'),
    ('vulcao', '#2e222f', '#6e2727', '#b33831', '#f9c22b'),
    ('assombrado', '#45293f', '#6b3e75', '#905ea9', '#8ff8e2'),
    ('ceu', '#4d65b4', '#4d9be6', '#8fd3ff', '#ffffff'),
    ('abismo', '#2e222f', '#45293f', '#6b3e75', '#fbff86'),
]
FX = 15   # altura de cada faixa


def banner_quadro(f, logo):
    t = Tela(BW, BH)
    rnd = random.Random(3)
    for i, (nome, esc, med, cla, des) in enumerate(REGIOES):
        y1 = BH - 1 - i * FX
        y0 = y1 - FX + 1
        # fundo da faixa: escuro, com a passagem em xadrez para a faixa de cima
        prox = REGIOES[i + 1][1] if i + 1 < len(REGIOES) else esc
        for y in range(y0, y1 + 1):
            for x in range(BW):
                c = esc
                if y == y0 and (x + y) % 2 == 0:
                    c = prox
                t.p(x, y, c)
        paisagem(t, nome, y0, y1, esc, med, cla, des, f, rnd)
    banner_torre(t, f)
    # o logótipo numa janela do Sistema, à esquerda da Torre
    lq = logo[f % len(logo)]
    jw, jh = lq.width + 16, lq.height + 12
    jx, jy = (BW // 2 - 26 - jw) // 2 + 6, (BH - jh) // 2
    janela_sistema(t, jx, jy, jw, jh)
    t.colar(lq, jx + 7, jy + 5)
    return t.im


def paisagem(t, nome, y0, y1, esc, med, cla, des, f, rnd):
    """A paisagem de cada região numa faixa de 10 px (só dos lados: o meio é da Torre)."""
    W = BW
    if nome == 'floresta':     # pinheiros
        for x in range(0, W, 8):
            h = 8 + (x * 7) % 5
            for k in range(h):
                for xx in range(x - k // 2, x + k // 2 + 1):
                    t.p(xx, y1 - h + k + 1, med if xx < x else esc if k == h - 1 else '#1ebc73' if xx == x else med)
            t.p(x, y1 - h, cla)
    elif nome == 'cavernas':   # estalactites e cristais
        for x in range(2, W, 6):
            h = 4 + (x * 5) % 7
            for k in range(h):
                t.p(x, y0 + 1 + k, med)
                if k < h - 2:
                    t.p(x + 1, y0 + 1 + k, cla if k == 0 else med)
        for x in range(5, W, 17):
            t.p(x, y1 - 1, des)
            t.p(x, y1 - 2, '#a884f3' if x % 2 else des)
            t.p(x + 1, y1 - 1, '#4d9be6')
    elif nome == 'pantano':    # canas e água parada
        for x in range(W):
            if (x + f) % 9 < 6:
                t.p(x, y1, '#374e4a' if x % 3 else '#547e64')
        for x in range(1, W, 4):
            h = 4 + (x * 3) % 7
            for k in range(h):
                t.p(x, y1 - 1 - k, cla if k < h - 1 else '#4c3e24')
            if x % 12 == 1:
                t.p(x, y1 - h, '#c32454')
        for x in range(7, W, 23):
            t.p(x, y1 - 7 + (f // 2 + x) % 2, des)      # pirilampos
    elif nome == 'deserto':    # dunas
        for x in range(W):
            h = int(5.5 + 3.5 * math.sin(x / 11.0) + 1.5 * math.sin(x / 4.3))
            for y in range(y1 - h, y1 + 1):
                t.p(x, y, cla if y == y1 - h else med)
            if x % 31 == 0:   # um cacto
                t.ret(x, y1 - h - 4, x, y1 - h, '#239063')
                t.p(x - 1, y1 - h - 2, '#239063')
    elif nome == 'gelo':       # picos de neve
        for x0 in range(-4, W, 17):
            h = 10 + (x0 * 3) % 4
            for k in range(h):
                for xx in range(x0 - k, x0 + k + 1):
                    c = cla if k < 3 else (med if xx < x0 else esc)
                    if k < 2:
                        c = des
                    t.p(xx, y1 - h + k + 1, c)
        for x in range(3, W, 11):   # neve a cair
            t.p(x, y0 + (f + x) % 9, des)
    elif nome == 'oceano':     # ondas
        for x in range(W):
            o = int(1.5 * math.sin((x + f * 2) / 4.0))
            for y in range(y1 - 4 + o, y1 + 1):
                t.p(x, y, med if y > y1 - 3 + o else cla)
            if (x + f * 2) % 8 == 0:
                t.p(x, y1 - 5 + o, des)
    elif nome == 'vulcao':     # vulcões com lava
        for x0 in range(6, W, 30):
            h = 11
            for k in range(h):
                for xx in range(x0 - k - 2, x0 + k + 3):
                    t.p(xx, y1 - h + k + 1, med if xx < x0 else '#45293f')
            t.ret(x0 - 1, y1 - h + 1, x0 + 1, y1 - h + 1, des)
            for k in range(1, 9):
                t.p(x0 + (k % 2), y1 - h + 1 + k, '#ea4f36' if k < 5 else '#b33831')
            t.p(x0, y1 - h - 1 - (f % 3), '#fb6b1d')
    elif nome == 'assombrado':   # lápides e torres de castelo
        for x0 in range(3, W, 15):
            if x0 % 2:
                t.ret(x0, y1 - 11, x0 + 4, y1, med)
                t.ret(x0, y1 - 12, x0 + 4, y1 - 12, cla)
                for k in range(3):
                    t.p(x0 + 1 + k % 3, y1 - 13 - (k == 1), cla)
                t.ret(x0 + 2, y1 - 8, x0 + 2, y1 - 7, des if (f // 2 + x0) % 3 else med)
            else:
                t.ret(x0, y1 - 4, x0 + 3, y1, med)
                t.ret(x0 + 1, y1 - 5, x0 + 2, y1 - 5, med)
                t.p(x0 + 1, y1 - 3, cla)
        for x in range(9, W, 37):
            gy = y0 + 2 + (f // 2 + x) % 3
            t.p(x, gy, des)
            t.p(x + 1, gy, des)
            t.p(x, gy + 1, des)
    elif nome == 'ceu':        # nuvens a passar
        for x0 in range(0, W + 40, 34):
            cx = (x0 + f) % (W + 40) - 20
            for xx in range(cx - 8, cx + 9):
                hh = 5 if abs(xx - cx) < 5 else 3
                for y in range(y1 - hh - 1, y1):
                    t.p(xx, y, des if y == y1 - hh - 1 else cla)
            for xx in range(cx - 3, cx + 4):
                t.p(xx, y1 - 7, des)
        for x in range(13, W, 41):
            t.p(x, y0 + 2, '#f9c22b')
    elif nome == 'abismo':     # estrelas e falhas
        for i in range(110):
            x, y = (i * 53) % W, y0 + (i * 7) % FX
            fase = (f + i) % 4
            if fase:
                t.p(x, y, des if fase == 1 else ('#a884f3' if i % 2 else '#8fd3ff'))
        for x in range((f * 37) % W, (f * 37) % W + 9):
            t.p(x, y0 + 4, '#a884f3')


def banner_torre(t, f):
    """A Torre a subir pelo meio: a pedra muda com a luz de cada região (orla e janelas)."""
    tx = BW // 2
    for y in range(BH):
        i = min(len(REGIOES) - 1, (BH - 1 - y) // FX)
        nome, esc, med, cla, des = REGIOES[i]
        mw = 19 + (y / BH) * 6
        x0, x1 = int(tx - mw), int(tx + mw)
        for x in range(x0, x1 + 1):
            u = (x - x0) / max(1, x1 - x0)
            if x in (x0, x1):
                c = OUT
            elif u < 0.1:
                c = cla                  # a luz da região na orla
            elif u < 0.35:
                c = '#9babb2'
            elif u < 0.75:
                c = '#7f708a'
            else:
                c = '#625565'
            if y % 4 == 0 and x not in (x0, x1):
                c = {'#9babb2': '#7f708a', '#7f708a': '#625565', '#625565': '#3e3546'}.get(c, med)
            elif (x - x0 + (y // 4) * 3) % 7 == 0 and 0.1 < u < 0.9:
                c = {'#9babb2': '#7f708a', '#7f708a': '#625565', '#625565': '#3e3546'}[c]
            t.p(x, y, c)
    # anéis entre regiões, com a "cobertura" de cada uma (musgo, neve, areia, lava...)
    for i, (nome, esc, med, cla, des) in enumerate(REGIOES):
        ry = BH - 1 - (i + 1) * FX + 1
        mw = 19 + (ry / BH) * 6 + 2
        x0, x1 = int(tx - mw), int(tx + mw)
        for x in range(x0, x1 + 1):
            t.p(x, ry, OUT if x in (x0, x1) else (des if (x + i) % 3 else cla))
            t.p(x, ry + 1, OUT)
        # janelas da região (acesas com a cor dela)
        for k, dx in enumerate((-11, -1, 9)):
            wy = ry + 5 + (k % 2) * 2
            if wy + 3 >= BH:
                continue
            luz = des if (f + k + i) % 6 else cla
            t.ret(tx + dx, wy, tx + dx + 2, wy + 4, OUT)
            t.ret(tx + dx + 1, wy + 1, tx + dx + 1, wy + 3, luz)


def janela_sistema(t, x, y, w, h):
    """Janela azul do Sistema (como arte/ui/janela_sistema.png): fundo escuro com linhas, moldura e cantos."""
    for yy in range(y, y + h):
        for xx in range(x, x + w):
            borda = xx in (x, x + w - 1) or yy in (y, y + h - 1)
            dentro = xx in (x + 1, x + w - 2) or yy in (y + 1, y + h - 2)
            canto = (xx in (x, x + w - 1)) and (yy in (y, y + h - 1))
            if canto:
                continue
            if borda:
                c = '#4d9be6'
            elif dentro:
                c = '#8fd3ff' if yy == y + 1 else '#4d65b4'
            else:
                c = '#2e222f' if (yy - y) % 3 == 0 else '#323353'
            t.p(xx, yy, c)
    for (cx, cy, dx, dy) in ((x + 1, y + 1, 1, 1), (x + w - 2, y + 1, -1, 1), (x + 1, y + h - 2, 1, -1),
                             (x + w - 2, y + h - 2, -1, -1)):
        for k in range(3):
            t.p(cx + dx * k, cy, '#8fd3ff')
            t.p(cx, cy + dy * k, '#8fd3ff')


def fazer_banner():
    logo = logo_quadros()
    quadros = [banner_quadro(f, logo) for f in range(8)]
    verificar_paleta(quadros[0], 'banner')
    ampliar(quadros[0], 2).save(os.path.join(PASTA, 'banner.png'))
    guardar_gif([ampliar(q, 2) for q in quadros], os.path.join(PASTA, 'banner.gif'), 140)
    print('banner: 960×300 + banner.gif')


# ------------------------------------------------------------------ ícone ---------------------------------------------
def icone(fundo=True):
    """64×64: a janela do Sistema com uma torre pequenina dentro (em cima de uma colina, com nuvens e estrelas)."""
    t = Tela(64, 64, OUT)
    x0, y0, x1, y1 = 4, 4, 59, 59
    # janela: fundo, linhas de ecrã, moldura com brilho em cima, cantos
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            canto = (x in (x0, x1) and y in (y0, y0 + 1, y1 - 1, y1)) or (y in (y0, y1) and x in (x0 + 1, x1 - 1))
            if canto:
                continue
            borda = x in (x0, x1) or y in (y0, y1)
            dentro = x in (x0 + 1, x1 - 1) or y in (y0 + 1, y1 - 1)
            if borda:
                c = '#4d9be6'
            elif dentro:
                c = '#8fd3ff' if y == y0 + 1 else '#4d65b4'
            else:
                u = (y - y0) / (y1 - y0)
                c = '#323353' if u < 0.55 else ('#484a77' if u < 0.8 else '#4d65b4')
                if u > 0.5 and u < 0.58 and (x + y) % 2 == 0:
                    c = '#484a77'
                if u > 0.76 and u < 0.82 and (x + y) % 2 == 0:
                    c = '#4d65b4'
                if (y - y0) % 4 == 0 and u < 0.5 and x % 2 == 0:
                    c = '#2e222f'
            t.p(x, y, c)
    # barra de título com 3 bolinhas
    t.ret(x0 + 2, y0 + 2, x1 - 2, y0 + 6, '#4d65b4')
    t.ret(x0 + 2, y0 + 7, x1 - 2, y0 + 7, '#4d9be6')
    for k, c in enumerate(('#8fd3ff', '#8fd3ff', '#f9c22b')):
        t.ret(x1 - 13 + k * 4, y0 + 3, x1 - 12 + k * 4, y0 + 4, c)
    t.ret(x0 + 4, y0 + 4, x0 + 16, y0 + 4, '#8fd3ff')
    # estrelas
    for (sx, sy, c) in ((12, 17, '#ffffff'), (49, 15, '#8fd3ff'), (16, 30, '#8fd3ff'), (51, 28, '#ffffff'),
                        (9, 24, '#4d9be6'), (44, 20, '#4d9be6'), (54, 36, '#8fd3ff')):
        t.p(sx, sy, c)
    for (sx, sy) in ((12, 17), (51, 28)):
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            t.p(sx + dx, sy + dy, '#4d9be6')
    # colina
    for x in range(x0 + 2, x1 - 1):
        h = int(7 - ((x - 32) / 13.0) ** 2 * 2.2)
        h = max(2, h)
        for y in range(y1 - 1 - h, y1 - 1):
            c = '#1ebc73' if y == y1 - 1 - h else '#239063'
            if y > y1 - 1 - h + 2:
                c = '#165a4c'
            if y == y1 - 1 - h and x < 26:
                c = '#91db69'
            t.p(x, y, c)
    # a torre
    cx, base, topo = 32, 52, 16
    for y in range(topo, base + 1):
        mw = 4 + (y - topo) / (base - topo) * 3
        a, b = int(round(cx - mw)), int(round(cx + mw))
        for x in range(a, b + 1):
            u = (x - a) / max(1, b - a)
            c = OUT if x in (a, b) else ('#c7dcd0' if u < 0.22 else ('#9babb2' if u < 0.5 else ('#7f708a' if u < 0.8 else '#625565')))
            if y % 4 == 0 and x not in (a, b):
                c = {'#c7dcd0': '#9babb2', '#9babb2': '#7f708a', '#7f708a': '#625565', '#625565': '#3e3546'}[c]
            t.p(x, y, c)
    for ry in (26, 38):   # anéis
        mw = 4 + (ry - topo) / (base - topo) * 3 + 1
        for x in range(int(cx - mw), int(cx + mw) + 1):
            t.p(x, ry, OUT if x in (int(cx - mw), int(cx + mw)) else ('#ffffff' if x < cx - 1 else '#c7dcd0'))
            t.p(x, ry + 1, OUT)
    # telhado em bico, com a ponta dourada
    for k in range(8):
        y = topo - 1 - k
        mw = 5 - k * 0.65
        a, b = int(round(cx - mw)), int(round(cx + mw))
        for x in range(a, b + 1):
            t.p(x, y, OUT if x in (a, b) or k == 0 else ('#ea4f36' if x < cx else '#b33831'))
    t.p(cx, topo - 9, '#f9c22b')
    t.p(cx, topo - 10, '#fbff86')
    t.p(cx - 1, topo - 9, OUT)
    t.p(cx + 1, topo - 9, OUT)
    # janelas
    for (wx, wy, c) in ((30, 20, '#fbff86'), (33, 30, '#f9c22b'), (30, 42, '#f9c22b'), (34, 44, '#f79617')):
        t.ret(wx - 1, wy - 1, wx + 1, wy + 2, OUT)
        t.ret(wx, wy, wx, wy + 1, c)
    # a porta com o Cristal Mestre
    t.ret(30, 47, 34, base, OUT)
    t.ret(31, 48, 33, base, '#45293f')
    t.p(32, 49, '#8fd3ff')
    t.p(32, 50, '#4d9be6')
    t.p(31, 50, '#4d9be6')
    t.p(33, 50, '#4d65b4')
    t.p(32, 51, '#4d65b4')
    # duas nuvenzinhas ao lado da torre
    for (nx, ny) in ((15, 38), (46, 25)):
        for (dx, dy, c) in ((0, 0, '#c7dcd0'), (1, 0, '#c7dcd0'), (2, 0, '#c7dcd0'), (3, 0, '#c7dcd0'), (4, 0, '#9babb2'),
                            (1, -1, '#ffffff'), (2, -1, '#ffffff'), (3, -1, '#c7dcd0'), (2, -2, '#ffffff'), (-1, 0, '#9babb2'),
                            (5, 0, '#9babb2')):
            t.p(nx + dx, ny + dy, c)
    im = t.im.convert('RGBA')
    if not fundo:   # fora da janela fica transparente (para o ícone adaptativo do Android)
        px = im.load()
        for y in range(64):
            for x in range(64):
                if not (x0 <= x <= x1 and y0 <= y <= y1) or px[x, y][:3] == hx(OUT) and (x < x0 + 1 or x > x1 - 1 or y < y0 + 1 or y > y1 - 1):
                    px[x, y] = (0, 0, 0, 0)
    return im


def fazer_icone():
    im = icone()
    verificar_paleta(im, 'icone')
    ampliar(im, 8).save(os.path.join(PASTA, 'icone.png'))
    ui = os.path.join(ARTE, 'ui')
    ampliar(im, 4).save(os.path.join(ui, 'icone_jogo.png'))                     # 256: projeto (janela, Web)
    ampliar(im, 3).save(os.path.join(ui, 'icone_android_192.png'))              # 192: Android (normal)
    frente = Image.new('RGBA', (432, 432))                                      # adaptativo: dentro da zona segura
    frente.alpha_composite(ampliar(icone(fundo=False), 4), (88, 88))
    frente.save(os.path.join(ui, 'icone_android_frente.png'))
    Image.new('RGBA', (432, 432), hx(OUT) + (255,)).save(os.path.join(ui, 'icone_android_fundo.png'))
    tamanhos = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    ampliar(im, 4).save(os.path.join(ui, 'icone_jogo.ico'), sizes=tamanhos)    # Windows
    print('icone: 512×512 + arte/ui/icone_jogo.png/.ico + icone_android_*.png')


# ------------------------------------------------------------------ GIF e capturas do jogo ------------------------------
def numeradas(pasta):
    fs = [f for f in os.listdir(pasta) if re.match(r'captura_\d+\.png$', f)]
    return [os.path.join(pasta, f) for f in sorted(fs, key=lambda f: int(re.findall(r'\d+', f)[0]))]


def fazer_gif(pasta, primeira, n=120):
    """GIF 640×360 de 6 s (120 quadros a 50 ms) a partir das capturas 1280×720 do robô (zoom 4): metade do tamanho
    sem desfocar (cada píxel da arte, 4×4 no ecrã, fica 2×2). Paleta comum a todos os quadros."""
    fs = numeradas(pasta)[primeira:primeira + n]
    quadros = [Image.open(f).convert('RGB') for f in fs]
    quadros = [q.resize((q.width // 2, q.height // 2), Image.NEAREST) for q in quadros]
    amostra = Image.new('RGB', (640, 360 * 6))
    for i, k in enumerate(range(0, len(quadros), max(1, len(quadros) // 6))[:6]):
        amostra.paste(quadros[k], (0, i * 360))
    pal = amostra.quantize(colors=128, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    q = [f.quantize(palette=pal, dither=Image.Dither.NONE) for f in quadros]
    destino = os.path.join(PASTA, 'esquiva_golpe.gif')
    q[0].save(destino, save_all=True, append_images=q[1:], duration=50, loop=0, optimize=True)
    print('gif: %s (%d quadros, %.1f s, %d KB)' % (destino, len(q), len(q) * 0.05, os.path.getsize(destino) // 1024))


def fazer_capturas(pares):
    for par in pares:
        nome, origem = par.split('=', 1)
        im = Image.open(origem).convert('RGB')
        assert im.size == (1920, 1080), (origem, im.size)
        im.save(os.path.join(PASTA, 'captura_%s.png' % nome), optimize=True)
        print('captura_%s.png' % nome)


def main():
    os.makedirs(PASTA, exist_ok=True)
    open(os.path.join(PASTA, '.gdignore'), 'a').close()
    o = sys.argv[1] if len(sys.argv) > 1 else 'tudo'
    if o in ('capa', 'tudo'):
        fazer_capa()
    if o in ('banner', 'tudo'):
        fazer_banner()
    if o in ('icone', 'tudo'):
        fazer_icone()
    if o == 'gif':
        fazer_gif(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]) if len(sys.argv) > 4 else 120)
    if o == 'capturas':
        fazer_capturas(sys.argv[2:])


if __name__ == '__main__':
    main()
