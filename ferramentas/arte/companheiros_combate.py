"""Animações de combate dos 26 companheiros (golpes de cada tipo de arma e levar dano), com as poses do herói.
Os estilos (cores, cabelo, acessórios) vêm dos scripts de cada um. Saída: arte/npcs/<id>_<anim>_<dir>.png.

Uso: python3 ferramentas/arte/companheiros_combate.py
"""
import json
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from humano import animacoes_combate
from motor import guardar
import aventureiros
import npcs_ascendia
import npcs_regioes

if __name__ == '__main__':
    estilos = dict(npcs_ascendia.ESTILOS, **npcs_regioes.ESTILOS, **aventureiros.ESTILOS)
    ids = [c['id'] for c in json.load(open(os.path.join('dados', 'companheiros.json')))]
    for i in ids:
        guardar(os.path.join('arte', 'npcs'), i, animacoes_combate(estilos[i]))
    print('ok', len(ids), 'companheiros com animações de combate')
