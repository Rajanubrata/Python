from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from score import ScoreBord

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()
score = ScoreBord()

screen.listen()
screen.onkey(paddle_right.go_up, "i")
screen.onkey(paddle_right.go_down, "j")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    ball.move()

    # check collision with upper and lower wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # check collision with paddle
    if ball.xcor() > 320 and ball.distance(paddle_right) < 50 or ball.xcor() < -320 and ball.distance(paddle_left) < 50:
        ball.bounce_x()

    # collision with right_wall
    if ball.xcor() > 380:
        ball.reset()
        score.L_increase()

    # collision with left_wall
    if ball.xcor() < -380:
        ball.reset()
        score.R_increase()

screen.exitonclick()
