import csv
import uuid
import click

from datetime import datetime

# Note's fields or keys
keys = ['id', 'content', 'end_date', 'end_time', 'priority', 'created_datetime']


def generate_id():
    '''
    generate_id
    
    Generate note's id from UUID by get only first 8 charecters
    
    :return: note's ID
    :rtype: String
    '''

    return str(uuid.uuid4())[:8]


def adding(data):
    '''
    adding
    
    Adding note to store

    :param data: 
    :type data: Dict
    :return: Status of adding
    :rtype: Bool
    '''

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
    '''
    priority_display
    
    Displaying priority text by styling.
    
    :param priority_text: text in set {high, medium, low}
    :type priority_text: String
    '''

    text = str.lower(priority_text)
    colors = {
        'high': 'red',
        'medium': 'white',
        'low': 'black'
    }
    click.secho(f'Priority: {priority_text}', fg=colors.get(text, 'black'), bold=True)


def deadline_display(end_date, end_time):
    '''
    deadline_display
    
    Displaying deadline text by styling
    
    :param end_date: deadline date or finish date
    :type end_date: String with the format (dd-mm-yyyy)
    :param end_time: deadline time or finish time
    :type end_time: Straing with the format (hh:mm)
    :return: Status of deadline which in time or overdue
    :rtype: Bool
    '''

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
    return True


def display():
    '''
    display
    
    Main note displaying method
    
    '''

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
