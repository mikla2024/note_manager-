# import classes 'date', 'datetime' from 'datetime' module
from datetime import datetime

# main variables entered by user
username = input('Enter your name: ')
content = input("Enter the note's content: ")
status = input('Enter status of the note: ')
created_date: datetime = datetime.today()
# date format check with err handler
while True:
    try:
        parsed_issue_date: datetime = \
            datetime.strptime(input('Enter deadline in dd.mm.yyyy format: '),
                              '%d.%m.%Y')
    except ValueError:
        print('Wrong date format, try one more time!')
    else:
        break
title1 = input("input note's title 1: ")
title2 = input("input note's title 2: ")
title3 = input("input note's title 3: ")
titles = [title1, title2, title3]
# Output data
print('\nВы ввели:')
print(f'имя пользователя: {username}')
print(f'заголовки заметки: {titles}')
print(f'содержание: {content}')
print(f'текущий статус: {status}')
print(f'дата создания: {created_date:%d %b}')
print(f'дата истечения: {parsed_issue_date:%d %b}')
