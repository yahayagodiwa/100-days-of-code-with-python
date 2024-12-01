from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race? ")

colors = ["red", "green", "yellow", "orange", "Blue"]
y_position = [-70, -40, -10, 20, 50]
turtles = []
is_race = False

for i in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-240, y= y_position[i])
    turtles.append(new_turtle)

if user_bet:
    is_race = True
while is_race:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turle is the winner")
            else:
                print(f"You have lost! The {winning_color} turle is the winner")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()


        

