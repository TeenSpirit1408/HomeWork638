import turtle

def draw_levi(l,n):
    if n == 0:
        turtle.forward(l)

    else:
        turtle.left(45)
        draw_levi(l*(2**0.5)/2, n-1)
        turtle.right(90)
        draw_levi(l*(2**0.5)/2, n-1)
        turtle.left(45)

draw_levi(400, 3)
