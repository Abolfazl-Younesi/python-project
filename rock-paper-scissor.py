import random

print("Welcome to Rock-Paper-Scissors!")

# Define the game rules
game_rules = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

# Define the score variables
user_score = 0
computer_score = 0

# Define the number of rounds to play
num_rounds = int(input("How many rounds do you want to play? "))

# Play the game for the specified number of rounds
for i in range(num_rounds):
    print(f"\nRound {i+1}:")

    # Get user input with error handling
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in game_rules:
            break
        print("Invalid choice. Please try again.")

    # Generate computer choice
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose {computer_choice}.")

    # Determine the winner and update the score
    if user_choice == computer_choice:
        print("It's a tie!")
    elif game_rules[user_choice] == computer_choice:
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

# Print the final score
print("\nFinal score:")
print(f"You: {user_score}")
print(f"Computer: {computer_score}")
if user_score > computer_score:
    print("You win the game!")
elif user_score < computer_score:
    print("Computer wins the game!")
else:
    print("It's a tie game!")

