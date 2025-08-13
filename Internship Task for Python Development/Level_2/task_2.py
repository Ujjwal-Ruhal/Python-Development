# Task-2: Number Guesser

import random

# Ask the user to set the range
low_range = int(input("Enter the lower limit of the range: "))
high_range = int(input("Enter the upper limit of the range: "))

# Generate a random number within the specified range
secret_number = random.randint(low_range, high_range)

print(f"\nI have chosen a number between {low_range} and {high_range}. Can you guess it?")

attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess > secret_number:
            print("Too high! Try again.")
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed the correct number {secret_number}.")
            print(f"You guessed it in {attempts} attempt{'s' if attempts > 1 else ''}.")
            break

    except ValueError:
        print("❌ Please enter a valid number.")

# that's it, thank you...