def max_dlina(a, X, Y):
    max = 0
    for i in range(a):
        for j in range(a):
            if ((A[i]-A[j])**2 + (B[i]-B[j])**2)**0.5 > max:
                max = ((A[i]-A[j])**2 + (B[i]-B[j])**2)**0.5
    return max

a = int(input())
A = []
B = []
for i in range(a):
    k, n = list(map(float, input().split()))
    A.append(k)
    B.append(n)
print(max_dlina(a, A, B))
