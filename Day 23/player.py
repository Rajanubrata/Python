from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.gotoStart()
        self.setheading(self.heading()+90)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    # check if it cross the end line
    def reach_destination(self):
        if self.ycor() > FINISH_LINE_Y:
            return True

    def gotoStart(self):
        self.goto(STARTING_POSITION)
