import turtle as t


class Screen:
    def __init__(self):
        self.screen = t.Screen()
        self.screen.title("Breakout Game")
        self.screen.bgcolor('black')
        self.screen.setup(width=800, height=600)

    def run_screen(self):
        self.screen.mainloop()
