import turtle
t = turtle.Turtle()
turtle.title("Love Shape Programming")
screen = turtle.Screen()
screen.bgcolor("black")
t.color("yellow", "red")
t.begin_fill()
t.pensize(3)
t.fillcolor("red")
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(180)
t.end_fill()
t.begin_fill()
t.fillcolor("green")
t.left(140)
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(180)
t.end_fill()
t.begin_fill()
t.fillcolor("blue")
t.left(140)
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(180)
t.end_fill()
t.exitonclick()