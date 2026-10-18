from .collections import create_cube_instance


def create_road(center, size, collection, rotation_z=0.0):
    """A flat road slab instanced from the shared mesh."""
    cx, cy, cz = center
    sx, sy = size
    return create_cube_instance("Road", (cx, cy, cz + 0.05), (sx, sy, 0.1), collection, rotation_z=rotation_z)

