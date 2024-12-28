# Replacing blanks with guesses.

import random
words_list=["advark","baboon","camel"]
chosen_word= random.choice(words_list)

#Testing Code:
print(f"Pssst, the solution is {chosen_word}.")

# ToDo-1: Create an empty list called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_","_","_","_","_"] with 5 "_" representing each letter to guess.
display=[]
for letter in range(len(chosen_word)):
    display+= "_"

guess = input("Guess a letter : ").lower()

# ToDo-2: Loop through each position in the chosen_word;
# if the letter at the position matches 'guess' then reveal that letter in display at that position.
# eg. if the user guessed "p" and the chosen_word was "apple", then display should be ["_","p","p","_","_"].

for position in range(len(chosen_word)):
    letter= chosen_word[position]
    if letter == guess:
        display[position] = letter

# ToDo-3: Print "display" and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint- Don't worry about getting the user to guess the next letter. That will be tackled in Step 3. 

print(display)