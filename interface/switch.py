import sys

from copy import deepcopy
from data import f_empty_list, f_add_new_note, f_update_note, \
    f_del_note, search_note, save_chg_cloud
from interface import f_print_all


def distrib_func(my_choice, list_notes_local):
    my_list_notes = deepcopy(list_notes_local)

    # show all notes
    if my_list_notes is None or len(my_list_notes) == 0:
        my_list_notes = f_empty_list()

    # show all
    if my_choice == '2':

        f_print_all(my_list_notes)

        my_list_notes = context_menu(my_list_notes)

        if my_list_notes != list_notes_local:
            list_notes_local = save_chg_cloud(my_list_notes)

        return list_notes_local

    # create new
    if my_choice == '1':

        print('\nStart new note')
        my_list_notes.append(
            f_add_new_note(my_list_notes))

        if my_list_notes != list_notes_local:
            list_notes_local = save_chg_cloud(my_list_notes)

        return list_notes_local

    # update
    if my_choice == '3':

        f_print_all(my_list_notes)
        print(
            '\n Укажите заголовок для поиска заметки '
            'для обновления. Оставьте поле пустым для возврата '
            'в главное меню...')

        srch_str = input('Ваш выбор: ').lower()

        my_list_notes = f_update_note(
            my_list_notes, srch_str)

        f_print_all(my_list_notes)

        if my_list_notes != list_notes_local:
            list_notes_local = save_chg_cloud(my_list_notes)

        return list_notes_local

    # delete
    if my_choice == '4':

        f_print_all(my_list_notes)

        print(
            '\n Укажите заголовок или имя пользователя '
            'для поиска заметки для удаления... '
            'Оставьте поле пустым для возврата '
            'в главное меню')

        srch_str = input('\nВаш выбор: ').lower()

        my_list_notes = f_del_note(
            my_list_notes, srch_str)

        f_print_all(my_list_notes)

        if my_list_notes != list_notes_local:
            list_notes_local = save_chg_cloud(my_list_notes)

        return list_notes_local

    # search
    if my_choice == '5':

        srch_str = input(
            '\n Укажите заголовок для поиска заметки '
            'для обновления... Оставьте поле пустым для возврата '
            'в главное меню... ').lower()

        srch_status = input(
            '\nВведите статус для поиска '
            '(или оставьте пустым): ').lower()

        found_list_notes = search_note(
            my_list_notes, srch_str, srch_status)

        if len(found_list_notes) > 0:
            f_print_all(found_list_notes)
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


def context_menu(my_list_notes):
    while True:

        choice = input(
            '\nIf you want to delete some notes '
            'press (D)el, to Add new press (A)dd '
            '\nFor exit to main menu press X... ').lower()

        if choice in ['del', 'd']:
            del_str = input(
                '\nEnter username or title of the note '
                'you want to delete... '
            )
            my_list_notes = f_del_note(
                my_list_notes, srch_str=del_str)
            f_print_all(my_list_notes)
            continue

        elif choice in ['add', 'a']:
            my_list_notes.append(
                f_add_new_note(my_list_notes))
            f_print_all(my_list_notes)
            continue

        elif choice in ['x', 'exit']:

            return my_list_notes

        else:
            print('\nUnknown command, try more time...')
            continue
#   ******************** end of context menu *************