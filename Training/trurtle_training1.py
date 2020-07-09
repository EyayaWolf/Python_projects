import turtle

ninja = turtle.Turtle()
ninja.pencolor("red")
ninja.speed(10)

def square(length):
    for i in range(4):
        ninja.forward(length)
        ninja.right(90)
    for j in range(4):
        ninja.forward(length)
        ninja.left(90)
    for k in range(4):
        ninja.backward(length)
        ninja.left(90)
    for l in range(4):
        ninja.backward(length)
        ninja.right(90)


square(300)
square(250)
square(200)
square(150)
square(100)
square(50)
