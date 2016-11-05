a, b = list(input().split())
a = int(a, 16)
b = int(b, 16)
c = a ^ b
print('{0:x}'.format(c))
