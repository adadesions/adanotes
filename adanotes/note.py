import csv
import uuid
import click
import adanotes

from datetime import datetime

'''
Development Task
2. Show note by deadline
'''


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


def get_notes():
    '''
    get_notes
    
    Getting notes from store
    
    :return: All notes from store in this version is .csv file
    :rtype: List
    '''

    with open(adanotes.store_uri, newline='') as file:
        note_reader = csv.DictReader(file)
        store = [row for row in note_reader]

        return store


def write_note(store, data={}):
    '''
    write_note
    
    Writing a new row of note to store
    
    :param data: new note data from user
    :type data: Dict
    :param store: all notes data read from storage
    :type store: List
    :return: Writing status
    :rtype: Bool
    '''

    with open(adanotes.store_uri, 'w', newline='') as file:
            note_writer = csv.DictWriter(file, fieldnames=keys)

            if data:
                store.append(data)

            note_writer.writeheader()
            note_writer.writerows(store)
            return True

    return False


def adding(data):
    '''
    adding
    
    Adding note to store

    :param data: 
    :type data: Dict
    :return: Status of adding
    :rtype: Bool
    '''

    store = get_notes()
    data_keys = [key for key in data]
    data['id'] = generate_id()

    if data_keys == keys:
        return write_note(store, data)
    
    return False


def deleting(id_):
    is_found = False
    store = get_notes()
    for i, note in enumerate(store):
        if note['id'] == id_:
            del store[i]
            is_found = True
            break

    if is_found:
        write_note(store)
        click.secho(f'Deleting note id: {id_} ', fg='red', nl=False)
        click.secho(f'COMPLETED', fg='white', bg='green')

        return True


    click.secho(f'Deleting note id: {id_} ', fg='red', nl=False)
    click.secho(f'NOT FOUND', fg='white', bg='red')


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

        if cur < end:
            break
        elif cur == end:
            continue
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
    store = get_notes()
    for row in store:
        click.secho(f'ID: {row["id"]}', fg='yellow', bg='blue', bold=True)
        priority_display(row['priority'])
        click.secho(f'Note: {row["content"]}', fg='yellow')
        click.secho(f'Start: {row["created_datetime"]}', fg='magenta')
        deadline_display(row['end_date'], row['end_time'])

        print(f'{"-"*92}\n')
