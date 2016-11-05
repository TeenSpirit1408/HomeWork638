d, n = list(map(int, input().split()))
k = 0
while n != 0:
    if n % 10 == d:
        k += 1
    n //= 10
print(k)
