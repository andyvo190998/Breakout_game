from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.color("red")
        self.penup()
        self.shape("circle")
        self.setposition(0,-250)
        self.xmove = 3
        self.ymove = 3
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bound_y(self):
        self.ymove *= -1

    def bound_x(self):
        self.xmove *= -1