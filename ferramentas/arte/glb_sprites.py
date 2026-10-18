"""Acaba as fotografias das peças 3D (ferramentas/arte/glb_sprites.gd): passa cada píxel à cor mais perto da
paleta Resurrect 64 (docs/ARTE.md, secção 1), tira a meia-transparência e põe o contorno escuro (#2e222f) à
volta, como em toda a arte do jogo.

Uso: python3 ferramentas/arte/glb_sprites.py [pasta]   (por omissão: arte/sprites2d)
"""
import glob
import os
import sys

from PIL import Image

RESURRECT_64 = """2e222f 3e3546 625565 966c6c ab947a 694f62 7f708a 9babb2 c7dcd0 ffffff 6e2727 b33831 ea4f36 f57d4a ae2334
e83b3b fb6b1d f79617 f9c22b 7a3045 9e4539 cd683d e6904e fbb954 4c3e24 676633 a2a947 d5e04b fbff86 165a4c 239063 1ebc73
91db69 cddf6c 313638 374e4a 547e64 92a984 b2ba90 0b5e65 0b8a8f 0eaf9b 30e1b9 8ff8e2 323353 484a77 4d65b4 4d9be6 8fd3ff
45293f 6b3e75 905ea9 a884f3 eaaded 753c54 a24b6f cf657f ed8099 831c5d c32454 f04f78 f68181 fca790 fdcbb0""".split()
PALETA = [tuple(int(c[i:i + 2], 16) for i in (0, 2, 4)) for c in RESURRECT_64]
OUT = (0x2e, 0x22, 0x2f)
_cache = {}


def perto(c):
    if c in _cache:
        return _cache[c]
    r, g, b = c
    # distância "à vista": o verde pesa mais, o azul menos
    m = min(PALETA, key=lambda p: 3 * (p[0] - r) ** 2 + 4 * (p[1] - g) ** 2 + 2 * (p[2] - b) ** 2)
    _cache[c] = m
    return m


def acabar(caminho):
    im = Image.open(caminho).convert('RGBA')
    w, h = im.size
    px = im.load()
    cheio = set()
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a >= 128:
                px[x, y] = perto((r, g, b)) + (255,)
                cheio.add((x, y))
            else:
                px[x, y] = (0, 0, 0, 0)
    for (x, y) in cheio:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            v = (x + dx, y + dy)
            if v not in cheio and 0 <= v[0] < w and 0 <= v[1] < h:
                px[v] = OUT + (255,)
    im.save(caminho)


def main():
    pasta = sys.argv[1] if len(sys.argv) > 1 else os.path.join('arte', 'sprites2d')
    fs = sorted(glob.glob(os.path.join(pasta, '**', '*.png'), recursive=True))
    for i, f in enumerate(fs):
        acabar(f)
        if i % 500 == 0:
            print(i, '/', len(fs))
    print('acabadas:', len(fs))


if __name__ == '__main__':
    main()
