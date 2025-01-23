import sqlite3

with sqlite3.connect('../note_manager.db') as cn:
    cursor = cn.cursor()

cursor.execute(
    'CREATE TABLE IF NOT EXISTS notes ('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'username TEXT NOT NULL,'
    'title TEXT NOT NULL,'
    'content TEXT NOT NULL,'
    'status TEXT NOT NULL,'
    'created_date TEXT NOT NULL,'
    'issue_date TEXT NOT NULL);')

cn.commit()
