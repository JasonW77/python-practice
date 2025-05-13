import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("I'm thinking of a number between 1 and 100. can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too Low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Correct! You guessed it in {attempts} tries.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guessing_game()