a = int(input())
imin = 0
jmin = 0
A = list(map(int, input().split()))
if len(A) == a:
    min = max(A)
    for i in range(a):
        for j in range(i+1, a):
            if abs(A[i] - A[j]) < min:
                min = abs(A[i] - A[j])
                imin = i
                jmin = j
    print(imin, jmin)
