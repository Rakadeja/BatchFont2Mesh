# dependencies.py
import sys
import subprocess
import os
import importlib

# The name of the package on PyPI (for pip) and the name of the module (for import)
PACKAGE_NAME = "freetype-py"
MODULE_NAME = "freetype"

def get_blender_site_packages():
    """
    Returns the site-packages directory for Blender's Python environment.
    This is the most reliable place to install and check for packages.
    """
    py_exec = sys.executable
    # This path construction is robust for standard Blender installations.
    return os.path.join(os.path.dirname(py_exec), "lib", "site-packages")

def ensure_pip():
    """
    Ensures that pip is available in Blender's Python environment.
    
    If pip is not found, it attempts to install it using the bundled `ensurepip`
    module. This is the standard, recommended way to bootstrap pip.
    """
    site_packages = get_blender_site_packages()
    
    try:
        import pip
        print("BF2M Log: pip is already available.")
        return True
    except ImportError:
        print("BF2M Log: pip not found. Attempting to install it.")
        
        try:
            import ensurepip
            # This installs pip into the correct site-packages directory.
            ensurepip.bootstrap()
            
            # We must clear importlib's caches for it to find the new module
            importlib.invalidate_caches()
            
            print("BF2M Log: pip installed successfully.")
            return True
        except Exception as e:
            print(f"BF2M CRITICAL: Failed to bootstrap pip! Error: {e}")
            print("BF2M CRITICAL: Addon will not be able to install dependencies.")
            return False

def install_dependencies():
    """
    Installs all required packages for the addon.
    
    First, it ensures pip is available. Then, it checks if the required package
    is already installed. If not, it uses pip to install it.
    """
    if not ensure_pip():
        # If pip itself can't be installed, we can't proceed.
        return

    site_packages = get_blender_site_packages()
    
    # We add our target directory to the path to ensure Python can find it.
    if site_packages not in sys.path:
        sys.path.append(site_packages)

    # Check if the module can be imported.
    try:
        importlib.import_module(MODULE_NAME)
        print(f"BF2M Log: '{MODULE_NAME}' is already installed and available.")
        return
    except ImportError:
        print(f"BF2M Log: '{PACKAGE_NAME}' is not installed. Attempting to install with pip...")
        
        try:
            # We now use the guaranteed-to-exist pip module via subprocess.
            # This is the most reliable way to call pip from a script.
            subprocess.check_call([sys.executable, "-m", "pip", "install", PACKAGE_NAME])
            
            importlib.invalidate_caches() # Clear caches again
            
            print(f"BF2M Log: '{PACKAGE_NAME}' installed successfully.")

        except subprocess.CalledProcessError as e:
            print(f"BF2M CRITICAL: FAILED to install '{PACKAGE_NAME}' with pip. Error: {e}")
            # Re-raise the exception to let the __init__.py know it failed.
            raise e

def are_dependencies_installed():
    """
    A final, simple check to see if the dependency is met.
    """
    try:
        importlib.import_module(MODULE_NAME)
        return True
    except ImportError:
        return False
