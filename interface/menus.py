import switch
import show_notes as shn

def main_menu(my_list_notes=None):

    if my_list_notes is None:
        my_list_notes=[]

    while True:
        print('''

Меню действий:

1. Создать новую заметку

2. Показать все заметки

3. Обновить заметку

4. Удалить заметку

5. Найти заметки

6. Выйти из программы

''')

        my_list_notes = switch.distrib_func(
        input('Ваш выбор: '), my_list_notes
        )

        continue


def context_menu(my_list_notes):
    while True:

        choice = input(
            '\nIf you want to delete some notes '
            'press (D)el, to Add new press (A)dd'
            '\nFor exit to main menu press X...').lower()

        if choice in ['del', 'd']:
            del_str = input(
                '\nEnter username or title of the note '
                'you want to delete...'
            )
            my_list_notes = f_del_note(
                my_list_notes, srch_str=del_str)
            shn.f_print_all(my_list_notes)
            continue

        elif choice in ['add', 'a']:
            my_list_notes.append(
                f_add_new_note(my_list_notes))
            shn.f_print_all(my_list_notes)
            continue

        elif choice in ['x', 'exit']:

            return my_list_notes

        else:
            print('\nUnknown command, try more time...')
            continue
#   ******************** end of context menu *************