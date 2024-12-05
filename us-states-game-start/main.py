import pandas
import  turtle

screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()

guess = []

while len(guess) < 50:

    answer = screen.textinput(title="Guess the state",
            prompt="What is another state name?").title()
    if answer == "Exit":
        missing_states = []
        for state in all_state:
            if state not in guess:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States to know")
        break
    if answer in all_state:
        guess.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)



# def mouse_click(x, y):
#     print(x, y)
#
# turtle.onscreenclick(mouse_click)

turtle.mainloop()
