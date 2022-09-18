import turtle
import random
import time

#screen setup
screen = turtle.Screen()
screen.setup(1000, 700)
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
ball.shape("circle")
ball.penup()
ball.goto(0, 0)
ball.turtlesize(1.5)



#pen
pen = turtle.Turtle()
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("Goalie 1 : 0    Goalie 2: 0",
          align="center", font=("Courier", 24, "normal"))


def ball_move():
    goalie1_score = 0
    goalie2_score = 0
    speed = 100
    if ball.pos() == (0, 0):
        sign = random.randint(0, 1)
        if sign == 1:
            speed *= -1

    while ball.xcor() in range(-700, 700):

        y = ball.ycor()
        dy = random.randint(-100, 100)
        if y + dy in range(-200, 200):
            y += dy
        x = ball.xcor()
        dx = speed
        x += dx
        ball.goto(x, y)

        check_score(goalie1_score, goalie2_score)

        if ((ball.xcor() < goalie1.xcor() + 60 and ball.xcor() > goalie1.xcor() - 60) and (ball.ycor() < goalie1.ycor() + 60 and ball.ycor() > goalie1.ycor() - 60)):
            print("collision1")

            speed = -speed
            ball.forward(speed)




        if ((ball.xcor() < goalie2.xcor() + 60 and ball.xcor() > goalie2.xcor() - 60) and (ball.ycor() < goalie2.ycor() + 60 and ball.ycor() > goalie2.ycor() - 60)):
            print("collision2")

            speed = -speed
            ball.forward(speed)




        if (ball.xcor() < -500):

            goalie2_score += 1
            pen.clear()
            pen.write("Goalie 1 : {}    Goalie 2: {}".format(
                goalie1_score, goalie2_score), align="center",
                font=("Courier", 24, "normal"))


            speed = -speed
            ball.forward(speed)
            ball.home()


        if (ball.xcor() > 500):
            goalie1_score += 1
            pen.clear()
            pen.write("Goalie 1 : {}    Goalie 2: {}".format(
                goalie1_score, goalie2_score), align="center",
                font=("Courier", 24, "normal"))
            #ball.goto(-500, random.randint(-350, 350))
            speed = -speed
            ball.forward(speed)
            ball.home()



#player 1 setup
goalie1 = turtle.Turtle()
goalie1.color("#2914e3")
goalie1.shape("turtle")
goalie1.penup()
goalie1.goto(-390, 0)
goalie1.turtlesize(3)
goalie1.left(90)

#player 2 setup
goalie2 = turtle.Turtle()
goalie2.color("#2914e3")
goalie2.shape("turtle")
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


def check_score(goalie1_score, goalie2_score):
    if(goalie2_score == 15 and goalie2_score > goalie1_score):
        pen.clear()
        pen.write("Goalie 2 won!", align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.color("#e3d624")


    if(goalie1_score == 15 and goalie1_score > goalie2_score):
        pen.clear()
        pen.write("Goalie 1 won!", align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.color("#e3d624")




screen.listen()
screen.onkey(goalie2_move_up, 'Up')
screen.onkey(goalie2_move_down, 'Down')
screen.onkey(goalie1_move_up, 'w')
screen.onkey(goalie1_move_down, 's')


run = True
while run:

    screen.update()
    ball_move()







