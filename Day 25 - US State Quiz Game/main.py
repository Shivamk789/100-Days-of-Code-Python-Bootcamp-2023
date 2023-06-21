import turtle
import pandas as pd

screen = turtle.Screen()
t = turtle.Turtle()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")

guess = []

while len(guess) < 50:
    answer = screen.textinput(title=f"{len(guess)}/50",
                              prompt="What's another State name?").title()
    all_states = data["state"].to_list()

    if answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guess:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in all_states:
        guess.append(answer)
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)

