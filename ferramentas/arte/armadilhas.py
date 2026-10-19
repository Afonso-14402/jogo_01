"""Armadilhas das masmorras (docs/TORRE.md 3.1, salas "linhas"): o que salta do chão ou atravessa a sala quando a
faixa vermelha acaba de avisar. Tudo animado, com as formas do motor (luz de cima à esquerda, contorno #2e222f).

  - raiz:   raiz com espinhos a sair do chão (4 quadros: ponta → raiz inteira a tremer)
  - osso:   espinho de osso a sair do chão (4 quadros)
  - lamina: serra redonda a girar (4 quadros)
  - dardo:  dardo de ponta verde a voar (2 quadros: a pena abana)
  - bala:   bala de canhão com riscos de velocidade (2 quadros)
  - fogo:   bola de fogo a crepitar (4 quadros)
  - olhos:  raio vermelho dos olhos dos retratos (2 quadros: pulsa)

Saída: arte/masmorras/armadilha_<nome>.png (tira horizontal de quadros)
Uso:   python3 ferramentas/arte/armadilhas.py [--previa]
"""
import math
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from motor import Parte, elipse, retangulo, capsula, poligono, desenhar, tira, previa_gif

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..')
PASTA = os.path.join(RAIZ, 'arte', 'masmorras')


def ponto(x, y, cor, z=60):
    return Parte({(x, y)}, None, z=z, cor=cor, separar=False)


def pontos(lista, cor, z=60):
    return Parte(set(lista), None, z=z, cor=cor, separar=False)


def espinho(fase, rampa, nos):
    """16×24: sai do chão (fase 0 = só a ponta, 2 = inteiro, 3 = inteiro e inclinado um píxel: treme)."""
    W, H = 16, 24
    alt = [6, 14, 21, 21][fase]
    inc = 1 if fase == 3 else 0
    base = H - 2
    P = []
    pts = [(4, base), (12, base), (8 + inc, base - alt)]
    P.append(Parte(poligono(pts), rampa, z=1, volume='cilindro_v'))
    if fase >= 1:   # espinhos (raiz) ou nós (osso) nos lados
        for k, y in enumerate(range(base - 4, base - alt + 3, -5)):
            lado = -1 if k % 2 == 0 else 1
            x = 8 + lado * (3 - k // 2) + (inc if y < base - 8 else 0)
            if nos:
                P.append(Parte(elipse(x, y, 1.5, 1.2), rampa, z=2))
            else:
                P.append(Parte(poligono([(x, y), (x, y - 2), (x + lado * 3, y - 3)]), rampa, z=2, plano=True))
    # terra a saltar à volta da base
    P.append(Parte(elipse(8, base + 0.5, 6, 1.5), 'castanho', z=0, plano=True))
    if fase in (1, 2):
        P.append(pontos([(2, base - 2 - fase), (14, base - 3), (1, base - 5)], '#966c6c'))
    if not nos:
        P.append(pontos([(7, base - 6), (9, base - 11)], '#547e64', 3))   # musgo na raiz
    return desenhar(P, W, H)


def serra(fase):
    W = H = 24
    P = [Parte(elipse(12, 12, 9, 9), 'ferro', z=1)]
    for k in range(8):   # dentes: rodam 1/4 de dente por quadro
        a = (k + fase / 4.0) * math.tau / 8
        x, y = 12 + math.cos(a) * 10, 12 + math.sin(a) * 10
        x2, y2 = 12 + math.cos(a + 0.35) * 8, 12 + math.sin(a + 0.35) * 8
        P.append(Parte(poligono([(round(x), round(y)), (round(x2), round(y2)), (12, 12)]), 'ferro', z=2, plano=True))
    P.append(Parte(elipse(12, 12, 3, 3), 'cinza', z=3))
    P.append(ponto(12, 12, '#2e222f', 4))
    a = fase * math.tau / 4
    P.append(pontos([(round(12 + math.cos(a) * 6), round(12 + math.sin(a) * 6))], '#ffffff', 5))
    return desenhar(P, W, H)


def dardo(fase):
    W, H = 16, 8
    P = [Parte(retangulo(3, 3, 12, 4), 'madeira', z=1, plano=True),
         Parte(poligono([(12, 2), (12, 5), (15, 3)]), 'verde', z=2, plano=True)]   # ponta envenenada
    abana = fase % 2
    P.append(Parte(poligono([(0, 1 + abana), (4, 3), (0, 6 - abana)]), 'vermelho', z=0, plano=True))   # pena
    return desenhar(P, W, H)


def bala(fase):
    W, H = 16, 12
    P = [Parte(elipse(10, 6, 4.5, 4.5), 'preto', z=1)]
    P.append(ponto(8, 4, '#c7dcd0', 3))
    riscos = [(0, 4), (1, 4), (2, 4), (1, 7), (2, 7), (3, 7), (4, 7)] if fase == 0 else [(1, 5), (2, 5), (3, 5), (0, 8), (1, 8), (2, 8)]
    P.append(pontos(riscos, '#9babb2', 0))
    return desenhar(P, W, H, contorno_fora=True)


def fogo(fase):
    W = H = 16
    r = [5.5, 6, 5.5, 5][fase]
    P = [Parte(elipse(8, 9, r, r - 0.5), 'vermelho', z=1),
         Parte(elipse(8, 9.5, r - 2, r - 2.5), 'laranja', z=2),
         Parte(elipse(8, 10, max(1.5, r - 4), max(1.5, r - 4)), 'amarelo', z=3)]
    # labaredas em cima, a mudar de quadro para quadro
    for k, dx in enumerate((-3, 0, 3)):
        h = [3, 5, 2, 4][(fase + k) % 4]
        P.append(Parte(poligono([(8 + dx - 2, 6), (8 + dx + 2, 6), (8 + dx + (fase % 2), 6 - h)]), 'laranja', z=2, plano=True))
    return desenhar(P, W, H)


def olho(fase):
    W = H = 12
    r = 4 if fase == 0 else 5
    P = [Parte(elipse(6, 6, r, r), 'vermelho', z=1), Parte(elipse(6, 6, r - 2, r - 2), 'rosa', z=2)]
    P.append(ponto(6, 6, '#ffffff', 3))
    return desenhar(P, W, H)


SPRITES = {
    'raiz': [espinho(f, 'madeira', False) for f in range(4)],
    'osso': [espinho(f, 'branco', True) for f in range(4)],
    'lamina': [serra(f) for f in range(4)],
    'dardo': [dardo(f) for f in range(2)],
    'bala': [bala(f) for f in range(2)],
    'fogo': [fogo(f) for f in range(4)],
    'olhos': [olho(f) for f in range(2)],
}


def main():
    os.makedirs(PASTA, exist_ok=True)
    for nome, frames in SPRITES.items():
        tira(frames).save(os.path.join(PASTA, 'armadilha_%s.png' % nome))
    if '--previa' in sys.argv:
        caminho = sys.argv[sys.argv.index('--previa') + 1]
        quadrados = []
        for frames in SPRITES.values():   # todos no mesmo tamanho (24×24) para a prévia
            q = []
            for f in frames:
                from PIL import Image
                im = Image.new('RGBA', (24, 24), (0, 0, 0, 0))
                im.paste(f, ((24 - f.size[0]) // 2, 24 - f.size[1]))
                q.append(im)
            quadrados.append(q)
        previa_gif([quadrados], caminho, escala=8, ms=140)
    print('armadilhas:', ', '.join(SPRITES))


if __name__ == '__main__':
    main()
