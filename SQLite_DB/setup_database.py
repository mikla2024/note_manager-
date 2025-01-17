import sqlite3

connection = sqlite3.connect('note_manager.db')
cursor = connection.cursor()

cursor.execute(
               'CREATE TABLE IF NOT EXISTS notes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'username TEXT NOT NULL,'
               'title TEXT NOT NULL,'
               'content TEXT NOT NULL,'
               'status TEXT NOT NULL,'
               'created_date TEXT NOT NULL,'
               'issue_date TEXT NOT NULL);')

connection.commit()
connection.close()

