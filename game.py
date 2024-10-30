import random

# Number Guessing Game
number_to_guess = random.randint(1, 10)
guess = None

print("Guess a number between 1 and 10!")

while guess != number_to_guess:
    guess = int(input("Your guess: "))
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the right number!")
