import tkinter as tk
from player import Player
from ball import Ball
from screen import Screen


class Interface:
    def __init__(self):
        self.root = tk.Tk()
        self.widgets = {
            "welcome label": tk.Label(self.root, text="Welcome to the Breakout Game"),
            "start button": tk.Button(self.root, text="Play", command=self.run_game),
            "goodbye label": tk.Label(self.root, text="You lost 😓"),
            "score label": tk.Label(self.root, text="Final score: 0"),
            "quit button": tk.Button(self.root, text="Quit", command=self.close_interface),
            "restart button": tk.Button(self.root, text="Restart Game", command=self.run_game)

        }
        # Screen setup
        self.root.title("Breakout Game")
        self.root.geometry("800x600")

        # Objects instances
        self.player = Player()
        self.ball = Ball()
        self.screen = Screen(self.player, self.ball, self.on_game_over)

    def run_interface(self):
        self.set_welcome()
        self.root.mainloop()

    def close_interface(self):
        self.root.withdraw()

    def run_game(self):
        self.close_interface()
        self.screen.run_screen()

    def on_game_over(self, score):
        self.root.deiconify()
        self.set_goodbye(score)
        self.root.mainloop()

    def set_welcome(self):
        self.widgets["welcome label"].pack()
        self.widgets["start button"].pack()

    def set_goodbye(self, score):
        self.widgets["goodbye label"].pack()
        self.widgets["score label"].config(text=f"Final score: {score}")
        self.widgets["score label"].pack()
        self.widgets["quit button"].pack()
        self.widgets["restart button"].pack()
