import turtle

def draw_kox(l,n):
    if n == 0:
        turtle.forward(l)
    else:
        x = l / 4
        draw_kox(x, n-1)
        turtle.left(60)
        draw_kox(x, n-1)
        turtle.right(120)
        draw_kox(x, n-1)
        turtle.left(60)
        draw_kox(x, n-1)

draw_kox(500,3)
turtle.right(120)
draw_kox(500, 3)
turtle.right(120)
draw_kox(500, 3)
