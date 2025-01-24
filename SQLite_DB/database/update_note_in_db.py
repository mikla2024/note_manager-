import sqlite3
import sys
import os
import json

def update_note_in_db(note_id: int, my_upd_d: dict, db_path: str = '', io_table='notes',
                      my_cn: sqlite3.Connection = None):
    if not db_path:
        db_path = os.environ.get('db_path')
    if not my_cn:
        with sqlite3.connect(db_path) as cn:
            crsr = cn.cursor()
    else:
        crsr = my_cn.cursor()

    sql_str = (
        f'SELECT * FROM {io_table} WHERE id = {note_id};'
    )

    crsr.execute(sql_str)
    row = crsr.fetchone()
    my_exist_d = {}

    my_exist_d['username'] = row[1]
    my_exist_d['titles'] = json.loads(row[2])
    my_exist_d['content'] = row[3]
    my_exist_d['status'] = row[4]
    my_exist_d['issue_date'] = row[6]

    try:
        updates = {k: v for k, v in my_exist_d.items() if not k in my_upd_d.keys()}
    except:
        print('Ошибка генератора словаря в модуле', __name__)
        sys.exit(1)
    my_upd_d.update(updates)

    sql_str = (
        f'UPDATE {io_table} '
        f'SET titles = ?, content = ?, status = ?, issue_date = ? '
        f'WHERE id = {note_id};', (json.dumps(my_upd_d.get('titles'), ensure_ascii=False), my_upd_d.get('content'),
                                   my_upd_d.get('status'), my_upd_d.get('issue_date'))
    )

    crsr.execute(sql_str[0], sql_str[1])
    crsr.connection.commit()


if __name__ == '__main__':
    upd_note = {
        'username': 'miklka',
        'titles': ['gym', 'learn math', 'classes'],
        'content': 'upd to do list',
        'status': 'in progress',
        'create_date': '17.01.2025',
        'issue_date': '15.02.2025'
    }
    update_note_in_db(note_id=3, my_upd_d=upd_note)
