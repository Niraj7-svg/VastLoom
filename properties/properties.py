import bpy
from bpy.props import (
    StringProperty,
    IntProperty,
    FloatProperty,
    EnumProperty,
)


class VASTLOOM_PG_ProjectSettings(bpy.types.PropertyGroup):
    """Stores all Vastloom settings attached to the current scene."""

    # The name of this project

    project_name: StringProperty(  # type: ignore
        name="Project name",
        description="Name of the Vastloom Project",
        default="untitled world",
        maxlen=128,
    )

    environment_type: EnumProperty(
        name="Environment Type",
        description="What kind of world to generate",
        items=[
            ("LANDSCAPE", "Landscape", "Pure terrian with few buildings"),
            ("CITY", "City", "Urban city environment"),
            ("MOUNTAIN_CITY", "Mountain City", "City built into mountains"),
        ],
        default="LANDSCAPE",
    )  # type: ignore

    blocks_x: IntProperty(  # type: ignore
        name="Blocks X",
        description="City blocks along X",
        default=3,
        min=1,
        max=8,
    )
    blocks_y: IntProperty(  # type: ignore
        name="Blocks Y",
        description="City blocks along Y",
        default=3,
        min=1,
        max=8,
    )
    city_layout_type: EnumProperty(  # type: ignore
        name="Layout Style",
        description="Geometric pattern of the city streets",
        items=[
            ("GRID", "Regular Grid", "Classic Manhattan-style orthogonal grid"),
            ("ANGLED", "Angled Diagonal", "Streets running at diagonal angles"),
            ("RADIAL", "Curved / Radial", "Curved circular concentric ring streets with radial avenues"),
        ],
        default="GRID",
    )
    street_angle: FloatProperty(  # type: ignore
        name="Street Angle",
        description="Grid rotation angle in degrees",
        default=30.0,
        min=0.0,
        max=90.0,
    )
    ring_count: IntProperty(  # type: ignore
        name="Rings",
        description="Number of concentric circular street rings",
        default=3,
        min=1,
        max=8,
    )
    ring_radius: FloatProperty(  # type: ignore
        name="Ring Step",
        description="Distance between concentric road rings",
        default=30.0,
        min=15.0,
        max=100.0,
    )
    avenues_count: IntProperty(  # type: ignore
        name="Avenues",
        description="Radial avenues extending from city center",
        default=6,
        min=3,
        max=16,
    )

    block_size: FloatProperty(  # type: ignore
        name="Block Size",
        description="Side length of one square block in meters",
        default=40.0,
        min=16.0,
        max=200.0,
    )

    house_spacing: FloatProperty(
        # type: ignore
        name="House Spacing",
        description="Distance between houses in meters",
        default=6.0,
        min=0.0,
        max=100.0,
    )

    road_width: FloatProperty(  # type: ignore
        name="Road Width",
        description="Width of the road between the two rows of houses",
        default=8.0,
        min=2.0,
        max=50.0,
    )

    seed: IntProperty(  # type: ignore
        name="Random Seed",
        description="Seed for random variations (heights, styles)",
        default=42,
        min=0,
    )

    min_floors: IntProperty(  # type: ignore
        name="Min Floors",
        description="Minimum building stories",
        default=1,
        min=1,
        max=10,
    )

    max_floors: IntProperty(  # type: ignore
        name="Max Floors",
        description="Maximum building stories",
        default=4,
        min=1,
        max=20,
    )
