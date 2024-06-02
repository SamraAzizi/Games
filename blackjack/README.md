# Blackjack Game README

## Introduction
This Python script simulates a simple game of Blackjack, a classic card game where the goal is to get your card total to as close to 21 as possible, without going over. The game is played against a dealer, with both players trying to achieve a better hand. The script provides an interactive experience, allowing players to "hit" for more cards or "stand" to halt their hand progression.

## Features
- **Automatic Deck Creation**: Creates a shuffled 52-card deck, representing each card as a dictionary with suit and rank.
- **Value Assignment**: Determines the value of each card, with face cards valued at 10, and Aces flexibly valued at 1 or 11 to benefit the player's hand.
- **Total Hand Value**: Calculates the sum of the hand's card values, adjusting for Aces to avoid busting over 21.
- **Player Interaction**: Players can decide to "hit" for another card or "stand" to keep their current hand through console prompts.
- **Dealer Behavior**: Emulates dealer play according to Blackjack rules, where the dealer must continue to "hit" until reaching a total of at least 17.

## How to Play
1. **Game Initialization**: Run the script to begin. Both player and dealer are dealt two cards, with one of the dealer's cards hidden from the player.
2. **Player's Choice**: The player's cards are shown, and they must choose whether to "hit" or "stand". The player can continue to "hit" until they decide to "stand" or until their total exceeds 21 (bust).
3. **Dealer's Turn**: After the player stands or busts, the dealer reveals their hidden card and takes additional cards until their total is 17 or higher.
4. **Outcome Determination**: The game compares the totals of the player's and dealer's hands to determine the winner or declare a tie.


