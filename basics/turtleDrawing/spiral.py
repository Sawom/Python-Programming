import turtle
sc=turtle.Screen()
sc.setup(600, 600)
spiral=turtle.Turtle()
spiral.speed(6)
sc.bgcolor("black")
col = ("cyan", "blue", "yellow", "green","blue", "grey")
c=0
for i in range(110):
    spiral.pensize(2)
    spiral.forward(i*5)
    spiral.right(144)
    spiral.color(col[c])
    if c==3:
       c=0
    else:
       c+=1

turtle.exitonclick()