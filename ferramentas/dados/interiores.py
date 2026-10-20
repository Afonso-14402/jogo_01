"""Por dentro dos edifícios (docs/CIDADES.md, secção 1.6) -> dados/interiores.json.

Cada tipo de divisão: tamanho (largura × fundo, em metros), chão e paredes (texturas de arte/interiores/), os móveis
(arte/moveis/<id>.glb, ou um sprite de arte/regioes/.../natureza) com a posição (x, z) e a rotação, e onde ficam as
pessoas. A parede do fundo fica em z = -fundo/2 e a porta a meio da frente (z = +fundo/2).
Nas povoações, os móveis básicos trocam-se pelos da região (docs/textos/moveis.md): cadeira, mesa, cama, tapete,
candeeiro e estante.

Uso: python3 ferramentas/dados/interiores.py
"""
import json
import os

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..')
BARRIL = 'res://arte/regioes/r01_floresta/natureza/barril.png'
CALDEIRAO = 'res://arte/moveis2d/caldeirao.png'          # (móveis só em 2D: ferramentas/arte/moveis2d.py)
BOLA_CRISTAL = 'res://arte/moveis2d/bola_cristal.png'
CAIXOTE = 'res://arte/regioes/r01_floresta/natureza/caixote.png'

# os básicos que têm versão de cada região (movel_rNN_01 … _06)
REGIONAL = {'movel_b05': '01', 'movel_b06': '01', 'movel_b03': '02', 'movel_b01': '03', 'movel_b09': '04', 'movel_b10': '04',
            'movel_b11': '05', 'movel_b13': '06', 'movel_b14': '06'}


def mesa_com_cadeiras(x, z, banco=False):
    c = 'movel_b06' if banco else 'movel_b05'
    return [['movel_b03', x, z, 0], [c, x - 1.1, z, 90], [c, x + 1.1, z, -90]]


TIPOS = {
    'casa': {'tamanho': [8, 6], 'chao': 'madeira', 'parede': 'reboco', 'pessoas': [[-0.9, -0.6], [2.6, 0.9]],
             'moveis': [['movel_b01', -2.9, -1.9, 0], ['movel_b25', -1.5, -2.55, 0], ['movel_b22', 0.6, -2.55, 0], ['movel_b13', 2.8, -2.7, 0],
                        ['movel_b09', 0.2, 1.3, 0], ['movel_b20', -3.5, 2.4, 0], ['movel_b11', 3.5, 1.8, 0]] + mesa_com_cadeiras(1.6, -0.4)},
    'estalagem': {'tamanho': [12, 9], 'chao': 'madeira', 'parede': 'madeira', 'pessoas': [[-3.4, -2.9], [2.5, 1.6]],
                  'moveis': [['movel_b15', -4.2, -2.0, 0], ['movel_b15', -2.6, -2.0, 0], ['movel_b24', -3.4, -4.15, 0], ['movel_b22', 1.5, -4.05, 0],
                             ['movel_b01', 5.0, -3.2, 0], ['movel_b01', 3.6, -3.2, 0], ['movel_b10', 0, 3.2, 0], ['movel_b21', -5.5, 3.8, 0],
                             ['movel_b21', 5.5, 3.8, 0], [BARRIL, -5.4, -0.5, 0]] + mesa_com_cadeiras(1.0, 0.2, True) + mesa_com_cadeiras(4.4, 0.2, True)
                            + mesa_com_cadeiras(-2.6, 1.8, True)},
    'taberna': {'tamanho': [14, 10], 'chao': 'madeira', 'parede': 'madeira', 'pessoas': [[-4.2, -3.4], [4.6, -3.6], [1.8, 1.4]],
                'moveis': [['movel_b15', -5.4, -2.5, 0], ['movel_b15', -3.8, -2.5, 0], ['movel_b15', -2.2, -2.5, 0], ['movel_b24', -4.0, -4.6, 0],
                           [BARRIL, -6.4, -4.3, 0], [BARRIL, -6.4, -3.4, 0], [BARRIL, -0.9, -4.4, 0], ['movel_b22', 0.8, -4.55, 0],
                           ['movel_b10', 4.6, -3.6, 0], ['movel_b11', 6.3, -4.4, 0], ['movel_b11', 2.9, -4.4, 0]]
                          + mesa_com_cadeiras(-3.0, 1.2) + mesa_com_cadeiras(1.0, -0.6) + mesa_com_cadeiras(1.8, 2.6) + mesa_com_cadeiras(5.0, 1.0)},
    'forja': {'tamanho': [10, 8], 'chao': 'pedra', 'parede': 'tijolo', 'pessoas': [[0.9, -1.4]],
              'moveis': [['movel_r02_07', 0.0, -1.2, 0], ['movel_b22', -2.6, -3.55, 0], ['movel_b24', 3.0, -3.65, 0], ['movel_b25', 4.0, 0.5, 0],
                         [BARRIL, -4.2, -1.0, 0], [BARRIL, -4.2, 0.0, 0], [CAIXOTE, 3.8, 2.6, 0], ['movel_b15', -3.0, 2.0, 0]]},
    'alquimia': {'tamanho': [9, 7], 'chao': 'madeira', 'parede': 'reboco', 'pessoas': [[0.0, -1.0]],
                 'moveis': [['movel_b14', -2.4, -3.2, 0], ['movel_b14', 2.4, -3.2, 0], ['movel_b15', 0.0, -0.2, 0], ['movel_b20', -3.8, 2.6, 0],
                            ['movel_b21', 3.8, 2.6, 0], ['movel_b21', -3.9, -1.0, 0], ['movel_b12', 0.6, -0.2, 0], ['movel_b09', 0.0, 1.8, 0],
                            ['movel_b05', 0.0, 0.9, 180]]},
    'guilda': {'tamanho': [14, 10], 'chao': 'madeira', 'parede': 'pedra', 'pessoas': [[0.0, -3.0], [-4.0, 1.5]],
               'moveis': [['movel_b15', -1.6, -2.0, 0], ['movel_b15', 0.0, -2.0, 0], ['movel_b15', 1.6, -2.0, 0], ['movel_b14', -4.5, -4.7, 0],
                          ['movel_b14', 4.5, -4.7, 0], ['movel_b10', 0.0, 2.0, 0], ['movel_b11', -6.3, -4.5, 0], ['movel_b11', 6.3, -4.5, 0],
                          ['movel_b21', -6.3, 4.2, 0], ['movel_b21', 6.3, 4.2, 0]] + mesa_com_cadeiras(-4.4, 1.6) + mesa_com_cadeiras(4.4, 1.6)},
    'igreja': {'tamanho': [10, 14], 'chao': 'pedra', 'parede': 'pedra', 'pessoas': [[0.0, -5.4]],
               'moveis': [['movel_b15', 0.0, -6.0, 0], ['movel_b12', -1.4, -6.2, 0], ['movel_b12', 1.4, -6.2, 0], ['movel_b10', 0.0, -3.2, 90],
                          ['movel_b10', 0.0, 0.6, 90], ['movel_b11', -4.3, -6.3, 0], ['movel_b11', 4.3, -6.3, 0]]
                         + [['res://arte/moveis2d/banco_igreja.png', x, z, 0] for z in (-3.0, -1.5, 0.0, 1.5, 3.0) for x in (-2.6, 2.6)]},
    'biblioteca': {'tamanho': [12, 10], 'chao': 'madeira', 'parede': 'madeira', 'pessoas': [[0.0, 1.4]],
                   'moveis': [['movel_b14', x, -4.7, 0] for x in (-4.4, -2.6, -0.8, 1.0, 2.8, 4.6)]
                             + [['movel_b14', x, -1.6, 0] for x in (-4.0, -2.2, 2.2, 4.0)]
                             + [['movel_b15', -2.4, 2.0, 0], ['movel_b15', 2.4, 2.0, 0], ['movel_b05', -2.4, 2.9, 180], ['movel_b05', 2.4, 2.9, 180],
                                ['movel_b12', -2.0, 2.0, 0], ['movel_b12', 2.8, 2.0, 0], ['movel_b10', 0.0, 3.6, 0]]},
    'casa_heroi': {'tamanho': [9, 7], 'chao': 'madeira', 'parede': 'reboco', 'pessoas': [],
                   'moveis': [['movel_b01', -3.4, -2.3, 0], ['movel_b04', -2.4, -3.0, 0], ['movel_b25', 0.0, -3.0, 0], ['movel_b24', 2.4, -3.15, 0],
                              ['movel_b22', 3.9, -1.0, 90], ['movel_b09', 0.0, 1.0, 0], ['movel_b20', -4.0, 2.9, 0], ['movel_b19', 0.0, -3.4, 0]]
                             + mesa_com_cadeiras(1.6, 0.8),
                   'estacoes': {'cama': [-3.4, -2.3], 'bau': [0.0, -3.0], 'fogao': [2.4, -3.15]}},
}
TIPOS['loja'] = dict(TIPOS['alquimia'])
TIPOS['camara'] = dict(TIPOS['guilda'])
TIPOS['quartel'] = {**TIPOS['guilda'], 'parede': 'tijolo'}
# a vidente: a mesa redonda com a bola de cristal ao meio, velas, tapete e pouca luz (ela fica atrás da mesa)
TIPOS['vidente'] = {'tamanho': [9, 7], 'chao': 'madeira', 'parede': 'madeira', 'pessoas': [[0.0, -1.5]],
                    'moveis': [[BOLA_CRISTAL, 0.0, -0.6, 0], ['movel_b09', 0.0, -0.2, 0], ['movel_b05', 0.0, 0.6, 180],
                               ['movel_b13', -2.6, -3.0, 0], ['movel_b19', 0.0, -3.4, 0], ['movel_b12', -3.6, -2.9, 0],
                               ['movel_b12', 3.6, -2.9, 0], ['movel_b12', -3.6, 2.6, 0], ['movel_b20', 3.7, 2.6, 0],
                               ['movel_b25', 2.8, -2.9, 0]]}
# a alquimia: o caldeirão ao lume (a loja de costura fica sem ele)
TIPOS['alquimia'] = {**TIPOS['alquimia'], 'moveis': TIPOS['alquimia']['moveis'] + [[CALDEIRAO, 2.4, -1.4, 0], [BARRIL, -2.6, -1.2, 0]]}

# Ascendia: o modelo do edifício -> tipo de divisão
ASCENDIA = {'guilda': ['guilda', 'Guilda dos Aventureiros'], 'estalagem': ['estalagem', 'Estalagem "Ninho do Viajante"'],
            'taberna': ['taberna', 'Taberna "O Primeiro Degrau"'], 'forja_brom': ['forja', 'Forja do Brom'], 'oficina_gizmo': ['forja', 'Oficina do Gizmo'],
            'alquimia_selene': ['alquimia', 'Alquimia da Selene'], 'costura_elva': ['loja', 'Costura da Elva'], 'tenda_vidente': ['vidente', 'Tenda da Vidente'],
            'igreja': ['igreja', 'Igreja da Luz'], 'biblioteca': ['biblioteca', 'Biblioteca'], 'camara_governador': ['camara', 'Câmara do Governador'],
            'quartel': ['quartel', 'Quartel'], 'casa_1': ['casa', 'Casa'], 'casa_2': ['casa', 'Casa'], 'casa_pobre': ['casa', 'Casa'],
            'esconderijo_rook': ['casa', 'Esconderijo'], 'casa_heroi': ['casa_heroi', 'A tua casa']}
# povoações: palavras no nome da peça -> tipo (o resto é casa)
POVOACAO = [('estalagem', 'estalagem'), ('salao', 'estalagem'), ('cantina', 'estalagem'), ('taberna', 'taberna'), ('hotel', 'estalagem'),
            ('forja', 'forja'), ('mosteiro', 'igreja'), ('capela', 'igreja'), ('observatorio', 'biblioteca'), ('palacio', 'camara')]


# nas povoações, as casas e estalagens têm o chão e as paredes da região
MATERIAIS_REGIAO = {1: ['madeira', 'madeira'], 2: ['pedra', 'pedra'], 3: ['madeira', 'madeira'], 4: ['pedra', 'reboco'], 5: ['madeira', 'madeira'],
                    6: ['madeira', 'reboco'], 7: ['pedra', 'tijolo'], 8: ['pedra', 'pedra'], 9: ['pedra', 'reboco'], 10: ['pedra', 'pedra']}

if __name__ == '__main__':
    out = {'tipos': TIPOS, 'ascendia': ASCENDIA, 'povoacao': POVOACAO, 'regional': REGIONAL, 'materiais_regiao': MATERIAIS_REGIAO}
    with open(os.path.join(RAIZ, 'dados', 'interiores.json'), 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print('interiores: %d tipos' % len(TIPOS))
