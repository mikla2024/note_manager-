# import classes 'datetime' from 'datetime' module
from datetime import datetime as dt, timedelta
from copy import deepcopy
import json
import requests
import base64
import uuid
from requests.adapters import HTTPAdapter
import os
import sys
import colorama
from colorama import Fore, Back, Style, init
init(convert=True)


def f_update_note (my_list_notes, srch_str):

    if srch_str == '':
        print('\nВы ничего не выбрали')
        input('\nДля возврата в главное меню нажмите Enter...')
        print('заглушка для меню')
        sys.exit(1)

    # search user keyword in titles and other values of notes
    for my_note in my_list_notes:
        
        # search in dict.values regardless of capital letters
        x = [a.lower() for a in my_note.get('titles')]
        if srch_str in x:
            print('\nNote is found \n*********************')
            #f_print_note_data(my_note,0)
            
            while True:
                f_print_note_data(my_note, 0)
                
                print(
                    '\nВведите название поля для обновления, '
                    'или оставьте пустым для обновления нескольких '
                    'полей. Для возврата введите "X"')
                
                ans = input('Ваш выбор: ').lower()
                if ans == '':
                    x = [
                        a for a in my_list_notes
                        if a.get('note_id') != my_note.get('note_id')
                                    ]
                    my_note = f_add_new_note(x, my_note)

                    x.append(my_note)

                    return x
                
                elif ans == 'x':
                    return my_list_notes
                    
                
                else:
                    if ans in [a for a in my_note.keys()]:
                        x = [
                        a for a in my_list_notes
                        if a.get('note_id') != my_note.get('note_id')
                                    ]
                        my_note = f_add_new_note(x, my_note, ans)
                        x.append(my_note)
                    else:    
                        print('поле с таким названием не найдено...')
                        input('для продолжения нажмите Enter')
                        continue
        
    print('\nНичего не найдено. Поробуйте изменить поиск')
    input('\nДля продолжения нажмите Enter...')
        
    return my_list_notes

# ******************* end of update note ******************


# update current status.
def f_status_update(my_note):

    while True:
        ans = input(
        '\nChoose new status of your note then press Enter...:'
        '\n1. In progress'
        '\n2. Postponed'
        '\n3. Done'
                )
        if ans == '1':
            my_note['status'] = 'In progress'
            break
        elif ans == '2':
            my_note['status'] = 'Postponed'
            break
        elif ans == '3':
            my_note['status'] = 'Done'
            break
        else:
            print('Wrong status. Try one more time')

    print(f'\nStatus is updated. New status is: '
    f'{my_note.get("status").upper()}')
    input("\nTo continue press Enter...")
    return my_note
# ****************** end status update *************


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
# *********** end print note data *********************


def f_parser_date(date_str):
    while True:
        #user_date = input('Enter deadline in DD.MM.YYYY format '
        #'---leave this field empty for default '
        #'value (7 days from today---)')
        if date_str == '':
            parsed_issue_date = dt.today() + timedelta(days=7)
            break
        else:
            try:
                parsed_issue_date = dt.strptime(date_str, '%d.%m.%Y')
                break
            except ValueError:
                return False
    return parsed_issue_date.strftime('%d.%m.%Y')

#****************** end parser date ***********************


 # check how many days to deadline
def f_deadline_check(note):
    day_delta = dt.today() - \
    dt.strptime(note.get('issue_date'),'%d.%m.%Y')
    return day_delta.days


# make dict. with note
def f_add_new_note(my_list_notes, my_note=None, upd_key=None):

    if my_note is None:
        my_note={
                'note_id':'',
                'username':'mikla',
                'content':'',
                'status':'in progress',
                'create_date':dt.strftime(dt.today(),'%d.%m.%Y'),
                'issue_date':dt.strftime(
                    (dt.today()+timedelta(days=7)),'%d.%m.%Y'),
                'titles':[]
                }


    print(
            '\nПри вводе новых значений, если оставить '
            'поле пустым, запишется [значение по умолчанию]. '
            'Даты вводить в формате ДД.ММ.ГГГГ'
            )
    
    if upd_key is not None:
        upd_note = {
            k: v for k,v in my_note.items() if k == upd_key}
    else:
        upd_note = {
        	k: v for k,v in my_note.items()
        }
    
    for key, value in upd_note.items():
        #print(type(value))
        if not isinstance(value, list):

            if key == 'note_id':
                continue

            while True:
                if key == 'status':
                    user_value = f_status_update(my_note).get('status')

                else:
                    user_value = input(
                    f'\nEnter new value or leave the original one [{key}]: '
                    f'[{value}]...'
                    )

                if key in ['create_date', 'issue_date']:
                    new_value = f_parser_date(user_value)
                    if not new_value:
                        print(
                                'Неправильный формат даты, '
                                'попробуйте еще раз...'
                                )
                        continue

                if user_value == '':
                    new_value = value
                else:
                    new_value = user_value

                break

            # list of titles
        else:
            new_value=[]
            #print(len(new_value))
            while True:
                user_value = input(
                    f'\nEnter any amount of new titles.'
                    f'For finish leave field empty {new_value}: '
                                )

                if user_value not in [
                        a for n in my_list_notes if
                        isinstance(n,dict) for a in n.get('titles')
                        ] and \
                        user_value != '' and \
                        user_value not in new_value:

                    new_value.append(user_value)

                elif user_value == '' and len(new_value) > 0:
                    break

                else:
                    print('\n Item should be unique')
                    continue

        upd_note[key] = new_value
    # generator of random value
    upd_note['note_id'] = str(uuid.uuid4())
    
    for k,v in my_note.items():
        my_note[k] = upd_note.get(k,v)
    
    return my_note
# **************** end of add new_note ******************



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
            #print('*************************')
    return my_list_notes
# ******************** end f_print_all *******************

note1 = {
    'note_id':str(uuid.uuid4()),
    'username':'mikla',
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

my_list_notes = [note1,note2]

f_print_all(my_list_notes)

srch_str = input(
    '\n Укажите заголовок для поиска заметки '
    'для обновления...Оставьте поле пустым для возврата '
    'в главное меню...'
        ).lower()
        
my_list_notes =  f_update_note(
    my_list_notes, srch_str)

f_print_all(my_list_notes)

        
