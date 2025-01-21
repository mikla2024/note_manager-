import sys

from copy import deepcopy
import data as d
import interface as iface
import utils

def main_menu(my_list_notes=None):

    if my_list_notes is None:
        my_list_notes=[]

    while True:
        print('''

*** Меню управления заметками ***:

1. Создать новую заметку

2. Показать все заметки

3. Обновить заметку

4. Удалить заметку

5. Найти заметки

6. Выйти из программы

''')

        my_list_notes = (
        iface.distrib_func(input('Ваш выбор: '), my_list_notes)
        )

        continue


def distrib_func(my_choice, my_list_notes):

    list_notes_local = deepcopy(my_list_notes)

    # show all notes
    if not my_list_notes:
        iface.f_empty_list()

    # show all
    if my_choice == '2':

        iface.f_print_all(my_list_notes)

        context_menu(my_list_notes)

        if my_list_notes != list_notes_local and \
                save_chg_cloud(my_list_notes):
                return my_list_notes

        return list_notes_local


        # return

    # create new
    if my_choice == '1':

        print('\nНачало новой заметки')
        my_list_notes.append(
            d.f_add_new_note()
        )

        if my_list_notes != list_notes_local and \
                save_chg_cloud(my_list_notes):
            return my_list_notes

        return list_notes_local

    # update
    if my_choice == '3':

        iface.f_print_all(my_list_notes)

        print('\n[F] Фильр заметок | '
              '[Enter] Продолжить без фильтра')

        if input('Ваш выбор: ').lower() == 'f':
            list_for_update = filter_notes(my_list_notes)

        else:
            list_for_update = my_list_notes.copy()

        iface.f_print_all(list_for_update)

        if (note_for_update := get_only_note(list_for_update,'обновить')) is not None:
            d.f_update_note(note_for_update)

        if my_list_notes != list_notes_local and \
                save_chg_cloud(my_list_notes):
            return my_list_notes

        return list_notes_local

    # delete
    if my_choice == '4':

        iface.f_print_all(my_list_notes)
        print('\n[F] Фильр заметок | '
              '[Enter] Продолжить без фильтра')

        if input('Ваш выбор: ').lower() == 'f':
            list_for_delete = filter_notes(my_list_notes)

        else:
            list_for_delete = my_list_notes.copy()

        iface.f_print_all(list_for_delete)

        if (note_for_delete := get_only_note(list_for_delete, 'удалить')) is not None:
            d.f_del_note(my_list_notes, note_for_delete)

        iface.f_print_all(my_list_notes)

        if my_list_notes != list_notes_local and \
                save_chg_cloud(my_list_notes):
            return my_list_notes

        return list_notes_local

    # search
    if my_choice == '5':

        found_list_notes = filter_notes(my_list_notes)

        if found_list_notes:
            iface.f_print_all(found_list_notes)
            context_menu(my_list_notes)
        else:
            utils.handle_error('empty_list')

        if my_list_notes != list_notes_local and \
                save_chg_cloud(my_list_notes):
            return my_list_notes

        return list_notes_local

    if my_choice == '6':
        sys.exit(0)

    return list_notes_local
# ****************** end distrib func *****************

# ****************** context menu ******************
def context_menu(my_list_notes):
    while True:
        try:
            print('\n[D] Удаление | [N] Новая | [X] Выход в главное меню')
            choice = input(
            'Ваш выбор: '
            ).strip().lower()

            if choice in ['del', 'd']:

                if (my_note := get_only_note(my_list_notes,'удалить')) is not None:
                    d.f_del_note(my_list_notes, my_note)
                    iface.f_print_all(my_list_notes)
                    continue

            elif choice in ['new', 'n']:
                my_list_notes.append(d.f_add_new_note())
                iface.f_print_all(my_list_notes)
                continue

            elif choice in ['x', 'exit']:

                return # my_list_notes

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

            if ans.lower() in ['y','yes']:
                d.save_to_json_git(my_list_note)
                return True

            elif ans in ['n','no']:
                return False

            else:
                raise ValueError
        except ValueError:
            utils.handle_error('invalid_input')

# ******************* end of save_chd_cloud *************

def f_empty_list():
    my_list_notes: list = []
    print ('Сохраненные заметки не найдены...')
    while True:
        try:
            print('\n[N] Добавить новую заметку | [X] Выход')
            ans = input(
                'Ваш выбор: '
                ).strip().lower()

            if ans.lower() in ['n', 'add']:
                my_list_notes.append(d.f_add_new_note(my_list_notes))
                iface.f_print_all(my_list_notes)

            elif ans.lower() in ['x', 'exit']:
                if len(my_list_notes) > 0:
                    iface.save_chg_cloud(my_list_notes)
                iface.main_menu(my_list_notes)
                # return my_list_notes
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

    iface.f_print_all(my_list_notes)
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