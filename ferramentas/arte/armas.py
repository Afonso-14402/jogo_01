"""Armas: sprite vertical (a apontar para cima, punho no centro em baixo) + ícone 16x16 na diagonal.
Regras: docs/ARTE.md, secção 4. Tipos e tamanhos: docs/ARMAS.md.

Cada TIPO de arma é desenhado píxel a píxel (lâmina com 3–5 tons e brilho, guarda, punho enrolado, pomo),
com contorno escuro automático; o ícone 16x16 é desenhado à parte, na diagonal.
Os materiais (rampas do motor) mudam as cores: o mesmo gerador faz as armas de todas as regiões.

Uso: python3 ferramentas/arte/armas.py [regiao] [previa.png]
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image
from motor import Parte, elipse, desenhar, RAMPAS

TAM = {'espada': 32, 'espada_grande': 48, 'adaga': 32, 'katana': 48, 'machado': 32, 'martelo': 48,
       'lanca': 48, 'foice': 48, 'arco': 32, 'besta': 32, 'cajado': 48, 'manoplas': 32}


# ---------- desenho píxel a píxel ----------
# Cada arma pinta-se com LETRAS (tons das rampas) e no fim leva contorno escuro automático:
#   1..5 = metal (escuro -> claro) · a..e = cabo · p q r = punho (couro enrolado) · x y z w = enfeite · W = brilho
#   S = corda (arco/besta)
OUT = '#2e222f'


class Pix:
    def __init__(self, W):
        self.W = W
        self.p = {}

    def put(self, x, y, ch):
        x, y = int(round(x)), int(round(y))
        if 0 <= x < self.W and 0 <= y < self.W:
            self.p[(x, y)] = ch

    def vband(self, xc, y0, y1, cores):
        """Faixa vertical: cores da esquerda (luz) para a direita (sombra)."""
        x0 = xc - (len(cores) - 1) // 2
        for y in range(y0, y1 + 1):
            for i, ch in enumerate(cores):
                self.put(x0 + i, y, ch)

    def dband(self, x0, y0, n, cores):
        """Faixa na diagonal (para cima e para a direita): cores[0] do lado da luz (cima-esquerda)."""
        for i in range(n):
            x, y = x0 + i, y0 - i
            for k, ch in enumerate(cores):
                # k=0 centro; 1 = lado da luz; 2 = lado da sombra; 3 = mais luz
                dx, dy = [(0, 0), (-1, 0), (0, 1), (-1, -1)][k]
                self.put(x + dx, y + dy, ch)

    def blob(self, cx, cy, rx, ry, tons, filtro=None):
        """Mancha com luz de cima à esquerda: tons = 5 letras (escuro -> claro)."""
        for y in range(int(cy - ry) - 1, int(cy + ry) + 2):
            for x in range(int(cx - rx) - 1, int(cx + rx) + 2):
                u, v = (x + .5 - cx) / rx, (y + .5 - cy) / ry
                if u * u + v * v <= 1 and (filtro is None or filtro(x, y)):
                    i = -0.7 * u - 0.9 * v + (0.3 if u * u + v * v < 0.35 else -0.2)
                    self.put(x, y, tons[4 if i > 0.9 else 3 if i > 0.3 else 2 if i > -0.3 else 1 if i > -0.9 else 0])

    def imagem(self, m):
        M, C, P, E = (_rampa(m[k]) for k in ('metal', 'cabo', 'punho', 'enfeite'))
        cor = {'1': M[0], '2': M[1], '3': M[2], '4': M[3], '5': M[4], 'a': C[0], 'b': C[1], 'c': C[2], 'd': C[3],
               'e': C[4], 'p': P[1], 'q': P[2], 'r': P[3], 'x': E[1], 'y': E[2], 'z': E[3], 'w': E[4],
               'W': '#ffffff', 'S': '#c7dcd0', 'o': OUT}
        im = Image.new('RGBA', (self.W, self.W))
        borda = {(x + dx, y + dy) for (x, y) in self.p for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))} - set(self.p)
        for (x, y) in borda:
            if 0 <= x < self.W and 0 <= y < self.W:
                im.putpixel((x, y), _hex(OUT))
        for (x, y), ch in self.p.items():
            im.putpixel((x, y), _hex(cor[ch]))
        return im


def _hex(c):
    return tuple(int(c[i:i + 2], 16) for i in (1, 3, 5)) + (255,)


def _rampa(r):
    return RAMPAS[r] if isinstance(r, str) else r


METAL = '12345'
ENF = 'xxyzw'
CABO = 'abcde'


def _punho(P, xc, y0, y1, larg=3):
    for y in range(y0, y1 + 1):
        linha = ['r', 'q', 'p'] if (y - y0) % 2 == 0 else ['q', 'p', 'p']
        P.vband(xc, y, y, linha[:larg])


def _lamina(P, xc, y0, y1, cores, brilho=True):
    P.vband(xc, y0, y1, cores)
    n = len(cores)
    x0 = xc - (n - 1) // 2
    # ponta afiada
    for k in range(1, (n + 1) // 2 + 1):
        lo, hi = k, n - 1 - k
        if lo <= hi:
            for i in range(lo, hi + 1):
                P.put(x0 + i, y0 - k, cores[i])
        else:
            P.put(x0 + (n - 1) // 2, y0 - k, cores[(n - 1) // 2])
    if brilho:
        P.put(x0, y0 + 3, 'W')


def sprite(tipo, m):
    W = TAM[tipo]
    P = Pix(W)
    c = W // 2
    b = W - 2   # última linha com desenho (a de baixo é o contorno)
    if tipo == 'espada':
        P.blob(c, b - 1, 1.6, 1.4, ENF)
        _punho(P, c, b - 7, b - 3)
        P.vband(c, b - 9, b - 9, 'wzzzzzzyx')
        P.vband(c, b - 8, b - 8, 'zyyyyyyxx')
        _lamina(P, c, 4, b - 10, '542')
    elif tipo == 'espada_grande':
        P.blob(c, b - 1, 2.0, 1.6, ENF)
        _punho(P, c, b - 10, b - 3)
        P.vband(c, b - 12, b - 12, 'wzzzzzzzzzzyx')
        P.vband(c, b - 11, b - 11, 'zyyyyyyyyyyxx')
        P.put(c - 6, b - 10, 'y'); P.put(c + 6, b - 10, 'x')
        _lamina(P, c, 6, b - 13, '54432')
        P.vband(c, 10, b - 16, '3')   # sulco no meio da lâmina
    elif tipo == 'adaga':
        P.blob(c, b - 1, 1.4, 1.2, ENF)
        _punho(P, c, b - 5, b - 2, 2)
        P.vband(c, b - 7, b - 7, 'wzzzzyx')
        P.vband(c, b - 6, b - 6, 'yyyyyxx')
        _lamina(P, c, b - 19, b - 8, '542')
    elif tipo == 'katana':
        P.vband(c, b - 1, b, 'zy')
        for y in range(b - 14, b - 1):
            P.vband(c, y, y, 'rp' if (y // 2) % 2 else 'pr')
        P.blob(c, b - 15.5, 3.2, 1.3, ENF)
        P.vband(c, b - 17, b - 17, 'wz')
        for y in range(4, b - 17):
            curva = int(round(((b - 17 - y) / (b - 21)) ** 2 * 2.5))
            P.vband(c + curva, y, y, '53')
        P.put(c + 3, 3, '4'); P.put(c + 3, 2, '5')
    elif tipo == 'machado':
        P.vband(c, 5, b, 'cb')
        _punho(P, c, b - 6, b, 2)
        cx0 = c + 1
        for x in range(cx0, cx0 + 9):
            meia = 2 + (x - cx0) * 0.55
            for y in range(int(9 - meia), int(9 + meia) + 1):
                d = x - cx0
                ch = '5' if d >= 7 else '4' if y < 9 - meia + 1.5 else '2' if y > 9 + meia - 1.5 else '3'
                P.put(x, y, ch)
        for x, h in ((c - 1, 3), (c - 2, 2), (c - 3, 1)):
            for y in range(9 - h // 2 - 1, 9 + h // 2 + 1):
                P.put(x, y, '3' if y > 8 else '4')
        P.vband(c, 3, 4, 'y'); P.put(c, 2, 'z')
    elif tipo == 'martelo':
        P.vband(c, 14, b, 'cb')
        _punho(P, c, b - 9, b, 2)
        P.vband(c, 14, 15, 'zyx')
        for y in range(4, 14):
            for x in range(c - 6, c + 7):
                if (x in (c - 6, c + 6)) and y in (4, 13):
                    continue
                ch = '5' if y == 4 or x == c - 6 else '2' if y == 13 or x == c + 6 else '4' if y < 8 else '3'
                P.put(x, y, ch)
        P.vband(c, 8, 9, 'zzzzzzzzzzzzz')
    elif tipo == 'lanca':
        P.vband(c, 14, b, 'cb')
        _punho(P, c, b - 10, b - 4, 2)
        P.vband(c, 14, 15, 'wzy')
        for y in range(2, 14):
            meia = 2.6 * math.sin(math.pi * (y - 1) / 13)
            for x in range(int(round(c - meia)), int(round(c + meia)) + 1):
                P.put(x, y, '5' if x < c - meia + 1.2 else '2' if x > c + meia - 1.2 else '4')
        for y in range(16, 22):
            P.put(c - 2 - (y - 16) // 3, y, 'x' if y % 2 else 'y')
    elif tipo == 'foice':
        P.vband(c, 7, b, 'cb')
        _punho(P, c, b - 10, b - 4, 2)
        P.vband(c, 5, 7, 'zy')
        for i in range(14):
            x = c - 1 - i
            ytop = 4 + (i / 13) ** 2 * 7
            esp = max(1, round(3 - i * 0.16))
            for k in range(esp):
                P.put(x, ytop + k, '5' if k == 0 else '2' if k == esp - 1 and esp > 1 else '4')
    elif tipo == 'arco':
        for y in range(2, W - 2):
            u = (y - (W - 1) / 2) / ((W - 4) / 2)
            x = c + 2 - round(5 * (1 - u * u))
            P.put(x, y, 'd' if u < 0 else 'c'); P.put(x + 1, y, 'b')
            P.put(c + 3, y, 'S')
        _punho(P, c - 3, W // 2 - 3, W // 2 + 2, 2)
        for y in (2, 3, W - 4, W - 3):
            P.put(c + 2, y, 'z')
    elif tipo == 'besta':
        P.vband(c, 7, b, 'dcb')
        _punho(P, c, b - 7, b - 1, 3)
        for x in range(c - 11, c + 12):
            u = (x - c) / 11
            y = 7 + round(3 * u * u)
            P.put(x, y, '4'); P.put(x, y + 1, '2')
        for i in range(12):
            P.put(c - 11 + i, 9 + round(i * 0.5), 'S'); P.put(c + 11 - i, 9 + round(i * 0.5), 'S')
        P.vband(c, 4, 6, '5'); P.put(c, 3, '4')
        P.put(c + 2, b - 9, 'z'); P.put(c + 2, b - 8, 'y')
    elif tipo == 'cajado':
        P.vband(c, 12, b, 'cb')
        for y in (20, 30, 40):
            if y < b:
                P.vband(c, y, y, 'dc')
        P.blob(c, 7, 3.4, 3.4, ENF)
        P.put(c - 1, 5, 'W')
        for y in range(6, 13):
            P.put(c - 4 - (1 if y < 9 else 0), y, '4' if y < 10 else '3')
            P.put(c + 4 + (1 if y < 9 else 0), y, '3' if y < 10 else '2')
        P.vband(c, 11, 12, '424')
    return P.imagem(m)


def icone(tipo, m):
    P = Pix(16)
    if tipo in ('espada', 'espada_grande', 'adaga', 'katana'):
        n = {'espada': 8, 'espada_grande': 9, 'adaga': 5, 'katana': 9}[tipo]
        cores = {'espada': '452', 'espada_grande': '4525', 'adaga': '452', 'katana': '42'}[tipo]
        P.dband(6, 9, n, cores)
        P.put(6 + n, 9 - n, '5')
        g = {'katana': 1, 'adaga': 1}.get(tipo, 2)
        for k in range(-g, g + 1):
            P.put(5 + k, 10 + k, 'w' if k == -g else 'z')
        if tipo == 'katana':
            P.put(4, 10, 'y'); P.put(5, 11, 'y')
        for i in range(1, 3 if tipo != 'katana' else 4):
            P.put(5 - i, 10 + i, 'q' if i % 2 else 'p')
            P.put(5 - i + 1, 10 + i, 'p')
        P.blob(5 - (3 if tipo != 'katana' else 4) + 0.5, 10 + (3 if tipo != 'katana' else 4) + 0.5, 1.2, 1.2, ENF)
    elif tipo in ('machado', 'martelo', 'lanca', 'foice', 'cajado', 'besta'):
        fim = {'machado': 9, 'martelo': 8, 'lanca': 10, 'foice': 11, 'cajado': 9, 'besta': 9}[tipo]
        P.dband(2, 14, fim, 'cb' if tipo != 'besta' else 'dcb')
        P.put(2, 14, 'q'); P.put(3, 13, 'p'); P.put(4, 12, 'q')
        if tipo == 'machado':
            P.blob(12, 4, 3.6, 3.6, METAL, lambda x, y: (x - 12) - (y - 4) > -2.5)
            P.put(9, 6, 'z'); P.put(10, 7, 'y')
        elif tipo == 'martelo':
            for y in range(1, 7):
                for x in range(9, 15):
                    if (x, y) not in ((9, 1), (14, 6)):
                        P.put(x, y, '5' if y == 1 or x == 9 else '2' if y == 6 or x == 14 else '4' if x + y < 16 else '3')
            P.put(9, 7, 'z'); P.put(8, 7, 'y')
        elif tipo == 'lanca':
            P.dband(11, 4, 3, '452')
            P.put(14, 1, '5')
            P.put(10, 5, 'z'); P.put(11, 6, 'y'); P.put(9, 4, 'w')
        elif tipo == 'foice':
            for i, (x, y) in enumerate(((12, 2), (11, 2), (10, 2), (9, 2), (8, 3), (7, 3), (6, 4), (5, 5))):
                P.put(x, y, '5'); P.put(x, y + 1, '4' if i < 5 else '2')
            P.put(12, 1, '4')
        elif tipo == 'cajado':
            P.blob(12.5, 3.5, 2.6, 2.6, ENF)
            P.put(12, 2, 'W')
            P.put(9, 3, '4'); P.put(9, 4, '3'); P.put(13, 7, '3'); P.put(12, 7, '2')
        elif tipo == 'besta':
            for k in range(-5, 6):   # o arco da besta, de través
                P.put(10 + k, 6 + k, '4' if k < 0 else '2')
            P.put(12, 3, '5'); P.put(13, 2, '4')
    elif tipo == 'arco':
        for t in range(0, 26):
            ang = math.pi * 1.0 + (math.pi / 2) * t / 25
            x, y = 13 + 11.3 * math.cos(ang), 13 + 11.3 * math.sin(ang)
            P.put(x, y, 'c')
        for i in range(10):
            P.put(2 + i, 11 - i, 'S')
        P.put(4, 4, 'q'); P.put(5, 3, 'q'); P.put(3, 5, 'p')
        P.put(2, 12, 'z'); P.put(12, 2, 'z')
    return P.imagem(m)


def manoplas(m, W=32, ic=False):
    """As manoplas não têm eixo: desenha-se o punho fechado."""
    k = 1.0 if not ic else 0.5
    o = 0 if not ic else -0.5
    P = [Parte(elipse((16 + o) * k, (24 + o) * k, 7 * k, 5 * k), _rampa(m['punho']), z=1),
         Parte(elipse((16 + o) * k, (15 + o) * k, 8.5 * k, 7.5 * k), _rampa(m['metal']), z=2)]
    for dx in (-5, -1.7, 1.7, 5):
        P.append(Parte(elipse((16 + dx + o) * k, (9.5 + o) * k, 1.9 * k, 1.9 * k), _rampa(m['enfeite']), z=3))
    P.append(Parte(elipse((22.5 + o) * k, (17 + o) * k, 2.4 * k, 3.5 * k), _rampa(m['metal']), z=3))
    return desenhar(P, W if not ic else 16, W if not ic else 16)


def fazer(tipo, m):
    if tipo == 'manoplas':
        return manoplas(m), manoplas(m, ic=True)
    return sprite(tipo, m), icone(tipo, m)


# ---------- as armas de cada região ----------

def mat(metal, cabo='madeira', punho='couro', enfeite=None):
    return {'metal': metal, 'cabo': cabo, 'punho': punho, 'enfeite': enfeite or metal}


TIPOS_NORMAIS = ['espada', 'espada_grande', 'adaga', 'katana', 'machado', 'martelo', 'lanca', 'foice', 'arco', 'besta', 'cajado', 'manoplas']


def normais(material_id, metal, gema='verde'):
    out = {}
    for t in TIPOS_NORMAIS:
        m = mat(metal)
        if t == 'cajado':
            m['enfeite'] = gema
        if t in ('arco',):
            m['cabo'] = 'madeira'
        out[f'{t}_{material_id}'] = (t, m)
    return out


REGIOES = {
    1: dict(pasta='r01', normais=('cobre', 'cobre', 'verde'), especiais={
        # únicas dos bosses
        'presa_javali_rei': ('machado', mat('branco', 'madeira', 'couro', 'castanho')),
        'raiz_ancestral': ('cajado', mat('madeira', ['#2e222f', '#4c3e24', '#694f62', '#966c6c', '#ab947a'], 'verde_esc', 'verde')),
        # dos guardiões
        'chifre_partido': ('adaga', mat('branco', 'madeira', 'couro', 'castanho')),
        'pena_noturna': ('arco', mat('preto', 'preto', 'roxo', 'roxo')),
        'martelo_pinca': ('martelo', mat('vermelho', 'madeira', 'couro', 'laranja')),
        'esporo_luz': ('cajado', mat('vermelho', 'branco', 'branco', 'musgo')),
        'ferrao_de_mel': ('lanca', mat('amarelo', 'madeira', 'castanho', 'preto')),
        'tronco_velho': ('espada_grande', mat('madeira', 'madeira', 'verde_esc', 'verde_esc')),
        'lamina_cavaleiro_esquecido': ('espada', mat('ferro', 'madeira', 'couro', 'verde_esc')),
        'foice_bruma': ('foice', mat('branco', 'cinza', 'agua', 'agua')),
        # secreta
        'espada_treino': ('espada', mat('madeira', 'madeira', 'couro', 'madeira')),
        'arco_curto_carvalho': ('arco', mat('madeira', 'madeira', 'couro', 'castanho')),
        'arco_raiz_viva': ('arco', mat('verde', ['#2e222f', '#4c3e24', '#694f62', '#966c6c', '#ab947a'], 'verde', 'verde')),
    }),
}

REGIOES.update({
    2: dict(normais=('ferro', 'ferro', 'agua'), especiais={
        'presa_venenosa': ('adaga', mat('branco', 'roxo', 'roxo', 'verde')),
        'nucleo_cristal': ('martelo', mat('agua', 'cinza', 'couro', 'lilas')),
        'martelo_carril': ('martelo', mat('ferro', 'madeira', 'couro', 'laranja')),
        'chifre_picareta': ('machado', mat('branco', 'madeira', 'couro', 'castanho')),
        'cajado_prisma': ('cajado', mat('agua', 'branco', 'lilas', 'lilas')),
        'remo_barqueiro': ('lanca', mat('madeira', 'madeira', 'verde_esc', 'verde')),
        'foice_micelio': ('foice', mat('rosa', 'branco', 'rosa', 'amarelo')),
        'besta_ressonante': ('besta', mat('roxo', 'madeira', 'couro', 'lilas')),
        'manoplas_fornalha': ('manoplas', mat('cobre', 'cobre', 'couro', 'laranja')),
        'lamina_reflexo': ('katana', mat('preto', 'preto', 'roxo', 'roxo')),
        'machado_rei_montanha': ('machado', mat('ouro', 'madeira', 'vermelho', 'agua')),
        'martelo_vagoneta': ('martelo', mat('ferro', 'madeira', 'couro', 'cobre')),
    }),
    3: dict(normais=('aco', 'cinza', 'verde'), especiais={
        'lingua_serpente': ('lanca', mat('musgo', 'verde_esc', 'couro', 'vermelho')),
        'arco_hidra': ('arco', mat('verde', 'verde_esc', 'roxo', 'amarelo')),
        'bico_garca': ('lanca', mat('amarelo', 'cinza', 'couro', 'branco')),
        'cajado_lodoso': ('cajado', mat('verde', 'castanho', 'verde', 'verde')),
        'garras_jade': ('manoplas', mat('verde_esc', 'verde_esc', 'couro', 'agua')),
        'machado_totemico': ('machado', mat('madeira', 'vermelho', 'verde', 'vermelho')),
        'pinca_maior': ('espada_grande', mat('laranja', 'laranja', 'couro', 'amarelo')),
        'arco_cascata': ('arco', mat('agua', 'azul', 'agua', 'branco')),
        'martelo_bugio': ('martelo', mat('castanho', 'madeira', 'couro', 'vermelho')),
        'foice_espinhos': ('foice', mat('verde_esc', 'castanho', 'verde', 'vermelho')),
        'katana_garra_sol': ('katana', mat('ouro', 'preto', 'vermelho', 'amarelo')),
        'lanca_tribal_aco': ('lanca', mat('cinza', 'madeira', 'verde', 'vermelho')),
        'lanca_ssark': ('lanca', mat('cinza', 'madeira', 'vermelho', 'amarelo')),
        'arco_tribal_aco': ('arco', mat('cinza', 'madeira', 'verde', 'vermelho')),
    }),
    4: dict(normais=('prata', 'branco', 'azul'), especiais={
        'ferrao_imperial': ('besta', mat('ouro', 'preto', 'preto', 'azul')),
        'khopesh_farao': ('espada', mat('ouro', 'azul', 'azul', 'agua')),
        'espinho_duna': ('adaga', mat('amarelo', 'castanho', 'couro', 'laranja')),
        'cajado_miragem': ('cajado', mat('agua', 'branco', 'agua', 'agua')),
        'arco_abutre': ('arco', mat('castanho', 'castanho', 'rosa', 'ouro')),
        'martelo_arenito': ('martelo', mat('amarelo', 'madeira', 'couro', 'laranja')),
        'cimitarra_vento': ('espada', mat('agua', 'azul', 'branco', 'branco')),
        'lanca_cavaleiro_ossos': ('lanca', mat('branco', 'branco', 'cinza', 'vermelho')),
        'garras_esfinge': ('manoplas', mat('amarelo', 'amarelo', 'castanho', 'agua')),
        'foice_ouro_sacerdote': ('foice', mat('ouro', 'preto', 'preto', 'agua')),
        'espada_grande_osso_dragao': ('espada_grande', mat('branco', 'cinza', 'couro', 'azul')),
        'cimitarra_sultao': ('espada', mat('ouro', 'vermelho', 'vermelho', 'vermelho')),
        'cimitarra_velha_prata': ('espada', mat('branco', 'castanho', 'couro', 'cinza')),
    }),
    5: dict(normais=('gelo_eterno', 'agua', 'branco'), especiais={
        'punhos_yeti': ('manoplas', mat('branco', 'branco', 'agua', 'azul')),
        'sopro_gelido': ('katana', mat('agua', 'azul', 'branco', 'branco')),
        'presas_morsa': ('adaga', mat('branco', 'castanho', 'couro', 'castanho')),
        'arco_chifre': ('arco', mat('agua', 'branco', 'cinza', 'agua')),
        'lanca_tentaculo': ('lanca', mat('agua', 'roxo', 'roxo', 'rosa')),
        'cajado_gelido': ('cajado', mat('agua', 'branco', 'azul', 'agua')),
        'foice_wendigo': ('foice', mat('branco', 'preto', 'agua', 'agua')),
        'martelo_glaciar': ('martelo', mat('agua', 'cinza', 'couro', 'branco')),
        'katana_aurora': ('katana', mat('lilas', 'branco', 'verde', 'rosa')),
        'lamina_cavaleiro_gelido': ('espada_grande', mat('agua', 'azul', 'azul', 'branco')),
        'lanca_inverno_eterno': ('lanca', mat('agua', 'azul', 'branco', 'ouro')),
        'besta_pesada_gelo_eterno': ('besta', mat('agua', 'agua', 'azul', 'branco')),
    }),
    6: dict(normais=('coral_abissal', 'rosa', 'agua'), especiais={
        'sabre_afogado': ('espada', mat('agua', 'preto', 'vermelho', 'ouro')),
        'tridente_leviata': ('lanca', mat('azul', 'azul', 'agua', 'agua')),
        'martelo_casco_tartaruga': ('martelo', mat('verde', 'madeira', 'couro', 'amarelo')),
        'arco_gaivota': ('arco', mat('branco', 'cinza', 'vermelho', 'amarelo')),
        'ancora_imediato': ('martelo', mat('ferro', 'ferro', 'agua', 'agua')),
        'adaga_peixe_leao': ('adaga', mat('laranja', 'branco', 'vermelho', 'branco')),
        'lanca_alga': ('lanca', mat('verde', 'verde_esc', 'verde', 'amarelo')),
        'manoplas_coral': ('manoplas', mat('rosa', 'rosa', 'branco', 'branco')),
        'cajado_lanterna_abissal': ('cajado', mat('preto', 'preto', 'azul', 'agua')),
        'foice_mares': ('foice', mat('branco', 'agua', 'azul', 'agua')),
        'besta_arpao_almirante': ('besta', mat('ferro', 'madeira', 'azul', 'ouro')),
    }),
    7: dict(normais=('obsidiana', 'preto', 'laranja'), especiais={
        'martelo_forja': ('martelo', mat('preto', 'couro', 'couro', 'laranja')),
        'coracao_magma': ('espada_grande', mat('preto', 'preto', 'vermelho', 'laranja')),
        'arco_fenix': ('arco', mat('laranja', 'cinza', 'vermelho', 'amarelo')),
        'lanca_magma': ('lanca', mat('laranja', 'preto', 'preto', 'amarelo')),
        'machado_brasa_viva': ('machado', mat('laranja', 'preto', 'couro', 'vermelho')),
        'martelo_broca': ('martelo', mat('cobre', 'ferro', 'couro', 'laranja')),
        'manoplas_geiser': ('manoplas', mat('vermelho', 'vermelho', 'couro', 'laranja')),
        'espada_grande_portao': ('espada_grande', mat('preto', 'preto', 'roxo', 'roxo')),
        'cajado_sumo_sacerdote': ('cajado', mat('ouro', 'vermelho', 'vermelho', 'laranja')),
        'martelo_primordial': ('martelo', mat('cobre', 'cobre', 'couro', 'laranja')),
        'lamina_kai': ('espada', mat('ferro', 'preto', 'azul', 'azul')),
    }),
    8: dict(normais=('mitril', 'lilas', 'branco'), especiais={
        'grimorio_proibido': ('cajado', mat('roxo', 'preto', 'roxo', 'lilas')),
        'lamina_rei_caido': ('espada_grande', mat('preto', 'preto', 'vermelho', 'ouro')),
        'arco_sentinela': ('arco', mat('agua', 'cinza', 'agua', 'branco')),
        'martelo_sino': ('martelo', mat('ouro', 'madeira', 'couro', 'amarelo')),
        'pa_machado_coveiro': ('machado', mat('ferro', 'madeira', 'couro', 'cinza')),
        'espada_grande_ossos': ('espada_grande', mat('branco', 'branco', 'cinza', 'cinza')),
        'adaga_rosa_negra': ('adaga', mat('preto', 'verde_esc', 'vermelho', 'vermelho')),
        'katana_vitral': ('katana', mat('lilas', 'azul', 'amarelo', 'vermelho')),
        'manoplas_carcereiro': ('manoplas', mat('ferro', 'ferro', 'couro', 'preto')),
        'lanca_comandante': ('lanca', mat('preto', 'preto', 'vermelho', 'vermelho')),
        'foice_rainha_viuva': ('foice', mat('agua', 'preto', 'branco', 'branco')),
        'foice_tesoura': ('foice', mat('ferro', 'madeira', 'verde', 'amarelo')),
        'besta_mitril_abencoada': ('besta', mat('lilas', 'branco', 'ouro', 'amarelo')),
    }),
    9: dict(normais=('oricalco', 'ouro', 'agua'), especiais={
        'pena_de_grifo': ('arco', mat('ouro', 'branco', 'castanho', 'amarelo')),
        'foice_serafim': ('foice', mat('branco', 'preto', 'branco', 'preto')),
        'arpao_baleia': ('lanca', mat('branco', 'madeira', 'agua', 'agua')),
        'martelo_ilha': ('martelo', mat('castanho', 'madeira', 'verde', 'verde')),
        'espada_luz_solida': ('espada', mat('amarelo', 'branco', 'amarelo', 'branco')),
        'foice_jardineira': ('foice', mat('cobre', 'verde', 'verde', 'rosa')),
        'manoplas_leao': ('manoplas', mat('branco', 'branco', 'cinza', 'ouro')),
        'katana_relampago': ('katana', mat('amarelo', 'azul', 'azul', 'amarelo')),
        'cajado_vento': ('cajado', mat('branco', 'madeira', 'laranja', 'agua')),
        'arco_sol': ('arco', mat('ouro', 'laranja', 'vermelho', 'amarelo')),
        'lanca_arcanjo': ('lanca', mat('cobre', 'cobre', 'branco', 'ouro')),
        'lanca_relampago': ('lanca', mat('amarelo', 'ouro', 'azul', 'amarelo')),
    }),
    10: dict(normais=('estelar', 'roxo', 'amarelo'), especiais={
        'segundo_parado': ('adaga', mat('cobre', 'cobre', 'agua', 'agua')),
        'chave_sistema': ('espada', mat('agua', 'azul', 'azul', 'branco')),
        'chave_espada_porteiro': ('espada', mat('roxo', 'preto', 'roxo', 'ouro')),
        'arpao_cometa': ('lanca', mat('azul', 'roxo', 'lilas', 'amarelo')),
        'adaga_espelho': ('adaga', mat('agua', 'branco', 'agua', 'branco')),
        'lamina_ecos': ('katana', mat('roxo', 'preto', 'lilas', 'lilas')),
        'martelo_gravidade': ('martelo', mat('preto', 'roxo', 'roxo', 'lilas')),
        'arco_desistente': ('arco', mat('ferro', 'madeira', 'couro', 'cinza')),
        'cajado_indice': ('cajado', mat('azul', 'madeira', 'azul', 'agua')),
        'espada_grande_escada': ('espada_grande', mat('amarelo', 'preto', 'roxo', 'amarelo')),
        'katana_erro': ('katana', mat('roxo', 'verde', 'vermelho', 'agua')),
    }),
    # armas de amizade e míticas (não são de nenhuma região)
    11: dict(normais=None, especiais={
        'decima_milesima': ('espada', mat('ferro', 'madeira', 'couro', 'ouro')),
        'arma_inacabada_10000': ('espada', mat('cinza', 'madeira', 'couro', 'cinza')),
        'arco_da_mia': ('arco', mat('verde', 'madeira', 'verde', 'rosa')),
        'lamina_gemea': ('espada', mat('agua', 'preto', 'azul', 'vermelho')),
        'machado_da_equipa': ('machado', mat('ferro', 'madeira', 'vermelho', 'ouro')),
        'lanca_da_capita': ('lanca', mat('branco', 'azul', 'azul', 'ouro')),
        'aurora_primeiro_dia': ('espada', mat('amarelo', 'branco', 'rosa', 'laranja')),
        'fim_dos_mundos': ('espada_grande', mat('preto', 'roxo', 'vermelho', 'laranja')),
        'sussurro_vazio': ('adaga', mat('roxo', 'preto', 'roxo', 'lilas')),
        'lua_mil_anos': ('katana', mat('branco', 'azul', 'azul', 'amarelo')),
        'raiz_do_mundo': ('machado', mat('verde', 'madeira', 'verde', 'ouro')),
        'coracao_torre': ('martelo', mat('cinza', 'cinza', 'agua', 'agua')),
        'agulha_ceu': ('lanca', mat('agua', 'branco', 'branco', 'amarelo')),
        'ceifeira_estrelas': ('foice', mat('roxo', 'preto', 'amarelo', 'amarelo')),
        'arco_iris_eterno': ('arco', mat('rosa', 'branco', 'agua', 'amarelo')),
        'cometa_final': ('besta', mat('laranja', 'preto', 'roxo', 'amarelo')),
        'voz_sistema': ('cajado', mat('agua', 'azul', 'azul', 'agua')),
        'punhos_aren': ('manoplas', mat('vermelho', 'vermelho', 'azul', 'cobre')),
    }),
})


def gerar(regiao):
    R = REGIOES[regiao]
    pasta = os.path.join('arte', 'armas')
    os.makedirs(pasta, exist_ok=True)
    lista = dict(normais(*R['normais'])) if R.get('normais') else {}
    lista.update(R['especiais'])
    feitos = {}
    for nome, (tipo, m) in lista.items():
        s, i = fazer(tipo, m)
        s.save(os.path.join(pasta, f'{nome}.png'))
        i.save(os.path.join(pasta, f'{nome}_icone.png'))
        feitos[nome] = (s, i)
    return feitos


if __name__ == '__main__':
    reg = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    feitos = gerar(reg)
    print('ok', len(feitos), 'armas')
    if len(sys.argv) > 2:
        from PIL import Image
        n = len(feitos)
        E = 4
        folha = Image.new('RGBA', (8 * 52 * E, ((n + 7) // 8) * 70 * E), (50, 51, 83, 255))
        for idx, (nome, (s, i)) in enumerate(feitos.items()):
            x, y = (idx % 8) * 52 * E, (idx // 8) * 70 * E
            ss = s.resize((s.width * E, s.height * E), Image.NEAREST)
            folha.paste(ss, (x, y), ss)
            ii = i.resize((16 * E, 16 * E), Image.NEAREST)
            folha.paste(ii, (x, y + 50 * E), ii)
        folha.save(sys.argv[2])
