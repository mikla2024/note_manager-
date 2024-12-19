# import classes 'date', 'datetime' from 'datetime' module
from datetime import datetime

username = input('input your name')  # define username
content = input("input the note's content")  # content of note
status = input('input status of the note')  # current status of the note
created_date: datetime = datetime.today()  # date of creation
# value check with err handler
while True:
	try:
		parsed_issue_date: datetime =  \
			datetime.strptime(input('input deadline in dd.mm.yyyy format'),
																					'%d.%m.%Y')
	except ValueError:
		print('wrong date format, try one more time')
	else:
		break
title1 = input("input note's title 1: ")
title2 = input("input note's title 2: ")
title3 = input("input note's title 3: ")
titles = [title1, title2, title3]
print('Вы ввели:')
print(f'имя пользователя: {username}')
print(f'заголовки заметки: {titles}')
print(f'содержание: {content}')
print(f'текущий статус: {status}')
print(f'дата создания: {created_date:%-d %b}')
print(f'дата истечения: {parsed_issue_date:%-d %b}')

