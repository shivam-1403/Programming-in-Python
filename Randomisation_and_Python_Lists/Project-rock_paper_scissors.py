
import random

rock= ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

choice=int(input("Welcome to the Rock, Paper, Scissors Game\nPress 0 for Rock, 1 for Paper or 2 for Scissors : "))
if choice==0:
    print(rock)
    print("rock")
elif choice==1:
    print(paper)
    print("paper")
elif choice==2:
    print(scissors)
    print("scissors")
else:
    print("Invalid Choice.")
  
comp_choice= random.randint(0,2)
if comp_choice==0:
    print(rock)
    print("rock")
elif comp_choice==1:
    print(paper)
    print("paper")
elif comp_choice==2:
    print(scissors)
    print("scissors")
else:
    print("Invalid Choice.")

if choice == comp_choice:
    print("It's a Tie.")
elif choice==0:
    if comp_choice==1:
        print("You Lose !")
    else:
        print("You Won !")
elif choice==1:
    if comp_choice==0:
        print("You Won !")
    else:
        print("You Lose !")
else:
    if comp_choice==0:
        print("You Lose !")
    else:
        print("You Won !")