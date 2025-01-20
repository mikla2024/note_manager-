import data
import interface
import utils


def display_pages(my_list_notes, page_nr, notes_per_page=2):
    start = (page_nr - 1) * notes_per_page
    end = start + notes_per_page
    page_notes = my_list_notes[start:end]

    print(f'\n*** Страница {page_nr} ***')
    start_index = (page_nr - 1) * notes_per_page + 1
    interface.f_print_all(page_notes, start_index)

def paginate_notes (my_list_notes):
    page_nr = 1
    notes_per_page = 3
    total_pages = (len(my_list_notes) + notes_per_page - 1) // notes_per_page

    while True:
        display_pages(my_list_notes, page_nr, notes_per_page)
        print('\n[N] Следующая | [P] Предыдущая | [X] Выход')
        choice = input('Ваш выбор: ').strip().lower()
        if choice == 'n' and page_nr < total_pages:
            page_nr += 1

        elif choice == 'p' and page_nr > 1:
            page_nr -= 1

        elif choice == 'x':
            break

        else:
            utils.handle_error('invalid_input')

if __name__ == '__main__':
    my_list_notes = data.load_from_json_git()
    paginate_notes(my_list_notes)
