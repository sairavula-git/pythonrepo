#This program counts the number of sundays on first day of a month from 01-Jan-1901 to 31-Dec-2000
#This is solution to Problem 19 of ProjectEuler

days_in_month = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
days_in_leap = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def days(month,year):
    if is_leap(year):
        return days_in_leap.get(month)
    else:
        return days_in_month.get(month)

present_day = 2 #Defaulting 1-Jan-1901 as Tuesday
count_sundays=0
for year in range(1901,2001):
    for month in range (1,13):
        present_day = present_day + days(month,year)
        if not (present_day % 7):
            count_sundays+=1
        present_day = present_day % 7

print(count_sundays)
