x = 0
y = 0
A = [0, 0]
while True:
    A = list(input().split())
    if A[0] == 'Treasure!':
        break
    A[-1] = int(A[1])
    if A[0] == 'North':
        y += A[1]
    elif A[0] == 'South':
        y -= A[1]
    elif A[0] == 'East':
        x += A[1]
    elif A[0] == 'West':
        x -= A[1]
    A = [0, 0]
print(x, y)

