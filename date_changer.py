# import classes 'date', 'datetime' from 'datetime' module
from datetime import date, datetime
# main variables
username = 'mikla'
title = 'Note 1'
content = 'Conference call'
status = 'open'
created_date: date = date.today()
issue_date: datetime = datetime(2024, 12, 18, 15, 45)
# output values
print('имя пользователя: ', username)
print('название: ', title)
print('содержание: ', content)
print('текущий статус: ', status)
# returns string from date object
print('дата создания:', created_date.strftime('%-d %b'))
print('дата истечения:', issue_date.strftime('%-d %b %H:%M'))
