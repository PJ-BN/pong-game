from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.7)
        self.penup()
        self.color("blue")

        self.setheading(0)

    def move(self):
        self.forward(6)

    def refresh(self):
        self.goto(0, 0)

        self.setheading(0)
