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
ball.shape("triangle")
ball.penup()
ball.goto(0, 0)
ball.turtlesize(1.5)

#ball movement
ball_x = ball.xcor()
# ball_speed = 200
speed = 100

def ball_move():
    # ball_speed = random.randint(0, 350)
    # x = ball.xcor()
    # y = ball.ycor()
    # while x in range(-350, 350):
    #     ball.forward(ball_speed)
    #     x += ball_speed
    #     # y += ball_speed
    #     ball.setx(x)
    #     # y = ball.sety(y)
    # if x >= 350:
    #     #ball_speed *= -1
    #     ball.backward(ball_speed)
    #     x += ball_speed
    #     ball.setx(x)
    speed = 100
    sign = random.randint(0,1)
    if sign == 1:
       speed *= -1
    while ball.xcor() in range(-350, 350):
        ball.forward(speed)

    if ball.xcor() <= -350:
        #ball.forward(-speed)
        ball.goto(350, random.randint(-200, 200))
    if ball.xcor() >= 350:
        #ball.backward(speed)
        ball.goto(-350, random.randint(-200, 200))






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

def is_collided_with(self, run):
    return self.rect.colliderect(run.rect)


screen.listen()
screen.onkey(goalie2_move_up, 'Up')
screen.onkey(goalie2_move_down, 'Down')
screen.onkey(goalie1_move_up, 'w')
screen.onkey(goalie1_move_down, 's')

ball_x = ball.xcor()
g1_x = goalie1.xcor()
ball_y = ball.ycor()
g1_y = goalie1.xcor()


while True:
    #angle = 72
    screen.update()
    ball_move()



    # #if ball.xcor() <= 350:
    # if ball.xcor() in range(300, 350):
    #     ball.setx(goalie1.xcor() + 50)
    #     ball.setheading(ball.heading() + 180 + random.randint(0, 60))
    #     ball_speed = ball_speed * -1
    #
    # if ball.xcor() >= -350:
    #     ball.setx(goalie2.xcor() - 50)
    #     #ball.left(angle)
    #     ball.setheading(ball.heading() + 180 + + random.randint(0, 60))
    #     ball_speed = ball_speed * -1
    #
    # if ball.ycor() > 340:
    #     ball.sety(330)
    #     #ball.left(angle)
    #     ball.setheading(ball.heading() + 180 + random.randint(0, 60))
    #     ball_speed = ball_speed * -1
    #
    # if ball.ycor() < -340:
    #     ball.sety(-330)
    #     #ball.left(angle)
    #     ball.setheading(ball.heading() + 360 + random.randint(0, 60))
    #     # time.sleep(2)
    #     ball_speed = ball_speed * -1

    if ((ball.xcor() < goalie1.xcor() + 60 and ball.xcor() > goalie1.xcor() - 60) and (ball.ycor() < goalie1.ycor() + 60 and ball.ycor() > goalie1.ycor() - 60)):
        print("collision1")
        #angle += 72


    if ((ball.xcor() < goalie2.xcor() + 60 and ball.xcor() > goalie2.xcor() - 60) and (ball.ycor() < goalie2.ycor() + 60 and ball.ycor() > goalie2.ycor() - 60)):
        print("collision2")







