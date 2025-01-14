from interface import distrib_func

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

        my_list_notes = distrib_func(
        input('Ваш выбор: '), my_list_notes
        )

        continue