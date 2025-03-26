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

    def set_position(self, x, y):
        self.brick.setx(x)
        self.brick.sety(y)