import emoji

def handle_error(err_type):

    errors = {
        'invalid_input': emoji.emojize(':warning:') + 'Ошибка: Введены некорректные данные или неизвестная команда',
        'note_not_found': emoji.emojize(':warning:') + 'Ошибка: Заметка не найдена.',
        'empty_list': emoji.emojize(':warning:') + 'Ошибка: Список заметок пуст. '
    }

    print('\n', errors.get(err_type, 'Неизвестная ошибка'))
