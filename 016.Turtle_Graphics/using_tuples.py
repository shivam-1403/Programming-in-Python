#Let we create a random walk with random colors using Tuples

# A Tuple is the immutable collection of data items stored in ()
# eg -->  my_tuple = (1, 3, 8)

import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

tim = Turtle()
tim.shape("turtle")
tim.pensize(15)
tim.speed("fastest")

def random_colors() :
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r, g, b)
    return random_color


direction = [0, 90, 180, 270]

for _ in range(200):
    tim.color(random_colors())
    tim.forward(20)
    tim.setheading(random.choice(direction))



screen = Screen()
screen.exitonclick()