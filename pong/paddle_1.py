from turtle import Turtle, Screen

screen = Screen()

X_cord = 370
Y_cord = 0


class PaddleOne(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.shapesize(0.6, 3)
        self.color("white")
        self.speed(0)
        self.goo()

    def goo(self):

        self.goto(X_cord, Y_cord)

    def up(self):

        self.forward(50)

    def down(self):

        self.backward(50)





