from .functions import say_hi
from . import __version__

{% if cookiecutter.cli == "typer" +%}
import typer
from typing_extensions import Annotated


def version_callback(value: bool):
    if value:
        print(f"Awesome CLI Version: {__version__}")
        raise typer.Exit()


def main(name: Annotated[str, typer.Option(help="The name of the person to greet.")] = "world",
         version: Annotated[
             bool | None, typer.Option(help="Show the version and exit.", callback=version_callback)] = None, ):
    say_hi(name)


if __name__ == "__main__":
    typer.run(main)

{% elif cookiecutter.cli == "click" +%}
import click


@click.command()
@click.option("--name", help="The name of the person to greet.", default="world")
@click.version_option(version=__version__)
def main(name):
    say_hi(name)


if __name__ == "__main__":
    main()

{% elif cookiecutter.cli == "argparse" +%}
import argparse


def main():
    parser = argparse.ArgumentParser(prog="{{cookiecutter.project_package.replace('_', '-')}}",
                                     description="{{cookiecutter.description}}",
                                     epilog="Have fun!", )
    parser.add_argument("-n", "--name", default="world",
                        help="the name of the person to greet")
    args = parser.parse_args()
    say_hi(args.name)


if __name__ == "__main__":
    main()

{% else +%}

if __name__ == "__main__":
    say_hi()
{% endif +%}
