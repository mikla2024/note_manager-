import utils


def get_status_input():
    while True:
        print(
        '\nВыберете один из предложенных статусов и нажмите Enter...:'
        '\n1. Важно'
        '\n2. На исполнении'
        '\n3. Выполнено'
                )
        user_input = input('Ваш выбор: ')
        try:
            return utils.validate_user_status(user_input)

        except:
            print('Статус должен соответствовать одному из значений')




def f_status_update(my_note, new_status):

    my_note['status'] = new_status
    print(f'\nStatus is updated. New status is: '
    f'{my_note.get("status").upper()}')
    input("\nTo continue press Enter... ")
    return my_note

# ****************** end status update *************