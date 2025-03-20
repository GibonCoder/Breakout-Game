import turtle as t
import random


class Ball:
    def __init__(self):
        self.ball = t.Turtle()
        self.ball.shape('circle')
        self.ball.color('white')
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.setheading(225)

    def move(self):
        if self.ball.heading() in range(0, 90):
            self.ball.setx(self.ball.xcor() + 2)
            self.ball.sety(self.ball.ycor() + 2)
        elif self.ball.heading() in range(90, 180):
            self.ball.setx(self.ball.xcor() - 2)
            self.ball.sety(self.ball.ycor() + 2)
        elif self.ball.heading() in range(180, 270):
            self.ball.setx(self.ball.xcor() - 2)
            self.ball.sety(self.ball.ycor() - 2)
        elif self.ball.heading() in range(270, 360):
            self.ball.setx(self.ball.xcor() + 2)
            self.ball.sety(self.ball.ycor() - 2)

    def hit_paddle(self, p_x, p_y):
        if self.ball.distance(p_x, p_y) < 25:
            if p_x < 0:
                self.ball.setheading(random.randint(0, 90))
            elif p_x > 0:
                self.ball.setheading(random.randint(90, 180))
