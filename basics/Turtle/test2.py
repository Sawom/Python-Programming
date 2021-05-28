import turtle
turtle.shape("turtle")
turtle.color("blue")
height = 8
width = 8
turtle.speed(1)
turtle.penup()

for y in range(height):
    for x in range(width):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(20*width)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)

turtle.exitonclick()