"""docs/textos/itens.md (+ preços e efeitos de docs/ITENS.md) -> dados/itens.json (docs/PROGRAMACAO.md, secção 5.7).

Uso: python3 ferramentas/dados/itens.py
"""
import json
import os
import re
import sys
sys.path.insert(0, os.path.dirname(__file__))
from tabelas import tabelas, limpar, numero, slug, ascii_

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..')
CATEGORIA = [('materia', 'material'), ('armadura', 'armadura'), ('arma', 'arma'), ('acessor', 'acessorio'),
             ('ferramenta', 'ferramenta'), ('consum', 'consumivel'), ('comida', 'comida'), ('peixe', 'peixe'),
             ('semente', 'semente'), ('planta', 'semente'), ('miss', 'missao'), ('especia', 'missao')]
EMPILHA = {'material': 99, 'consumivel': 99, 'comida': 99, 'peixe': 99, 'semente': 99, 'missao': 1, 'arma': 1,
           'armadura': 1, 'acessorio': 1, 'ferramenta': 1}
PESO = {'material': 0.2, 'consumivel': 0.2, 'comida': 0.3, 'peixe': 0.5, 'semente': 0.05, 'missao': 0.0, 'arma': 2.0,
        'armadura': 3.0, 'acessorio': 0.1, 'ferramenta': 2.0}


def efeito_de(desc, nome=''):
    """Tira efeitos simples do texto: 'cura 30% do HP' · 'cura 50%' · '+20% DEF 5 min'."""
    t = ascii_(desc)
    ef = {}
    m = re.search(r'(?:cura|devolve|repoe|recupera)\s+(\d+)\s*%\s*(?:do|da|de)?\s*(hp|vida|mp|mana|estamina)?', t)
    if m:
        alvo = m.group(2) or ('mp' if 'mana' in ascii_(nome) else 'estamina' if 'estamina' in ascii_(nome) else 'hp')
        chave = {'hp': 'curar_hp_percent', 'vida': 'curar_hp_percent', 'mp': 'curar_mp_percent', 'mana': 'curar_mp_percent',
                 'estamina': 'curar_estamina_percent'}[alvo]
        ef[chave] = int(m.group(1)) / 100
    m = re.search(r'cura\s+(\d+)\s*(hp|vida|mp)', t)
    if m and not ef:
        ef['curar_hp' if m.group(2) != 'mp' else 'curar_mp'] = int(m.group(1))
    m = re.search(r'\+(\d+)\s*%\s*(atq|def|velocidade|critico)[^0-9]*(\d+)\s*min', t)
    if m:
        ef['bonus'] = {'stat': m.group(2), 'valor': int(m.group(1)) / 100, 'minutos': int(m.group(3))}
    return ef


def gerar():
    texto = open(os.path.join(RAIZ, 'docs', 'textos', 'itens.md'), encoding='utf-8').read()
    icones = {f[:-4] for f in os.listdir(os.path.join(RAIZ, 'arte', 'icones')) if f.endswith('.png')}
    regiao = 0
    itens = []
    for titulo, linhas in tabelas(texto):
        m = re.match(r'Região (\d+)', titulo)
        if m:
            regiao = int(m.group(1))
        cat = next((c for k, c in CATEGORIA if k in ascii_(titulo)), 'material')
        for l in linhas:
            vals = list(l.values())
            if not vals or not vals[0].startswith('`'):
                continue
            iid = limpar(vals[0])
            nome = limpar(vals[1]) if len(vals) > 1 else iid
            desc = limpar(vals[2]) if len(vals) > 2 else ''
            if cat == 'arma':
                icone = f'res://arte/armas/{iid}_icone.png'
            else:
                icone = f'res://arte/icones/{iid}.png' if iid in icones else ''
            itens.append({'id': iid, 'nome': 'ITEM_' + iid.upper(), 'nome_pt': nome, 'descricao_pt': desc, 'categoria': cat,
                          'regiao': regiao, 'efeito': efeito_de(desc), 'preco': 0, 'peso': PESO[cat],
                          'empilha': EMPILHA[cat], 'icone': icone})
    # preços (docs/ITENS.md e docs/LOJAS.md têm tabelas com "Preço")
    precos, efeitos = {}, {}
    for doc in ('ITENS.md', 'LOJAS.md'):
        for _, linhas in tabelas(open(os.path.join(RAIZ, 'docs', doc), encoding='utf-8').read()):
            for l in linhas:
                vals = list(l.values())
                if not vals:
                    continue
                nome = slug(limpar(vals[0]))
                preco = next((v for k, v in l.items() if k.startswith('Preço')), None)
                if preco and numero(preco):
                    precos.setdefault(nome, int(numero(preco.replace(' ', ''))))
                ef = next((v for k, v in l.items() if k.startswith('Efeito')), None)
                if ef:
                    efeitos.setdefault(nome, limpar(ef))
    for it in itens:
        s_ = slug(it['nome_pt'])
        it['preco'] = precos.get(s_, it['preco'])
        if s_ in efeitos:
            it['efeito_pt'] = efeitos[s_]
            it['efeito'] = efeito_de(efeitos[s_], it['nome_pt']) or it['efeito']
    # itens do jogo que não estão na lista das regiões
    itens.append({'id': 'chave_bau_ouro', 'nome': 'ITEM_CHAVE_BAU_OURO', 'nome_pt': 'Chave de Baú de Ouro',
                  'descricao_pt': 'Abre um baú de ouro. Cai de guardiões e de baús de prata, às vezes.', 'categoria': 'missao',
                  'regiao': 0, 'efeito': {}, 'preco': 0, 'peso': 0.0, 'empilha': 99, 'icone': 'res://arte/icones/chave_bau_ouro.png'})
    with open(os.path.join(RAIZ, 'dados', 'itens.json'), 'w', encoding='utf-8') as f:
        json.dump(itens, f, ensure_ascii=False, indent=1)
    from collections import Counter
    print('ok', len(itens), 'itens', dict(Counter(i['categoria'] for i in itens)), '; com preço:', sum(1 for i in itens if i['preco']),
          '; com efeito:', sum(1 for i in itens if i['efeito']))


if __name__ == '__main__':
    gerar()
