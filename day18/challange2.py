from turtle import Turtle, Screen
import random 

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color =  (r,g,b)
    return random_color

timmy = Turtle()
screen = Screen()
screen.colormode(255)


timmy.width(10)

directions = [0, 90, 180, 270]

for i in range(200):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))


screen.exitonclick()