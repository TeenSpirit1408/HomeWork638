price, delta, m = list(map(int, input().split()))
day = 1
week = 1
money = 0
while week <= m:
    money += price
    price += delta
    day += 1
    if day == 8:
        day = 1
        week += 1
print(money)
