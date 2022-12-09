from turtle import Screen, Turtle
from paddle import Paddle
from target import Target
from ball import Ball

import time


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("BREAKOUT")
screen.tracer(0)

#create ball
ball = Ball()

#create targets
target = Target()

# create player
player = Paddle()


#player movements
screen.listen()
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")


game_is_on = True
time = 0

while game_is_on:
    screen.update()
    time += 1

    ball.move()
    if ball.xcor() >=280 or ball.xcor() <=-280:
        ball.bound_x()
    if ball.ycor() >=280:
        ball.bound_y()
    if ball.ycor() <=-280:
        game_is_on = False
        print("game over!")


    if ball.distance(player) < 40:
        ball.bound_y()
    for i in target.target:
        if ball.distance(i)<40:
            ball.bound_y()
            target.remove_target(i)

        if i.ycor() == -250:
            print("game over!")
            game_is_on = False


    if time == 700:
        target.go_down()
        time = 0
    if len(target.target) ==0:
        game_is_on = False
        print("you win")

screen.exitonclick()