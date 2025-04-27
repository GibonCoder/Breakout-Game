import turtle as t
from random_color_generator import random_color_generator as random_color


class Brick:
    def __init__(self, x, y):
        self._brick = t. Turtle()
        self._brick.shape('square')
        t.Screen().colormode(255)
        self._brick.color(random_color())
        self._brick.penup()
        self._brick.speed(0)
        self._brick.shapesize(stretch_len=1, stretch_wid=1)
        self._brick.goto(x, y)

    def get_x(self):
        return self._brick.xcor()

    def get_y(self):
        return self._brick.ycor()

    def is_break(self, bricks_list: list):
        self._brick.hideturtle()
        self._brick.goto(1000, 1000)
        bricks_list.remove(self)
