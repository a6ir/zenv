import subprocess
from pathlib import Path


def create_env(env_path: Path, python_path: str):
    subprocess.run(
        [python_path, "-m", "venv", str(env_path)],
        check=True
    )
