a = int(input())


b = 1
c = 1
k = 3
while (b + c) < a:
    c += b
    b = c - b
    k += 1
if (b + c) == a:
    print(k)
else:
    print(-1)
