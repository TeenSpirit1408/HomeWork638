a = 0
k = 0

while True:
    a = int(input())
    if a == 0:
        a = int(input())
        if a == 0:
            break
    k += a


print(k)
