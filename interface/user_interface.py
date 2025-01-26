import sys
import data
import data as d
import interface as iface
import utils
import SQLite_DB.database as db


def main_menu():
    while True:
        print('''

*** Меню управления заметками ***:

1. Создать новую заметку

2. Показать все заметки

3. Обновить заметку

4. Удалить заметку

5. Найти 

6. Показать напоминания

7. Выйти из программы

''')

        my_list_notes = (
            iface.distrib_func(input('Ваш выбор: '))
        )

        continue


def distrib_func(my_choice):
    # show all
    if my_choice == '2':
        iface.f_print_all(db.load_notes_from_db())
        context_menu()

    # create new
    if my_choice == '1':
        print('\nНачало новой заметки')
        db.save_note_to_db(d.f_add_new_note())

    # update
    if my_choice == '3':
        my_list_notes = db.load_notes_from_db()
        iface.f_print_all(my_list_notes)

        print('\n[F] Фильр заметок | '
              '[Enter] Продолжить без фильтра')

        if input('Ваш выбор: ').lower() == 'f':
            list_for_update = filter_notes(my_list_notes)

        else:
            list_for_update = my_list_notes.copy()

        iface.f_print_all(list_for_update)

        if (note_update := get_only_note(list_for_update, 'обновить')) is not None:
            d.f_update_note(note_update)
            db.update_note_in_db(note_update.get('id'), note_update)

    # delete
    if my_choice == '4':
        my_list_notes = db.load_notes_from_db()
        iface.f_print_all(my_list_notes)
        print('\n[F] Фильр заметок | '
              '[Enter] Продолжить без фильтра')

        if input('Ваш выбор: ').lower() == 'f':
            list_for_delete = filter_notes(my_list_notes)

        else:
            list_for_delete = my_list_notes.copy()

        iface.f_print_all(list_for_delete)

        if (note_for_delete := get_only_note(list_for_delete, 'удалить')) is not None:
            db.delete_note_from_db(note_for_delete.get('id'))

        iface.f_print_all(db.load_notes_from_db())

    # search
    if my_choice == '5':
        my_list_notes = db.load_notes_from_db()
        found_list_notes = filter_notes(my_list_notes)

        if found_list_notes:
            iface.f_print_all(found_list_notes)
            context_menu(found_list_notes)
        else:
            utils.handle_error('empty_list')

    if my_choice == '7':
        sys.exit(0)

    if my_choice == '6':
        reminder_notes = utils.check_reminders()
        context_menu(reminder_notes)


# ****************** end distrib func *****************

# ****************** context menu ******************
def context_menu(my_list_notes: list = None):
    if not my_list_notes:
        my_list_notes = db.load_notes_from_db()

    while True:
        try:
            print('\n[D] Удаление | [E] Правка | [N] Новая | [X] Назад')
            choice = input(
                'Ваш выбор: '
            ).strip().lower()

            if choice in ['del', 'd']:
                if (my_note := get_only_note(my_list_notes, 'удалить')) is not None:
                    db.delete_note_from_db(my_note.get('id'))
                    my_list_notes.remove(my_note)
                    iface.f_print_all(my_list_notes)
                    continue

            elif choice in ['new', 'n']:
                my_note = data.f_add_new_note()
                db.save_note_to_db(my_note)
                my_list_notes.append(my_note)
                iface.f_print_all(my_list_notes)
                continue

            elif choice == 'e':
                if (note_update := get_only_note(my_list_notes, 'обновить')) is not None:
                    my_list_notes.remove(note_update)
                    d.f_update_note(note_update)
                    db.update_note_in_db(note_update.get('id'), note_update)
                    my_list_notes.append(note_update)
                    iface.f_print_all(my_list_notes)
                    continue

            elif choice in ['x', 'exit']:

                return

            else:
                raise ValueError

        except ValueError:
            utils.handle_error('invalid_input')


#   ******************** end of context menu *************

# save change dialog
def save_chg_cloud(my_list_note):
    while True:
        try:

            ans = input('Хотите сохранить изменения'
                        '---(y/n)... ').lower()

            if ans.lower() in ['y', 'yes']:
                d.save_to_json_git(my_list_note)
                return True

            elif ans in ['n', 'no']:
                return False

            else:
                raise ValueError
        except ValueError:
            utils.handle_error('invalid_input')


# ******************* end of save_chd_cloud *************

def f_empty_list():
    my_list_notes: list = []
    print('Сохраненные заметки не найдены...')
    while True:
        try:
            print('\n[N] Добавить новую заметку | [X] Выход')
            ans = input(
                'Ваш выбор: '
            ).strip().lower()

            if ans.lower() in ['n', 'add']:
                db.save_note_to_db(d.f_add_new_note())
                iface.f_print_all(db.load_notes_from_db())

            elif ans.lower() in ['x', 'exit']:

                iface.main_menu()

            else:
                raise ValueError

        except ValueError:
            utils.handle_error('invalid_input')


# ***************** end of empty list *********************


def get_search_input():
    print(
        '\n Укажите ключевое слово для поиска заметки '
        'для обновления (или оставьте пустым)... '
    )

    srch_str: str = input('Ваш выбор: ').strip().lower()

    print(
        '\nВведите статус для поиска '
        '(или оставьте пустым):')

    srch_status: str = input('Ваш выбор: ').strip().lower()

    while True:
        print(
            '\nВведите дату (дд.мм.гггг) для поиска '
            '(или оставьте пустым):')

        try:
            srch_date = input('Ваш выбор: ')
            if srch_date:
                srch_date: str = utils.f_parser_date(srch_date)
            break
        except ValueError:
            utils.handle_error('invalid_input')

    d = dict()
    d['s_str'] = srch_str
    d['s_sts'] = srch_status
    d['s_dt'] = srch_date
    return d


def get_only_note(my_list_notes: list, action_str: str):
    # iface.f_print_all(my_list_notes)
    print(f'\nУкажите номер # заметки, которую хотите {action_str}. | '
          '[X] Возврат в главное меню')

    if (srch_index := input('Ваш выбор: ').lower()) == 'x':
        return None
    else:
        try:
            srch_index = int(srch_index)
        except ValueError:
            pass
    while srch_index not in range(1, len(my_list_notes) + 1):
        print('Заметки с таким номером не существует. '
              'Попробуйте еще раз')
        try:
            srch_index = int(input('Ваш выбор: '))

        except ValueError:
            pass

    for i, n in enumerate(my_list_notes, start=1):
        if srch_index == i:
            return n


def filter_notes(my_list_notes):
    while not (
            list_for_update := d.apply_filter_to_list(my_list_notes, get_search_input())
    ):
        print('[X] Возврат | [Enter] Повторить ввод')
        if input('Ваш выбор: '
                 ).strip().lower() == 'x':
            return my_list_notes

    return list_for_update
