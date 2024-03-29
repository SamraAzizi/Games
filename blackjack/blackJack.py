
#Blackjack:
# Players aim to get cards totaling as close to 21 as possible without going over.
# Each player is dealt two cards initially.
# Players can "hit" to receive another card or "stand" to keep their current total.
# The dealer also plays and must hit until their total is at least 17.
# The player closest to 21 without going over wins.


import random

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def card_value(card):
    if card['rank'] in ['Jack', 'Queen', 'King']:
        return 10
    elif card['rank'] == 'Ace':
        return 11
    else:
        return int(card['rank'])

def hand_value(hand):
    value = sum(card_value(card) for card in hand)
    num_aces = sum(1 for card in hand if card['rank'] == 'Ace')
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

def display_hand(hand):
    return ', '.join(card['rank'] + ' of ' + card['suit'] for card in hand)

def blackjack():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("Welcome to Blackjack!")
    print("Dealer's hand:", dealer_hand[0]['rank'] + ' of ' + dealer_hand[0]['suit'])
    print("Your hand:", display_hand(player_hand))

    while hand_value(player_hand) < 21:
        action = input("Do you want to hit or stand? ").lower()
        if action == 'hit':
            player_hand.append(deck.pop())
            print("Your hand:", display_hand(player_hand))
        elif action == 'stand':
            break

    player_score = hand_value(player_hand)
    dealer_score = hand_value(dealer_hand)
    while dealer_score < 17:
        dealer_hand.append(deck.pop())
        dealer_score = hand_value(dealer_hand)

    print("Dealer's hand:", display_hand(dealer_hand))
    print("Your score:", player_score)
    print("Dealer's score:", dealer_score)

    if player_score > 21:
        print("Bust! You lose.")
    elif dealer_score > 21 or player_score > dealer_score:
        print("You win!")
    elif player_score < dealer_score:
        print("Dealer wins.")
    else:
        print("It's a tie!")

blackjack()
