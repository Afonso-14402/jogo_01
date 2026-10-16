"""Texturas das peças 3D em pixel art a sério (em vez de ruído píxel a píxel): tijolos, lajes, tábuas, casca,
telhas, janelas, toldos às riscas, folhagem e superfícies lisas — sempre com as cores que a peça já tinha.

O Godot tira as texturas de dentro dos .glb para ficheiros ao lado (<peça>_<material>.png): este script redesenha
esses ficheiros. O base3d.py (Blender) também usa padrao(), por isso as peças novas já saem assim.

Uso: python3 ferramentas/arte/texturas3d.py [pasta ...]   (por omissão: arte/cidade e arte/regioes)
"""
import glob
import math
import os
import random
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(__file__))
import natureza as N
from motor import hexrgb

CONSTRUIDO = ('muralha', 'torre', 'parede', 'casa', 'igreja', 'castelo', 'coluna', 'ruina', 'templo', 'arco', 'portao',
              'poco', 'fonte', 'guilda', 'estalagem', 'taberna', 'forja', 'biblioteca', 'camara', 'quartel', 'arena',
              'escada', 'muro', 'altar', 'trono', 'farol', 'cais', 'adobe', 'castelo')


def _hex(c):
    return '#%02x%02x%02x' % c[:3]


def _lum(c):
    r, g, b = hexrgb(c)
    return 0.3 * r + 0.59 * g + 0.11 * b


def paleta(cores):
    """5 tons do mais escuro para o mais claro, a partir das cores da peça (repete as pontas se forem poucas)."""
    cs = sorted(dict.fromkeys(cores), key=_lum)
    if len(cs) >= 5:
        idx = [0, len(cs) // 4, len(cs) // 2, (3 * len(cs)) // 4, len(cs) - 1]
        return [cs[i] for i in idx]
    while len(cs) < 5:
        cs = [cs[0]] + cs if len(cs) % 2 else cs + [cs[-1]]
    return cs


def tijolos(rnd, r, t):
    img = Image.new('RGB', (t, t), hexrgb(r[0]))
    px = img.load()
    alt = 8 if t >= 32 else 4
    comp = 16 if t >= 32 else 8
    for fila in range(t // alt):
        off = (comp // 2) * (fila % 2)
        for k in range(-1, t // comp + 1):
            x0 = k * comp + off
            cor = rnd.choice([r[2], r[2], r[3], r[1]])
            for y in range(fila * alt + 1, fila * alt + alt):
                for x in range(x0 + 1, x0 + comp):
                    c = cor
                    if y == fila * alt + 1 or x == x0 + 1:
                        c = r[4] if cor == r[3] else r[3]
                    elif y == fila * alt + alt - 1 or x == x0 + comp - 1:
                        c = r[1] if cor != r[1] else r[0]
                    elif rnd.random() < 0.05:
                        c = r[1]
                    px[x % t, y % t] = hexrgb(c)
    return img


def casca(rnd, r, t):
    img = Image.new('RGB', (t, t), hexrgb(r[2]))
    px = img.load()
    for x in range(t):
        faixa = (x * 3 + int(2 * math.sin(x))) % 7
        for y in range(t):
            c = r[2]
            if faixa == 0:
                c = r[0]
            elif faixa == 1:
                c = r[1]
            elif faixa in (3, 4):
                c = r[3] if (y + x) % 9 else r[2]
            px[x, y] = hexrgb(c)
    for _ in range(t // 4):   # nós da madeira
        x, y = rnd.randrange(t), rnd.randrange(t)
        for dx, dy in ((0, 0), (1, 0), (0, 1), (1, 1)):
            px[(x + dx) % t, (y + dy) % t] = hexrgb(r[0])
        px[(x - 1) % t, (y - 1) % t] = hexrgb(r[3])
    return img


def telhas(rnd, r, t):
    img = Image.new('RGB', (t, t), hexrgb(r[1]))
    px = img.load()
    alt = 6 if t >= 32 else 4
    larg = 8 if t >= 32 else 4
    for fila in range(t // alt + 1):
        off = (larg // 2) * (fila % 2)
        for y in range(alt):
            for x in range(t):
                lx = (x + off) % larg
                # cada telha é um arco: claro em cima, escuro em baixo e nas juntas
                c = r[2]
                if y == 0:
                    c = r[3]
                if lx == 0 or y == alt - 1:
                    c = r[0]
                elif lx == 1 and y < alt - 2:
                    c = r[4] if y < 2 else r[3]
                elif lx == larg - 1:
                    c = r[1]
                if rnd.random() < 0.03 and c == r[2]:
                    c = r[1]
                px[x, (fila * alt + y) % t] = hexrgb(c)
    return img


def janela(rnd, r, t):
    """Vidro com caixilho em cruz e um reflexo na diagonal."""
    img = Image.new('RGB', (t, t), hexrgb(r[2]))
    px = img.load()
    for y in range(t):
        for x in range(t):
            c = r[2] if y > t // 2 else r[3]
            if (x + y) % t in range(t // 3, t // 3 + 3) or (x + y) % t == t // 3 + 6:
                c = r[4]
            if x in (0, t - 1, t // 2, t // 2 - 1) or y in (0, t - 1, t // 2, t // 2 - 1):
                c = r[0]
            px[x, y] = hexrgb(c)
    return img


def riscas(rnd, r, t):
    """Toldo às riscas (a cor da peça e branco)."""
    img = Image.new('RGB', (t, t))
    px = img.load()
    viva = r[2]
    for y in range(t):
        for x in range(t):
            faixa = (x // 4) % 2
            c = viva if faixa == 0 else r[4]
            if x % 4 == 3:
                c = r[1] if faixa == 0 else r[3]
            if y == t - 1:
                c = r[1]
            px[x, y] = hexrgb(c)
    return img


def liso(rnd, r, t, brilhos=True):
    """Superfícies lisas (metal, ouro, cristal, tecido): manchas suaves grandes e alguns brilhos."""
    tela = N.Tela(r[2])
    N.base_manchas(tela, rnd, [r[1], r[2], r[2], r[3]], 4)
    if brilhos:
        for _ in range(t // 6):
            x, y = rnd.randrange(t), rnd.randrange(t)
            tela.p(x, y, r[4])
            tela.p(x + 1, y + 1, r[3])
    return tela.img


def reboco(rnd, r, t):
    """Parede rebocada: manchas suaves, rachas finas e a parte de baixo mais suja."""
    tela = N.Tela(r[3])
    N.base_manchas(tela, rnd, [r[2], r[3], r[3], r[4]], 4)
    for _ in range(2):
        x, y = rnd.randrange(t), rnd.randrange(t)
        for k in range(rnd.randint(3, 7)):
            tela.p(x, y, r[1])
            x += rnd.choice([-1, 0, 1])
            y += 1
    for _ in range(t):
        tela.p(rnd.randrange(t), rnd.randrange(t), r[2])
    return tela.img


def padrao(nome, cores, tam=32, semente=1, contexto=''):
    """Escolhe o desenho pelo nome do material (e da peça) e desenha-o com as cores dadas."""
    rnd = random.Random(semente * 31 + sum(map(ord, nome + contexto)))
    r = paleta(cores)
    n = nome.lower()
    ctx = contexto.lower()
    N.T = tam
    try:
        if any(k in n for k in ('telha', 'telhado')):
            return telhas(rnd, r, tam)
        if 'janela' in n or 'vitral' in n or 'vidro' in n:
            return janela(rnd, r, tam)
        if 'toldo' in n:
            return riscas(rnd, r, tam)
        if any(k in n for k in ('casca', 'tronco')):
            return casca(rnd, r, tam)
        if any(k in n for k in ('madeira', 'tabua', 'porta', 'barco', 'ponte', 'passadico', 'caixa', 'palha', 'estante', 'colmeia')):
            return N.chao_tabuas(rnd, r)
        if any(k in n for k in ('folha', 'pinho', 'relva', 'musgo', 'alga', 'erva', 'mato')):
            return N.chao_erva(rnd, r)
        if 'parede' in n and not any(k in n for k in ('pedra', 'rocha')):
            return reboco(rnd, r, tam)
        if any(k in n for k in ('areia', 'duna')):
            return N.chao_areia(rnd, r)
        if any(k in n for k in ('neve', 'gelo')):
            return N.chao_neve(rnd, r) if 'neve' in n else N.chao_lajes(rnd, r, n=5)
        if any(k in n for k in ('terra', 'lama', 'cinza', 'chao', 'caminho')):
            return N.chao_terra(rnd, r)
        if any(k in n for k in ('pedra', 'rocha', 'muralha', 'calcada', 'marmore', 'basalto', 'obsidiana', 'falesia', 'tijolo', 'adobe', 'campa', 'lapide')):
            if any(k in ctx for k in CONSTRUIDO) or any(k in n for k in ('muralha', 'tijolo', 'adobe')):
                return tijolos(rnd, r, tam)
            return N.chao_lajes(rnd, r, n=6 if tam <= 32 else 11)
        return liso(rnd, r, tam)
    finally:
        N.T = 64


def redesenhar(caminho):
    """Um .png tirado de um .glb (<peça>_<material>.png): redesenha-o com as mesmas cores e o mesmo tamanho."""
    pasta, base = os.path.split(caminho)
    nome = base[:-4]
    peca = ''
    for glb in glob.glob(os.path.join(pasta, '*.glb')):
        g = os.path.basename(glb)[:-4]
        if nome.startswith(g + '_') and len(g) > len(peca):
            peca = g
    if not peca:
        return False
    material = nome[len(peca) + 1:]
    img = Image.open(caminho).convert('RGBA')
    if img.size[0] != img.size[1] or img.size[0] > 128:
        return False
    cores = [_hex(c) for n, c in sorted(img.getcolors(1 << 16), reverse=True) if c[3] > 0][:6]
    novo = padrao(material, cores, img.size[0], 1, peca).convert('RGBA')
    novo.save(caminho)
    return True


def main():
    pastas = sys.argv[1:] or ['arte/cidade', 'arte/regioes']
    n = 0
    for p in pastas:
        for f in sorted(glob.glob(os.path.join(p, '**', '*.png'), recursive=True)):
            if os.sep + 'texturas' + os.sep in f or os.sep + 'natureza' + os.sep in f:
                continue
            if redesenhar(f):
                n += 1
    print('texturas 3D redesenhadas: %d' % n)


if __name__ == '__main__':
    main()
