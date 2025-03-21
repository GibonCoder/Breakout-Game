import turtle as t
from brick import Brick


class Screen:
    def __init__(self, player, ball):
        # Variables
        self.screen = t.Screen()
        self._is_game_on = True
        self.bricks = [[Brick() for _ in range(10)] for _ in range(5)]
        # Screen setup
        self.screen.title("Breakout Game")
        self.screen.bgcolor('black')
        self.screen.setup(width=800, height=600)
        self.play(player, ball)

    def run_screen(self):
        self.screen.mainloop()

    @staticmethod
    def place_ball(self, ball):
        ball.showturtle()

    @staticmethod
    def place_player(player):
        player.showturtle()

    def place_bricks(self):
        for row in range(len(self.bricks)):
            for col in range(len(self.bricks[row])):
                x = -380 + (col * 80)
                y = 250 - (row * 20)
                self.bricks[row][col].set_position(x, y)
                self.bricks[row][col].set_size('small')

    def play(self, player, ball):
        self.screen.listen()
        self.screen.onkeypress(player.move_left, 'Left')
        self.screen.onkeypress(player.move_right, 'Right')
        self.place_bricks()
        while self._is_game_on:
            ball.move()
            # Collision check with paddle
            paddle_x = player.get_x()
            paddle_y = player.get_y()
            ball.hit_paddle(paddle_x, paddle_y)