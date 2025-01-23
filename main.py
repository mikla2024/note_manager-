
import interface as iface
import utils
import SQLite_DB.database as db



if __name__ == '__main__':

    print(
        '\nЗдравствуйте! Добро пожаловать в программу управления заметками! '
    )

    input('\nДля продолжения нажмите Enter...')
    my_list_notes = db.load_notes_from_db()
    if not my_list_notes:
        utils.handle_error('empty_list')

    # main menu endless cycle
    while True:
        iface.main_menu()
