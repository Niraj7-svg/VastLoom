import bpy

from .properties import classes as property_classes, VASTLOOM_PG_ProjectSettings
from .ui import classes as ui_classes
from .operators import classes as operator_classes

# Blender needs this to know what to register
classes = property_classes + ui_classes + operator_classes


def register():
    # Register every class with blender
    for cls in classes:
        bpy.utils.register_class(cls)

    # Attach our settings notebook to every Blender Scene
    bpy.types.Scene.Vastloom_Settings = bpy.props.PointerProperty(  # type: ignore
        type=VASTLOOM_PG_ProjectSettings
    )

    
def unregister():
    del bpy.types.Scene.Vastloom_Settings # type: ignore
        
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
        
