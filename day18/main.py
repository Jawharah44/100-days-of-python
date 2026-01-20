# import colorgram

# colors = colorgram.extract('day18/image.jpeg', 30)

# lst = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     lst.append(new_color)

# print(lst)

from turtle import Turtle, Screen
import random


color_list = [(198, 173, 119), (214, 225, 218), (222, 224, 229), (162, 100, 54), (126, 35, 23), (185, 158, 50), (5, 55, 83), (51, 32, 28), (110, 68, 86), (116, 162, 176), (22, 120, 171), (76, 34, 43), (66, 154, 132), (83, 140, 64), (7, 65, 44), (184, 97, 79), (128, 37, 41), (204, 201, 147), (145, 178, 162), (174, 152, 157), (177, 201, 185), (219, 182, 168), (25, 80, 60), (12, 79, 100), (166, 106, 110), (73, 148, 170), (208, 184, 189), (180, 197, 201)]
    


tom = Turtle()
screen = Screen()
tom.penup()
tom.hideturtle()
screen.colormode(255)
tom.setheading(225)
tom.forward(300)
tom.setheading(0)

number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
    tom.dot(20,random.choice(color_list))
    tom.forward(50)
    if dot_count % 10 == 0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)
screen.exitonclick()