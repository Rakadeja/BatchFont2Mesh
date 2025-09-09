# BATCHFONT2MESH (BF2M) - THE ROADMAP

This is the "wouldn't it be cool if..." list. The place where dreams and feature creep hang out. Text is underrated, and we've only just begun.

## THE HIT LIST (PLANNED & DREAM FEATURES)

---

### CORE WORKFLOW & UI

- **GRANULAR CHARACTER SELECTION:**
    Instead of all-or-nothing, a real UI to pick and choose characters. Think custom ranges (e.g., A-Z, 0-9), preset checkboxes for "Punctuation" or "Math Symbols", or even pasting in a string to generate only what you need.
- **SETTINGS PRESETS:**
    The ability to save and load your entire configuration. Dial in the perfect chiseled look for "GothicStone" and the perfect soft look for "BubbleFont" and swap between them instantly.
- **GRID LAYOUT GENERATION:**
    An option to automatically arrange all generated meshes in a grid, like a character sheet. Perfect for viewing your whole set or baking to a texture atlas.
- **SVG & CURVE OBJECT SUPPORT:**
    Expand the addon to accept SVG files or Blender Curve objects as input. Imagine yeeting any vector art into the system and applying the same extrude, bevel, and post-processing magic to it.

---

### GEOMETRY & POST-PROCESSING

- **ADAPTIVE BEVEL SCALING (THE HOLY GRAIL):**
    A smart algorithm to prevent small details (like the dot on an 'i' or the inside of an 'o') from getting obliterated or clipping when using large bevel depths. This would be a massive level-up in quality.
- **ADVANCED UV UNWRAPPING:**
    Options to automatically run a Smart UV Project, control island margins, or even mark seams on the bevels before unwrapping for more control.
- **MORE POST-PROCESSING MAYHEM:**
    Go beyond the basics. Think Decimate, Remesh, or applying other modifiers (like a Weld to fuse overlapping characters) automatically after generation. Maybe even a simple Geometry Nodes setup on each character.

---

### QUALITY OF LIFE & ROBUSTNESS

- **CUSTOM NAMING PATTERNS:**
    Go beyond the default `FontName_A` with user-definable patterns like `{font}_{char}_{ascii_code}` for maximum organization.
- **AUTOMATIC MATERIAL SETUP:**
    A checkbox that, if using the Vertex Colors mode, will auto-create a basic material for you that pipes the vertex color attribute directly into the Base Color of a Principled BSDF. Saves a ton of clicks.
- **VERBOSE LOGGING:**
    An option to output a detailed log of the entire generation process into a timestamped file (`batchfont2mesh_UTCtimestamp.log`) for serious debugging.
- **FREETYPE-LESS FALLBACK MODE:**
    A "basic" mode that can run without `freetype-py`. It wouldn't know the character count and would require the user to type in the characters they want, but it would improve accessibility for offline/restricted environments.

---

### BIG BRAIN FUTURE STUFF

- **PERFORMANCE OPTIMIZATIONS:**
    For fonts with thousands of characters, a "Fast Mode" that might skip some of the heavier post-processing for quicker drafts.
- **GEOMETRY INSTANCING SUPPORT:**
    An option to generate a single mesh for each character and then create a set of lightweight instances, which would be way more performant for huge scenes or game exports.
