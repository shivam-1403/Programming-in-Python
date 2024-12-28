# Checking if the user has won.

import random
words_list=["advark","baboon","camel"]
chosen_word= random.choice(words_list)

#Testing Code:
print(f"Pssst, the solution is {chosen_word}.")

# Generate Blanks:
display=[]
for letter in range(len(chosen_word)):
    display+= "_"

# ToDo-1 : Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

end_of_game= False

while not end_of_game:
    guess = input("Guess a letter : ").lower()

    # Check guessed letter : 
    for position in range(len(chosen_word)):
        letter= chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game= True
        print("You Win")