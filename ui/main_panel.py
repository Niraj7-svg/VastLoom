import bpy
from .city_panel import draw_city_panel


class VASTLOOM_PT_MainPanel(bpy.types.Panel):
    """Main Vastloom control panel in the 3D Viewport sidebar."""

    bl_idname = "VASTLOOM_PT_MainPanel"
    bl_label = "Vastloom Studio"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Vastloom"

    def draw(self, context):
        layout = self.layout
        if not layout:
            return

        settings = context.scene.Vastloom_Settings

        # ==========================================
        # 1. GLOBAL PROJECT SETTINGS (Always Visible)
        # ==========================================
        header_box = layout.box()
        header_box.label(text="Project Setup", icon="WORLD")

        col = header_box.column(align=True)
        col.prop(settings, "project_name")
        col.prop(settings, "environment_type")

        layout.separator()

        # ==========================================
        # 2. DYNAMIC ENVIRONMENT SECTIONS
        # ==========================================
        if settings.environment_type == "CITY":
            draw_city_panel(self, layout, settings)

        elif settings.environment_type == "LANDSCAPE":
            self.draw_landscape_settings(layout, settings)

        elif settings.environment_type == "MOUNTAIN_CITY":
            draw_city_panel(self, layout, settings)
            layout.separator()
            self.draw_landscape_settings(layout, settings)

        # ==========================================
        # 3. ACTION / EXECUTION BUTTONS
        # ==========================================
        layout.separator()
        if settings.environment_type in ("CITY", "MOUNTAIN_CITY"):
            col = layout.column()
            col.scale_y = 1.4
            col.operator("vastloom.create_city", text="Generate City", icon="PLAY")
        else:
            col = layout.column()
            col.enabled = False
            col.operator("vastloom.create_city", text="Generate (Coming Soon)", icon="TIME")

    def draw_landscape_settings(self, layout, settings):
        """Draws controls specific to terrain generation."""
        box = layout.box()
        box.label(text="Terrain & Mountain Parameters", icon="OUTLINER_OB_MESH")

        col = box.column(align=True)
        col.label(text="Terrain Engine: Under Development", icon="INFO")

