"""Vida do mapa: bichinhos pequenos que andam pelos andares só para dar ambiente
(borboletas, pássaros, coelhos, morcegos, libelinhas, sapos, lagartos, caranguejos, peixes e folhas a cair).

Como se desenha:
  - cada pose é uma GRELHA de letras, píxel a píxel (uma letra = um papel: corpo, barriga, asa, olho...);
  - uma pose pode ter várias CAMADAS (ex.: o corpo do pássaro e a asa por cima). A camada da frente ganha um
    contorno escuro que a separa da de trás, como na Aranha-Mãe;
  - o contorno de fora (#2e222f) é posto pelo motor; os píxeis SOLTOS (patas finas, antenas, língua, gotas)
    vão por cima, sem contorno, para ficarem finos;
  - as variantes de cor (gaivota, corvo, coelho da neve...) usam as MESMAS grelhas: só trocam as cores dos papéis;
  - o peixe é feito com as formas do motor (elipse rodada), porque muda de inclinação durante o salto.

Quadros de 16x16 (folhas: 8x8), virados para a DIREITA (o jogo espelha). Os bichos do chão ficam em baixo ao
centro, com os pés na penúltima linha; os que voam ficam ao centro do quadro.

Saída: arte/vida/<nome>_<anim>.png  (tira horizontal de quadros, fundo transparente)
Uso:   python3 ferramentas/arte/vida.py
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from motor import OUT, Parte, poligono, desenho_a_mao, desenhar, tira, previa_gif, hexrgb

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..')
PASTA = os.path.join(RAIZ, 'arte', 'vida')
PREVIA = '/tmp/claude-0/-home-user-jogo-01/1927e887-160f-5d34-9e8c-45231f72ddcb/scratchpad/vida_previa.gif'

SOLTO = set(':;!')      # letras desenhadas por cima, sem contorno (patas, antenas, língua, gotas)

# Paleta Resurrect 64 (para confirmar que não fugiu nenhuma cor).
R64 = set(('2e222f 3e3546 625565 966c6c ab947a 694f62 7f708a 9babb2 c7dcd0 ffffff 6e2727 b33831 '
           'ea4f36 f57d4a ae2334 e83b3b fb6b1d f79617 f9c22b 7a3045 9e4539 cd683d e6904e fbb954 4c3e24 676633 a2a947 '
           'd5e04b fbff86 165a4c 239063 1ebc73 91db69 cddf6c 313638 374e4a 547e64 92a984 b2ba90 0b5e65 0b8a8f 0eaf9b '
           '30e1b9 8ff8e2 323353 484a77 4d65b4 4d9be6 8fd3ff 45293f 6b3e75 905ea9 a884f3 eaaded 753c54 a24b6f cf657f '
           'ed8099 831c5d c32454 f04f78 f68181 fca790 fdcbb0').split())


# ---------------- ajudas ----------------

def _camadas(pose):
    """Uma pose é uma grelha (lista de linhas) ou um tuplo de grelhas (camadas, de trás para a frente)."""
    return list(pose) if isinstance(pose, tuple) else [pose]


def quadro(pose, cores, W, x0, y0):
    """Desenha uma pose num quadro WxW com o canto da grelha em (x0, y0)."""
    partes = []
    soltos = []
    for z, g in enumerate(_camadas(pose)):
        corpo = [''.join('.' if c in SOLTO else c for c in l) for l in g]
        if any(c not in '. ' for l in corpo for c in l):
            partes.append(desenho_a_mao(corpo, x0, y0, cores, z=z, separar=z > 0))
        for y, l in enumerate(g):
            for x, c in enumerate(l):
                if c in SOLTO:
                    soltos.append((x0 + x, y0 + y, cores[c]))
    img = desenhar(partes, W, W)
    for x, y, c in soltos:
        if 0 <= x < W and 0 <= y < W:
            img.putpixel((x, y), hexrgb(c) + (255,))
    return img


def animacao(poses, cores, W=16, modo='chao', dx=0, dy=0):
    """Faz os quadros de uma animação. Todas as poses partilham a mesma origem (o bicho não salta de lado):
    'chao'   -> a última linha das grelhas fica na penúltima linha do quadro (pés no chão), centrado na largura;
    'centro' -> as grelhas ficam ao centro do quadro (bichos que voam)."""
    larg = max(len(l) for p in poses for g in _camadas(p) for l in g)
    alt = max(len(g) for p in poses for g in _camadas(p))
    x0 = (W - larg) // 2 + dx
    y0 = (W - 1 - alt if modo == 'chao' else (W - alt) // 2) + dy
    out = []
    for p in poses:
        cam = []
        alt_pose = max(len(g) for g in _camadas(p))     # as camadas de uma pose alinham-se por cima
        for g in _camadas(p):
            linhas = [l.ljust(larg, '.') for l in g] + ['.' * larg] * (alt_pose - len(g))
            falta = alt - alt_pose
            cam.append(['.' * larg] * falta + linhas if modo == 'chao' else linhas + ['.' * larg] * falta)
        out.append(quadro(tuple(cam), cores, W, x0, y0))
    return out


SPRITES = {}     # nome_anim -> lista de quadros (por ordem de criação)


def juntar(nome, anims):
    for an, frames in anims.items():
        SPRITES[f'{nome}_{an}' if an else nome] = frames


# =====================================================================
# Borboletas (vistas de cima, de cabeça para cima: é assim que as asas melhor se leem num boneco tão
# pequeno; como são simétricas, o espelho do jogo não as muda)
#   3,4,5 asa (escuro -> claro), s mancha, b corpo, h cabeça, : antena
#   batida: abertas -> meio -> fechadas (juntas por cima do corpo, de lado) -> meio
# =====================================================================

BORB_ABERTA = [
    "..:...:..",
    "...:.:...",
    "44..h..44",
    "4554b4554",
    "4s44b44s4",
    ".444b444.",
    "..33b33..",
    ".3s3b3s3.",
    "..3.b.3..",
]
BORB_MEIA = [
    "..:...:..",
    "...:.:...",
    ".4..h..4.",
    ".454b454.",
    "..s4b4s..",
    "..44b44..",
    "...3b3...",
    "..s3b3s..",
    "....b....",
]
BORB_FECHADA = [
    "..:...:..",
    "...:.:...",
    "....h....",
    "...4b4...",
    "...5b4...",
    "...4b4...",
    "...3b3...",
    "...3b3...",
    "....b....",
]
BORB_BASE = {'b': '#3e3546', 'h': '#625565', ':': OUT}
BORBOLETAS = {
    'amarela': {'3': '#f79617', '4': '#f9c22b', '5': '#fbff86', 's': '#9e4539'},
    'azul':    {'3': '#4d65b4', '4': '#4d9be6', '5': '#8fd3ff', 's': '#323353'},
    'rosa':    {'3': '#f04f78', '4': '#f68181', '5': '#fdcbb0', 's': '#831c5d'},
}


def borboletas():
    for nome, c in BORBOLETAS.items():
        cores = dict(BORB_BASE, **c)
        juntar(f'borboleta_{nome}', {'voar': animacao([BORB_ABERTA, BORB_MEIA, BORB_FECHADA, BORB_MEIA], cores, modo='centro')})


# =====================================================================
# Pássaros (pardal + variantes de cor: gaivota, corvo, pássaro do céu)
#   a,b,c asa (escuro -> claro), 2..5 corpo, q,r barriga, k bico, t cauda, x olho, : patas
# =====================================================================

PASS_PARADO = [
    [
        "......454..",
        ".....45444.",
        ".....44x4kk",
        "tt..cc3444.",
        ".tabbc33rr.",
        "..abbbb3rr.",
        "...aabqrr..",
        ".....:.:...",
        ".....:.:...",
    ],
    [   # abana a cabeça e a cauda
        "...........",
        "t.....454..",
        "tt...45444.",
        ".t..c44x4kk",
        "..abbc33rr.",
        "..abbbb3rr.",
        "...aabqrr..",
        ".....:.:...",
        ".....:.:...",
    ],
]
PASS_BICAR = [
    PASS_PARADO[0],
    [   # baixa a cabeça
        ".............",
        ".............",
        "t......454...",
        "tt..cc45444..",
        ".tabbc44x4kk.",
        "..abbbb3rr...",
        "...aabqrr....",
        ".....:.:.....",
        ".....:.:.....",
    ],
    [   # bica o chão
        ".............",
        ".............",
        "t............",
        "tt..cc3......",
        ".tabbc334....",
        "..abbbb3454..",
        "...aabq45444.",
        ".....:.44x4k.",
        ".....:.:...k.",
    ],
]
PASS_CORPO_VOO = [
    "............",
    "............",
    "............",
    "........454.",
    "tt..33344x4k",
    ".t2334444q..",
    "...qqrrrr...",
    "............",
    "............",
    "............",
]
PASS_ASAS = [
    [   # asa em cima
        "..ab........",
        "..abc.......",
        "...abc......",
        "...abc......",
        "....bc......",
    ],
    [   # asa ao meio
        "............",
        "............",
        "............",
        "...aabc.....",
        "..aabbc.....",
        "....ab......",
    ],
    [   # asa em baixo
        "............",
        "............",
        "............",
        "............",
        "............",
        "....abc.....",
        "....abc.....",
        "...abc......",
        "...ab.......",
        "..ab........",
    ],
]
PASS_VOAR = [(PASS_CORPO_VOO, PASS_ASAS[0]), (PASS_CORPO_VOO, PASS_ASAS[1]),
             (PASS_CORPO_VOO, PASS_ASAS[2]), (PASS_CORPO_VOO, PASS_ASAS[1])]

PASSAROS = {
    'passaro': {   # pardal castanho
        'a': '#7a3045', 'b': '#9e4539', 'c': '#e6904e',
        '2': '#9e4539', '3': '#cd683d', '4': '#e6904e', '5': '#fbb954',
        'q': '#ab947a', 'r': '#fdcbb0', 'k': '#f9c22b', 't': '#7a3045', 'x': OUT, ':': '#9e4539',
    },
    'passaro_gaivota': {
        'a': '#625565', 'b': '#9babb2', 'c': '#c7dcd0',
        '2': '#9babb2', '3': '#c7dcd0', '4': '#ffffff', '5': '#ffffff',
        'q': '#c7dcd0', 'r': '#ffffff', 'k': '#f9c22b', 't': '#3e3546', 'x': OUT, ':': '#f79617',
    },
    'passaro_corvo': {
        'a': '#45293f', 'b': '#3e3546', 'c': '#625565',
        '2': '#3e3546', '3': '#3e3546', '4': '#625565', '5': '#7f708a',
        'q': '#3e3546', 'r': '#625565', 'k': '#9babb2', 't': '#45293f', 'x': '#c7dcd0', ':': '#3e3546',
    },
    'passaro_ceu': {
        'a': '#4d65b4', 'b': '#4d9be6', 'c': '#8fd3ff',
        '2': '#4d9be6', '3': '#8fd3ff', '4': '#c7dcd0', '5': '#ffffff',
        'q': '#c7dcd0', 'r': '#ffffff', 'k': '#f9c22b', 't': '#f9c22b', 'x': OUT, ':': '#4d65b4',
    },
}


def passaros():
    for nome, cores in PASSAROS.items():
        juntar(nome, {
            'voar': animacao(PASS_VOAR, cores, modo='centro'),
            'parado': animacao(PASS_PARADO, cores),
            'bicar': animacao(PASS_BICAR, cores),
        })


# =====================================================================
# Coelho (castanho-acinzentado) e lebre da neve
#   2..5 pelo, e ponta da orelha, p orelha por dentro, w cauda, x olho, n nariz
# =====================================================================

COELHO_PARADO = [
    [
        "....e..ee...",
        "....2..4p...",
        "....3..4p...",
        "....3..4p...",
        ".....45443..",
        "....344x44n.",
        "..33344443..",
        ".3453333....",
        "w3443333....",
        "w33333..4...",
        ".222222.44..",
    ],
    [   # a orelha de trás mexe-se e o nariz também
        "...e...ee...",
        "...2...4p...",
        "...3...4p...",
        "....3..4p...",
        ".....45443..",
        "....344x443n",
        "..33344443..",
        ".3453333....",
        "w3443333....",
        "w33333..4...",
        ".222222.44..",
    ],
]
COELHO_SALTAR = [
    [   # agacha-se
        "............",
        "............",
        "............",
        ".....e.ee...",
        ".....2.4p...",
        "......34p...",
        ".....45443..",
        "..33344x44n.",
        ".345333443..",
        "w34433334...",
        ".2222222.44.",
    ],
    [   # estica-se e sai do chão
        "..........ee.",
        "........e.4p.",
        ".........34p.",
        "........45443",
        "......3344x4n",
        "...334544443.",
        "..3453333.44.",
        "w34433332..4.",
        "w33333.......",
        "222..........",
        "2............",
    ],
    [   # no ar, encolhido
        "......e.ee..",
        "......2.4p..",
        ".......34p..",
        "......45443.",
        "...33344x44n",
        ".3453333443.",
        "w34433333...",
        "w3433332.4..",
        "..22222.....",
        "............",
        "............",
    ],
    [   # aterra
        "............",
        "............",
        "....e..ee...",
        "....2..4p...",
        ".....3.4p...",
        ".....45443..",
        "....344x44n.",
        "..33344443..",
        "w34533333...",
        "w3443333.4..",
        ".2222222.44.",
    ],
]
COELHOS = {
    'coelho': {
        '2': '#694f62', '3': '#966c6c', '4': '#ab947a', '5': '#ab947a', 'e': '#694f62',
        'p': '#f68181', 'w': '#ffffff', 'x': OUT, 'n': '#f04f78',
    },
    'coelho_neve': {
        '2': '#9babb2', '3': '#c7dcd0', '4': '#ffffff', '5': '#ffffff', 'e': '#625565',
        'p': '#fca790', 'w': '#ffffff', 'x': OUT, 'n': '#f68181',
    },
}


def coelhos():
    for nome, cores in COELHOS.items():
        juntar(nome, {'parado': animacao(COELHO_PARADO, cores), 'saltar': animacao(COELHO_SALTAR, cores)})


# =====================================================================
# Morcego (visto de frente, com a cabeça um pouco virada para a direita)
#   a,b asa (membrana), 2..5 corpo, R olho vermelho
# =====================================================================

MORC_CORPO = [
    ".............",
    ".............",
    ".....2..2....",
    ".....3443....",
    ".....4R4R....",
    ".....3443....",
    "......33.....",
]
MORC_ASAS = [
    [   # asas em cima
        ".............",
        "a...........a",
        "ab.........ba",
        "abb.......bba",
        ".abbb...bbba.",
        "..abb...bba..",
        "..a.b...b.a..",
    ],
    [   # asas ao meio
        ".............",
        ".............",
        ".............",
        ".............",
        "..abb...bba..",
        "aabbb...bbbaa",
        ".a.ab...ba.a.",
    ],
    [   # asas em baixo
        ".............",
        ".............",
        ".............",
        ".............",
        "....b...b....",
        "...abb.bba...",
        "..abbb.bbba..",
        ".abb.a.a.bba.",
        ".ab.......ba.",
        "a...........a",
    ],
]
MORC_CORES = {'a': '#45293f', 'b': '#6b3e75', '2': '#45293f', '3': '#6b3e75', '4': '#905ea9', '5': '#a884f3',
              'R': '#e83b3b'}


def morcego():
    poses = [(a, MORC_CORPO) for a in (MORC_ASAS[0], MORC_ASAS[1], MORC_ASAS[2], MORC_ASAS[1])]
    juntar('morcego', {'voar': animacao(poses, MORC_CORES, modo='centro')})


# =====================================================================
# Libelinha (vista de cima; as asas claras dão ideia de transparência e alternam para parecer um borrão)
#   2..5 corpo turquesa, E olho, w,W asa
# =====================================================================

LIB_CORPO = [
    "..............",
    "..............",
    "..............",
    "..........45..",
    "2233344444355E",
    "..........33..",
    "..............",
    "..............",
    "..............",
]
LIB_ASAS = [
    [   # asas abertas
        "......W..W....",
        "......w..ww...",
        ".....ww..ww...",
        ".....ww..w....",
        "..............",
        ".....ww..w....",
        ".....ww..ww...",
        "......w..ww...",
        "......W..W....",
    ],
    [   # asas a bater (borrão)
        "..............",
        "....WW..WW....",
        "....www.www...",
        "......vv.vv...",
        "..............",
        "......vv.vv...",
        "....www.www...",
        "....WW..WW....",
        "..............",
    ],
]
LIB_CORES = {'2': '#0b8a8f', '3': '#0eaf9b', '4': '#30e1b9', '5': '#8ff8e2', 'E': '#0b5e65',
             'w': '#c7dcd0', 'W': '#ffffff', 'v': '#8fd3ff'}


def libelinha():
    poses = [(LIB_ASAS[0], LIB_CORPO), (LIB_ASAS[1], LIB_CORPO)]
    juntar('libelinha', {'voar': animacao(poses, LIB_CORES, modo='centro')})


# =====================================================================
# Sapo
#   2..5 verde, m boca, r barriga, x olho, w brilho do olho, g papo (claro), G brilho do papo
# =====================================================================

SAPO_PARADO = [
    [
        "......55.55.",
        ".....4wx4wx.",
        "...334444444",
        "..3444444443",
        ".344444mmmm.",
        ".3.33rrrrrr.",
        "343.3rrrr3..",
        "2222.2...2..",
    ],
    [   # incha o papo
        "......55.55.",
        ".....4wx4wx.",
        "...334444444",
        "..3444444443",
        ".344444mmmm.",
        ".3.33rGGggg.",
        "343.3rggggg.",
        "2222.2.ggg..",
    ],
]
SAPO_SALTAR = [
    [   # agacha-se
        "............",
        "............",
        "......55.55.",
        ".....4wx4wx.",
        "..3344444444",
        ".344444mmmm4",
        "3433rrrrrr3.",
        "2222.....22.",
    ],
    [   # salta, todo esticado
        "........55.55",
        ".......4wx4wx",
        "......3444444",
        "....334444mm.",
        "..3334rrrr...",
        ".22.......4..",
        "2.........4..",
        ".............",
    ],
    [   # aterra
        "............",
        ".....55.55..",
        "....4wx4wx..",
        "..334444444.",
        ".33444444444",
        "334444mmmm4.",
        "33.3rrrrr3..",
        "22..22..22..",
    ],
]
SAPO_CORES = {'2': '#165a4c', '3': '#239063', '4': '#1ebc73', '5': '#91db69', 'm': OUT, 'r': '#cddf6c',
              'x': OUT, 'w': '#ffffff', 'g': '#cddf6c', 'G': '#fbff86'}


def sapo():
    juntar('sapo', {'parado': animacao(SAPO_PARADO, SAPO_CORES), 'saltar': animacao(SAPO_SALTAR, SAPO_CORES)})


# =====================================================================
# Lagarto (da areia) e salamandra de fogo
#   2..5 corpo, m manchas, r barriga, x olho, ! língua, : nada
# =====================================================================

LAG_PARADO = [
    [
        ".........445.",
        "..33m3m3344x4",
        "233rrrrrr4444",
        "....3....3...",
        "...33...33...",
    ],
    [   # levanta a cabeça e deita a língua de fora
        ".........4454",
        "..33m3m334x44!",
        "233rrrrrr444..",
        "....3....3....",
        "...33...33....",
    ],
]
LAG_CORRER = [
    [
        ".........445.",
        "..33m3m3344x4",
        "233rrrrrr4444",
        "...3.....3...",
        "..33......33.",
    ],
    [
        ".........445.",
        "2.33m3m3344x4",
        ".33rrrrrr4444",
        "....3...3....",
        "....33..33...",
    ],
    [
        ".........445.",
        "..33m3m3344x4",
        "233rrrrrr4444",
        ".....3.3.....",
        ".....3.33....",
    ],
    [
        ".........445.",
        "..33m3m3344x4",
        ".33rrrrrr4444",
        "2...3...3....",
        "....33..33...",
    ],
]
LAGARTOS = {
    'lagarto': {'2': '#9e4539', '3': '#cd683d', '4': '#e6904e', '5': '#fbb954', 'm': '#9e4539', 'r': '#fbb954',
                'x': OUT, '!': '#f04f78'},
    'lagarto_fogo': {'2': '#6e2727', '3': '#b33831', '4': '#ea4f36', '5': '#f57d4a', 'm': '#f9c22b', 'r': '#f57d4a',
                     'x': OUT, '!': '#f9c22b'},
}


def lagartos():
    for nome, cores in LAGARTOS.items():
        juntar(nome, {'parado': animacao(LAG_PARADO, cores), 'correr': animacao(LAG_CORRER, cores)})


# =====================================================================
# Caranguejo (de lado, a andar de lado)
#   2..5 carapaça, w olho (branco), x pupila, : patas
# =====================================================================

CARANG_A = [
    ".4.......4.",
    "45.w...w.45",
    ".3.x...x.3.",
    "..3454443..",
    ".3344444433",
    "..2333332..",
    ".:.:...:.:.",
]
CARANG_B = [
    "...........",
    "45.w...w.45",
    "43.x...x.34",
    "..3454443..",
    ".3344444433",
    "..2333332..",
    "..:.:.:.:..",
]
CARANG_CORES = {'2': '#6e2727', '3': '#b33831', '4': '#ea4f36', '5': '#f57d4a', 'w': '#ffffff', 'x': OUT,
                ':': '#6e2727'}


def caranguejo():
    juntar('caranguejo', {'andar': animacao([CARANG_A, CARANG_B, CARANG_A, CARANG_B], CARANG_CORES)})


# =====================================================================
# Peixe a saltar fora de água (formas do motor: elipse rodada + cauda + barbatana)
# =====================================================================

PEIXE_CORPO = ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff']
PEIXE_BARRIGA = ['#7f708a', '#9babb2', '#c7dcd0', '#ffffff', '#ffffff']
PEIXE_BARB = ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#4d9be6']
AGUA = ['#4d9be6', '#8fd3ff', '#ffffff']


def _rodar(cx, cy, ang):
    c, s = math.cos(ang), math.sin(ang)
    return lambda u, v: (cx + u * c - v * s, cy + u * s + v * c)


def peixe_pose(cx, cy, graus, gotas=()):
    """Peixe com o centro em (cx, cy), inclinado 'graus' (negativo = nariz para cima)."""
    P = _rodar(cx, cy, math.radians(graus))
    corpo = set()
    barriga = set()
    c, s = math.cos(math.radians(graus)), math.sin(math.radians(graus))
    for y in range(16):
        for x in range(16):
            dx, dy = x + .5 - cx, y + .5 - cy
            u, v = dx * c + dy * s, -dx * s + dy * c
            if (u / 4.0) ** 2 + (v / 2.1) ** 2 <= 1:
                corpo.add((x, y))
                if v > 0.75:
                    barriga.add((x, y))
    cauda = poligono([P(-3.2, 0), P(-6.4, -2.6), P(-5.4, 0), P(-6.4, 2.6)])
    dorsal = poligono([P(-1.4, -1.5), P(1.0, -1.5), P(-1.6, -3.1)])
    olho = P(2.0, -0.5)
    partes = [
        Parte(cauda, PEIXE_BARB, z=0),
        Parte(dorsal, PEIXE_BARB, z=0.5, plano=True),
        Parte(corpo, PEIXE_CORPO, z=1),
        Parte(barriga, PEIXE_BARRIGA, z=1.5, separar=False, plano=True),
        Parte({(int(olho[0]), int(olho[1]))}, None, z=2, separar=False, cor=OUT),
    ]
    img = desenhar(partes, 16, 16)
    for x, y, i in gotas:
        img.putpixel((x, y), hexrgb(AGUA[i]) + (255,))
    return img


def salpico():
    """Último quadro: o peixe voltou a entrar na água; ficam gotas a saltar e um anel de água (sem contorno)."""
    img = desenhar([], 16, 16)
    claras = [(9, 14), (10, 14), (11, 14), (12, 14), (8, 13), (13, 13), (10, 11), (11, 10), (9, 9), (12, 8)]
    medias = [(7, 14), (14, 14), (7, 12), (14, 12), (8, 10), (13, 10), (10, 8)]
    brancas = [(11, 12), (9, 11), (12, 11), (10, 13), (11, 13)]
    for lista, cor in ((medias, '#4d9be6'), (claras, '#8fd3ff'), (brancas, '#ffffff')):
        for x, y in lista:
            img.putpixel((x, y), hexrgb(cor) + (255,))
    return img


def peixe():
    frames = [
        peixe_pose(6.0, 9.5, -42, gotas=[(2, 14, 1), (4, 13, 2), (1, 12, 0)]),
        peixe_pose(8.5, 5.5, 0),
        peixe_pose(11.0, 9.5, 42),
        salpico(),
    ]
    juntar('peixe', {'saltar': frames})


# =====================================================================
# Folhas e pétalas a cair (8x8): rodam e viram-se enquanto caem
#   2..5 folha (escuro -> claro), v nervura
# =====================================================================

FOLHA = [
    [   # de frente, inclinada
        "...45",
        "..454",
        ".4v43",
        "4v33.",
        "v2...",
    ],
    [   # a rodar
        ".....",
        "..445",
        "44v43",
        "3332.",
        ".....",
    ],
    [   # de lado (fina)
        ".....",
        ".....",
        "4433v",
        ".....",
        ".....",
    ],
    [   # virada ao contrário (mostra o lado de baixo, mais escuro)
        "v....",
        "23...",
        "3v33.",
        ".3v32",
        "..332",
    ],
]
FOLHAS = {
    'verde':   {'2': '#165a4c', '3': '#239063', '4': '#1ebc73', '5': '#91db69', 'v': '#165a4c'},
    'laranja': {'2': '#9e4539', '3': '#cd683d', '4': '#f79617', '5': '#f9c22b', 'v': '#9e4539'},
    'rosa':    {'2': '#c32454', '3': '#f04f78', '4': '#f68181', '5': '#fdcbb0', 'v': '#c32454'},
}


def folhas():
    for nome, cores in FOLHAS.items():
        juntar(f'folha_cair_{nome}', {'': animacao(FOLHA, cores, W=8, modo='centro')})


# ---------------- gravar e verificar ----------------

def gravar():
    os.makedirs(PASTA, exist_ok=True)
    for nome, frames in SPRITES.items():
        tira(frames).save(os.path.join(PASTA, f'{nome}.png'))


def verificar():
    """Confirma tamanhos, fundo transparente, quadros não vazios e cores da Resurrect 64."""
    erros = []
    for nome, frames in SPRITES.items():
        W = frames[0].size[0]
        for i, f in enumerate(frames):
            if f.size != (W, W):
                erros.append(f'{nome}: quadro {i} com tamanho {f.size}')
            px = f.load()
            for y in range(W):
                for x in range(W):
                    r, g, b, a = px[x, y]
                    if a not in (0, 255):
                        erros.append(f'{nome}: píxel meio transparente')
                    if a and '%02x%02x%02x' % (r, g, b) not in R64:
                        erros.append(f'{nome}: cor fora da paleta #{r:02x}{g:02x}{b:02x}')
            if not f.getbbox():
                erros.append(f'{nome}: quadro {i} vazio')
    for e in sorted(set(erros)):
        print('  ERRO', e)
    return not erros


def previas():
    """GIF a mexer com todas as animações (16x16 num GIF, folhas 8x8 noutro).
    Cada linha junta as animações de um ou mais bichos inteiros (até 6 por linha)."""
    bichos = {}
    for nome, frames in SPRITES.items():
        if frames[0].size[0] == 16:
            bichos.setdefault(nome.rsplit('_', 1)[0], []).append(frames)
    linhas = [[]]
    for anims in bichos.values():
        if len(linhas[-1]) + len(anims) > 6:
            linhas.append([])
        linhas[-1].extend(anims)
    previa_gif(linhas, PREVIA, escala=6, fundo=(84, 126, 100), ms=140)
    pequenas = [[frames for frames in SPRITES.values() if frames[0].size[0] == 8]]
    previa_gif(pequenas, PREVIA.replace('.gif', '_folhas.gif'), escala=6, fundo=(84, 126, 100), ms=140)


if __name__ == '__main__':
    borboletas()
    passaros()
    coelhos()
    morcego()
    libelinha()
    sapo()
    lagartos()
    caranguejo()
    peixe()
    folhas()
    gravar()
    print('ok' if verificar() else 'com erros', len(SPRITES), 'animações em', os.path.normpath(PASTA))
    previas()
