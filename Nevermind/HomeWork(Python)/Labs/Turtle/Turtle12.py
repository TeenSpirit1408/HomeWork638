import turtle


turtle.shape("turtle")


def o(x, y):
    turtle.right(360/x)
    turtle.forward(y)


def n(a, b):
    turtle.right(360/a)
    turtle.forward(b)

turtle.left(90)
s = 0
while s < 10:
    for i in range(15):
        o(30, 10)
    for j in range(5):
        n(10, 10)
