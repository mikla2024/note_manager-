from datetime import datetime as dt, timedelta


def f_parser_date(date_str:str):

    while True:
        if not date_str:
            parsed_issue_date = dt.today() + timedelta(days=7)
            break
        else:
            try:
                parsed_issue_date = dt.strptime(date_str, '%d.%m.%Y')
                break
            except:
                raise ValueError
    return parsed_issue_date.strftime('%d.%m.%Y')

#****************** end parser date ***********************


# check how many days to deadline
def f_deadline_check(note):
    try:
        day_delta = dt.today() - \
        dt.strptime(note.get('issue_date'),'%d.%m.%Y')
        return day_delta.days
    except:
        raise TypeError