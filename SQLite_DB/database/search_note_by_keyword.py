import sqlite3
import interface


def search_note_by_keyword (keyword: str, db_path: str):
    with sqlite3.connect(db_path) as cn:
        crsr = cn.cursor()

    sql_str = (
        'SELECT * FROM notes '
        f'WHERE title LIKE "%{keyword}%" '
        f'OR content LIKE "%{keyword}%";'
    )

    crsr.execute(sql_str)
    rows = crsr.fetchall()
    my_list_notes = []
    for r in rows:
        my_list_notes.append({
            'id': r[0],
            'username': r[1],
            'title': r[2],
            'content': r[3],
            'created_date': r[5],
            'issue_date': r[6]
        })
    return my_list_notes

def filter_notes_by_status(status, db_path):
    with sqlite3.connect(db_path) as cn:
        crsr = cn.cursor()
    sql_str = (
               'SELECT * FROM notes '
               f'WHERE status = "{status}"; '
    )
    crsr.execute(sql_str)
    rows = crsr.fetchall()
    my_list_notes = []
    for r in rows:
        my_list_notes.append({
            'id': r[0],
            'username': r[1],
            'title': r[2],
            'content': r[3],
            'created_date': r[5],
            'issue_date': r[6]
        })
    return my_list_notes

if __name__ == '__main__':

    keyword = input('Введите ключевое слово для поиска: ')
    list_notes = search_note_by_keyword(keyword, '../note_manager.db')
    interface.f_print_all(list_notes)
    input('для продолжения Enter...')
    status = input('Введите статус для поиска: ')
    list_notes = filter_notes_by_status('in progress', '../note_manager.db')
    interface.f_print_all(list_notes)