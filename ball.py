import turtle as t
import random


class Ball:
    def __init__(self):
        self.ball = t.Turtle()
        self.ball.shape('circle')
        self.ball.color('white')
        self.ball.penup()
        self.ball.speed(0)
        self.ball.goto(0, 0)
        self.ball.setheading(225)

    def move(self):
        if self.ball.heading() in range(0, 90):
            self.ball.setx(self.ball.xcor() + 5)
            self.ball.sety(self.ball.ycor() + 5)
        elif self.ball.heading() in range(90, 180):
            self.ball.setx(self.ball.xcor() - 5)
            self.ball.sety(self.ball.ycor() + 5)
        elif self.ball.heading() in range(180, 270):
            self.ball.setx(self.ball.xcor() - 5)
            self.ball.sety(self.ball.ycor() - 5)
        elif self.ball.heading() in range(270, 360):
            self.ball.setx(self.ball.xcor() + 5)
            self.ball.sety(self.ball.ycor() - 5)

    def hit_paddle(self, p_x, p_y):
        if self.ball.distance(p_x, p_y) < 30 and self.ball.ycor() < -250:
            if self.ball.heading() in range(270, 360):
                self.ball.setheading(random.randint(0, 90))
            elif self.ball.heading() in range(180, 270):
                self.ball.setheading(random.randint(90, 180))

    def hit_brick(self, b_x, b_y):
        if self.ball.distance(b_x, b_y) < 25:
            if self.ball.heading() in range(90, 180):
                self.ball.setheading(random.randint(180, 270))
            elif self.ball.heading() in range(0, 90):
                self.ball.setheading(random.randint(270, 360))
            return True

    def hit_wall(self):
        if self.ball.xcor() > 390 or self.ball.xcor() < -390:
            self.ball.setheading(180 - self.ball.heading())

    def is_out(self):
        if self.ball.ycor() < -300:
            return True
