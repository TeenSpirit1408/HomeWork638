line = input()
k = 0
for i in range(len(line)):
    if line[i] == '(':
        k += 1
    elif line[i] == ')':
        k -= 1
    if k < 0:
        k = 1
        break
if k == 0:
    print('YES')
else:
    print('NO')
