import os
import sqlite3
import unittest
from copy import deepcopy

import SQLite_DB.database as db

TEST_ID = 0

TEST_NOTE = {
    'id': 1,
    'username': 'test_name',
    'title': ['one', 'two', 'three'],
    'content': 'test_shopping_list',
    'status': 'Важно',
    'created_date': '17.01.2025',
    'issue_date': '28.02.2025'
}

TEST_NOTE2 = {
    'id': 2,
    'username': 'test_name2',
    'title': ['three', 'four', 'five'],
    'content': 'test_content',
    'status': 'Выполнено',
    'created_date': '17.01.2025',
    'issue_date': '28.02.2025'
}

TEST_LIST_NOTES = [TEST_NOTE, TEST_NOTE2]
DB_PATH = os.environ.get('db_path')
IO_TABLE = os.environ.get('test_io_table')


class TestDB(unittest.TestCase):

    def test_add_and_load(self):
        with sqlite3.connect(DB_PATH) as cn:
            create_tmp_table(cn)
            self.assertEqual(
                db.load_notes_from_db(DB_PATH, IO_TABLE, cn), TEST_LIST_NOTES)

    def test_search_note(self):
        with sqlite3.connect(DB_PATH) as cn:
            create_tmp_table(cn)
            self.assertEqual(
                db.search_note_by_keyword('test_content', DB_PATH, IO_TABLE, cn),
                [TEST_NOTE2])

    def test_c_update_note(self):
        upd_dict = {'status': 'test', }
        with sqlite3.connect(DB_PATH) as cn:
            create_tmp_table(cn)
            db.update_note_in_db(1, upd_dict, DB_PATH, io_table=IO_TABLE, my_cn=cn)
            assert_note = deepcopy(TEST_NOTE)
            assert_note['status'] = 'test'

            list_for_assert = db.filter_notes_by_status('test', DB_PATH, IO_TABLE, cn)
            self.assertEqual(list_for_assert, [assert_note])

    def test_d_delete_note(self):
        with sqlite3.connect(DB_PATH) as cn:
            create_tmp_table(cn)
            db.delete_note_from_db(2, db_path=DB_PATH, io_table=IO_TABLE, my_cn=cn)

            self.assertEqual(db.load_notes_from_db(DB_PATH, IO_TABLE, cn), [TEST_NOTE])


def create_tmp_table(my_cn: sqlite3.Connection):
    my_sql_str = (f'CREATE TEMPORARY TABLE {IO_TABLE} ('
                  'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                  'username TEXT NOT NULL,'
                  'title TEXT NOT NULL,'
                  'content TEXT NOT NULL,'
                  'status TEXT NOT NULL,'
                  'created_date TEXT NOT NULL,'
                  'issue_date TEXT NOT NULL);')

    my_crsr = my_cn.cursor()
    my_crsr.execute(my_sql_str)
    my_cn.commit()
    for n in TEST_LIST_NOTES:
        db.save_note_to_db(note=n, db_path=DB_PATH, io_table=IO_TABLE, my_cn=my_cn)


if __name__ == '__main__':
    unittest.main()
