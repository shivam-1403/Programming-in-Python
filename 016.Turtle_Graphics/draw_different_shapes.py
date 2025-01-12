#This will draw Triangle, Square, Pentagon, Hexagon, Heptagon, Octagon, Nonagon, Decagon Pattern.


from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")

colors = ["black", "red", "blue", "green", "DeepPink2", "aquamarine3", "chocolate", "yellow"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides) :
        tim.forward(50)
        tim.right(angle)

def start ():
    for sides in range(3,10) :
        tim.color(random.choice(colors))
        draw_shape(sides)

for _ in range(6):
    start()
    tim.forward(50)
    tim.left(60)


screen = Screen()
screen.exitonclick()