import turtle
turtle.shape("turtle")
turtle.color("orange")
turtle.speed(1)

for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.forward(150)
turtle.color("blue")
for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.exitonclick()