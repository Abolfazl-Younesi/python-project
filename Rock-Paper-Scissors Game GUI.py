import random
import tkinter as tk

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
num_rounds = 3

# Define the GUI functions
def play_round():
    global user_score, computer_score
    user_choice = user_choice_var.get().lower()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    computer_choice_var.set(f"Computer chose {computer_choice}.")
    if user_choice == computer_choice:
        result_var.set("It's a tie!")
    elif game_rules[user_choice] == computer_choice:
        result_var.set("You win!")
        user_score += 1
    else:
        result_var.set("Computer wins!")
        computer_score += 1
    user_score_var.set(f"You: {user_score}")
    computer_score_var.set(f"Computer: {computer_score}")
    if user_score + computer_score == num_rounds:
        end_game()

def end_game():
    global user_score, computer_score
    if user_score > computer_score:
        result_var.set("You win the game!")
    elif user_score < computer_score:
        result_var.set("Computer wins the game!")
    else:
        result_var.set("It's a tie game!")
    play_button.config(state=tk.DISABLED)

# Create the GUI
root = tk.Tk()
root.title("Rock-Paper-Scissors")

user_choice_label = tk.Label(root, text="Choose rock, paper, or scissors:")
user_choice_label.grid(row=0, column=0)

user_choice_var = tk.StringVar()
user_choice_var.set('rock')
user_choice_menu = tk.OptionMenu(root, user_choice_var, 'rock', 'paper', 'scissors')
user_choice_menu.grid(row=0, column=1)

play_button = tk.Button(root, text="Play", command=play_round)
play_button.grid(row=0, column=2)

computer_choice_var = tk.StringVar()
computer_choice_label = tk.Label(root, textvariable=computer_choice_var)
computer_choice_label.grid(row=1, column=1)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.grid(row=2, column=1)

user_score_var = tk.StringVar()
user_score_var.set("You: 0")
user_score_label = tk.Label(root, textvariable=user_score_var)
user_score_label.grid(row=3, column=0)

computer_score_var = tk.StringVar()
computer_score_var.set("Computer: 0")
computer_score_label = tk.Label(root, textvariable=computer_score_var)
computer_score_label.grid(row=3, column=2)

root.mainloop()