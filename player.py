import turtle as t


class Player:
    def __init__(self):
        self.player = t.Turtle()
        self.player.shape('square')
        self.player.color('green')
        self.player.shapesize(stretch_wid=5, stretch_len=1)
        self.player.penup()
