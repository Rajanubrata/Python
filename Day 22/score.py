from turtle import Turtle

class ScoreBord(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.color("white")
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 240)
        self.write(self.l_score, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 240)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))

    def L_increase(self):
        self.l_score += 1
        self.update()

    def R_increase(self):
        self.r_score += 1
        self.update()
