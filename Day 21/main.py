import time
from turtle import Screen
from snake import Snake
from food import Food
from scorebord import Score_Bord


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)
snake = Snake()
food = Food()
score = Score_Bord()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # if collision with snake then re adjust the food position
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score.add_score()

    # check if collide with wall
    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        is_game_on = False
        score.game_over()

    # check if collid with tail
    for segment in snake.segment[1:-1]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()
