import random

def guess_the_number():
    while True:
        print("Welcome to Guess the Number!")
        print("I'm thinking of a number between 1 and 100.")
        secret_number = random.randint(1, 100)
        attempts = 0

        while True:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                break
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing!")
            break

guess_the_number()
