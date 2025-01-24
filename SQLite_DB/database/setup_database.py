import os.path
import sqlite3
import sys
import SQLite_DB.database as db
import data

path_db = os.environ.get('db_path')

try:
    with sqlite3.connect('..note_manager.db') as cn:
        cursor = cn.cursor()
        #sql_str = 'DROP TABLE notes'
        sql_str = (
            'CREATE TABLE IF NOT EXISTS notes ('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'username TEXT NOT NULL,'
            'titles TEXT NOT NULL,'
            'content TEXT NOT NULL,'
            'status TEXT NOT NULL,'
            'create_date TEXT NOT NULL,'
            'issue_date TEXT NOT NULL);')

        cursor.execute(sql_str)
        cn.commit()

        cursor.execute('SELECT * FROM notes')
        rows = cursor.fetchall()
except sqlite3.OperationalError as e:
    print(e)
    sys.exit(1)

if not rows:
    my_list = data.load_from_json_git()
    for n in my_list:
        db.save_note_to_db(note=n)
