# BATCHFONT2MESH (BF2M) - QUICKSTART INSTRUCTIONS

Yo, what's the dealio? So you got the addon and you're ready to rock.
This file is the 411, the TL;DR, the SparkNotes. Let's get it.

`(⌐■_■) <- Gemini was here`

---

## THE RITUAL (INSTALLATION)

1. **GET THE ZIP:** Grab the `BatchFont2Mesh.zip` from the GitHub Releases page.
2. **DON'T UNZIP IT:** For real. Blender likes its zips whole.
3. **PEEP THE CONSOLE (SUPER IMPORTANT!):**
    - Before you do anything else, go to `Window -> Toggle System Console`.
    - Keep this window open. It's where the addon will spill the tea on its installation progress. No cap.
4. **INSTALL IN BLENDER:**
    - Fire up Blender.
    - Go to `Edit -> Preferences -> Add-ons`.
    - Click that "Install..." button at the top.
    - Find the `BatchFont2Mesh.zip` file and select it.
5. **ENABLE IT & WATCH THE CONSOLE:**
    - You'll see "Object: BatchFont2Mesh (BF2M)" in the list.
    - Check the box next to it.
    - **!! IMPORTANT !!** Watch the System Console! It's gonna download a dependency (`freetype-py`) which needs internet. Give it a sec to cook.
6. **IF IT'S BUSTED: RESTART BLENDER!**
    - Sometimes Blender is a little dense and needs a restart to see the new stuff. If the addon panel looks broken or is throwing errors after installing, just close Blender completely and open it again. It's the magic fix.
7. **FIND IT:** If all went well, the panel is now in your 3D View.
    - Press 'N' to open the sidebar.
    - Click the "Tool" tab.
    - Scroll down until you see "Batch Font To Mesh". You're in.

---

## HOW TO USE IT (THE WORKFLOW)

The whole thing is a 3-step process. Easy peasy.

### STEP 1: PREPARE FONT

1. **FONT INPUT:** Click the folder icon and pick a `.ttf` or `.otf` font file.
2. **PREPARE:** Smash the "Prepare Font" button.
3. **THE MAGIC:** The addon loads the font, creates a collection set for you (like `[BF2M] Arial`), and spawns a live "Preview" text object in the viewport. The rest of the UI will now unlock.

### STEP 2: LIVE TWEAK

This is where you get all artsy. Look at the "Preview" object and mess with the settings in the panel.

- **MATERIALS:** Assign your base and (optional) bevel materials.
- **GEOMETRY:** Tweak the Size, Extrude, and Bevel sliders. See it change live!
- **TRANSFORMS:** Set the final Location and Rotation for all generated meshes.
- **POST-PROCESSING:** This is the fun part. Toggle on any combination of the bevel modes you want:
  - Mark Sharp: For crisp edges.
  - Vertex Groups: For masking/modifiers.
  - Multi-Material: To use that second material on the bevels.
  - Vertex Colors: To isolate bevels for shaders.

### STEP 3: GENERATE MESHES

When your preview looks like a certified banger...

1. **GENERATE:** Hit the big "Generate Meshes" button.
2. **THE PAYOFF:** A progress bar will appear. The addon will now loop through EVERY character in the font, creating a mesh for each one with all your settings applied. They all get chucked into the "Processed" sub-collection.

When it's done, the preview object deletes itself and the UI resets, ready for another round.
