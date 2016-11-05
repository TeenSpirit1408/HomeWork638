def max_chislo(n):
    k = 0
    while n != 0:
        n //= 10
        k += 1
    return k

n = int(input())
massive = list(map(int, input().split()))
k = max_chislo(max(massive)) - 1
while k != -1:
    A = []
    for i in range(10):
        A.append([])
    for i in range(len(massive)):
        for j in range(10):
            if (massive[i] // 10 ** k) % 10 == j:
                A[j].append(massive[i])
    massive_true = []
    for i in range(10):
        for j in range(len(A[i])):
            massive_true.append(A[i][j])
    massive = massive_true
    k -= 1
print(*massive)
