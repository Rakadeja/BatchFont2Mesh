# BatchFont2Mesh (BF2M) Addon

<p align="left">
<!-- Badges cringelord area -->
  <img src="https://img.shields.io/badge/Blender-4.2%2B-F5792A?logo=blender" alt="Blender Version"/>
  <img src="https://img.shields.io/badge/Python-3.13-3776AB?logo=python" alt="Python Version"/>
  <img src="https://img.shields.io/badge/Version-1.3.0-green" alt="Version 1.3.0"/>
  <img src="https://img.shields.io/badge/Co--Developed%20with-Gemini%202.5%20Pro-4285F4?logo=google" alt="Co-developed with Gemini 2.5 Pro"/>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue" alt="License: MIT"/>
  </a>
</p>

<p align="left">
  <table>
      <tr>
        <td><img src="https://github.com/user-attachments/assets/78536709-3f64-4738-9b9e-2a83980bb9b6" alt="BatchFont2Mesh UI Panel"/></td>
        <td><img src="https://github.com/user-attachments/assets/2d013219-fcb0-4b73-beb6-10578aedf145" alt="Example Text Mesh Output"/></td>
      </tr>
  </table>
</p>

Your new best friend for turning entire font files into properly beveled, processed, and organized 3D meshes directly within Blender.

Stop creating text one... character... at a... time. Let's automate the pain away.

For less *cringe*, see [README_REAL.md](README_REAL.md).

---

## ⚠️ WARNING ⚠️

**!! PLEASE NOTE:** This addon is fresh outta the oven. It works on my machine™, but who knows what fresh hell awaits on yours.

*   **INTERNET REQUIRED:** On first launch, this addon will try to install `freetype-py` using `pip`. It needs an internet connection.
    *   **BUT...** if it fails, the addon won't completely die! It will enter a "Fallback Mode" where the full glyph preview and batch generation are disabled, but you can still use it to process text that you type manually into the preview object.
*   **DON'T:** Use this for a client project with a deadline of tomorrow without testing it first.
*   **DO:** Backup your project! Use Git! Save often! You get the picture.

---

## Description

Ever needed to generate a whole alphabet of 3D characters for a project? And then you realize you have to do it for every single symbol, number, and variation? And then you have to process each one? Yeah, hard pass.

This addon provides an in-editor UI for a streamlined, two-stage workflow:

1.  **Prepare & Preview:** Load any font, and the addon will generate a live, editable preview object.
2.  **Tweak & Generate:** Visually tweak your 3D text settings (size, extrusion, bevels, materials) and see the changes in real-time. When you're happy, click one button to batch-process every single character from the font into its own mesh, neatly organized into new collections.

---

## Features

I may have gone a little overboard, but I wanted '3d Spyro font' and *then* some.

*   **Two-Stage Workflow:** A non-destructive "Prepare Font" and "Generate Meshes" process that gives you full control.
*   **Live Preview:** Tweak settings in the UI and see them applied to a live text object in your viewport instantly. No more guessing games.
*   **Full Font Processing:** Iterates through *every* available glyph in a `.ttf` or `.otf` file, not just A-Z.
*   **Smart Collection Management:** Automatically creates a main collection (e.g., `[BF2M] Arial`) with `Unprocessed` and `Processed` sub-collections to keep your scene tidy.
    *   Handles naming conflicts by appending `_1`, `_2`, etc. if a collection already exists.
*   **Detailed Geometry Control:**
    *   Character Size, Extrusion, Bevel Depth, and Bevel Resolution.
*   **Transform Control:**
    *   Set a universal location and rotation for all generated meshes.
*   **Dependency Manager:** Automatically bootstraps `pip` and installs the required `freetype-py` library. Includes a fallback mode if installation fails.

---

## Installation (The Ritual - Now With More Steps!)

1.  **Get the Goods:** Head to the [Releases](https://github.com/Rakadeja/BatchFont2Mesh/releases/) page on this GitHub repo and download the latest [BatchFont2Mesh.zip](https://github.com/Rakadeja/BatchFont2Mesh/releases/download/v1.3.0-alpha/BatchFont2Mesh.zip) file.
2.  **DON'T UNZIP IT:** For real. Blender handles that part.
   
   <img width="397" height="276" alt="image" src="https://github.com/user-attachments/assets/ad7719d2-bdf4-4401-b017-82881c8bffb3" />

3.  **Open the System Console (👀 IMPORTANT!):**
    *   Before you install, go to `Window -> Toggle System Console` in Blender's top menu.
    *   Keep this console window open! It's where our addon will print its installation progress and any errors. This is your lifeline if something goes wrong.
4.  **Install in Blender:**
    *   With the console open, go to `Edit -> Preferences`.
    *   Navigate to the `Add-ons` tab.
    *   Click `Install...` at the top right.
    *   Find and select the `BatchFont2Mesh.zip` file you downloaded.
5.  **Enable the Addon & Watch the Console:**
    *   After installing, you should see "Object: BatchFont2Mesh (BF2M)" in the list.
    *   Check the little box next to its name to enable it.
    *   **Watch the System Console!** You should see messages about `pip` and `freetype-py` being installed. This is the magic happening. This step requires an internet connection and might take a moment.
6.  **If It Doesn't Work: RESTART BLENDER!**
    *   Sometimes, even after a successful install, Blender needs a swift kick to recognize the new packages. If the addon panel shows an error or seems broken, **completely close and restart Blender.** This usually fixes it.
7.  **Witness the Magic:** A new "Batch Font To Mesh" panel should now appear in the **3D Viewport's sidebar** (press `N` to open it) under the **"Tool"** tab, fully functional.

---

## How to Use (The SparkNotes Version)

The whole workflow is designed to be top-to-bottom.

### 📜 Step 1: Prepare Font

1.  **Font Input:** In the BF2M panel, select a `.ttf` or `.otf` font from your computer.
2.  **Prepare:** Smash that `Prepare Font` button.
3.  **What Happens:** The addon will load the font, count its characters, create a new collection structure, and spawn a live "Preview" text object.

### ✂️ Step 2: Live Tweak

With the "Preview" object visible, change the settings in the UI to see the results in real-time.

1.  **Adjust Geometry:** Play with the `Character Size`, `Extrude`, and `Bevel` sliders.
2.  **Set Transforms:** Dial in the final `Translation` and `Rotation` for the generated meshes.

### ✨ Step 3: Generate Meshes

Once the preview looks exactly how you want it...

1.  **Generate:** Hit the big `Generate Meshes` button at the bottom.
2.  **What Happens:** A progress bar will appear as the addon loops through every character, creating a fully processed mesh for each one and placing it in the "Processed" collection.

---

## ⚠️ Known Issues & Wack Features ⚠️

Let's be real, this is a work in progress. Here's a list of features that are in the UI but ain't quite there yet.

*   **Post-Processing Toggles:** All of the toggles in the "Post-Processing Options" section (`Mark Sharp`, `Vertex Groups`, `Multi-Material`, `Vertex Colors`) are currently UI placeholders and **do not work yet.** They are the top priority for the next development phase. (See Issue [#1](https://github.com/Rakadeja/BatchFont2Mesh/issues/1))
*   **Live Transform Preview:** The `Translation` and `Rotation` sliders don't update the live preview object in real-time. The values *are* saved and will be applied correctly when you click `Generate Meshes`, but you won't see the preview object move. (See Issue [#5](https://github.com/Rakadeja/BatchFont2Mesh/issues/5))
*   **Material Slots:** Because `Multi-Material` post-processing is not yet implemented, the `Bevel Material` slot is also not currently functional.
*   **Merge Distance UI:** The input field for `Merge Distance` is too small and truncates the default value. It still works correctly (`0.0001` is the default), it just looks weird.

---

## 🚀 Roadmap / Future Ideas 🚀

This is just the beginning. The Vibe is strong, but the Feature Creep is stronger.

*   **Implement Post-Processing:** Actually make the toggles work!
*   **Granular Character Selection:** An interface to pick and choose characters.
*   **Settings Presets:** The ability to save and load your entire configuration.
*   **Advanced UV Unwrapping:** Options to automatically run a Smart UV Project.
*   **Custom Naming Patterns:** User-definable patterns like `{font}_{char}_{ascii}`.
*   **Adaptive Bevel Scaling (The Holy Grail):** A smart algorithm to prevent small details from getting obliterated by big bevels.
*   **More Post-Processing Mayhem:** Think Decimate, Remesh, or other modifiers.
*   **Verbose Logging:** An option to output a detailed log file for debugging.

---

## Feedback / Contributing

Find a bug? Did the addon tell a bad joke? Got an idea?

*   Please open an issue on the GitHub repository. The more detail, the better.
*   Pull requests are welcome, but maybe open an issue first to chat about it.

---

## Credits

*   **Rakadeja:** The visionary and prime directive officer.
*   **Gemini 2.5 Pro:** The humble-but-rad code-monkey assistant.

---

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
