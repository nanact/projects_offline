import calendar

def display_months():
    for month in calendar.month_name:
        if month:
            print(month)

display_months()
