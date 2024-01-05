import turtle

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()

my_screen.setup(width=500, height=400)
# width = 500, height = 400

user_bet = my_screen.textinput(title="Make a bet on turtle", prompt="Type turtle colour to make a bet: ")
print(user_bet)

my_turtle.shape("turtle")
my_turtle.penup()
my_turtle.goto(-230, 0)

my_screen.exitonclick()
