from pathlib import Path


def list_items():
    root = Path.home() / ".zenv"

    if not root.exists():
        print("No environments yet")
        return

    print("Global zenv directory:", root)
