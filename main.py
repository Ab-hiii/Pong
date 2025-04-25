from math import gamma

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.screensize(800, 600)
screen.title("Pong")
screen.tracer(0)
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
l_score = Score((-50, 250))
r_score = Score((50,250))
ball = Ball()
screen.listen()






screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_ison = False

def start():
    global game_ison, ball_speed
    game_ison = True

    while game_ison:
        screen.update()
        ball.move()
        time.sleep(0.02)
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() < -325:
            ball.inc_speed()
            ball.bounce_x()


        if ball.xcor() > 400 :
            l_score.update_score()
            ball.refresh("left")
            game_ison = False


        if ball.xcor() < -400:
            r_score.update_score()
            ball.refresh("right")
            game_ison = False




screen.onkeypress(start, "space")








screen.exitonclick()