"""NPCs das povoações da Região 1 (Acampamento dos Lenhadores e Folhalta) e animais da região.
Ficha: docs/regioes/r01_floresta.md (secções 7 e 10). Saída: arte/npcs/ e arte/animais/.

Uso: python3 ferramentas/arte/npcs_r01.py
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from humano import animacoes
from motor import guardar
import monstros_r01 as M

ESTILOS = {
    'bruno': dict(cabelo='curto', cor_cabelo='ruivo', barba='curta', largo=2, bracos=0.5, roupa='vermelho', mangas='vermelho',
                  calcas='castanho', cinto='couro'),
    'tina': dict(cabelo='rabo', cor_cabelo='ruivo', baixo=3, roupa='verde', saia='castanho', calcas='castanho'),
    'velho_cass': dict(cabelo='careca', barba='longa', cor_cabelo='branco', baixo=1, roupa='castanho', calcas='cinza',
                       acessorios=['oculos']),
    'lothiel': dict(cabelo='comprido', cor_cabelo='branco', acessorios=['orelha_elfo', ('coroa', 'verde')], roupa='verde', saia='verde',
                    calcas='verde'),
    'faelan': dict(cabelo='comprido', cor_cabelo='loiro', acessorios=['orelha_elfo'], roupa='verde_esc', calcas='castanho', cinto='couro'),
    'mira': dict(cabelo='rabo', cor_cabelo='prateado', acessorios=['orelha_elfo'], roupa='musgo', saia='verde', calcas='verde'),
    'eldrin': dict(cabelo='curto', cor_cabelo='prateado', acessorios=['orelha_elfo'], roupa='verde', calcas='castanho'),
    'tilly': dict(cabelo='curto', cor_cabelo='loiro', acessorios=['orelha_elfo', 'fita'], baixo=5, roupa='rosa', saia='rosa', calcas='rosa'),
}


def animal_cao(rampa, olho='#2e222f'):
    kw = dict(rampa=rampa, olho=olho)
    return {'parado': [M.lobo(t=0, **kw), M.lobo(t=2, **kw), M.lobo(t=1, baixo=1, **kw), M.lobo(t=2, **kw)],
            'mover': M.anims_lobo(**kw)['mover'],
            'atacar': M.anims_lobo(**kw)['atacar']}


def slime_bebe():
    s = lambda rx, ry, **k: M.slime(rx * 0.6, ry * 0.6, **k)
    return {'parado': [s(9, 7), s(9.3, 6.7), s(9.6, 6.4), s(9.3, 6.7)],
            'mover': [s(10.5, 5.5), s(8, 8.5, dy=-2), s(8.5, 8, dx=1, dy=-3), s(9.5, 6.5, dx=1)],
            'atacar': [s(10.5, 5.2, cara='fechado'), s(8, 9, dy=-4), s(8.5, 8, dx=3, dy=-4), s(10.5, 5.5, dx=3)]}


if __name__ == '__main__':
    for nome, est in ESTILOS.items():
        guardar(os.path.join('arte', 'npcs'), nome, animacoes(est))
    pasta_an = os.path.join('arte', 'animais')
    guardar(pasta_an, 'tronco', animal_cao('castanho'))
    guardar(pasta_an, 'raposa_floresta', animal_cao('laranja'))
    guardar(pasta_an, 'slime_bebe', slime_bebe())
    lumi = M.anims_fada()
    guardar(os.path.join('arte', 'npcs'), 'fada_lumi', {'parado': lumi['parado'], 'mover': lumi['mover']})
    print('ok', len(ESTILOS) + 1, 'NPCs, 3 animais')
