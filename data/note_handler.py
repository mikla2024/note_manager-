import uuid

from data.update_note import f_status_update
from interface.menus import main_menu
from interface.show_notes import f_print_all

from datetime import datetime as dt, timedelta

from utils.date_validation import f_parser_date


def f_empty_list():
    my_list_notes = []

    while True:
        ans = input(
            '\nTo add new note press (A)dd '
            'or press e(X)it...').lower()

        if ans.lower() in ['a', 'add']:
            my_list_notes.append(f_add_new_note(my_list_notes))
            f_print_all(my_list_notes)

        elif ans.lower() in ['x', 'exit']:
            main_menu(my_list_notes)
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