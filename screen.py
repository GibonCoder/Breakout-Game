import turtle as t


class Screen:
    def __init__(self):
        self.screen = t.Screen()
        self.screen.title("Breakout Game")
        self.screen.bgcolor('black')
        self.screen.setup(width=800, height=600)

        self._is_game_on = True

    def run_screen(self):
        self.screen.mainloop()

    def place_ball(self, ball):
        ball.showturtle()
        self.screen.listen()
