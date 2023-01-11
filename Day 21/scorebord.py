from turtle import Turtle
SCORE = 0

class Score_Bord(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.update()
        self.hideturtle()

    def add_score(self):
        global SCORE
        SCORE += 1
        self.update()

    def update(self):
        self.penup()
        self.goto(0, 270)
        self.clear()
        self.write(f"Score : {SCORE}", align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 25, "normal"))
