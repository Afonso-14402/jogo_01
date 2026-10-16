"""Desenhos que o jogo precisa e que não pertencem a uma região: o Mímico (baú-monstro, a partir do andar 6),
a moeda de ouro (drops) e a chave do baú de ouro. Saída: arte/monstros_comuns/ e arte/icones/.

Uso: python3 ferramentas/arte/extras_jogo.py
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
import icones as I
from criaturas import lote
from motor import Parte, elipse, RAMPAS

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..', 'arte')


def moeda():
    return [Parte(elipse(8, 8.5, 5.5, 5.5), RAMPAS['ouro'], z=1),
            Parte({p for p in elipse(8, 8.5, 3.6, 3.6) if p not in elipse(8, 8.5, 2.6, 2.6)}, RAMPAS['laranja'], z=2, separar=False)]


if __name__ == '__main__':
    lote(os.path.join(RAIZ, 'monstros_comuns'), [('mimico', 'objeto', dict(tipo='mimico', cor='madeira'), ['golpe', 'salto'])])
    I.icone(moeda()).save(os.path.join(RAIZ, 'icones', 'moeda_ouro.png'))
    I.icone(I.chave('ouro')).save(os.path.join(RAIZ, 'icones', 'chave_bau_ouro.png'))
    print('ok: mímico, moeda, chave')
