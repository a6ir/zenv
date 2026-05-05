import json
from pathlib import Path


def init():
    root = Path.cwd()
    zenv_dir = root / ".zenv"

    zenv_dir.mkdir(exist_ok=True)

    config = {
        "python": "system",
        "env": ".zenv/env"
    }

    with open(zenv_dir / "config.json", "w") as f:
        json.dump(config, f, indent=2)

    print("Initialized zenv project")
