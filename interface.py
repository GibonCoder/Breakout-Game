import tkinter as tk


class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.welcome_lbl = tk.Label(self.root, text="Welcome to Breakout, Game")
        self.goodbye_lbl = tk.Label(self.root, text="You lost 😓")
        self.score_lbl = tk.Label(self.root)
        self.start_btn = tk.Button(self.root, text="Play")
