import sys
import data as d
import interface as iface
import utils

if __name__ == '__main__':

    print(
        '\nЗдравствуйте! Добро пожаловать в программу управления заметками! '
        '\nДля нормальной работы необходимо подключение к интернет! '
        )

    input('\nTo start press Enter...')

    if (my_list_notes := d.load_from_json_git()) is None:
        while True:
            try:
                ans = input(
                '\nПрограмма не может получить доступ к серверу. Вы можете ' 
                'продолжить работать с локальной версией, при этом любые ' 
                'изменения не смогут быть сохранены. '
                'Желаете продолжить? \n(yes/no)... '
                )
                if ans.lower() in ['yes','y']:
                    online_mode = False
                    my_list_notes = []
                    break
                elif ans.lower() in ['no','n']:
                    sys.exit(0)
                else:
                    raise ValueError
            except ValueError:
                utils.handle_error('invalid_input')
            except:
                pass


    # main menu endless cycle
    while True:
        iface.main_menu(my_list_notes)