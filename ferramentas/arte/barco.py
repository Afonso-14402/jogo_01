"""O barco do oceano (docs/SISTEMAS.md 2.5): um bote de madeira visto de lado, com remos, a balançar na água
(2 quadros). Saída: arte/objetos/barco.png (tira de 2 quadros de 40×24).

Uso: python3 ferramentas/arte/barco.py
"""
import os
from PIL import Image

OUT = (0x2e, 0x22, 0x2f, 255)
M = ['#4c3e24', '#694f62', '#966c6c', '#ab947a', '#c7dcd0']   # madeira (escuro -> claro)
AGUA = ['#0b8a8f', '#30e1b9', '#8ff8e2']


def rgba(c):
    return tuple(int(c[i:i + 2], 16) for i in (1, 3, 5)) + (255,)


def quadro(f):
    W, H = 40, 24
    im = Image.new('RGBA', (W, H))
    px = im.load()
    sobe = f   # o barco sobe e desce 1 píxel
    casco = set()
    for x in range(3, 37):
        # o casco: mais fundo no meio, a proa (direita) sobe
        topo = 11 + sobe - (2 if x > 32 else 0) - (1 if x < 6 else 0)
        fundo = 18 + sobe - (abs(x - 19) // 7)
        for y in range(topo, fundo + 1):
            casco.add((x, y))
    for (x, y) in casco:
        k = 3 if y <= min(yy for (xx, yy) in casco if xx == x) + 1 else (2 if (y - 12) % 3 else 1)
        px[x, y] = rgba(M[k])
    for (x, y) in casco:   # contorno
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            q = (x + dx, y + dy)
            if q not in casco and 0 <= q[0] < W and 0 <= q[1] < H:
                px[q] = OUT
    for x in range(8, 31, 7):   # bancos (tábuas por dentro)
        px[x, 12 + sobe] = rgba(M[0])
    for i in range(9):   # remo
        x, y = 26 + i, 9 + sobe + i // 2 + (f == 1)
        if 0 <= x < W and 0 <= y < H:
            px[x, y] = rgba(M[1])
    for x in range(1, 39):   # água a bater no casco
        y = 19 + sobe if (x + f) % 5 else 18 + sobe
        if y < H and px[x, y][3] == 0 or (x < 4 or x > 35):
            px[x, min(H - 1, y)] = rgba(AGUA[2 if (x + f) % 3 == 0 else 1])
    return im


if __name__ == '__main__':
    pasta = os.path.join('arte', 'objetos')
    os.makedirs(pasta, exist_ok=True)
    tira = Image.new('RGBA', (80, 24))
    for f in range(2):
        tira.paste(quadro(f), (f * 40, 0))
    tira.save(os.path.join(pasta, 'barco.png'))
    tira.resize((480, 144), Image.NEAREST).save('/tmp/claude-0/-home-user-jogo-01/3de90a57-1f56-55e2-a780-332a66dff1fc/scratchpad/barco.png')
    print('ok barco')
