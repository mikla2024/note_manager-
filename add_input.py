# import classes 'date', 'datetime' from 'datetime' module
from datetime import datetime

username = input('input your name')		# define username
title = input('input title of note')		# def. name of note
content = input("input the note's content")		# content of note
status = 'open'		# current status of the note
created_date: datetime = datetime.today()		# date of creation
while True:
	try:
		parsed_issue_date: datetime =  \
			datetime.strptime(input('input deadline in dd.mm.yyyy format'),
																					'%d.%m.%Y')
	except ValueError:
		print('wrong date format, try one more time')
	else:
		break
print("\nYou inserted next data:")
print('имя пользователя: ', username)
print('название: ', title)
print('содержание: ', content)
print('текущий статус: ', status)
print('дата создания:', created_date.strftime('%-d %b'))
print('дата истечения:', parsed_issue_date.strftime('%-d %b'))


