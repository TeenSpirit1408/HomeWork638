N, M = list(map(int, input().split()))
N += 1
M += 1

A = [[0]*N for i in range(M)]

A[0][0] = 1
for i in range(M):
    for j in range(N):
        if i != 0 or j != 0:
            if i == 0:
                A[i][j] += A[i][j-1]
            elif j == 0:
                A[i][j] += A[i-1][j]
            else:
                A[i][j] += (A[i-1][j] + A[i][j-1])

print(A[-1][-1])
