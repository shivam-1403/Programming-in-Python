import random
import os

def deal_cards(): 
    """Gives a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # Ace can act as both 1 or 11 according to needs.

    card = random.choice(cards)
    return card

# Defining a function that calculates the sum of cards.
def calculate_scores(cards) : 
    """Take a list of cards and returns the score calculated from cards."""
    score = sum(cards)

    # If there is a blackjack (a hand with only 2 cards : an ace and a 10), return 0 instead of actual sum.
    if score == 21 and len(cards) == 2 : 
        return 0
    
    # Check for an 11, if the score is already above 21, remove 11 and replace it with 1.
    if 11 in cards and score > 21 :
        cards.remove(11)
        cards.append(1)
    return score

# Compare the score. If the user and computer has the same score, it will be a draw, if any of them has a blackjack then he wins. If anyone has a score more than 21, he loses, else one with the maximum score (must be less than 21) wins.
def compare(user_score, comp_score) :
    if user_score == comp_score : 
       return "DRAW 🙃!!"
    elif user_score == 0 : 
        return "You Won with Blackjack 😎!"
    elif comp_score == 0 :
       return "Lose, Opponent has Blackjack 😱!"
    elif user_score > 21 :
        return "You went over. You Lose 😭!"
    elif comp_score > 21 :
        return "Opponent went over. You Win 😁!"
    elif user_score > comp_score :
       return "You Win 😃!"
    else :
        return "You Lose 😤!"

def play_game():
    from art import logo
    print(logo)
    # Deal user and computer 2 random cards from the deck.
    user_cards = []
    comp_cards = []
    is_game_over = False

    for _ in range(2) :
        user_cards.append(deal_cards())
        comp_cards.append(deal_cards())

    # calling calculate_scores() and then checking if the user or computer has a blackjack (0) or the user_score is over 21, game ends. If game isn't over ask the user whether they want to draw more card or not.
    while not is_game_over :
        user_score = calculate_scores(user_cards)
        comp_score = calculate_scores(comp_cards)

        print(f"Your cards : {user_cards} , Your score : {user_score}")
        print(f"Computer's first card : {comp_cards[0]}")
        if user_score == 0 or comp_score == 0 or user_score > 21 :
            is_game_over = True
        else : 
            user_should_deal = input("Type 'y' to get another card or type 'n' to pass : ")
            if user_should_deal == "y" : 
                user_cards.append(deal_cards())
            else : 
                is_game_over = True

    # Now the computer will play, it has to draw cards as long as it's score is less than 17.
    while comp_score != 0 and comp_score < 17 : 
        comp_cards.append(deal_cards())
        comp_score = calculate_scores(comp_cards)

    print(f"Your final hand : {user_cards}, final score : {user_score}")
    print(f"Opponent's final hand : {comp_cards}, final score : {comp_score}")
    print(compare(user_score, comp_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls')
    play_game()