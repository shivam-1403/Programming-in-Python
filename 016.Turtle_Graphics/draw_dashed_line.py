from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")

for _ in range(50) :
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


screen = Screen()
screen.exitonclick()