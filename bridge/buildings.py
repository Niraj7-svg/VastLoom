import math
from .collections import create_collections, create_cube_instance


def create_house(location, rotation_z, parent_collection, index, floors=1):
    """Create a dedicated sub-collection for each house containing linked instances for body, roof, and door."""
    house_col = create_collections(f"House_{index}", parent_collection)

    x, y, z = location
    floor_height = 2.5
    total_height = floors * floor_height

    # Body (instanced)
    create_cube_instance(
        f"House_{index}_Body",
        (x, y, z + total_height / 2.0),
        (4.0, 4.0, total_height),
        house_col,
        rotation_z,
    )

    # Roof (instanced)
    create_cube_instance(
        f"House_{index}_Roof",
        (x, y, z + total_height + 0.5),
        (4.5, 4.5, 1.0),
        house_col,
        rotation_z,
    )

    # Door (instanced)
    push = 2.0
    door_x = x - push * math.sin(rotation_z)
    door_y = y + push * math.cos(rotation_z)
    create_cube_instance(
        f"House_{index}_Door",
        (door_x, door_y, z + 0.7),
        (1.0, 0.2, 1.4),
        house_col,
        rotation_z,
    )

