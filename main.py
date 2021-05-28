import random 
from art import logo

# house rules
    # the deck is unlimited in size
    # Ace can count as 11 or 1

# deck of cards simplified
def deal_card():
    """returns random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# user and ai cards
user_cards = []
computer_cards = []

for num in range(2):
    user_cards.append(deal_card())
    
# play game
print(logo)