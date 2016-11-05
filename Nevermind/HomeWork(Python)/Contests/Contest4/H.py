x = int(input())
y = 1
z = 0
b = 1
z = x
while x != 0:
    if x == z:
        x = int(input())
    if x > z:
        while z < x:

            y += 1
            z = x
            x = int(input())
            if y > b:
                b = y
        y = 1
    else:
        while (z > x) and (x != 0):

            y += 1
            z = x
            x = int(input())
            if y > b:
                b = y
        y = 1


print(b)
