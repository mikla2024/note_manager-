import os
import sqlite3
from time import strptime

import interface
import json


def load_notes_from_db(db_path: str = '', io_table='notes',
                       my_cn: sqlite3.Connection = None):
    if not db_path:
        db_path = os.environ.get('db_path')

    if not my_cn:
        with sqlite3.connect(db_path) as cn:
            crsr = cn.cursor()
    else:
        crsr = my_cn.cursor()

    sql_str = f'SELECT * FROM {io_table}'

    crsr.execute(sql_str)
    rows = crsr.fetchall()

    my_list_notes = []
    for row in rows:
        my_list_notes.append({
            "id": int(row[0]),
            "username": row[1],
            "titles": json.loads(row[2]),
            "content": row[3],
            "status": row[4],
            "create_date": row[5],
            "issue_date": row[6]
        })

    return my_list_notes


if __name__ == '__main__':
    interface.f_print_all(load_notes_from_db(os.environ.get('db_path')))
