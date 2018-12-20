import click

from datetime import datetime
from pyfiglet import figlet_format

import adanotes
from adanotes import note


@click.group()
def adanote():
    '''
    Welcome to AdaNotes
    CLI Application for taking meaningful note.

    '''
    click.secho(figlet_format('...Ada', font='speed'), fg='red')
    click.secho(figlet_format('...Notes++', font='speed'), fg='yellow')
    click.secho(f'Author: {adanotes.__author__}', fg='cyan')
    click.secho(f'Version: {adanotes.__version__}', fg='cyan')
    pass


@adanote.command()
@click.option('--content', prompt='Taking note')
@click.option('--end_date', prompt='End Date(DD-MM-YYYY)')
@click.option('--end_time', prompt='End Time(HH:MM)')
@click.option('--priority', prompt='Priority')
def add_note(content, end_date, end_time, priority):
    now = datetime.now()
    data = {
        'id': '',
        'content': content,
        'end_date': end_date,
        'end_time': end_time,
        'priority': priority,
        'created_datetime': now.strftime("%d-%m-%Y %H:%M")
    }
    note.adding(data)


@adanote.command()
def show_note():
    note.display()

if __name__ == '__main__':
    adanote()