import random

# Task-1: Guessing Game
GUESS_NUM = random.randint(1, 101)  # Random number between 1 and 100

print("Welcome to the Guessing Game!")
print("I have chosen a number between 1 and 100. Can you guess it?")

count = 0

while True:
    guessing_number = int(input("Enter your guess: "))
    count += 1  # Count every attempt

    if guessing_number > GUESS_NUM:
        print("Too high! Try again.")

    elif guessing_number < GUESS_NUM:
        print("Too low! Try again.")

    else:  # Correct guess
        print(f"👍 Congratulations! You guessed the correct number {GUESS_NUM}.")
        break

print(f"You guessed the number in {count} attempt{'s' if count > 1 else ''}.")
