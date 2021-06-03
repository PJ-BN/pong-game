from turtle import Turtle, Screen
import random
import time

from paddle_1 import PaddleOne
from paddle_2 import PaddleTwo
from ball import Ball
from score import Score

screen = Screen()

paddle_1 = PaddleOne()
paddle_2 = PaddleTwo()
ball = Ball()
score = Score()

screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

screen.listen()
screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")

screen.onkey(paddle_2.up, "w")
screen.onkey(paddle_2.down, "s")

x_cord = 0
y_cord = 270

y_down = -300
y_up = 300

x_right = 420
x_left = -420


def line():
    tur = Turtle("square")
    tur.penup()
    tur.shapesize(0.7, 0.25)
    tur.color("white")
    tur.goto(x_cord, y_cord)
    screen.update()


while y_cord > -280:
    line()
    y_cord -= 30

game = True

while game:
    screen.update()
    ball.move()
    ran1 = random.randint(195, 230)
    ran2 = random.randint(15, 50)
    score_first = 0
    score_second = 0

    if ball.distance(paddle_1) < 30:
        ball.setheading(ran1)

    if ball.distance(paddle_2) < 30:
        ball.setheading(ran2)

    for x_tot in range(-400, 400):

        if ball.distance(x_tot, y_down) < 10:

            ref = ran1 - 180
            ref_tot = 180 - ref
            ball.setheading(ref_tot)

        if ball.distance(x_tot, y_up) < 10:
            ref = 360 - ran2

            ball.setheading(ref)

    for y_tot in range(-300, 300):

        if ball.distance(x_right, y_tot) < 15:
            score.score_second += 1
            score.increase()
            ball.refresh()
            paddle_1.goo()
            paddle_2.goo()
            screen.update()
            time.sleep(3)

        if ball.distance(x_left, y_tot) < 15:
            score.score_first += 1
            score.increase()
            ball.refresh()
            paddle_1.goo()
            paddle_2.goo()
            screen.update()
            time.sleep(3)

screen.exitonclick()
