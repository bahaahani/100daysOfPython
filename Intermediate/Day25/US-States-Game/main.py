import turtle
import pandas

screen = turtle.Screen()
screen.title("US STATES GAME")

image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guess_states = []

while len(guess_states) < 50:
    answer = screen.textinput(f"{(len(guess_states))}/50 states guessed", "whats another state's name")
    answer = answer.title()
    if answer == 'Exit':
        break
        missing_state = []
        for state in all_states:
            if state not in guess_states:
                missing_state.append(state)
        new_Data = pandas.DataFrame(missing_state)
        new_Data.to_csv("States_missing.csv")
    if answer in all_states:
        guess_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)


#states to learn.csv



screen.exitonclick()
