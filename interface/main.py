import sys
import data as d
import interface as iface

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

        my_list_notes = iface.distrib_func(
        input('Ваш выбор: '), my_list_notes
        )

        continue







if __name__ == '__main__':

    print(
        'Hi there! Welcome to Note Manager! '
        'For correct work you need connection to internet! '
        )

    input('\nTo start press Enter...')
    if (my_list_notes := d.get_json_cloud()) is None:
        while True:

            ans = input(
            '\nПрограмма не может получить доступ к серверу. Вы можете ' 'продолжить работать с локальной версией, при этом любые ' 'изменения не смогут быть сохранены. '
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
        main_menu(my_list_notes)