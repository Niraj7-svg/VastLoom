import bpy
import bmesh

_SHARED_MESH_NAME = "VastLoom_UnitCube"


def get_or_create_unit_cube_mesh():
    """
    Returns a shared 1x1x1 unit cube mesh datablock.
    Objects using this mesh share the exact same vertex memory (Option + D style linked duplication).
    """
    mesh = bpy.data.meshes.get(_SHARED_MESH_NAME)
    if mesh is not None:
        return mesh

    mesh = bpy.data.meshes.new(_SHARED_MESH_NAME)
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bm.to_mesh(mesh)
    bm.free()
    return mesh


def clear_collection(name):
    """Delete an old collection and everything in it, so regenerating doesn't stack duplicates."""
    old = bpy.data.collections.get(name)
    if old is None:
        return
    for obj in list(old.objects):
        bpy.data.objects.remove(obj, do_unlink=True)
    for child in list(old.children):
        clear_collection(child.name)
    bpy.data.collections.remove(old)


def create_collections(name, parent_col):
    """Create a new collection and link it under parent_col (or scene.collection)."""
    collection = bpy.data.collections.new(name)
    if hasattr(parent_col, "children"):
        parent_col.children.link(collection)
    elif hasattr(parent_col, "collection"):
        parent_col.collection.children.link(collection)
    return collection


def create_cube_instance(name, location, dimension, collection, rotation_z=0.0):
    """
    Spawns an object that shares the base unit-cube mesh data (Option + D linked duplication).
    Scales and positions via object transform matrices with zero duplicated vertex memory!
    """
    mesh = get_or_create_unit_cube_mesh()
    obj = bpy.data.objects.new(name, mesh)
    obj.location = location
    obj.scale = dimension
    obj.rotation_euler = (0.0, 0.0, rotation_z)
    collection.objects.link(obj)
    return obj

