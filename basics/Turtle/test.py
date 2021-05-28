import turtle
turtle.shape("turtle")
turtle.color("orange")
turtle.speed(1)

for i in range(50,100,10):
    for j in range(4):
        turtle.forward(i)
        turtle.left(90)

turtle.exitonclick()