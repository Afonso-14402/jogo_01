"""Estados alterados (docs/SISTEMAS.md, secção 5) -> dados/estados.json, e uma função para os encontrar em textos
(ataques dos monstros, efeitos das armas, poções). Os números vêm das tabelas da secção 5.

Campos de cada estado:
  dura (s) · dano_hp_s (fração do HP máx. por segundo) · dano_hp_m (por metro andado) · def_mult · vel_mult ·
  atq_vel_mult · cura_mult · dano_mult · parado (não anda) · sem_atacar · sem_skills · interrompe · acumula/vira ·
  golpe_mult (o próximo golpe faz ×) · elemento (de onde vem) · cor (números e ícone) · nome_pt

Uso: python3 ferramentas/dados/estados.py
"""
import json
import os
import re
import sys
sys.path.insert(0, os.path.dirname(__file__))
from tabelas import ascii_

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..')

ESTADOS = {
    'veneno': {'nome_pt': 'Veneno', 'dura': 6, 'dano_hp_s': 0.02, 'elemento': 'veneno', 'cor': '#a884f3'},
    'queimadura': {'nome_pt': 'Queimadura', 'dura': 4, 'dano_hp_s': 0.03, 'def_mult': 0.9, 'elemento': 'fogo', 'cor': '#ea4f36'},
    'frio': {'nome_pt': 'Frio', 'dura': 4, 'vel_mult': 0.7, 'atq_vel_mult': 0.7, 'acumula': 3, 'vira': 'congelado',
             'elemento': 'gelo', 'cor': '#8fd3ff'},
    'congelado': {'nome_pt': 'Congelado', 'dura': 1.5, 'parado': True, 'sem_atacar': True, 'golpe_mult': 1.5,
                  'elemento': 'gelo', 'cor': '#c7dcd0'},
    'choque': {'nome_pt': 'Choque', 'dura': 0.2, 'interrompe': True, 'salta': [2, 3.0, 0.5], 'elemento': 'raio', 'cor': '#f9c22b'},
    'atordoado': {'nome_pt': 'Atordoado', 'dura': 1, 'dura_boss': 0.3, 'parado': True, 'sem_atacar': True, 'cor': '#fbff86'},
    'sangrar': {'nome_pt': 'Sangrar', 'dura': 5, 'dano_hp_m': 0.01, 'cor': '#ae2334'},
    'lentidao': {'nome_pt': 'Lentidão', 'dura': 3, 'vel_mult': 0.5, 'cor': '#7a4841'},
    'cegueira': {'nome_pt': 'Cegueira', 'dura': 4, 'precisao': 0.7, 'cor': '#3e3546'},
    'medo': {'nome_pt': 'Medo', 'dura': 1.5, 'sem_atacar': True, 'cor': '#6b3e75'},
    'maldicao': {'nome_pt': 'Maldição', 'dura': 10, 'cura_mult': 0.5, 'elemento': 'sombra', 'cor': '#45293f'},
    'encharcado': {'nome_pt': 'Encharcado', 'dura': 6, 'elem_mult': {'raio': 1.5, 'fogo': 0.5}, 'cor': '#4d9be6'},
    'agarrado': {'nome_pt': 'Agarrado', 'dura': 3, 'parado': True, 'sem_atacar': True, 'soltar': True, 'cor': '#9a4f50'},
    'preso': {'nome_pt': 'Preso', 'dura': 2, 'parado': True, 'cor': '#5d4954'},
    'puxado': {'nome_pt': 'Puxado', 'dura': 2, 'puxar': 1.5, 'cor': '#fca790'},
    'partida': {'nome_pt': 'Partida', 'dura': 0.1, 'trocar_arma': True, 'cor': '#f5a097'},
    'trocado': {'nome_pt': 'Controlos trocados', 'dura': 3, 'trocar_controlos': True, 'cor': '#b2ba90'},
    'sapo': {'nome_pt': 'Sapo', 'dura': 3, 'sem_atacar': True, 'sem_skills': True, 'cor': '#5ac54f'},
    'parado': {'nome_pt': 'Parado', 'dura': 1.25, 'parado': True, 'sem_atacar': True, 'cor': '#c7b08b'},
    'silencio': {'nome_pt': 'Silêncio', 'dura': 3, 'sem_skills': True, 'cor': '#9babb2'},
    'encolhido': {'nome_pt': 'Encolhido', 'dura': 30, 'dano_mult': 0.5, 'escala': 0.5, 'cor': '#e3c896'},
}

# palavras (sem acentos, minúsculas) -> estado
PALAVRAS = [
    (r'envenen|veneno', 'veneno'), (r'queimadura|em chamas|incendeia', 'queimadura'), (r'\bfrio\b', 'frio'),
    (r'congela', 'congelado'), (r'choque|eletrocut', 'choque'), (r'atordo|derruba', 'atordoado'),
    (r'sangra|sangue', 'sangrar'), (r'lentidao', 'lentidao'), (r'cegueira|\bcega', 'cegueira'), (r'\bmedo\b', 'medo'),
    (r'maldi', 'maldicao'), (r'encharcad', 'encharcado'), (r'agarra|enrola-se', 'agarrado'),
    (r'prende|\bpreso|enraiz', 'preso'), (r'puxa', 'puxado'), (r'troca a tua arma', 'partida'),
    (r'controlos trocados|tonto', 'trocado'), (r'\bsapo\b', 'sapo'), (r'para o tempo|\bparado\b', 'parado'),
    (r'silencio', 'silencio'), (r'encolh|ficas pequeno', 'encolhido'),
]


def estados_em(texto):
    """'Cegueira 2 s e Lentidão' -> [{'estado': 'cegueira', 'dura': 2.0}, {'estado': 'lentidao'}] (por ordem)"""
    t = ascii_(texto or '').lower()
    out = []
    for padrao, est in PALAVRAS:
        m = re.search(padrao, t)
        if m and all(o['estado'] != est for o in out):
            e = {'estado': est, '_pos': m.start()}
            d = re.match(r'[^.;:x(]{0,22}?(\d+(?:,\d+)?)\s*s\b', t[m.start():])
            if d:
                e['dura'] = float(d.group(1).replace(',', '.'))
            h = re.search(r'(\d+)\s*%', t[max(0, m.start() - 12):m.end() + 22])
            if h:
                e['hipotese'] = int(h.group(1)) / 100
            out.append(e)
    out.sort(key=lambda e: e.pop('_pos'))
    return out


def gerar():
    with open(os.path.join(RAIZ, 'dados', 'estados.json'), 'w', encoding='utf-8') as f:
        json.dump(ESTADOS, f, ensure_ascii=False, indent=1)
    print('ok', len(ESTADOS), 'estados')


if __name__ == '__main__':
    gerar()
