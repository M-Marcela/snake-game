from turtle import Turtle

class Borders(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(-310, -310)
        self.color("white")
        self.goto(-310, 310)
        self.goto(310, 310)
        self.goto(310, -310)
        self.goto(-310, -310)
