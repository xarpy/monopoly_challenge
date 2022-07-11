# import os
from pathlib import Path

import click

from app import execute

# import pytest
# from IPython import embed


BASE_DIR = Path(__file__).resolve().parent


@click.group()
def cli():
    pass


@click.command("run", short_help="Command to execute application")
def compile_command():
    click.echo(execute())


# @click.command("runtest", short_help="Command to execute tests")
# @click.option(
#     "--list",
#     is_flag=True,
#     default=False,
#     help="Obtain module tests list",
# )
# @click.option(
#     "--node",
#     "-n",
#     help="Inform the module name and the function you want to run the tests",
# )
# def test_command(list, node):
#     folder_path = os.path.join(BASE_DIR, "tests")
#     if not os.path.exists(folder_path):
#         print("There is no folder named tests anywhere!")
#     if list:
#         pytest.main(["--co"])
#     if node:
#         pytest.main(["-v", f"{folder_path}/{node}"])
#     else:
#         pytest.main(["-vv", "--cov=."])


# @click.command("shell", short_help="Command to execute ipython shell")
# def shell_command():
#     embed(colors="neutral")


cli.add_command(compile_command)
# cli.add_command(shell_command)
# cli.add_command(test_command)

if __name__ == "__main__":
    cli()
