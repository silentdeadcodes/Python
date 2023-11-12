import random
import tkinter as tk
from tkinter import ttk, messagebox
import time

class GuessTheNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number")

        self.difficulty = tk.StringVar()
        self.difficulty.set("Easy")

        self.style = ttk.Style()
        self.style.configure("TButton", padding=5, font=('Helvetica', 12))

        self.difficulty_label = ttk.Label(master, text="Select Difficulty:")
        self.difficulty_label.grid(row=0, column=0, pady=10)

        self.difficulty_menu = ttk.Combobox(master, textvariable=self.difficulty, values=["Easy", "Medium", "Hard"])
        self.difficulty_menu.grid(row=0, column=1, pady=10)

        self.start_button = ttk.Button(master, text="Start Game", command=self.start_game)
        self.start_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.label = ttk.Label(master, text="", font=('Helvetica', 14))
        self.label.grid(row=2, column=0, columnspan=2, pady=10)

        self.entry = ttk.Entry(master, font=('Helvetica', 12))
        self.entry.grid(row=3, column=0, columnspan=2, pady=10)

        self.guess_button = ttk.Button(master, text="Guess", command=self.check_guess, state=tk.DISABLED)
        self.guess_button.grid(row=4, column=0, pady=10)

        self.restart_button = ttk.Button(master, text="Restart", command=self.restart_game, state=tk.DISABLED)
        self.restart_button.grid(row=4, column=1, pady=10)

        self.history_label = ttk.Label(master, text="Guess History:", font=('Helvetica', 14))
        self.history_label.grid(row=5, column=0, columnspan=2, pady=10)

        self.history_text = tk.Text(master, height=5, width=30, state=tk.DISABLED, font=('Helvetica', 12))
        self.history_text.grid(row=6, column=0, columnspan=2, pady=10)

        self.secret_number = 0
        self.attempts = 0
        self.max_attempts = 0
        self.score = 0
        self.start_time = 0

    def start_game(self):
        difficulty_mapping = {"Easy": (1, 50, 10), "Medium": (1, 100, 15), "Hard": (1, 200, 20)}
        start, end, max_attempts = difficulty_mapping[self.difficulty.get()]

        self.secret_number = random.randint(start, end)
        self.max_attempts = max_attempts
        self.attempts = 0
        self.score = 100
        self.start_time = time.time()

        self.label.config(text=f"Guess the number between {start} and {end}:", font=('Helvetica', 14))
        self.guess_button.config(state=tk.NORMAL)
        self.restart_button.config(state=tk.NORMAL)
        self.history_text.config(state=tk.NORMAL)
        self.history_text.delete("1.0", tk.END)

    def check_guess(self):
        user_input = self.entry.get()

        try:
            user_guess = int(user_input)
            self.attempts += 1

            if user_guess < self.secret_number:
                messagebox.showinfo("Incorrect Guess", "Too low! Try again.")
            elif user_guess > self.secret_number:
                messagebox.showinfo("Incorrect Guess", "Too high! Try again.")
            else:
                elapsed_time = round(time.time() - self.start_time, 2)
                self.score = max(0, round(100 - self.attempts * 5 - elapsed_time, 2))
                messagebox.showinfo("Congratulations", f"You guessed the number in {self.attempts} attempts. Your score is {self.score}.")
                self.history_text.insert(tk.END, f"Attempt {self.attempts}: {user_guess} (Score: {self.score})\n")

                self.guess_button.config(state=tk.DISABLED)
                self.restart_button.config(state=tk.DISABLED)

            if self.attempts >= self.max_attempts:
                messagebox.showinfo("Game Over", f"Sorry, you've run out of attempts. The secret number was {self.secret_number}.")
                self.guess_button.config(state=tk.DISABLED)
                self.restart_button.config(state=tk.DISABLED)

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def restart_game(self):
        self.start_game()
        self.history_text.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    root.mainloop()
