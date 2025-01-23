import data
import interface

if __name__ == '__main__':
    search_keys: dict = {
        's_str': str('content1').lower(),
        's_sts': str('Важно').lower(),
        's_dt': ''
    }

    test_note_1 = {
        'username': 'name1',
        'content': 'content1',
        'status': 'Важно',
        'titles': ['one', 'two'],
        'issue_date': '01.01.2025'
    }
    test_note_2 = {
        'username': 'name2',
        'content': 'content2',
        'status': 'В процессе',
        'titles': ['three', 'four'],
        'issue_date': '01.01.2026'
    }
    test_note_3 = {
        'username': 'name3',
        'content': 'content3',
        'status': 'Выполнено',
        'titles': ['five', 'six'],
        'issue_date': '01.01.2027'
    }
    test_list = [test_note_1, test_note_2, test_note_3]

    interface.f_print_all(
        data.apply_filter_to_list(test_list, search_keys)
    )
