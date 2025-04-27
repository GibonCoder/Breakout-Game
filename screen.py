import turtle as t
from brick import Brick


class Screen:
    def __init__(self, player, ball, game_over_callback):
        # Variables
        self.screen = t.Screen()
        self._is_game_on = True
        self.bricks = []
        self.game_over_callback = game_over_callback
        self.score = 0
        # Screen setup
        self.screen.title("Breakout Game")
        self.screen.bgcolor('black')
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)
        # Game
        self.play(player, ball)

    def run_screen(self):
        self.screen.mainloop()

    def stop_game(self):
        self.screen.clear()

    def close_screen(self):
        self.screen.bye()

    def place_bricks(self):
        rows = 10
        cols = 39
        for row in range(rows):
            for col in range(cols):
                x = -385 + (col * 20)
                y = 290 - (row * 20)
                brick = Brick(x, y)
                self.bricks.append(brick)

    def play(self, player, ball):
        # Player movement
        self.screen.listen()
        self.screen.onkeypress(player.move_left, 'Left')
        self.screen.onkeypress(player.move_right, 'Right')
        # Bricks placement
        self.place_bricks()
        while self._is_game_on:
            # Ball movement
            ball.move()
            # Collision detection with walls
            ball.hit_wall()
            # Collision detection with paddle
            paddle_x = player.get_x()
            paddle_y = player.get_y()
            ball.hit_paddle(paddle_x, paddle_y)
            # Collision detection with bricks
            for brick in self.bricks:
                brick_x = brick.get_x()
                brick_y = brick.get_y()
                # To investigate if work correctly
                if ball.hit_brick(brick_x, brick_y):
                    brick.is_break(self.bricks)
                    self.score += 1
            # Ball out of screen detection
            if ball.is_out():
                self._is_game_on = False
                self.stop_game()
                self.game_over_callback(self.score)
            self.screen.update()
