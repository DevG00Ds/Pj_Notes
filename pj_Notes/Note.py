from datetime import datetime
import module, counter
import uuid


class Note:
    def __init__(self, id=str(counter.counter()), title="Текст", body="Текст",
                 date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def cr_id(note):
        return note.id

    def cr_title(note):
        return note.title

    def cr_body(note):
        return note.body

    def cr_date(note):
        return note.date

    def wr_id(note):
        note.id = str(counter.counter())

    def wr_title(note):
        note.title = note

    def wr_body(note):
        note.body = note

    def wr_date(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(note):
        return note.id + ':' + note.title + ':' + note.body + ':' + note.date

    def map_note(note):
        return 'id : ' + note.id + '\n' + 'Название : ' + note.title + '\n' + 'Описание : ' + note.body + '\n' + 'Дата публикации : ' + note.date
