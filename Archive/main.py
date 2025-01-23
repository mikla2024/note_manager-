import sys
import data as d
import interface as iface
import utils
import SQLite_DB.database as db

if __name__ == '__main__':

    if (db.load_notes_from_db()) is None:
        while True:
            try:
                ans = input(
                    '\nПрограмма не может получить доступ к серверу. Вы можете '
                    'продолжить работать с локальной версией, при этом любые '
                    'изменения не смогут быть сохранены. '
                    'Желаете продолжить? \n(yes/no)... '
                )
                if ans.lower() in ['yes', 'y']:
                    online_mode = False
                    my_list_notes = []
                    break
                elif ans.lower() in ['no', 'n']:
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
