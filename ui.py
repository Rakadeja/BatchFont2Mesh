# ui.py

import bpy
from . import dependencies


class BF2M_PT_Panel(bpy.types.Panel):
    """The main UI Panel for the Batch Font To Mesh addon."""

    bl_label = "Batch Font To Mesh"
    bl_idname = "BF2M_PT_main_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"

    def draw(self, context):
        layout = self.layout

        if not dependencies.are_dependencies_installed():
            box = layout.box()
            box.label(text="Dependencies Missing!", icon="ERROR")
            box.label(text="Freetype-py failed to install.")
            box.label(text="Check Blender's System Console for errors.")
            return

        props = context.scene.bf2m_props

        # ==== Input & Status ====
        box = layout.box()
        box.label(text="1. Font Input", icon="FILE_FONT")
        box.prop(props, "font_path")
        box.operator("bf2m.prepare")
        box = layout.box()
        row = box.row()
        row.label(text="Status:", icon=props.status_icon)
        row.label(text=props.status_text)

        if props.is_prepared:
            box = layout.box()
            box.label(text="Live Preview Options", icon="TEXT")
            box.prop(props, "preview_all_glyphs")
            # The Grid Width property only shows up if the toggle is on.
            if props.preview_all_glyphs:
                box.prop(props, "preview_grid_width")

            # ==== Live-Tweak Sections ====
            box = layout.box()
            box.label(text="2. Live Tweaking", icon="SETTINGS")
            box.prop(props, "material_base")
            box.prop(props, "material_bevel")
            box.label(text="Text Geometry")
            box.prop(props, "char_size")
            box.prop(props, "char_extrude")
            bevel_box = box.box()
            bevel_box.label(text="Bevel")
            bevel_box.prop(props, "bevel_depth")
            bevel_box.prop(props, "bevel_resolution")
            box.label(text="Transforms")
            box.prop(props, "translation")
            box.prop(props, "rotation")
            box.label(text="Post-Processing Options")
            post_proc_box = box.box()
            col = post_proc_box.column()
            row = col.row()
            row.prop(props, "bevel_mode_sharp")
            row.prop(props, "bevel_mode_vgroup")
            row = col.row()
            row.prop(props, "bevel_mode_material")
            row.prop(props, "bevel_mode_vcolor")
            doubles_row = post_proc_box.row()
            doubles_row.prop(props, "remove_doubles")
            if props.remove_doubles:
                doubles_row.prop(props, "merge_distance")

            box = layout.box()
            box.label(text="3. Final Generation", icon="MOD_MESHDEFORM")
            row = box.row()
            row.scale_y = 1.5
            row.operator("bf2m.generate")
