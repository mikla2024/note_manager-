import base64
import json
import requests

ACCESS_TOKEN = 'github_pat_11BNS6T2Q0xo1KfeeMGoYb_'\
'MSHe1i90jgk6uZBmZgztqZa2j3dH1slzMKYRiWzf8MH44UKWY7P9dXGQeud'

USERNAME = 'mikla2024'
REPO_NAME = 'note_manager-'
PATH = 'data.json'
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
