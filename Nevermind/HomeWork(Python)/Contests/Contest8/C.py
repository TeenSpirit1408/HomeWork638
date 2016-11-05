n = int(input())
Ans = list(map(int, input().split()))
a = 1
b = 0
knights = 1
liars = 0
for i in range(len(Ans) - 1):
    if Ans[i] == 1 and a == 1:
        a = 1
        b = 0
        knights += 1
    elif Ans[i] == 1 and b == 1:
        a = 0
        b = 1
        liars += 1
    elif Ans[i] == 0 and a == 1:
        a = 0
        b = 1
        liars += 1
    elif Ans[i] == 0 and b == 1:
        a = 1
        b = 0
        knights += 1
if ((Ans[-1] == 1) and (a == 1)) or ((Ans[-1] == 0) and (b == 1)):
    knights = min(knights, liars)
else:
    knights = 0
print(knights)
