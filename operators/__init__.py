"""
Vastloom Operators Package
"""

from .city_ops import VASTLOOM_OT_CreateHouse, VASTLOOM_OT_CreateCity

classes = [
    VASTLOOM_OT_CreateHouse,
    VASTLOOM_OT_CreateCity,
]

__all__ = [
    "classes",
    "VASTLOOM_OT_CreateHouse",
    "VASTLOOM_OT_CreateCity",
]