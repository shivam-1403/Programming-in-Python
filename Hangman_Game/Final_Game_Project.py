import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''' , r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''' , r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''' , r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''' , r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''' , r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["dear"
,"remind"
,"frame"
,"free"
,"trap"
,"vivacious"
,"boorish"
,"rush"
,"peep"
,"comparison"
,"stare"
,"veil"
,"uncle"
,"daughter"
,"slap"
,"fascinated"
,"rural"
,"evasive"
,"whistle"
,"ablaze"
,"fuel"
,"grey"
,"beds"
,"gusty"
,"organic"
,"toys"
,"spiritual"
,"fragile"
,"mysterious"
,"corn"
,"huge"
,"wacky"
,"distinct"
,"invite"
,"grieving"
,"expert"
,"pot"
,"burn"
,"help"
,"hydrant"
,"unnatural"
,"homely"
,"observe"
,"better"
,"throne"
,"brown"
,"minute"
,"disarm"
,"machine"
,"string"
,"sweet"
,"gigantic"
,"young"
,"endurable"
,"bounce"
,"eight"
,"mine"
,"thumb"
,"acceptable"
,"press"
,"agreement"
,"sulky"
,"rhetorical"
,"old"
,"program"
,"educated"
,"whip"
,"unkempt"
,"temper"
,"jumbled"
,"breakable"
,"appliance"
,"destroy"
,"fetch"
,"porter"
,"important"
,"friend"
,"undress"
,"dangerous"
,"decorate"
,"wrestle"
,"mark"
,"suppose"
,"ten"
,"tremble"
,"excite"
,"lettuce"
,"fluffy"
,"parcel"
,"record"
,"next"
,"desire"
,"low"
,"cub"
,"reading"
,"electric"
,"fresh"
,"vast"
,"abrupt"
,"card"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#ToDo-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

print(display)
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #ToDo-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
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

    #ToDo-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])