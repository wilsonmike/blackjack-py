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

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
        
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

# user and ai cards
user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

calculate_score(user_cards)
calculate_score(computer_cards)

# play game
print(logo)