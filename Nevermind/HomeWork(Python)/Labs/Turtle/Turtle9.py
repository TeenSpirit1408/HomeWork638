import turtle
import math


def r(s, a):
    turtle.left(360 / a)
    turtle.forward(s)

a = 15
x = 45
b = 3
turtle.left(30)
turtle.goto(0, 0)

for i in range(1, 10):
    turtle.left(math.fabs(360/(b+1) - 360/b)/2)
    for j in range(0, b):
        turtle.shape("turtle")
        r(x, b)
        j += 1
    turtle.penup()
    turtle.goto(a, 0)
    turtle.pendown()
    b += 1
    i += 1
    x += 10
    a += 23
