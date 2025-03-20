import turtle as t


class Player:
    def __init__(self):
        self.paddle = t.Turtle()
        self.paddle.shape('square')
        self.paddle.color('green')
        self.paddle.shapesize(stretch_wid=1, stretch_len=5)
        self.paddle.penup()
        self.paddle.goto(0, -280)
        self.paddle.speed(1)

    def move_left(self):
        x = self.paddle.xcor()
        x -= 20
        if x < -347:
            x = -347
        self.paddle.setx(x)

    def move_right(self):
        x = self.paddle.xcor()
        x += 20
        if x > 340:
            x = 340
        self.paddle.setx(x)

    def get_x(self):
        return self.paddle.xcor()

    def get_y(self):
        return self.paddle.ycor()

