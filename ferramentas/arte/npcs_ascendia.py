"""Os 20 NPCs de Ascendia (sprites 32x32: parado e andar, 3 direções). Aspeto: docs/NPCS.md, secção 3.
Saída: arte/npcs/. Uso: python3 ferramentas/arte/npcs_ascendia.py
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from humano import animacoes
from motor import guardar

CASACO_KAI = ['#2e222f', '#323353', '#484a77', '#4d65b4', '#4d9be6']
FARDA = ['#323353', '#484a77', '#4d65b4', '#4d9be6', '#8fd3ff']
ARMADURA = ['#3e3546', '#7f708a', '#9babb2', '#c7dcd0', '#ffffff']

ESTILOS = {
    # --- os 9 da Demo ---
    'lyra': dict(cabelo='rabo', cor_cabelo='ruivo', acessorios=['oculos', 'sardas'], roupa=FARDA, saia=FARDA,
                 calcas='cinza', cinto='castanho'),
    'gorvan': dict(cabelo='careca', barba='curta', cor_cabelo='cinzento', acessorios=['cicatriz'], roupa='castanho',
                   capa='couro', sem_braco='d', largo=1, bracos=0.4, calcas='preto', cinto='couro'),
    'brom': dict(cabelo='curto', cor_cabelo='ruivo', barba='trancas', baixo=4, largo=2, bracos=0.6, perna=2.0,
                 roupa='vermelho', avental='couro', calcas='castanho'),
    'selene': dict(cabelo='comprido', cor_cabelo='prateado', acessorios=['orelha_elfo', 'oculos_testa', 'lapis'],
                   roupa='branco', saia='roxo', calcas='roxo'),
    'tobias': dict(cabelo='curto', cor_cabelo='castanho', barba='bigode', acessorios=['chapeu_pena'], baixo=2, largo=2,
                   roupa='verde', mangas='branco', calcas='cinza', cinto='castanho'),
    'marta': dict(cabelo='carrapito', cor_cabelo='branco', roupa='roxo', saia='roxo', avental='rosa', baixo=1, largo=1,
                  calcas='roxo'),
    'kai': dict(cabelo='espetado', cor_cabelo='preto', roupa=CASACO_KAI, calcas='cinza', botas='branco'),
    'pip': dict(cabelo='curto', cor_cabelo='castanho', acessorios=['chapeu_palha'], roupa='verde', calcas='azul'),
    'mia': dict(cabelo='curto', cor_cabelo='castanho', acessorios=['fita'], baixo=5, roupa='lilas', saia='lilas',
                calcas='lilas', botas='castanho'),
    # --- os outros 11 ---
    'celia': dict(cabelo='curto', cor_cabelo='castanho', acessorios=[('lenco_cabeca', 'azul')], roupa='branco', saia='azul',
                  calcas='azul', cinto='ouro'),
    'fausto': dict(cabelo='curto', cor_cabelo='branco', barba='longa', acessorios=['oculos'], roupa='castanho', saia='castanho',
                   calcas='castanho', lenco='vermelho'),
    'rook': dict(cabelo='tapado', cor_cabelo='preto', acessorios=[('capuz', 'preto')], roupa='preto', calcas='preto', cinto='couro'),
    'freya': dict(cabelo='curto', cor_cabelo='loiro', acessorios=['cicatriz'], roupa=ARMADURA, calcas='cinza', botas='ferro', largo=1),
    'hana': dict(cabelo='rabo', cor_cabelo='castanho', acessorios=['chapeu_palha'], roupa='azul', calcas='azul', botas='amarelo'),
    'zed': dict(cabelo='comprido', cor_cabelo='castanho', barba='curta', roupa='couro', calcas='castanho', capa='castanho'),
    'oriel': dict(cabelo='curto', cor_cabelo='preto', acessorios=[('lenco_cabeca', 'roxo')], roupa='roxo', saia='roxo',
                  calcas='roxo', olhos_cor='#4d9be6'),
    'lucien': dict(cabelo='comprido', cor_cabelo='loiro', acessorios=[('chapeu_pena', 'vermelho')], roupa='vermelho',
                   mangas='amarelo', calcas='verde'),
    'gizmo': dict(cabelo='espetado', cor_cabelo='branco', acessorios=[('oculos', '#f79617')], baixo=6, roupa='castanho',
                  calcas='castanho', cinto='couro'),
    'elva': dict(cabelo='carrapito', cor_cabelo='preto', roupa='rosa', saia='rosa', calcas='rosa', lenco='amarelo'),
    'aldric': dict(cabelo='curto', cor_cabelo='cinzento', acessorios=['oculos'], roupa=FARDA, calcas='preto', cinto='ouro'),
}

if __name__ == '__main__':
    pasta = os.path.join('arte', 'npcs')
    for nome, est in ESTILOS.items():
        guardar(pasta, nome, animacoes(est))
    print('ok', len(ESTILOS), 'NPCs')
