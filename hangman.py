
# Hangman:

# A word is chosen and represented by dashes.
# The player guesses letters one at a time.
# Correct guesses reveal the letters in the word, while incorrect guesses result in drawing a part of the hangman.
# The player wins by guessing all the letters in the word before completing the hangman.

import random

def choose_word():
    # List of words for the game
    words = ["apple", "banana", "orange", "grape", "pear", "strawberry", "blueberry", "kiwi", "pineapple", "watermelon","computer", "programming", "keyboard", "elephant", "universe", "basketball", "skyscraper", "adventure", "guitar", "butterfly"]
    return random.choice(words)

def display_word(word, guessed_letters):
    # Display the word with dashes for missing letters
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Welcome to Hangman!")
    secret_word = choose_word()
    guessed_letters = []
    attempts = 6

    while True:
        print("\n" + display_word(secret_word, guessed_letters))
        print("Attempts left:", attempts)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue
        elif guess in secret_word:
            print("Correct guess!")
            guessed_letters.append(guess)
            if display_word(secret_word, guessed_letters) == secret_word:
                print("Congratulations! You've guessed the word:", secret_word)
                break
        else:
            print("Wrong guess!")
            attempts -= 1
            if attempts == 0:
                print("Game over! The word was:", secret_word)
                break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()

hangman()
