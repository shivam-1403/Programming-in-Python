# numbers = [1, 2, 3, 4]
# num = [n+1 for n in numbers]
# print(num)

# name = "Shivam"
# name_list = [letter for letter in name]
# print(name_list)

# new_range = [2*n for n in range(1,5)]
# print(new_range)


# ***************CONDITIONAL LIST COMPREHENSION*************

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_name = [name for name in names if len(name) < 5]
upper_name = [name.upper() for name in names if len(name) > 5]
print(upper_name)