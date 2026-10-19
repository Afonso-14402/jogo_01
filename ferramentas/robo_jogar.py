"""Corre o robô que joga (testes/robo_jogar.tscn) em vários andares e junta tudo num resumo.

Para cada andar: prepara o "jogador esperado" (ferramentas/equilibrio.py), corre o Godot sem janela
(--headless --fixed-fps 60: 1 frame = 1/60 s de jogo, o mais depressa que o computador conseguir), guarda o
registo do Godot e procura nele os erros (SCRIPT ERROR, ERROR:, Invalid..., null instance, WARNING).

Uso:
  python3 ferramentas/robo_jogar.py --godot <caminho do godot> [--pasta <saída>] [--segundos 120]
         [--modo andar|boss|pontes] [--habilidade 0.5] [--sem2d] 1 2 3 5 10
  python3 ferramentas/robo_jogar.py --godot <godot> --cidade        (Ascendia: edifícios, janelas, lojas, pessoas)
  python3 ferramentas/robo_jogar.py --mapas                         (sem Godot: chega-se a pé ao guardião e à escada?)
Sem andares, usa a lista de amostra (a Demo inteira e alguns de cada região, com os bosses); no modo "pontes",
todos os andares que têm pontes.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
AMOSTRA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 35, 50, 65, 80, 95, 100]
ERROS = re.compile(r'SCRIPT ERROR|^ERROR:|USER ERROR|Invalid (get|set|call|access|operands)|null instance|Nonexistent function|'
                   r'Attempt to call|Parse Error|Cannot call|out of bounds|WARNING|USER WARNING', re.M)


def correr(godot, args_robo, pasta, nome, sem2d, timeout):
    saida = os.path.join(pasta, nome + '.json')
    log = os.path.join(pasta, nome + '.log')
    if os.path.exists(saida):
        os.remove(saida)
    env = dict(os.environ)
    if sem2d:
        env['SEM2D'] = '1'
    cmd = [godot, '--headless', '--fixed-fps', '60', '--path', RAIZ, 'res://testes/robo_jogar.tscn', '--'] + args_robo[:1] + \
          [args_robo[1], saida] + args_robo[2:]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, env=env)
        texto = p.stdout + p.stderr
    except subprocess.TimeoutExpired as e:
        texto = (e.stdout or b'').decode(errors='replace') if isinstance(e.stdout, bytes) else (e.stdout or '')
        texto += '\nROBO: TIMEOUT\n'
    with open(log, 'w', encoding='utf-8') as f:
        f.write(texto)
    erros = []
    linhas = texto.splitlines()
    fim = next((i for i, l in enumerate(linhas) if l.startswith('ROBO: fim')), len(linhas))
    for i, l in enumerate(linhas):
        if i > fim and 'WARNING' in l:
            continue   # avisos ao fechar o Godot a meio (tweens e objetos por libertar): não são do jogo
        if ERROS.search(l) and 'ROBO:' not in l and 'leaked at exit' not in l:   # (a fuga ao sair é só de fechar a meio)
            # a linha seguinte costuma dizer onde (at: ... (res://...))
            onde = linhas[i + 1].strip() if i + 1 < len(linhas) and 'at:' in linhas[i + 1] else ''
            erros.append((l.strip() + ' ' + onde).strip())
    rel = {}
    if os.path.exists(saida):
        with open(saida, encoding='utf-8') as f:
            rel = json.load(f)
    else:
        erros.append('o robô não escreveu o relatório (crash ou timeout?)')
    rel['erros_godot'] = sorted(set(erros))
    rel['erros_godot_n'] = len(erros)
    with open(saida, 'w', encoding='utf-8') as f:
        json.dump(rel, f, ensure_ascii=False, indent=1)
    return rel


PAREDES = ('TT', '##', '~~', 'ww', '  ')   # células que não se atravessam a pé (andar.gd: _parede, rocha, água funda, vazio)


def garantir_caminhos(g):
    """O mesmo que scripts/mundo/caminhos.gd: abre o caminho mais curto (passadiço == ou trilho ::) até à Zona Segura,
    ao guardião, ao boss e à escada quando não se chega lá a pé. Devolve (grelha nova, células abertas)."""
    from collections import deque
    g = [list(r) for r in g]
    H, W = len(g), len(g[0])
    cod = lambda x, y: g[y][x] if 0 <= x < W and 0 <= y < H else 'TT'
    ini = next(((x, y) for y in range(H) for x in range(W) if g[y][x] in ('EE', 'AA')), None)
    abertos = []
    if not ini:
        return g, abertos
    for alvo in ('SS', 'GG', 'BB', '>>'):
        vis = {ini}
        pilha = [ini]
        while pilha:
            x, y = pilha.pop()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                q = (x + dx, y + dy)
                if q not in vis and cod(*q) not in PAREDES:
                    vis.add(q)
                    pilha.append(q)
        cel = [(x, y) for y in range(H) for x in range(W) if g[y][x] == alvo]
        if not cel or any(c in vis for c in cel):
            continue
        dist = {p: 0 for p in vis}
        veio = {}
        fila = deque(vis)
        fim = None
        while fila:
            p = fila.popleft()
            if cod(*p) == alvo:
                fim = p
                break
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                q = (p[0] + dx, p[1] + dy)
                if not (0 <= q[0] < W and 0 <= q[1] < H):
                    continue
                c = cod(*q)
                borda = q[0] in (0, W - 1) or q[1] in (0, H - 1)
                custo = 0 if (c not in PAREDES or c == alvo) else (50 if borda else 1)
                if dist[p] + custo < dist.get(q, 1 << 30):
                    dist[q] = dist[p] + custo
                    veio[q] = p
                    (fila.appendleft if custo == 0 else fila.append)(q)
        p = fim
        while p is not None and p in veio:
            c = cod(*p)
            if c in PAREDES:
                g[p[1]][p[0]] = '==' if c in ('~~', 'ww', '  ') else '::'
                abertos.append(p)
            p = veio[p]
    return g, abertos


CAMINHO_POR_PUZZLE = (67,)   # andar.gd: o caminho abre-se com um puzzle


def verificar_mapas():
    """Sem abrir o Godot: em cada andar, a partir da chegada EE, chega-se a pé (sem atravessar as PAREDES) ao
    guardião / boss, à escada e à Zona Segura? (As células só se tocam pelos lados: pelos cantos não se passa.)"""
    for n in range(1, 101):
        with open(os.path.join(RAIZ, 'dados', 'andares', 'a%03d.json' % n), encoding='utf-8') as f:
            a = json.load(f)
        g = a['grelha']
        if n not in CAMINHO_POR_PUZZLE:
            g, abertos = garantir_caminhos(g)
            if abertos:
                print('andar %3d %-28s passadiços/trilhos abertos pelo jogo: %d células' % (n, a.get('nome_pt', '')[:28], len(abertos)))

        def cod(x, y):
            return g[y][x] if 0 <= y < len(g) and 0 <= x < len(g[0]) else 'TT'

        def alcance(viz):
            ini = [(x, y) for y in range(len(g)) for x in range(len(g[0])) if cod(x, y) in ('EE', 'AA')]
            vis = set(ini[:1])
            fila = list(vis)
            while fila:
                x, y = fila.pop()
                for dx, dy in viz:
                    q = (x + dx, y + dy)
                    if q not in vis and cod(*q) not in PAREDES:
                        vis.add(q)
                        fila.append(q)
            return vis
        lados = alcance(((1, 0), (-1, 0), (0, 1), (0, -1)))
        cantos = alcance(((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)))
        alvos = sorted({cod(x, y) for y in range(len(g)) for x in range(len(g[0]))
                        if cod(x, y) in ('GG', 'BB', '>>', 'SS') and (x, y) not in lados})
        if alvos:
            print('andar %3d %-28s não se chega a pé a: %s%s' % (n, a.get('nome_pt', '')[:28], ' '.join(alvos),
                  '' if not any((x, y) in cantos for y in range(len(g)) for x in range(len(g[0])) if cod(x, y) in alvos)
                  else '  (só pelos cantos: falta uma célula de passagem)'))


def resumo(n, rel):
    ms = rel.get('monstros', {})
    mortos = sum(m.get('mortos', 0) for m in ms.values())
    normais = {k: v for k, v in ms.items() if v.get('tipo') not in ('guardiao', 'mini_boss', 'boss')}
    gm = [v['golpes_por_morte'] for v in normais.values() if v.get('mortos')]
    tm = [v['segundos_matar_media'] for v in normais.values() if v.get('mortos')]
    dl = [v['dano_por_golpe_levado'] for v in normais.values() if v.get('golpes_levados')]
    hp = rel.get('hp_max', 1) or 1
    ch = rel.get('chefe', {})
    chefe = ''
    if ch:
        dur = (ch.get('fim', -1) - ch.get('inicio', -1)) if ch.get('fim', -1) >= 0 else None
        if ch.get('vivo_s'):
            dur = None
        chefe = '%s %s: %s, HP final %d%%, mortes %d' % (ch.get('tipo'), ch.get('id'), ('%.0f s' % dur) if dur is not None else
                                                       ('morri aos %.0f s de luta' % ch['vivo_s'] if ch.get('vivo_s') else 'vivo'),
                                                       100 * ch.get('hp_final', 0) / max(1, ch.get('hp_max', 1)), ch.get('mortes_heroi', 0))
    print('andar %3d | mortos %3d | golpes/morte %4.1f | s/morte %4.1f | golpes p/ morrer %5.1f | mortes %d | poções %d | +nv %d | erros %d | %s'
          % (n, mortos, sum(gm) / len(gm) if gm else 0, sum(tm) / len(tm) if tm else 0, hp / (sum(dl) / len(dl)) if dl else 0,
             rel.get('mortes', 0), rel.get('pocoes_usadas', 0), rel.get('subidas_nivel', 0), rel.get('erros_godot_n', 0), chefe))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--godot', default=os.environ.get('GODOT', 'godot'))
    ap.add_argument('--pasta', default=os.path.join(tempfile.gettempdir(), 'robo_jogar'))
    ap.add_argument('--segundos', type=float, default=120.0)
    ap.add_argument('--modo', default='andar')
    ap.add_argument('--habilidade', type=float, default=0.5)
    ap.add_argument('--sem2d', action='store_true')
    ap.add_argument('--cidade', action='store_true')
    ap.add_argument('--mapas', action='store_true', help='só verifica os mapas (sem Godot): chega-se a pé ao guardião e à escada?')
    ap.add_argument('--timeout', type=float, default=900.0)
    ap.add_argument('andares', nargs='*', type=int)
    a = ap.parse_args()
    if a.mapas:
        verificar_mapas()
        return
    os.makedirs(a.pasta, exist_ok=True)
    subprocess.run([sys.executable, os.path.join(RAIZ, 'ferramentas', 'equilibrio.py'), '1'], capture_output=True)
    if a.cidade:
        rel = correr(a.godot, ['1', '60', 'cidade'], a.pasta, 'cidade', a.sem2d, a.timeout)
        print('cidade: erros do robô', rel.get('erros_robo'), '| notas', rel.get('notas'))
        for e in rel['erros_godot']:
            print('   ', e)
        return
    andares = a.andares or AMOSTRA
    if a.modo == 'pontes' and not a.andares:   # todos os andares com pontes
        andares = [n for n in range(1, 101) if '"=="' in open(os.path.join(RAIZ, 'dados', 'andares', 'a%03d.json' % n), encoding='utf-8').read()]
    for n in andares:
        nome = 'a%03d_%s' % (n, a.modo)
        rel = correr(a.godot, [str(n), str(a.segundos), a.modo, str(a.habilidade)], a.pasta, nome, a.sem2d, a.timeout)
        if a.modo == 'pontes':
            p = rel.get('pontes', [])
            print('andar %3d | pontes atravessadas %d/%d | erros %d' % (n, sum(1 for x in p if x['ok']), len(p), rel.get('erros_godot_n', 0)))
        else:
            resumo(n, rel)
        for e in rel['erros_godot'][:12]:
            print('    ', e)
        for e in rel.get('erros_robo', []):
            print('     robô:', e)


if __name__ == '__main__':
    main()
