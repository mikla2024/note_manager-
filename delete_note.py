# import classes 'datetime' from 'datetime' module
from datetime import datetime as dt, timedelta


# check unique title when add: if title exists returns False
def f_uni(list_title, title_):
	# check repetitive title in current note
	if list_title is not None:
		if title_ in list_title:
			return False
	# check repetitive title in another notes
	if list_notes is not None:
		for note_loc in list_notes:
			if title_ in note_loc.get('titles'):
				return False
	return True


# update current status.
def f_status_update(note):
	print(
		'\nChoose new status of your note then press Enter...:'
		'\n1. In progress \n2. Postponed \n3. Done'
		)
	while True:
		ans = input()
		if ans == '1':
			note['status'] = 'In progress'
			break
		elif ans == '2':
			note['status'] = 'Postponed'
			break
		elif ans == '3':
			note['status'] = 'Done'
			break
		else:
			print('Wrong status. Try one more time')
	
	print(
		f'\nStatus is updated. New status is: '
		f'{note.get("status").upper()}'
		)
	
	input("\nTo continue press Enter...")
	return True


# print all note's data' Arguments: note - dict
def f_print_note_data(note):
	print(f'\nNote #{note.get("note_id")}:')
	# output all values from dictionary
	for key, value in note.items():
		# additional format of dates
		
		if type(value) == dt:
			print(f'***{key.capitalize()}: {value:%-d %b}')
			continue
		
		elif type(value) == list:
			print(f'***{key.capitalize()}: {", ".join(value)}')
			continue
		
		print(f'***{key.capitalize()}: {value}')
	deadline_delta_days = f_deadline_check(note)
	
	if deadline_delta_days > 0:
		print(
			f'\nYou missed your deadline'
			f'{deadline_delta_days} days ago'
			)
	
	elif deadline_delta_days < 0:
		print(
			f'\nYour deadline is in '
			f'{str(deadline_delta_days)[1:]} days'
			)
	
	elif deadline_delta_days == 0:
		print('\nYour deadline is TODAY!!!')


# check how many days to deadline
def f_deadline_check(note):
	day_delta = dt.today() - note.get('issue_date')
	return day_delta.days


# make dict. with note
def f_add_new_note():
	my_id = len(list_notes) + 1
	note = {}
	note['note_id'] = my_id
	note['username'] = input('\nEnter your name: ')
	note['content'] = input("Enter the note's content: ")
	note['status'] = 'In progress'
	note['created_date'] = dt.today()
	
	# date parser and err handler
	while True:
		user_date = input(
			'Enter deadline in DD.MM.YYYY format '
			'---leave this field empty for default '
			'value (7 days from today---)'
			)
		if user_date == '':
			parsed_issue_date = dt.today() + timedelta(days=7)
			break
		else:
			try:
				parsed_issue_date = dt.strptime(user_date, '%d.%m.%Y')
				break
			except ValueError:
				print('Wrong date format, try one more time!')
				continue
	note['issue_date'] = parsed_issue_date

	# user can input any amounts of titles or exit if press enter with empty field
	while True:
		title_str = input(
			'\nEnter title or leave this field empty '
			'if you complete your titles. '
			'To continue press Enter: '
			)
		
		if title_str != '':
			# check repetitive titles in function
			
			if f_uni(note.get('titles'), title_str):
				# if key doesnt exist in dict it will be added as list
				note.setdefault('titles', []).append(title_str)
				print(f'\n{note.get("titles")} will be added')
			else:
				
				print(
					'\nThe note with such title already exists!'
					' Titles should be unique'
							)
		else:
			# doesn't allow add the note without at least one title'
			if note.get('titles') is not None:
				break
			else:
				print("\nYou should choose at least one title...")
	# output note's data
	f_print_note_data(note)
	# ask to change the status
	
	while True:
		choice = input(
			'\nDo you want to change the status of your '
			'note (yes/no)'
			).lower()
		
		if choice in ['yes', 'y'] and f_status_update(note):
			f_print_note_data(note)
			# break
		elif choice in ['no', 'n']:
			print('\nNote is added')
			break
		else:
			print('\nUnknown command, try more time...')
	return note


def f_del_note(my_list_notes, srch_str=None):
	i = 0  # amount of notes for delete
	if srch_str == '':
		print('\nYou should enter at least one key word')
		input('\nTo continue press Enter...')
		return
	# search user keyword in titles and other values of notes
	for my_note in my_list_notes:
		
		# search in dict.values regardless of capital letters
		if srch_str.lower() in [
			str(a).lower() for a in my_note.values()
			]:
			
			i += 1
			my_note.setdefault('del_flag', True)
		# search in titles
		
		elif srch_str.lower() in [
			str(a).lower() for a in my_note.get('titles')
			]:
			
			i += 1
			my_note.setdefault('del_flag', True)
	# if something is founded
	if i > 0:
		del_confrm = input(
			f'\n{i} notes will be deleted..Yes/No ').lower()
		if del_confrm in ['Yes', 'y']:
			
			new_list_notes = [
				a for a in my_list_notes if not (a.get('del_flag'))
				]
			
			print('\nThe choosen note(s) is(are) deleted')
			return new_list_notes
		elif del_confrm in ['No', 'n']:
			return my_list_notes
	print('\nThe note with such parameters can not be found')
	input('\nTo continue press Enter...')
	return


def f_print_all():
	print('\nYour notes:')
	for note in list_notes:
		f_print_note_data(note)
		print('*************************')


# make list with notes, every note as dict
list_notes = []
print('Hi there! Welcome to Note Manager!')
input('\nTo start your first note press Enter...')
list_notes.append(f_add_new_note())
f_print_all()

# dialog with options for delete or Add new notes
while True:
	if len(list_notes) > 0:
		
		choice = input(
			'\nIf you want to delete some notes '
			'press (D)el, to Add new press (A)dd'
			).lower()
		
		if choice in ['del', 'd']:
			del_str = input(
				'\nEnter username, note id or title of the note '
				'you want to delete...'
				)
			
			updt_list = f_del_note(list_notes, srch_str=del_str)
			
			if updt_list is not None:
				list_notes = updt_list
			
			if len(list_notes) > 0:
				f_print_all()
			
			else:
				print('\nAll notes deleted')
				continue
		
		elif choice in ['add', 'a']:
			list_notes.append(f_add_new_note())
			f_print_all()
		
		else:
			print('\nUnknown command, try more time...')
			continue
	
	else:
		choice = input('\nTo add new note press (A)dd').lower()
		
		if choice in ['a', 'add']:
			list_notes.append(f_add_new_note())
			f_print_all()
		else:
			print('\nUnknown command, try more time...')
			continue

