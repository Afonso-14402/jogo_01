"""Lê um ficheiro .glb (glTF binário) sem bibliotecas extra: triângulos já no mundo (com as transformações dos nós),
o material de cada triângulo e as cores de cada material (cor base, cores da textura, emissão).

Uso noutros scripts:  from glb_ler import ler_glb;  tris, mats = ler_glb('arte/.../peca.glb')
  tris: lista de (v0, v1, v2, indice_material, n0, n1, n2) com vértices em metros (x, y para cima, z para sul)
  mats: lista de dicts {'nome', 'cor' (r,g,b 0-255), 'cores' (cores da textura, da mais frequente), 'emissao' (bool), 'alfa'}
"""
import io
import json
import math
import struct

import numpy as np
from PIL import Image

_TIPOS = {5120: np.int8, 5121: np.uint8, 5122: np.int16, 5123: np.uint16, 5125: np.uint32, 5126: np.float32}
_N = {'SCALAR': 1, 'VEC2': 2, 'VEC3': 3, 'VEC4': 4, 'MAT4': 16}


def _ler(caminho):
    dados = open(caminho, 'rb').read()
    magia, versao, total = struct.unpack_from('<4sII', dados, 0)
    assert magia == b'glTF', caminho
    pos = 12
    js, binario = None, b''
    while pos < total:
        tam, tipo = struct.unpack_from('<I4s', dados, pos)
        pedaco = dados[pos + 8: pos + 8 + tam]
        if tipo == b'JSON':
            js = json.loads(pedaco.decode('utf-8'))
        elif tipo == b'BIN\x00':
            binario = pedaco
        pos += 8 + tam
    return js, binario


def _acessor(js, binario, i):
    a = js['accessors'][i]
    bv = js['bufferViews'][a['bufferView']]
    tipo = _TIPOS[a['componentType']]
    n = _N[a['type']]
    inicio = bv.get('byteOffset', 0) + a.get('byteOffset', 0)
    passo = bv.get('byteStride', 0)
    tam_el = np.dtype(tipo).itemsize * n
    if passo and passo != tam_el:
        linhas = [np.frombuffer(binario, tipo, n, inicio + k * passo) for k in range(a['count'])]
        return np.array(linhas)
    arr = np.frombuffer(binario, tipo, a['count'] * n, inicio)
    return arr.reshape(-1, n) if n > 1 else arr


def _matriz(no):
    if 'matrix' in no:
        return np.array(no['matrix'], dtype=float).reshape(4, 4).T
    t = no.get('translation', [0, 0, 0])
    x, y, z, w = no.get('rotation', [0, 0, 0, 1])
    s = no.get('scale', [1, 1, 1])
    r = np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
                  [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
                  [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])
    m = np.eye(4)
    m[:3, :3] = r * np.array(s)
    m[:3, 3] = t
    return m


def _cores_imagem(js, binario, i_tex):
    try:
        img_i = js['textures'][i_tex]['source']
        im = js['images'][img_i]
        bv = js['bufferViews'][im['bufferView']]
        b = binario[bv.get('byteOffset', 0): bv.get('byteOffset', 0) + bv['byteLength']]
        pil = Image.open(io.BytesIO(b)).convert('RGBA')
        cores = pil.getcolors(1 << 16) or []
        cores = sorted([(n, c[:3]) for n, c in cores if c[3] > 128], reverse=True)
        total = sum(n for n, c in cores) or 1
        _cores_imagem.freq = [n / total for n, c in cores[:6]]
        return [c for n, c in cores[:6]]
    except Exception:
        return []


def ler_glb(caminho):
    js, binario = _ler(caminho)
    mats = []
    for m in js.get('materials', []):
        pbr = m.get('pbrMetallicRoughness', {})
        f = pbr.get('baseColorFactor', [1, 1, 1, 1])
        cores = []
        freq = []
        if 'baseColorTexture' in pbr:
            cores = _cores_imagem(js, binario, pbr['baseColorTexture']['index'])
            freq = list(getattr(_cores_imagem, 'freq', []))
        cor = tuple(int(round(c * 255)) for c in f[:3])
        if cores:   # a cor do material é a média das cores da textura (vezes o fator)
            cores = [tuple(int(c[k] * f[k]) for k in range(3)) for c in cores]
        em = m.get('emissiveFactor', [0, 0, 0])
        mats.append({'nome': m.get('name', ''), 'cor': cor, 'cores': cores, 'freq': freq, 'emissao': max(em) > 0.05,
                     'alfa': m.get('alphaMode', 'OPAQUE') != 'OPAQUE'})
    if not mats:
        mats.append({'nome': '', 'cor': (200, 200, 200), 'cores': [], 'emissao': False, 'alfa': False})
    tris = []

    def visitar(i_no, pai):
        no = js['nodes'][i_no]
        m = pai @ _matriz(no)
        if 'mesh' in no:
            for prim in js['meshes'][no['mesh']]['primitives']:
                if prim.get('mode', 4) != 4:
                    continue
                pos = _acessor(js, binario, prim['attributes']['POSITION']).astype(float)
                pos = (np.c_[pos, np.ones(len(pos))] @ m.T)[:, :3]
                nor = None
                if 'NORMAL' in prim['attributes']:
                    nor = _acessor(js, binario, prim['attributes']['NORMAL']).astype(float) @ m[:3, :3].T
                    nor /= np.maximum(np.linalg.norm(nor, axis=1, keepdims=True), 1e-9)
                idx = _acessor(js, binario, prim['indices']).astype(int) if 'indices' in prim else np.arange(len(pos))
                mi = prim.get('material', 0)
                for k in range(0, len(idx) - 2, 3):
                    a, b, c = idx[k], idx[k + 1], idx[k + 2]
                    tris.append((pos[a], pos[b], pos[c], mi,
                                 nor[a] if nor is not None else None, nor[b] if nor is not None else None,
                                 nor[c] if nor is not None else None))
        for f in no.get('children', []):
            visitar(f, m)

    cena = js['scenes'][js.get('scene', 0)]
    for i in cena['nodes']:
        visitar(i, np.eye(4))
    return tris, mats


if __name__ == '__main__':
    import sys
    for c in sys.argv[1:]:
        t, m = ler_glb(c)
        print(c, len(t), 'triângulos')
        for x in m:
            print('  ', x['nome'], x['cor'], x['cores'][:4], 'emissão' if x['emissao'] else '')
