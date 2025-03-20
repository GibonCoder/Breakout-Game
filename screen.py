import turtle as t


class Screen:
    def __init__(self, player, ball):
        # Variables
        self.screen = t.Screen()
        self._is_game_on = True
        # Screen setup
        self.screen.title("Breakout Game")
        self.screen.bgcolor('black')
        self.screen.setup(width=800, height=600)
        self.play(player, ball)

    def run_screen(self):
        self.screen.mainloop()

    def place_ball(self, ball):
        ball.showturtle()
        self.screen.listen()

    def place_player(self, player):
        player.showturtle()
        self.screen.listen()

    def place_bricks(self):
        pass

    def play(self, player, ball):
        self.screen.listen()
        self.screen.onkeypress(player.move_left, 'Left')
        self.screen.onkeypress(player.move_right, 'Right')
        while self._is_game_on:
            ball.move()
            # Collision check with paddle
            paddle_x = player.get_x()
            paddle_y = player.get_y()
            ball.hit_paddle(paddle_x, paddle_y)
