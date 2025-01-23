from SQLite_DB.database.load_notes_from_db import load_notes_from_db
from SQLite_DB.database.save_note_to_db import save_note_to_db
from SQLite_DB.database.search_note_by_keyword import search_note_by_keyword, filter_notes_by_status
from SQLite_DB.database.update_note_in_db import update_note_in_db
from SQLite_DB.database.delete_note import delete_note_from_db
import os

os.environ['db_path'] = r'C:\Users\BMW\PycharmProjects\note_manager-\SQLite_DB\note_manager.db'
os.environ['test_io_table'] = 'temp_notes'
os.environ['work_table'] = 'notes'
