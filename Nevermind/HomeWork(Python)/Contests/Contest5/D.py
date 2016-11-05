k = 0
A = list(input().split('.'))
if len(A) == 4:
    for elem in A:
        if not elem.isdigit():
            k = 0
            break
        elif elem.isdigit():
            elem = int(elem)
            if elem > 255:
                k = 0
                break
            else:
                k = 1
if k == 1:
    print('YES')
else:
    print('NO')
