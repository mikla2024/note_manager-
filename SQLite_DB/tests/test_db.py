import unittest

from SQLite_DB.database.load_notes_from_db import load_notes_from_db
from SQLite_DB.database.save_note_to_db import save_note_to_db
from data import f_add_new_note


class test_db (unittest.TestCase):


    def test_add_and_load(self):

        db_path = 'C:\\Users\BMW\PycharmProjects\\note_manager-\SQLite_DB\\note_manager.db'
        test_list = load_notes_from_db(db_path= db_path)


        test_note = {
        'username': 'test_name',
        'title': ['eggs', 'coffee', 'sugar'],
        'content': 'test_shopping_list',
        'status': 'Важно',
        'created_date': '17.01.2025',
        'issue_date': '28.02.2025'
        }

        save_note_to_db(note= test_note, db_path= db_path)

        self.assertEqual(load_notes_from_db(db_path), test_list.append(test_note))

if __name__ == '__main__':
    unittest.main()