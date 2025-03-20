import turtle as t
from random_color_generator import random_color_generator as random_color


class Brick:
    def __init__(self):
        self.brick = t. Turtle()
        self.brick.shape('square')
        self.brick.color(random_color())

    def set_size(self, size):
        match size:
            case 'small':
                self.brick.shapesize(stretch_len=1, stretch_wid=1)
            case ' medium':
                self.brick.shapesize(stretch_len=2, stretch_wid=1)
            case 'large':
                self.brick.shapesize(stretch_len=3, stretch_wid=1)
