from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.Level = 0
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-280, 250)
        self.next_level()

    def next_level(self):
        self.Level += 1
        self.clear()
        self.write(f"Level: {self.Level}", font=(FONT))

    def game_over(self):
        self.goto(-20, 0)
        self.write("GAME OVER", font=("Courier", 24, "bold"))
