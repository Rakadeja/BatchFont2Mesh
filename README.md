# BatchFont2Mesh (BF2M) Addon

<p align="left">
<!-- Badges cringelord area -->
  <img src="https://img.shields.io/badge/Blender-4.2%2B-F5792A?logo=blender" alt="Blender Version"/>
  <img src="https://img.shields.io/badge/Python-3.13-3776AB?logo=python" alt="Python Version"/>
  <img src="https://img.shields.io/badge/Version-1.1-green" alt="Version 1.1"/>
  <img src="https://img.shields.io/badge/Co--Developed%20with-Gemini%202.5%20Pro-4285F4?logo=google" alt="Co-developed with Gemini 2.5 Pro"/>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue" alt="License: MIT"/>
  </a>
</p>

<p align="left">
  <!-- TODO: Add a cool GIF of the addon in action -->
  <img src="https://placehold.co/600x300/1e1e1e/c0de42?text=Imagine+a+Sick+GIF+Here" alt="Placeholder GIF of the BF2M Addon" width="500">
</p>

Your new best friend for turning entire font files into properly beveled, processed, and organized 3D meshes directly within Blender.

Stop creating text one... character... at a... time. Let's automate the pain away.

For less *cringe*, see [README_REAL.md](README_REAL.md).

---

## ⚠️ WARNING ⚠️

**!! PLEASE NOTE:** This addon is fresh outta the oven. It works on my machine™, but who knows what fresh hell awaits on yours.

* **INTERNET REQUIRED:** On first launch, this addon will try to install `freetype-py` using `pip`. It needs an internet connection. If it fails, the addon will be disabled.
* **DON'T:** Use this for a client project with a deadline of tomorrow without testing it first.
* **DO:** Backup your project! Use Git! Save often! You get the picture.

---

## Description

Ever needed to generate a whole alphabet of 3D characters for a project? And then you realize you have to do it for every single symbol, number, and variation? And then you have to process each one? Yeah, hard pass.

This addon provides an in-editor UI for a streamlined, two-stage workflow:

1. **Prepare & Preview:** Load any font, and the addon will generate a live, editable preview object.
2. **Tweak & Generate:** Visually tweak your 3D text settings (size, extrusion, bevels, materials) and see the changes in real-time. When you're happy, click one button to batch-process every single character from the font into its own mesh, neatly organized into new collections.

---

## Features

I may have gone a little overboard, but I wanted '3d Spyro font' and *then* some.

* **Two-Stage Workflow:** A non-destructive "Prepare Font" and "Generate Meshes" process that gives you full control.
* **Live Preview:** Tweak settings in the UI and see them applied to a live text object in your viewport instantly. No more guessing games.
* **Full Font Processing:** Iterates through *every* available glyph in a `.ttf` or `.otf` file, not just A-Z.
* **Smart Collection Management:** Automatically creates a main collection (e.g., `[BF2M] Arial`) with `Unprocessed` and `Processed` sub-collections to keep your scene tidy.
  * Handles naming conflicts by appending `_1`, `_2`, etc. if a collection already exists.
* **Detailed Geometry Control:**
  * Character Size, Extrusion, Bevel Depth, and Bevel Resolution.
* **Transform Control:**
  * Set a universal location and rotation for all generated meshes.
* **Mix-and-Match Post-Processing:** Choose any combination of the following for your beveled geometry:
  * **Mark Sharp:** Automatically mark beveled edges as sharp for clean shading.
  * **Vertex Groups:** Generate "Inner" and "Bevel" vertex groups on each mesh.
  * **Multi-Material:** Assign a separate material to the beveled faces.
  * **Vertex Colors:** Generate a vertex color attribute to isolate inner and beveled faces, perfect for custom shaders.
* **Mesh Cleanup:**
  * Optional "Remove Doubles" (Merge by Distance) to clean up geometry.
* **Progress Bar:** A proper progress bar in the Blender status area so you know it's not dead, just thinking.
* **Dependency Manager:** Automatically installs the required `freetype-py` library into a local folder, avoiding system-wide conflicts.

---

## 🚀 Roadmap / Future Ideas 🚀

This is just the beginning. The Vibe is strong, but the Feature Creep is stronger.

* **Granular Character Selection:** Instead of all-or-nothing, an interface to pick and choose characters. Think custom ranges (e.g., A-Z, 0-9), specific character sets (`!@#$%^&*`), or even pasting in a custom string to generate only what you need.
* **Settings Presets:** The ability to save and load your entire configuration. Dial in the perfect chiseled look for "GothicStone" and the perfect soft look for "BubbleFont" and swap between them instantly.
* **Advanced UV Unwrapping:** Options to automatically run a Smart UV Project or maybe even mark seams on the bevels before unwrapping for more control.
* **Custom Naming Patterns:** Go beyond the default `FontName_A` with user-definable patterns like `{font}_{char}_{ascii}`.
* **Adaptive Bevel Scaling (The Holy Grail):** A smart algorithm to prevent small details (like the dot on an 'i' or the inside of an 'o') from getting obliterated or clipping when using large bevel depths. This would be a massive level-up.
* **More Post-Processing Mayhem:** Think Decimate, Remesh, or applying other modifiers automatically after generation.
* **Freetype-less Fallback Mode:** A "basic" mode that can run without `freetype-py` installed. It wouldn't know the character count and could only generate a user-specified string of characters, but it would improve accessibility for offline/restricted environments.
* **Verbose Logging:** An option to output a detailed log of the entire generation process into a timestamped file (`batchfont2mesh_UTCtimestamp.log`) for serious debugging.

---

## Installation (The Ritual - Now With More Steps!)

1. **Get the Goods:** Head to the **Releases** page on this GitHub repo and download the latest `BatchFont2Mesh.zip` file.

2. **DON'T UNZIP IT:** For real. Blender handles that part.

3. **Open the System Console (👀 IMPORTANT!):**
    * Before you install, go to `Window -> Toggle System Console` in Blender's top menu.
    * Keep this console window open! It's where our addon will print its installation progress and any errors. This is your lifeline if something goes wrong.

4. **Install in Blender:**
    * With the console open, go to `Edit -> Preferences`.
    * Navigate to the `Add-ons` tab.
    * Click `Install...` at the top right.
    * Find and select the `BatchFont2Mesh.zip` file you downloaded.

5. **Enable the Addon & Watch the Console:**
    * After installing, you should see "Object: BatchFont2Mesh (BF2M)" in the list.
    * Check the little box next to its name to enable it.
    * **Watch the System Console!** You should see messages about `pip` and `freetype-py` being installed. This is the magic happening. This step requires an internet connection and might take a moment.

6. **If It Doesn't Work: RESTART BLENDER!**
    * Sometimes, even after a successful install, Blender needs a swift kick to recognize the new packages. If the addon panel shows an error or seems broken, **completely close and restart Blender.** This usually fixes it.

7. **Witness the Magic:** A new "Batch Font To Mesh" panel should now appear in the **3D Viewport's sidebar** (press `N` to open it) under the **"Tool"** tab, fully functional.

---

## How to Use (The SparkNotes Version)

The whole workflow is designed to be top-to-bottom.

<p align="left">
  <table>
      <tr>
        <td><img src="https://placehold.co/400x450/1e1e1e/c0de42?text=UI+Panel+(Before+Prepare)" alt="UI Before Preparation"></td>
        <td><img src="https://placehold.co/400x450/1e1e1e/c0de42?text=UI+Panel+(After+Prepare)" alt="UI After Preparation"></td>
      </tr>
  </table>
</p>

### 📜 Step 1: Prepare Font

1. **Font Input:** In the BF2M panel, click the folder icon next to "Font File" and select a `.ttf` or `.otf` font from your computer.
2. **Prepare:** Smash that `Prepare Font` button.
3. **What Happens:** The addon will:
    * Load the font and count all its characters (glyphs).
    * Create a new collection structure in the Outliner (e.g., `[BF2M] MyFont`).
    * Create a live "Preview" text object in the viewport.
    * Unlock the rest of the UI for tweaking.

### ✂️ Step 2: Live Tweak

This is the fun part. With the "Preview" object visible, start changing the settings in the UI.

1. **Assign Materials:** Select a base material and, if you plan on using the "Multi-Material" mode, a bevel material.
2. **Adjust Geometry:** Play with the `Character Size`, `Extrude`, and `Bevel` sliders. You'll see the changes on the "Preview" object in real-time.
3. **Set Transforms:** Dial in the final `Translation` and `Rotation` you want for all the characters.
4. **Choose Post-Processing:** In the "Post-Processing Options" box, toggle on any and all of the bevel modes you want to apply.

### ✨ Step 3: Generate Meshes

Once the preview looks exactly how you want it...

1. **Generate:** Hit the big `Generate Meshes` button at the bottom.
2. **What Happens:** The addon will:
    * Display a progress bar at the bottom of the Blender window.
    * Loop through every single character in the font.
    * For each character, it creates a mesh, applies all your settings, runs your chosen post-processing steps, and names it correctly.
    * All the final meshes are placed in the `Processed` sub-collection.
    * The "Preview" object is deleted, and the UI resets, ready for the next font.

---

## Feedback / Contributing

Find a bug? Did the addon tell a bad joke? Got an idea?

* Please open an issue on the GitHub repository. The more detail, the better.
* Pull requests are welcome, but maybe open an issue first to chat about it.

---

## Credits

* **Rakadeja:** The visionary and prime directive officer.
* **Gemini 2.5 Pro:** The humble-but-rad code-monkey assistant.

---

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
