from SQLite_DB.database.load_notes_from_db import load_notes_from_db
from SQLite_DB.database.save_note_to_db import save_note_to_db
from SQLite_DB.database.search_note_by_keyword import search_note_by_keyword, filter_notes_by_status
from SQLite_DB.database.update_note_in_db import update_note_in_db
from SQLite_DB.database.delete_note import delete_note_from_db
from SQLite_DB.database.setup_database import setup_database
import os
from pathlib import Path
import sqlite3
import sys

os.environ['db_path'] = str(Path(__file__).resolve().parents[1]) + r'\note_manager.db'
os.environ['test_io_table'] = 'temp_notes'
os.environ['io_table'] = 'notes'

try:
    setup_database()
    print('Соединение с БД установлено')
except sqlite3.OperationalError:
    print(
        'Программа не может получить доступ к БД '
        'и будет закрыта...')
    sys.exit(1)
