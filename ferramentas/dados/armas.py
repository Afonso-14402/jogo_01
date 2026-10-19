"""docs/ARMAS.md -> dados/armas.json (formato em docs/PROGRAMACAO.md, secção 5.1).

Uso: python3 ferramentas/dados/armas.py
"""
import json
import os
import re
import sys
sys.path.insert(0, os.path.dirname(__file__))
from estados import estados_em, ESTADOS
from tabelas import tabelas, seccao, limpar, numero, slug, ascii_

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..')
TIPOS = ['espada_grande', 'espada', 'adaga', 'katana', 'machado', 'martelo', 'lanca', 'foice', 'arco', 'besta', 'cajado', 'manoplas']
DISTANCIA = {'arco', 'besta', 'cajado'}
MULT = {'espada': 1.0, 'espada_grande': 1.8, 'adaga': 0.6, 'katana': 1.1, 'machado': 1.4, 'martelo': 1.7, 'lanca': 1.15,
        'foice': 1.3, 'arco': 0.9, 'besta': 1.4, 'cajado': 1.0, 'manoplas': 0.55}
ATQ_TIER = [12, 24, 40, 60, 85, 115, 150, 190, 235, 290]
RARIDADE_FIXA = {'unica': 'epico', 'guardiao': 'raro', 'secreta': 'lendario', 'rara': 'raro', 'amizade': 'lendario',
                 'mitica': 'mitico'}


def tipo_de(texto):
    t = slug(texto)
    t = {'espada_grande': 'espada_grande', 'lanca': 'lanca'}.get(t, t)
    for tp in TIPOS:
        if t.startswith(tp) or tp in t:
            return tp
    return 'espada'


ALIAS = {'espada_grande_da_escada_final': 'espada_grande_escada', 'machado_do_rei_sob_a_montanha': 'machado_rei_montanha'}


def ficheiro_arte(nome, ids_arte):
    s = slug(nome)
    if s in ALIAS:
        return ALIAS[s]
    if s in ids_arte:
        return s
    sem_artigo = re.sub(r'^(a|o|as|os)_', '', s)
    sem_de = re.sub(r'_(de|do|da|dos|das)_', '_', sem_artigo)
    for cand in (sem_artigo, sem_de):
        if cand in ids_arte:
            return cand
    parecidas = [i for i in ids_arte if i.startswith(sem_de.split('_')[0]) and set(sem_de.split('_')) <= set(i.split('_')) | {'de', 'do', 'da'}]
    return parecidas[0] if len(parecidas) == 1 else s


def gerar():
    texto = open(os.path.join(RAIZ, 'docs', 'ARMAS.md'), encoding='utf-8').read()
    ids_arte = {f[:-4] for f in os.listdir(os.path.join(RAIZ, 'arte', 'armas')) if f.endswith('.png') and '_icone' not in f}
    armas, base = [], {}

    def nova(aid, nome, tipo, tier, atq, vel, alcance, crit, peso, preco, categoria, efeito=''):
        magico = tipo == 'cajado'
        a = {'id': aid, 'nome': 'ARMA_' + aid.upper(), 'nome_pt': nome, 'tipo': tipo, 'tier': tier,
             'atq': 0 if magico else round(atq, 1), 'atq_magico': round(atq, 1) if magico else 0,
             'velocidade': vel, 'alcance': alcance, 'critico': crit, 'elemento': next((ESTADOS[e['estado']].get('elemento') for e in estados_em(efeito) if ESTADOS[e['estado']].get('elemento')), None),
             'efeitos': [dict(e, hipotese=e.get('hipotese', 1.0), so_carregado='carregado' in efeito.lower()) for e in estados_em(efeito)],
             'efeito_texto': efeito, 'nivel_minimo': max(1, (tier - 1) * 10 + 1), 'preco': int(preco), 'peso': peso,
             'distancia': tipo in DISTANCIA, 'categoria': categoria,
             'raridade': RARIDADE_FIXA.get(categoria),
             'sprite': f'res://arte/armas/{aid}.png', 'icone': f'res://arte/armas/{aid}_icone.png',
             'unica': categoria != 'normal'}
        armas.append(a)
        return a

    # ---- 3. armas normais (com todos os números)
    for titulo, linhas in tabelas(seccao(texto, '## 3.')):
        m = re.search(r'Tier (\d+)', titulo)
        if not m:
            continue
        tier = int(m.group(1))
        for l in linhas:
            aid = limpar(l.get('ID', ''))
            if not aid:
                continue
            tp = tipo_de(aid)
            a = nova(aid, limpar(l['Arma']), tp, tier, numero(l['ATQ']), numero(l['Vel.']), numero(l['Alcance']),
                     numero(l['Crít.']), numero(l['Peso']), numero(l['Preço'].replace(' ', '')), 'normal')
            base[(tp, tier)] = a

    def copia_base(nome, tp, tier, atq, categoria, efeito):
        b = base.get((tp, max(1, min(10, tier))), base.get((tp, 1)))
        aid = ficheiro_arte(nome, ids_arte)
        if any(x['id'] == aid for x in armas):
            return
        nova(aid, nome, tp, tier, atq or ATQ_TIER[tier - 1] * MULT[tp], b['velocidade'], b['alcance'],
             b['critico'], b['peso'], b['preco'] * 3, categoria, efeito)

    # ---- 4. únicas dos bosses
    for _, linhas in tabelas(seccao(texto, '## 4.')):
        for l in linhas:
            if 'Arma' in l and 'Tier' in l:
                copia_base(limpar(l['Arma']), tipo_de(l['Tipo']), int(numero(l['Tier'], 1)), numero(l.get('ATQ base', '0')),
                           'unica', limpar(l.get('Efeito', '')))
    # ---- 5. de guardião (tier = região do andar)
    for _, linhas in tabelas(seccao(texto, '## 5.')):
        for l in linhas:
            if 'Guardião' in l and l.get('Andar', '').strip().isdigit():
                tier = (int(l['Andar']) - 1) // 10 + 1
                tp = tipo_de(l['Tipo'])
                copia_base(limpar(l['Arma']), tp, tier, ATQ_TIER[tier - 1] * MULT[tp] * 1.15, 'guardiao', limpar(l.get('Efeito', '')))
    # ---- 6. secretas, 7. raras
    for sec, cat in (('## 6.', 'secreta'), ('## 7.', 'rara')):
        for _, linhas in tabelas(seccao(texto, sec)):
            for l in linhas:
                if 'Arma' in l and 'Tipo' in l:
                    tier = int(numero(l.get('Tier', '1'), 1)) or 1
                    copia_base(limpar(l['Arma']), tipo_de(l['Tipo']), tier, numero(l.get('ATQ base', '0')), cat,
                               limpar(l.get('Efeito', l.get('Como é', ''))))
    # ---- 8. amizade (ATQ ao nível do jogador: o jogo calcula; aqui fica o tier 1)
    for _, linhas in tabelas(seccao(texto, '## 8.')):
        for l in linhas:
            if 'Arma' in l and 'De quem' in l:
                copia_base(limpar(l['Arma']), tipo_de(l['Tipo']), 1, 0, 'amizade', limpar(l.get('Como é', '')))
    sem_arte = [a['id'] for a in armas if a['id'] not in ids_arte]
    os.makedirs(os.path.join(RAIZ, 'dados'), exist_ok=True)
    with open(os.path.join(RAIZ, 'dados', 'armas.json'), 'w', encoding='utf-8') as f:
        json.dump(armas, f, ensure_ascii=False, indent=1)
    print('ok', len(armas), 'armas;', len(sem_arte), 'sem imagem:', sem_arte[:12])


if __name__ == '__main__':
    gerar()
