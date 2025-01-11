# import classes 'datetime' from 'datetime' module
from datetime import datetime as dt, timedelta
import uuid
import sys

    # print all note's data'
def f_print_note_data(my_note, my_count):
    print(f'\nNote #{my_count+1}:')
    # output all values from dictionary
    for key, value in my_note.items():
        # additional format of dates
        if key == 'created_date' or key == 'issue_date':
            print(f'***{key.capitalize()}: '
            f'{dt.strptime(value,"%d.%m.%Y").strftime("%d %b")}')
            continue
        elif type(value) == list:
            print(f'***{key.capitalize()}: {", ".join(value)}')
            continue
        elif key == 'note_id':
            continue
        print(f'***{key.capitalize()}: {value}')
    deadline_delta_days = f_deadline_check(my_note)
    if deadline_delta_days > 0:
        print(
            f'\nYou missed your deadline '
            f'{deadline_delta_days} days ago')
    elif deadline_delta_days < 0:
        print(f'\nYour deadline is in '
        f'{str(deadline_delta_days)[1:]} days')
    elif deadline_delta_days == 0:
        print('\nYour deadline is TODAY!!!')
    print ('****************************')


# check how many days to deadline
def f_deadline_check(note):
    day_delta = dt.today() - \
    dt.strptime(note.get('issue_date'),'%d.%m.%Y')
    return day_delta.days 


def f_print_all(my_list_notes):
    print('\nYour notes:')
    if my_list_notes is None or len(my_list_notes) == 0:
        print(
        	'There is no notes yet. But you can '
        	'always add some...')
        my_list_notes = f_empty_list()
    for index_, note in enumerate(my_list_notes):
        if isinstance(note, dict) :
            f_print_note_data(note, index_)

# ******************** end f_print_all *******************

def search_note(my_list_notes, srch_str, srch_status):
    
    
    
    if srch_str == '' and srch_status != '':
        	  
        found_list_notes = [a for a in my_list_notes
            if a.get('status')==srch_status] 
            
        return found_list_notes   
        
    found_list_notes = []
        
    for my_note in my_list_notes:           
            
        if srch_str in [a for a in 
            {k:v for k,v in my_note.items() 
                     if k!='status'}.values() ] or \
           srch_str in [a for b in my_note.values() for
               	a in b if type(b)==list]:
               
            found_list_notes.append(my_note)

    if len(found_list_notes) > 0 and srch_status != '':
        found_list_notes = [a for a in found_list_notes if a.get('status') == srch_status]
            
    return found_list_notes


note1 = {
    'note_id':str(uuid.uuid4()),
    'username':'amikla',
    'content':'grocery list',
    'status':'in progress',
    'created_date':dt.strftime(dt.today(),'%d.%m.%Y'),
    'issue_date':dt.strftime(
        (dt.today()+timedelta(days=7)),'%d.%m.%Y'),
     'titles':['bread','butter','sugar']
                }
                
note2 = {
     'note_id':str(uuid.uuid4()),
    'username':'mikla',
    'content':'list to do',
    'status':'in progress',
    'created_date':dt.strftime(dt.today(),'%d.%m.%Y'),
    'issue_date':dt.strftime(
        (dt.today()+timedelta(days=7)),'%d.%m.%Y'),
     'titles':['learn math','english classes','gym']
           }
note3 = {
     'note_id':str(uuid.uuid4()),
    'username':'mikla',
    'content':'workshop',
    'status':'done',
    'created_date':dt.strftime(dt.today(),'%d.%m.%Y'),
    'issue_date':dt.strftime(
        (dt.today()+timedelta(days=7)),'%d.%m.%Y'),
     'titles':['tool','switch','screw']
           }


my_list_notes = [note1,note2,note3]

f_print_all(my_list_notes)

srch_str = input(
    '\n Укажите заголовок или имя '
    'пользователя для поиска заметки ').lower()
srch_status = input(
	'\nВведите статус для поиска ' 
  '(или оставьте пустым): ').lower()
                  
if srch_str == '' and srch_status == '':
    print(
        'Вы ничего не выбрали и будете '
        'перенаправлены в главное меню...')
    sys.exit(1)

my_list_notes =  search_note(
    my_list_notes, srch_str, srch_status)
    
if len(my_list_notes) > 0: 
    print(f'\nНайдено заметок: {len(my_list_notes)}')
    f_print_all(my_list_notes)              
else:
    print(
        '\nНичего не нашлось, попробуйте '
        'поискать с другими параметрами...')



        
