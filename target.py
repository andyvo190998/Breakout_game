from turtle import Turtle
import time
class Target(Turtle):
    def __init__(self):
        super().__init__()
        self.target = []
        self.create_target()

    def create_target(self):
        x = -290
        y = 280
        for i in range (1,9):
            if x < 220 and y == 280:
                x += 65
                self.add_target(x=x,y=y)
        x2 = -290
        for i in range (1,9):
            if x2 < 220 and y == 280:
                x2 += 65
                self.add_target(x=x2,y=250)
        x3 = -290
        for i in range (1,9):
            if x3 < 220 and y == 280:
                x3 += 65
                self.add_target(x=x3,y=220)
    def add_target(self,x,y):
        target = Turtle("square")
        target.speed("fast")
        target.color("green")
        target.penup()
        target.shapesize(stretch_wid=1, stretch_len=3)
        target.setposition(x,y)
        self.target.append(target)

    def go_down(self):

        for item in self.target:
            y = item.ycor() - 50
            item.goto(item.xcor(), y)
        pass
    def remove_target(self,hit):
        hit.goto(x=400,y=600)