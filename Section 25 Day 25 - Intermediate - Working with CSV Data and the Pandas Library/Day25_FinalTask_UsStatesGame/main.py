import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# # x and y values of the 50_states.csv are obtained using below code
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# screen.mainloop()  # used instead of screen.exitonclick() so that screen remains even after a click


data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # t.write(answer_state)
        t.write(state_data.state.item())

missed_states = []
for state in all_states:
    if state not in guessed_states:
        missed_states.append(state)
new_data = pandas.DataFrame(missed_states)
new_data.to_csv("States_to_learn.csv")