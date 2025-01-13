from datetime import datetime as dt, timedelta


def f_parser_date(date_str):
    while True:
        #user_date = input('Enter deadline in DD.MM.YYYY format '
        #'---leave this field empty for default '
        #'value (7 days from today---)')
        if date_str == '':
            parsed_issue_date = dt.today() + timedelta(days=7)
            break
        else:
            try:
                parsed_issue_date = dt.strptime(date_str, '%d.%m.%Y')
                break
            except ValueError:
                return False
    return parsed_issue_date.strftime('%d.%m.%Y')

#****************** end parser date ***********************