from turtle import Turtle, Screen

timmy_the_object = Turtle()
timmy_the_object.width(10)
def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        for c in ('blue', 'red', 'green'):
            timmy_the_object.color(c)
            timmy_the_object.forward(100)
            timmy_the_object.right(angle)
        

for shape_side_n in range(3,11):
    draw_shape(shape_side_n)

screen = Screen()


screen.exitonclick()