# In this program, you will enter a year and a month, it will check whether the year is leap or not and then will see the month in accordance to year and will tell the no. of days in that month.

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
               return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):

    if month > 12 or month < 1 :
        return "Invalid Month !"
    
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2 :
        return 29
    return month_days[month - 1]

year = int(input("Enter a Year : "))
month = int(input("Enter a Month : "))
days = days_in_month(year, month)
print(days) 