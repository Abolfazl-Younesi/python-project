import random

# set the difficulty level
difficulty = input("Choose a difficulty level (easy, medium, hard): ")

# set the range of numbers based on the difficulty level
if difficulty == "easy":
    min_num, max_num = 1, 10
    max_guesses = 6
elif difficulty == "medium":
    min_num, max_num = 1, 50
    max_guesses = 8
else:
    min_num, max_num = 1, 100
    max_guesses = 10

# generate a random number within the range
number = random.randint(min_num, max_num)

# initialize the number of guesses
num_guesses = 0

# ask the user to guess the number
while num_guesses < max_guesses:
    print(f"You have {max_guesses - num_guesses} guesses left.")
    guess = int(input(f"Guess a number between {min_num} and {max_num}: "))
    num_guesses += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {num_guesses} guesses.")
        break

# if the user runs out of guesses, reveal the number
if num_guesses == max_guesses:
    print(f"Sorry, you ran out of guesses. The number was {number}.")