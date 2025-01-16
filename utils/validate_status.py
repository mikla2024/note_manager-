def validate_user_status(value):
    try:
        if value == '1':
            return 'In progress'
        elif value == '2':
            return 'Postponed'
        elif value == '3':
            return 'Done'
        else:
            raise Exception()
    except:
        raise ValueError('Выберите статус из предложенных вариантов')


