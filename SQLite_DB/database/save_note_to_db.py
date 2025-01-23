import sqlite3
import json



def save_note_to_db(note: dict, db_path: str, io_table='notes', my_cn: sqlite3.Connection = None):
    if not my_cn:
        with sqlite3.connect(db_path) as cn:
            crsr = cn.cursor()
    else:
        crsr = my_cn.cursor()

    sql_str = (f'INSERT INTO {io_table} (username, title, content, status, '
                   'created_date, issue_date) '
                   f'VALUES (?, ?, ?, ?, ?, ?)',
               [note['username'], json.dumps(note['title'], ensure_ascii= False),
                note['content'], note['status'], note['created_date'],
                note['issue_date']
                ])

    crsr.execute(sql_str[0], sql_str[1])
    added_id = crsr.lastrowid if crsr.lastrowid else None
    crsr.connection.commit()

    return added_id


if __name__ == '__main__':
    note = {
        'username': 'mikla',
        'title': ['eggs', 'coffee', 'sugar'],
        'content': 'shopping_list',
        'status': 'in progress',
        'created_date': '17.01.2025',
        'issue_date': '28.02.2025'
    }
    note2 = {
        'username': 'miklka',
        'title': ['gym', 'learn math', 'classes'],
        'content': 'to do list',
        'status': 'in progress',
        'created_date': '17.01.2025',
        'issue_date': '31.01.2025'
    }
    my_list_notes = [note, note2]

    for note in my_list_notes:
        save_note_to_db(note, '../note_manager.db')