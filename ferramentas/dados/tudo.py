"""Gera todos os dados do jogo (dados/*.json) a partir dos documentos, pela ordem certa.

Uso: python3 ferramentas/dados/tudo.py
"""
import os
import runpy
import sys

PASTA = os.path.dirname(os.path.abspath(__file__))
ORDEM = ['estados', 'armas', 'itens', 'receitas', 'monstros', 'andares', 'progressao', 'clima', 'dialogos', 'missoes', 'cidade', 'colecoes', 'vida', 'povoacoes']

if __name__ == '__main__':
    sys.path.insert(0, PASTA)
    for nome in ORDEM:
        print('--', nome)
        runpy.run_path(os.path.join(PASTA, nome + '.py'), run_name='__main__')
