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

        my_list_notes = iface.distrib_func(
        input('Ваш выбор: '), my_list_notes
        )

        continue


def distrib_func(my_choice, list_notes_local):

    my_list_notes = deepcopy(list_notes_local)

    # show all notes
    if my_list_notes is None or len(my_list_notes) == 0:
        iface.f_empty_list()

    # show all
    if my_choice == '2':

        iface.f_print_all(my_list_notes)

        my_list_notes = context_menu(my_list_notes)

        if my_list_notes != list_notes_local:
            list_notes_local = save_chg_cloud(my_list_notes)

        return list_notes_local

    # create new
    if my_choice == '1':

        print('\nНачало новой заметки')
        my_list_notes.append(
            d.f_add_new_note(my_list_notes))

        if my_list_notes != list_notes_local:
            list_notes_local = save_chg_cloud(my_list_notes)

        return list_notes_local

    # update
    if my_choice == '3':

        iface.f_print_all(my_list_notes)

        print('\nЕсли хотите применить фильтр, введите F или f. '
              'Для продолжения нажмите Enter...')

        if input('Ваш выбор: ').lower() == 'f':
            list_for_update = filter_notes(my_list_notes)

        else:
            list_for_update = [a for a in my_list_notes]

        iface.f_print_all(list_for_update)

        if (note_for_update := get_only_note(list_for_update,'обновить')) is None:
            return my_list_notes

        my_list_notes.remove(note_for_update)
        my_list_notes.append(d.f_update_note(note_for_update))

        iface.f_print_all(my_list_notes)

        if my_list_notes != list_notes_local:
            list_notes_local = save_chg_cloud(my_list_notes)

        return list_notes_local

    # delete
    if my_choice == '4':

        iface.f_print_all(my_list_notes)
        print('\nЕсли хотите применить фильтр, введите F или f. '
              'Для продолжения нажмите Enter...')

        if input('Ваш выбор: ').lower() == 'f':
            list_for_delete = filter_notes(my_list_notes)

        else:
            list_for_delete = [a for a in my_list_notes]

        iface.f_print_all(list_for_delete)

        if (note_for_delete := get_only_note(list_for_delete, 'удалить')) is None:
            return my_list_notes

        my_list_notes = d.f_del_note(
            list_for_delete, note_for_delete)

        iface.f_print_all(my_list_notes)

        if my_list_notes != list_notes_local:
            list_notes_local = save_chg_cloud(my_list_notes)

        return list_notes_local

    # search
    if my_choice == '5':

        found_list_notes = filter_notes(my_list_notes)

        if len(found_list_notes) > 0:
            iface.f_print_all(found_list_notes)
            my_list_notes = context_menu(my_list_notes)
        else:
            print(
                '\nПохоже, что ничего не нашлось. '
                'Постарайтесь изменить параметры поиска. '
                'Для продолжения нажмите Enter...')
            input()
        if my_list_notes != list_notes_local:
            list_notes_local = save_chg_cloud(my_list_notes)

    if my_choice == '6':
        sys.exit(0)

    return list_notes_local
# ****************** end distrib func *****************

# ****************** context menu ******************
def context_menu(my_list_notes):
    while True:
        try:
            choice = input(
            '\nДля удаления заметок '
            'введите (D)el, для добавления новой заметки - (A)dd '
            '\nДля выхода в главное меню введите X... ').lower()

            if choice in ['del', 'd']:

                if my_note := (get_only_note(my_list_notes,'удалить')) is None:
                    return my_list_notes



                my_list_notes = d.f_del_note(
                    my_list_notes, my_note)

                iface.f_print_all(my_list_notes)
                continue

            elif choice in ['add', 'a']:
                my_list_notes.append(
                    d.f_add_new_note())

                iface.f_print_all(my_list_notes)
                continue

            elif choice in ['x', 'exit']:

                return my_list_notes

            else:
                raise ValueError

        except ValueError:
            utils.handle_error('invalid_input')
#   ******************** end of context menu *************

# save change dialog
def save_chg_cloud(my_list_note):

    while True:
        try:

            ans = input('Хотите синхронизировать изменения с облаком'
                        '---(y/n)...').lower()

            if ans.lower() in ['y','yes']:
                new_list: list = d.save_to_json_git(my_list_note)
                return new_list

            elif ans in ['n','no']:
                return my_list_note

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
            ans = input(
                '\nЧтобы добавить новую заметку введите (A)dd '
                'Для выхода - e(X)it... ').lower()

            if ans.lower() in ['a', 'add']:
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

    srch_str: str = input('Ваш выбор: ').lower()

    print(
        '\nВведите статус для поиска '
        '(или оставьте пустым): ')

    srch_status: str = input('Ваш выбор: ').lower()

    while True:
        print(
            '\nВведите дату (дд.мм.гггг) для поиска '
            '(или оставьте пустым): ')

        try:
            srch_date: str = utils.f_parser_date(input('Ваш выбор: '))
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
    print(f'\nУкажите номер # заметки, которую хотите {action_str}. '
          'Для возврата в главное меню, введите X')

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
        if input('Для возврата введите X. '
                 'Для продолжения нажмите Enter... ').lower() == 'x':
            return my_list_notes

    return list_for_update