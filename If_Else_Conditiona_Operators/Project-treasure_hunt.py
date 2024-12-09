print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to the Treasre Island.\nYour Mission is to find the Treasure !")
choice1=input("You're at a crossroad, where would you like to go, enter 'L' for Left or 'R' for Right : ").lower()
if choice1 == 'l':
    choice2=input("You've come to a Lake. There is an island in the middle of the lake, type 'W' to wait for a Boat or 'S' to Swim Across : ").lower()
    if choice2 == 'w':
        choice3=input("You've reached the island. There are 3 doors, Yellow, Red and Blue, one has the treasure, which one to choose ?\nPress 'Y' for Yellow, 'R' for Red or 'B' for Blue : ").lower()
        if choice3 == 'y':
            print("The Treasure was not there. GAME OVER !")
        elif choice3 == 'r':
            print("You Found the Treasure !\nYou Win !")
        elif choice3 == 'b':
            print("The Treasure was not there. GAME OVER !")
        else:
            print("Invalid Choice.")
    elif choice2 == 's':
        print("You were eaten by the Crocodiles. GAME OVER !")
    else:
        print("Invalid Choice.")
elif choice1 == 'r':
    print("You fell into a Hole. GAME OVER !")
else:
    print("Invalid Choice. ")