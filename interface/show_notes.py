from datetime import datetime as dt, timedelta
import utils

def f_print_all(my_list_notes):
    print('\nYour notes:')
    # if my_list_notes is None or len(my_list_notes) == 0:
    #     print(
    #         'There is no notes yet. But you can '
    #         'always add some...')
    #     my_list_notes = f_empty_list()

    for index_, note in enumerate(my_list_notes):
        if isinstance(note, dict):
            f_print_note_data(note, index_)


def f_print_note_data(my_note, my_count):
    print(f'\nNote #{my_count+1}:')
    # output all values from dictionary
    for key, value in my_note.items():
        # additional format of dates
        if key == 'created_date' or key == 'issue_date':
            print(f'***{key.capitalize()}: '
            f'{dt.strptime(value,"%d.%m.%Y").strftime("%d %b")}')
            continue
        elif type(value) == list:
            print(f'***{key.capitalize()}: {", ".join(value)}')
            continue
        elif key == 'note_id':
            continue
        print(f'***{key.capitalize()}: {value}')
    deadline_delta_days = utils.f_deadline_check(my_note)
    if deadline_delta_days > 0:
        print(
            f'\nYou missed your deadline '
            f'{deadline_delta_days} days ago')
    elif deadline_delta_days < 0:
        print(f'\nYour deadline is in '
        f'{str(deadline_delta_days)[1:]} days')
    elif deadline_delta_days == 0:
        print('\nYour deadline is TODAY!!!')
    print('*' * 30)
