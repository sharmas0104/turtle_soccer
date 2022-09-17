

import turtle
screen = turtle.Screen()
screen.setup(1000, 1000)
# screen.screensize(500,500)
screen.bgcolor("green")

goal1 = turtle.Turtle()
goal1.color("brown")
goal1.shape("square")
goal1.penup()
goal1.goto(-490, 0)
goal1.turtlesize(stretch_wid=20, stretch_len=10)


goal2 = turtle.Turtle()
goal2.color("brown")
goal2.shape("square")
goal2.penup()
goal2.goto(490, 0)
goal2.turtlesize(stretch_wid=20, stretch_len=10)

ball = turtle.Turtle()
ball.color("#cdd4c7")
ball.shape("circle")
ball.penup()
ball.goto(0, 0)
ball.turtlesize(1.5)

goalie1 = turtle.Turtle()
goalie1.color("#2914e3")
goalie1.shape("circle")
goalie1.penup()
goalie1.goto(-390, 0)
goalie1.turtlesize(3)
goalie1.left(90)

goalie2 = turtle.Turtle()
goalie2.color("#2914e3")
goalie2.shape("circle")
goalie2.penup()
goalie2.goto(390, 0)
goalie2.turtlesize(3)
goalie2.left(90)


def move_up():

    if goalie2.pos()[1] <= 150:
        goalie2.forward(50)


def move_down():

    if goalie2.pos()[1] >= -150:
        goalie2.backward(50)


def move1_up():

    if goalie1.pos()[1] <= 150:
        goalie1.forward(25)


def move1_down():

    if goalie1.pos()[1] >= -150:
        goalie1.backward(25)


while True:
    screen.update()
    screen.onkeypress(move_up, 'Up')
    screen.onkeypress(move_down, 'Down')
    screen.onkeypress(move1_up, 'w')
    screen.onkeypress(move1_down, 's')
    screen.listen()
