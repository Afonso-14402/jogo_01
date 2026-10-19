"""Logótipo "A TORRE" para o menu inicial (docs/INTERFACE.md, secção 6): letras grossas douradas com contorno,
uma torrezinha no lugar do "T" grande, e um brilho que passa (8 frames).
Saída: arte/ui/logo.png (tira de 8 frames de 160×64).

Uso: python3 ferramentas/arte/logo.py [previa.gif]
"""
import os
import sys
from PIL import Image

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..', 'arte', 'ui')
W, H, N = 160, 64, 8
OURO = ['#7a3045', '#b33831', '#f79617', '#f9c22b', '#fbff86']
CONTORNO = '#2e222f'

# letras 6×9 (X = cheio)
L = {
    'A': ['..XX..', '.XXXX.', 'XX..XX', 'XX..XX', 'XXXXXX', 'XXXXXX', 'XX..XX', 'XX..XX', 'XX..XX'],
    'T': ['XXXXXX', 'XXXXXX', '..XX..', '..XX..', '..XX..', '..XX..', '..XX..', '..XX..', '..XX..'],
    'O': ['.XXXX.', 'XXXXXX', 'XX..XX', 'XX..XX', 'XX..XX', 'XX..XX', 'XX..XX', 'XXXXXX', '.XXXX.'],
    'R': ['XXXXX.', 'XXXXXX', 'XX..XX', 'XX..XX', 'XXXXX.', 'XXXX..', 'XX.XX.', 'XX..XX', 'XX..XX'],
    'E': ['XXXXXX', 'XXXXXX', 'XX....', 'XX....', 'XXXXX.', 'XXXXX.', 'XX....', 'XXXXXX', 'XXXXXX'],
}
TORRE = ['...XX...', '..XXXX..', '..XXXX..', '.XXXXXX.', '..XXXX..', '..X..X..', '..XXXX..', '..XXXX..', '..X..X..',
         '..XXXX..', '.XXXXXX.', '.XXXXXX.', 'XXXXXXXX']


def hexrgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5)) + (255,)


def frame(f):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    cheio = set()
    esc = 2
    x0, y0 = 12, 20
    texto = 'A TORRE'
    x = x0
    for ch in texto:
        if ch == ' ':
            x += 8
            continue
        g = L[ch]
        for yy, linha in enumerate(g):
            for xx, c in enumerate(linha):
                if c == 'X':
                    for dx in range(esc):
                        for dy in range(esc):
                            cheio.add((x + xx * esc + dx, y0 + yy * esc + dy))
        x += 6 * esc + 3
    # a torre ao lado, com uma janela que acende
    tx = x + 2
    for yy, linha in enumerate(TORRE):
        for xx, c in enumerate(linha):
            if c == 'X':
                cheio.add((tx + xx, y0 - 8 + yy * 2))
                cheio.add((tx + xx, y0 - 8 + yy * 2 + 1))
    # contorno
    for (px, py) in list(cheio):
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)):
            q = (px + dx, py + dy)
            if q not in cheio and 0 <= q[0] < W and 0 <= q[1] < H:
                im.putpixel(q, hexrgb(CONTORNO))
    # preencher com degradê de cima para baixo e o brilho em diagonal
    brilho = -20 + f * (W + 40) / (N - 1)
    faixas = [4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 0]   # de cima para baixo (18 px de letra)
    for (px, py) in cheio:
        rel = py - y0 if px < tx else (py - (y0 - 8)) * 18 // 26
        i = faixas[max(0, min(len(faixas) - 1, rel))]
        d = abs((px - rel * 0.6) - brilho)
        if d < 2:
            i = 4
        elif d < 4:
            i = min(4, i + 1)
        im.putpixel((px, py), hexrgb(OURO[i]))
    # janela da torre a piscar
    jx, jy = tx + 3, y0 - 8 + 5 * 2
    if f % 4 < 2:
        for dx in range(2):
            for dy in range(2):
                im.putpixel((jx + dx, jy + dy), hexrgb('#fbff86'))
    return im


def nuvem(semente, w=48, h=16):
    """Nuvem da noite (azul-acinzentada, com contorno claro por cima), 2 tons."""
    import random
    r = random.Random(semente)
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    bolas = [(r.randint(8, w - 8), r.randint(6, h - 5), r.randint(4, 7)) for _ in range(6)]
    for y in range(h):
        for x in range(w):
            dentro = [((x - bx) ** 2 + ((y - by) * 1.6) ** 2) ** 0.5 < br for bx, by, br in bolas]
            if any(dentro) and y < h - 2:
                cima = not any(((x - bx) ** 2 + ((y - 2 - by) * 1.6) ** 2) ** 0.5 < br for bx, by, br in bolas)
                im.putpixel((x, y), hexrgb('#9babb2' if cima else ('#484a77' if y > h * 0.6 else '#625565')))
    return im


if __name__ == '__main__':
    for i in range(3):
        nuvem(i * 7 + 3).save(os.path.join(RAIZ, 'nuvem_%d.png' % (i + 1)))
    frames = [frame(f) for f in range(N)]
    tira = Image.new('RGBA', (W * N, H), (0, 0, 0, 0))
    for i, fr in enumerate(frames):
        tira.paste(fr, (i * W, 0))
    tira.save(os.path.join(RAIZ, 'logo.png'))
    if len(sys.argv) > 1:
        big = [Image.alpha_composite(Image.new('RGBA', (W, H), (30, 29, 57, 255)), fr).resize((W * 4, H * 4), Image.NEAREST).convert('P', palette=Image.ADAPTIVE) for fr in frames]
        big[0].save(sys.argv[1], save_all=True, append_images=big[1:], duration=110, loop=0)
    print('ok logo', N, 'frames')
