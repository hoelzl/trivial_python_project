import click


def say_hi(name="world"):
    print(f"Hello, {name}!")


@click.command()
@click.option("--name", help="The name of the person to greet.", default="world")
def main(name):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    main()
