a = int(input())


b = 0
c = 1
for i in range(1, a):
    c += b
    b = c - b
print(c)
