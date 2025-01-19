import interface

test_note_1 = {
    'username':'name',
    'status': 'Важно',
    'titles': ['one','two']
}
test_note_2 = {
    'username':'name',
    'status': 'В процессе',
    'titles': ['one','two']
}
test_note_3 = {
    'username':'name',
    'status': 'Выполнено',
    'titles': ['one','two']
}

test_list = [test_note_1,test_note_2,test_note_3]

interface.f_print_all(test_list)