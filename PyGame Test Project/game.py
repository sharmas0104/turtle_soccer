import turtle
import random
import time


#screen setup
screen = turtle.Screen()
screen.setup(1000, 1000)
screen.bgcolor("green")


#goal1 setup
goal1 = turtle.Turtle()
goal1.color("brown")
goal1.shape("square")
goal1.penup()
goal1.goto(-490, 0)
goal1.turtlesize(stretch_wid=20, stretch_len=10)


#goal2 setup
goal2 = turtle.Turtle()
goal2.color("brown")
goal2.shape("square")
goal2.penup()
goal2.goto(490, 0)
goal2.turtlesize(stretch_wid=20, stretch_len=10)

#ball setup
ball = turtle.Turtle()
ball.color("#cdd4c7")
ball.shape("triangle")
ball.penup()
ball.goto(0, 0)
ball.turtlesize(1.5)


#player 1 setup
goalie1 = turtle.Turtle()
goalie1.color("#2914e3")
goalie1.shape("circle")
goalie1.penup()
goalie1.goto(-390, 0)
goalie1.turtlesize(3)
goalie1.left(90)

#player 2 setup
goalie2 = turtle.Turtle()
goalie2.color("#2914e3")
goalie2.shape("circle")
goalie2.penup()
goalie2.goto(390, 0)
goalie2.turtlesize(3)
goalie2.left(90)


def goalie2_move_up():
    y = goalie2.ycor()
    y += 50
    goalie2.sety(y)


def goalie2_move_down():
    y = goalie2.ycor()
    y -= 50
    goalie2.sety(y)


def goalie1_move_up():
    y = goalie1.ycor()
    y += 50
    goalie1.sety(y)


def goalie1_move_down():
    y = goalie1.ycor()
    y -= 50
    goalie1.sety(y)


def move_ball():

    # 0 means randomize the x coordinate, 1 means randomize the y coordinate
    random_coord = random.randint(0, 1)
    # determine if the remaining coordinate will be negative or positive
    sign = random.randint(0, 1)
    x_pos = 500
    y_pos = 500
    if random_coord == 0:
        x_pos = random.randint(-500, 500)
        if sign == 1:
            y_pos *= -1
    else:
        y_pos = random.randint(-500, 500)
        if sign == 1:
            x_pos *= -1

    ball.goto(x_pos, y_pos)
    print(x_pos, y_pos)


screen.listen()
screen.onkey(goalie2_move_up, 'Up')
screen.onkey(goalie2_move_down, 'Down')
screen.onkey(goalie1_move_up, 'w')
screen.onkey(goalie1_move_down, 's')


while True:
    screen.update()
    move_ball()





