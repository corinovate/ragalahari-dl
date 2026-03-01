"""
Build script for ragalahari-dl executable.
Creates a standalone .exe using PyInstaller.

Usage:
    pip install pyinstaller
    python build.py

Output:
    dist/ragalahari-dl/ragalahari-dl.exe
"""

import subprocess
import sys
import os
import shutil

def build():
    print("=" * 50)
    print("  Building ragalahari-dl.exe")
    print("=" * 50)

    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print(f"  PyInstaller version: {PyInstaller.__version__}")
    except ImportError:
        print("  PyInstaller not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

    # Clean previous builds
    for folder in ["build", "dist"]:
        if os.path.exists(folder):
            print(f"  Cleaning {folder}/...")
            shutil.rmtree(folder)

    spec_file = "ragalahari_dl.spec"
    if os.path.exists(spec_file):
        os.remove(spec_file)

    # Check for icon file
    icon_path = os.path.join("docs", "favicon.ico")
    has_icon = os.path.exists(icon_path)
    if has_icon:
        print(f"  Icon found: {icon_path}")
    else:
        print("  No icon file found, building without icon")

    # Build the exe
    print("\n  Compiling with PyInstaller...\n")
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--name", "ragalahari-dl",
        "--onefile",
        "--console",
        "--clean",
        "--noconfirm",
    ]
    if has_icon:
        cmd.extend(["--icon", icon_path])
    cmd.append("ragalahari_dl.py")
    subprocess.check_call(cmd)

    # Check output
    exe_name = "ragalahari-dl.exe" if sys.platform == "win32" else "ragalahari-dl"
    exe_path = os.path.join("dist", exe_name)

    if os.path.exists(exe_path):
        size_mb = os.path.getsize(exe_path) / (1024 * 1024)
        print("\n" + "=" * 50)
        print(f"  Build successful!")
        print(f"  Output: {exe_path}")
        print(f"  Size:   {size_mb:.1f} MB")
        print("=" * 50)
        print(f"\n  Run it:  .\\dist\\{exe_name}")
    else:
        print("\n  Build failed! Check the output above for errors.")
        sys.exit(1)


if __name__ == "__main__":
    build()
