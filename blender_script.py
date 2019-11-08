import os
import random
import sys

import bmesh
import bpy

filepath = bpy.data.filepath

# we get the directory relative to the blend file path
dir = os.path.dirname(filepath)

# we append our path to blender modules path
# we use if not statement to do this one time only
if dir not in sys.path:
    sys.path.append(dir)

from noise import NOISE_HEIGHT, NOISE_WIDTH, get_noise_arr

# Очистка сцены
bpy.data.objects['Plane'].select_set(True)
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.delete()

# Очистка материалов и текстур
for image in bpy.data.images:
    bpy.data.images.remove(image)
for tex in bpy.data.textures:
    bpy.data.textures.remove(tex)
for mat in bpy.data.materials:
    bpy.data.materials.remove(mat)

# Создание плоскости
bpy.ops.mesh.primitive_plane_add()
bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
bpy.data.objects['Plane'].scale = (2.0, 2.0, 1.0)
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.subdivide(number_cuts=50)
bpy.ops.object.mode_set(mode='OBJECT')

# Displace
height_tex = bpy.data.textures.new('heightmapAYY', type='IMAGE')
height_tex.image = bpy.data.images.load("C:\\Users\\user\\PycharmProjects\\blender_test\\test.png")
bpy.ops.object.modifier_add(type='DISPLACE')
bpy.context.object.modifiers['Displace'].strength = -1.0
bpy.context.object.modifiers['Displace'].texture = height_tex

# Material
color_mat = bpy.data.materials.new('colormap')
bpy.context.object.data.materials.append(color_mat)
color_mat.use_nodes = True
bsdf = color_mat.node_tree.nodes["Principled BSDF"]
color_tex = color_mat.node_tree.nodes.new('ShaderNodeTexImage')
color_tex.image = bpy.data.images.load("C:\\Users\\user\\PycharmProjects\\blender_test\\color.png")
color_mat.node_tree.links.new(bsdf.inputs['Base Color'], color_tex.outputs['Color'])
