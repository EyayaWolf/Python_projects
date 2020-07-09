import turtle

ninja = turtle.Turtle()
ninja.pencolor("red")
ninja.speed(10)

def square(length, angle, corner):
    for i in range(corner):
        ninja.forward(length)
        ninja.right(angle)
    for j in range(corner):
        ninja.forward(length)
        ninja.left(angle)
    for k in range(corner):
        ninja.backward(length)
        ninja.left(angle)
    for l in range(corner):
        ninja.backward(length)
        ninja.right(angle)


square(300, 90, 4)
