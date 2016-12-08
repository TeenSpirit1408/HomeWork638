#n, A, k = list(map(int, input().split()))
n = int(input())
A = int(input(), n)
k = int(input())
digit_str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
right_chislo = ''

while A != 0:
    c = A % k
    for i in range(len(digit_str)):
        if c == i:
            c = str(digit_str[i])
            break
    right_chislo = str(c) + right_chislo
    A //= k

print(right_chislo)
