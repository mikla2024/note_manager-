import sqlite3



def update_note_in_db(note_id:int, updates: dict, db_path: str):

    with sqlite3.connect(db_path) as cn:
        crsr = cn.cursor()

    sql_str = (
        'UPDATE notes '
        f'SET title = "{updates['title']}", content = "{updates['content']}", '
        f'status = "{updates['status']}", issue_date = "{updates['issue_date']}" '
        f'WHERE id = {note_id};'
    )

    crsr.execute(sql_str)
    cn.commit()


if __name__ == '__main__':

    upd_note = {
        'username': 'miklka',
        'title': ['gym', 'learn math', 'classes'],
        'content': 'upd to do list',
        'status': 'in progress',
        'created_date': '17.01.2025',
        'issue_date': '15.02.2025'
    }
    update_note_in_db(note_id= 3, updates= upd_note, db_path='../note_manager.db')