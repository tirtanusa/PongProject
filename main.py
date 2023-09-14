from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height= 600)
screen.bgcolor("Black")
screen.tracer(0)
r_paddle = Paddle(350)
l_paddle = Paddle(-350)
score = Scoreboard()
ball = Ball()
line = Turtle()
line.goto(x=0, y=300)
line.seth(270)
line.color("white")
line.pensize(20)
for i in range (0,250):
    line.pendown()
    line.forward(30)
    line.penup()
    line.forward(30)
    
screen.update()

screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")
speed = 0.07

game_is_on = True
while game_is_on :
    screen.update()
    time.sleep(speed)
    ball.move()
    
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.xcor() > 330 and ball.distance(r_paddle) < 50 or ball.xcor() < -330 and ball.distance(l_paddle) <50:
        ball.bounce_x()
        speed *= 0.5
    
    if ball.xcor() > 380:
        speed = 0.07
        ball.restart()
        ball.bounce_x()
        score.l_point()

    elif ball.xcor() < -380:
        speed = 0.07
        ball.restart()
        ball.bounce_x()
        score.r_point()






screen.exitonclick()