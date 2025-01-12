from turtle import Turtle, Screen

tim = Turtle()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_counter_clockwise():
    tim.left(10)

def move_clockwise():
    tim.right(10)

def clear():
    tim.reset()
    tim.home()

screen = Screen()
screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=move_counter_clockwise, key="d")
screen.onkey(fun=move_clockwise, key="a")
screen.onkey(fun=clear, key="c")
screen.exitonclick()