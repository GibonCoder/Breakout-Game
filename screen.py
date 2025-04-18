import turtle as t
from brick import Brick


class Screen:
    def __init__(self, player, ball, game_over_callback):
        # Variables
        self.screen = t.Screen()
        self._is_game_on = True
        self.bricks = [[Brick() for _ in range(39)] for _ in range(10)]
        self.game_over_callback = game_over_callback
        self.score = 0
        # Screen setup
        self.screen.title("Breakout Game")
        self.screen.bgcolor('black')
        self.screen.setup(width=800, height=600)
        self.play(player, ball)

    def run_screen(self):
        self.screen.mainloop()

    def stop_game(self):
        self.screen.clear()

    def close_screen(self):
        self.screen.bye()

    @staticmethod
    def place_ball(ball):
        ball.showturtle()

    @staticmethod
    def place_player(player):
        player.showturtle()

    def place_bricks(self):
        for row in range(len(self.bricks)):
            for col in range(len(self.bricks[row])):
                x = -385 + (col * 20)
                y = 290 - (row * 20)
                self.bricks[row][col].set_position(x, y)

    def play(self, player, ball):
        # Bricks placement
        self.place_bricks()
        while self._is_game_on:
            # Player movement
            self.screen.listen()
            self.screen.onkeypress(player.move_left, 'Left')
            self.screen.onkeypress(player.move_right, 'Right')
            # Ball movement
            ball.move()
            # Collision detection with walls
            ball.hit_wall()
            # Collision detection with paddle
            paddle_x = player.get_x()
            paddle_y = player.get_y()
            ball.hit_paddle(paddle_x, paddle_y)
            # Collision detection with bricks
            for row in self.bricks:
                for brick in row:
                    brick_x = brick.get_x()
                    brick_y = brick.get_y()
                    # To investigate if work correctly
                    if ball.hit_brick(brick_x, brick_y):
                        brick.is_break(row)
                        self.score += 1
            # Ball out of screen detection
            if ball.is_out():
                self._is_game_on = False
                self.stop_game()
                self.game_over_callback(self.score)
