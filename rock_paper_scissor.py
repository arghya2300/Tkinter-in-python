import tkinter as tk
from random import choice

def play(user_choice):
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = choice(options)

    result_label.config(text=f"Computer: {computer_choice}")

    if user_choice == computer_choice:
        winner_label.config(text="It's a Tie!")
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        winner_label.config(text="You Win!")
    else:
        winner_label.config(text="Computer Wins!")

def reset_game():
    result_label.config(text="")
    winner_label.config(text="")

root = tk.Tk()
root.title("Rock Paper Scissors")

instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14))
instruction_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=5)

winner_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
winner_label.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 12), width=10, command=lambda: play('Rock'))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 12), width=10, command=lambda: play('Paper'))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 12), width=10, command=lambda: play('Scissors'))
scissors_button.grid(row=0, column=2, padx=5)

reset_button = tk.Button(root, text="Reset Game", font=("Arial", 12), width=15, command=reset_game)
reset_button.pack(pady=10)

root.mainloop()
