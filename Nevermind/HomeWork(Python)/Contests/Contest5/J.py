def nickelback(n, money):
    coins = 0
    maxcoins = 0
    for i in range(n):
        if money[i] != 5:
            nb = (money[i] - 5) / 5
            coins += nb
            if coins > maxcoins:
                maxcoins = coins
        else:
            coins -= 1
    return maxcoins


n = int(input())
money = list(map(int, input().split()))
if len(money) == n:
    if nickelback(n, money) <= 0:
        print('0')
    else:
        print(int(nickelback(n, money)))
