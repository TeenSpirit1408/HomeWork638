k = 0
c = 1
a = int(input())
b = int(input())
if (a != 0) and (b != 0):
    while c != 0:
        c = int(input())
        if c == 0:
            break
        if (b > a) and (b > c):
            k += 1
        a, b = b, c
print(k)
