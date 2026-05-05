import typer

from zenv.commands.init import init
from zenv.commands.use import use
from zenv.commands.env import create as env_create
from zenv.commands.add import add
from zenv.commands.run import run
from zenv.commands.list import list_items

app = typer.Typer()

# top-level commands
app.command()(init)
app.command()(use)
app.command()(add)
app.command()(run)
app.command()(list_items)

# 👇 env group
env_app = typer.Typer()
env_app.command("create")(env_create)

app.add_typer(env_app, name="env")


def main():
    app()


if __name__ == "__main__":
    main()
