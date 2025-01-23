import emoji


def handle_error(err_type: str):
    errors = {
        'invalid_input': emoji.emojize(':warning:') + 'Ошибка: Введены некорректные данные.',
        'note_not_found': emoji.emojize(':warning:') + 'Ошибка: Заметка не найдена.',
        'empty_list': emoji.emojize(':warning:') + 'Ошибка: Список заметок пуст. '
    }

    print('\n', errors.get(err_type, 'Неизвестная ошибка'))


if __name__ == '__main__':
    handle_error('empty_list')
    handle_error('invalid_input')
    handle_error('note_not_found')
    handle_error('unknown')
