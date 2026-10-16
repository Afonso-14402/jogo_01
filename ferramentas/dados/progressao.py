"""docs/PROGRESSAO.md -> dados/classes.json, dados/skills_armas.json, dados/skills_vida.json,
dados/skills_unicas.json e dados/origens.json.

Cada skill fica com o texto (efeito_pt) e com uma "ação" tirada do texto para o jogo a poder fazer:
  forma (golpe · linha · area · investida · projetil · multi · buff · cura) · mult · dist (m) · golpes · elemento · estados
  custo {estamina | mp | hp_percent} · recarga (s)
As passivas ficam com "bonus": [{stat, valor}] quando o texto é simples (ex.: '+10% DEF e +10% HP').

Uso: python3 ferramentas/dados/progressao.py
"""
import json
import os
import re
import sys
sys.path.insert(0, os.path.dirname(__file__))
from estados import estados_em
from tabelas import tabelas, limpar, slug, ascii_

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..')
ELEMENTOS = {'luz': 'luz', 'fogo': 'fogo', 'ardente': 'fogo', 'gelo': 'gelo', 'nevao': 'gelo', 'raio': 'raio',
             'trovao': 'raio', 'sombra': 'sombra', 'sombrio': 'sombra', 'veneno': 'veneno'}
STATS = [('dano critico', 'dano_critico'), ('critico', 'critico'), ('velocidade de ataque', 'vel_ataque'),
         ('velocidade', 'velocidade'), ('atq', 'atq'), ('def', 'def'), ('res', 'res'), ('hp', 'hp'), ('mp', 'mp'),
         ('estamina', 'estamina'), ('alcance', 'alcance'), ('dano magico', 'dano_magico'), ('dano', 'dano')]
TIPOS_ARMA = {'espada': 'espada', 'espada grande': 'espada_grande', 'adaga': 'adaga', 'katana': 'katana',
              'machado': 'machado', 'martelo': 'martelo', 'lanca': 'lanca', 'foice': 'foice', 'arco': 'arco',
              'besta': 'besta', 'cajado': 'cajado', 'manoplas': 'manoplas'}


def num(t):
    return float(t.replace(',', '.'))


def custo(t):
    t = ascii_(limpar(t))
    m = re.search(r'(\d+)\s*%\s*do hp', t)
    if m:
        return {'hp_percent': int(m.group(1)) / 100}
    m = re.search(r'(\d+)\s*(est|mp)', t)
    if m:
        return {'estamina' if m.group(2) == 'est' else 'mp': int(m.group(1))}
    return {}


def acao(texto):
    t = ascii_(limpar(texto))
    a = {}
    m = re.search(r'[x×]\s*(\d+(?:,\d+)?)', t)
    a['mult'] = num(m.group(1)) if m else 1.5
    m = re.search(r'(\d+(?:,\d+)?)\s*m\b', t)
    if m:
        a['dist'] = num(m.group(1))
    m = re.search(r'(\d+)\s*(cortes|golpes|socos|virotes|flechas|giros|ceifadas|estocadas|lancas)', t)
    if m:
        a['golpes'] = int(m.group(1))
    if re.search(r'avanca|carga|investida|salto|teletransporte|salta', t):
        a['forma'] = 'investida'
    elif re.search(r'area|a tua volta|circulo|360|anel|giro|todos os inimigos|chuva|meteoro|nevao|tempestade', t):
        a['forma'] = 'area'
    elif re.search(r'linha|onda|atravessa|coluna', t):
        a['forma'] = 'linha'
    elif re.search(r'flecha|virote|bola|tiro|projetil|arremesso|lanca de gelo|raio', t):
        a['forma'] = 'projetil'
    elif a.get('golpes', 1) > 1:
        a['forma'] = 'multi'
    elif re.search(r'^cura|curas|cura \d', t):
        a['forma'] = 'cura'
    elif re.search(r'durante \d+ s|\d+ s:', t) and not re.search(r'[x×]\s*\d', t):
        a['forma'] = 'buff'
    else:
        a['forma'] = 'golpe'
    if a['forma'] == 'area' and 'dist' not in a:
        a['dist'] = 3.0
    for k, v in ELEMENTOS.items():
        if re.search(r'\b' + k, t):
            a['elemento'] = v
            break
    est = estados_em(texto)
    if est:
        a['estados'] = est
    m = re.search(r'(\d+)\s*s:\s*\+(\d+)\s*%\s*(atq|def)', t) or re.search(r'\+(\d+)\s*%\s*(atq|def)\s*durante\s*(\d+)\s*s', t)
    if m and a['forma'] == 'buff':
        g = m.groups()
        a['buff'] = {'stat': g[2] if g[0].isdigit() and len(g) == 3 and not g[2].isdigit() else g[1],
                     'valor': int(g[1] if g[2].isalpha() else g[0]) / 100,
                     'dura': int(g[0] if g[2].isalpha() else g[2])}
    return a


def bonus(texto):
    t = ascii_(limpar(texto))
    out = []
    for m in re.finditer(r'\+(\d+)\s*%\s*([a-z ]+)', t):
        alvo = m.group(2)
        for k, v in STATS:
            if alvo.startswith(k):
                out.append({'stat': v, 'valor': int(m.group(1)) / 100})
                break
    return out


def gerar():
    texto = open(os.path.join(RAIZ, 'docs', 'PROGRESSAO.md'), encoding='utf-8').read()
    classes, base_info = [], {}
    arvore = {'espadachim': None, 'cavaleiro': 'espadachim', 'paladino': 'cavaleiro', 'mestre_de_laminas': 'espadachim',
              'santo_da_espada': 'mestre_de_laminas', 'arqueiro': None, 'atirador': 'arqueiro', 'olho_de_falcao': 'atirador',
              'ranger': 'arqueiro', 'senhor_da_floresta': 'ranger', 'mago': None, 'arquimago': 'mago',
              'sabio_dos_elementos': 'arquimago', 'necromante': 'mago', 'rei_dos_mortos': 'necromante', 'tanque': None,
              'guardiao': 'tanque', 'fortaleza_viva': 'guardiao', 'berserker': 'tanque', 'senhor_da_guerra': 'berserker'}
    unicas, origens, armas, vida = [], [], [], []
    for titulo, linhas in tabelas(texto):
        if not linhas:
            continue
        cab = list(linhas[0].keys())
        m = re.match(r'3\.\d+ (.+?) \(níveis (\d+)', titulo)
        if m:
            cid = slug(m.group(1))
            skills = []
            for l in linhas:
                s = {'id': slug(limpar(l['Skill'])), 'nome_pt': limpar(l['Skill']), 'nivel': int(l['Nível']),
                     'tipo': limpar(l['Tipo']), 'custo': custo(l['Custo']),
                     'recarga': float(re.sub(r'[^\d,]', '', l['Recarga']).replace(',', '.') or 0),
                     'efeito_pt': limpar(l['Efeito'])}
                if s['tipo'] == 'ativa':
                    s.update(acao(l['Efeito']))
                else:
                    s['bonus'] = bonus(l['Efeito'])
                skills.append(s)
            classes.append({'id': cid, 'nome_pt': m.group(1), 'nivel_minimo': int(m.group(2)), 'anterior': arvore.get(cid),
                            'skills': skills})
        elif 'Classe base' in cab:
            for l in linhas:
                base_info[slug(limpar(l['Classe base']))] = {
                    'armas_preferidas': [TIPOS_ARMA[ascii_(a.strip())] for a in limpar(l['Armas preferidas']).split(',')
                                         if ascii_(a.strip()) in TIPOS_ARMA],
                    'bonus_pt': limpar(l['Bónus da classe']), 'bonus': bonus(l['Bónus da classe'])}
        elif 'Skill Única' in cab:
            for l in linhas:
                unicas.append({'id': slug(limpar(l['Skill Única'])), 'nome_pt': limpar(l['Skill Única']),
                               'efeito_pt': limpar(l['Efeito exato'])})
        elif 'Origem' in cab:
            for l in linhas:
                oid = re.search(r'`(\w+)`', l['Origem']).group(1)
                origens.append({'id': oid, 'nome_pt': re.sub(r'\(.*', '', limpar(l['Origem'])).strip(),
                                'frase_pt': limpar(l['Frase da escolha']).strip('"'), 'bonus_pt': limpar(l['Bónus']),
                                'bonus': bonus(l['Bónus']), 'comentam': [slug(n) for n in limpar(l['Quem comenta']).split(',')]})
        elif cab[:2] == ['Arma', 'Nível 3']:
            for l in linhas:
                tipo = TIPOS_ARMA[ascii_(limpar(l['Arma']))]
                for col, nv in (('Nível 3', 3), ('Nível 6', 6), ('Nível 10', 10)):
                    cel = l[col]
                    nome = re.search(r'\*\*(.+?)\*\*', cel).group(1)
                    par = re.search(r'\(([^)]*\d+\s*s)\)', cel)
                    efeito = cel.split('):', 1)[1] if '):' in cel else ''
                    s = {'id': slug(nome), 'nome_pt': nome, 'arma': tipo, 'nivel': nv,
                         'custo': custo(par.group(1)) if par else {'mp': 30},
                         'recarga': num(re.search(r'(\d+(?:,\d+)?)\s*s', par.group(1)).group(1)) if par else 12.0,
                         'efeito_pt': limpar(efeito) or limpar(cel)}
                    s.update(acao(efeito or nome))
                    if tipo == 'cajado':
                        s.update({'forma': 'projetil' if nv == 3 else 'area', 'mult': [2.0, 3.0, 5.0][[3, 6, 10].index(nv)],
                                  'custo': {'mp': [15, 30, 60][[3, 6, 10].index(nv)]}, 'recarga': [4, 12, 30][[3, 6, 10].index(nv)],
                                  'elemento_da_gema': True})
                    armas.append(s)
        elif cab[:2] == ['Skill', 'Sobe ao…']:
            for l in linhas:
                vida.append({'id': slug(limpar(l['Skill'])), 'nome_pt': limpar(l['Skill']), 'sobe_pt': limpar(l['Sobe ao…']),
                             'vantagens_pt': [limpar(l[f'Nv {n}']) for n in (10, 20, 30, 40, 50)]})
    for c in classes:
        raiz = c['id']
        while arvore.get(raiz):
            raiz = arvore[raiz]
        c['base'] = raiz
        if c['id'] in base_info:
            c.update(base_info[c['id']])
    # ícones (arte/icones/skills/<id>.png); o cajado usa o primeiro feitiço da lista (muda com a gema)
    icones = {f[:-4] for f in os.listdir(os.path.join(RAIZ, 'arte', 'icones', 'skills')) if f.endswith('.png')}
    for s in armas + vida + unicas + [s for c in classes for s in c['skills']]:
        cand = [s['id']] + [slug(p) for p in s['nome_pt'].split('/')]
        s['icone'] = next((f'res://arte/icones/skills/{c}.png' for c in cand if c in icones), '')
    for s in armas:
        if s['arma'] == 'cajado':
            s['id'] = slug(s['nome_pt'].split('/')[0])
    pasta = os.path.join(RAIZ, 'dados')
    for nome, dados in (('classes', classes), ('skills_armas', armas), ('skills_vida', vida), ('skills_unicas', unicas),
                        ('origens', origens)):
        with open(os.path.join(pasta, nome + '.json'), 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=1)
    print('ok', len(classes), 'classes,', sum(len(c['skills']) for c in classes), 'skills de classe,', len(armas),
          'de armas,', len(vida), 'de vida,', len(unicas), 'únicas,', len(origens), 'origens')


if __name__ == '__main__':
    gerar()
