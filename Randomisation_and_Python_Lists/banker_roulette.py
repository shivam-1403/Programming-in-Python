# Banker Roulette - Who will pay the Bill ?

import random
print("Welcome to the Roulette --> ")
test_seed=int(input("Enter a Seed Number : "))
random.seed(test_seed)

names_input=input("Give me everyone's name, separated by a comma and a space : ")
names= names_input.split(", ")
payer=random.randint(0,len(names)-1)
print(names[payer],"is going to buy the meal today !")