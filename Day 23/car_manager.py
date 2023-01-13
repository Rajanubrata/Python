from turtle import Turtle
from random import *

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_house = []
        self.carspeed = STARTING_MOVE_DISTANCE


    def create_car(self):
        creator =  randint(1, 6)
        if creator == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.color(choice(COLORS))
            y_cor = randint(-250, 250)
            new_car.goto(300, y_cor)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.car_house.append(new_car)

    def move(self):
        for car in self.car_house:
            car.backward(self.carspeed)

    def speedUp(self):
        self.carspeed += MOVE_INCREMENT
