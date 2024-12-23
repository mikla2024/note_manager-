# import classes 'date', 'datetime' from 'datetime' module
from datetime import datetime
# main variables entered by user
username = input('Enter your name: ')
title = input('Enter title of note: ')
content = input("Enter the note's content: ")
status = input('Enter the status: ')
created_date: datetime = datetime.today()
# date format check and err handler
while True:
  try:
    parsed_issue_date: datetime =  \
     datetime.strptime(input('Enter deadline in dd.mm.yyyy format: '),
																					'%d.%m.%Y')
  except ValueError:
    print('Wrong date format, try one more time!')
  else:
    break
# output of variables
print("\nYou entered:")
print('имя пользователя: ', username)
print('название: ', title)
print('содержание: ', content)
print('текущий статус: ', status)
print('дата создания:', created_date.strftime('%-d %b'))
print('дата истечения:', parsed_issue_date.strftime('%-d %b'))


