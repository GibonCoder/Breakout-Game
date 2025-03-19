import turtle as t


class Ball:
    def __init__(self):
        self.ball = t.Turtle()
        self.ball.shape('circle')
        self.ball.color('white')
        self.ball.penup()
        self.ball.goto(0, 0)

    def move(self):
        self.ball.setx(self.ball.xcor() + 2)
        self.ball.sety(self.ball.ycor() + 2)

    def hit_paddle(self):
        pass
