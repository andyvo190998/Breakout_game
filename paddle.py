from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setposition(0,-270)

    def go_left(self):
        if self.xcor() > -260:
            self.goto(self.xcor() - 10, -270)
        else:
            pass

    def go_right(self):
        if self.xcor() < 260:
            self.goto(self.xcor() + 10, -270)
        else:
            pass