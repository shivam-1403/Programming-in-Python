import random
from art import logo

def choose_num() :
    num_chosen = random.randint(1,100)
    return num_chosen

def play(lives) :
    game_over = False
    while not game_over :
        guess = int(input(f"You have {lives} attempts to guess the number.\nMake a Guess : "))
        if guess == num :
            print(f"You guess right, the number was {guess} ! You Win !")
            game_over = True
        elif lives == 0 :
            print("You ran out of Attempts. You Lose !")
            print(f"The number was : {num}")
        else :
            lives -= 1
            if guess > num :
                print("Too High.\nGuess Again.")
            else :
                print("Too Low.\nGuess Again.")



print(logo)
num = choose_num()
end_game = False
print("Welcome to the Number Guessing Game.\nI am thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()

if level == "easy" :
    play(10)
elif level == "hard" :
    play(5)