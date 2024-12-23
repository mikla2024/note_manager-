# import classes 'datetime' from 'datetime' module
from datetime import datetime as dt, timedelta


# check unique title when add: if title exists returns False
def f_uni(list_, title_):
	if list_ is not None:
		if title_ in list_:
			return False
	return True


# dict. with notes
notes = {}
notes['username'] = input('Enter your name: ')
notes['content'] = input("Enter the note's content: ")
notes['status'] = input('Enter status: ')
notes['created_date'] = dt.today()
# check input date format and err handler
while True:
	user_date = input('Enter deadline in DD.MM.YYYY format '
		'---leave this field empty for default value (7 days from today---)')
	if user_date == '' :
		parsed_issue_date = dt.today() + timedelta(days=7)
		break
	else:
		try:
			parsed_issue_date = dt.strptime(user_date, '%d.%m.%Y')
			break
		except ValueError:
			print('Wrong date format, try one more time!')
			continue
notes['issue_date'] = parsed_issue_date

# user can input any amounts of titles or exit if press enter with empty field
while True:
	title_str = input('\nEnter title or leave this field empty '
										'if you complete your titles. '
										'To continue press Enter: ')
	if title_str != '':
		# check repetitive titles in function
		if f_uni(notes.get('titles'), title_str):
			# if key doesnt exist in dict it will be added as list
			notes.setdefault('titles', []).append(title_str)
			print(f'\n{notes.get("titles")} will be added')
		else:
			print('\nThe note with such title already exists!'
							' Titles should be unique')
	else:
		if notes.get('titles') is not None:
			break
		else:
			print("\nYou should choose at least one title...")

# как вариант, можно сделать ввод заголовков
# через строку с разделителем вместо ввода друг за другом
# notes['titles'] = input('введите заголовки через запятую:').split(',')

print('\nData you entered:')
# output all values from dictionary
for key, value in notes.items():
	# additional format of dates
	if type(value) == dt:
		print(f'***{key.capitalize()}: {value:%-d %b}')
		continue
	elif type(value) == list:
		print(f'***{key.capitalize()}: {", ".join(value)}')
		continue
	print(f'***{key.capitalize()}: {value}')
