def proverka(a):
    k = 0
    while a != 0:
        a //= 10
        k += 1
    if k >= 4:
        return True
    else:
        return False


a = 1
b = 1
n = 0
while a != 0 and b != 0:
    a, b = list(map(int, input().split()))
    if a % 2 == 0 and b % 7 == 0 and (proverka(a) or proverka(b)):
        n += 1

print(n)
