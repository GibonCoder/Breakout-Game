import turtle as t


class Player:
    def __init__(self):
        self.player = t.Turtle()
        self.player.shape('square')
        self.player.color('green')
        self.player.shapesize(stretch_wid=1, stretch_len=5)
        self.player.penup()
        self.player.goto(0, -280)
        self.player.speed(1)

    def move_left(self):
        x = self.player.xcor()
        x -= 20
        if x < -347:
            x = -347
        self.player.setx(x)

    def move_right(self):
        x = self.player.xcor()
        x += 20
        if x > 340:
            x = 340
        self.player.setx(x)

