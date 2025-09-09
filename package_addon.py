"""
Packages a Blender addon into a distributable .zip file.

This script is designed to be placed directly inside the root of your addon
folder (e.g., inside 'BatchFont2Mesh/'). It requires no path configuration.

When run, it will:
    1. Automatically determine the addon's name from the folder it's in.
    2. Create a 'build' folder INSIDE the addon folder.
    3. Create a clean .zip file containing the entire addon, ready for installation.
    4. Exclude common development files and itself from the package.

This script was corrected (again) with the assistance of Gemini 2.5 Pro.
"""

import os
import zipfile

# ==== Configuration ====

# A set of folder and file names to ALWAYS exclude from the package.
# This is case-sensitive.
EXCLUDE = {
    ".git",
    ".vscode",
    "__pycache__",
    ".DS_Store",
    "package_addon.py",
    ".editorconfig",
    ".gitignore",
    "BatchFont2Mesh.code-workspace",
    "bf2m_addon.py",
}


def zip_addon():
    """
    Finds all addon files and packages them into a distributable archive.
    """
    # ==== 1. Determine Paths Automatically ====
    # The source directory is the folder this script is located in.
    source_dir = os.path.dirname(os.path.abspath(__file__))
    addon_name = os.path.basename(source_dir)

    # The output 'build' folder will be created INSIDE this script's directory.
    output_dir = os.path.join(source_dir, "build")

    output_zip_file = f"{addon_name}.zip"
    output_path = os.path.join(output_dir, output_zip_file)

    # ==== 2. Create Output Directory ====
    os.makedirs(output_dir, exist_ok=True)

    print(f"Packaging addon '{addon_name}'...")
    print(f"Source: '{source_dir}'")
    print(f"Output: '{output_path}'")

    files_to_archive = []

    # ==== 3. Walk the Addon Folder and Collect Files ====
    for root, dirs, files in os.walk(source_dir):
        # Prune excluded directories so we don't even walk them.
        dirs[:] = [d for d in dirs if d not in EXCLUDE]

        for file in files:
            if file in EXCLUDE or file.endswith(".zip"):
                continue

            file_path = os.path.join(root, file)

            # The path inside the zip must be relative to the addon's source folder,
            # and then nested under a root folder with the addon's name.
            relative_path = os.path.relpath(file_path, source_dir)
            archive_name = os.path.join(addon_name, relative_path)

            files_to_archive.append((file_path, archive_name))

    # ==== 4. Create the Zip Archive ====
    if not files_to_archive:
        print("\nWarning: No files found to package. No archive created.")
        return

    try:
        with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zf:
            for file_path, archive_name in sorted(files_to_archive):
                print(f"  Adding: {archive_name}")
                zf.write(file_path, archive_name)

        print(
            f"\nSuccessfully created addon package with {len(files_to_archive)} file(s)."
        )

    except Exception as e:
        print(f"\nAn error occurred during archiving: {e}")


if __name__ == "__main__":
    zip_addon()
