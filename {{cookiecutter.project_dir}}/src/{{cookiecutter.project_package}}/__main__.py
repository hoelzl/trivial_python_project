{% if cookiecutter.cli == "click" %}
import click


def say_hi(name="world"):
    click.echo(f"Hello, {name}!")


@click.command()
@click.option("--name", help="The name of the person to greet.", default="world")
def main(name):
    say_hi(name)


if __name__ == "__main__":
    main()

{% elif cookiecutter.cli == "argparse" %}

import argparse


def say_hi(name="world"):
    print(f"Hello, {name}!")


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

{% else %}

def say_hi():
    print(f"Hello, world!")


if __name__ == "__main__":
    say_hi()

{% endif %}
