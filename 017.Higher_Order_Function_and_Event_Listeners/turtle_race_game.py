from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width= 500, height= 400)

user_bet = screen.textinput(title="Make Your Bet !!", prompt="Which Turtle will win the race ? Enter a color (purple/blue/green/yellow/orange/red) : ").lower()
print(user_bet)

colors= ["purple", "blue", "green", "yellow", "orange", "red"]
y_positions = [125, 75, 25, -25, -75, -125]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape= "turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x= -230, y= y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet :
    is_race_on = True

while is_race_on :
    for turtle in all_turtles :
        if turtle.xcor() > 230 :
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet :
                print(f"You've Won ! The {winning_color} turtle is the winner.")
            else :
                print(f"You've Lost ! The {winning_color} turtle is the winner.")
        random_pace = random.randint(0,10)
        turtle.forward(random_pace)

screen.exitonclick()