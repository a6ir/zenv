from typing import List
import typer

from zenv.core.runner import run_in_env
from zenv.core.utils import find_project_root


def run(cmd: List[str] = typer.Argument(..., help="Command to run inside the env")):
    """
    Run any command inside the project environment.
    Use `--` to pass flags (e.g., -c) to the underlying command.
    """
    root = find_project_root()
    if not root:
        typer.echo("Not a zenv project. Run: zenv init")
        raise typer.Exit(code=1)

    env_path = root / ".zenv/env"

    if not env_path.exists():
        typer.echo("Env not found. Run: zenv env create")
        raise typer.Exit(code=1)

    run_in_env(env_path, cmd)
