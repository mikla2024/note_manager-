import json
import os
import unittest
import SQLite_DB.database as db

DB_PATH = r'C:\Users\BMW\PycharmProjects\note_manager-\SQLite_DB\note_manager.db'
TEST_NOTE =   {
            'username': 'test_name',
            'title': ['eggs', 'coffee', 'sugar'],
            'content': 'test_shopping_list',
            'status': 'Важно',
            'created_date': '17.01.2025',
            'issue_date': '28.02.2025'
        }
TEST_ID = 0

class TestDB (unittest.TestCase):



    def test_a_add_and_load(self):
        global TEST_NOTE
        global TEST_ID


        test_list = db.load_notes_from_db(db_path= DB_PATH)

        TEST_ID = db.save_note_to_db(note= TEST_NOTE, db_path= DB_PATH, db_table='temp')

        TEST_NOTE['id'] = TEST_ID

        test_list.append(TEST_NOTE)
        new_test_list = db.load_notes_from_db(DB_PATH)

        self.assertEqual(new_test_list, test_list)

    def test_b_search_note(self):

        self.assertEqual(db.search_note_by_keyword('test_shopping_list', db_path= DB_PATH),
                         [TEST_NOTE])


    def test_c_update_note(self):


        upd_dict = {'Status': 'test'}
        db.update_note_in_db(TEST_ID, upd_dict, DB_PATH)

        self.assertEqual(db.filter_notes_by_status('test', DB_PATH), [TEST_NOTE])


    def test_d_delete_note(self):


        db_path = r'C:\Users\BMW\PycharmProjects\note_manager-\SQLite_DB\note_manager.db'
        test_list = db.load_notes_from_db(DB_PATH)
        db.delete_note_from_db(TEST_ID, db_path= DB_PATH)
        test_list.remove(TEST_NOTE)
        new_test_list = db.load_notes_from_db(DB_PATH)
        self.assertEqual(test_list, new_test_list)






if __name__ == '__main__':
    TEST_ID = 0
    unittest.main()