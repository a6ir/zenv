import json
from pathlib import Path


def load_config(root: Path):
    config_file = root / ".zenv/config.json"
    if not config_file.exists():
        return {}

    with open(config_file) as f:
        return json.load(f)
