n = int(input())
rank1 = []
rank2 = []
height, weight = list(map(float, input().split()))
rank1.append(weight)
rank2.append(height)
for i in range(n - 1):
    height, weight = list(map(float, input().split()))
    for j in range(len(rank1)):
        if weight < rank1[j]:
            safe_zone1 = rank1[-1]
            safe_zone2 = rank2[-1]
            for k in range(len(rank1) - 1, j, -1):
                rank1[k] = rank1[k-1]
                rank2[k] = rank2[k-1]
            rank1[j] = weight
            rank2[j] = height
            rank1.append(safe_zone1)
            rank2.append(safe_zone2)
            break
        elif weight == rank1[j]:
            safe_zone1 = rank1[-1]
            safe_zone2 = rank2[-1]
            for k in range(len(rank1) - 1, j, -1):
                rank1[k] = rank1[k - 1]
                rank2[k] = rank2[k - 1]
            rank1[j] = weight
            rank2[j] = height
            rank1.append(safe_zone1)
            rank2.append(safe_zone2)
            if height > rank2[j]:
                break
            else:
                if j != len(rank2) - 1:
                    while rank2[j] < rank2[j+1]:
                        rank1[j], rank1[j+1] = rank1[j+1], rank1[j]
                        rank2[j], rank2[j+1] = rank2[j+1], rank2[j]
                        j += 1
                        if j == len(rank2) - 1:
                            break
                    break
        elif weight > rank1[j] and j == len(rank1) - 1:
            rank1.append(weight)
            rank2.append(height)
            break

for i in range(n):
    print("%.2f" % (rank2[i]), "%.3f" % (rank1[i]))
