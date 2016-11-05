a = 1
n = 0
k = 1
while a != 0:
    a = int(input())
    if a > n:
        n = a
        k = 1
    elif a == n:
        k += 1
print(k)
