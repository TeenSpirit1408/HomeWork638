import turtle
turtle.speed('fastest')

def draw_dragon(l, n, an = 45):
    if n == 0:
        turtle.forward(l)
    else:
        x = l/2
        turtle.right(an)
        draw_dragon(x, n-1, 45)
        turtle.left(an * 2)
        draw_dragon(x, n-1, -45)
        turtle.right(an)

draw_dragon(15000, 10)
