a = int(input())
n = a
k = 1
l = 1
while a != 0:
    a = int(input())
    if a == n:
        k += 1
        if k > l:
            l = k
    else:
        k = 1
    n = a
print(l)
