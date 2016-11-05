a = int(input())
if a <= 10:
    n = 45 * a
    if a % 2 == 0:
        n += (a // 2 * 20) - 15
    else:
        n += (a // 2 * 20)
print(9 + (n // 60), n % 60)
