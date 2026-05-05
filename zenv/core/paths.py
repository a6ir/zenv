from pathlib import Path

HOME = Path.home()
ZENV_ROOT = HOME / ".zenv"

PYTHON_DIR = ZENV_ROOT / "pythons"
ENV_DIR = ZENV_ROOT / "envs"
CACHE_DIR = ZENV_ROOT / "cache"

def ensure_dirs():
    for p in [PYTHON_DIR, ENV_DIR, CACHE_DIR]:
        p.mkdir(parents=True, exist_ok=True)
