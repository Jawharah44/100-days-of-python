from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboared
import time

tom = Turtle()
screen = Screen()
ball = Ball()
scoreboared = Scoreboared()

screen.setup(width=800, height= 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle((305,0))
paddle_2 = Paddle((-305,0))

screen.listen()
screen.onkey(paddle_1.go_up,"Up")
screen.onkey(paddle_1.go_down,"Down")

screen.onkey(paddle_2.go_up,"w")
screen.onkey(paddle_2.go_down,"s")

game_is_on = True 

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < 320 : 
        ball.bounce_x()
        
    #detect right paddle misses
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboared.l_point()
    
    #detect left paddle misses
    if ball.xcor() < -380 :
        ball.reset_position()
        scoreboared.r_point()
screen.exitonclick()