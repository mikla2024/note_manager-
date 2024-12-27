# import classes 'datetime' from 'datetime' module
from datetime import datetime as dt


# check unique title when add: if title exists returns False
def f_uni(list_, title_):
    if list_ is not None:
        if title_ in list_:
            return False
    return True


# dict. with notes
notes = {}
notes['username'] = input('Enter your name: ')
notes['content'] = input("Enter the note's content: ")
notes['status'] = input('Enter status: ')
notes['created_date'] = dt.today()
# check input date format and err handler
while True:
    try:
        parsed_issue_date: dt = dt.strptime(input(
            'Enter deadline in DD.MM.YYYY format: '
            ),'%d.%m.%Y'
            )
                                                                          
    except ValueError:
        print('Wrong date format, try one more time!')
    else:
        break
notes['issue_date'] = parsed_issue_date

# user can input any amounts of titles or exit if press enter with empty field
while True:
    title_str = input(
        '\nEnter title or leave this field empty.'
        'To continue press Enter: '
        )
                                                                                                                                           
    if title_str != '':
        if f_uni(notes.get('titles'), title_str):
            # if key doesnt exist in dict it will be added as list
            notes.setdefault('titles', []).append(title_str)
        else:
            print('This title already exists')
    else:
        print('\nYour titles are:')
        if notes.get('titles') is not None:
            for title in notes.get('titles'):
                print(title)
            break
        else:
            print("You should choose at least one title...")

print('\nData you entered:')
# output all values from dictionary
for key, value in notes.items():
    # additional format of dates
    if type(value) == dt:
        print(f'***{key.capitalize()}: {value:%-d %b}')
        continue
    elif type(value) == list:
        print(f'***{key.capitalize()}: {", ".join(value)}')
        continue
    print(f'***{key.capitalize()}: {value}')

