import base64
import json

import requests

ACCESS_TOKEN = 'github_pat_11BNS6T2Q0xo1KfeeMGoYb_'\
'MSHe1i90jgk6uZBmZgztqZa2j3dH1slzMKYRiWzf8MH44UKWY7P9dXGQeud'

USERNAME = 'mikla2024'
REPO_NAME = 'note_manager-'
PATH = 'data'
CACHE_LIST=[]


def check_sha(filename='data.json'):
    try:

        r = requests.get(
        f'https://api.github.com/repos/{USERNAME}/'
        f'{REPO_NAME}/contents/{PATH}/{filename}'
        )

        if r.status_code == 200:
            return r.json().get('sha')

        else:
            return ''
    except:
        pass

def load_from_json_git(filename='data.json'):

    if len(CACHE_LIST) > 0:
        return CACHE_LIST

    try:
        # check internet connection
        url = 'http://google.com'
        r = requests.head(url,timeout=4)

        r = requests.get(
        f'https://api.github.com/repos/{USERNAME}/'
        f'{REPO_NAME}/contents/{PATH}/{filename}'
        )

        if r.status_code == 200:

            serv_byte_data = r.json().get('content') # base64 string
            serv_json = base64.b64decode(serv_byte_data) # base 64 bytes
            serv_res = json.loads(serv_json.decode('utf-8')) # json string
            print('connection established...')
            return serv_res

        elif r.status_code == 404:
            print('Файл с заметками не найден. Файл будет создан при '
                  'следующем сохранении ')
            return []

        else:
            print('\nconnection status: ', r.status_code)
            input()
            return None

    except requests.RequestException as e:
        print(e)
        print ('\nno internet connection')
        input('Press any key...')
        return None
# **************** end of json get ************************

def save_to_json_git(json_content,filename='data.json'):

    global CACHE_LIST
    json_str = json.dumps(json_content)
    byte_data = json_str.encode('utf-8')
    encoded_data = base64.b64encode(byte_data) # base64 bytes
    data_to_serv = encoded_data.decode(encoding='utf-8') # base64 string

    try:
        r = requests.put(
        f'https://api.github.com/repos/{USERNAME}/'
        f'{REPO_NAME}/contents/{PATH}/{filename}',

        headers = {
        'Authorization': f'Token {ACCESS_TOKEN}'
        },

        json = {
        'message': 'update file by API',
        'content': data_to_serv,
        'sha': check_sha(filename)
        }
        )

        #print(r.status_code)
        if r.status_code == 200:
            print('\nall notes saved successfully')
            input('press Enter to continue...')
            #json_content.append({'sha': r.json().get('content').get('sha')})
            CACHE_LIST = [a for a in json_content]
            return json_content

        elif r.status_code == 201:
            print('new file is created')
            input('press enter... ')
            json_content.append({'sha': r.json().get('content').get('sha')})
            CACHE_LIST = [a for a in json_content]
            return json_content
        else:
            print(f'something went wrong, code = {r.status_code}')
            input('press Enter....')
            CACHE_LIST = [a for a in json_content]
            return json_content


    except requests.RequestException as e:
            #print(e)
        print ('\nsavings is fail')
        input('Press any key...')
        return json_content

# test_list = [{'username':'test3'},{'content':'test'}]
# save_to_json_git(test_list,'raw_test.json')