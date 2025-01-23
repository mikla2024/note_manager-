# import classes 'datetime' from 'datetime' module
from datetime import datetime as dt, timedelta
import sys
import os


# check unique title when add: if title exists returns False
def f_uni(list_, title_):
    if list_ is not None:
        if title_ in list_:
            return False
    return True


# update current status.
def f_status_update(note):
    print(
        '\nChoose new status of your note then press Enter...:'
        '\n1. In progress \n2. Postponed \n3. Done')
    while True:
        ans = input()
        if ans == '1':
            note['status'] = 'In progress'
            break
        elif ans == '2':
            note['status'] = 'Postponed'
            break
        elif ans == '3':
            note['status'] = 'Done'
            break
        else:
            print('Error. Try one more time')

    print(f'\nStatus is updated. New status is: '
          f'{note.get("status").upper()}')

    input("\nTo continue press Enter...")
    return True


# print all note's data' Arguments: note - dict, c - counter (optional)
def f_print_note_data(note, c=''):
    print(f'\nNote #{note.get("note id")}:')
    # output all values from dictionary
    for key, value in note.items():
        # additional format of dates
        if type(value) == dt:
            print(f'***{key.capitalize()}: {value:%d %b}')
            continue
        elif type(value) == list:
            print(f'***{key.capitalize()}: {", ".join(value)}')
            continue
        print(f'***{key.capitalize()}: {value}')
    deadline_delta_days = f_deadline_check(note)
    if deadline_delta_days > 0:
        print(
            f'\nYou missed your deadline '
            f'{deadline_delta_days} days ago')

    elif deadline_delta_days < 0:
        print(f'\nYour deadline is in '
              f'{str(deadline_delta_days)[1:]} days')

    elif deadline_delta_days == 0:
        print('\nYour deadline is TODAY!!!')


# check how many days to deadline
def f_deadline_check(note):
    day_delta = dt.today() - note.get('issue_date')
    return day_delta.days


# make dict. with note
def f_add_new_note():
    my_id = len(list_notes) + 1
    note = {}
    note['note id'] = my_id
    note['username'] = input('\nEnter your name: ')
    note['content'] = input("Enter the note's content: ")
    note['status'] = 'In progress'
    note['created_date'] = dt.today()
    # check input date format and err handler
    while True:
        try:
            parsed_issue_date: dt = \
                dt.strptime(input(
                    'Enter deadline in DD.MM.YYYY format:'
                ), '%d.%m.%Y')

        except ValueError:
            print('Wrong date format, try one more time!')
        else:
            break
    note['issue_date'] = parsed_issue_date

    # user can input any amounts of titles or exit if press enter with empty field
    while True:
        title_str = input(
            '\nEnter title or leave this field empty.'
            'To continue press Enter: ')
        if title_str != '':
            if f_uni(note.get('titles'), title_str):
                # if key doesnt exist in dict it will be added as list
                note.setdefault('titles', []).append(title_str)
            else:
                print('This title already exists')
        else:
            print('\nYour titles are:')
            if note.get('titles') is not None:
                for title in note.get('titles'):
                    print(title)
                break
            else:
                print("You should choose at least one title...")
    # output note's data
    f_print_note_data(note)
    # ask to change the status
    while True:
        choice = input(
            '\nDo you want to change the status of your '
            'note (yes/no)').lower()

        if choice in ['yes', 'y'] and f_status_update(note):
            f_print_note_data(note)
            # break
        elif choice in ['no', 'n']:
            print('Note is added')
            break
        else:
            print('Error, try more time...')
    return note


# make list with notes, every note as dict
list_notes = []
i = True  # flag for welcome message

while True:
    if i == True:
        print('Hi there! Welcome to Note Manager...')
        i = False
    choice = input(
        '\nDo you want to add the new note'
        '(yes/no)').lower()
    if choice in ['yes', 'y']:
        list_notes.append(f_add_new_note())
        # break
    elif choice in ['no', 'n']:
        if len(list_notes) < 1:
            continue
        else:
            sys.exit(1)
        print('\nYour notes:')
        for note in list_notes:
            f_print_note_data(note)
            print('*************************')
