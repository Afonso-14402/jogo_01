"""Efeitos sonoros do jogo (docs/AUDIO.md, secção 3), feitos por código com o sintetizador.

Cada efeito é uma função que devolve o som (array). Saída: sons/<nome>.ogg (o jogo toca-os com Audio.efeito("nome")).
Uso: python3 ferramentas/som/efeitos.py [nome ...]   (sem nomes: todos)
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
import sintetizador as S
from sintetizador import SR, onda, env, env_rapido, deslize, passa_baixo, passa_alto, eco, misturar, colocar, nota_hz

PASTA = os.path.join(os.path.dirname(__file__), '..', '..', 'sons')


# ---------------- blocos ----------------

def tom(tipo, f0, f1=None, dur=0.15, duty=0.5, a=0.002, queda=None, s=0.5, vol=1.0, curva=1.0):
    f = deslize(f0, f1 if f1 else f0, dur, curva) if f1 else f0
    x = onda(tipo, f, dur, duty)
    n = len(x)
    e = env_rapido(n, a, queda) if queda else env(n, a, 0.04, s, min(0.08, dur / 2))
    return x * e * vol


def ruido(f0, f1=None, dur=0.15, queda=12.0, corte=None, alto=None, vol=1.0, semente=1):
    f = deslize(f0, f1 if f1 else f0, dur) if f1 else f0
    x = onda('ruido', f, dur, semente=semente)
    if corte:
        x = passa_baixo(x, corte)
    if alto:
        x = passa_alto(x, alto)
    return x * env_rapido(len(x), 0.001, queda) * vol


def jingle(notas, passo=0.08, tipo='quadrada', duty=0.25, queda=6.0, vol=0.8, eco_=True):
    """notas: lista de MIDI (ou None = pausa)."""
    buf = np.zeros(int(SR * (passo * len(notas) + 0.6)))
    for i, n in enumerate(notas):
        if n is None:
            continue
        som = tom(tipo, nota_hz(n), dur=passo * 2.2, duty=duty, queda=queda, vol=vol)
        colocar(buf, som, i * passo)
    return eco(buf, 0.12, 0.25, 2) if eco_ else buf


# ---------------- herói ----------------

def passo(f, corte, vol=0.5, sem=1):
    return ruido(f, f * 0.6, 0.07, 40, corte=corte, vol=vol, semente=sem)


EFEITOS = {
    # passos (duas variantes cada: o jogo alterna)
    'passo_relva_1': lambda: passo(5000, 2500, 0.35, 1), 'passo_relva_2': lambda: passo(4500, 2200, 0.35, 2),
    'passo_pedra_1': lambda: misturar(passo(2500, 4000, 0.5, 3), tom('triangulo', 180, 120, 0.04, queda=60, vol=0.3)),
    'passo_pedra_2': lambda: misturar(passo(2300, 4000, 0.5, 4), tom('triangulo', 170, 110, 0.04, queda=60, vol=0.3)),
    'passo_areia_1': lambda: passo(7000, 1800, 0.35, 5), 'passo_areia_2': lambda: passo(6500, 1700, 0.35, 6),
    'passo_neve_1': lambda: ruido(3000, 1500, 0.11, 22, corte=1400, vol=0.5, semente=7),
    'passo_neve_2': lambda: ruido(2800, 1400, 0.11, 22, corte=1300, vol=0.5, semente=8),
    'passo_agua_1': lambda: misturar(ruido(4000, 2000, 0.12, 18, corte=3000, vol=0.4, semente=9), tom('seno', 600, 1200, 0.06, queda=40, vol=0.2)),
    'passo_agua_2': lambda: misturar(ruido(3800, 1900, 0.12, 18, corte=3000, vol=0.4, semente=10), tom('seno', 550, 1100, 0.06, queda=40, vol=0.2)),
    'passo_madeira_1': lambda: misturar(tom('triangulo', 220, 160, 0.06, queda=45, vol=0.6), passo(2000, 2500, 0.25, 11)),
    'passo_madeira_2': lambda: misturar(tom('triangulo', 200, 150, 0.06, queda=45, vol=0.6), passo(1900, 2500, 0.25, 12)),
    'esquiva': lambda: ruido(1500, 6000, 0.18, 10, alto=800, vol=0.5),
    'saltar': lambda: tom('quadrada', 300, 700, 0.12, duty=0.25, queda=14, vol=0.4),
    'dano_heroi': lambda: misturar(tom('quadrada', 420, 140, 0.18, duty=0.5, queda=12, vol=0.6), ruido(1200, 400, 0.12, 20, vol=0.4)),
    'morrer': lambda: misturar(jingle([67, 63, 60, 55, 51], 0.14, 'triangulo', queda=3, vol=0.9, eco_=True),
                               tom('quadrada', 300, 60, 0.9, duty=0.5, queda=3, vol=0.25)),
    'subir_nivel': lambda: jingle([60, 64, 67, 72, 76, 79, 84], 0.06, 'quadrada', 0.25, 4, 0.7),
    'beber_pocao': lambda: misturar(*[S.np.pad(tom('seno', 500 + i * 90, 700 + i * 90, 0.07, queda=25, vol=0.5), (int(SR * i * 0.07), 0))
                                      for i in range(5)]),
    'comer': lambda: misturar(ruido(3000, 2000, 0.06, 30, corte=2500, vol=0.5), S.np.pad(ruido(2800, 1800, 0.06, 30, corte=2500, vol=0.5, semente=3), (int(SR * 0.14), 0))),
    'planar': lambda: ruido(800, 1200, 0.6, 2.5, corte=1500, vol=0.4),
    'nadar': lambda: ruido(2500, 1200, 0.25, 9, corte=2200, vol=0.45),

    # armas
    'corte': lambda: ruido(800, 5000, 0.14, 16, alto=600, vol=0.6),
    'corte_pesado': lambda: misturar(ruido(500, 3500, 0.22, 10, alto=300, vol=0.7), tom('triangulo', 160, 80, 0.15, queda=12, vol=0.3)),
    'estocada': lambda: ruido(2500, 7000, 0.09, 26, alto=1200, vol=0.55),
    'katana_iai': lambda: misturar(ruido(1000, 9000, 0.1, 20, alto=1500, vol=0.6), tom('seno', 2400, 3200, 0.3, queda=9, vol=0.15)),
    'impacto_martelo': lambda: misturar(tom('seno', 140, 50, 0.25, queda=11, vol=0.9), ruido(900, 300, 0.15, 18, vol=0.6)),
    'machado': lambda: misturar(ruido(700, 2500, 0.16, 14, alto=400, vol=0.6), tom('triangulo', 200, 110, 0.1, queda=20, vol=0.3)),
    'arco_esticar': lambda: tom('serra', 120, 180, 0.3, s=0.3, vol=0.15),
    'arco_disparar': lambda: misturar(tom('triangulo', 330, 180, 0.12, queda=20, vol=0.5), ruido(5000, 8000, 0.15, 14, alto=3000, vol=0.3)),
    'besta_recarregar': lambda: misturar(tom('quadrada', 900, None, 0.03, duty=0.5, queda=80, vol=0.4),
                                         S.np.pad(tom('quadrada', 700, None, 0.03, duty=0.5, queda=80, vol=0.4), (int(SR * 0.12), 0))),
    'besta_disparar': lambda: misturar(tom('quadrada', 220, 90, 0.08, duty=0.5, queda=30, vol=0.5), ruido(3000, 6000, 0.1, 25, alto=2000, vol=0.35)),
    'soco': lambda: misturar(tom('seno', 180, 70, 0.1, queda=25, vol=0.8), ruido(1500, 500, 0.06, 40, vol=0.5)),
    'feitico_fogo': lambda: misturar(ruido(600, 2500, 0.4, 5, corte=2500, vol=0.6), tom('serra', 200, 400, 0.3, queda=7, vol=0.15)),
    'feitico_gelo': lambda: misturar(*[S.np.pad(tom('seno', f, None, 0.25, queda=10, vol=0.35), (int(SR * i * 0.04), 0))
                                       for i, f in enumerate((1568, 2093, 2637, 3136))]),
    'feitico_raio': lambda: misturar(ruido(9000, 2000, 0.35, 8, vol=0.6), tom('quadrada', 1800, 300, 0.25, duty=0.1, queda=10, vol=0.25)),
    'feitico_veneno': lambda: misturar(*[S.np.pad(tom('seno', 300 + 80 * (i % 3), 500, 0.08, queda=30, vol=0.4), (int(SR * i * 0.06), 0)) for i in range(6)]),
    'feitico_luz': lambda: jingle([84, 88, 91, 96], 0.05, 'seno', 0.5, 5, 0.6),
    'feitico_sombra': lambda: misturar(tom('serra', 110, 55, 0.5, queda=4, vol=0.4), ruido(400, 200, 0.5, 4, corte=600, vol=0.4)),

    # impactos
    'acerto': lambda: misturar(ruido(2000, 600, 0.08, 35, vol=0.7), tom('quadrada', 300, 150, 0.06, duty=0.5, queda=40, vol=0.35)),
    'critico': lambda: misturar(ruido(3000, 800, 0.14, 18, vol=0.8), tom('quadrada', 900, 1800, 0.12, duty=0.25, queda=14, vol=0.4)),
    'bloqueado': lambda: misturar(tom('quadrada', 1200, 1150, 0.12, duty=0.5, queda=20, vol=0.35), tom('quadrada', 1810, None, 0.1, duty=0.5, queda=25, vol=0.2)),
    'imune': lambda: tom('triangulo', 400, 380, 0.2, queda=12, vol=0.4),
    'monstro_morre': lambda: misturar(ruido(1500, 200, 0.35, 7, vol=0.6), tom('quadrada', 400, 80, 0.3, duty=0.5, queda=8, vol=0.3)),
    'boss_fase': lambda: misturar(tom('serra', 80, 40, 1.0, queda=2.5, vol=0.7), ruido(300, 100, 1.0, 3, corte=500, vol=0.5)),
    'boss_rugido': lambda: misturar(passa_baixo(onda('serra', S.vibrato(90, 0.9, 0.08, 18), 0.9), 900) * env(int(SR * 0.9), 0.05, 0.2, 0.7, 0.3),
                                    ruido(500, 200, 0.9, 3, corte=800, vol=0.5)),

    # estados
    'envenenado': lambda: misturar(*[S.np.pad(tom('seno', 220, 330, 0.07, queda=25, vol=0.4), (int(SR * i * 0.09), 0)) for i in range(3)]),
    'a_arder': lambda: ruido(1200, 2400, 0.3, 7, corte=3000, vol=0.5),
    'congelar': lambda: misturar(ruido(8000, 4000, 0.3, 9, alto=3000, vol=0.4), tom('seno', 2500, 2000, 0.3, queda=9, vol=0.2)),
    'atordoado': lambda: misturar(*[S.np.pad(tom('triangulo', 1200 if i % 2 else 1500, None, 0.06, queda=25, vol=0.3), (int(SR * i * 0.08), 0)) for i in range(4)]),

    # mundo
    'bau_madeira': lambda: misturar(tom('triangulo', 160, 240, 0.25, queda=8, vol=0.5), S.np.pad(jingle([72, 76, 79], 0.06, 'quadrada', 0.25, 6, 0.4, False), (int(SR * 0.2), 0))),
    'bau_prata': lambda: misturar(tom('triangulo', 180, 260, 0.2, queda=9, vol=0.5), S.np.pad(jingle([76, 79, 83, 88], 0.06, 'quadrada', 0.25, 6, 0.45), (int(SR * 0.18), 0))),
    'bau_ouro': lambda: misturar(tom('triangulo', 200, 300, 0.2, queda=9, vol=0.5), S.np.pad(jingle([72, 76, 79, 84, 88, 91], 0.06, 'quadrada', 0.25, 5, 0.5), (int(SR * 0.18), 0))),
    'mimico': lambda: misturar(tom('serra', 300, 90, 0.4, queda=6, vol=0.5), ruido(800, 300, 0.4, 6, corte=1200, vol=0.5)),
    'porta': lambda: misturar(tom('serra', 90, 140, 0.45, s=0.4, vol=0.25), ruido(600, 300, 0.2, 8, corte=900, vol=0.4)),
    'alavanca': lambda: misturar(tom('quadrada', 300, 200, 0.06, duty=0.5, queda=40, vol=0.4), S.np.pad(ruido(2000, 800, 0.08, 30, vol=0.4), (int(SR * 0.08), 0))),
    'clique': lambda: tom('quadrada', 1600, 1200, 0.03, duty=0.5, queda=90, vol=0.4),
    'placa_pressao': lambda: misturar(tom('triangulo', 120, 90, 0.12, queda=20, vol=0.6), ruido(800, 400, 0.08, 30, vol=0.3)),
    'cristal_teletransporte': lambda: misturar(jingle([79, 86, 91, 98, 91, 86], 0.07, 'seno', 0.5, 4, 0.5), ruido(6000, 9000, 0.8, 3, alto=4000, vol=0.15)),
    'apanhar': lambda: jingle([84, 91], 0.05, 'quadrada', 0.25, 12, 0.45, False),
    'moeda': lambda: jingle([88, 95], 0.045, 'quadrada', 0.5, 10, 0.4, False),
    'recolher_minerio': lambda: misturar(tom('quadrada', 1400, 1350, 0.12, duty=0.5, queda=25, vol=0.3), ruido(3000, 1200, 0.08, 30, vol=0.4)),
    'recolher_madeira': lambda: misturar(tom('triangulo', 260, 180, 0.08, queda=30, vol=0.6), ruido(1800, 900, 0.07, 30, vol=0.35)),
    'recolher_erva': lambda: ruido(5000, 3000, 0.12, 20, alto=2000, vol=0.4),
    'pancada': lambda: misturar(tom('seno', 120, 60, 0.18, queda=14, vol=0.8), ruido(700, 300, 0.1, 25, vol=0.5)),
    'bolha': lambda: tom('seno', 300, 900, 0.09, queda=20, vol=0.5, curva=0.5),
    'dado': lambda: misturar(*[S.np.pad(tom('triangulo', 900 + 130 * i, None, 0.03, queda=80, vol=0.4), (int(SR * i * 0.07), 0)) for i in range(4)]),
    'sino': lambda: misturar(tom('seno', 880, None, 1.5, queda=2, vol=0.5), tom('seno', 2210, None, 1.0, queda=3, vol=0.2)),

    # interface
    'abrir_janela': lambda: jingle([79, 86], 0.04, 'quadrada', 0.125, 14, 0.35, False),
    'fechar_janela': lambda: jingle([86, 79], 0.04, 'quadrada', 0.125, 14, 0.35, False),
    'cursor': lambda: tom('quadrada', 1760, None, 0.025, duty=0.25, queda=120, vol=0.25),
    'aceitar': lambda: jingle([84, 88], 0.04, 'quadrada', 0.25, 16, 0.35, False),
    'recusar': lambda: jingle([62, 58], 0.06, 'quadrada', 0.5, 12, 0.35, False),
    'sem_dinheiro': lambda: jingle([55, 55], 0.08, 'quadrada', 0.5, 10, 0.35, False),
    'comprar': lambda: jingle([84, 88, 96], 0.045, 'quadrada', 0.5, 10, 0.4, False),
    'vender': lambda: jingle([96, 91, 88], 0.045, 'quadrada', 0.5, 10, 0.4, False),
    'equipar': lambda: misturar(tom('quadrada', 600, 900, 0.06, duty=0.5, queda=30, vol=0.3), ruido(2500, 1500, 0.05, 40, vol=0.3)),
    'melhoria_ok': lambda: jingle([72, 79, 84, 88, 91, 96], 0.05, 'quadrada', 0.25, 6, 0.5),
    'melhoria_falhada': lambda: misturar(jingle([67, 61], 0.12, 'quadrada', 0.5, 6, 0.4, False), ruido(1500, 300, 0.4, 7, vol=0.3)),
    'notificacao': lambda: jingle([81, 88], 0.06, 'seno', 0.5, 8, 0.45, True),
    'missao_concluida': lambda: jingle([72, 76, 79, 84, None, 79, 84], 0.08, 'quadrada', 0.25, 5, 0.55),
    'monstro_com_nome': lambda: misturar(jingle([60, 63, 66, 69], 0.1, 'serra', 0.5, 4, 0.35), tom('seno', 80, 60, 0.8, queda=3, vol=0.5)),
    'vitoria': lambda: jingle([67, 67, 67, 72, None, 70, 72, None, 76, 79], 0.09, 'quadrada', 0.25, 4, 0.55),
    'mensagem_sistema': lambda: jingle([93, 98], 0.035, 'quadrada', 0.125, 20, 0.3, False),

    # pesca e quinta
    'pesca_lancar': lambda: misturar(ruido(1500, 5000, 0.2, 9, alto=1000, vol=0.4), S.np.pad(tom('seno', 500, 300, 0.1, queda=20, vol=0.4), (int(SR * 0.3), 0))),
    'pesca_boia': lambda: tom('seno', 700, 1100, 0.08, queda=25, vol=0.4),
    'pesca_mordida': lambda: jingle([88, 88, 88], 0.07, 'quadrada', 0.5, 14, 0.4, False),
    'pesca_puxar': lambda: tom('serra', 200, 260, 0.25, s=0.5, vol=0.25),
    'pesca_apanhado': lambda: jingle([76, 79, 84, 88, 84, 88, 91], 0.06, 'quadrada', 0.25, 6, 0.5),
    'pesca_fugiu': lambda: jingle([72, 67, 64], 0.09, 'triangulo', 0.5, 6, 0.6, False),
    'plantar': lambda: ruido(1200, 700, 0.12, 18, corte=1500, vol=0.5),
    'regar': lambda: ruido(4500, 3500, 0.5, 4, corte=5000, alto=1500, vol=0.35),
    'colher': lambda: misturar(ruido(3000, 1500, 0.08, 25, vol=0.4), S.np.pad(jingle([84, 91], 0.05, 'quadrada', 0.25, 12, 0.35, False), (int(SR * 0.06), 0))),
    'galinha': lambda: misturar(*[S.np.pad(tom('quadrada', 900, 700, 0.06, duty=0.25, queda=25, vol=0.3), (int(SR * i * 0.09), 0)) for i in range(3)]),
    'vaca': lambda: passa_baixo(onda('serra', S.vibrato(130, 0.8, 0.03, 4), 0.8), 700) * env(int(SR * 0.8), 0.08, 0.2, 0.7, 0.3) * 0.6,
    'cabra': lambda: passa_baixo(onda('serra', S.vibrato(300, 0.5, 0.08, 14), 0.5), 1500) * env(int(SR * 0.5), 0.03, 0.1, 0.7, 0.15) * 0.5,
    'ovelha': lambda: passa_baixo(onda('quadrada', S.vibrato(240, 0.6, 0.06, 11), 0.6, 0.3), 1200) * env(int(SR * 0.6), 0.04, 0.1, 0.7, 0.2) * 0.45,
}


# vozes dos NPCs (docs/AUDIO.md, secção 4): um bip por letra; cada NPC tem a sua altura e timbre
VOZES = {
    'voz_brom': ('quadrada', 150, 0.5, 0.045), 'voz_lyra': ('quadrada', 880, 0.25, 0.03), 'voz_gorvan': ('triangulo', 110, 0.5, 0.06),
    'voz_selene': ('seno', 520, 0.5, 0.045), 'voz_kai': ('quadrada', 330, 0.25, 0.04), 'voz_fantasma': ('seno', 440, 0.5, 0.06),
    'voz_fungoide': ('seno', 260, 0.5, 0.09), 'voz_sistema': ('quadrada', 1320, 0.125, 0.025), 'voz_administrador': ('triangulo', 660, 0.5, 0.035),
    'voz_grave': ('quadrada', 200, 0.5, 0.045), 'voz_media': ('quadrada', 400, 0.25, 0.04), 'voz_aguda': ('quadrada', 700, 0.25, 0.035),
    'voz_crianca': ('quadrada', 1000, 0.25, 0.03), 'voz_velho': ('triangulo', 260, 0.5, 0.05),
}


def voz(tipo, f, duty, dur):
    x = tom(tipo, f, f * 1.02, dur, duty=duty, queda=18, vol=0.35)
    if tipo == 'seno' and f in (440, 260):   # fantasmas e fungoides: eco e tremido
        x = eco(x * (1 + 0.3 * np.sin(np.arange(len(x)) / SR * 2 * np.pi * 9)), 0.07, 0.4, 2)
    return x


def gerar(nomes=None):
    feitos = 0
    for nome, f in EFEITOS.items():
        if nomes and nome not in nomes:
            continue
        S.gravar_ogg(S.normalizar(f(), 0.8), os.path.join(PASTA, f'{nome}.ogg'))
        feitos += 1
    for nome, (tipo, fr, duty, dur) in VOZES.items():
        if nomes and nome not in nomes:
            continue
        S.gravar_ogg(S.normalizar(voz(tipo, fr, duty, dur), 0.6), os.path.join(PASTA, f'{nome}.ogg'))
        feitos += 1
    print('ok', feitos, 'efeitos')


if __name__ == '__main__':
    gerar(sys.argv[1:] or None)
