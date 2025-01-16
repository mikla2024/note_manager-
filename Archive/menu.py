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


ACCESS_TOKEN = 'github_pat_11BNS6T2Q0xo1KfeeMGoYb_'\
'MSHe1i90jgk6uZBmZgztqZa2j3dH1slzMKYRiWzf8MH44UKWY7P9dXGQeud'

USERNAME = 'mikla2024'
REPO_NAME = 'note_manager-'
PATH = 'data/data.json'
sha_put = ''
sha_get = ''


def get_json_cloud():
    try:
        # check internet connection
        url = 'http://google.com'
        r = requests.head(url,timeout=4)

        r = requests.get(
        f'https://api.github.com/repos/{USERNAME}/'
        f'{REPO_NAME}/contents/{PATH}'
        )

        if r.status_code == 200:
            sha_get = r.json().get('sha')
            serv_byte_data = r.json().get('content')
            serv_json = base64.b64decode(serv_byte_data)
            serv_res = json.loads(serv_json.decode('utf-8'))
            print('connection established...')
            return serv_res
        else:
            print('\nconnection status: ', r.status_code)
            input()
            return None

    except requests.RequestException as e:
        #print(e)
        print ('\nno internet connection')
        input('Press any key...')
        return None
# **************** end of json get ************************

def update_json_git(json_content):

    try:

        r = requests.get(
        f'https://api.github.com/repos/{USERNAME}/'
        f'{REPO_NAME}/contents/{PATH}'
        )

        #print(r.status_code)

        if r.status_code == 200:
            my_sha = r.json().get('sha')
            serv_byte_data = r.json().get('content')
            serv_json = base64.b64decode(serv_byte_data)
            serv_res = json.loads(serv_json.decode('utf-8'))
            # print('\nnew file downloaded')

        else:
            print("couldn't find a file'")
            return json_content

        data_to_server = json_content
        json_str = json.dumps(data_to_server)
        byte_data = json_str.encode('utf-8')
        encoded_data = base64.b64encode(byte_data)

        r = requests.put(
        f'https://api.github.com/repos/{USERNAME}/'
        f'{REPO_NAME}/contents/{PATH}',

        headers = {
        'Authorization': f'Token {ACCESS_TOKEN}'
        },

        json = {
        'message': 'update file by API',
        'content': encoded_data.decode(),
        'sha': my_sha
        }
        )

        #print(r.status_code)
        if r.status_code == 200:
            print('\nall notes saved succesfully')
            #print(f'\nold_sha: {my_sha}')
            #print(f'\nupd_sha: {r.json().get("content").get("sha")}')

            #for k,v in r.json().items():

                    #print(f'\n{k}: {v}')
                    #print('***********************')
            input('press Enter to continue...')
            return json_content

        else:
            print('savings is fail')
            input('press Enter....')
            return json_content


    except requests.RequestException as e:
            #print(e)
        print ('\nno internet connection')
        input('Press any key...')
        return json_content
# ***************** end json git update ****************


# check unique title when add: if title exists returns False
'''
def f_uni(my_list_notes, my_list_title, srch_str):
    # check repetitive title in current note
    if my_list_title is not None:
        if srch_str in my_list_title:
            return False
    # check repetitive title in another notes
    if my_list_notes is not None:
        for v in my_list_notes:
            if srch_str in v.get('titles'):
                return False
    return True
'''

# update current status.
def f_status_update(my_note):

    while True:
        print(
        '\nChoose new status of your note then press Enter...:'
        '\n1. In progress'
        '\n2. Postponed'
        '\n3. Done'
                )
        ans = input('Ваш выбор: ')
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
    print('******************************')
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
                'issue_date':dt.strftime((dt.today()+timedelta(days=7)),'%d.%m.%Y'),
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
                    f'\nEnter any amount of new titles. '
                    f'For finish leave field empty {new_value}: '
                                )

                # if user_value not in [
                #         a for n in my_list_notes if
                #         isinstance(n,dict) for a in n.get('titles')
                #         ] and \
                if user_value != '' and \
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

def f_del_note(my_list_notes, srch_str = None):

    i = 0  # amount of notes for delete

    if srch_str == '':
        print('\nВы ничего не выбрали')
        input('\nДля возврата в главное меню нажмите Enter...')
        return my_list_notes

    # search user keyword in titles and other values of notes
    for my_note in my_list_notes:
        # search in dict.values regardless of capital letters
        if srch_str.lower() in [str(a).lower() for a in my_note.values()]:
            i += 1
            my_note.setdefault('del_flag', True)
        # search in titles
        elif srch_str.lower() in [str(a).lower() for a in
        my_note.get('titles')]:
            i += 1
            my_note.setdefault('del_flag', True)
    # if something is founded
    if i > 0:

        while True:
            del_confrm = input(
                    f'\n{i} notes will be deleted..Yes/No ').lower()

            if del_confrm in ['yes', 'y']:
                new_list_notes=[a for a in my_list_notes
                if not (a.get('del_flag'))]
                print('\nThe choosen note(s) is(are) deleted')
                return new_list_notes

            elif del_confrm in ['no', 'n']:
                new_list_notes = []
                for d in my_list_notes:
                    d.pop('del_flag', None)
                    new_list_notes.append(d)
                return new_list_notes

            else:
                print('Неизвестная команда. Попробуйте еще раз...')
                continue

    print('\nThe note with such parameters can not be found')
    input('\nTo continue press Enter...')
    return my_list_notes
# ******************* end of del_note *********************


def f_update_note (my_list_notes, srch_str):

    
    
    if srch_str == '':
        print('\nВы ничего не выбрали')
        input('\nДля возврата в главное меню нажмите Enter...')
        return my_list_notes

    
    # search user keyword in titles and other values of notes
    for my_note in my_list_notes:
        
        # search in titles
        x = [a.lower() for a in my_note.get('titles')]
        if srch_str in x:
            print('\nNote is found \n*********************')
            
            
            while True:
                f_print_note_data(my_note, 0)
                
                print(
                    '\nВведите название поля для обновления, '
                    'или оставьте пустым для обновления нескольких '
                    'полей. Для возврата введите "X"')
                # choosing the key for update
                ans = input('Ваш выбор: ').lower()
                if ans == '':
                    new_list = [
                        a for a in my_list_notes
                        if a.get('note_id') != my_note.get('note_id')
                                    ]
                    my_note = f_add_new_note(new_list, my_note)

                    new_list.append(my_note)
                    return new_list
                
                elif ans == 'x':
                    return my_list_notes
                    
                
                else:
                    # if key is found
                    if ans in [a for a in my_note.keys()]:
                        new_list = [
                            a for a in my_list_notes 
                            if a.get('note_id') !=
                            my_note.get('note_id')  
                                    ]
                        my_note = f_add_new_note(
                            new_list, my_note, ans)
                        
                        new_list.append(my_note)
                        return new_list
                    # key is not found
                    else:    
                        print('\nполе с таким названием не найдено...')
                        input('для продолжения нажмите Enter')
                        continue
        
    print('\nНичего не найдено. Поробуйте изменить поиск')
    input('\nДля продолжения нажмите Enter...')
        
        
    return my_list_notes

# ******************* end of update note ******************

def search_note(my_list_notes,srch_str,srch_status):
    
    if srch_str == '' and srch_status == '':
        print(
            '\nВы ничего не выбрали и будете '
            'перенаправлены в главное меню. '
            'Нажмите Enter для продолжения...')
        input()
        main_menu(my_list_notes)
    
    elif srch_str == '' and srch_status != '':
        	  
        found_list_notes = [a for a in my_list_notes
            if a.get('status')==srch_status] 
            
        return found_list_notes   
        
    found_list_notes = []
        
    for my_note in my_list_notes:           
            
        if srch_str in [a for a in 
            {k:v.lower() for k,v in my_note.items() 
                     if k!='status' and type(v)!=list}.values() ] or \
             srch_str in [a.lower() for b in my_note.values() for
               	a in b if type(b)==list]:
               
            found_list_notes.append(my_note)

    if len(found_list_notes) > 0 and srch_status != '':
        
        found_list_notes = [a for a in found_list_notes if str(a.get('status')).lower() == srch_status]
            
    return found_list_notes
# ****************** end search note **********************

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


def save_chg_cloud(my_list_note):
    while True:

        ans = input('Do you want to sync changes with cloud'
                    '---(y/n)...').lower()

        if ans.lower() in ['y','yes']:
            new_list = update_json_git(my_list_note)
            return new_list

        elif ans in ['n','no']:
            return my_list_note
        else:
            print('\nUnknown command, try more time...')
            continue  # saving notes dialog
    return False
# ******************* end of save_chd_cloud *************


def f_empty_list():

    my_list_notes = []
    
    while True:
        ans = input(
        	'\nTo add new note press (A)dd '
          'or press e(X)it...').lower()
        
        if ans.lower() in ['a', 'add']:
            my_list_notes.append(f_add_new_note(my_list_notes))
            f_print_all(my_list_notes)

        elif ans.lower() in ['x', 'exit']:
            main_menu(my_list_notes)
            #return my_list_notes
        else:
            print('Command is unknown')
            continue
# ***************** end of empty list *********************


def context_menu(my_list_notes):
    while True:

        choice = input(
        '\nIf you want to delete some notes '
        'press (D)el, to Add new press (A)dd'
        '\nFor exit to main menu press X...').lower()

        if choice in ['del', 'd']:
            del_str = input(
            '\nEnter username or title of the note '
            'you want to delete...'
            )
            my_list_notes = f_del_note(
                my_list_notes, srch_str=del_str)
            f_print_all(my_list_notes)
            continue

        elif choice in ['add', 'a']:
            my_list_notes.append(
                f_add_new_note(my_list_notes))
            f_print_all(my_list_notes)
            continue

        elif choice in ['x','exit']:
            
            return my_list_notes
        
        else:
            print('\nUnknown command, try more time...')
            continue
#   ******************** end of context menu *************


def main_menu(my_list_notes=None):

    if my_list_notes is None:
        my_list_notes=[]

    while True:
        print('''

Меню действий:

1. Создать новую заметку

2. Показать все заметки

3. Обновить заметку

4. Удалить заметку

5. Найти заметки

6. Выйти из программы

''')

        my_list_notes = main_module(
        input('Ваш выбор: '), my_list_notes
        )

        continue
# *********** end of MAIN menu ***************


def main_module(my_choice, list_notes_local):

    my_list_notes = deepcopy(list_notes_local)
    #show all notes

    if my_list_notes is None or len(my_list_notes) == 0:
             my_list_notes = f_empty_list()
    
    # show all
    if my_choice == '2':

        f_print_all(my_list_notes)

        my_list_notes = context_menu(my_list_notes)

        if my_list_notes != list_notes_local:
            list_notes_local = save_chg_cloud(my_list_notes)

        return list_notes_local

    # create new
    if my_choice == '1':

        print('\nStart new note')
        my_list_notes.append(
            f_add_new_note(my_list_notes))

        if my_list_notes != list_notes_local:
            list_notes_local = save_chg_cloud(my_list_notes)


        return list_notes_local

    # update
    if my_choice == '3':

        f_print_all(my_list_notes)
        print(
            '\n Укажите заголовок для поиска заметки '
            'для обновления. Оставьте поле пустым для возврата '
            'в главное меню...')
        
        srch_str = input('Ваш выбор: ').lower()
        
       
        
        my_list_notes =  f_update_note(
            my_list_notes, srch_str)

        f_print_all(my_list_notes)

        if my_list_notes != list_notes_local:
            list_notes_local = save_chg_cloud(my_list_notes)

        return list_notes_local

    # delete
    if my_choice == '4':

        f_print_all(my_list_notes)

        print(
            '\n Укажите заголовок или имя пользователя '
            'для поиска заметки для удаления... '
            'Оставьте поле пустым для возврата '
            'в главное меню')
        
        srch_str = input('\nВаш выбор: ').lower()
        
        my_list_notes =  f_del_note(
            my_list_notes, srch_str)

        f_print_all(my_list_notes)

        if my_list_notes != list_notes_local and \
        online_mode:
            list_notes_local = save_chg_cloud(my_list_notes)

        return list_notes_local

    
    # search
    if my_choice == '5':
        
        srch_str = input(
             '\n Укажите заголовок для поиска заметки '
             'для обновления... Оставьте поле пустым для возврата '
             'в главное меню...').lower()
             
        srch_status = input(
	          '\nВведите статус для поиска ' 
            '(или оставьте пустым): ').lower()
                  
         
        found_list_notes = search_note(
            my_list_notes, srch_str, srch_status)
             
        if len(found_list_notes) > 0:
            f_print_all(found_list_notes)
            my_list_notes = context_menu(my_list_notes)
        else:
            print(
                '\nПохоже, что ничего не нашлось. '
                'Постарайтесь изменить параметры поиска. '
                'Для продолжения нажмите Enter...')
            input()
        if my_list_notes != list_notes_local:
            list_notes_local = save_chg_cloud(my_list_notes)

    if my_choice == '6':
        sys.exit(1)

    return list_notes_local
# ************* end of main module***************


# ************* Enter to programm **************
print(
    'Hi there! Welcome to Note Manager! '
    'For correct work you need connection to internet! '
    )
input('\nTo start press Enter...')
if (my_list_notes := get_json_cloud()) is None:
    while True:

        ans = input(
        '\nПрограмма не может получить доступ к серверу. Вы можете ' 'продолжить работать с локальной версией, при этом любые ' 'изменения не смогут быть сохранены. '
        'Желаете продолжить? \n(yes/no)...'
        )
        if ans.lower() in ['yes','y']:
            online_mode = False
            my_list_notes = []
            break
        elif ans.lower() in ['no','n']:
            sys.exit(1)
        else:
            print('Неизвестная команда, попробуйте еще раз')
            continue

# main menu endless cycle
while True:
    main_menu(my_list_notes)
