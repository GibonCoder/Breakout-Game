import turtle as t


class Player:
    def __init__(self):
        self.player = t.Turtle()
        self.player.shape('square')
        self.player.color('green')
        self.player.shapesize(stretch_wid=1, stretch_len=5)
        self.player.penup()
        self.player.goto(0, -280)

