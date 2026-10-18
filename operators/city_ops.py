import bpy

from ..core import generate_city_grid, generate_city_radial
from ..bridge import create_house, create_road, create_collections, clear_collection

WORLD_NAME = "VastLoom World"


class VASTLOOM_OT_CreateCity(bpy.types.Operator):
    """Generate the city based on current settings"""

    bl_idname = "vastloom.create_city"
    bl_label = "Generate City"

    def execute(self, context):
        s = context.scene.Vastloom_Settings

        if s.city_layout_type == "RADIAL":
            layout = generate_city_radial(
                ring_count=s.ring_count,
                ring_radius=s.ring_radius,
                avenues_count=s.avenues_count,
                road_width=s.road_width,
                spacing=s.house_spacing,
                seed=s.seed,
                min_floors=s.min_floors,
                max_floors=s.max_floors,
            )
        else:
            angle_deg = s.street_angle if s.city_layout_type == "ANGLED" else 0.0
            layout = generate_city_grid(
                s.blocks_x,
                s.blocks_y,
                s.block_size,
                s.road_width,
                s.house_spacing,
                seed=s.seed,
                min_floors=s.min_floors,
                max_floors=s.max_floors,
                angle_deg=angle_deg,
            )

        clear_collection(WORLD_NAME)
        world = create_collections(WORLD_NAME, context.scene)
        roads_collection = create_collections("Roads", world)
        houses_collection = create_collections("Houses", world)

        for center, size, rot in layout["roads"]:
            create_road(center, size, roads_collection, rotation_z=rot)

        for i, (pos, rot, floors) in enumerate(layout["houses"], start=1):
            create_house(pos, rot, houses_collection, i, floors=floors)

        return {"FINISHED"}


# Alias for backwards compatibility with earlier UI
class VASTLOOM_OT_CreateHouse(VASTLOOM_OT_CreateCity):
    bl_idname = "vastloom.create_house"

