import bpy #type: ignore

#IMPORTING THE CLASS FORM THE PROERTIES.PY FILE
from .properties import VASTLOOM_PG_ProjectSettings  # type: ignore
CLASSES = (
    VASTLOOM_PG_ProjectSettings,
)


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)
