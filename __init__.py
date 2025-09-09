# __init__.py

bl_info = {
    "name": "BatchFont2Mesh (BF2M)",
    "author": "Rakadeja",
    "version": (1, 3, 0),
    "blender": (4, 2, 0),
    "location": "3D View > Sidebar > Tool Tab > Batch Font To Mesh",
    "description": "Batch generates 3D mesh objects from a font's characters. Requires internet for first-time setup for full-functionality. Reset Blender after first install!",
    "warning": "This addon may install third-party libraries (freetype-py) using pip! See (Window -> Toggle System Console) for more info.",
    "doc_url": "https://github.com/Rakadeja/BatchFont2Mesh",
    "category": "Object",
}

# ==== Dependency Management ====
from . import dependencies

dependencies_met = False
try:
    dependencies.install_dependencies()
    if dependencies.are_dependencies_installed():
        dependencies_met = True
except Exception as e:
    print(
        f"BF2M Critical Error: Failed to install dependencies. Addon will be disabled. Error: {e}"
    )

# ==== Regular Imports ====
if dependencies_met:
    import bpy
    import os
    import sys
    import math
    import bmesh
    import freetype
    from bpy.props import (
        StringProperty,
        FloatProperty,
        FloatVectorProperty,
        BoolProperty,
        PointerProperty,
        IntProperty,
    )
    from . import ui
else:
    import bpy
    from . import ui

    class BF2M_Properties(bpy.types.PropertyGroup):
        """Placeholder PropertyGroup for when dependencies are not met."""

        pass

    class BF2M_OT_Prepare(bpy.types.Operator):
        """Placeholder Operator that displays an error and is always disabled."""

        bl_idname = "bf2m.prepare"
        bl_label = "Prepare Font (Dependencies Missing)"

        def execute(self, context):
            """Reports an error when clicked."""
            self.report(
                {"ERROR"},
                "Dependencies are missing. Please check the System Console for errors.",
            )
            return {"CANCELLED"}

        @classmethod
        def poll(cls, context):
            """Ensures this operator is always greyed out and unusable."""
            return False

    class BF2M_OT_Generate(bpy.types.Operator):
        """Placeholder Operator that displays an error and is always disabled."""

        bl_idname = "bf2m.generate"
        bl_label = "Generate Meshes (Dependencies Missing)"

        def execute(self, context):
            """Reports an error when clicked."""
            self.report(
                {"ERROR"},
                "Dependencies are missing. Please check the System Console for errors.",
            )
            return {"CANCELLED"}

        @classmethod
        def poll(cls, context):
            """Ensures this operator is always greyed out and unusable."""
            return False


# This block contains the entire functional addon logic.
if dependencies_met:

    def update_preview_grid(self, context):
        """Updates the preview object's text body to show a grid of all available glyphs."""
        props = context.scene.bf2m_props
        preview_obj_name = props.preview_object_name
        if not preview_obj_name or preview_obj_name not in bpy.data.objects:
            return

        preview_obj = bpy.data.objects[preview_obj_name]

        if not props.preview_all_glyphs:
            preview_obj.data.body = "Preview"
            return

        try:
            face = freetype.Face(bpy.path.abspath(props.font_path))
            char_map = face.get_chars()
            grid_string = ""
            grid_width = props.preview_grid_width

            # Use a counter to handle newlines correctly, skipping null glyphs
            char_count = 0
            for char_code, glyph_index in char_map:
                if glyph_index == 0:
                    continue
                grid_string += chr(char_code)
                char_count += 1
                if char_count % grid_width == 0:
                    grid_string += "\n"
            preview_obj.data.body = grid_string
        except Exception as e:
            preview_obj.data.body = f"Error generating preview:\n{e}"

    def update_preview_object(self, context):
        """Finds the preview text object and applies the current UI settings to it."""
        preview_obj_name = context.scene.bf2m_props.preview_object_name
        if not preview_obj_name or preview_obj_name not in bpy.data.objects:
            return

        preview_obj = bpy.data.objects[preview_obj_name]
        text_data = preview_obj.data

        text_data.size = self.char_size
        text_data.extrude = self.char_extrude
        text_data.bevel_depth = self.bevel_depth
        text_data.bevel_resolution = self.bevel_resolution
        preview_obj.location = self.translation
        preview_obj.rotation_euler = (
            math.radians(self.rotation[0]),
            math.radians(self.rotation[1]),
            math.radians(self.rotation[2]),
        )
        update_preview_grid(self, context)

    class BF2M_Properties(bpy.types.PropertyGroup):
        """Stores all the properties and settings for the BF2M addon."""

        font_path: StringProperty(
            name="Font File",
            description="Path to the .ttf or .otf font file",
            subtype="FILE_PATH",
        )
        material_base: PointerProperty(
            name="Base Material",
            description="Material for the main character mesh",
            type=bpy.types.Material,
        )
        material_bevel: PointerProperty(
            name="Bevel Material",
            description="Material for the beveled edges",
            type=bpy.types.Material,
        )
        char_size: FloatProperty(
            name="Character Size", default=1.0, min=0.01, update=update_preview_object
        )
        char_extrude: FloatProperty(
            name="Extrude", default=0.1, min=0.0, update=update_preview_object
        )
        bevel_depth: FloatProperty(
            name="Bevel Depth", default=0.02, min=0.0, update=update_preview_object
        )
        bevel_resolution: IntProperty(
            name="Bevel Resolution", default=2, min=0, update=update_preview_object
        )
        translation: FloatVectorProperty(
            name="Translation",
            subtype="TRANSLATION",
            size=3,
            default=(0.0, 0.0, 0.0),
            update=update_preview_object,
        )
        rotation: FloatVectorProperty(
            name="Rotation",
            subtype="EULER",
            unit="ROTATION",
            size=3,
            default=(0.0, 0.0, 0.0),
            update=update_preview_object,
        )
        bevel_mode_sharp: BoolProperty(
            name="Mark Sharp", default=True, description="Mark beveled edges as sharp"
        )
        bevel_mode_vgroup: BoolProperty(
            name="Vertex Groups",
            default=False,
            description="Create 'Inner' and 'Bevel' vertex groups",
        )
        bevel_mode_material: BoolProperty(
            name="Multi-Material",
            default=False,
            description="Assign a separate material to beveled faces",
        )
        bevel_mode_vcolor: BoolProperty(
            name="Vertex Colors",
            default=False,
            description="Create a vertex color attribute for bevels",
        )
        remove_doubles: BoolProperty(
            name="Remove Doubles",
            default=True,
            description="Run a 'Merge by Distance' operation",
        )
        merge_distance: FloatProperty(
            name="Merge Distance",
            default=0.0001,
            min=0.0,
            description="Threshold for merging vertices",
        )
        preview_all_glyphs: BoolProperty(
            name="Preview All Glyphs",
            default=False,
            description="Display all font characters in the preview object as a grid",
            update=update_preview_grid,
        )
        preview_grid_width: IntProperty(
            name="Grid Width",
            default=16,
            min=1,
            soft_max=64,
            description="Number of characters per line in the grid preview",
            update=update_preview_grid,
        )
        status_text: StringProperty(default="Select a font file to begin.")
        status_icon: StringProperty(default="INFO")
        char_count: IntProperty(default=0)
        is_prepared: BoolProperty(default=False)
        preview_object_name: StringProperty(default="")

    class BF2M_OT_Prepare(bpy.types.Operator):
        """Prepares the workspace by validating the font, creating collections, etc."""

        bl_idname = "bf2m.prepare"
        bl_label = "Prepare Font"
        bl_options = {"REGISTER", "UNDO"}

        def execute(self, context):
            """Main execution logic for the Prepare operator."""
            props = context.scene.bf2m_props
            props.is_prepared = False
            if not props.font_path or not os.path.exists(
                bpy.path.abspath(props.font_path)
            ):
                props.status_text = "Error: Font file not found."
                props.status_icon = "ERROR"
                return {"CANCELLED"}
            font_name = os.path.basename(props.font_path).split(".")[0]
            sanitized_name = "".join(
                c for c in font_name if c.isalnum() or c in ["_", "-"]
            )
            try:
                face = freetype.Face(bpy.path.abspath(props.font_path))
                props.char_count = face.num_glyphs
                font_data = bpy.data.fonts.load(
                    filepath=bpy.path.abspath(props.font_path)
                )
            except Exception as e:
                props.status_text = f"Error loading font: {e}"
                props.status_icon = "ERROR"
                print("\n" + "=" * 40)
                print("BF2M CRITICAL ERROR: Failed during font preparation.")
                print(f"Font Path: {props.font_path}")
                print(f"Error Details: {e}")
                print("=" * 40 + "\n")
                self.report(
                    {"ERROR"},
                    "Failed to prepare font. Check System Console for details.",
                )
                return {"CANCELLED"}

            base_col_name = f"[BF2M] {sanitized_name}"
            final_col_name = base_col_name
            i = 1
            while final_col_name in bpy.data.collections:
                final_col_name = f"{base_col_name}_{i}"
                i += 1
            main_col = bpy.data.collections.new(final_col_name)
            unprocessed_col = bpy.data.collections.new("Unprocessed")
            processed_col = bpy.data.collections.new("Processed")
            context.scene.collection.children.link(main_col)
            main_col.children.link(unprocessed_col)
            main_col.children.link(processed_col)
            text_curve_data = bpy.data.curves.new(
                name=f"{sanitized_name}_Preview_Data", type="FONT"
            )
            preview_obj = bpy.data.objects.new(
                name=f"{sanitized_name}_Preview", object_data=text_curve_data
            )
            unprocessed_col.objects.link(preview_obj)
            preview_obj.data.body = "Preview"
            preview_obj.data.font = font_data
            props.preview_object_name = preview_obj.name
            context.view_layer.objects.active = preview_obj
            preview_obj.select_set(True)
            props.status_text = (
                f"Font '{font_name}' loaded. ({props.char_count} glyphs)"
            )
            props.status_icon = "CHECKMARK"
            props.is_prepared = True

            update_preview_object(props, context)
            self.report({"INFO"}, "BF2M Workspace prepared successfully.")
            return {"FINISHED"}

    class BF2M_OT_Generate(bpy.types.Operator):
        """
        The main operator that batch-processes the entire font into individual
        mesh objects based on the currently configured settings.
        """

        bl_idname = "bf2m.generate"
        bl_label = "Generate Meshes"
        bl_options = {"REGISTER", "UNDO"}

        @classmethod
        def poll(cls, context):
            """Greys out the 'Generate Meshes' button if the workspace is not prepared."""
            return context.scene.bf2m_props.is_prepared

        def execute(self, context):
            """Main execution logic for the Generate operator."""
            props = context.scene.bf2m_props
            wm = context.window_manager

            font_path = bpy.path.abspath(props.font_path)
            font_name = os.path.basename(font_path).split(".")[0]
            sanitized_name = "".join(c for c in font_name if c.isalnum())

            try:
                face = freetype.Face(font_path)
                char_map = list(face.get_chars())
                total_chars = len(char_map)
            except Exception as e:
                self.report({"ERROR"}, f"Failed to inspect font with Freetype: {e}")
                return {"CANCELLED"}

            main_col = next(
                (
                    c
                    for c in bpy.data.collections
                    if c.name.startswith(f"[BF2M] {sanitized_name}")
                ),
                None,
            )
            if not main_col:
                self.report(
                    {"ERROR"}, f"Could not find main collection for '{sanitized_name}'"
                )
                return {"CANCELLED"}

            processed_col = main_col.children.get("Processed")
            if not processed_col:
                self.report({"ERROR"}, "Could not find 'Processed' sub-collection!")
                return {"CANCELLED"}

            preview_obj = bpy.data.objects.get(props.preview_object_name)
            if not preview_obj:
                self.report(
                    {"ERROR"}, "Preview object is missing! Please Prepare Font again."
                )
                return {"CANCELLED"}
            blender_font = preview_obj.data.font

            wm.progress_begin(0, total_chars)
            depsgraph = context.evaluated_depsgraph_get()

            for i, (char_code, glyph_index) in enumerate(char_map):
                wm.progress_update(i)
                props.status_text = f"Processing char {i+1}/{total_chars}..."
                if glyph_index == 0:
                    continue
                character = chr(char_code)

                temp_text_data = bpy.data.curves.new(
                    name="temp_text_for_conversion", type="FONT"
                )
                temp_text_obj = bpy.data.objects.new(
                    name="temp_text_obj", object_data=temp_text_data
                )

                temp_text_obj.data.body = character
                temp_text_obj.data.font = blender_font
                temp_text_obj.data.size = props.char_size
                temp_text_obj.data.extrude = props.char_extrude
                temp_text_obj.data.bevel_depth = props.bevel_depth
                temp_text_obj.data.bevel_resolution = props.bevel_resolution

                try:
                    evaluated_mesh_data = temp_text_obj.to_mesh(
                        preserve_all_data_layers=True, depsgraph=depsgraph
                    )
                except RuntimeError:
                    bpy.data.objects.remove(temp_text_obj, do_unlink=True)
                    bpy.data.curves.remove(temp_text_data)
                    continue

                final_mesh_data = evaluated_mesh_data.copy()
                mesh_obj_name = f"{sanitized_name}_{character}"
                mesh_obj = bpy.data.objects.new(
                    name=mesh_obj_name, object_data=final_mesh_data
                )
                processed_col.objects.link(mesh_obj)

                bpy.data.objects.remove(temp_text_obj, do_unlink=True)
                bpy.data.curves.remove(temp_text_data)
                # bpy.data.meshes.remove(evaluated_mesh_data)

                if props.material_base:
                    mesh_obj.data.materials.append(props.material_base)
                if props.bevel_mode_material and props.material_bevel:
                    mesh_obj.data.materials.append(props.material_bevel)

                context.view_layer.objects.active = mesh_obj
                mesh_obj.select_set(True)

                if (
                    props.bevel_mode_sharp
                    or props.bevel_mode_vgroup
                    or props.bevel_mode_vcolor
                ):
                    bpy.ops.object.mode_set(mode="EDIT")
                    if len(mesh_obj.material_slots) > 1:
                        bpy.ops.mesh.select_all(action="DESELECT")
                        mesh_obj.active_material_index = 1
                        bpy.ops.object.material_slot_select()
                    if props.bevel_mode_sharp:
                        bpy.ops.mesh.mark_sharp()
                    if props.bevel_mode_vgroup:
                        bevel_vg = mesh_obj.vertex_groups.new(name="Bevel")
                        inner_vg = mesh_obj.vertex_groups.new(name="Inner")
                        bpy.ops.object.vertex_group_assign()
                        bpy.ops.mesh.select_all(action="INVERT")
                        mesh_obj.vertex_groups.active = inner_vg
                        bpy.ops.object.vertex_group_assign()
                    if props.bevel_mode_vcolor:
                        vcol_layer = mesh_obj.data.vertex_colors.new(name="BF2M_Colors")
                        bm = bmesh.from_edit_mesh(mesh_obj.data)
                        color_bevel = (1.0, 0.0, 0.0, 1.0)
                        color_inner = (0.0, 0.0, 1.0, 1.0)
                        for face in bm.faces:
                            color = color_bevel if face.select else color_inner
                            for loop_idx in face.loops:
                                vcol_layer.data[loop_idx].color = color
                        bmesh.update_edit_mesh(mesh_obj.data)
                    bpy.ops.object.mode_set(mode="OBJECT")

                if props.remove_doubles:
                    bpy.ops.object.mode_set(mode="EDIT")
                    bpy.ops.mesh.select_all(action="SELECT")
                    bpy.ops.mesh.remove_doubles(threshold=props.merge_distance)
                    bpy.ops.object.mode_set(mode="OBJECT")

                mesh_obj.location = props.translation
                mesh_obj.rotation_euler = (
                    math.radians(props.rotation[0]),
                    math.radians(props.rotation[1]),
                    math.radians(props.rotation[2]),
                )
                mesh_obj.select_set(False)

            wm.progress_end()
            props.status_text = (
                f"Generation Complete! Created {len(processed_col.objects)} meshes."
            )
            props.status_icon = "CHECKMARK"

            bpy.data.objects.remove(preview_obj, do_unlink=True)
            props.is_prepared = False

            self.report({"INFO"}, "Batch Font to Mesh generation complete.")
            return {"FINISHED"}


# ==== Register & Unregister ====
classes = (
    BF2M_Properties,
    BF2M_OT_Prepare,
    BF2M_OT_Generate,
    ui.BF2M_PT_Panel,
)


def register():
    """Registers all addon classes with Blender."""
    for cls in classes:
        bpy.utils.register_class(cls)
    if dependencies_met:
        bpy.types.Scene.bf2m_props = PointerProperty(type=BF2M_Properties)


def unregister():
    """Unregisters all addon classes from Blender."""
    if dependencies_met and hasattr(bpy.types.Scene, "bf2m_props"):
        del bpy.types.Scene.bf2m_props
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
