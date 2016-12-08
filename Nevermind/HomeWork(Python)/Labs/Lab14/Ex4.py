maximum1 = 0
maximum2 = 0
k1 = 0
k2 = 0
N = int(input())
popular = []
product = []

for i in range(N):
    a = int(input())
    if a not in product:
        product.append(a)
        popular.append(int(1))
    else:
        for j in range(len(product)):
            if product[j] == a:
                popular[j] += 1

print(popular)

for t in range(len(popular)):
    if popular[t] > maximum1:
        k2 = k1
        maximum2 = maximum1
        k1 = 1
        maximum1 = popular[t]
    elif popular[t] == maximum1:
        k1 += 1
    elif popular[t] > maximum2:
        k2 = 1
        maximum2 = popular[t]
    elif popular[t] == maximum2:
        k2 += 1

print(k1, k2)
