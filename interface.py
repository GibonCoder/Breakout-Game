import tkinter as tk
from player import Player
from ball import Ball
from screen import Screen


class Interface:
    def __init__(self):
        self.root = tk.Tk()
        # Screen setup
        self.root.title("Breakout Game")
        self.root.geometry("800x600")

    def run_interface(self):
        self.root.mainloop()
        self.set_welcome()

    def close_interface(self):
        self.root.destroy()

    @staticmethod
    def run_game():
        # Initialize Player and Ball
        player = Player()
        ball = Ball()
        screen = Screen(player, ball)
        screen.place_player(player.paddle)

        screen.run_screen()

    def restart_game(self):
        self.close_interface()
        self.run_game()

    def set_welcome(self):
        welcome_lbl = tk.Label(self.root, text="Welcome to the Breakout Game")
        start_btn = tk.Button(self.root, text="Play", command=self.close_interface)

        welcome_lbl.pack()
        start_btn.pack()

    def set_goodbye(self, score):
        goodbye_lbl = tk.Label(self.root, text="You lost 😓")
        score_lbl = tk.Label(self.root, text=f"Final score: {score}")
        quit_btn = tk.Button(self.root, text="Quit", command=self.close_interface)
        restart_btn = tk.Button(self.root, text="Restart")

        goodbye_lbl.pack()
        score_lbl.pack()
        quit_btn.pack()
        restart_btn.pack()
