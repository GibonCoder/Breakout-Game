import turtle as t
from brick import Brick


class Screen:
    def __init__(self, player, ball):
        # Variables
        self.screen = t.Screen()
        self._is_game_on = True
        self.bricks = [[None for _ in range(10)] for _ in range(5)]

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

    def bricks_setup(self):
        for row in range(len(self.bricks)):
            for col in range(len(self.bricks[row])):
                x = -380 + (col * 80)
                y = 250 - (row * 20)
                self.bricks[row][col] = Brick(x, y)

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
