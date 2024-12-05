# To check whether a year is leap or not we will follow these rules :
#  > Divide by 4, if it is not divisible, it is not leap, exit; if it is, go ahead
#  > Divide by 100, if not divisible, it is leap, exit; if it is, go ahead
#  > Divide by 400, if divisible, it is leap; if not,it is not leap

year= int(input("Enter year : "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,"is a leap year")
else:
    print(year,"is not a leap year")