from datetime import date # import class 'date' from 'datetime' module

username = 'mikla' # define username
title = 'Note 1'	# def. name of note
content = 'Conference call' # content of note
status = 'open' # current status of the note
created_date: date = date.today() # date of creation
issued_date: date = date(2024,12,18) # deadline date

print ('имя пользователя: ',username)
print ('название: ',title)
print ('содержание: ',content)
print ('текущий статус: ',status)
print('дата создания:',created_date.day,
				'.',created_date.month)	#show creat. date in 'dd.mm' form.
print ('дата истечения: ',issued_date.day,
				'.',issued_date.month)	#show issued date in 'dd.mm' form.
