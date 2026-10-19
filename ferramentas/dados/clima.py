"""Clima (docs/SISTEMAS.md, 14.1, para a cidade por estação) e o clima de cada região (docs/regioes/rXX, linha "Clima")
-> dados/clima.json. Cada tipo de tempo tem um "efeito" que o jogo sabe mostrar:
sol · chuva · trovoada · nevoeiro · neve · nevao · areia · cinza · fumo · brasas · nublado · escuro · nenhum

Uso: python3 ferramentas/dados/clima.py
"""
import glob
import json
import os
import re
import sys
sys.path.insert(0, os.path.dirname(__file__))
from tabelas import tabelas, limpar, slug, ascii_

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..')
EFEITO = [('tempestade de areia', 'areia'), ('nevoeiro roxo', 'nevoeiro_roxo'), ('nevoeiro gelado', 'nevoeiro'),
          ('nevoeiro', 'nevoeiro'), ('nuvens baixas', 'nevoeiro'), ('tempestade', 'trovoada'), ('trovoada', 'trovoada'),
          ('chuva de brasas', 'brasas'), ('erupcao', 'brasas'), ('chuva', 'chuva'), ('nevao', 'nevao'), ('neve', 'neve'),
          ('cinza', 'cinza'), ('ceu de fumo', 'fumo'), ('ceu nublado', 'nublado'), ('noite sem lua', 'escuro'),
          ('noite gelada', 'sol'), ('ceu limpo', 'sol'), ('calmaria', 'sol'), ('sol', 'sol')]


def efeito(nome):
    a = ascii_(nome)
    return next((e for k, e in EFEITO if k in a), 'sol')


def gerar():
    out = {'estacoes': {}, 'regioes': {}}
    sis = open(os.path.join(RAIZ, 'docs', 'SISTEMAS.md'), encoding='utf-8').read()
    for _, linhas in tabelas(sis):
        for l in linhas:
            if 'Estação' in l and 'Chuva' in l:
                est = slug(l['Estação']).replace('verao', 'verao')
                out['estacoes'][est] = [{'nome_pt': k, 'efeito': efeito(k), 'hipotese': int(re.sub(r'\D', '', v) or 0) / 100}
                                        for k, v in l.items() if k != 'Estação' and int(re.sub(r'\D', '', v) or 0) > 0]
    for f in sorted(glob.glob(os.path.join(RAIZ, 'docs', 'regioes', 'r*.md'))):
        regiao = int(os.path.basename(f)[1:3])
        m = re.search(r'^\| Clima \| (.+?) \|$', open(f, encoding='utf-8').read(), re.M)
        lista = []
        for parte in limpar(m.group(1)).split('·') if m else []:
            mm = re.match(r'\s*(.+?)\s+(\d+)%', parte)
            if mm:
                lista.append({'nome_pt': mm.group(1), 'efeito': efeito(mm.group(1)), 'hipotese': int(mm.group(2)) / 100,
                              'so_noite': 'só à noite' in parte})
        out['regioes'][str(regiao)] = lista or [{'nome_pt': 'Sem céu', 'efeito': 'nenhum', 'hipotese': 1.0}]
    with open(os.path.join(RAIZ, 'dados', 'clima.json'), 'w', encoding='utf-8') as fo:
        json.dump(out, fo, ensure_ascii=False, indent=1)
    print('ok', len(out['estacoes']), 'estações,', len(out['regioes']), 'regiões')


if __name__ == '__main__':
    gerar()
