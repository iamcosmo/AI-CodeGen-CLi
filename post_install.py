import os
import sys
import site
import subprocess

# Get the Scripts path where the executable is installed
scripts_path = site.USER_BASE + r"\Python" + sys.version[:3] + r"\Scripts"

# Get current PATH
current_path = os.environ.get("PATH", "")

if scripts_path not in current_path:
    print(f"Adding {scripts_path} to PATH...")

    # Update PATH for the current session
    os.environ["PATH"] += os.pathsep + scripts_path

    # Add it permanently to the user's environment variables
    subprocess.run(
        f'setx PATH "{current_path};{scripts_path}"',
        shell=True,
        check=False
    )

    print(f"\n[INFO] Successfully added {scripts_path} to PATH!")
else:
    print(f"\n[INFO] {scripts_path} is already in PATH.")
