"""Quinta: as plantas todas (docs/ITENS.md, secção 7) em 4 fases e os animais da quinta (secção 8).
Plantas: arte/icones/plantas/<planta>_fase_N.png (só faz as que ainda não existem).
Animais: arte/animais/<animal>_*.png (parado, mover, atacar = "dar carinho", dano, morrer não se usa).

Uso: python3 ferramentas/arte/quinta.py
"""
import os
import re
import sys
import unicodedata
sys.path.insert(0, os.path.dirname(__file__))
import icones as I
from criaturas import lote

DOC = os.path.join(os.path.dirname(__file__), '..', '..', 'docs', 'ITENS.md')
RAIZ = os.path.join(os.path.dirname(__file__), '..', '..', 'arte')

COR_FRUTO = [  # palavra -> cor do fruto/flor (rampa do motor)
    ('dourad', 'ouro'), ('roxa', 'roxo'), ('doce', 'laranja'), ('batata', 'castanho'), ('cenoura', 'laranja'),
    ('tomate', 'vermelho'), ('cebola', 'branco'), ('morango', 'vermelho'), ('mel', 'azul'), ('fungo', 'azul'),
    ('raiz', 'cinza'), ('cacau', 'castanho'), ('cafe', 'vermelho'), ('banan', 'amarelo'), ('lava', 'laranja'),
    ('pimenta', 'vermelho'), ('lirio', 'branco'), ('carnivora', 'rosa'), ('tamar', 'castanho'), ('cacto', 'agua'),
    ('melao', 'amarelo'), ('acafrao', 'lilas'), ('deserto', 'rosa'), ('bagas', 'vermelho'), ('couve', 'verde'),
    ('neve', 'branco'), ('musgo', 'verde_esc'), ('alga', 'agua'), ('ananas', 'amarelo'), ('cinza', 'cinza'),
    ('trigo', 'amarelo'), ('nabo', 'branco'), ('arroz', 'branco'), ('milho', 'amarelo'), ('uva', 'roxo'),
    ('rosa', 'preto'), ('tempo', 'lilas'), ('estel', 'roxo'), ('lotus', 'lilas'), ('nuvem', 'branco'), ('vento', 'agua'),
    ('ceu', 'agua'), ('perola', 'branco'), ('coral', 'rosa'), ('maca', 'vermelho'), ('flor', 'rosa'),
]
ALTA = ('arvore', 'tamar', 'banan', 'cacau', 'cafe', 'trigo', 'milho', 'macieira', 'cacto', 'girassol')


def _ascii(t):
    return ''.join(c for c in unicodedata.normalize('NFD', t.lower()) if unicodedata.category(c) != 'Mn')


def _slug(t):
    return re.sub(r'[^a-z0-9]+', '_', _ascii(t)).strip('_')


def plantas():
    txt = open(DOC, encoding='utf-8').read().split('## 7.')[1].split('\n## ')[0]
    pasta = os.path.join(RAIZ, 'icones', 'plantas')
    os.makedirs(pasta, exist_ok=True)
    feitas = 0
    for nome in re.findall(r'^\| (?!Planta)([^|]+?) \|', txt, re.M):
        pid = _slug(nome)
        if os.path.exists(os.path.join(pasta, f'{pid}_fase_4.png')):
            continue
        t = _ascii(nome)
        cor = next((c for k, c in COR_FRUTO if k in t), 'vermelho')
        folha = 'musgo' if 'trigo' in t or 'milho' in t else 'verde_esc' if 'neve' in t or 'musgo' in t else 'verde'
        tipo = 'alta' if any(k in t for k in ALTA) else 'baixa'
        for f in range(1, 5):
            I.planta(f, cor, folha, tipo).save(os.path.join(pasta, f'{pid}_fase_{f}.png'))
        feitas += 1
    return feitas


ANIMAIS = [
    ('galinha', 'voador', dict(cor='branco', asa='penas', bico='amarelo', k=0.5, crista='vermelho'), []),
    ('vaca', 'quadrupede', dict(cor='branco', manchas='preto', chifres='branco', comprimento=1.2, altura=1.1, grossura=1.3,
                                cor_focinho='rosa', k=0.8), []),
    ('cabra', 'quadrupede', dict(cor='castanho', chifres='cinza', comprimento=0.9, altura=0.9, k=0.65), []),
    ('ovelha', 'quadrupede', dict(cor='branco', juba='branco', grossura=1.4, comprimento=0.9, altura=0.8, cor_focinho='preto', k=0.65), []),
    ('abelhas', 'voador', dict(cor='amarelo', asa='inseto', manchas='preto', k=0.4), []),
]


if __name__ == '__main__':
    print('ok', plantas(), 'plantas novas x 4 fases')
    lote(os.path.join(RAIZ, 'animais'), ANIMAIS)
    print('ok', len(ANIMAIS), 'animais da quinta')
