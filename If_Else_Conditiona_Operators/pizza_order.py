# Choose a pizza, small for $15, medium for $20, large for $25
# ask if they want extra Pepperoni :
#  > $2 for small, and $3 for medium and large
# ask for extra Cheese :
#  > $1 for any pizza

print("Welcome to the Pizza Shop !")
print("Prices -->")
print(" $15 for Small Pizza\n $20 for Medium Pizza\n $25 for Large Pizza\n $2 for Extra Pepperoni on Small Pizza\n $3 for extra Pepperoni on Medium and Large Pizza\n $1 for extra Cheese on any Pizza")
size=input("Enter the size of Pizza; S, M or L : ")
bill=0
if size=='S':
    bill=15
elif size=='M':
    bill=20
elif size=='L':
    bill=25
else:
    print("Invalid Choice")
pepp=input("Do you want extra Pepperoni ? Y or N : ")
if pepp=='Y':
    if size=='S':
        bill+=2
    else:
        bill+=3
cheese=input("Do you want extra Cheese ? Y or N : ")
if cheese=='Y':
    bill+=1

print("Your Bill is",bill)