"""Gera o herói (pixel art 32x32) em arte/heroi/.

Cada parte do corpo é uma máscara de píxeis. Ao desenhar, cada parte leva:
  - contorno escuro (#2e222f) à volta (por cima das partes já desenhadas, para as separar);
  - luz de cima à esquerda (claro), cor base no meio e sombra em baixo à direita.
Só usa cores da paleta Resurrect 64.

Uso: python3 ferramentas/arte/heroi.py   (corre a partir da raiz do repositório)
"""
import os
from PIL import Image

T = 32
OUT = '#2e222f'
PAL = {
    'pele':   ('#fdcbb0', '#fca790', '#e6904e'),
    'cabelo': ('#9e4539', '#7a3045', '#45293f'),
    'tunica': ('#4d9be6', '#4d65b4', '#484a77'),
    'lenco':  ('#ea4f36', '#b33831', '#6e2727'),
    'calcas': ('#7f708a', '#625565', '#3e3546'),
    'calcas_longe': ('#625565', '#3e3546', '#3e3546'),
    'botas':  ('#966c6c', '#694f62', '#45293f'),
    'cinto':  ('#ab947a', '#4c3e24', '#4c3e24'),
}
FIVELA = '#f9c22b'
OLHO = '#2e222f'


def rect(x1, y1, x2, y2):
    return {(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)}


def cabeca_redonda(x1, y1, x2, y2):
    m = rect(x1, y1, x2, y2)
    for c in [(x1, y1), (x2, y1), (x1, y2), (x2, y2)]:
        m.discard(c)
    return m


def mover(m, dx=0, dy=0):
    return {(x + dx, y + dy) for x, y in m}


class Quadro:
    def __init__(self):
        self.px = {}

    def parte(self, mascara, cores, separar=True):
        claro, base, sombra = PAL[cores] if isinstance(cores, str) else cores
        contorno = set()
        for x, y in mascara:
            for vx, vy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                v = (x + vx, y + vy)
                if v not in mascara:
                    contorno.add(v)
        for p in contorno:
            if 0 <= p[0] < T and 0 <= p[1] < T and (separar or p not in self.px):
                self.px[p] = OUT
        for x, y in mascara:
            if not (0 <= x < T and 0 <= y < T):
                continue
            if (x - 1, y) not in mascara or (x, y - 1) not in mascara:
                c = claro
            elif (x + 1, y) not in mascara or (x, y + 1) not in mascara:
                c = sombra
            else:
                c = base
            self.px[(x, y)] = c

    def ponto(self, p, cor):
        self.px[p] = cor

    def imagem(self):
        img = Image.new('RGBA', (T, T), (0, 0, 0, 0))
        for (x, y), c in self.px.items():
            if 0 <= x < T and 0 <= y < T:
                img.putpixel((x, y), tuple(int(c[i:i + 2], 16) for i in (1, 3, 5)) + (255,))
        return img


# ---------- de frente (baixo) e de costas (cima) ----------

def perna_frente(q, x, levanta, cores='calcas'):
    q.parte(rect(x, 24, x + 2, 28 - levanta), cores)
    q.parte(rect(x - (1 if x < 16 else 0), 29 - levanta, x + 2 + (1 if x >= 16 else 0), 31 - levanta), 'botas')


def corpo_frente(q, bob, braco_e, braco_d, costas=False):
    # braços (atrás do tronco, para o contorno do tronco os separar)
    for x, d in ((9, braco_e), (21, braco_d)):
        q.parte(rect(x, 16 + bob, x + 1, 20 + bob + d), 'tunica')
        q.parte(rect(x, 21 + bob + d, x + 1, 22 + bob + d), 'pele')
    # tronco e cinto
    q.parte(rect(11, 16 + bob, 20, 24), 'tunica')
    q.parte(rect(11, 23, 20, 23), 'cinto', separar=False)
    if not costas:
        q.ponto((15, 23), FIVELA)
        q.ponto((16, 23), FIVELA)
    # cabeça
    cab = cabeca_redonda(10, 6 + bob, 21, 14 + bob)
    if costas:
        q.parte(cab, 'cabelo')
        for p in [(14, 8), (15, 9), (18, 10), (12, 12), (13, 13), (17, 13), (20, 12)]:
            q.ponto((p[0], p[1] + bob), PAL['cabelo'][2])
        for p in [(12, 7), (13, 7), (14, 8)]:
            q.ponto((p[0], p[1] + bob), PAL['cabelo'][0])
    else:
        q.parte(cab, 'pele')
        cabelo = rect(10, 6 + bob, 21, 8 + bob) | rect(10, 9 + bob, 11, 12 + bob) | rect(20, 9 + bob, 21, 12 + bob)
        cabelo |= {(13, 9 + bob), (16, 9 + bob), (17, 9 + bob)}
        cabelo -= {(10, 6 + bob), (21, 6 + bob)}
        q.parte(cabelo, 'cabelo', separar=False)
        for p in [(12, 7), (13, 7), (17, 7)]:
            q.ponto((p[0], p[1] + bob), PAL['cabelo'][0])
        for x in (13, 18):
            q.ponto((x, 11 + bob), OLHO)
            q.ponto((x, 12 + bob), OLHO)
    # lenço (por cima de tudo, à volta do pescoço)
    q.parte(rect(12, 15 + bob, 19, 16 + bob), 'lenco')
    if costas:
        q.parte(rect(15, 17 + bob, 16, 19 + bob), 'lenco')
    else:
        q.parte(rect(17, 17 + bob, 18, 18 + bob), 'lenco')


def frente(bob, l, r, costas=False):
    q = Quadro()
    perna_frente(q, 12, l)
    perna_frente(q, 17, r)
    braco_e = -1 if r else 0
    braco_d = -1 if l else 0
    corpo_frente(q, bob, braco_e, braco_d, costas)
    return q.imagem()


# ---------- de lado (direita) ----------

def perna_lado(q, dx, levanta, cores):
    q.parte(rect(15 + dx, 24, 17 + dx, 28 - levanta), cores)
    q.parte(rect(15 + dx, 29 - levanta, 18 + dx, 31 - levanta), 'botas')


def lado(bob, perto, longe, lev_perto, lev_longe, cauda):
    q = Quadro()
    sw = -perto // 2
    # braço de longe (atrás de tudo) e perna de longe (mais escura)
    q.parte(rect(15 - sw, 17 + bob, 16 - sw, 21 + bob), ('#4d65b4', '#484a77', '#484a77'))
    perna_lado(q, longe, lev_longe, 'calcas_longe')
    perna_lado(q, perto, lev_perto, 'calcas')
    # tronco
    q.parte(rect(13, 16 + bob, 19, 24), 'tunica')
    q.parte(rect(13, 23, 19, 23), 'cinto', separar=False)
    # cabeça
    q.parte(cabeca_redonda(11, 6 + bob, 21, 14 + bob), 'pele')
    cabelo = rect(11, 6 + bob, 21, 8 + bob) | rect(11, 9 + bob, 15, 12 + bob) | {(18, 9 + bob), (19, 9 + bob)}
    cabelo -= {(11, 6 + bob), (21, 6 + bob)}
    q.parte(cabelo, 'cabelo', separar=False)
    for p in [(13, 7), (14, 7), (18, 7)]:
        q.ponto((p[0], p[1] + bob), PAL['cabelo'][0])
    q.ponto((19, 11 + bob), OLHO)
    q.ponto((19, 12 + bob), OLHO)
    q.ponto((22, 12 + bob), '#e6904e')  # nariz
    # lenço com a ponta a voar para trás
    q.parte(rect(13, 15 + bob, 19, 16 + bob), 'lenco')
    q.parte(rect(9, 16 + bob + cauda, 12, 17 + bob + cauda), 'lenco')
    # braço de perto (balança ao contrário da perna de perto)
    q.parte(rect(15, 17 + bob, 17, 19 + bob), 'tunica')
    q.parte(rect(15 + sw, 20 + bob, 17 + sw, 20 + bob), 'tunica', separar=False)
    q.parte(rect(15 + sw, 21 + bob, 17 + sw, 22 + bob), 'pele')
    return q.imagem()


# ---------- animações ----------

ANDAR_FRENTE = [(1, 0, 0), (0, 1, 0), (0, 2, 0), (1, 0, 0), (0, 0, 1), (0, 0, 2)]
PARADO_BOB = [0, 0, 1, 1]
# (bob, perto, longe, levanta perto, levanta longe)
ANDAR_LADO = [(1, 2, -2, 0, 0), (0, 1, -1, 1, 0), (0, 0, 0, 2, 0),
              (1, -2, 2, 0, 0), (0, -1, 1, 0, 1), (0, 0, 0, 0, 2)]


def animacoes():
    a = {}
    a['parado_baixo'] = [frente(b, 0, 0) for b in PARADO_BOB]
    a['parado_cima'] = [frente(b, 0, 0, costas=True) for b in PARADO_BOB]
    a['parado_lado'] = [lado(b, 0, 0, 0, 0, b) for b in PARADO_BOB]
    a['andar_baixo'] = [frente(*f) for f in ANDAR_FRENTE]
    a['andar_cima'] = [frente(*f, costas=True) for f in ANDAR_FRENTE]
    a['andar_lado'] = [lado(b, p, l, lp, ll, i % 2) for i, (b, p, l, lp, ll) in enumerate(ANDAR_LADO)]
    return a


def tira(frames):
    img = Image.new('RGBA', (T * len(frames), T), (0, 0, 0, 0))
    for i, f in enumerate(frames):
        img.paste(f, (i * T, 0))
    return img


if __name__ == '__main__':
    pasta = os.path.join('arte', 'heroi')
    os.makedirs(pasta, exist_ok=True)
    for nome, frames in animacoes().items():
        tira(frames).save(os.path.join(pasta, f'heroi_{nome}.png'))
        print('ok', nome, len(frames))
