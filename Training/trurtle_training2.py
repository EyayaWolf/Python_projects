import turtle

ninja = turtle.Turtle()
ninja.pencolor("red")
ninja.speed(10)

def geometry(length):
    for i in range(6):
        ninja.forward(length)
        ninja.right(60)
    for j in range(6):
        ninja.forward(length)
        ninja.left(60)
    for k in range(6):
        ninja.backward(length)
        ninja.left(60)
    for l in range(6):
        ninja.backward(length)
        ninja.right(60)


geometry(50)
geometry(45)
geometry(30)
geometry(25)
geometry(20)
geometry(15)
