import random 
from art import logo
import os
clear = lambda: os.system('cls')

# house rules
    # the deck is unlimited in size
    # Ace can count as 11 or 1

# deck of cards simplified
def deal_card():
    """returns random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """takes list of cards and returns the score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
        
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw :|"
    elif computer_score == 0:
        return "Lose, computer won with a Blackjack :["
    elif user_score == 0:
        return "Win! With a Blackjack :]"
    elif user_score > 21:
        return "You went over 21. Good luck next time :["
    elif computer_score > 21:
        return "The computer went over, you win! :]"
    elif user_score > computer_score:
        return "You Win. Highest pair :]"
    else:
        return "You Lose. :["
    

def play_game():
    print(logo)
# user and ai cards
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(logo)
        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'hit' to get another card, type 'stay' to pass ")
            if user_should_deal == "hit":
                user_cards.append(deal_card())
            else:
                is_game_over = True
        # play game

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print("◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦")
    print("Scores Below")
    print("◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦")
    print(f"Your final hand: {user_cards}, Your final score: {user_score}")
    print("◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦")
    print(f"The computers final hand: {computer_cards}, The computers final score: {computer_score}")
    print("◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦◦") 
    print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()