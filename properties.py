import bpy # type: ignore

from bpy.props import StringProperty, IntProperty, BoolProperty # type: ignore

class VASTLOOM_PG_ProjectSettings(bpy.types.PropertyGroup):
    project_name: StringProperty(
        name = "Project Name",
        description = "Name of the VastLoom project",
        default = "Untitled World",
        maxlen = 128,
    ) # type: ignore

    project_seed: IntProperty(
        name = "Project Seed", 
        description = "Seed used for repeatable procedural generation of the world", 
        default = 1,
        min = 0,
    ) # type: ignore

    project_created: BoolProperty(
        name = "Project Created",
        description = "Indicates whether the project has been created or not",
        default = False,
    ) # type: ignore


