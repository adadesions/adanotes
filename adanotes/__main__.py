from datetime import datetime
import click

from adanotes import note


@click.group()
def adanote():
    pass


@adanote.command()
@click.option('--content', prompt='Taking note')
@click.option('--end_date', prompt='End Date(DD-MM-YYYY)')
@click.option('--end_time', prompt='End Time(HH:MM)')
def add_note(content, end_date, end_time):
    now = datetime.now()
    data = {
        'content': content,
        'end_date': end_date,
        'end_time': end_time,
        'created_datetime': now.strftime("%d-%m-%Y %H:%M")
    }
    note.adding(data)


@adanote.command()
def show_note():
    note.display()

if __name__ == '__main__':
    adanote()