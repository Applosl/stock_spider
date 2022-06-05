import click


@click.group()
def main():
    pass


@main.command()
def start():
    click.echo('start')


@main.command()
def tasks():
    click.echo('tasks')


if __name__ == '__main__':
    main()
