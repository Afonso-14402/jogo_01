"""O fundo do menu inicial em pixel art 2D (docs/INTERFACE.md, secção 6: "a torre à noite com nuvens a passar"):
o céu da noite com estrelas, a lua, a Torre a subir até se perder nas nuvens (pedra, janelas acesas, anéis de
pedra), Ascendia em baixo (telhados e janelas acesas) e o brilho do Cristal Mestre à porta.

Animado: 4 quadros (as estrelas piscam, as janelas tremeluzem, o cristal pulsa). As nuvens que passam são as do
menu (arte/ui/nuvem_*.png), por cima.

Saída: arte/ui/menu_fundo.png (tira de 4 quadros de 426×240; o jogo amplia 3× sem desfocar)
Uso:   python3 ferramentas/arte/menu_fundo.py [--previa caminho.gif]
"""
import math
import os
import random
import sys

from PIL import Image

PASTA = os.path.join(os.path.dirname(__file__), '..', '..', 'arte', 'ui')
W, H = 426, 240


def hx(c):
    return tuple(int(c[i:i + 2], 16) for i in (1, 3, 5))


CEU = [hx(c) for c in ('#2e222f', '#323353', '#484a77', '#4d65b4')]
PEDRA = [hx(c) for c in ('#2e222f', '#3e3546', '#625565', '#7f708a', '#9babb2')]
TELHA = [hx(c) for c in ('#45293f', '#6e2727', '#b33831')]
LUZ = [hx(c) for c in ('#f79617', '#f9c22b', '#fbff86')]
OUT = hx('#2e222f')


def quadro(f):
    rnd = random.Random(7)
    im = Image.new('RGB', (W, H), CEU[0])
    px = im.load()
    # céu: faixas de cor (mais claro perto do horizonte), em degraus com píxeis soltos na passagem
    for y in range(H):
        t = y / H * 3.6
        k = min(3, int(t))
        perto = t - k > 0.93 and k < 3       # as 2–3 linhas antes da faixa seguinte: xadrez (passagem suave)
        for x in range(W):
            px[x, y] = CEU[k + 1] if perto and (x + y) % 2 == 0 else CEU[k]
    # estrelas (algumas piscam de quadro para quadro)
    for i in range(140):
        x, y = rnd.randrange(W), rnd.randrange(int(H * 0.7))
        brilho = (i + f) % 5
        if brilho == 0:
            continue
        c = hx('#ffffff') if brilho > 2 else hx('#8fd3ff')
        px[x, y] = c
        if i % 17 == 0 and brilho > 2:   # estrelas grandes em cruz
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x + dx < W and 0 <= y + dy < H:
                    px[x + dx, y + dy] = hx('#8fd3ff')
    # a lua (com crateras) à esquerda
    cx, cy, r = 70, 46, 18
    for y in range(cy - r, cy + r + 1):
        for x in range(cx - r, cx + r + 1):
            d = math.hypot(x - cx, y - cy)
            if d <= r:
                c = hx('#fbff86') if d < r - 1 else hx('#f9c22b')
                if math.hypot(x - cx - 6, y - cy + 5) < 13:   # sombra (lua em quarto crescente)
                    c = hx('#c7dcd0') if d < r - 1 else hx('#9babb2')
                px[x, y] = c
    for (ox, oy, rr) in ((-6, 4, 3), (4, -6, 2), (-2, -8, 2)):
        for y in range(cy + oy - rr, cy + oy + rr + 1):
            for x in range(cx + ox - rr, cx + ox + rr + 1):
                if math.hypot(x - cx - ox, y - cy - oy) <= rr:
                    px[x, y] = hx('#c7dcd0') if px[x, y] == hx('#fbff86') else hx('#9babb2')
    # a Torre: um cilindro de pedra (luz da lua da esquerda), mais estreito lá em cima, a sumir nas nuvens
    base_y = 214
    for y in range(0, base_y):
        larg = 34 - (base_y - y) * 0.035
        x0, x1 = int(W / 2 - larg), int(W / 2 + larg)
        for x in range(x0, x1 + 1):
            u = (x - x0) / max(1, x1 - x0)          # 0 à esquerda, 1 à direita
            k = 4 if u < 0.12 else (3 if u < 0.35 else (2 if u < 0.7 else 1))
            c = PEDRA[k]
            if (y // 6) % 2 == 0 and (x + (y // 6) * 5) % 10 == 0:
                c = PEDRA[max(0, k - 1)]            # juntas dos blocos
            if y % 6 == 0:
                c = PEDRA[max(0, k - 1)]
            px[x, y] = c
        px[x0, y] = OUT
        px[x1, y] = OUT
        if y % 48 == 0 and y > 10:                  # anéis de pedra a cada "andar"
            for x in range(x0 - 3, x1 + 4):
                for dy in range(3):
                    if 0 <= y + dy < H:
                        px[x, y + dy] = PEDRA[3] if dy == 0 else (PEDRA[2] if dy == 1 else OUT)
    # nuvens lá em cima: a Torre perde-se nelas
    for i in range(9):
        ncx = W / 2 + (i - 4) * 26 + (i % 2) * 7
        ncy = 10 + (i % 3) * 7
        nr = 16 + (i % 3) * 5
        for y in range(int(ncy - nr * 0.55), int(ncy + nr * 0.55) + 1):
            for x in range(int(ncx - nr), int(ncx + nr) + 1):
                if 0 <= x < W and 0 <= y < H and ((x - ncx) / nr) ** 2 + ((y - ncy) / (nr * 0.55)) ** 2 <= 1:
                    v = (y - ncy) / (nr * 0.55)
                    u = (x - ncx) / nr
                    px[x, y] = hx('#7f708a') if v > 0.4 else (hx('#c7dcd0') if v < -0.3 and u < 0.3 else hx('#9babb2'))
    # janelas acesas (tremeluzem)
    for k, wy in enumerate(range(20, base_y - 20, 16)):
        for j in range(3):
            if (k * 3 + j) % 4 == 1:
                continue
            larg = 34 - (base_y - wy) * 0.035
            wx = int(W / 2 - larg * 0.6 + j * larg * 0.6)
            aceso = LUZ[(k + j + f) % 3] if (k * 5 + j + f) % 7 else LUZ[0]
            for y in range(wy, wy + 5):
                for x in range(wx, wx + 3):
                    px[x, y] = aceso if y > wy else hx('#45293f')
    # a porta da Torre e o Cristal Mestre
    for y in range(base_y - 22, base_y):
        for x in range(W // 2 - 8, W // 2 + 8):
            topo = base_y - 22 + int(8 - math.sqrt(max(0, 64 - (x - W / 2) ** 2)))
            if y >= topo:
                px[x, y] = hx('#45293f') if abs(x - W / 2) < 7 else OUT
    brilho = [hx('#4d9be6'), hx('#8fd3ff'), hx('#ffffff'), hx('#8fd3ff')][f]
    for y in range(base_y - 16, base_y + 2):
        meia = (y - (base_y - 16)) // 3
        for x in range(W // 2 - meia, W // 2 + meia + 1):
            px[x, y] = brilho if abs(x - W // 2) < meia else hx('#4d65b4')
    # Ascendia em baixo: telhados, paredes e janelas acesas
    rnd2 = random.Random(3)
    x = -6
    while x < W:
        w = rnd2.randint(18, 30)
        h = rnd2.randint(12, 22)
        if abs(x + w / 2 - W / 2) < 46:
            x += w + 2
            continue
        topo = H - h
        for yy in range(topo, H):
            for xx in range(x, x + w):
                if 0 <= xx < W:
                    px[xx, yy] = PEDRA[1] if xx - x > w * 0.25 else PEDRA[2]
        tecto = topo - w // 3
        for yy in range(tecto, topo):
            meia = (yy - tecto) * (w / 2) / max(1, topo - tecto)
            for xx in range(int(x + w / 2 - meia) - 1, int(x + w / 2 + meia) + 1):
                if 0 <= xx < W:
                    px[xx, yy] = TELHA[2] if xx < x + w / 2 else TELHA[1]
        for k in range(2):
            jx = x + 4 + k * (w - 11)
            jy = topo + 4
            if 0 <= jx < W - 3:
                c = LUZ[(k + x + f) % 3] if (x + k) % 3 else hx('#45293f')
                for yy in range(jy, jy + 4):
                    for xx in range(jx, jx + 3):
                        px[xx, yy] = c
        x += w + rnd2.randint(1, 5)
    # o chão (a praça) e o brilho do cristal no chão
    for yy in range(base_y, H):
        for xx in range(W // 2 - 60, W // 2 + 60):
            if px[xx, yy] in (CEU[3], CEU[2]):
                px[xx, yy] = PEDRA[1]
    return im


def main():
    frames = [quadro(f) for f in range(4)]
    tira = Image.new('RGB', (W * 4, H))
    for i, q in enumerate(frames):
        tira.paste(q, (i * W, 0))
    os.makedirs(PASTA, exist_ok=True)
    tira.save(os.path.join(PASTA, 'menu_fundo.png'))
    if '--previa' in sys.argv:
        c = sys.argv[sys.argv.index('--previa') + 1]
        big = [q.resize((W * 2, H * 2), Image.NEAREST) for q in frames]
        big[0].save(c, save_all=True, append_images=big[1:], duration=300, loop=0)
    print('menu_fundo: 4 quadros')


if __name__ == '__main__':
    main()
