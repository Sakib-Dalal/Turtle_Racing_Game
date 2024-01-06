""" Code Written by Sakib Dalal, GitHub:- https://github.com/Sakib-Dalal"""

import turtle
import random

is_race_on = False
my_screen = turtle.Screen()
my_screen.setup(width=500, height=400)
# width = 500, height = 400

user_bet = my_screen.textinput(title="Make a bet on turtle", prompt="Type turtle colour to make a bet "
                                                                    "red/orange/yellow/green/blue/purple: ")
print(f"your bet 🐢: {user_bet}")
turtle_colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coordinate = [-100, -50, 0, 50, 100, 150]
all_turtles = []

if user_bet:
    is_race_on = True

for turtles in range(0, 5):
    my_turtle = turtle.Turtle(shape="turtle")
    my_turtle.penup()
    my_turtle.color(turtle_colours[turtles])
    my_turtle.goto(x=-230, y=y_coordinate[turtles])
    all_turtles.append(my_turtle)

line_lst = [-215, 230]


def my_race_line(lst):
    race_line = turtle.Turtle()
    race_line.hideturtle()
    for x in range(len(lst)):
        race_line.penup()
        race_line.goto(lst[x], 200)
        race_line.right(90)
        race_line.pendown()
        race_line.goto(lst[x], -200)


my_race_line(line_lst)
while is_race_on:
    for i in range(len(all_turtles)):
        if all_turtles[i].xcor() > 220:
            print(f"{all_turtles[i].pencolor()} 🐢 is the winner 🏁")
            if user_bet == all_turtles[i].pencolor():
                print("You won the race! 🥳")
            else:
                print("You lost the race! 😭")
            is_race_on = False
            break
        random_move = random.randint(0, 10)
        all_turtles[i].forward(random_move)

my_screen.exitonclick()
