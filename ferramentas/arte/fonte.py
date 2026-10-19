"""A letra do jogo em pixel art (docs/INTERFACE.md, secção 1: "fonte pixel"), desenhada píxel a píxel, com os
acentos do português (á à â ã é ê í ó ô õ ú ç...), números, pontuação e alguns símbolos (— … « » × · º ª € °).

Cada letra tem a largura que precisa (o "i" é estreito, o "m" é largo) e 1 píxel de espaço. Linhas (de cima para
baixo, 12 no total): 0–1 acentos das maiúsculas · 2–8 maiúsculas e letras altas (7 píxeis) · 4–8 minúsculas
(5 píxeis), com os acentos nas linhas 2–3 · 9–10 as "pernas" (g, j, p, q, y, ç). A linha de base é a 9.

Saída: arte/ui/fonte_pixel.png + arte/ui/fonte_pixel.fnt (formato BMFont em texto, que o Godot lê como fonte) e a\nmesma com contorno escuro (fonte_pixel_contorno.*), para os textos por cima do mapa.
Uso:   python3 ferramentas/arte/fonte.py [--previa caminho.png]
"""
import os
import sys

from PIL import Image

PASTA = os.path.join(os.path.dirname(__file__), '..', '..', 'arte', 'ui')
ALTURA = 12
BASE = 9
COR = (255, 255, 255, 255)

# ---------------- maiúsculas e letras altas: 7 linhas (2–8) ----------------
ALTAS = {
    'A': ".##.|#..#|#..#|####|#..#|#..#|#..#",
    'B': "###.|#..#|#..#|###.|#..#|#..#|###.",
    'C': ".###|#...|#...|#...|#...|#...|.###",
    'D': "###.|#..#|#..#|#..#|#..#|#..#|###.",
    'E': "####|#...|#...|###.|#...|#...|####",
    'F': "####|#...|#...|###.|#...|#...|#...",
    'G': ".###|#...|#...|#.##|#..#|#..#|.###",
    'H': "#..#|#..#|#..#|####|#..#|#..#|#..#",
    'I': "###|.#.|.#.|.#.|.#.|.#.|###",
    'J': "..##|...#|...#|...#|...#|#..#|.##.",
    'K': "#..#|#..#|#.#.|##..|#.#.|#..#|#..#",
    'L': "#...|#...|#...|#...|#...|#...|####",
    'M': "#...#|##.##|#.#.#|#.#.#|#...#|#...#|#...#",
    'N': "#..#|##.#|##.#|#.##|#.##|#..#|#..#",
    'O': ".##.|#..#|#..#|#..#|#..#|#..#|.##.",
    'P': "###.|#..#|#..#|###.|#...|#...|#...",
    'Q': ".##.|#..#|#..#|#..#|#..#|#.#.|.#.#",
    'R': "###.|#..#|#..#|###.|#.#.|#..#|#..#",
    'S': ".###|#...|#...|.##.|...#|...#|###.",
    'T': "#####|..#..|..#..|..#..|..#..|..#..|..#..",
    'U': "#..#|#..#|#..#|#..#|#..#|#..#|.##.",
    'V': "#...#|#...#|#...#|.#.#.|.#.#.|..#..|..#..",
    'W': "#...#|#...#|#...#|#.#.#|#.#.#|##.##|#...#",
    'X': "#..#|#..#|.##.|.##.|.##.|#..#|#..#",
    'Y': "#...#|#...#|.#.#.|..#..|..#..|..#..|..#..",
    'Z': "####|...#|..#.|.##.|.#..|#...|####",
    '0': ".##.|#..#|#.##|##.#|#..#|#..#|.##.",
    '1': ".#.|##.|.#.|.#.|.#.|.#.|###",
    '2': ".##.|#..#|...#|..#.|.#..|#...|####",
    '3': "###.|...#|...#|.##.|...#|...#|###.",
    '4': "#..#|#..#|#..#|####|...#|...#|...#",
    '5': "####|#...|###.|...#|...#|#..#|.##.",
    '6': ".##.|#...|#...|###.|#..#|#..#|.##.",
    '7': "####|...#|..#.|..#.|.#..|.#..|.#..",
    '8': ".##.|#..#|#..#|.##.|#..#|#..#|.##.",
    '9': ".##.|#..#|#..#|.###|...#|...#|.##.",
    'b': "#...|#...|###.|#..#|#..#|#..#|###.",
    'd': "...#|...#|.###|#..#|#..#|#..#|.###",
    'f': "..##|.#..|####|.#..|.#..|.#..|.#..",
    'h': "#...|#...|###.|#..#|#..#|#..#|#..#",
    'k': "#...|#...|#..#|#.#.|##..|#.#.|#..#",
    'l': "##|.#|.#|.#|.#|.#|.##",
    't': ".#..|.#..|####|.#..|.#..|.#..|..##",
    '!': "#|#|#|#|#|.|#",
    '?': ".##.|#..#|...#|..#.|.#..|....|.#..",
    '(': ".#|#.|#.|#.|#.|#.|.#",
    ')': "#.|.#|.#|.#|.#|.#|#.",
    '[': "##|#.|#.|#.|#.|#.|##",
    ']': "##|.#|.#|.#|.#|.#|##",
    '/': "...#|...#|..#.|.#..|.#..|#...|#...",
    '\\': "#...|#...|.#..|..#.|..#.|...#|...#",
    '%': "#..#|#..#|..#.|.#..|.#..|#..#|#..#",
    '&': ".#..|#.#.|#.#.|.#..|#.##|#..#|.##.",
    '#': ".#.#.|.#.#.|#####|.#.#.|#####|.#.#.|.#.#.",
    '@': ".###.|#...#|#.###|#.#.#|#.###|#....|.###.",
    '$': ".###|#.#.|#.#.|.###|..##|..##|###.",
    '€': "..##|.#..|####|.#..|####|.#..|..##",
    '|': "#|#|#|#|#|#|#",
    '"': "#.#|#.#|...|...|...|...|...",
    "'": "#|#|.|.|.|.|.",
    '`': "#.|.#|..|..|..|..|..",
    '*': "....|#.#.|.#..|#.#.|....|....|....",
    '+': "...|...|.#.|###|.#.|...|...",
    '<': "...|..#|.#.|#..|.#.|..#|...",
    '>': "...|#..|.#.|..#|.#.|#..|...",
    '=': "...|...|###|...|###|...|...",
    '^': ".#.|#.#|...|...|...|...|...",
    '~': "....|....|.#.#|#.#.|....|....|....",
    '{': "..#|.#.|.#.|#..|.#.|.#.|..#",
    '}': "#..|.#.|.#.|..#|.#.|.#.|#..",
    'º': "###|#.#|###|...|###|...|...",
    # símbolos que aparecem nos textos do jogo (setas, estrelas, corações, notas, emojis simples)
    '→': ".....|..#..|...#.|#####|...#.|..#..|.....",
    '←': ".....|..#..|.#...|#####|.#...|..#..|.....",
    '↑': "..#..|.###.|#.#.#|..#..|..#..|..#..|..#..",
    '↓': "..#..|..#..|..#..|..#..|#.#.#|.###.|..#..",
    '⇒': ".....|...#.|#####|....#|#####|...#.|.....",
    '⇐': ".....|.#...|#####|#....|#####|.#...|.....",
    '▶': "#...|##..|###.|####|###.|##..|#...",
    '◀': "...#|..##|.###|####|.###|..##|...#",
    '▲': ".....|.....|..#..|.###.|#####|.....|.....",
    '▼': ".....|.....|#####|.###.|..#..|.....|.....",
    '◆': "..#..|.###.|#####|#####|.###.|..#..|.....",
    '•': "...|...|.#.|###|.#.|...|...",
    '⭐': "..#..|..#..|#####|.###.|.###.|##.##|#...#",
    '★': "..#..|..#..|#####|.###.|.###.|##.##|#...#",
    '☆': "..#..|.#.#.|##.##|#...#|.#.#.|#.#.#|##.##",
    '✦': "..#..|..#..|.###.|#####|.###.|..#..|..#..",
    '❤': ".....|##.##|#####|#####|.###.|..#..|.....",
    '♥': ".....|##.##|#####|#####|.###.|..#..|.....",
    '♪': "..##|..#.|..#.|..#.|.##.|###.|.#..",
    '🎵': "..##|..#.|..#.|..#.|.##.|###.|.#..",
    '✓': ".....|....#|...#.|#..#.|.##..|..#..|.....",
    '✕': ".....|#...#|.#.#.|..#..|.#.#.|#...#|.....",
    '✗': ".....|#...#|.#.#.|..#..|.#.#.|#...#|.....",
    '∞': ".......|.......|.##.##.|#..#..#|.##.##.|.......|.......",
    '−': "...|...|...|###|...|...|...",
    '²': "##.|..#|.#.|###|...|...|...",
    '⚙': ".#.#.|#####|##.##|#...#|##.##|#####|.#.#.",
    '☀': "#.#.#|.###.|#####|#####|#####|.###.|#.#.#",
    '💀': ".###.|#####|#.#.#|#####|.###.|.#.#.|.....",
    '🔥': "..#..|.##..|.###.|#####|##.##|##.##|.###.",
    '🔀': ".....|##.##|..#..|.#.#.|##.##|.....|.....",
    '⚔': "#...#|.#.#.|..#..|.#.#.|#...#|.....|.....",
    '🎒': ".###.|#...#|#####|#.#.#|#####|#####|.....",
    '🎬': "#.#.#|#####|.....|#####|#####|#####|.....",
    '▒': "#.#.|.#.#|#.#.|.#.#|#.#.|.#.#|#.#.",
    '░': "#...|..#.|#...|..#.|#...|..#.|#...",
    '▓': "###.|.###|###.|.###|###.|.###|###.",
    '◌': ".....|.#.#.|#...#|.....|#...#|.#.#.|.....",
    'ª': ".##|#.#|.##|...|###|...|...",
    '°': ".#.|#.#|.#.|...|...|...|...",
}

# ---------------- minúsculas: 5 linhas (4–8) + pernas (9–10) ----------------
BAIXAS = {
    'a': (".##.|...#|.###|#..#|.###", None),
    'c': (".###|#...|#...|#...|.###", None),
    'e': (".##.|#..#|####|#...|.###", None),
    'g': (".###|#..#|#..#|#..#|.###", "...#|###."),
    'i': ("#|#|#|#|#", None),
    'j': (".#|.#|.#|.#|.#", ".#|#."),
    'm': ("####.|#.#.#|#.#.#|#.#.#|#.#.#", None),
    'n': ("###.|#..#|#..#|#..#|#..#", None),
    'o': (".##.|#..#|#..#|#..#|.##.", None),
    'p': ("###.|#..#|#..#|#..#|###.", "#...|#..."),
    'q': (".###|#..#|#..#|#..#|.###", "...#|...#"),
    'r': ("#.##|##..|#...|#...|#...", None),
    's': (".###|#...|.##.|...#|###.", None),
    'u': ("#..#|#..#|#..#|#..#|.###", None),
    'v': ("#..#|#..#|#..#|.##.|.##.", None),
    'w': ("#...#|#...#|#.#.#|#.#.#|.#.#.", None),
    'x': ("#..#|.##.|.##.|.##.|#..#", None),
    'y': ("#..#|#..#|#..#|#..#|.###", "...#|###."),
    'z': ("####|..#.|.#..|#...|####", None),
    '.': (".|.|.|.|#", None),
    ',': (".|.|.|.|#", "#."),
    ':': (".|#|.|.|#", None),
    ';': (".|#|.|.|#", "#."),
    '-': ("...|...|###|...|...", None),
    '_': ("....|....|....|....|....", "####"),
    '·': (".|.|#|.|.", None),
    '×': ("...|#.#|.#.|#.#|...", None),
    '—': ("......|......|######|......|......", None),
    '–': ("....|....|####|....|....", None),
    '…': (".....|.....|.....|.....|#.#.#", None),
    '«': ("....|.#.#|#.#.|.#.#|....", None),
    '»': ("....|#.#.|.#.#|#.#.|....", None),
    '¿': ("..#.|....|..#.|.#..|#..#", ".##."),
    '¡': ("#|.|#|#|#", "#"),
}
# o "i" e o "j" levam o ponto por cima (linha 2), como os acentos
PONTO_IJ = {'i': "#", 'j': ".#"}

# ---------------- acentos (2 linhas) ----------------
ACENTOS = {
    'agudo': "..#|.#.", 'grave': "#..|.#.", 'circ': ".#.|#.#", 'til': ".#.#|#.#.", 'trema': "#.#|...",
}
COMPOSTAS = {
    'á': ('a', 'agudo'), 'à': ('a', 'grave'), 'â': ('a', 'circ'), 'ã': ('a', 'til'), 'ä': ('a', 'trema'),
    'é': ('e', 'agudo'), 'è': ('e', 'grave'), 'ê': ('e', 'circ'), 'ë': ('e', 'trema'),
    'í': ('ı', 'agudo'), 'ì': ('ı', 'grave'), 'î': ('ı', 'circ'), 'ï': ('ı', 'trema'),
    'ó': ('o', 'agudo'), 'ò': ('o', 'grave'), 'ô': ('o', 'circ'), 'õ': ('o', 'til'), 'ö': ('o', 'trema'),
    'ú': ('u', 'agudo'), 'ù': ('u', 'grave'), 'û': ('u', 'circ'), 'ü': ('u', 'trema'), 'ñ': ('n', 'til'),
    'Á': ('A', 'agudo'), 'À': ('A', 'grave'), 'Â': ('A', 'circ'), 'Ã': ('A', 'til'), 'Ä': ('A', 'trema'),
    'É': ('E', 'agudo'), 'È': ('E', 'grave'), 'Ê': ('E', 'circ'), 'Í': ('I', 'agudo'), 'Î': ('I', 'circ'),
    'Ó': ('O', 'agudo'), 'Ò': ('O', 'grave'), 'Ô': ('O', 'circ'), 'Õ': ('O', 'til'), 'Ö': ('O', 'trema'),
    'Ú': ('U', 'agudo'), 'Ü': ('U', 'trema'), 'Ñ': ('N', 'til'),
}


def _linhas(txt):
    return txt.split('|')


def glifos():
    """{caractere: lista de 12 strings (as linhas), todas da mesma largura}"""
    g = {}

    def vazio(w):
        return ['.' * w for _ in range(ALTURA)]

    for ch, t in ALTAS.items():
        ls = _linhas(t)
        w = len(ls[0])
        out = vazio(w)
        for i, l in enumerate(ls):
            out[2 + i] = l
        g[ch] = out
    for ch, (t, pernas) in BAIXAS.items():
        ls = _linhas(t)
        w = max(len(x) for x in ls + (_linhas(pernas) if pernas else []))
        out = vazio(w)
        for i, l in enumerate(ls):
            out[4 + i] = l.ljust(w, '.')
        if pernas:
            for i, l in enumerate(_linhas(pernas)):
                out[9 + i] = l.ljust(w, '.')
        g[ch] = out
    g['ı'] = g['i']   # o i sem ponto (para os acentos)
    for ch, ponto in PONTO_IJ.items():
        out = list(g[ch])
        out[2] = ponto.ljust(len(out[0]), '.')
        g[ch] = out
    # o ç / Ç: o c com uma perninha
    for base, novo in (('c', 'ç'), ('C', 'Ç')):
        out = list(g[base])
        w = len(out[0])
        out[9] = ('.#'.ljust(w, '.'))
        out[10] = ('##'.ljust(w, '.'))
        g[novo] = out
    for ch, (base, ac) in COMPOSTAS.items():
        out = list(g[base])
        w = len(out[0])
        a = _linhas(ACENTOS[ac])
        topo = 0 if base.isupper() else 2
        aw = len(a[0])
        x0 = max(0, (w - aw + 1) // 2)
        for i, l in enumerate(a):
            linha = list(out[topo + i])
            for k, c in enumerate(l):
                if c == '#' and x0 + k < w:
                    linha[x0 + k] = '#'
            out[topo + i] = ''.join(linha)
        g[ch] = out
    g[' '] = vazio(3)
    g['\ufe0f'] = ['' for _ in range(ALTURA)]   # (o "seletor" que vem depois de alguns emojis: não ocupa espaço)
    return g


def gerar():
    g = glifos()
    chars = sorted(g.keys(), key=ord)
    larg_total = sum(len(g[c][0]) + 2 for c in chars)
    colunas = 1024
    linhas_atlas = []
    x = y = 0
    pos = {}
    for c in chars:
        w = len(g[c][0])
        if x + w + 2 > colunas:
            x = 0
            y += ALTURA + 2
        pos[c] = (x + 1, y + 1)
        x += w + 2
    img = Image.new('RGBA', (colunas, y + ALTURA + 2), (0, 0, 0, 0))
    for c in chars:
        px, py = pos[c]
        for j, l in enumerate(g[c]):
            for i, ch in enumerate(l):
                if ch == '#':
                    img.putpixel((px + i, py + j), COR)
    os.makedirs(PASTA, exist_ok=True)
    img.save(os.path.join(PASTA, 'fonte_pixel.png'))
    # size=9: o Godot escala a letra pelo múltiplo inteiro mais perto de tamanho/9 — os textos de 13 a 22 (quase
    # todos) ficam a 2× (linhas de 24 píxeis), os títulos de 28 a 40 a 3× ou 4×; os píxeis ficam sempre certos
    linhas = ['info face="Torre" size=9 bold=0 italic=0 charset="" unicode=1 stretchH=100 smooth=0 aa=1 padding=0,0,0,0 spacing=1,1',
              'common lineHeight=%d base=%d scaleW=%d scaleH=%d pages=1 packed=0' % (ALTURA, BASE, img.size[0], img.size[1]),
              'page id=0 file="fonte_pixel.png"', 'chars count=%d' % len(chars)]
    for c in chars:
        px, py = pos[c]
        w = len(g[c][0])
        linhas.append('char id=%d x=%d y=%d width=%d height=%d xoffset=0 yoffset=0 xadvance=%d page=0 chnl=15'
                      % (ord(c), px, py, w, ALTURA, w + 1 if w else 0))
    with open(os.path.join(PASTA, 'fonte_pixel.fnt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(linhas) + '\n')
    return g


def gerar_contorno(g):
    """A mesma letra com um contorno escuro de 1 píxel à volta (#2e222f), para os textos por cima do mapa
    (números de dano, nomes, mensagens do Sistema): as letras em pixel não aceitam o contorno do Godot."""
    chars = sorted(g.keys(), key=ord)
    colunas = 1024
    x = y = 0
    pos = {}
    for c in chars:
        w = len(g[c][0]) + 2
        if x + w + 1 > colunas:
            x = 0
            y += ALTURA + 3
        pos[c] = (x, y)
        x += w + 1
    img = Image.new('RGBA', (colunas, y + ALTURA + 3), (0, 0, 0, 0))
    escuro = (0x2e, 0x22, 0x2f, 255)
    for c in chars:
        px, py = pos[c]
        cheio = {(i + 1, j + 1) for j, l in enumerate(g[c]) for i, ch in enumerate(l) if ch == '#'}
        for (i, j) in cheio:
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if (i + dx, j + dy) not in cheio:
                        img.putpixel((px + i + dx, py + j + dy), escuro)
        for (i, j) in cheio:
            img.putpixel((px + i, py + j), COR)
    img.save(os.path.join(PASTA, 'fonte_pixel_contorno.png'))
    linhas = ['info face="Torre contorno" size=9 bold=0 italic=0 charset="" unicode=1 stretchH=100 smooth=0 aa=1 padding=1,1,1,1 spacing=1,1',
              'common lineHeight=%d base=%d scaleW=%d scaleH=%d pages=1 packed=0' % (ALTURA + 1, BASE + 1, img.size[0], img.size[1]),
              'page id=0 file="fonte_pixel_contorno.png"', 'chars count=%d' % len(chars)]
    for c in chars:
        px, py = pos[c]
        w = len(g[c][0])
        linhas.append('char id=%d x=%d y=%d width=%d height=%d xoffset=-1 yoffset=0 xadvance=%d page=0 chnl=15'
                      % (ord(c), px, py, w + 2, ALTURA + 2, w + 1 if w else 0))
    with open(os.path.join(PASTA, 'fonte_pixel_contorno.fnt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(linhas) + '\n')


def previa(caminho, g):
    textos = ['A TORRE — Andar 1: Prado do Despertar', 'Olá! Missão aceite: «O Rei das Tocas» (1/3)',
              'Ação, coração, pão, mãe, avó, você, café, júri, órfão', 'ÁÀÂÃ ÉÊ Í ÓÔÕ Ú Ç ÑçÇ 0123456789',
              'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ', '[Sistema] Obtiveste: Gel de Slime ×3 · 120 ouro … 50%']
    esc = 3
    im = Image.new('RGB', (900 * esc // 2, (len(textos) * 14 + 8) * esc), (50, 51, 83))
    for k, t in enumerate(textos):
        x = 4
        for ch in t:
            gl = g.get(ch, g['?'])
            for j, l in enumerate(gl):
                for i, c in enumerate(l):
                    if c == '#':
                        for a in range(esc):
                            for b in range(esc):
                                im.putpixel(((x + i) * esc + a, (4 + k * 14 + j) * esc + b), (255, 255, 255))
            x += len(gl[0]) + 1
    im.save(caminho)


if __name__ == '__main__':
    g = gerar()
    gerar_contorno(g)
    if '--previa' in sys.argv:
        previa(sys.argv[sys.argv.index('--previa') + 1], g)
    print('letras:', len(g))
