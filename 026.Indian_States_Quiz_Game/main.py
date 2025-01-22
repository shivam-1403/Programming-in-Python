import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian States Quiz Game")
image = r"Programming-in-Python\026.Indian_States_Quiz_Game\indian_map-ezgif.com-resize.gif"
screen.addshape(image)
screen.setup(width=1000, height=750)
turtle.shape(image)
turtle.penup()
turtle.speed("fastest")
turtle.goto(-230, 50)
data = pandas.read_csv(r"Programming-in-Python\026.Indian_States_Quiz_Game\states_data_.csv")
states_list = data["state"].to_list()

user_guesses = []
while len(user_guesses) < 28:
    answer_state = screen.textinput(title=f"{len(user_guesses)}/28", prompt="What's another state's name ?").title()

    if answer_state == "Exit":
        missing_state = []
        for state in states_list :
            if state not in user_guesses:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv(r"Programming-in-Python\026.Indian_States_Quiz_Game\states_to_learn.csv")
        break
    if answer_state in states_list:
        user_guesses.append(answer_state)
        tim = turtle.Turtle()
        tim.penup()
        tim.hideturtle()
        state_data = data[data["state"] == answer_state]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write((f"◉ {answer_state}"))

