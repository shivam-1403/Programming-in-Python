import random
from data import data
import os
from art import logo
from art import vs

def print_def(keyword,choose):
    return (choose[keyword])

end_game = False
score = 0
while not end_game :
    choice = random.sample(data, 2)

    name1 = print_def("name", choice[0])
    follower1 = print_def("follower_count", choice[0])
    description1 = print_def("description", choice[0])
    country1 = print_def("country", choice[0])

    name2 = print_def("name", choice[1])
    follower2 = print_def("follower_count", choice[1])
    description2 = print_def("description", choice[1])
    country2 = print_def("country", choice[1])

    first = (f"{name1}, a {description1} from {country1}")
    second = (f"{name2}, a {description2} from {country2}")

    print(logo)

    print("Who has more followers on Instagram ? :\n")
    print(f"Compare A : {first}")
    print(vs)
    print(f"Against B : {second}")
    user_answer = input("Enter Answer : ").lower()
    os.system('cls')

    if user_answer == "a" :
        if int(follower1) > int(follower2) :
            score+=1
            print(f"You are right ! Current Score = {score}")
        else :
            print(f"Sorry that's wrong ! Your Score is : {score}")
            end_game = True
    else :
        if int(follower2) > int(follower1) :
            score+=1
            print(f"You are right ! Current Score = {score}")
        else :
            print(f"Sorry that's wrong ! Your Score is : {score}")
            end_game = True
