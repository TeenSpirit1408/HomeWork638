N, A, B, C, D = list(map(int, input().split()))
a = [i for i in range(1, N+1)]
a[A-1:B] = reversed(a[A-1:B])
a[C-1:D] = reversed(a[C-1:D])
print(*a)
