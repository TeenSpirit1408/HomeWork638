import turtle

def draw_minkov(l,n):
    if n == 0:
        turtle.forward(l)
    else:
        x = l/4
        draw_minkov(x, n-1)
        turtle.left(90)
        draw_minkov(x, n-1)
        turtle.right(90)
        draw_minkov(x, n-1)
        turtle.right(90)
        draw_minkov(x, n-1)
        draw_minkov(x, n-1)
        turtle.left(90)
        draw_minkov(x, n-1)
        turtle.left(90)
        draw_minkov(x, n-1)
        turtle.right(90)
        draw_minkov(x, n-1)

draw_minkov(400, 2)