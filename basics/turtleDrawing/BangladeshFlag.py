import turtle
turtle.bgcolor("black")

def rectangle():
    turtle.goto(-250,150)
    turtle.color('darkgreen')
    turtle.begin_fill()

    for i in range(2):
        turtle.forward(500)
        turtle.right(90)
        turtle.forward(300)
        turtle.right(90)
    turtle.end_fill()

def circle():
    turtle.goto(0,-96)
    turtle.color("darkred")
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()

rectangle()
circle()
turtle.exitonclick()