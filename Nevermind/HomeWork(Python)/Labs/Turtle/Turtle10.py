import turtle


turtle.shape("turtle")


def o(x, y):
    turtle.left(x)
    turtle.forward(y)


def n(a, b):
    turtle.right(a)
    turtle.forward(b)

a = 0
while a < 3:
        for i in range(24):
            o(15, 20)
        for i in range(24):
            n(15, 20)
        turtle.left(60)
        a += 1


