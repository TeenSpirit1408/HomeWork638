im = 0
jm = 0
n = 0
k = 1
c = 1
a = int(input())
b = int(input())
if (a != 0) and (b != 0):
    n = 100
    i = 1
    while c != 0:
        c = int(input())
        if c == 0:
            break
        i += 1
        if (b > a) and (b > c):
            jm = im
            im = i
            if ((im - jm) < n) and (jm != 0):
                n = im - jm
        a, b = b, c
if (im == 0) or (jm == 0):
    n = 0
print(n)
