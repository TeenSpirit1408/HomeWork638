a = 1
n = 0
k = 0
while a != 0:
    a = int(input())
    if a > n:
        k = n
        n = a
    elif (a > k) and (a < n):
        k = a
print(k)
