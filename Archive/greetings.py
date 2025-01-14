from datetime import date  # import class 'date' from 'datetime' module
# main variables
username = 'mikla'
title = 'title 1'
content = 'Conference call'
status = 'open'
created_date: date = date.today()
issued_date: date = date(2024, 12, 18)
# output of variable values
print('имя пользователя: ', username)
print('название: ', title)
print('содержание: ', content)
print('текущий статус: ', status)
# returns string from date object
print('дата создания: ', created_date.strftime('%d %b %Y'))
print('дата истечения: ', issued_date.strftime('%d %b %Y'))



