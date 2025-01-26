import SQLite_DB.database as db
from datetime import datetime as dt, timedelta
import interface as iface

def check_reminders():
    my_check_list = [a for a in db.load_notes_from_db()
                     if dt.strptime(a.get('issue_date'),'%d.%m.%Y') < dt.today()]
    print('\n**** Заметки с истекшим контрольным сроком: ****')
    iface.f_print_all(my_check_list)
    return my_check_list

if __name__ == '__main__':
    check_reminders()


