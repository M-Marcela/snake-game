from turtle import Turtle

ALIGHMENT = "center"
FONT = ("Courier", 14, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 310)
        self.update_score_text()

    def update_score_text(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  Hight Score: {self.high_score}", align=ALIGHMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score_text()

    def calculate_score(self):
        self.score += 1
        self.update_score_text()
