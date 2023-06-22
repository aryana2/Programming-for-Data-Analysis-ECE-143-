import calendar

def number_of_days(year, month):
    '''Return number of calendar days in a given year and month'''
    assert isinstance(year, int), 'year input must be an integer'
    assert isinstance(month, int), 'month input must be an integer'
    assert year > 0, 'year must be greater than 0'
    assert month > 0, 'month must be greater than 0'
    assert month < 13, 'month must be no larger than 12'
    return calendar.monthrange(year, month)[1]

def number_of_leap_years(year1,year2):
    '''Return number of leap years between two years'''
    assert isinstance(year1, int), 'year input must be an integer'
    assert isinstance(year2, int), 'year input must be an integer'
    assert year1 > 0, 'year input must be greater than 0'
    assert year2 > 0, 'year input must be greater than 0'
    assert year1 < year2, 'year1 must be less than year2'
    start = year1
    end = year2
    count = 0
    while start <= end:
        if (start % 4 == 0 and start % 100 != 0) or (start % 4 == 0 and start % 400 == 0):
            count += 1
        start += 1
    return count

def get_day_of_week(year,month,day):
    '''Return string name of day of week given month, day, year'''
    assert isinstance(year, int), 'year input must be an integer'
    assert isinstance(month, int), 'month input must be an integer'
    assert isinstance(day, int), 'day input must be an integer'
    assert year > 0, 'year must be greater than 0'
    assert month > 0, 'month must be greater than 0'
    assert month < 13, 'month must be no larger than 12'
    assert day > 0, 'day must be greater than 0'
    if month == 2:
       if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 400 == 0): 
           assert day < 30, 'day must not be greater than 30 for month of february'
       else:
           assert day < 29, 'day must not be greater than 30 for month of february'
    else:
        assert day < 32, 'day must not be greater than 31'
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[calendar.weekday(year, month, day)]