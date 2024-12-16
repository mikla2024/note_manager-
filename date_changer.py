from datetime import date,datetime # import classes 'date', 'datetime' from 'datetime' module

username = 'mikla' # define username
title = 'Note 1'	# def. name of note
content = 'Conference call' # content of note
status = 'open' # current status of the note
created_date: date = date.today() # date of creation
issued_date: datetime = datetime(2024,12,18,15,45) # deadline date with time

print ('имя пользователя: ',username)
print ('название: ',title)
print ('содержание: ',content)
print ('текущий статус: ',status)
#returns string from date object, %-d - day, %b - month in short format 
print ('дата создания:',created_date.strftime('%-d %b'))
print ('дата истечения:',issued_date.strftime('%-d %b %H:%M'))
