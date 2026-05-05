from pathlib import Path


def find_project_root():
    current = Path.cwd()

    while current != current.parent:
        if (current / ".zenv").exists():
            return current
        current = current.parent

    return None
