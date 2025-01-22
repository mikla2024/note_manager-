import sqlite3




def save_note_to_db(note: dict, db_path: str):

    with sqlite3.connect(db_path) as cn:
        crsr = cn.cursor()

    sql_str = str('INSERT INTO notes (username, title, content, status, '
                   'created_date, issue_date) '
                   f'VALUES ("{note['username']}", "{note['title']}", '
                   f'"{note['content']}", "{note['status']}", "{note['created_date']}", '
                   f'"{note['issue_date']}");'
                  )


    crsr.execute(sql_str)
    added_id = crsr.lastrowid if crsr.lastrowid else None

    cn.commit()
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