import turtle

class ajobTurtle(turtle.Turtle):
    def forward(self,pixel):
        super().backward(pixel)

    def backward(self,pixel):
        super().forward(pixel)

    def left(self,angle):
        super().right(angle)

    def right(self,angle):
        print("I won't turn right because its her choice, XDD")

if __name__ == '__main__' :
    montu = ajobTurtle()
    montu.left(30)
    montu.forward(200)
    montu.left(45)
    montu.backward(100)
    montu.right(90)
    montu.forward(10)

    jhontu = turtle.Turtle()
    jhontu.shape("turtle")
    jhontu.left(30)
    jhontu.forward(200)
    jhontu.left(45)
    jhontu.backward(100)
    jhontu.right(90)
    jhontu.forward(10)

turtle.done()