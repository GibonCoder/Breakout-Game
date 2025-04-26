import turtle as t
import random


class Ball:
    def __init__(self):
        self._ball = t.Turtle()
        self._ball.shape('circle')
        self._ball.color('white')
        self._ball.penup()
        self._ball.speed(0)
        self._ball.goto(0, 0)
        self._ball.setheading(225)

    def get_ball(self):
        return self._ball

    def move(self):
        if self._ball.heading() in range(0, 90):
            self._ball.setx(self._ball.xcor() + 5)
            self._ball.sety(self._ball.ycor() + 5)
        elif self._ball.heading() in range(90, 180):
            self._ball.setx(self._ball.xcor() - 5)
            self._ball.sety(self._ball.ycor() + 5)
        elif self._ball.heading() in range(180, 270):
            self._ball.setx(self._ball.xcor() - 5)
            self._ball.sety(self._ball.ycor() - 5)
        elif self._ball.heading() in range(270, 360):
            self._ball.setx(self._ball.xcor() + 5)
            self._ball.sety(self._ball.ycor() - 5)

    def hit_paddle(self, p_x, p_y):
        if self._ball.distance(p_x, p_y) < 30 and self._ball.ycor() < -250:
            if self._ball.heading() in range(270, 360):
                self._ball.setheading(random.randint(0, 90))
            elif self._ball.heading() in range(180, 270):
                self._ball.setheading(random.randint(90, 180))

    def hit_brick(self, b_x, b_y):
        if self._ball.distance(b_x, b_y) < 25:
            if self._ball.heading() in range(90, 180):
                self._ball.setheading(random.randint(180, 270))
            elif self._ball.heading() in range(0, 90):
                self._ball.setheading(random.randint(270, 360))
            return True

    def hit_wall(self):
        if self._ball.xcor() > 390 or self._ball.xcor() < -390:
            self._ball.setheading(180 - self._ball.heading())

    def is_out(self):
        if self._ball.ycor() < -300:
            return True
