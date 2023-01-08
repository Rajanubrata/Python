# Using colorgram Api to extract color of an image
# import colorgram

# colors = colorgram.extract('img.jpg', 10)
# container = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     container.append((r, g, b))
# print(container)

import turtle as t
import random
t.colormode(255)
color = [(253, 251, 248), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68),
         (238, 227, 5), (229, 159, 46), (27, 40, 157)]


timmi = t.Turtle()
timmi.shape("turtle")
timmi.penup()
timmi.setheading(225)
timmi.forward(300)
timmi.setheading(0)
timmi.speed("fast")
t.Screen().bgcolor("black")
dot_count = 100
for dots in range(1, dot_count+1):
    timmi.dot(20, random.choice(color))
    timmi.forward(50)
    if dots % 10 == 0:
        timmi.setheading(90)
        timmi.forward(50)
        timmi.setheading(180)
        timmi.forward(500)
        timmi.setheading(0)

screen = t.Screen()
screen.exitonclick()
