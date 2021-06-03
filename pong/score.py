from turtle import Turtle


class Score(Turtle):

    def __init__(self):

        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("red")
        self.score_first = 0
        self.score_second = 0
        self.goto(-45, 260)
        self.write(0, False, "center", ("Arial", 25, "normal"))
        self.goto(45, 260)
        self.write(0, False, "center", ("Arial", 25, "normal"))

    def increase(self):
        self.clear()

        self.goto(-45, 260)
        self.write(self.score_second, False, "center", ("Arial", 25, "normal"))

        self.goto(45, 260)
        self.write(self.score_first, False, "center", ("Arial", 25, "normal"))


