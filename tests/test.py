import unittest
import data as d

class Note(object):
    def __init__(self, username, content, status, created_date, issue_date, titles):
        self.username = str(username)
        self.content = str(content)
        self.status = status
        self.created_date = created_date
        self.issue_date = issue_date
        self.titles = titles




class TestNoteManager(unittest.TestCase):

    def test_save_and_load_notes(self):
        my_test_notes = [{
            'username':'test1',
            'titles':['one','two','three']
        }]
        d.save_to_json_git(my_test_notes,'test.json')
        loaded_notes = d.load_from_json_git('test.json')
        self.assertEqual(my_test_notes,loaded_notes)

    def test_status_update(self):
        my_test_note = {
            'username': 'test1',
            'titles': ['one', 'two', 'three'],
            'status':'in progress'
        }
        d.f_status_update(my_test_note,'test_status')
        self.assertEqual(my_test_note.get('status'),'test_status')



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

        test_list=[my_test_note,my_test_note2]

        found_note = d.search_note(test_list, srch_str='test2', srch_status='')
        self.assertEqual(found_note, [my_test_note2])

    def test_unique_id(self):
        pass


if __name__ == '__main__':
    unittest.main()