a = 1
n = 0
k = 0
while a != 0:
    a = int(input())
    if a > k:
        n += 1
    k = a
print(n - 1)
