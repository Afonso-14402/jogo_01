"""Jogos da Taberna (docs/ATIVIDADES.md, secções 4.2–4.4 e 4.9) -> dados/minijogos.json.

Uso: python3 ferramentas/dados/minijogos.py
"""
import json
import os
import re
import sys
sys.path.insert(0, os.path.dirname(__file__))
from tabelas import tabelas, limpar, ascii_

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..')


def num(t):
    return float(t.replace(' ', '').replace(',', '.'))


def gerar():
    texto = open(os.path.join(RAIZ, 'docs', 'ATIVIDADES.md'), encoding='utf-8').read()
    sec = re.search(r'^### 4\.9 .*?\n(.*?)(?=^### |^## |\Z)', texto, re.S | re.M).group(1)
    kv = {limpar(l['Regra']): limpar(l['Valor']) for _, ls in tabelas(sec) for l in ls}
    apostas = [int(x.replace(' ', '')) for x in re.findall(r'(\d[\d ]*\d|\d)(?= ouro|\s*·|\s*\()', kv['Apostas'])]
    tipos = {ascii_(k): int(v) for k, v in re.findall(r'(\w+) (\d+)', kv['Cartas: ATQ'].split('tipo', 1)[1])}
    adv_c = []
    for n, dif, r in re.findall(r'(\w+) \((\w+)(?:, monstros das regiões)?,? 1–(\d+)\)', kv['Cartas: adversários']):
        adv_c.append({'id': ascii_(n).lower(), 'nome_pt': n, 'dificuldade': dif, 'regioes': int(r)})
    adv_b = []
    for n, v, e in re.findall(r'(\w+) \((?:cursor )?×([\d,]+), (?:empurra )?(\d+)%/s\)', kv['Braço de ferro: adversários']):
        adv_b.append({'id': ascii_(n).lower(), 'nome_pt': n, 'velocidade': num(v), 'empurra': int(e) / 100})
    zona = re.findall(r'([\d,]+)%', kv['Braço de ferro: zona verde'])
    emp = re.findall(r'(\d+)%', kv['Braço de ferro: carregar'])
    cats = re.search(r'^### 4\.6 .*?\n(.*?)(?=^### )', texto, re.S | re.M).group(1)
    arena = []
    for _, ls in tabelas(cats):
        for l in ls:
            cat = limpar(l.get('Categoria', ''))
            if cat in ('Bronze', 'Prata', 'Ouro'):
                como = limpar(l.get('Como é', ''))
                arena.append({'id': ascii_(cat).lower(), 'nome_pt': cat, 'abre_pt': limpar(l.get('Abre', '')),
                              'ondas': int(re.search(r'(\d+) ondas', como).group(1)), 'regioes': int(re.search(r'regiões 1–(\d+)', como).group(1)),
                              'boss': 'Boss' in como})
    abre = {'bronze': 'rank >= D', 'prata': 'andar_maximo >= 30', 'ouro': 'rank >= S'}
    premios = re.findall(r'(\w+) ([\d ]+) ouro \+ arma (\w+)(?: \+ título \*([^*]+)\*)?', kv['Arena: prémios'])
    for a in arena:
        a['cond'] = abre[a['id']]
        for cat, ouro, rar, tit in premios:
            if ascii_(cat).lower() == a['id']:
                a['ouro'] = int(ouro.replace(' ', ''))
                a['raridade'] = {'Rara': 'raro', 'Épica': 'epico', 'Lendária': 'lendario'}.get(rar, 'raro')
                a['titulo_pt'] = tit
    return {
        'arena': arena, 'arena_max_onda': 6, 'arena_cura': 0.2, 'arena_pausa': 3.0,
        'apostas': apostas[:4], 'aposta_alta': 1000, 'aposta_alta_andar': 30,
        'dados_seguidas': int(re.search(r'até (\d+)', kv['Dados: seguidas']).group(1)),
        'cartas_minimo': int(re.search(r'(\d+) tipos', kv['Cartas: baralho']).group(1)),
        'cartas_base': 2, 'cartas_por_regiao': 1.2, 'cartas_tipo': tipos, 'cartas_elemento': 3, 'cartas_adversarios': adv_c,
        'braco_zona': num(zona[0]) / 100, 'braco_zona_for': num(zona[1]) / 100, 'braco_zona_max': num(zona[2]) / 100,
        'braco_acerto': int(emp[0]) / 100, 'braco_erro': int(emp[1]) / 100, 'braco_adversarios': adv_b,
    }


if __name__ == '__main__':
    d = gerar()
    with open(os.path.join(RAIZ, 'dados', 'minijogos.json'), 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
    print(json.dumps(d, ensure_ascii=False))
