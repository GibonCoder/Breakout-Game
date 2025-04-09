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
            "restart button": tk.Button(self.root, text="Restart Game", command=self.restart_game)

        }
        # Screen setup
        self.root.title("Breakout Game")
        self.root.geometry("800x600")

    def run_interface(self):
        self.set_welcome()
        self.root.mainloop()

    def close_interface(self):
        self.root.quit()

    def run_game(self):
        self.close_interface()
        # Initialize Player and Ball
        player = Player()
        ball = Ball()
        screen = Screen(player, ball, self.on_game_over)
        screen.place_player(player.paddle)

        screen.run_screen()

    def on_game_over(self, score):
        self.__init__()
        self.set_goodbye(score)
        self.root.mainloop()

    def restart_game(self):
        self.close_interface()
        self.run_game()

    def set_welcome(self):
        self.widgets["welcome label"].pack()
        self.widgets["start button"].pack()

    def set_goodbye(self, score):
        self.widgets["goodbye label"].pack()
        self.widgets["score label"].config(text=f"Final score: {score}")
        self.widgets["score label"].pack()
        self.widgets["quit button"].pack()
        self.widgets["restart button"].pack()
