import click
from config import VERSION, APP_NAME


@click.group()
def main():
    pass


@main.command()
def start():
    click.echo('start')


@main.command()
def tasks():
    click.echo('tasks')


@main.command()
def info():
    click.echo("App: {}\nVersion: {}".format(APP_NAME, VERSION))


if __name__ == '__main__':
    main()
