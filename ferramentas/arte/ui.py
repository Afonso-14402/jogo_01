"""Interface do "Sistema" (docs/INTERFACE.md): janelas azuis translúcidas com moldura brilhante, botões, barras,
casas do inventário, minimapa, marcadores, avisos e controlos de toque. As janelas e botões são 9-slice
(no Godot: NinePatchRect com margens de 6 px). Saída: arte/ui/

Uso: python3 ferramentas/arte/ui.py
"""
import math
import os
import random
from PIL import Image

PASTA = os.path.join(os.path.dirname(__file__), '..', '..', 'arte', 'ui')
FUNDO, MOLDURA, BRILHO, BRANCO, OURO, PERIGO, CURA = '#323353', '#4d9be6', '#8fd3ff', '#ffffff', '#f9c22b', '#e83b3b', '#91db69'
OUT = '#2e222f'


def hx(c, a=255):
    return tuple(int(c[i:i + 2], 16) for i in (1, 3, 5)) + (a,)


def janela(W=24, H=24, moldura=MOLDURA, brilho=BRILHO, fundo=FUNDO, alpha=217, cantos=True):
    """Janela 9-slice: fundo translúcido (85%), moldura fina com brilho em cima e cantos marcados."""
    im = Image.new('RGBA', (W, H))
    for y in range(H):
        for x in range(W):
            borda = x in (0, W - 1) or y in (0, H - 1)
            dentro = x in (1, W - 2) or y in (1, H - 2)
            if borda:
                if (x in (0, W - 1)) and (y in (0, H - 1)):
                    continue
                im.putpixel((x, y), hx(moldura))
            elif dentro:
                im.putpixel((x, y), hx(brilho if y == 1 else moldura, 160))
            else:
                # linhas de "ecrã" muito suaves
                im.putpixel((x, y), hx(fundo, alpha - (12 if y % 3 == 0 else 0)))
    if cantos:
        for (x, y) in ((1, 1), (2, 1), (1, 2), (W - 2, 1), (W - 3, 1), (W - 2, 2), (1, H - 2), (2, H - 2), (1, H - 3),
                       (W - 2, H - 2), (W - 3, H - 2), (W - 2, H - 3)):
            im.putpixel((x, y), hx(brilho))
    return im


def janela_falha(semente=1):
    """Região 10: janela com cores erradas e linhas deslocadas."""
    im = janela(24, 24, moldura='#e83b3b', brilho='#a884f3', fundo='#2e222f')
    rnd = random.Random(semente)
    out = Image.new('RGBA', im.size)
    for y in range(24):
        d = rnd.choice((0, 0, 0, 1, -1, 2))
        linha = im.crop((0, y, 24, y + 1))
        out.paste(linha, (d, y))
    return out


def botao(estado):
    cores = {'normal': (MOLDURA, '#484a77', BRILHO), 'por_cima': (BRILHO, '#4d65b4', BRANCO),
             'premido': ('#4d65b4', '#323353', MOLDURA), 'desligado': ('#625565', '#3e3546', '#7f708a')}[estado]
    m, f, b = cores
    W, H = 16, 16
    im = Image.new('RGBA', (W, H))
    dy = 1 if estado == 'premido' else 0
    for y in range(H):
        for x in range(W):
            if (x in (0, W - 1)) and (y in (0, H - 1)):
                continue
            if x in (0, W - 1) or y in (0, H - 1):
                c = OUT
            elif y == H - 2 and not dy:
                c = '#2e222f'
            elif x in (1, W - 2) or y in (1 + dy, H - 3 + dy):
                c = b if y == 1 + dy else m
            else:
                c = f
            im.putpixel((x, y), hx(c))
    return im


def barra_moldura():
    W, H = 16, 8
    im = Image.new('RGBA', (W, H))
    for y in range(H):
        for x in range(W):
            if (x in (0, W - 1)) and (y in (0, H - 1)):
                continue
            borda = x in (0, W - 1) or y in (0, H - 1)
            im.putpixel((x, y), hx(OUT if borda else '#2e222f', 255 if borda else 200))
    for x in range(1, W - 1):
        im.putpixel((x, 1), hx('#484a77'))
    return im


def barra_cheia(cores):
    """Preenchimento 8×6 que se repete na horizontal: claro em cima, escuro em baixo."""
    escura, media, clara = cores
    im = Image.new('RGBA', (8, 6))
    for y in range(6):
        for x in range(8):
            c = clara if y == 0 else escura if y == 5 else media
            if y == 1 and x % 4 == 0:
                c = BRANCO
            im.putpixel((x, y), hx(c))
    return im


BARRAS = {'hp': ('#b33831', '#e83b3b', '#f68181'), 'mp': ('#4d65b4', '#4d9be6', '#8fd3ff'),
          'estamina': ('#f79617', '#f9c22b', '#fbff86'), 'xp': ('#239063', '#1ebc73', '#91db69'),
          'boss': ('#6e2727', '#b33831', '#ea4f36'), 'temperatura': ('#4d65b4', '#8fd3ff', '#ffffff'),
          'ar': ('#0b8a8f', '#30e1b9', '#8ff8e2'), 'calor': ('#b33831', '#fb6b1d', '#f9c22b'),
          'amizade': ('#c32454', '#f04f78', '#f68181')}


def casa(selecionada=False, raridade=None):
    W = 20
    im = Image.new('RGBA', (W, W))
    m = OURO if selecionada else (raridade or '#484a77')
    for y in range(W):
        for x in range(W):
            if (x in (0, W - 1)) and (y in (0, W - 1)):
                continue
            borda = x in (0, W - 1) or y in (0, W - 1)
            if borda:
                im.putpixel((x, y), hx(m))
            else:
                im.putpixel((x, y), hx('#2e222f' if (x + y) % 2 else '#323353', 200))
    if selecionada:
        for (x, y) in ((1, 1), (W - 2, 1), (1, W - 2), (W - 2, W - 2)):
            im.putpixel((x, y), hx('#fbff86'))
    return im


RARIDADES = {'comum': '#9babb2', 'invulgar': '#1ebc73', 'raro': '#4d9be6', 'epico': '#a884f3', 'lendario': '#f9c22b',
             'mitico': '#e83b3b'}


def circulo(D, cor_borda, cor_fundo, alpha=170, anel=2):
    im = Image.new('RGBA', (D, D))
    c = (D - 1) / 2
    for y in range(D):
        for x in range(D):
            d = math.hypot(x - c, y - c)
            if d <= c:
                if d > c - anel:
                    im.putpixel((x, y), hx(cor_borda))
                elif d > c - anel - 1:
                    im.putpixel((x, y), hx(BRILHO if (x + y) < D else cor_borda, 200))
                else:
                    im.putpixel((x, y), hx(cor_fundo, alpha))
    return im


def grelha(txt, cores, W=None, H=None):
    linhas = txt.strip('\n').split('\n')
    W = W or max(len(l) for l in linhas)
    H = H or len(linhas)
    im = Image.new('RGBA', (W, H))
    cores = dict(cores, o=OUT)
    for y, l in enumerate(linhas):
        for x, ch in enumerate(l):
            if ch != '.':
                im.putpixel((x, y), hx(cores[ch]))
    return im


AVISO = """
.ooo.
oYYYo
oYYYo
oYYYo
oYYYo
.oYo.
.oYo.
..o..
.ooo.
oYYYo
.ooo.
"""
PERGUNTA = """
.ooooo.
oYYYYYo
oYoooYo
.o..oYo
...oYo.
..oYo..
..oYo..
...o...
..ooo..
..oYo..
..ooo..
"""
SETA = """
o.......
oo......
oWo.....
oWWo....
oWWWo...
oWWWWo..
oWWooo..
oWo.....
oo......
"""
BOLO = """
...o.o...
...Y.Y...
..oRoRo..
.oWWWWWo.
.oPWPWPo.
oPPPPPPPo
oWWWWWWWo
ooooooooo
"""
MARCAS = {  # minimapa, 5×5
    'npc': ('.ooo.\noGGGo\noGGGo\noGGGo\n.ooo.', {'G': CURA}),
    'missao': ('..o..\n.oYo.\noYYYo\n.oYo.\n..o..', {'Y': OURO}),
    'bau': ('ooooo\noBYBo\nooooo\noBBBo\nooooo', {'B': '#966c6c', 'Y': OURO}),
    'saida': ('..o..\n.oWo.\noWWWo\n..W..\n..W..', {'W': BRILHO}),
    'jogador': ('..o..\n.oWo.\noWWWo\noWoWo\no...o', {'W': BRANCO}),
    'inimigo': ('.ooo.\noRRRo\noRRRo\noRRRo\n.ooo.', {'R': PERIGO}),
    'boss': ('o.o.o\noRRRo\noRRRo\noRRRo\nooooo', {'R': PERIGO}),
}


def gerar():
    os.makedirs(PASTA, exist_ok=True)
    s = lambda nome, im: im.save(os.path.join(PASTA, nome + '.png'))
    s('janela_sistema', janela())
    s('janela_dialogo', janela(moldura='#4d65b4', brilho=MOLDURA))
    s('janela_aviso', janela(moldura=PERIGO, brilho='#f68181', fundo='#45293f'))
    s('janela_nivel', janela(moldura=OURO, brilho='#fbff86', fundo='#323353'))
    for i in range(3):
        s(f'janela_falha_{i + 1}', janela_falha(i + 1))
    s('dica', janela(16, 16, cantos=False))
    for e in ('normal', 'por_cima', 'premido', 'desligado'):
        s(f'botao_{e}', botao(e))
    s('barra_moldura', barra_moldura())
    for nome, cores in BARRAS.items():
        s(f'barra_{nome}', barra_cheia(cores))
    s('casa', casa())
    s('casa_selecionada', casa(True))
    for nome, cor in RARIDADES.items():
        s(f'casa_{nome}', casa(raridade=cor))
    s('minimapa_moldura', circulo(64, MOLDURA, FUNDO))
    s('toque_joystick_base', circulo(48, MOLDURA, FUNDO, alpha=110))
    s('toque_joystick_bola', circulo(20, BRILHO, MOLDURA, alpha=220))
    s('toque_atacar', circulo(40, OURO, '#9e4539', alpha=170, anel=3))
    s('toque_botao', circulo(24, MOLDURA, FUNDO))
    s('recarga_skill', circulo(24, '#2e222f', '#2e222f', alpha=150, anel=1))
    s('aviso_exclamacao', grelha(AVISO, {'Y': OURO}))
    s('aviso_exclamacao_vermelho', grelha(AVISO, {'Y': PERIGO}))
    s('aviso_pergunta', grelha(PERGUNTA, {'Y': OURO}))
    s('cursor', grelha(SETA, {'W': BRANCO}))
    s('aniversario', grelha(BOLO, {'Y': OURO, 'R': PERIGO, 'W': BRANCO, 'P': '#f04f78'}))
    for nome, (g, cores) in MARCAS.items():
        s(f'mapa_{nome}', grelha(g, cores))
    n = len([f for f in os.listdir(PASTA) if f.endswith('.png')])
    print('ok', n, 'peças de interface')


if __name__ == '__main__':
    gerar()
