# Picking a random word, taking a guess from user and checking if it's right or wrong.

words_list=["advark","baboon","camel"]

# ToDo_1 : Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random

chosen_word= random.choice(words_list)

# ToDo_2 : Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess= input("Guess a letter : ").lower()

# ToDo_3 : Check if the letter the user guessed is one of the letters in the chosen_word.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")