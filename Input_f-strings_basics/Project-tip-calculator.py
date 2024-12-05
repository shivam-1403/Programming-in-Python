# This is a tip calculator,which takes the total bill, adds tip amount in it, and divide it to certain no. of people.

print("Welcome To The Tip Calculator !")
bill=float(input("What was the total bill ? $ "))
tip=int(input("Enter the percentage of tip you want to give (10, 12 or 15) : "))
people=int(input("How many people to split the bill in ? "))
total_bill=((tip/100)*bill)+bill
bill_per_person=total_bill/people
final_amount=round(bill_per_person,2)
print("Each person has to pay $",final_amount)