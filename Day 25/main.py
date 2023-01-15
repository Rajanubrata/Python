import turtle
import pandas

screen = turtle.Screen()
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

score = 0
guessState = []

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

while len(guessState) < 50:
    answer_state = turtle.textinput(title=f"{len(guessState)}/50 Correct", prompt="What's another state's name").title()

    if answer_state == "Exit":
        missed = []
        for state in all_states:
            if state not in guessState:
                missed.append(state)
        new_data = pandas.DataFrame(missed)
        new_data.to_csv("missed_state.csv")
        break

    if answer_state in all_states:
        guessState.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        stateData = data[data.state == answer_state]
        t.goto(int(stateData.x), int(stateData.y))
        t.write(answer_state)
