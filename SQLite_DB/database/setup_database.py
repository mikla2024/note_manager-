import os.path
import sqlite3
import SQLite_DB.database as db
import data




def setup_database():

    try:
        with sqlite3.connect(os.environ.get('db_path')) as cn:
            cursor = cn.cursor()
            # sql_str = 'DROP TABLE notes'
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
        raise sqlite3.OperationalError

    if not rows:
        my_list = data.load_from_json_git()
        for n in my_list:
            db.save_note_to_db(note=n)

    return True
