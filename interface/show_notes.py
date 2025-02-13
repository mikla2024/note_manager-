from datetime import datetime as dt
import utils
from colorama import Fore, Style


def f_print_all(my_list_notes: list, start_=1):
    for index_, note in enumerate(my_list_notes, start=start_):
        if isinstance(note, dict):
            f_print_note_data(note, index_)


def f_print_note_data(my_note, index_):
    print(f'\nNote #{index_}:')

    status_colors = {
        'Важно': 'red',
        'Выполнено': 'green',
    }

    # if my_note['status'] == 'Важно':
    #     text_color = 'red'
    # elif my_note['status'] == 'Выполнено':
    #     text_color = 'green'
    # else:
    #     text_color = 'blue'

    # output all values from dictionary
    for key, value in my_note.items():

        # additional format of dates
        if key == 'created_date' or key == 'issue_date':
            print(f'*** {key.capitalize()}: '
                  f'{dt.strptime(value, "%d.%m.%Y").strftime("%d %b")}')
            continue
        elif key == 'titles':
            str_value = f'*** {key.capitalize()}: {", ".join(value)}'
            print(
                str_format(str_value, text_color=status_colors.get(my_note['status'], 'blue'))
            )
            continue

        elif key == 'note_id' or key == 'id':
            continue

        print(f'*** {key.capitalize()}: {value}')

    try:
        deadline_delta_days = utils.f_deadline_check(my_note)
        if deadline_delta_days > 0:
            print(
                str_format(f'\nВы пропустили контрольный срок '
                           f'{deadline_delta_days} день/дней назад', 'yellow')
            )
        elif deadline_delta_days < 0:
            print(f'\nКонтрольный срок наступит через '
                  f'{str(deadline_delta_days)[1:]} день/дней')
        elif deadline_delta_days == 0:
            print('\nКонтрольный  срок - сегодня!')

    except TypeError:
        pass

    print('*' * 30)


def str_format(str_text, text_color, style_=None):
    if text_color == 'red':
        return Fore.RED + f'{str_text}' + Style.RESET_ALL
    elif text_color == 'green':
        return Fore.GREEN + f'{str_text}' + Style.RESET_ALL
    elif text_color == 'cyan':
        return Fore.CYAN + f'{str_text}' + Style.RESET_ALL
    elif text_color == 'yellow':
        return Fore.YELLOW + f'{str_text}' + Style.RESET_ALL
    else:
        return Fore.BLUE + f'{str_text}' + Style.RESET_ALL
