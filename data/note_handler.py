import uuid
import interface.menu as menus
import interface.show_notes as shn
from datetime import datetime as dt, timedelta
from utils.date_handler import f_parser_date


def f_empty_list():
    my_list_notes = []

    while True:
        ans = input(
            '\nTo add new note press (A)dd '
            'or press e(X)it...').lower()

        if ans.lower() in ['a', 'add']:
            my_list_notes.append(f_add_new_note(my_list_notes))
            shn.f_print_all(my_list_notes)

        elif ans.lower() in ['x', 'exit']:
            menus.main_menu(my_list_notes)
            # return my_list_notes
        else:
            print('Command is unknown')
            continue
# ***************** end of empty list *********************


def f_add_new_note(my_list_notes, my_note=None, upd_key=None):
    if my_note is None:
        my_note = {
            'note_id': '',
            'username': 'mikla',
            'content': '',
            'status': 'in progress',
            'create_date': dt.strftime(dt.today(), '%d.%m.%Y'),
            'issue_date': dt.strftime((dt.today() + timedelta(days=7)), '%d.%m.%Y'),
            'titles': []
        }

    print(
        '\nПри вводе новых значений, если оставить '
        'поле пустым, запишется [значение по умолчанию]. '
        'Даты вводить в формате ДД.ММ.ГГГГ'
    )

    if upd_key is not None:
        upd_note = {
            k: v for k, v in my_note.items() if k == upd_key}
    else:
        upd_note = {
            k: v for k, v in my_note.items()
        }

    for key, value in upd_note.items():
        # print(type(value))
        if not isinstance(value, list):

            if key == 'note_id':
                continue

            while True:
                if key == 'status':
                    user_value = f_status_update(my_note).get('status')

                else:
                    user_value = input(
                        f'\nEnter new value or leave the original one [{key}]: '
                        f'[{value}]...'
                    )

                if key in ['create_date', 'issue_date']:
                    new_value = f_parser_date(user_value)
                    if not new_value:
                        print(
                            'Неправильный формат даты, '
                            'попробуйте еще раз...'
                        )
                        continue

                if user_value == '':
                    new_value = value
                else:
                    new_value = user_value

                break

            # list of titles
        else:
            new_value = []
            # print(len(new_value))
            while True:
                user_value = input(
                    f'\nEnter any amount of new titles. '
                    f'For finish leave field empty {new_value}: '
                )

                # if user_value not in [
                #         a for n in my_list_notes if
                #         isinstance(n,dict) for a in n.get('titles')
                #         ] and \
                if user_value != '' and \
                        user_value not in new_value:

                    new_value.append(user_value)

                elif user_value == '' and len(new_value) > 0:
                    break

                else:
                    print('\n Item should be unique')
                    continue

        upd_note[key] = new_value
    # generator of random value
    upd_note['note_id'] = str(uuid.uuid4())

    for k, v in my_note.items():
        my_note[k] = upd_note.get(k, v)

    return my_note
# **************** end of add new_note ******************


def f_status_update(my_note):

    while True:
        print(
        '\nChoose new status of your note then press Enter...:'
        '\n1. In progress'
        '\n2. Postponed'
        '\n3. Done'
                )
        ans = input('Ваш выбор: ')
        if ans == '1':
            my_note['status'] = 'In progress'
            break
        elif ans == '2':
            my_note['status'] = 'Postponed'
            break
        elif ans == '3':
            my_note['status'] = 'Done'
            break
        else:
            print('Wrong status. Try one more time')

    print(f'\nStatus is updated. New status is: '
    f'{my_note.get("status").upper()}')
    input("\nTo continue press Enter...")
    return my_note
# ****************** end status update *************


def f_del_note(my_list_notes, srch_str = None):

    i = 0  # amount of notes for delete

    if srch_str == '':
        print('\nВы ничего не выбрали')
        input('\nДля возврата в главное меню нажмите Enter...')
        return my_list_notes

    # search user keyword in titles and other values of notes
    for my_note in my_list_notes:
        # search in dict.values regardless of capital letters
        if srch_str.lower() in [str(a).lower() for a in my_note.values()]:
            i += 1
            my_note.setdefault('del_flag', True)
        # search in titles
        elif srch_str.lower() in [str(a).lower() for a in
        my_note.get('titles')]:
            i += 1
            my_note.setdefault('del_flag', True)
    # if something is founded
    if i > 0:

        while True:
            del_confrm = input(
                    f'\n{i} notes will be deleted..Yes/No ').lower()

            if del_confrm in ['yes', 'y']:
                new_list_notes=[a for a in my_list_notes
                if not (a.get('del_flag'))]
                print('\nThe choosen note(s) is(are) deleted')
                return new_list_notes

            elif del_confrm in ['no', 'n']:
                new_list_notes = []
                for d in my_list_notes:
                    d.pop('del_flag', None)
                    new_list_notes.append(d)
                return new_list_notes

            else:
                print('Неизвестная команда. Попробуйте еще раз...')
                continue

    print('\nThe note with such parameters can not be found')
    input('\nTo continue press Enter...')
    return my_list_notes
# ******************* end of del_note *********************


def f_update_note(my_list_notes, srch_str):
    if srch_str == '':
        print('\nВы ничего не выбрали')
        input('\nДля возврата в главное меню нажмите Enter...')
        return my_list_notes

    # search user keyword in titles and other values of notes
    for my_note in my_list_notes:

        # search in titles
        x = [a.lower() for a in my_note.get('titles')]
        if srch_str in x:
            print('\nNote is found \n*********************')

            while True:
                shn.f_print_note_data(my_note, 0)

                print(
                    '\nВведите название поля для обновления, '
                    'или оставьте пустым для обновления нескольких '
                    'полей. Для возврата введите "X"')
                # choosing the key for update
                ans = input('Ваш выбор: ').lower()
                if ans == '':
                    new_list = [
                        a for a in my_list_notes
                        if a.get('note_id') != my_note.get('note_id')
                    ]
                    my_note = f_add_new_note(new_list, my_note)

                    new_list.append(my_note)
                    return new_list

                elif ans == 'x':
                    return my_list_notes


                else:
                    # if key is found
                    if ans in [a for a in my_note.keys()]:
                        new_list = [
                            a for a in my_list_notes
                            if a.get('note_id') !=
                               my_note.get('note_id')
                        ]
                        my_note = f_add_new_note(
                            new_list, my_note, ans)

                        new_list.append(my_note)
                        return new_list
                    # key is not found
                    else:
                        print('\nполе с таким названием не найдено...')
                        input('для продолжения нажмите Enter')
                        continue

    print('\nНичего не найдено. Поробуйте изменить поиск')
    input('\nДля продолжения нажмите Enter...')

    return my_list_notes

# ******************* end of update note ******************


def search_note(my_list_notes, srch_str, srch_status):
    if srch_str == '' and srch_status == '':
        print(
            '\nВы ничего не выбрали и будете '
            'перенаправлены в главное меню. '
            'Нажмите Enter для продолжения...')
        input()
        menus.main_menu(my_list_notes)

    elif srch_str == '' and srch_status != '':

        found_list_notes = [a for a in my_list_notes
                            if a.get('status') == srch_status]

        return found_list_notes

    found_list_notes = []

    for my_note in my_list_notes:

        if srch_str in [a for a in
                        {k: v.lower() for k, v in my_note.items()
                         if k != 'status' and type(v) != list}.values()] or \
                srch_str in [a.lower() for b in my_note.values() for
                             a in b if type(b) == list]:
            found_list_notes.append(my_note)

    if len(found_list_notes) > 0 and srch_status != '':
        found_list_notes = [a for a in found_list_notes if str(a.get('status')).lower() == srch_status]

    return found_list_notes
# ****************** end search note **********************