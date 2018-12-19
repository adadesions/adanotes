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
    print('Welcome to AdaNotes!')
    print('='*100)
    print()
    with open('data/store.csv', newline='') as file:
        note_reader = csv.DictReader(file)
        for row in note_reader:
            print(
                f'Note: {row["content"]}\n'
                f'Start: {row["created_datetime"]}\n'
                f'Deadline: {row["end_date"]} {row["end_time"]}\n'
                f'{"="*100}\n'
            )
