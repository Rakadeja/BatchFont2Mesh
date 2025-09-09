# BatchFont2Mesh (BF2M) for Blender

<p align="left">
  <img src="https://img.shields.io/badge/Blender-4.2%2B-F5792A?logo=blender" alt="Blender Version"/>
  <img src="https://img.shields.io/badge/Python-3.13-3776AB?logo=python" alt="Python Version"/>
  <img src="https://img.shields.io/badge/Version-1.2-green" alt="Version 1.2"/>
  <img src="https://img.shields.io/badge/Co--Developed%20with-Gemini%202.5%20Pro-4285F4?logo=google" alt="Co-developed with Gemini 2.5 Pro"/>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue" alt="License: MIT"/>
  </a>
</p>

<p align="left">
  <!-- A demonstration of the addon's user interface and functionality. -->
  <img src="https://placehold.co/600x300/1e1e1e/c0de42?text=Demonstration+of+BF2M+Addon" alt="Demonstration of the BF2M Addon" width="500">
</p>

BatchFont2Mesh (BF2M) is a powerful Blender addon designed to streamline the procedural generation of 3D text meshes from font files. It provides an efficient, UI-driven workflow for creating, processing, and organizing large sets of characters.

---

## ⚠️ Important Notes ⚠️

* **Internet Connection Required:** On first-time activation, this addon will attempt to install the `freetype-py` Python library using `pip`. This is a one-time process that requires an active internet connection.
* **Beta Software:** This addon is in active development. While stable, it is recommended to back up your projects before use. Please report any issues encountered.

---

## Description

BF2M addresses the challenge of creating individual 3D models for every character in a font, a task that is typically manual and time-consuming. The addon implements a non-destructive, two-stage process to automate this entirely within Blender.

1. **Preparation & Live Preview:** Users load a font file and generate a live, editable preview object in the 3D viewport.
2. **Configuration & Batch Generation:** Users can visually configure all text parameters (geometry, materials, transforms) with real-time feedback. Once satisfied, a single command generates individual, processed meshes for every glyph in the font, which are then named and organized automatically.

---

## Key Features

* **Two-Stage Workflow:** A logical "Prepare" and "Generate" process provides full control and instant visual feedback.
* **Live Preview Object:** All geometry and transform settings are updated on a preview object in real-time, eliminating guesswork.
* **Comprehensive Font Processing:** Utilizes the Freetype library to iterate through every available glyph in a `.ttf` or `.otf` file.
* **Automated Scene Organization:** Automatically creates a main collection (e.g., `[BF2M] Arial`) with `Unprocessed` and `Processed` sub-collections. It also handles naming conflicts for pre-existing collections.
* **Detailed Geometry Control:** Includes settings for Character Size, Extrusion, Bevel Depth, and Bevel Resolution.
* **Flexible Post-Processing Options:** Apply any combination of the following operations to beveled geometry:
  * **Mark Sharp:** Automatically mark beveled edges as sharp for clean normals and shading.
  * **Vertex Groups:** Generate "Inner" and "Bevel" vertex groups for advanced masking and procedural workflows.
  * **Multi-Material Assignment:** Assign a separate material to beveled faces.
  * **Vertex Colors:** Generate a vertex color attribute to isolate inner and beveled faces for use in custom shaders.
* **Mesh Cleanup:** Includes an optional "Merge by Distance" operation to clean up generated topology.
* **Robust Dependency Management:** Automatically bootstraps `pip` (if missing) and installs required Python packages within Blender's environment, ensuring a self-contained and reliable installation.

---

## 🚀 Roadmap 🚀

Future development will focus on expanding the addon's flexibility and power-user features.

* **Selective Character Generation:** An interface for selecting specific character ranges or custom character sets for generation.
* **Settings Presets:** The ability to save and load entire addon configurations for different styles.
* **Advanced UV Unwrapping:** Automated UV unwrapping options, such as Smart UV Project or custom seam marking.
* **Custom Naming Conventions:** User-definable file naming patterns for generated meshes.
* **Adaptive Bevel Scaling:** An algorithm to intelligently scale bevels and prevent geometric artifacts on small character details.
* **Additional Post-Processing:** Integration of other operations, such as Decimate or Remesh modifiers.
* **Verbose Logging:** An option to generate a detailed log file of the batch process for debugging.

---

## Installation Instructions

1. **Download the Addon:** Go to the **Releases** page of the GitHub repository and download the latest `BatchFont2Mesh.zip` file. Do not extract the zip archive.

2. **Open Blender's System Console:** Before installing, it is highly recommended to open the System Console via `Window -> Toggle System Console`. This window provides detailed feedback on the installation process, which is crucial for troubleshooting.

3. **Install from File:**
    * In Blender, navigate to `Edit -> Preferences`.
    * Select the `Add-ons` tab.
    * Click the `Install...` button and select the downloaded `BatchFont2Mesh.zip` file.

4. **Enable the Addon:**
    * The addon will now appear in your addons list. Locate "Object: BatchFont2Mesh (BF2M)".
    * Enable it by checking the box next to its name.
    * **Monitor the System Console:** Upon activation, the addon will attempt to install its dependencies. You should see log messages related to `pip` and `freetype-py`. This requires an internet connection.

5. **Restart Blender (If Necessary):** In some cases, Blender may require a restart to correctly load the newly installed modules. If the addon's panel shows an error after installation, please close and reopen Blender.

6. **Verify Installation:** The "Batch Font To Mesh" panel will be available in the 3D Viewport's sidebar (hotkey `N`), under the "Tool" tab.

---

## Usage Guide

The addon's workflow is organized from top to bottom in the UI panel.

<p align="left">
  <table>
      <tr>
        <td><img src="https://placehold.co/400x450/1e1e1e/c0de42?text=UI+Panel+(Before+Preparation)" alt="UI Panel Before Preparation"></td>
        <td><img src="https://placehold.co/400x450/1e1e1e/c0de42?text=UI+Panel+(After+Preparation)" alt="UI Panel After Preparation"></td>
      </tr>
  </table>
</p>

### Step 1: Prepare Workspace

1. **Select Font File:** In the "Font Input" section, click the folder icon to browse for a `.ttf` or `.otf` file.
2. **Click Prepare Font:** This initiates the preparation process. The addon will load the font, analyze its contents, create the necessary collection structure in the Outliner, and generate the live "Preview" object. The rest of the UI options will then become active.

### Step 2: Configure Settings

With the "Preview" object visible in the viewport, adjust the settings in the panel to achieve the desired look. All changes will be reflected on the preview object in real-time.

1. **Assign Materials:** Select a base material and an optional bevel material (for use with the "Multi-Material" mode).
2. **Adjust Geometry:** Modify the `Character Size`, `Extrude`, and `Bevel` properties.
3. **Set Transforms:** Define the final `Translation` and `Rotation` to be applied to all generated meshes.
4. **Select Post-Processing Options:** Enable one or more of the post-processing toggles to control how the final mesh geometry is treated.

### Step 3: Generate Meshes

Once the preview object matches your specifications, you are ready for batch generation.

1. **Click Generate Meshes:** This will execute the main batch process. A progress bar will appear in the Blender status bar at the bottom of the window.
2. The addon will iterate through all characters in the font, creating and processing a mesh for each one. The final objects will be placed in the "Processed" sub-collection. Upon completion, the preview object is removed, and the UI is reset.

---

## Contributing

Bug reports and feature requests are welcome. Please use the **Issues** tab on the GitHub repository to submit them. Pull requests are also welcome for consideration.

---

## Credits

* **Author:** Rakadeja
* **Development Assistance:** Gemini 2.5 Pro

---

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
