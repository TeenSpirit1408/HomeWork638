import turtle


turtle.shape("turtle")


turtle.begin_fill()
for i in range(100):
    turtle.left(360 / 100)
    turtle.forward(10)
turtle.color("yellow")
turtle.end_fill()


turtle.goto(-90, 200)


turtle.color("Black")
turtle.begin_fill()
for i in range(50):
    turtle.left(360 / 50)
    turtle.forward(3)
turtle.color("blue")
turtle.end_fill()


turtle.penup()
turtle.goto(90, 200)


turtle.pendown()
turtle.color("Black")
turtle.begin_fill()
for i in range(50):
    turtle.left(360 / 50)
    turtle.forward(3)
turtle.color("blue")
turtle.end_fill()


turtle.penup()
turtle.goto(0, 170)


turtle.pendown()
turtle.color("Black")
turtle.width(20)
turtle.goto(0, 120)


turtle.penup()
turtle.goto(85, 110)


turtle.pendown()
turtle.right(90)
turtle.color("Red")
turtle.begin_fill()
for i in range(25):
    turtle.right(360 / 50)
    turtle.forward(11)
