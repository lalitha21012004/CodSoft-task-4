import tkinter as tk
from tkinter import messagebox
import random

def generate_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'Tie'
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return 'Win'
    else:
        return 'Lose'

def play():
    user_choice = user_choice_var.get()
    computer_choice = generate_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    # Update user score
    if result == 'Win':
        user_score_var.set(user_score_var.get() + 1)
    elif result == 'Lose':
        computer_score_var.set(computer_score_var.get() + 1)

    # Display result
    messagebox.showinfo("Result", f"Computer chose {computer_choice}. You {result}!")

# Create main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Create variables
user_choice_var = tk.StringVar()
user_score_var = tk.IntVar()
computer_score_var = tk.IntVar()

# Create GUI elements
tk.Label(root, text="Your choice:").grid(row=0, column=0)
user_choices = ['Rock', 'Paper', 'Scissors']
for i, choice in enumerate(user_choices):
    tk.Radiobutton(root, text=choice, variable=user_choice_var, value=choice).grid(row=i+1, column=0, sticky='w')

tk.Button(root, text="Play", command=play).grid(row=4, column=0, pady=10)
tk.Label(root, text="Your Score:").grid(row=5, column=0, pady=(0,5))
tk.Label(root, textvariable=user_score_var).grid(row=5, column=1, pady=(0,5))
tk.Label(root, text="Computer Score:").grid(row=6, column=0)
tk.Label(root, textvariable=computer_score_var).grid(row=6, column=1)

root.mainloop()
