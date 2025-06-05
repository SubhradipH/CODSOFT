import tkinter as tk
from tkinter import messagebox
import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def play_round(user_choice):
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)

    if winner == "user":
        result_text = f"You chose {user_choice.capitalize()}.\nComputer chose {computer_choice.capitalize()}.\nYou win!"
    elif winner == "computer":
         result_text = f"You chose {user_choice.capitalize()}.\nComputer chose {computer_choice.capitalize()}.\nComputer wins!"
    else:
        result_text = f"You chose {user_choice.capitalize()}.\nComputer chose {computer_choice.capitalize()}.\nIt's a tie!"
    
    messagebox.showinfo("Round Result", result_text)

window = tk.Tk()
window.title("Colorful Rock-Paper-Scissors")
window.geometry("350x280")

window.config(bg="#C67FE7")

button_style = {
    "padx": 25,
    "pady": 12,
    "fg": "white",
    "font": ("Helvetica", 14, "bold"),
    "relief": "raised",
    "bd": 4
}

rock_button = tk.Button(window, text="Rock", command=lambda: play_round('rock'), bg="#FF5733", **button_style)
rock_button.pack(pady=10)

paper_button = tk.Button(window, text="Paper", command=lambda: play_round('paper'), bg="#33FF57", **button_style)
paper_button.pack(pady=10)

scissors_button = tk.Button(window, text="Scissors", command=lambda: play_round('scissors'), bg="#3357FF", **button_style)
scissors_button.pack(pady=10)

window.mainloop()
