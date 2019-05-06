from datetime import date
import calendar

def dateCheck():
    # what is today?
    my_date = date.today()
    today = calendar.day_name[my_date.weekday()]

    return today
