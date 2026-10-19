"""Músicas do jogo (docs/AUDIO.md, secção 2), compostas por código: chiptune com instrumentos "reais" por cima.

Cada faixa é um ciclo de 16 compassos (A A' B A'') que repete sem cortes: melodia com motivo que se repete,
baixo, harmonia (arpejo ou cordas) e bateria. O ambiente de cada faixa (andamento, modo, instrumentos) vem de FAIXAS.
Saída: musica/<nome>.ogg (o jogo toca-as com Audio.tocar_musica("nome"), em ciclo).

Uso: python3 ferramentas/som/musica.py [nome ...]      (sem nomes: todas)
"""
import os
import random
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
import sintetizador as S
from sintetizador import SR, onda, env, env_rapido, deslize, nota_hz

PASTA = os.path.join(os.path.dirname(__file__), '..', '..', 'musica')

MODOS = {
    'maior': [0, 2, 4, 5, 7, 9, 11], 'menor': [0, 2, 3, 5, 7, 8, 10], 'dorico': [0, 2, 3, 5, 7, 9, 10],
    'frigio': [0, 1, 3, 5, 7, 8, 10], 'lidio': [0, 2, 4, 6, 7, 9, 11], 'mixolidio': [0, 2, 4, 5, 7, 9, 10],
    'menor_harm': [0, 2, 3, 5, 7, 8, 11], 'arabe': [0, 1, 4, 5, 7, 8, 10], 'tons_inteiros': [0, 2, 4, 6, 8, 10, 0],
}
PROGS = {
    'heroica': [0, 5, 3, 4], 'calma': [0, 3, 0, 4], 'triste': [5, 3, 0, 4], 'misterio': [0, 1, 0, 6], 'tensa': [0, 6, 5, 4],
    'festa': [0, 4, 5, 3], 'marcha': [0, 3, 4, 0], 'sonho': [0, 2, 3, 1], 'epica': [5, 3, 0, 4], 'parada': [0, 0, 6, 6],
}


def suavizar(x, corte):
    """Passa-baixo rápido (média móvel): bom para cordas e pads."""
    k = max(1, int(SR / max(corte, 1) / 2))
    if k <= 1:
        return x
    return np.convolve(x, np.ones(k) / k, mode='same')


# ---------------- instrumentos (devolvem o som de uma nota) ----------------

def inst(nome, f, dur, vel=1.0):
    n = int(SR * dur)
    if n <= 8:
        return np.zeros(max(n, 0))
    if nome == 'quadrada':
        return onda('quadrada', f, dur, 0.25) * env(n, 0.004, 0.06, 0.55, 0.05) * 0.32 * vel
    if nome == 'quadrada_fina':
        return onda('quadrada', f, dur, 0.125) * env(n, 0.003, 0.05, 0.5, 0.05) * 0.3 * vel
    if nome == 'flauta':
        x = onda('seno', S.vibrato(f, dur, 0.008, 5.0, 0.12), dur) + 0.25 * onda('triangulo', f * 2, dur)
        sopro = onda('ruido', 3000, dur, semente=int(f)) * 0.04
        return (x * 0.55 + sopro) * env(n, 0.05, 0.1, 0.8, 0.12) * 0.45 * vel
    if nome == 'cordas':
        x = onda('serra', S.vibrato(f, dur, 0.005, 5.5, 0.2), dur) + onda('serra', f * 1.004, dur)
        return suavizar(x, 1800) * env(n, 0.12, 0.2, 0.8, 0.25) * 0.16 * vel
    if nome == 'piano':
        x = onda('triangulo', f, dur) + 0.3 * onda('seno', f * 2, dur) + 0.1 * onda('quadrada', f, dur, 0.5)
        return x * env_rapido(n, 0.003, 3.2) * 0.42 * vel
    if nome == 'alaude':
        x = onda('quadrada', f, dur, 0.5) * 0.6 + onda('triangulo', f * 2, dur) * 0.4
        return suavizar(x, 2500) * env_rapido(n, 0.002, 5.0) * 0.45 * vel
    if nome == 'sino':
        x = onda('seno', f, dur) + 0.4 * onda('seno', f * 2.76, dur) * env_rapido(n, 0.001, 6)
        return x * env_rapido(n, 0.002, 2.2) * 0.32 * vel
    if nome == 'orgao':
        x = onda('seno', f, dur) + 0.5 * onda('seno', f * 2, dur) + 0.3 * onda('seno', f * 3, dur) + 0.2 * onda('quadrada', f / 2, dur, 0.5)
        return x * env(n, 0.03, 0.1, 0.9, 0.12) * 0.2 * vel
    if nome == 'caixa_musica':
        return (onda('seno', f * 2, dur) + 0.3 * onda('seno', f * 6, dur)) * env_rapido(n, 0.001, 5) * 0.3 * vel
    if nome == 'baixo':
        return onda('triangulo_nes', f, dur) * env(n, 0.004, 0.05, 0.8, 0.04) * 0.55 * vel
    if nome == 'baixo_quadrado':
        return onda('quadrada', f, dur, 0.5) * env(n, 0.004, 0.08, 0.6, 0.04) * 0.25 * vel
    if nome == 'pad':
        x = onda('serra', f, dur) + onda('serra', f * 1.007, dur) + onda('serra', f * 0.993, dur)
        return suavizar(x, 900) * env(n, 0.4, 0.3, 0.8, 0.4) * 0.07 * vel
    raise ValueError(nome)


def bombo(vel=1.0):
    d = 0.18
    return onda('seno', deslize(150, 45, d, 0.5), d) * env_rapido(int(SR * d), 0.001, 16) * 0.9 * vel


def tarola(vel=1.0):
    d = 0.16
    return (onda('ruido', 6000, d, semente=3) * 0.7 + onda('triangulo', 190, d) * 0.3) * env_rapido(int(SR * d), 0.001, 20) * 0.5 * vel


def prato(vel=1.0, aberto=False):
    d = 0.25 if aberto else 0.05
    x = onda('ruido', 11000, d, semente=5)
    x = x - suavizar(x, 4000)
    return x * env_rapido(int(SR * d), 0.001, 8 if aberto else 60) * 0.35 * vel


def tambor(vel=1.0):
    d = 0.22
    return onda('seno', deslize(220, 110, d, 0.6), d) * env_rapido(int(SR * d), 0.001, 12) * 0.6 * vel


# padrões de bateria (16 semicolcheias por compasso): k bombo, s tarola, h prato, t tambor
BATERIAS = {
    'nenhuma': '',
    'leve': 'k...h...s...h...',
    'pop': 'k.h.s.h.k.hks.h.',
    'marcha': 'k.s.k.s.k.s.kss.',
    'rapida': 'khshkhshkhshkhsh',
    'tribal': 't..t..t.t.t.t...',
    'valsa': 'k...h...h...k...',
    'taberna': 'k.h.s.h.k.h.s.hh',
    'batalha': 'k.hkshk.k.hkshkk',
}


# ---------------- compositor ----------------

def compor(nome, bpm=100, modo='maior', raiz=60, prog='heroica', lead='quadrada', harm='arpejo', harm_inst='quadrada_fina',
           baixo='baixo', bateria='pop', densidade=0.6, oitava_lead=12, eco_lead=True, semente=None, compassos=16):
    rnd = random.Random(semente if semente is not None else sum(map(ord, nome)) * 7)
    escala = MODOS[modo]
    graus = PROGS[prog] if isinstance(prog, str) else prog
    batida = 60.0 / bpm
    semi = batida / 4
    dur_total = compassos * 4 * batida
    buf = np.zeros(int(SR * dur_total) + SR * 3)

    def grau_nota(g, oitava=0):
        return raiz + escala[g % 7] + 12 * (g // 7) + 12 * oitava

    def acorde(g):
        return [grau_nota(g), grau_nota(g + 2), grau_nota(g + 4)]

    def por(som, t):
        S.colocar(buf, som, t)

    # ---- motivos da melodia (ritmo em semicolcheias + passos na escala) ----
    def motivo():
        ritmos = [[4, 4, 4, 4], [2, 2, 4, 8], [6, 2, 4, 4], [4, 2, 2, 8], [3, 3, 2, 8], [8, 4, 4], [2, 2, 2, 2, 8], [4, 4, 8],
                  [12, 4], [2, 2, 4, 4, 4]]
        if densidade < 0.4:
            ritmos = [r for r in ritmos if len(r) <= 3] or ritmos
        r1, r2 = rnd.choice(ritmos), rnd.choice(ritmos)
        passos = [rnd.choice([-2, -1, -1, 0, 1, 1, 2, 3, -3]) for _ in range(len(r1) + len(r2))]
        return r1, r2, passos

    A = motivo()
    B = motivo()
    prog16 = (graus * 4)[:compassos]
    secoes = ['A', 'A', 'B', 'A']
    for c in range(compassos):
        g = prog16[c]
        t0 = c * 4 * batida
        sec = secoes[(c // 4) % 4]
        # ---- baixo ----
        nb = grau_nota(g, -2)
        if baixo:
            padrao = [0, 8] if bateria in ('nenhuma', 'valsa') else ([0, 6, 8, 14] if bateria in ('rapida', 'batalha') else [0, 4, 8, 12])
            for i, p in enumerate(padrao):
                n = nb + (12 if (i % 2 and bateria not in ('nenhuma',)) else 0) * (1 if bateria in ('pop', 'taberna', 'rapida', 'batalha') else 0)
                por(inst(baixo, nota_hz(n), semi * (4 if len(padrao) == 4 else 7)), t0 + p * semi)
        # ---- harmonia ----
        ac = acorde(g)
        if harm == 'arpejo':
            ordem = ac + [ac[1]]
            for k in range(16 if bpm < 140 else 8):
                passo_ = 1 if bpm < 140 else 2
                por(inst(harm_inst, nota_hz(ordem[k % 4] + 12), semi * passo_ * 0.9, 0.55), t0 + k * semi * passo_)
        elif harm == 'acordes':
            for n in ac:
                por(inst(harm_inst, nota_hz(n), 4 * batida * 0.98, 0.5), t0)
        elif harm == 'batidas':   # acordes curtos no tempo fraco (taberna, festa)
            for k in (2, 6, 10, 14):
                for n in ac:
                    por(inst(harm_inst, nota_hz(n + 12), semi * 1.5, 0.45), t0 + k * semi)
        # ---- melodia ----
        if lead and not (sec == 'A' and c < 1 and densidade < 0.3):
            ritmo, ritmo2, passos = A if sec == 'A' else B
            r = ritmo if c % 2 == 0 else ritmo2
            # a melodia começa numa nota do acorde e anda pela escala
            gi = g + rnd.choice([0, 2, 4]) if c % 4 == 0 else g + [0, 2, 4][c % 3]
            tt = t0
            ultimo = c == compassos - 1
            for i, d in enumerate(r):
                if rnd.random() > densidade + 0.35 and i > 0:
                    tt += d * semi
                    continue
                gi_n = gi + passos[(i + (c % 2) * len(ritmo)) % len(passos)]
                if ultimo and i == len(r) - 1:
                    gi_n = g   # acaba no acorde (para o ciclo voltar bem)
                nota = grau_nota(gi_n) + oitava_lead
                por(inst(lead, nota_hz(nota), d * semi * 0.95), tt)
                gi = gi_n
                tt += d * semi
        # ---- bateria ----
        pad = BATERIAS.get(bateria, '')
        for k, ch in enumerate(pad):
            tk = t0 + k * semi
            if ch == 'k':
                por(bombo(), tk)
            elif ch == 's':
                por(tarola(), tk)
            elif ch == 'h':
                por(prato(0.7 if k % 4 else 1.0), tk)
            elif ch == 't':
                por(tambor(), tk)
        if bateria not in ('nenhuma', '') and c % 4 == 3:
            por(prato(0.8, True), t0 + 15 * semi)
    # ciclo: o que passa do fim volta ao início
    n = int(SR * dur_total)
    cauda = buf[n:]
    buf = buf[:n].copy()
    buf[:len(cauda)] += cauda[:n]
    if eco_lead:
        k = int(SR * batida * 0.75)
        eco_ = np.roll(buf, k) * 0.18
        buf = buf + eco_
    return S.normalizar(buf, 0.85)


# ---------------- as faixas ----------------

def regiao(prefixo, base, extras):
    """4 faixas por região: _1 exploração de dia, _2 variante, _3 perigo/fundo, _4 especial (povoação/masmorra)."""
    out = {}
    out[f'{prefixo}_1'] = dict(base)
    out[f'{prefixo}_2'] = dict(base, prog=extras.get('prog2', 'calma'), lead=extras.get('lead2', base.get('lead')), densidade=0.45,
                               bpm=int(base['bpm'] * 0.9), semente=2)
    out[f'{prefixo}_3'] = dict(base, modo=extras.get('modo3', 'menor'), prog='tensa', bateria=extras.get('bat3', 'batalha'),
                               bpm=int(base['bpm'] * 1.2), harm='arpejo', semente=3)
    out[f'{prefixo}_4'] = dict(base, **extras.get('esp', {}), semente=4)
    return out


FAIXAS = {}
FAIXAS.update(regiao('floresta', dict(bpm=104, modo='maior', raiz=62, prog='heroica', lead='flauta', harm='arpejo', bateria='leve'),
                     dict(prog2='calma', lead2='piano', esp=dict(lead='alaude', bateria='taberna', harm='batidas', harm_inst='alaude'))))
FAIXAS.update(regiao('cavernas', dict(bpm=88, modo='dorico', raiz=57, prog='misterio', lead='sino', harm='acordes', harm_inst='pad', bateria='leve'),
                     dict(lead2='piano', esp=dict(lead='quadrada', bateria='marcha', harm='arpejo', harm_inst='quadrada_fina', modo='mixolidio'))))
FAIXAS.update(regiao('pantano', dict(bpm=96, modo='dorico', raiz=55, prog='sonho', lead='flauta', harm='acordes', harm_inst='pad', bateria='tribal'),
                     dict(lead2='alaude', esp=dict(bateria='tribal', lead='orgao', modo='frigio'))))
FAIXAS.update(regiao('deserto', dict(bpm=100, modo='arabe', raiz=62, prog='misterio', lead='flauta', harm='arpejo', harm_inst='alaude', bateria='tribal'),
                     dict(modo3='arabe', esp=dict(lead='alaude', bateria='taberna', harm='batidas', harm_inst='alaude'))))
FAIXAS.update(regiao('gelo', dict(bpm=84, modo='lidio', raiz=64, prog='sonho', lead='sino', harm='acordes', harm_inst='cordas', bateria='nenhuma'),
                     dict(lead2='piano', esp=dict(lead='flauta', bateria='leve', modo='maior', prog='calma'))))
FAIXAS.update(regiao('oceano', dict(bpm=108, modo='mixolidio', raiz=60, prog='festa', lead='quadrada', harm='batidas', harm_inst='alaude', bateria='taberna'),
                     dict(lead2='flauta', esp=dict(lead='sino', bateria='nenhuma', modo='lidio', harm='acordes', harm_inst='pad', bpm=72))))
FAIXAS.update(regiao('vulcao', dict(bpm=126, modo='frigio', raiz=52, prog='tensa', lead='quadrada', harm='arpejo', harm_inst='quadrada_fina', bateria='batalha',
                                    baixo='baixo_quadrado'),
                     dict(prog2='parada', lead2='orgao', modo3='menor_harm', esp=dict(lead='orgao', bateria='marcha', harm='acordes', harm_inst='cordas'))))
FAIXAS.update(regiao('assombrado', dict(bpm=90, modo='menor_harm', raiz=57, prog='triste', lead='caixa_musica', harm='acordes', harm_inst='orgao', bateria='valsa'),
                     dict(lead2='orgao', esp=dict(lead='orgao', harm='acordes', harm_inst='cordas', bateria='nenhuma', bpm=70))))
FAIXAS.update(regiao('ceu', dict(bpm=112, modo='lidio', raiz=65, prog='epica', lead='flauta', harm='arpejo', harm_inst='quadrada_fina', bateria='pop'),
                     dict(lead2='sino', esp=dict(lead='cordas', harm='acordes', harm_inst='pad', bateria='leve'))))
FAIXAS.update(regiao('abismo', dict(bpm=76, modo='tons_inteiros', raiz=58, prog='misterio', lead='sino', harm='acordes', harm_inst='pad', bateria='nenhuma'),
                     dict(lead2='piano', modo3='frigio', esp=dict(lead='piano', modo='menor', prog='triste'))))

BOSS = dict(bpm=150, modo='menor_harm', prog='tensa', lead='quadrada', harm='arpejo', harm_inst='quadrada_fina', bateria='batalha', baixo='baixo_quadrado')
for i, (b, extra) in enumerate({
    'javali_rei': dict(raiz=55, modo='menor'), 'ent_anciao': dict(raiz=50, lead='orgao', bpm=132, modo='dorico'),
    'aranha_mae': dict(raiz=57, modo='frigio'), 'golem_de_cristal': dict(raiz=52, lead='sino', bpm=138),
    'serpente_do_lodo': dict(raiz=53, modo='dorico', bateria='tribal'), 'hidra_do_pantano': dict(raiz=50, bpm=156),
    'escorpiao_imperador': dict(raiz=55, modo='arabe'), 'farao_eterno': dict(raiz=50, modo='arabe', lead='orgao', bpm=140),
    'yeti_anciao': dict(raiz=52, bpm=144), 'dragao_de_gelo': dict(raiz=57, lead='cordas', bpm=160, prog='epica'),
    'capitao_esqueleto': dict(raiz=55, bateria='taberna', modo='menor'), 'leviata': dict(raiz=48, lead='cordas', prog='epica', bpm=132),
    'ferreiro_infernal': dict(raiz=52, modo='frigio', bateria='marcha'), 'kai': dict(raiz=57, modo='menor', prog='triste', lead='quadrada', bpm=144),
    'tita_de_magma': dict(raiz=48, modo='frigio', lead='orgao', bpm=136), 'lich_bibliotecario': dict(raiz=53, lead='orgao', bateria='valsa', bpm=150),
    'rei_sem_coroa': dict(raiz=50, lead='cordas', prog='epica', bateria='marcha'), 'grifo_real': dict(raiz=57, modo='mixolidio', prog='heroica', bpm=152),
    'serafim_caido': dict(raiz=55, lead='orgao', prog='epica', bpm=138), 'guardiao_do_tempo': dict(raiz=52, lead='caixa_musica', bpm=144),
    'administrador': dict(raiz=50, modo='tons_inteiros', lead='piano', prog='misterio', bateria='leve', bpm=96),
    'guardiao': dict(raiz=55, bpm=146), 'boss_desperto': dict(raiz=49, modo='frigio', lead='orgao', bpm=162),
}.items()):
    FAIXAS[b] = dict(BOSS, **extra, semente=10 + i)

FAIXAS.update({
    'menu': dict(bpm=80, modo='menor', raiz=57, prog='epica', lead='cordas', harm='arpejo', harm_inst='piano', bateria='nenhuma', densidade=0.4),
    'tema_principal': dict(bpm=92, modo='maior', raiz=60, prog='epica', lead='flauta', harm='acordes', harm_inst='cordas', bateria='marcha'),
    'prologo': dict(bpm=72, modo='dorico', raiz=57, prog='misterio', lead='sino', harm='acordes', harm_inst='pad', bateria='nenhuma', densidade=0.35),
    'ascendia_dia': dict(bpm=110, modo='maior', raiz=60, prog='festa', lead='flauta', harm='batidas', harm_inst='alaude', bateria='pop'),
    'ascendia_noite': dict(bpm=80, modo='maior', raiz=60, prog='calma', lead='piano', harm='acordes', harm_inst='pad', bateria='nenhuma', densidade=0.4),
    'taberna': dict(bpm=128, modo='mixolidio', raiz=62, prog='festa', lead='alaude', harm='batidas', harm_inst='alaude', bateria='taberna'),
    'guilda': dict(bpm=112, modo='dorico', raiz=60, prog='marcha', lead='quadrada', harm='arpejo', bateria='marcha'),
    'casa': dict(bpm=76, modo='maior', raiz=65, prog='calma', lead='piano', harm='acordes', harm_inst='pad', bateria='nenhuma', densidade=0.4),
    'festival': dict(bpm=124, modo='maior', raiz=62, prog='festa', lead='flauta', harm='batidas', harm_inst='alaude', bateria='taberna'),
    'dia_da_subida': dict(bpm=116, modo='maior', raiz=60, prog='heroica', lead='quadrada', harm='arpejo', bateria='marcha'),
    'cidade_errante': dict(bpm=118, modo='arabe', raiz=60, prog='festa', lead='orgao', harm='batidas', harm_inst='alaude', bateria='tribal'),
    'forja': dict(bpm=100, modo='menor', raiz=50, prog='marcha', lead='cordas', harm='acordes', harm_inst='orgao', bateria='marcha'),
    'lanternas_rio': dict(bpm=70, modo='lidio', raiz=64, prog='sonho', lead='flauta', harm='arpejo', harm_inst='sino', bateria='nenhuma', densidade=0.4),
    'invasao': dict(bpm=150, modo='menor', raiz=57, prog='tensa', lead='quadrada', harm='arpejo', bateria='rapida'),
    'tristeza': dict(bpm=64, modo='menor', raiz=57, prog='triste', lead='piano', harm='acordes', harm_inst='cordas', bateria='nenhuma', densidade=0.35),
    'revelacao': dict(bpm=72, modo='tons_inteiros', raiz=55, prog='misterio', lead='sino', harm='acordes', harm_inst='pad', bateria='nenhuma'),
    'amizade': dict(bpm=84, modo='maior', raiz=65, prog='calma', lead='flauta', harm='arpejo', harm_inst='piano', bateria='nenhuma'),
    'morte': dict(bpm=60, modo='menor', raiz=52, prog='triste', lead='piano', harm='acordes', harm_inst='cordas', bateria='nenhuma', compassos=4),
    'finais': dict(bpm=76, modo='maior', raiz=60, prog='epica', lead='cordas', harm='arpejo', harm_inst='piano', bateria='leve'),
})
TEMAS_NPC = {   # docs/AUDIO.md: um tema curto por NPC de Ascendia
    'lyra': ('piano', 'maior', 67), 'gorvan': ('cordas', 'dorico', 48), 'brom': ('orgao', 'mixolidio', 55), 'selene': ('caixa_musica', 'lidio', 64),
    'tobias': ('alaude', 'maior', 60), 'marta': ('alaude', 'maior', 57), 'kai': ('quadrada', 'dorico', 57), 'mia': ('flauta', 'maior', 72),
    'celia': ('piano', 'lidio', 65), 'fausto': ('orgao', 'menor', 53), 'rook': ('quadrada', 'menor', 55), 'freya': ('cordas', 'mixolidio', 57),
    'pip': ('alaude', 'mixolidio', 62), 'hana': ('flauta', 'dorico', 64), 'zed': ('alaude', 'maior', 55), 'oriel': ('sino', 'lidio', 69),
    'lucien': ('cordas', 'menor', 52), 'gizmo': ('quadrada_fina', 'mixolidio', 64), 'elva': ('sino', 'dorico', 67), 'aldric': ('cordas', 'maior', 55),
}
for i, (npc, (ld, md, rz)) in enumerate(TEMAS_NPC.items()):
    FAIXAS[f'tema_{npc}'] = dict(bpm=88, modo=md, raiz=rz, prog='calma' if md in ('maior', 'lidio', 'mixolidio') else 'triste', lead=ld,
                                 harm='arpejo', harm_inst='piano' if ld != 'piano' else 'sino', bateria='nenhuma', densidade=0.5, semente=50 + i)


def gerar(nomes=None):
    feitos = 0
    for nome, cfg in FAIXAS.items():
        if nomes and nome not in nomes:
            continue
        x = compor(nome, **cfg)
        S.gravar_ogg(x, os.path.join(PASTA, f'{nome}.ogg'), qualidade=1, ciclo=True)
        feitos += 1
        print('  ', nome, f'{len(x) / SR:.0f} s')
    print('ok', feitos, 'músicas')


if __name__ == '__main__':
    gerar(sys.argv[1:] or None)
