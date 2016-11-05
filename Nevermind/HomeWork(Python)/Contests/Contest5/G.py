A = []
B = []
for i in range(8):
    k, n = list(map(int, input().split()))
    A.append(k)
    B.append(n)
for j in range(8):
    for l in range(8):
        if j != l:
            for m in range(8):
                if (A[j] == A[l]) or (B[j] == B[l]) or ((A[j] == A[l]+m) and (B[j] == B[l]+m)) or ((A[j] == A[l]-m) and (B[j] == B[l] - m)) or ((A[j] == A[l]+m) and (B[j] == B[l]-m)) or ((A[j] == A[l]-m) and (B[j] == B[l]+m)):
                    s = 1
                    break
                else:
                    s = 0
            if (A[j] == A[l]) or (B[j] == B[l]) or ((A[j] == A[l] + m) and (B[j] == B[l] + m)) or (
                (A[j] == A[l] - m) and (B[j] == B[l] - m)) or ((A[j] == A[l] + m) and (B[j] == B[l] - m)) or (
                (A[j] == A[l] - m) and (B[j] == B[l] + m)):
                break
    if (A[j] == A[l]) or (B[j] == B[l]) or ((A[j] == A[l] + m) and (B[j] == B[l] + m)) or (
        (A[j] == A[l] - m) and (B[j] == B[l] - m)) or ((A[j] == A[l] + m) and (B[j] == B[l] - m)) or (
        (A[j] == A[l] - m) and (B[j] == B[l] + m)):
        break
if s == 1:
    print('YES')
else:
    print('NO')
