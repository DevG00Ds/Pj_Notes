import module, View


def start():
    View.hello()
    while True:
        View.menu()
        text = input('Сделайте выш выбор : ')
        if text == '1':
            module.show_all_notes("all")
        elif text == '2':
            module.show_all_notes("ID")
        elif text == '3':
            module.show_all_notes("data")
        elif text == '4':
            module.add_notes()
        elif text == '5':
            module.show_all_notes("all")
            module.change_notes()
        elif text == '6':
            module.show_all_notes("all")
            module.del_notes()
        elif text == '7':
            print('\n Приложение заметки закрывается.'
                  '\n Всего хорошего')
            break
        else:
            View.error_choice()
            break
