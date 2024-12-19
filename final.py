# import classes 'date', 'datetime' from 'datetime' module
from datetime import datetime


# check unique title when add
def f_uni(list_, title_):
	if list_ is not None:
		for title in list_:
			if title_ == title:
				return False
	return True


# dict. with notes
notes = {}
notes['username'] = input('Enter your name: ')
notes['content'] = input("Enter the note's content: ")
notes['status'] = input('Enter status: ')
notes['created_date'] = datetime.today()
# check input date format and err handler
while True:
	try:
		parsed_issue_date: datetime =  \
			datetime.strptime(input('Enter deadline in DD.MM.YYYY format: '),
																					'%d.%m.%Y')
	except ValueError:
		print('Wrong date format, try one more time!')
	else:
		break
notes['issue_date'] = parsed_issue_date

# user can input any amounts of titles or exit if press enter with empty field
while True:
	title_str = input('\nEnter title or leave this field empty.'
																			'To continue press Enter: ')
	if title_str != '':
		if f_uni(notes.get('titles'), title_str):
			# if key doesnt exist in dict it will be added as list
			notes.setdefault('titles', []).append(title_str)
		else:
			print('This title already exists')
	else:
		print('\nYour titles are:')
		for title in notes.get('titles'):
			print(title)
		break

# как вариант, можно сделать ввод заголовков
# через строку с разделителем вместо ввода друг за другом
# notes['titles'] = input('введите заголовки через запятую:').split(',')

print('\nNote data:')
# output all values from dictionary
for key, value in notes.items():
	# additional format of dates
	if type(value) == datetime:
		print(f'{key}: {value:%-d %b}')
		continue
	print(f'{key}: {value}')
	
