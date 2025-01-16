import data

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

my_list = [my_test_note, my_test_note2]
print(data.search_note(my_list,srch_str='five', srch_status='done'))