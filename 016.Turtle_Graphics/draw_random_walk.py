from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.pensize(15)
tim.speed("fastest")

colors = ["black", "red", "blue", "green", "DeepPink2", "aquamarine3", "chocolate", "yellow"]
direction = [0, 90, 180, 270]

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(20)
    tim.setheading(random.choice(direction))


screen = Screen()
screen.exitonclick()