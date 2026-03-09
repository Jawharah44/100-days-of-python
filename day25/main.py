import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "day25/blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
data = pd.read_csv("day25/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title= f"{len(guessed_states)}/50 States Correct", prompt= "What's another state's name?").title()

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        print(state_data)
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

screen.exitonclick()