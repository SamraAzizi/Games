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

