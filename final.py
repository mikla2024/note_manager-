# import classes 'date', 'datetime' from 'datetime' module
from datetime import datetime
# dict. with notes
notes = {}
notes['username'] = input('input your name: ')
notes['content'] = input("input the note's content: ")
notes['status'] = input('input status: ')
notes['created_date'] = datetime.today()
# check input date format and err handler
while True:
	try:
		parsed_issue_date: datetime =  \
			datetime.strptime(input('input deadline in dd.mm.yyyy format: '),
																					'%d.%m.%Y')
	except ValueError:
		print('Wrong date format, try one more time!')
	else:
		break
notes['issue_date'] = parsed_issue_date
notes['titles'] = input('введите заголовки заметки через запятую:').split(',')
print('\nNote data:'.upper())
for key, value in notes.items():
	# additional formating the date
	if type(value) == datetime:
		print(f'{key}: {value:%-d %b}')
		continue
	print(f'{key}: {value}')

