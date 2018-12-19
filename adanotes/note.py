import csv
import uuid
import click

from datetime import datetime

keys = ['id', 'content', 'end_date', 'end_time', 'priority', 'created_datetime']


def generate_id():
    return str(uuid.uuid4())[:8]


def adding(data):
    stores = []
    data_keys = [key for key in data]
    
    with open('data/store.csv', newline='') as file:
        note_reader = csv.DictReader(file)
        stores = [row for row in note_reader]

    if data_keys == keys:
        with open('data/store.csv', 'w', newline='') as file:
            data['id'] = generate_id()
            note_writer = csv.DictWriter(file, fieldnames=keys)
            stores.append(data)

            note_writer.writeheader()
            note_writer.writerows(stores)

        return True
    
    return False


def priority_display(priority_text):
    text = str.lower(priority_text)
    colors = {
        'high': 'red',
        'medium': 'white',
        'low': 'black'
    }
    click.secho(f'Priority: {priority_text}', fg=colors.get(text, 'black'), bold=True)


def deadline_display(end_date, end_time):
    now = datetime.now().strftime('%Y-%m-%d-%H-%M')
    cur_datetime = now.split('-')

    end_datetime = end_date.split('-')[::-1]+end_time.split(':')
    for i, end in enumerate(end_datetime):
        end = int(end)
        cur = int(cur_datetime[i])
        if cur <= end:
            # End year greater than current year
            if i == 0 and cur < end:
                break

            # End hours greater than current hours, no need to check minutes
            if i == 3 and cur < end:
                break
        else:
            click.secho('Deadline:', fg='white', nl=False )
            click.secho(f'{end_date} {end_time}', fg='white', bg='red')
            return False

    click.secho('Deadline:', fg='white', nl=False )
    click.secho(f'{end_date} {end_time}', fg='white', bg='green')

def display():
    # TODO: Display sorted by deadline
    click.secho('AdaNotes showing your meaningful', fg='green', bold=True)
    print()
    with open('data/store.csv', newline='') as file:
        note_reader = csv.DictReader(file)
        for row in note_reader:
            click.secho(f'ID: {row["id"]}', fg='yellow', bg='blue', bold=True)
            priority_display(row['priority'])
            click.secho(f'Note: {row["content"]}', fg='yellow')
            click.secho(f'Start: {row["created_datetime"]}', fg='magenta')
            
            deadline_display(row['end_date'], row['end_time'])
            
            print(
                f'{"-"*92}\n'
            )
