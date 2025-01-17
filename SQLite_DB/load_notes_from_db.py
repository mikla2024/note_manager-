import sqlite3
import interface
def load_notes_from_db(db_path: str):
    connection = sqlite3.connect('note_manager.db')
    crsr = connection.cursor()
    sql_str = str(
        'SELECT * FROM notes'
    )
    crsr.execute(sql_str)
    rows = crsr.fetchall()

    my_list_notes = []
    for row in rows:
        my_list_notes.append({
            'id':row[0],
            'username':row[1],
            'title':row[2],
            'content':row[3],
            'created_date':row[5],
            'issue_date':row[6]
            })
    connection.close()
    return my_list_notes

if __name__ == '__main__':
    interface.f_print_all(load_notes_from_db('note_manager.db'))