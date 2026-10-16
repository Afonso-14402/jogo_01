"""A vida dos andares (docs/ARTE.md, secção 6.1): bichos pequenos que andam pelo mapa só para dar ambiente
(não se lutam nem se apanham) e partículas do ar. -> dados/vida.json

bichos: sprite (arte/vida/<sprite>_<anim>.png) · tipo (voa, ave, salta, anda) · quando (dia, noite, sempre)
        · por_100 (quantos por cada 100 células de chão aberto)
ar:     pirilampos, polen, esporos, brasas, fogos_fatuos, orbes, folhas_<cor> (com quando)
peixes: há peixes a saltar na água da região

Uso: python3 ferramentas/dados/vida.py
"""
import json
import os

RAIZ = os.path.join(os.path.dirname(__file__), '..', '..')


def b(sprite, tipo, quando='dia', por_100=4):
    return {'sprite': sprite if isinstance(sprite, list) else [sprite], 'tipo': tipo, 'quando': quando, 'por_100': por_100}


BORBOLETAS = ['borboleta_amarela', 'borboleta_azul', 'borboleta_rosa']
VIDA = {
    1: {'bichos': [b(BORBOLETAS, 'voa', por_100=9), b('passaro', 'ave', por_100=6), b('coelho', 'salta', por_100=4)],
        'ar': [('pirilampos', 'noite'), ('polen', 'dia'), ('folhas_verde', 'sempre')], 'peixes': True, 'bandos': 'passaro'},
    2: {'bichos': [b('morcego', 'voa', 'sempre', 7)], 'ar': [('esporos', 'sempre')], 'peixes': False},
    3: {'bichos': [b('libelinha', 'voa', por_100=8), b('sapo', 'salta', 'sempre', 6), b('passaro', 'ave', por_100=2)],
        'ar': [('pirilampos', 'noite'), ('folhas_verde', 'sempre')], 'peixes': True},
    4: {'bichos': [b('lagarto', 'anda', por_100=5), b('passaro_corvo', 'ave', por_100=2)], 'ar': [('polen', 'dia')], 'peixes': True},
    5: {'bichos': [b('coelho_neve', 'salta', por_100=4), b('passaro', 'ave', por_100=2)], 'ar': [], 'peixes': True},
    6: {'bichos': [b('caranguejo', 'anda', 'sempre', 7), b('passaro_gaivota', 'ave', por_100=5)], 'ar': [], 'peixes': True,
        'bandos': 'passaro_gaivota'},
    7: {'bichos': [b('lagarto_fogo', 'anda', 'sempre', 5)], 'ar': [('brasas', 'sempre')], 'peixes': False},
    8: {'bichos': [b('morcego', 'voa', 'noite', 6), b('passaro_corvo', 'ave', 'sempre', 4)],
        'ar': [('fogos_fatuos', 'sempre'), ('folhas_rosa', 'sempre')], 'peixes': False, 'bandos': 'passaro_corvo'},
    9: {'bichos': [b('passaro_ceu', 'ave', por_100=6), b('borboleta_azul', 'voa', por_100=5)],
        'ar': [('folhas_rosa', 'sempre'), ('polen', 'dia')], 'peixes': False, 'bandos': 'passaro_ceu'},
    10: {'bichos': [], 'ar': [('orbes', 'sempre')], 'peixes': False},
}

if __name__ == '__main__':
    out = {str(r): {**v, 'ar': [{'tipo': t, 'quando': q} for t, q in v['ar']]} for r, v in VIDA.items()}
    with open(os.path.join(RAIZ, 'dados', 'vida.json'), 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print('vida: %d regiões' % len(out))
