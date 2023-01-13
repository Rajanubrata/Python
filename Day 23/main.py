import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

# Make objects here 👇
player = Player()
car = CarManager()
level = Scoreboard()

# TODO 1: move the turtle
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    # Todo 2: detect collision with cars
    for Car in car.car_house:
        if Car.distance(player) < 25:
            game_is_on = False
            level.game_over()

    # Todo 3: check if player win
    if player.reach_destination():
        player.gotoStart()
        level.next_level()
        car.speedUp()

screen.exitonclick()
