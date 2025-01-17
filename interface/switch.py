import sys

from copy import deepcopy
import data as d
import interface as iface



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

        print('\nStart new note')
        my_list_notes.append(
            d.f_add_new_note(my_list_notes))

        if my_list_notes != list_notes_local:
            list_notes_local = save_chg_cloud(my_list_notes)

        return list_notes_local

    # update
    if my_choice == '3':

        iface.f_print_all(my_list_notes)

        print('\nЕсли хотите применить фильтр, введите F. '
              'Для продолжения нажмите Enter...')

        if input('Ваш выбор: ').lower() == 'f':
            list_for_update = filter_list_input(my_list_notes)

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
        print('Если хотите применить фильтр, введите F. '
              'Для продолжения нажмите Enter...')

        if input('Ваш выбор: ').lower() == 'f':
            list_for_delete = filter_list_input(my_list_notes)

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

        found_list_notes = filter_list_input(my_list_notes)

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

        choice = input(
            '\nIf you want to delete some notes '
            'press (D)el, to Add new press (A)dd '
            '\nFor exit to main menu press X... ').lower()

        if choice in ['del', 'd']:

            if my_note := (get_only_note(my_list_notes,'удалить')) is None:
                return my_list_notes



            my_list_notes = d.f_del_note(
                my_list_notes, my_note)

            iface.f_print_all(my_list_notes)
            continue

        elif choice in ['add', 'a']:
            my_list_notes.append(
                d.f_add_new_note(my_list_notes))
            iface.f_print_all(my_list_notes)
            continue

        elif choice in ['x', 'exit']:

            return my_list_notes

        else:
            print('\nUnknown command, try more time...')
            continue
#   ******************** end of context menu *************

# save change dialog
def save_chg_cloud(my_list_note):
    while True:

        ans = input('Do you want to sync changes with cloud'
                    '---(y/n)...').lower()

        if ans.lower() in ['y','yes']:
            new_list: list = d.save_to_json_git(my_list_note)
            return new_list

        elif ans in ['n','no']:
            return my_list_note
        else:
            print('\nUnknown command, try more time...')
            continue  # saving notes dialog
    return False

# ******************* end of save_chd_cloud *************

def f_empty_list():
    my_list_notes: list = []
    print ('Сохраненные заметки не найдены...')
    while True:
        ans = input(
            '\nTo add new note press (A)dd '
            'or press e(X)it... ').lower()

        if ans.lower() in ['a', 'add']:
            my_list_notes.append(d.f_add_new_note(my_list_notes))
            iface.f_print_all(my_list_notes)

        elif ans.lower() in ['x', 'exit']:
            if len(my_list_notes) > 0:
                iface.save_chg_cloud(my_list_notes)
            iface.main_menu(my_list_notes)
            # return my_list_notes
        else:
            print('Command is unknown')
            continue
# ***************** end of empty list *********************


def get_search_input():
    print(
        '\n Укажите ключевое слово для поиска заметки '
        'для обновления... '
        )

    srch_str: str = input('Ваш выбор: ').lower()

    print(
        '\nВведите статус для поиска '
        '(или оставьте пустым): ')

    srch_status: str = input('Ваш выбор: ').lower()
    d = dict()
    d['s_str'] = srch_str
    d['s_sts'] = srch_status
    return d


def get_only_note(my_list_notes: list, action_str: str):

    iface.f_print_all(my_list_notes)
    print(f'Укажите номер # заметки, которую хотите {action_str}. '
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

def filter_list_input(my_list_notes):

    while len(
            list_for_update := d.apply_filter_to_list(my_list_notes, get_search_input())
    ) == 0:
        if input('Для возврата введите X. '
                 'Для продолжения нажмите Enter... ').lower() == 'x':
            return my_list_notes

    return list_for_update