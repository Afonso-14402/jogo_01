"""Ícones 16x16 (itens, materiais, comida, peixes, armaduras) e plantas da quinta (4 fases).
Cada ícone é um MOLDE (forma do objeto) + cores. Os moldes servem para todas as regiões.
Saída: arte/icones/{id}.png e arte/icones/plantas/{planta}_fase_{n}.png

Uso: python3 ferramentas/arte/icones.py [regiao]
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from motor import Parte, elipse, retangulo, capsula, poligono, desenhar, RAMPAS

W = 16


def R(n):
    return RAMPAS[n] if isinstance(n, str) else n


def pts(P, lista, cor, z=50):
    P.append(Parte({(int(x), int(y)) for x, y in lista}, None, z=z, separar=False, cor=cor))


# ---------------- moldes ----------------

def minerio(c, pedra='cinza'):
    P = [Parte(poligono([(2, 12), (3, 6), (7, 3), (12, 4), (14, 9), (12, 14), (5, 14)]), R(pedra), z=1)]
    for x, y in ((6, 7), (10, 6), (8, 11), (11, 10)):
        P.append(Parte(elipse(x, y, 1.4, 1.2), R(c), z=2, separar=False))
    return P


def lingote(c):
    return [Parte(poligono([(1, 12), (4, 6), (12, 6), (15, 12)]), R(c), z=1),
            Parte(poligono([(4, 6), (5, 4), (11, 4), (12, 6)]), R(c), z=2)]


def madeira(c='madeira'):
    return [Parte(capsula(3, 11, 12, 5, 3.2), R(c), z=1), Parte(elipse(12.5, 5, 2.6, 2.6), ['#4c3e24', '#966c6c', '#ab947a', '#c7dcd0', '#c7dcd0'], z=2)]


def couro(c):
    return [Parte(poligono([(3, 3), (6, 4), (10, 3), (13, 4), (12, 8), (14, 13), (9, 12), (6, 13), (2, 12), (4, 8)]), R(c), z=1, plano=True)]


def fio(c):
    P = [Parte(retangulo(4, 4, 11, 12, canto=1), R(c), z=1, volume='cilindro_h')]
    for y in (6, 8, 10):
        pts(P, [(x, y) for x in range(5, 11)], R(c)[1], 40)
    P.append(Parte(retangulo(3, 3, 12, 3), R('madeira'), z=2, plano=True))
    P.append(Parte(retangulo(3, 13, 12, 13), R('madeira'), z=2, plano=True))
    return P


def cristal(c):
    return [Parte(poligono([(8, 1), (12, 6), (10, 14), (6, 14), (4, 6)]), R(c), z=1),
            Parte(poligono([(3, 9), (5, 8), (6, 14), (3, 14)]), R(c), z=0.5)]


def gema(c):
    return [Parte(poligono([(4, 5), (12, 5), (14, 8), (8, 14), (2, 8)]), R(c), z=1),
            Parte(poligono([(4, 5), (12, 5), (11, 7), (5, 7)]), R(c), z=2, separar=False)]


def erva(c='verde'):
    return [Parte(capsula(8, 14, 8, 6, 0.6), R('verde_esc'), z=0),
            Parte(poligono([(8, 10), (3, 7), (2, 3), (7, 5)]), R(c), z=1),
            Parte(poligono([(8, 8), (13, 4), (14, 1), (9, 3)]), R(c), z=1),
            Parte(poligono([(8, 13), (13, 11), (14, 8), (9, 10)]), R(c), z=1)]


def flor(c, centro='amarelo'):
    P = [Parte(capsula(8, 15, 8, 8, 0.7), R('verde'), z=0)]
    for dx, dy in ((-3, 0), (3, 0), (0, -3), (0, 3)):
        P.append(Parte(elipse(8 + dx, 6 + dy, 2.4, 2.4), R(c), z=1))
    P.append(Parte(elipse(8, 6, 1.6, 1.6), R(centro), z=2))
    return P


def cogumelo(c='vermelho', pe='branco', brilho=False):
    P = [Parte(retangulo(6, 8, 9, 14, canto=1), R(pe), z=1, volume='cilindro_v'),
         Parte({p for p in elipse(7.5, 8, 6.5, 5.5) if p[1] <= 8}, R(c), z=2)]
    pts(P, [(5, 5), (9, 4), (11, 7)], '#ffffff' if not brilho else '#fbff86', 50)
    return P


def frasco(c, forma='redondo'):
    vidro = ['#9babb2', '#c7dcd0', '#c7dcd0', '#ffffff', '#ffffff']
    P = [Parte(retangulo(6, 1, 9, 2), R('madeira'), z=3, plano=True),
         Parte(retangulo(6, 3, 9, 5), vidro, z=1, plano=True)]
    if forma == 'redondo':
        P.append(Parte(elipse(7.5, 10.5, 5.5, 5), R(c), z=2))
    elif forma == 'alto':
        P.append(Parte(retangulo(4, 6, 11, 14, canto=1), R(c), z=2, volume='cilindro_v'))
    else:
        P.append(Parte(poligono([(6, 5), (9, 5), (14, 14), (1, 14)]), R(c), z=2))
    pts(P, [(5, 8), (5, 9)], '#ffffff', 50)
    return P


def pote(c):
    return [Parte(retangulo(4, 6, 11, 14, canto=1), R(c), z=1, volume='cilindro_v'),
            Parte(retangulo(3, 3, 12, 5), R('madeira'), z=2, plano=True),
            Parte(retangulo(5, 9, 10, 11), ['#c7dcd0'] * 5, z=3, plano=True)]


def carne(c='rosa'):
    return [Parte(capsula(3, 12, 6, 9, 1.4), ['#9babb2', '#c7dcd0', '#ffffff', '#ffffff', '#ffffff'], z=0),
            Parte(elipse(9.5, 6.5, 5, 4.5), R(c), z=1)]


def peixe(c, barbatana=None, olho='#2e222f'):
    P = [Parte(poligono([(2, 4), (5, 8), (2, 12)]), R(barbatana or c), z=0),
         Parte(elipse(9, 8, 6, 3.6), R(c), z=1),
         Parte(poligono([(7, 5), (10, 2), (11, 5)]), R(barbatana or c), z=0.5)]
    pts(P, [(12, 7)], olho, 50)
    return P


def saco(c, marca=None):
    P = [Parte(poligono([(4, 5), (12, 5), (14, 14), (2, 14)]), R('madeira'), z=1),
         Parte(retangulo(5, 3, 11, 4), R('madeira'), z=2, plano=True)]
    P.append(Parte(elipse(8, 10, 2.5, 2.5), R(marca or c), z=3))
    return P


def fruto(c, folha=True, forma='redondo'):
    P = []
    if forma == 'redondo':
        P.append(Parte(elipse(8, 9.5, 5.5, 5.2), R(c), z=1))
    elif forma == 'raiz':
        P.append(Parte(poligono([(3, 5), (13, 5), (8, 15)]), R(c), z=1))
    elif forma == 'batata':
        P.append(Parte(elipse(8, 9, 6, 4.5), R(c), z=1))
    elif forma == 'morango':
        P.append(Parte(poligono([(3, 6), (13, 6), (12, 10), (8, 15), (4, 10)]), R(c), z=1))
        pts(P, [(6, 8), (9, 9), (7, 11), (10, 12)], '#fbff86', 50)
    if folha:
        P.append(Parte(poligono([(8, 5), (5, 2), (8, 3), (11, 1), (10, 5)]), R('verde'), z=2))
    return P


def pena(c):
    return [Parte(poligono([(3, 14), (6, 7), (11, 2), (13, 3), (9, 9), (5, 14)]), R(c), z=1),
            Parte(capsula(3, 14, 11, 4, 0.4), R('branco'), z=2, separar=False)]


def presa(c='branco'):
    return [Parte(poligono([(4, 14), (3, 9), (5, 4), (9, 1), (8, 5), (7, 9), (8, 14)]), R(c), z=1)]


def chifre(c='branco'):
    return [Parte(poligono([(4, 14), (5, 9), (8, 5), (12, 2), (11, 6), (9, 10), (8, 14)]), R(c), z=1)]


def gota(c):
    return [Parte(elipse(8, 10, 5, 4.5) | poligono([(4, 8), (8, 1), (12, 8)]), R(c), z=1)]


def po(c):
    P = [Parte(elipse(8, 11, 6, 3.5), R(c), z=1)]
    pts(P, [(4, 4), (8, 2), (12, 5), (6, 6), (10, 7)], R(c)[4], 50)
    return P


def folha(c='verde'):
    return [Parte(poligono([(2, 14), (4, 7), (9, 3), (14, 2), (13, 8), (8, 13)]), R(c), z=1),
            Parte(capsula(2.5, 13.5, 11, 5, 0.4), R(c)[0:1] * 5, z=2, separar=False)]


def pedra(c='cinza'):
    return [Parte(poligono([(2, 13), (3, 6), (8, 3), (13, 5), (14, 12), (9, 14)]), R(c), z=1)]


def papel(c='branco', selo=None):
    P = [Parte(retangulo(3, 2, 12, 13), R(c), z=1, plano=True)]
    for y in (5, 7, 9):
        pts(P, [(x, y) for x in range(5, 11)], '#7f708a', 40)
    if selo:
        P.append(Parte(elipse(10, 11, 2, 2), R(selo), z=3))
    return P


def chave(c='ouro'):
    return [Parte({p for p in elipse(5, 5, 3.5, 3.5) if p not in elipse(5, 5, 1.5, 1.5)}, R(c), z=1),
            Parte(capsula(7, 7, 13, 13, 1.0), R(c), z=1),
            Parte(capsula(11, 13, 12, 11, 0.8), R(c), z=1)]


def ovo(c, manchas=None):
    P = [Parte(elipse(8, 9, 5, 6), R(c), z=1)]
    if manchas:
        pts(P, [(6, 7), (10, 9), (7, 12)], manchas, 50)
    return P


def anel(c='ouro', pedra_c='vermelho'):
    return [Parte({p for p in elipse(8, 10, 5, 4.5) if p not in elipse(8, 10, 3, 2.5)}, R(c), z=1),
            Parte(elipse(8, 5, 2.4, 2.2), R(pedra_c), z=2)]


def amuleto(c='prata', pedra_c='azul'):
    return [Parte(capsula(3, 2, 8, 8, 0.4) | capsula(13, 2, 8, 8, 0.4), R('cinza'), z=0, separar=False),
            Parte(elipse(8, 10, 4, 4.5), R(c), z=1), Parte(elipse(8, 10, 2, 2.4), R(pedra_c), z=2)]


def bolsa(c='couro'):
    return [Parte(elipse(8, 10, 6, 5), R(c), z=1), Parte(retangulo(4, 4, 11, 6), R(c), z=2, plano=True),
            Parte(elipse(8, 8, 1.4, 1.4), R('ouro'), z=3)]


def tocha():
    return [Parte(capsula(6, 14, 9, 7, 1.2), R('madeira'), z=1), Parte(elipse(9.5, 5, 3, 3.6), R('laranja'), z=2),
            Parte(elipse(9.5, 5.5, 1.5, 2), R('amarelo'), z=3, separar=False)]


def prato(c, comida_forma='monte'):
    P = [Parte(elipse(8, 11, 7, 3.5), R('branco'), z=0)]
    if comida_forma == 'monte':
        P.append(Parte(elipse(8, 9, 4.5, 3.2), R(c), z=1))
    elif comida_forma == 'sopa':
        P[0] = Parte(poligono([(1, 8), (15, 8), (12, 14), (4, 14)]), R('madeira'), z=0)
        P.append(Parte(elipse(8, 8, 6.5, 1.6), R(c), z=1, plano=True))
    elif comida_forma == 'panquecas':
        for i in range(3):
            P.append(Parte(elipse(8, 10 - i * 2, 5, 1.6), R(c), z=1 + i))
        P.append(Parte(elipse(8, 5, 2, 1.2), R('azul'), z=5))
    elif comida_forma == 'torta':
        P.append(Parte({p for p in elipse(8, 10, 6, 4) if p[1] >= 7}, R(c), z=1))
        P.append(Parte(retangulo(3, 7, 12, 8), R('laranja'), z=2, plano=True))
    return P


def espeto(c):
    P = [Parte(capsula(2, 14, 14, 2, 0.4), R('madeira'), z=0)]
    for t in (0.35, 0.55, 0.75):
        x, y = 2 + 12 * t, 14 - 12 * t
        P.append(Parte(elipse(x, y, 2, 2), R(c), z=1))
    return P


def armadura(peca, c):
    if peca == 'cabeca':
        return [Parte({p for p in elipse(8, 9, 6, 6) if p[1] <= 10}, R(c), z=1), Parte(retangulo(2, 10, 13, 11), R(c), z=2, plano=True)]
    if peca == 'corpo':
        return [Parte(poligono([(3, 3), (6, 2), (8, 4), (10, 2), (13, 3), (14, 7), (12, 7), (12, 14), (4, 14), (4, 7), (2, 7)]), R(c), z=1)]
    if peca == 'maos':
        return [Parte(elipse(7, 9, 4, 4.5), R(c), z=1), Parte(capsula(10, 10, 12, 6, 1.4), R(c), z=2),
                Parte(retangulo(4, 12, 10, 14), R(c), z=0, plano=True)]
    if peca == 'pes':
        return [Parte(retangulo(4, 2, 9, 11), R(c), z=1, volume='cilindro_v'), Parte(elipse(8.5, 12, 5.5, 2.4), R(c), z=2)]
    if peca == 'capa':
        return [Parte(poligono([(5, 2), (11, 2), (14, 14), (8, 12), (2, 14)]), R(c), z=1)]


def ferramenta(tipo, c):
    if tipo == 'picareta':
        return [Parte(capsula(3, 14, 11, 4, 0.8), R('madeira'), z=0),
                Parte(poligono([(3, 5), (8, 2), (13, 3), (14, 8), (12, 5), (8, 4), (4, 7)]), R(c), z=1)]
    if tipo == 'machado':
        return [Parte(capsula(3, 14, 11, 4, 0.8), R('madeira'), z=0), Parte(poligono([(9, 2), (14, 4), (13, 9), (9, 7)]), R(c), z=1)]
    if tipo == 'cana':
        P = [Parte(capsula(2, 14, 13, 2, 0.7), R(c), z=0), Parte(capsula(13, 2, 14, 10, 0.2), ['#c7dcd0'] * 5, z=1, separar=False)]
        P.append(Parte(elipse(14, 11, 1, 1), R('vermelho'), z=2))
        return P


def lixo(tipo):
    if tipo == 'bota':
        return [Parte(retangulo(4, 2, 9, 11), R('castanho'), z=1), Parte(elipse(9, 12, 5, 2.4), R('castanho'), z=2)]
    if tipo == 'lata':
        return [Parte(retangulo(4, 4, 11, 13), R('ferro'), z=1, volume='cilindro_v')]
    return [Parte(poligono([(3, 13), (6, 3), (8, 9), (11, 2), (13, 13)]), R('verde_esc'), z=1)]


def generico(c, letra=None):
    return [Parte(elipse(8, 8, 6, 6), R(c), z=1)]


def coroa(c):
    return [Parte(poligono([(1, 13), (1, 5), (5, 9), (8, 3), (11, 9), (15, 5), (15, 13)]), R(c), z=1)]


def icone(partes):
    return desenhar(partes, W, W)


# ---------------- plantas (4 fases) ----------------

def planta(fase, fruto_c, folha_c='verde', tipo='baixa'):
    P = [Parte(elipse(8, 14.5, 6, 1.6), R('castanho'), z=0, plano=True)]
    if fase == 1:
        P.append(Parte(capsula(8, 14, 8, 11, 0.5), R(folha_c), z=1))
        P.append(Parte(elipse(6.5, 10.5, 1.6, 1), R(folha_c), z=2))
        P.append(Parte(elipse(9.5, 10.5, 1.6, 1), R(folha_c), z=2))
    elif fase == 2:
        P.append(Parte(capsula(8, 14, 8, 8, 0.6), R(folha_c), z=1))
        for dx, dy in ((-3, 9), (3, 8), (-2, 12), (3, 11)):
            P.append(Parte(elipse(8 + dx, dy, 2, 1.2), R(folha_c), z=2))
    else:
        h = 3 if tipo == 'alta' else 5
        P.append(Parte(capsula(8, 14, 8, h, 0.7), R(folha_c), z=1))
        for dx, dy in ((-4, h + 3), (4, h + 2), (-3, h + 7), (4, h + 6), (0, h)):
            P.append(Parte(elipse(8 + dx, dy, 2.6, 1.6), R(folha_c), z=2))
        if fase == 4:
            for dx, dy in ((-4, h + 4), (4, h + 7), (0, h + 1)):
                P.append(Parte(elipse(8 + dx, dy, 1.8, 1.8), R(fruto_c), z=3))
    return desenhar(P, W, W)


# ---------------- a lista da Região 1 ----------------

def lista_r01():
    L = {
        'minerio_cobre': minerio('cobre'), 'lingote_cobre': lingote('cobre'), 'carvalho': madeira(),
        'seiva_cristalizada': cristal('laranja'), 'couro_javali': couro('castanho'), 'linho_bravo': fio('branco'),
        'erva_verde': erva(), 'flor_de_mel': flor('azul', 'amarelo'), 'cogumelo_luminoso': cogumelo('agua', 'branco', True),
        'mel_azul': pote('azul'), 'po_de_fada': po('agua'), 'po_de_fada_dourado': po('ouro'), 'bolota_dourada': fruto('ouro', True, 'batata'),
        'rubi_pequeno': gema('vermelho'), 'gel_slime': gota('verde'), 'gel_real': gota('musgo'), 'chifre_pequeno': chifre(),
        'pelo_macio': couro('branco'), 'pele_lobo': couro('cinza'), 'presa_lobo': presa(), 'presa_negra': presa('preto'),
        'presa_javali': presa(), 'presa_real': presa('ouro'), 'carne': carne(), 'carne_coelho': carne('lilas'), 'carne_javali': carne('vermelho'),
        'esporo': po('musgo'), 'chapeu_cogumelo': cogumelo('vermelho', 'vermelho'), 'asa_de_fada': pena('agua'), 'mel': pote('ouro'),
        'ferrao': presa('preto'), 'cera': pedra('amarelo'), 'madeira_viva': madeira('verde_esc'), 'madeira_fulminada': madeira('preto'),
        'folha_dourada': folha('ouro'), 'hera': folha('verde'), 'pedra_trabalhada': pedra('cinza'),
        # armaduras e acessórios
        'couro_javali_cabeca': armadura('cabeca', 'castanho'), 'couro_javali_corpo': armadura('corpo', 'castanho'),
        'couro_javali_maos': armadura('maos', 'castanho'), 'couro_javali_pes': armadura('pes', 'castanho'),
        'couro_javali_capa': armadura('capa', 'branco'), 'coroa_de_gel': coroa('verde'), 'manto_cicatriz': armadura('capa', 'preto'),
        'anel_sussurro': anel('cobre', 'agua'), 'anel_vigia': anel('ferro', 'amarelo'), 'amuleto_nevoa': amuleto('ferro', 'agua'),
        'faixa_aprendiz': fio('vermelho'), 'bussola_darian': amuleto('cobre', 'branco'), 'bolsa_viagem': bolsa('castanho'),
        'bolsa_materiais': bolsa('couro'), 'mochila_couro': bolsa('castanho'),
        # ferramentas
        'picareta_cobre': ferramenta('picareta', 'cobre'), 'machado_lenhador_cobre': ferramenta('machado', 'cobre'),
        'cana_bambu': ferramenta('cana', 'musgo'),
        # consumíveis
        'pocao_vida_p': frasco('vermelho'), 'pocao_mana_p': frasco('azul'), 'pocao_estamina': frasco('amarelo'),
        'pocao_elfica': frasco('verde', 'alto'), 'antidoto': frasco('musgo', 'cone'), 'ligadura': fio('branco'),
        'colirio': frasco('agua', 'cone'), 'pocao_forca': frasco('laranja', 'alto'), 'pocao_velocidade': frasco('agua', 'alto'),
        'pocao_encolher': frasco('roxo', 'cone'), 'tocha': tocha(), 'pedra_regresso': cristal('azul'),
        'frasco_vagalumes': frasco('musgo', 'alto'), 'isco': gota('rosa'), 'isco_dourado': gota('ouro'),
        # comida
        'truta_grelhada': prato('laranja'), 'espetada_coelho': espeto('castanho'), 'sopa_legumes': prato('laranja', 'sopa'),
        'sopa_cogumelos': prato('castanho', 'sopa'), 'panquecas_mel_azul': prato('amarelo', 'panquecas'),
        'torta_maca': prato('amarelo', 'torta'), 'morangos_natas': prato('rosa'), 'assado_javali': prato('castanho'),
        'maca_selvagem': fruto('vermelho'), 'maca_dourada': fruto('ouro'), 'folha_com_mel': folha('ouro'),
        # peixes
        'truta_ribeiro': peixe('lilas', 'verde_esc'), 'perca_prateada': peixe('ferro'), 'peixe_folha': peixe('verde', 'musgo'),
        'carpa_dourada': peixe('ouro', 'laranja'), 'enguia_musgo': [Parte(capsula(2, 11, 14, 5, 2), R('verde_esc'), z=1)],
        'rei_lago_nevoento': peixe('agua', 'branco', '#e83b3b'), 'bota_velha': lixo('bota'), 'lata': lixo('lata'), 'alga_seca': lixo('alga'),
        # sementes e colheitas
        'semente_nabo_bravo': saco('madeira', 'branco'), 'semente_morango': saco('madeira', 'vermelho'),
        'semente_batata_pradaria': saco('madeira', 'castanho'), 'semente_flor_mel': saco('madeira', 'azul'),
        'nabo_bravo': fruto('branco', True, 'raiz'), 'morango_silvestre': fruto('vermelho', True, 'morango'),
        'batata_pradaria': fruto('castanho', False, 'batata'),
        # missão e especiais
        'pedra_inicial': pedra(), 'formulario_guilda': papel('branco', 'azul'), 'carta_lyra': papel('branco', 'vermelho'),
        'carta_eldrin': papel('branco', 'verde'), 'resposta_selene': papel('branco', 'roxo'), 'caixa_tobias': [Parte(retangulo(2, 4, 13, 13), R('madeira'), z=1)],
        'cristal_seiva': cristal('laranja'), 'chave_ruinas': chave('ferro'), 'chave_bau_ouro_ilhota': chave('ouro'),
        'ovo_ouro_javali': ovo('ouro'), 'ovo_slime_bebe': ovo('verde', '#91db69'), 'semente_arvore_mae': fruto('verde', True, 'batata'),
        'trofeu_javali_rei': presa('ouro'), 'trofeu_ramo_ent': folha('verde'), 'lanterna_papel': frasco('laranja', 'alto'),
        'pagina_diario': papel('branco'), 'gel_real_coroa': coroa('verde'),
    }
    plantas = {'nabo_bravo': ('branco', 'baixa'), 'morango_silvestre': ('vermelho', 'baixa'), 'batata_pradaria': ('castanho', 'baixa'),
               'flor_de_mel': ('azul', 'alta'), 'macieira_selvagem': ('vermelho', 'alta')}
    return L, plantas


if __name__ == '__main__':
    L, plantas = lista_r01()
    pasta = os.path.join('arte', 'icones')
    os.makedirs(os.path.join(pasta, 'plantas'), exist_ok=True)
    for nome, partes in L.items():
        icone(partes).save(os.path.join(pasta, f'{nome}.png'))
    for nome, (c, tipo) in plantas.items():
        for f in range(1, 5):
            planta(f, c, tipo=tipo).save(os.path.join(pasta, 'plantas', f'{nome}_fase_{f}.png'))
    print('ok', len(L), 'ícones,', len(plantas), 'plantas x 4 fases')
