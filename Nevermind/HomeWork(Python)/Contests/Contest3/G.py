a = 1
n = 0
l = 0
k = 0


while a != 0:
    a = int(input())
    n += a**2
    l += a
    k += 1


b = l / (k-1)
print((n/(k-2) - (2*l*b)/(k-2) + (k-1)*(b**2)/(k-2))**0.5)
