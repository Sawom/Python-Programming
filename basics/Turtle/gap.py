import turtle
turtle.shape("turtle")
turtle.color("orange")
turtle.speed(1)

for i in range(15):
    turtle.forward(30)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

turtle.exitonclick()