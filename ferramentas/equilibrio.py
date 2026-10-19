"""Equilíbrio do combate, só com as contas (docs/SISTEMAS.md, secções 2, 4 e 6).

1. Define o "jogador esperado" em cada andar (nível, atributos, arma, armadura, poções, classe, Manejo) — as
   regras estão em docs/SISTEMAS.md, secção 23 — e grava-o em testes/jogador_esperado.json (o robô
   testes/robo_jogar.gd usa este ficheiro para preparar o herói).
2. Para cada andar 1–100 calcula: golpes para matar um monstro normal do andar, golpes que o herói aguenta,
   e para o guardião / mini-boss / boss a duração da luta e quantos golpes dele o herói aguenta.

As contas copiam o jogo (scripts/personagens/jogador.gd, monstro.gd, boss.gd), não só o documento.

Uso: python3 ferramentas/equilibrio.py            (tabela resumida dos 100 andares)
     python3 ferramentas/equilibrio.py 1 2 3 10   (só estes andares, com o detalhe de cada monstro)
"""
import json
import math
import os
import sys

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')


def _json(*p):
    with open(os.path.join(RAIZ, *p), encoding='utf-8') as f:
        return json.load(f)


C = _json('dados', 'constantes.json')
ARMAS = {a['id']: a for a in _json('dados', 'armas.json')}
_it = _json('dados', 'itens.json')
ITENS = {i['id']: i for i in (_it if isinstance(_it, list) else _it.values())}
MONSTROS = {m['id']: m for m in _json('dados', 'monstros.json')}
BOSSES = {b['id']: b for b in _json('dados', 'bosses.json')}

TIER_ARMA = ['cobre', 'ferro', 'aco', 'prata', 'gelo_eterno', 'coral_abissal', 'obsidiana', 'mitril', 'oricalco', 'estelar']
TIER_ARMADURA = ['couro_javali', 'ferro', 'crocodilo', 'deserto', 'urso', 'tubarao', 'salamandra', 'mitril',
                 'penas_trovao', 'estelar']
PECAS = ['corpo', 'cabeca', 'maos', 'pes', 'capa']
# a parte dos pontos de atributo que o jogador esperado (espadachim) põe em cada atributo
REPARTICAO = {'for': 0.4, 'vit': 0.3, 'agi': 0.2, 'des': 0.1, 'int': 0.0, 'sor': 0.0}
UPTIME = 0.6   # fração do tempo de uma luta de boss em que o herói está mesmo a bater (o resto: esquivar, andar, beber)


# ------------------------------------------------------------------ o jogador esperado ------------------------------------------------------------------

def perfil(n):
    """O herói "normal" ao chegar ao andar n (regras em docs/SISTEMAS.md, secção 23)."""
    regiao = (n - 1) // 10 + 1
    k = (n - 1) % 10                      # 0 = 1.º andar da região
    nivel = max(1, n)
    pontos = (nivel - 1) * C['pontos_por_nivel']
    atr = {a: C['atributo_inicial'] + int(round(pontos * f)) for a, f in REPARTICAO.items()}
    # arma: a espada do tier da região a partir do 3.º andar dela (antes, a da região anterior bem melhorada)
    if regiao == 1 or k >= 2:
        tier, melhoria = regiao, min(3, k // 3)
    else:
        tier, melhoria = regiao - 1, 4
    # armadura: nenhuma nos andares 1–2; corpo e cabeça nos 3–5; o conjunto todo depois (do mesmo tier da arma)
    if n <= 2:
        pecas = []
    elif n <= 5:
        pecas = ['corpo', 'cabeca']
    else:
        pecas = PECAS
    pocao = 'pocao_vida_p' if regiao <= 2 else ('pocao_vida_m' if regiao <= 4 else ('pocao_vida_g' if regiao <= 9 else 'pocao_vida_maxima'))
    classe = ''
    if nivel >= 70:
        classe = 'santo_da_espada'
    elif nivel >= 40:
        classe = 'mestre_de_laminas'
    elif nivel >= 10:
        classe = 'espadachim'
    return {'andar': n, 'nivel': nivel, 'atributos': atr, 'arma': 'espada_' + TIER_ARMA[tier - 1], 'melhoria': melhoria,
            'armadura': [TIER_ARMADURA[tier - 1] + '_' + p for p in pecas], 'armadura_melhoria': melhoria,
            'pocao': pocao, 'pocoes': 5, 'classe': classe, 'manejo_espada': 200 * (n - 1)}


# ------------------------------------------------------------------ contas do jogo ------------------------------------------------------------------

def nivel_manejo(pontos):
    n, resto = 1, pontos
    while n < C['skill_arma_max']:
        custo = C['skill_arma_base'] * n * n
        if resto < custo:
            return n
        resto -= custo
        n += 1
    return n


def heroi(p):
    a = p['atributos']
    m_inst = 1.0 + p['melhoria'] * C['melhoria_atq']
    arma = ARMAS[p['arma']]
    dfs = sum(ITENS[x]['def'] for x in p['armadura']) * (1.0 + p['armadura_melhoria'] * C['melhoria_atq'])
    bonus_hp = 0.0
    bonus_atq = 0.0
    if p['classe']:   # o Espadachim dá +10% de ATQ com espadas (as classes seguintes ainda não estão nos dados)
        bonus_atq = 0.1
    hp = (C['hp_base'] + a['vit'] * C['hp_por_vit'] + p['nivel'] * C['hp_por_nivel']) * (1 + bonus_hp)
    # o jogo multiplica (ATQ da arma + FOR × 1,5) pela melhoria (jogador.gd, golpe_com)
    atq = (arma['atq'] + a['for'] * C['atq_por_for']) * m_inst
    manejo = 1.0 + C['skill_arma_dano'] * nivel_manejo(p['manejo_espada']) + bonus_atq
    critico = min(C['critico_base'] + a['des'] * C['critico_por_des'] + a['sor'] * C['critico_por_sor'] + arma['critico'],
                  C['critico_maximo'])
    combo = sum(C['combo_mult']) / 3.0
    return {'hp': hp, 'def': dfs + a['vit'] * C['def_por_vit'], 'atq': atq, 'mult': combo * manejo * (1 + critico * (C['critico_dano'] - 1)),
            'golpes_s': arma['velocidade']}


def monstro(id_, nivel, tipo=None):
    d = MONSTROS.get(id_) or BOSSES.get(id_) or {}
    t = tipo or d.get('tipo', 'normal')
    m = C['tipos_monstro'].get(t, C['tipos_monstro']['normal'])
    k = C['monstro_hp']
    hp = (k[0] + k[1] * nivel + k[2] * nivel * nivel) * m['hp']
    atq = (C['monstro_atq'][0] + C['monstro_atq'][1] * nivel) * m['atq']
    ataques = d.get('ataques') or [a for f in d.get('fases', [])[:1] for a in f.get('ataques', [])] or [{'mult': 1.0}]
    mult = sum(float(a.get('mult', 1.0)) for a in ataques) / len(ataques)
    return {'id': id_, 'tipo': t, 'nivel': nivel, 'hp': hp, 'atq': atq * mult, 'def': nivel * C['monstro_def'] * m['def']}


def golpe(atq, mult, defesa):
    return max(1.0, atq * mult * 100.0 / (100.0 + defesa))


def contas(n):
    a = _json('dados', 'andares', 'a%03d.json' % n)
    p = perfil(n)
    h = heroi(p)
    nivel = int(a.get('nivel', n))
    linhas = []
    for mid in a.get('monstros', []):
        if mid not in MONSTROS:
            continue
        m = monstro(mid, nivel)
        linhas.append({'id': mid, 'tipo': m['tipo'], 'golpes_matar': m['hp'] / golpe(h['atq'], h['mult'], m['def']),
                       'golpes_aguenta': h['hp'] / golpe(m['atq'], 1.0, h['def'])})
    chefe = None
    if a.get('boss') and a['boss'] in BOSSES:
        b = BOSSES[a['boss']]
        chefe = monstro(b['id'], int(b.get('nivel', nivel + 3)), b['tipo'])
    elif a.get('guardiao'):
        chefe = monstro(a['guardiao'], nivel + 1, 'guardiao')
    if chefe:
        g = golpe(h['atq'], h['mult'], chefe['def'])
        chefe['golpes_matar'] = chefe['hp'] / g
        chefe['segundos'] = chefe['golpes_matar'] / (h['golpes_s'] * UPTIME)
        chefe['golpes_aguenta'] = h['hp'] / golpe(chefe['atq'], 1.0, h['def'])
    return p, h, linhas, chefe


def main():
    so = [int(x) for x in sys.argv[1:]]
    with open(os.path.join(RAIZ, 'testes', 'jogador_esperado.json'), 'w', encoding='utf-8') as f:
        json.dump({str(n): perfil(n) for n in range(1, 101)}, f, ensure_ascii=False, indent=1)
    print('andar nv | HP   DEF  ATQ | normal: golpes p/ matar (min–máx)  golpes que aguenta (min–máx) | chefe: tipo   HP     golpes  segundos  aguenta')
    for n in (so or range(1, 101)):
        p, h, linhas, chefe = contas(n)
        gm = [l['golpes_matar'] for l in linhas] or [0]
        ga = [l['golpes_aguenta'] for l in linhas] or [0]
        txt = '%5d %2d | %4d %4d %4d | %4.1f–%4.1f   %5.1f–%5.1f' % (n, p['nivel'], h['hp'], h['def'], h['atq'], min(gm), max(gm), min(ga), max(ga))
        if chefe:
            txt += ' | %-9s %7d %6.0f %6.0f s %6.1f' % (chefe['tipo'], chefe['hp'], chefe['golpes_matar'], chefe['segundos'], chefe['golpes_aguenta'])
        print(txt)
        if so:
            for l in linhas:
                print('        %-24s %-9s matar %4.1f  aguenta %5.1f' % (l['id'], l['tipo'], l['golpes_matar'], l['golpes_aguenta']))


if __name__ == '__main__':
    main()
