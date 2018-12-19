from datetime import datetime
from adanotes import note

now = datetime.now().strftime('%d-%m-%Y %H:%M')
data = {
    'content': 'Write a website for AdaBrain',
    'end_date': '01-01-2019',
    'end_time': '02:20',
    'created_datetime': now
}


def test_adding_note():
    status = note.adding(data)
    assert status == True