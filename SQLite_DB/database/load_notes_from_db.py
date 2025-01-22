import sqlite3
import interface
import json

def load_notes_from_db(db_path: str):
    with sqlite3.connect('../note_manager.db') as cn:
        crsr = cn.cursor()

    sql_str = 'SELECT * FROM notes'

    crsr.execute(sql_str)
    rows = crsr.fetchall()

    my_list_notes = []
    for row in rows:
        my_list_notes.append({
            "id": row[0],
            "username": row[1],
            "title": eval(row[2]),
            "content": row[3],
            "status": row[4],
            "created_date": row[5],
            "issue_date": row[6]
            })

    return my_list_notes

if __name__ == '__main__':
    interface.f_print_all(load_notes_from_db('../note_manager.db'))