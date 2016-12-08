n = 1
maximum = 0
k = 0
while n != 0:
    n = int(input())
    if n > maximum:
        k = 1
        maximum = n
    elif n == maximum:
        k += 1

print(k)
