import csv 
import click

keys = ['content', 'end_date', 'end_time', 'created_datetime']


def adding(data):
    # TODO: add id to a note
    stores = []
    data_keys = [key for key in data]
    
    with open('data/store.csv', newline='') as file:
        note_reader = csv.DictReader(file)
        stores = [row for row in note_reader]

    if data_keys == keys:
        with open('data/store.csv', 'w', newline='') as file:

            note_writer = csv.DictWriter(file, fieldnames=keys)
            stores.append(data)

            note_writer.writeheader()
            note_writer.writerows(stores)

        return True
    
    return False

def display():
    # TODO: Display sorted by deadline
    click.secho('AdaNotes showing your meaningful', fg='green', bold=True)
    print()
    with open('data/store.csv', newline='') as file:
        note_reader = csv.DictReader(file)
        for row in note_reader:
            click.secho(f'Note: {row["content"]}', fg='yellow')
            click.secho(f'Start: {row["created_datetime"]}', fg='magenta')
            click.secho('Deadline:', fg='green', nl=False )
            click.secho(f'{row["end_date"]}', fg='green', bg='black', nl=False)
            click.secho(f'  {row["end_time"]}', fg='green', bg='black')
            
            # {row["end_time"]}')
            print(
                f'{"-"*92}\n'
            )
