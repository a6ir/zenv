from pathlib import Path
from zenv.core.env import create_env
from zenv.core.python import get_python
from zenv.core.utils import find_project_root


def create():
    root = find_project_root()
    if not root:
        print("Not a zenv project. Run: zenv init")
        return

    env_path = root / ".zenv/env"

    python = get_python("system")

    create_env(env_path, python)

    print("Environment created")
