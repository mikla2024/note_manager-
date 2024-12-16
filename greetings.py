from datetime import date # import class 'date' from 'datetime' module

username = 'mikla' # define username
title = 'Note 1'	# def. name of note
content = 'Conference call' # content of note
status = 'open' # current status of the note
created_date: date = date.today() # present date (today)
issued_date: date = date(2024,12,18) # deadline date

print ('имя пользователя: ',username)
print ('название: ',title)
print ('содержание: ',content)
print ('текущий статус: ',status)
#returns string from date object, %-d - day, %b - month in short format
print ('дата создания: ',created_date.strftime('%-d %b %Y'))
print ('дата истечения: ',issued_date.strftime('%-d %b %Y'))
