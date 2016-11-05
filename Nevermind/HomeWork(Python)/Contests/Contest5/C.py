A = list(input().split())
T = list(A[0].split(':'))
T = list(map(int, T))
if T[0] < 10 and A[1] == 'a.m.' and T[1] < 10:
    print('0' + str(T[0]), ':', '0' + str(T[1]), sep="")
elif A[1] == 'a.m.' and T[0] == 12 and T[1] >= 10:
    print('00', ':', str(T[1]), sep="")
elif A[1] == 'a.m.' and T[0] == 12 and T[1] < 10:
    print('00', ':', '0', str(T[1]), sep="")
elif T[0] == 12 and T[1] == 0 and A[1] == 'a.m.':
    print('00', ':', '0' + str(T[1]), sep="")
elif T[0] >= 10 and A[1] == 'a.m.' and T[1] >= 10:
    print(T[0], ':', T[1], sep="")
elif T[0] < 10 and A[1] == 'a.m.' and T[1] >= 10:
    print('0' + str(T[0]), ':', T[1], sep="")
elif T[0] >= 10 and A[1] == 'a.m.' and T[1] < 10:
    print(T[0], ':', '0' + str(T[1]), sep="")
elif A[1] == 'p.m.' and T[0] != 12 and T[1] < 10:
    print(T[0]+12, ':', '0' + str(T[1]), sep="")
elif A[1] == 'p.m.' and T[0] != 12 and T[1] >= 10:
    print(T[0]+12, ':', T[1], sep="")
elif A[1] == 'p.m.' and T[0] == 12 and T[1] < 10:
    print(T[0], ':', '0' + str(T[1]), sep="")
elif A[1] == 'p.m.' and T[0] == 12 and T[1] >= 10:
    print(T[0], ':', T[1], sep="")
