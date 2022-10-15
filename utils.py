#Put functions that multiple files use in here

import datetime

def add_day(date):
    day_1 = datetime.datetime.strptime(date, "%Y-%m-%d")
    next_date = day_1 + datetime.timedelta(days=1)    #Hopefully this takes care of month years/leap years and stuff for us

    return next_date.strftime("%Y-%m-%d")   #Convert datetime object back into a string with format %Y-%m-%d