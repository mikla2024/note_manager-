import base64
import json
import requests

ACCESS_TOKEN = 'github_pat_11BNS6T2Q0xo1KfeeMGoYb_'\
'MSHe1i90jgk6uZBmZgztqZa2j3dH1slzMKYRiWzf8MH44UKWY7P9dXGQeud'

USERNAME = 'mikla2024'
REPO_NAME = 'note_manager-'
PATH = 'data.json'

def load_from_json_git():
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
            serv_byte_data = r.json().get('content') # base64 string
            serv_json = base64.b64decode(serv_byte_data) # base 64 bytes
            serv_res = json.loads(serv_json.decode('utf-8')) # json string
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

def save_to_json_git(json_content):

    try:

        r = requests.get(
        f'https://api.github.com/repos/{USERNAME}/'
        f'{REPO_NAME}/contents/{PATH}'
        )

        if r.status_code == 200:
            my_sha = r.json().get('sha')

        else:
            print("couldn't find a file'")
            return json_content

        json_str = json.dumps(json_content)
        byte_data = json_str.encode('utf-8')
        encoded_data = base64.b64encode(byte_data) # base64 bytes
        data_to_serv = encoded_data.decode(encoding='utf-8') # base64 string

        r = requests.put(
        f'https://api.github.com/repos/{USERNAME}/'
        f'{REPO_NAME}/contents/{PATH}',

        headers = {
        'Authorization': f'Token {ACCESS_TOKEN}'
        },

        json = {
        'message': 'update file by API',
        'content': data_to_serv,
        'sha': my_sha
        }
        )

        #print(r.status_code)
        if r.status_code == 200:
            print('\nall notes saved succesfully')
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