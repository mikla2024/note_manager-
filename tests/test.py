import unittest
import data as d

class TestNoteManager(unittest.TestCase):
    def test_save_and_load_notes(self):
        my_list_notes = [{
            'username':'test3',
            'titles':['one','two','three']
        }]
        d.save_to_json_git(my_list_notes,'test.json')
        loaded_notes = d.load_from_json_git('test.json')
        self.assertEqual(my_list_notes,loaded_notes)

if __name__ == '__main__':
    unittest.main()