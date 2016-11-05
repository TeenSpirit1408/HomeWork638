import turtle


turtle.shape("turtle")


def o(x, y):
    turtle.left(360/x)
    turtle.forward(y)


def n(a, b):
    turtle.right(360/a)
    turtle.forward(b)

turtle.left(90)
s = 0
p = 20
while s < 10:
    for i in range(25):
        o(25, p)
    for j in range(25):
        n(25, p)
    p += 5
    s += 1

