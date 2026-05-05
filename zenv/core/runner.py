import subprocess
import os
from pathlib import Path


def run_in_env(env_path: Path, cmd: list[str]):
    env = os.environ.copy()

    if os.name == "nt":
        python_bin = env_path / "Scripts/python.exe"
        bin_path = env_path / "Scripts"
    else:
        python_bin = env_path / "bin/python"
        bin_path = env_path / "bin"

    env["PATH"] = str(bin_path) + os.pathsep + env["PATH"]
    env["VIRTUAL_ENV"] = str(env_path)

    # 🔥 IMPORTANT: force using correct python
    if cmd and cmd[0] == "python":
        cmd[0] = str(python_bin)

    subprocess.run(cmd, env=env)
