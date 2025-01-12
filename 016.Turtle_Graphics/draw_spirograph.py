# We will make a spirograph using no. of circles

import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")

def random_colors() :
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r, g, b)
    return random_color

def draw_spirograph(size_of_gap) :
    for _ in range(int(360 / size_of_gap)) :
        tim.pencolor(random_colors())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(4)

screen = Screen()
screen.exitonclick()