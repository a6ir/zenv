import shutil


def get_python(version: str):
    if version == "system":
        python = shutil.which("python")
        if not python:
            raise Exception("System Python not found")
        return python

    raise Exception(f"Python version {version} not supported yet")
