n = int(input())
k = 0
if n != 0:
    while n != 1:
        if n % 2 == 1:
            k += 1
        n //= 2
    print(k+1)
else:
    print(k)
