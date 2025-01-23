import unittest
import data as d
import utils


class TestNoteManager(unittest.TestCase):

    def test_save_and_load_notes(self):
        my_test_notes = [{
            'username': 'test1',
            'titles': ['one', 'two', 'three']
        }]
        d.save_to_json_git(my_test_notes, 'test.json')
        loaded_notes = d.load_from_json_git('test.json')
        self.assertEqual(my_test_notes, loaded_notes)

    def test_status_update(self):
        my_test_note = {
            'username': 'test1',
            'titles': ['one', 'two', 'three'],
            'status': 'in progress'
        }
        d.f_status_update(my_test_note, 'test_status')
        self.assertEqual(my_test_note.get('status'), 'test_status')

    def test_search_note(self):
        my_test_note = {
            'username': 'test1',
            'titles': ['one', 'two', 'three'],
            'status': 'in progress'
        }
        my_test_note2 = {
            'username': 'test2',
            'titles': ['four', 'five', 'six'],
            'status': 'done'
        }

        test_list = [my_test_note, my_test_note2]
        test_search_keys: dict = {
            's_str': 'test2',
            's_sts': '',
            's_dt': ''
        }
        found_note = d.apply_filter_to_list(test_list, test_search_keys)
        self.assertEqual(found_note, [my_test_note2])

    @unittest.expectedFailure
    def test_validate_date_fail(self):
        test_date_str: str = '01.31.2025'
        self.assertEqual(utils.f_parser_date(date_str=test_date_str), '31.01.2025')

    def test_del_note(self):
        my_test_note = {
            'username': 'test1',
            'titles': ['one', 'two', 'three'],
            'status': 'in progress'
        }
        my_test_note2 = {
            'username': 'test2',
            'titles': ['four', 'five', 'six'],
            'status': 'done'
        }

        test_list = [my_test_note, my_test_note2]
        d.f_del_note(test_list, my_test_note)
        self.assertEqual(test_list, [my_test_note2])


if __name__ == '__main__':
    unittest.main()
