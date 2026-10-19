"""Base para os modelos 3D (Blender por script): texturas pixel art, peças low-poly, exportar .glb e .blend.

Regras (docs/ARTE.md, secção 6): 1 unidade = 1 m · grelha de 2x2 m · origem no centro em baixo ·
texturas 32x32 com interpolação Closest · uma peça por .glb.

Corre-se com o Python que tem o módulo bpy (Blender como biblioteca), por exemplo:
    python3 -m venv blenv && blenv/bin/pip install bpy pillow
    blenv/bin/python ferramentas/arte/blender/kit_r01.py
"""
import math
import os
import sys
import random
import bpy  # tem de vir antes do bmesh
import bmesh
from mathutils import Vector
from PIL import Image

PALETA = {}


def hexrgb(c):
    return tuple(int(c[i:i + 2], 16) for i in (1, 3, 5))


# ---------------- texturas (32x32, só cores da Resurrect 64) ----------------

def textura_ruido(nome, cores, pasta, semente=1, manchas=None, tam=32, riscas=None, tabuas=None):
    """cores: lista de cores (mais frequentes primeiro). manchas: [(cor, quantidade, tamanho)].
    Desenha com os padrões de ferramentas/arte/texturas3d.py (tijolos, tábuas, telhas...) pelo nome do material."""
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
        import texturas3d
        os.makedirs(pasta, exist_ok=True)
        caminho = os.path.join(pasta, f'{nome}.png')
        texturas3d.padrao(nome, list(cores) + [m[0] for m in (manchas or [])], tam, semente).convert('RGB').save(caminho)
        return caminho
    except ImportError:
        pass
    rnd = random.Random(semente)
    img = Image.new('RGB', (tam, tam), hexrgb(cores[0]))
    px = img.load()
    pesos = [0.5, 0.3, 0.15, 0.05][:len(cores)]
    for y in range(tam):
        for x in range(tam):
            px[x, y] = hexrgb(rnd.choices(cores, weights=pesos + [0.05] * (len(cores) - len(pesos)))[0])
    if riscas:  # riscas verticais (casca de árvore)
        cor, n = riscas
        for _ in range(n):
            x = rnd.randrange(tam)
            y0 = rnd.randrange(tam)
            for k in range(rnd.randrange(4, 12)):
                px[x, (y0 + k) % tam] = hexrgb(cor)
    if tabuas:  # tábuas horizontais
        cor_linha, alt = tabuas
        for y in range(0, tam, alt):
            for x in range(tam):
                px[x, y] = hexrgb(cor_linha)
            xs = rnd.randrange(tam)
            for k in range(1, alt):
                px[xs, (y + k) % tam] = hexrgb(cor_linha)
    for cor, n, t in (manchas or []):
        for _ in range(n):
            cx, cy = rnd.randrange(tam), rnd.randrange(tam)
            for dy in range(-t, t + 1):
                for dx in range(-t, t + 1):
                    if dx * dx + dy * dy <= t * t:
                        px[(cx + dx) % tam, (cy + dy) % tam] = hexrgb(cor)
    os.makedirs(pasta, exist_ok=True)
    caminho = os.path.join(pasta, f'{nome}.png')
    img.save(caminho)
    return caminho


# ---------------- materiais ----------------

_mats = {}


def material(nome, textura=None, cor=None, emissao=0.0):
    if nome in _mats:
        return _mats[nome]
    m = bpy.data.materials.new(nome)
    m.use_nodes = True
    nt = m.node_tree
    bsdf = nt.nodes.get('Principled BSDF')
    bsdf.inputs['Roughness'].default_value = 1.0
    if textura:
        img = bpy.data.images.load(os.path.abspath(textura))
        tex = nt.nodes.new('ShaderNodeTexImage')
        tex.image = img
        tex.interpolation = 'Closest'
        nt.links.new(tex.outputs['Color'], bsdf.inputs['Base Color'])
        if emissao:
            nt.links.new(tex.outputs['Color'], bsdf.inputs['Emission Color'])
            bsdf.inputs['Emission Strength'].default_value = emissao
    elif cor:
        r, g, b = [v / 255 for v in hexrgb(cor)]
        bsdf.inputs['Base Color'].default_value = (r, g, b, 1)
        if emissao:
            bsdf.inputs['Emission Color'].default_value = (r, g, b, 1)
            bsdf.inputs['Emission Strength'].default_value = emissao
    _mats[nome] = m
    return m


# ---------------- formas (bmesh) ----------------

def _uv_projetar(bm, escala=0.5):
    """UV por projeção na direção dominante de cada face: 1 textura por 2 m (escala 0.5)."""
    uv = bm.loops.layers.uv.verify()
    for f in bm.faces:
        n = f.normal
        ax = max(range(3), key=lambda i: abs(n[i]))
        for l in f.loops:
            co = l.vert.co
            if ax == 2:
                u, v = co.x, co.y
            elif ax == 1:
                u, v = co.x, co.z
            else:
                u, v = co.y, co.z
            l[uv].uv = (u * escala, v * escala)


class Peca:
    """Junta várias formas numa só peça (um objeto), cada forma com o seu material."""

    def __init__(self, nome):
        self.nome = nome
        self.bm = bmesh.new()
        self.mats = []

    def _mat_idx(self, mat):
        if mat not in self.mats:
            self.mats.append(mat)
        return self.mats.index(mat)

    def _juntar(self, bm2, mat, escala_uv=0.5, transform=None):
        _uv_projetar(bm2, escala_uv)
        idx = self._mat_idx(mat)
        for f in bm2.faces:
            f.material_index = idx
        me = bpy.data.meshes.new('tmp')
        bm2.to_mesh(me)
        bm2.free()
        self.bm.from_mesh(me)
        bpy.data.meshes.remove(me)

    def caixa(self, mat, cx, cy, cz, sx, sy, sz, rot_z=0.0, escala_uv=0.5):
        """Caixa com o centro de baixo em (cx, cy, cz) e tamanho (sx, sy, sz)."""
        bm2 = bmesh.new()
        bmesh.ops.create_cube(bm2, size=1.0)
        for v in bm2.verts:
            v.co = Vector((v.co.x * sx, v.co.y * sy, (v.co.z + 0.5) * sz))
            if rot_z:
                v.co.rotate(_rotz(rot_z))
            v.co += Vector((cx, cy, cz))
        self._juntar(bm2, mat, escala_uv)

    def cilindro(self, mat, cx, cy, cz, r1, r2, h, lados=8, rot=(0, 0, 0), escala_uv=0.5):
        bm2 = bmesh.new()
        bmesh.ops.create_cone(bm2, cap_ends=True, cap_tris=False, segments=lados, radius1=r1, radius2=r2, depth=h)
        for v in bm2.verts:
            v.co.z += h / 2
            if any(rot):
                v.co.rotate(_euler(rot))
            v.co += Vector((cx, cy, cz))
        self._juntar(bm2, mat, escala_uv)

    def bola(self, mat, cx, cy, cz, rx, ry, rz, sub=1, semente=None, irregular=0.0, escala_uv=0.5):
        bm2 = bmesh.new()
        bmesh.ops.create_icosphere(bm2, subdivisions=sub, radius=1.0)
        rnd = random.Random(semente)
        for v in bm2.verts:
            k = 1 + (rnd.uniform(-irregular, irregular) if irregular else 0)
            v.co = Vector((v.co.x * rx * k, v.co.y * ry * k, v.co.z * rz * k)) + Vector((cx, cy, cz))
        self._juntar(bm2, mat, escala_uv)

    def prisma(self, mat, pontos, z0, z1, escala_uv=0.5):
        """Prisma a partir de um polígono no chão (pontos x,y) entre as alturas z0 e z1."""
        bm2 = bmesh.new()
        baixo = [bm2.verts.new((x, y, z0)) for x, y in pontos]
        cima = [bm2.verts.new((x, y, z1)) for x, y in pontos]
        bm2.faces.new(list(reversed(baixo)))
        bm2.faces.new(cima)
        n = len(pontos)
        for i in range(n):
            j = (i + 1) % n
            bm2.faces.new([baixo[i], baixo[j], cima[j], cima[i]])
        bmesh.ops.recalc_face_normals(bm2, faces=bm2.faces)
        self._juntar(bm2, mat, escala_uv)

    def rampa(self, mat, sx, sy, h, escala_uv=0.5):
        bm2 = bmesh.new()
        p = [(-sx / 2, -sy / 2, 0), (sx / 2, -sy / 2, 0), (sx / 2, sy / 2, 0), (-sx / 2, sy / 2, 0),
             (-sx / 2, sy / 2, h), (sx / 2, sy / 2, h)]
        v = [bm2.verts.new(c) for c in p]
        for f in ([0, 3, 2, 1], [0, 1, 5, 4], [3, 4, 5, 2], [0, 4, 3], [1, 2, 5]):
            bm2.faces.new([v[i] for i in f])
        bmesh.ops.recalc_face_normals(bm2, faces=bm2.faces)
        self._juntar(bm2, mat, escala_uv)

    def telhado(self, mat, cx, cy, z, sx, sy, h, beiral=0.25, escala_uv=0.5):
        """Telhado de duas águas: cumeeira ao longo de y."""
        bm2 = bmesh.new()
        x0, x1 = cx - sx / 2 - beiral, cx + sx / 2 + beiral
        y0, y1 = cy - sy / 2 - beiral, cy + sy / 2 + beiral
        e = 0.15
        pts = [(x0, y0, z), (x1, y0, z), (cx, y0, z + h), (x0, y1, z), (x1, y1, z), (cx, y1, z + h)]
        v = [bm2.verts.new(p) for p in pts]
        vb = [bm2.verts.new((p[0], p[1], p[2] - e)) for p in pts]
        bm2.faces.new([v[0], v[1], v[2]])
        bm2.faces.new([v[3], v[5], v[4]])
        bm2.faces.new([v[0], v[2], v[5], v[3]])
        bm2.faces.new([v[1], v[4], v[5], v[2]])
        bm2.faces.new([v[0], v[3], v[4], v[1]])
        bmesh.ops.recalc_face_normals(bm2, faces=bm2.faces)
        for x in vb:
            bm2.verts.remove(x)
        self._juntar(bm2, mat, escala_uv)

    def criar(self, x=0.0, y=0.0):
        me = bpy.data.meshes.new(self.nome)
        self.bm.to_mesh(me)
        self.bm.free()
        for m in self.mats:
            me.materials.append(m)
        ob = bpy.data.objects.new(self.nome, me)
        bpy.context.scene.collection.objects.link(ob)
        ob.location = (x, y, 0)
        return ob


def _rotz(a):
    from mathutils import Matrix
    return Matrix.Rotation(a, 3, 'Z')


def _euler(r):
    from mathutils import Euler
    return Euler(r)


# ---------------- cena, exportar e pré-visualizar ----------------

def limpar():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    _mats.clear()


def exportar(objetos, pasta, blend_nome):
    os.makedirs(pasta, exist_ok=True)
    for ob in objetos:
        loc = ob.location.copy()
        ob.location = (0, 0, 0)
        for o in bpy.context.scene.objects:
            o.select_set(False)
        ob.select_set(True)
        bpy.context.view_layer.objects.active = ob
        bpy.ops.export_scene.gltf(filepath=os.path.abspath(os.path.join(pasta, ob.name + '.glb')), use_selection=True,
                                  export_format='GLB', export_yup=True)
        ob.location = loc
    bpy.ops.wm.save_as_mainfile(filepath=os.path.abspath(os.path.join(pasta, blend_nome)))


def previa(caminho, largura=1280, altura=720, distancia=30.0, alvo=(0, 0, 0), amostras=24):
    sc = bpy.context.scene
    sc.render.engine = 'CYCLES'
    sc.cycles.samples = amostras
    sc.cycles.device = 'CPU'
    sc.render.resolution_x, sc.render.resolution_y = largura, altura
    sc.render.film_transparent = False
    world = bpy.data.worlds.new('mundo')
    sc.world = world
    world.use_nodes = True
    world.node_tree.nodes['Background'].inputs['Color'].default_value = (0.2, 0.2, 0.33, 1)
    world.node_tree.nodes['Background'].inputs['Strength'].default_value = 0.6
    sol = bpy.data.lights.new('sol', 'SUN')
    sol.energy = 3.5
    ob_sol = bpy.data.objects.new('sol', sol)
    ob_sol.rotation_euler = (math.radians(50), math.radians(10), math.radians(-35))
    sc.collection.objects.link(ob_sol)
    cam = bpy.data.cameras.new('cam')
    cam.type = 'ORTHO'
    cam.ortho_scale = distancia
    ob_cam = bpy.data.objects.new('cam', cam)
    sc.collection.objects.link(ob_cam)
    ob_cam.location = (alvo[0] + distancia, alvo[1] - distancia, alvo[2] + distancia * 0.9)
    cam.clip_end = distancia * 5
    d = Vector(alvo) - ob_cam.location
    ob_cam.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
    sc.camera = ob_cam
    sc.render.filepath = os.path.abspath(caminho)
    bpy.ops.render.render(write_still=True)
