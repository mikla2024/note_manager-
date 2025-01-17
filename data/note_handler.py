import sys
import uuid

from datetime import datetime as dt, timedelta
import utils
import interface as iface
import data


def f_add_new_note(my_list_notes, my_note=None, upd_field=None):

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

    if upd_field is not None:
        upd_note = {
            k: v for k, v in my_note.items() if k == upd_field}
    else:
        upd_note = {
            k: v for k, v in my_note.items()
        }

    for key, value in upd_note.items():

        if not isinstance(value, list):

            if key == 'note_id':
                continue

            while True:
                if key == 'status':
                    user_value = data.get_status_input()

                else:
                    user_value = input(
                        f'\nEnter new value or leave the original one [{key}]: '
                        f'[{value}]... '
                    )

                if key in ['create_date', 'issue_date']:
                    new_value = utils.f_parser_date(user_value)

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


def f_del_note(my_list_notes, note_for_delete):
    try:
        my_list_notes.remove(note_for_delete)
        return my_list_notes
    except:
        print ('f_del_note is fail')
        sys.exit(1)

# ******************* end of del_note *********************


def f_update_note(my_note:dict):

    while True:
        iface.f_print_note_data(my_note, 1)

        print(
            '\nВведите название поля для обновления, '
            'или оставьте пустым для обновления нескольких '
            'полей. Для возврата введите "X"')
        # choosing the key for update
        ans = input('Ваш выбор: ').lower()

        if ans == '':

            my_note = f_add_new_note([], my_note)
            return my_note

        elif ans == 'x':
            return my_note



        elif ans in [a for a in my_note.keys()]:

            my_note = f_add_new_note(
                [], my_note, ans)


            return my_note
        # key is not found
        else:
            print('\nполе с таким названием не найдено...')
            input('для продолжения нажмите Enter ')
            continue

    print('\nНичего не найдено. Поробуйте изменить поиск')
    input('\nДля продолжения нажмите Enter... ')

    return my_note

# ******************* end of update note ******************


def apply_filter_to_list(my_list_notes, search_keys: dict):

    srch_str = search_keys.get('s_str')
    srch_status = search_keys.get('s_sts')

    if srch_str == '':
        list_notes_found = [a for a in my_list_notes]


    else:
        list_notes_found = [a for a in my_list_notes if srch_str in
                           [b.lower() for b in a.get('titles')]
                           or srch_str in
                           [c.lower() for c in a.values() if type(c) != list]
                           ]

    if srch_status != '':
        list_notes_found = [a for a in list_notes_found if
                           srch_status == str(a.get('status')).lower()]

    if len(list_notes_found) == 0:
        print('Ничего не нашлось. Попробуйте изменить поиск')
        return []

    #iface.f_print_all(list_notes_found)
    return list_notes_found
# ****************** end search note **********************