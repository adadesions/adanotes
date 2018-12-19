import click


@click.group()
def adanote():
    pass


@adanote.command()
@click.option('--note', prompt='your note:')
def add_note(note):
    click.echo(note)


if __name__ == '__main__':
    adanote()