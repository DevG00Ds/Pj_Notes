import Note


def show_all_notes(txt):
    array_note = read_file()
    if txt == "all":
        print("Журнал заметок : ")
        for i in array_note:
            print(Note.Note.map_note(i))


def create_file(array, mode):
    file = open("notes.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("notes.csv", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(Note.Note.to_string(notes))
        file.write('\n')
    file.close()


def read_file():
    try:
        array = []
        file = open("notes.csv", 'r', encoding='utf-8')
        notes = file.read().strip().split('\n')
        for n in notes:
            split_n = n.split(':')
            notes = Note.Note(id=split_n[0], title=split_n[1], body=split_n[2], date=split_n[3])
            array.append(notes)
    except Exception:
        print(' Журнал заметок пустой')
    finally:
        return array


def add_notes():
    title = input("Введите загаловок заметки : ")
    body = input("Введите описание заметки : ")
    note = Note.Note(title=title, body=body)
    array_notes = read_file()
    for i in array_notes:
        if Note.Note.cr_id(note) == Note.Note.cr_id(i):
            Note.Note.wr_id(note)
    array_notes.append(note)
    create_file(array_notes, 'a')
    print("Заметка добавлена в журнал заметок !.")


def change_notes():
    id = input("Введите №ID изминяемой заметки : ")
    array_notes = read_file()
    flag = True
    array_notes_new = []
    for i in array_notes:
        if id == Note.Note.cr_id(i):
            i.title = input("Изминение заголовка заметки : ")
            i.body = input("Изминение описания заметки : ")
            Note.Note.wr_date(i)
            logic = False
        array_notes_new.append(i)
    if flag:
        create_file(array_notes, 'a')
        print("Заметка с №ID : ", id, "успешно изминена!.")
    else:
        print("Нет такого №ID заметки")


def del_notes():
    id = input("Введите ID удаляемой заметки : ")
    array_notes = read_file()
    flag = False
    for i in array_notes:
        if id == Note.Note.cr_id(i):
            array_notes.remove(i)
            flag = True
    if flag:
        create_file(array_notes, 'a')
        print("Заметка с №ID : ", id, "успешно удалена!. ")
    else:
        print("Нет такого №ID заметки")
