import turtle as t


class Player:
    def __init__(self):
        self._paddle = t.Turtle()
        self._paddle.shape('square')
        self._paddle.color('green')
        self._paddle.shapesize(stretch_wid=1, stretch_len=5)
        self._paddle.penup()
        self._paddle.goto(0, -280)
        self._paddle.speed(1)

    def get_paddle(self):
        return self._paddle

    def move_left(self):
        x = self._paddle.xcor()
        x -= 20
        if x < -347:
            x = -347
        self._paddle.setx(x)

    def move_right(self):
        x = self._paddle.xcor()
        x += 20
        if x > 340:
            x = 340
        self._paddle.setx(x)

    def get_x(self):
        return self._paddle.xcor()

    def get_y(self):
        return self._paddle.ycor()

