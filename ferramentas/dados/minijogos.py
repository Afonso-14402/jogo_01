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


def _n(t, padrao=0.0):
    m = re.search(r'([\d][\d ]*(?:,\d+)?)', t)
    return num(m.group(1)) if m else padrao


def corridas(texto):
    """As corridas (secção 4.5): números de cada uma e quem organiza (id do NPC da povoação)."""
    sec = re.search(r'^### 4\.5 .*?\n(.*?)(?=^### )', texto, re.S | re.M).group(1)
    npcs = json.load(open(os.path.join(RAIZ, 'dados', 'npcs_povoacoes.json'), encoding='utf-8'))
    npcs = npcs.values() if isinstance(npcs, dict) else npcs
    premio = int(re.search(r'(\d+) ouro × região', sec).group(1))
    obst = [int(x) for x in re.search(r'de (\d+) em \d+ a (\d+) em', sec).groups()]
    r = {}
    for _, ls in tabelas(sec):
        for l in ls:
            nome = limpar(l.get('Corrida', ''))
            if not nome:
                continue
            org = limpar(l.get('Quem organiza', ''))
            quem = next((n['id'] for n in npcs if org and org != '—' and n.get('nome_pt', '').startswith(org)), '')
            vel = limpar(l['Velocidade'])
            ctl = limpar(l['Controlo'])
            bat = limpar(l['Bater num obstáculo'])
            gan = limpar(l['Ganhar'])
            c = {'id': ascii_(nome).lower(), 'nome_pt': nome, 'andar': int(limpar(l['Andar'])), 'organizador': quem,
                 'pista': _n(limpar(l['Pista'])), 'velocidade': _n(vel), 'premio_regiao': premio, 'obstaculos': obst}
            m = re.search(r'\+([\d,]+)(?: m/s)? por (cristal|remada)', vel)
            if m:
                c['por_' + m.group(2)] = num(m.group(1))
                if m.group(2) == 'remada':   # nas canoas começa-se parado
                    c['velocidade'] = 0.0
            m = re.search(r'até (\d+)', vel)
            if m:
                c['maximo'] = int(m.group(1))
            m = re.search(r'trava ([\d,]+)', vel)
            if m:
                c['atrito'] = num(m.group(1))
            m = re.search(r'\+([\d,]+) m/s por segundo', vel)
            if m:
                c['aceleracao'] = num(m.group(1))
            m = re.search(r'baixar.*?\(([\d,]+) s\)', ctl)
            if m:
                c['baixar'] = num(m.group(1))
            m = re.search(r'saltar.*?\(([\d,]+) s', ctl)
            if m:
                c['salto'] = num(m.group(1))
            m = re.search(r'parada ([\d,]+) s', bat)
            if m:
                c['parar'] = num(m.group(1))
            m = re.search(r'−(\d+)% de velocidade durante ([\d,]+) s', bat)
            if m:
                c['travar'] = int(m.group(1)) / 100
                c['travar_s'] = num(m.group(2))
            if 'volta a' in bat:
                c['recomecar'] = True
            m = re.search(r'menos de (\d+) s', gan)
            if m:
                c['tempo'] = int(m.group(1))
            m = re.search(r'missão (R\d_\d+)', gan)
            if m:
                c['missao'] = m.group(1)
            m = re.search(r'(\d+) vitórias', gan)
            if m:
                c['vitorias_missao'] = int(m.group(1))
            m = re.search(r'\(([\d, em/s]+)\)', gan)
            if m:
                c['rivais'] = [num(x) for x in re.findall(r'[\d]+(?:,\d+)?', m.group(1).replace('m/s', ''))]
                k = re.search(r'(\d+) canoas rivais', gan)
                if k and len(c['rivais']) == 1:
                    c['rivais'] = c['rivais'] * int(k.group(1))
            m = re.search(r'(\d+) ouro por (cristal|bandeira)', gan)
            if m:
                c['ouro_coisa'] = int(m.group(1))
            r[c['id']] = c
    return r


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
    ritmo = {'setas': int(re.search(r'(\d+) setas', kv['Ritmo: música']).group(1)), 'bpm': int(re.search(r'(\d+) batidas', kv['Ritmo: música']).group(1)),
             'perfeito': num(re.search(r'Perfeito a ±([\d,]+)', kv['Ritmo: acertar']).group(1)), 'bom': num(re.search(r'Bom a ±([\d,]+)', kv['Ritmo: acertar']).group(1)),
             'pontos_perfeito': 100, 'pontos_bom': 50,
             'notas': {k: int(v) for k, v in re.findall(r'(\w) ≥ (\d+)%', kv['Ritmo: nota'])}, 'ouro_por': 20}
    return {
        'ritmo': ritmo,
        'corridas': corridas(texto),
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
