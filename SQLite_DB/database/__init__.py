from SQLite_DB.database.load_notes_from_db import load_notes_from_db
from SQLite_DB.database.save_note_to_db import save_note_to_db
from SQLite_DB.database.search_note_by_keyword import search_note_by_keyword, filter_notes_by_status
from SQLite_DB.database.update_note_in_db import update_note_in_db
from SQLite_DB.database.delete_note import delete_note_from_db
import os
from pathlib import Path
import sqlite3
import sys

os.environ['db_path'] = str(Path(__file__).resolve().parents[1]) + r'\note_manager.db'
os.environ['test_io_table'] = 'temp_notes'
os.environ['io_table'] = 'notes'

db_path = os.environ.get('db_path')

try:
    with sqlite3.connect(db_path) as cn:
        cursor = cn.cursor()
        # sql_str = 'DROP TABLE notes'
        sql_str = (
            'CREATE TABLE IF NOT EXISTS notes ('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'username TEXT NOT NULL,'
            'title TEXT NOT NULL,'
            'content TEXT NOT NULL,'
            'status TEXT NOT NULL,'
            'created_date TEXT NOT NULL,'
            'issue_date TEXT NOT NULL);')

        cursor.execute(sql_str)
        cn.commit()

        cursor.execute('SELECT * FROM notes')
        rows = cursor.fetchall()
        print('Соединение с БД установлено')
except sqlite3.OperationalError as e:
    print('Нет соединения с БД', e)
    sys.exit(1)

if not rows:
    import data
    my_list = data.load_from_json_git()
    for n in my_list:
        save_note_to_db(note=n, db_path=DB_PATH)
