import random

# List of secret words
word_bank = ["python", "java", "javascript", "ruby", "php", "csharp", "swift", "html", "css", "sql"]

# Select a random word from the word bank
secret_word = random.choice(word_bank)

# Initialize variables
guesses = ''
turns = 10
letters_guessed = []

# Display welcome message and rules
print("Welcome to Hangman!")
print("You have 10 turns to guess the secret word.")
print("If you guess a letter that is not in the secret word, you will lose a turn.")
print("If you guess the same letter twice, it will not count against you.")
print("Good luck!\n")

# Loop until the player wins or runs out of turns
while turns > 0:
    # Display the current progress
    progress = ''
    for letter in secret_word:
        if letter in guesses:
            progress += letter
        else:
            progress += '_'
    print(progress)

    # Get the player's guess
    guess = input("Guess a letter: ").lower()

    # Check if the guess is valid
    if not guess.isalpha() or len(guess) != 1:
        print("Invalid guess. Please enter a single letter.")
        continue

    # Check if the letter has already been guessed
    if guess in letters_guessed:
        print("You already guessed that letter. Please try again.")
        continue
    else:
        letters_guessed.append(guess)

    # Check if the guess is correct
    if guess in secret_word:
        print("Correct!")
        guesses += guess
    else:
        print("Incorrect!")
        turns -= 1

    # Check if the player has won
    if '_' not in progress:
        print("Congratulations, you won!")
        break

    # Display the remaining turns
    print("You have", turns, "turns left.")

# Display the secret word if the player has lost
if turns == 0:
    print("Sorry, you lost. The secret word was", secret_word)