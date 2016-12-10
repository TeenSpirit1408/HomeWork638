def Decomp(n, k):
    if n == 0 and k == 0:
        return 1
    if n > 0 and k == 0:
        return 0
    if k <= n:
        return Decomp(n, k - 1) + Decomp(n-k, k)
    else:
        return Decomp(n, n)


n = int(input())

print(Decomp(n, n))


