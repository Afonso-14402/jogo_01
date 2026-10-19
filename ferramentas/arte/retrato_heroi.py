"""Retratos do herói para a criação de personagem: um por penteado e emoção, com CORES-ÍNDICE na pele, no cabelo
e nos olhos. O jogo troca-as pelas cores escolhidas (como nos sprites; arte/heroi/paletas.json).
Saída: arte/retratos/heroi/<penteado>_<emocao>.png + arte/retratos/heroi/indices.json

Uso: python3 ferramentas/arte/retrato_heroi.py
"""
import json
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
import retratos as R
import humano

PASTA = os.path.join(os.path.dirname(__file__), '..', '..', 'arte', 'retratos', 'heroi')
# cores que o retrato do herói não usa noutro sítio (do escuro para o claro)
PELE_I = ['#0b5e65', '#0b8a8f', '#0eaf9b', '#30e1b9', '#8ff8e2']
CABELO_I = ['#165a4c', '#239063', '#1ebc73', '#91db69', '#cddf6c']
OLHOS_I = '#a884f3'
ESTILO = {'espetado': 'espetado', 'curto': 'curto', 'rapado': 'curto', 'comprido': 'comprido', 'rabo': 'rabo',
          'carrapito': 'carrapito', 'tranca': 'rabo', 'caracois': 'curto'}

if __name__ == '__main__':
    os.makedirs(PASTA, exist_ok=True)
    humano.PELES['_indice'] = PELE_I
    humano.CABELOS['_indice'] = CABELO_I
    R.PELES['_indice'] = PELE_I
    R.CABELOS['_indice'] = CABELO_I
    for pent, estilo in ESTILO.items():
        e = dict(R.HEROI, cabelo=estilo, pele='_indice', cor_cabelo='_indice', olhos_cor=OLHOS_I)
        for em in R.EMOCOES:
            R.retrato(e, em).save(os.path.join(PASTA, f'{pent}_{em}.png'))
    # posição na rampa do retrato -> posição na rampa da paleta (pele: K D S L P; cabelo: H h r R Y)
    json.dump({'pele': PELE_I, 'cabelo': CABELO_I, 'olhos': OLHOS_I, 'mapa_pele': [0, 0, 1, 2, 3], 'mapa_cabelo': [0, 1, 2, 3, 4]},
              open(os.path.join(PASTA, 'indices.json'), 'w'), indent=1)
    print('ok', len(ESTILO), 'penteados x', len(R.EMOCOES), 'emoções')
