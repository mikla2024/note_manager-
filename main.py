import sys
import data as d
import interface as iface


if __name__ == '__main__':

    print(
        'Hi there! Welcome to Note Manager! '
        'For correct work you need connection to internet! '
        )

    input('\nTo start press Enter...')
    if (my_list_notes := d.load_from_json_git()) is None:
        while True:

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
                print('Неизвестная команда, попробуйте еще раз')
                continue

    # main menu endless cycle
    while True:
        iface.main_menu(my_list_notes)