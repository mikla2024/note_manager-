
import unittest
import SQLite_DB.database as db

class TestDB (unittest.TestCase):


    def test_add_and_load(self):

        db_path = r'C:\Users\BMW\PycharmProjects\note_manager-\SQLite_DB\note_manager.db'

        test_list = db.load_notes_from_db(db_path= db_path)


        test_note = {
            'username': 'test_name',
            'title': ['eggs', 'coffee', 'sugar'],
            'content': 'test_shopping_list',
            'status': 'Важно',
            'created_date': '17.01.2025',
            'issue_date': '28.02.2025'
        }
        global TEST_ID
        TEST_ID = db.save_note_to_db(note= test_note, db_path= db_path)
        test_note['id'] = TEST_ID

        test_list.append(test_note)
        new_test_list = db.load_notes_from_db(db_path)

        self.assertEqual(new_test_list, test_list)

    def test_delete_note(self):

        test_note = {
            'username': 'test_name',
            'title': ['eggs', 'coffee', 'sugar'],
            'content': 'test_shopping_list',
            'status': 'Важно',
            'created_date': '17.01.2025',
            'issue_date': '28.02.2025'
            }
        db_path = r'C:\Users\BMW\PycharmProjects\note_manager-\SQLite_DB\note_manager.db'
        test_list = db.load_notes_from_db(db_path)
        db.delete_note_from_db(TEST_ID, db_path= db_path)
        test_list.remove(test_note)
        new_test_list = db.load_notes_from_db(db_path)
        self.assertEqual(test_list, new_test_list)



if __name__ == '__main__':
    TEST_NOTE_ID = 0
    unittest.main()