import sys
import uuid

from datetime import datetime as dt, timedelta
import utils
import interface as iface
import data


def f_add_new_note(my_note: dict = None, upd_field=None):
    if my_note is None:
        my_note = {
            'note_id': '',
            'username': 'mikla',
            'content': '',
            'status': 'На исполнении',
            'create_date': dt.strftime(dt.today(), '%d.%m.%Y'),
            'issue_date': dt.strftime((dt.today() + timedelta(days=7)), '%d.%m.%Y'),
            'titles': []
        }

    print(
        '\nПри вводе новых значений, если оставить '
        'поле пустым, запишется [значение по умолчанию]. '
        'Даты вводить в формате ДД.ММ.ГГГГ'
    )

    if upd_field is not None:
        upd_note = {
            k: v for k, v in my_note.items() if k == upd_field}
    else:
        upd_note = {
            k: v for k, v in my_note.items()
        }

    for key, value in upd_note.items():

        if not isinstance(value, list):

            if key == 'note_id' or key == 'id':
                continue

            while True:
                if key == 'status':
                    user_value = data.get_status_input()

                else:
                    user_value = input(
                        f'\nВведите новое значение или оставьте существующее [{key}]: '
                        f'[{value}]... '
                    )

                if key in ['create_date', 'issue_date']:
                    try:
                        new_value = utils.f_parser_date(user_value)

                    except ValueError:
                        utils.handle_error('invalid_input')
                        continue

                if not user_value:
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
                    f'\nВведите любое количество заголовков. '
                    f'Для завершения оставьте поле пустым {new_value}: '
                )

                if user_value and \
                        user_value not in new_value:

                    new_value.append(user_value)

                elif not user_value and new_value:
                    break

                else:
                    print('\n Значение должно быть уникальным. '
                          '(Хотя бы одно значение должно быть введено) ')
                    continue

        upd_note[key] = new_value
    # generator of unique value
    upd_note['note_id'] = str(uuid.uuid4())

    for k, v in my_note.items():
        my_note[k] = upd_note.get(k, v)

    return my_note


# **************** end of add new_note ******************


def f_del_note(my_list_notes, note_for_delete):
    try:
        my_list_notes.remove(note_for_delete)
        print('Заметка успешно удалена')
        input('Для продолжения нажмите Enter... ')

    except:
        print('f_del_note is fail')
        sys.exit(1)


# ******************* end of del_note *********************


def f_update_note(my_note: dict):
    while True:
        iface.f_print_note_data(my_note, 1)

        print(
            '\nВведите название поля для обновления, '
            'или оставьте пустым для обновления нескольких '
            'полей | [X] Закончить')
        # choosing the key for update
        ans = input('Ваш выбор: ').strip().lower()

        if ans == '':
            f_add_new_note(my_note)

        elif ans == 'x':
            break

        elif ans in my_note.keys():

            f_add_new_note(my_note, ans)

        # key is not found
        else:
            print('\nполе с таким названием не найдено...')
            continue


# ******************* end of update note ******************


def apply_filter_to_list(my_list_notes, search_keys: dict):
    srch_str = search_keys.get('s_str')
    srch_status = search_keys.get('s_sts')
    srch_dt = search_keys.get('s_dt')
    list_notes_found = [a for a in my_list_notes]

    if srch_str:
        list_notes_found = [a for a in my_list_notes if srch_str in
                            [b.lower() for b in a.get('titles')]
                            or srch_str in
                            [c.lower() for c in a.values() if type(c) == str]
                            ]

    if srch_status:
        list_notes_found = [a for a in list_notes_found if
                            str(a.get('status')).lower() == srch_status]

    if srch_dt:
        list_notes_found = [a for a in list_notes_found if
                            a.get('issue_date') == srch_dt]

    if not list_notes_found:
        utils.handle_error('empty_list')
        return []

    # iface.f_print_all(list_notes_found)
    return list_notes_found
# ****************** end search note **********************
