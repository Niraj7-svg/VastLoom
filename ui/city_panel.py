def draw_city_panel(self, layout, settings):
    """Draws controls specific to urban generation."""
    box = layout.box()
    box.label(text="Urban Layout Parameters", icon="HOME")

    col = box.column(align=True)
    col.prop(settings, "city_layout_type")

    if settings.city_layout_type in ("GRID", "ANGLED"):
        col.prop(settings, "blocks_x")
        col.prop(settings, "blocks_y")
        col.prop(settings, "block_size")
        if settings.city_layout_type == "ANGLED":
            col.prop(settings, "street_angle")
    elif settings.city_layout_type == "RADIAL":
        col.prop(settings, "ring_count")
        col.prop(settings, "ring_radius")
        col.prop(settings, "avenues_count")

    col.prop(settings, "house_spacing")
    col.prop(settings, "road_width")

    box_var = box.box()
    box_var.label(text="Skyline Variations", icon="RNDCURVE")
    col_var = box_var.column(align=True)
    col_var.prop(settings, "seed")
    col_var.prop(settings, "min_floors")
    col_var.prop(settings, "max_floors")

