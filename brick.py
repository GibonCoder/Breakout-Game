import turtle as t
from random_color_generator import random_color_generator as random_color


class Brick:
    def __init__(self):
        self.brick = t. Turtle()
        self.brick.shape('square')
        t.Screen().colormode(255)
        self.brick.color(random_color())
        self.brick.penup()
        self.brick.speed(0)
        self.brick.shapesize(stretch_len=1, stretch_wid=1)

    def get_x(self):
        return self.brick.xcor()

    def get_y(self):
        return self.brick.ycor()

    def is_break(self, bricks_list: list):
        self.brick.hideturtle()
        self.brick.goto(1000, 1000)
        bricks_list.remove(self)
