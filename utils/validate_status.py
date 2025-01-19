def validate_user_status(value):
    try:
        if value == '1':
            return 'Важно'
        elif value == '2':
            return 'На исполнении'
        elif value == '3':
            return 'Выполнено'
        else:
            raise Exception
    except:
        raise ValueError

