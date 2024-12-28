import random
import os

import hangman_art
import hangman_words

img= hangman_art.logo
print(img)

end_of_game = False

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

lives = 6

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

print(display)
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    os.system('cls')
    # if the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")
         
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a LIFE.")
        lives-=1
        if lives == 0:
            end_of_game = True
            print("You Lose.")
            print(f"The word was {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You Win.")

    print(hangman_art.stages[lives])