# Cows and Bulls game
# Guess a 4-digit number with unique digits to crack the secret code.
# Each correct digit in the right place earns you a "bull".
# Every correct digit in the wrong position gets you a "cow".
# Use the feedback to refine your guesses and crack the code.
# Win by guessing the secret number with all 4 digits in the correct positions.


import random

def generate_secret_number():
    """Generate a random 4-digit number with unique digits."""
    digits = random.sample(range(10), 4)
    return ''.join(map(str, digits))

def get_feedback(secret_number, guess):
    """Provide feedback (cows and bulls) for a guess."""
    bulls = sum(1 for i in range(4) if secret_number[i] == guess[i])
    cows = sum(1 for digit in guess if digit in secret_number) - bulls
    return bulls, cows

def play_game():
    """Main function to play the game."""
    secret_number = generate_secret_number()
    attempts = 0

    print("Welcome to the Cows and Bulls Game!")
    print("Try to guess the 4-digit number with no repeating digits.")

    while True:
        guess = input("Enter your guess: ")

        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            print("Invalid guess. Please enter a 4-digit number with unique digits.")
            continue

        attempts += 1
        bulls, cows = get_feedback(secret_number, guess)

        print(f"Your guess: {guess}")
        print(f"Bulls: {bulls}, Cows: {cows}")

        if bulls == 4:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    play_game()


