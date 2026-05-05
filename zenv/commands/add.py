import subprocess
from pathlib import Path
import os
from zenv.core.utils import find_project_root


def add(package: str):
    root = find_project_root()
    if not root:
        print("Not a zenv project")
        return

    env_path = root / ".zenv/env"

    if os.name == "nt":
        pip = env_path / "Scripts/pip"
    else:
        pip = env_path / "bin/pip"

    subprocess.run([str(pip), "install", package], check=True)
