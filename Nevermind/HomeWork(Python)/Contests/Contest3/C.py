x = int(input())
p = int(input())
y = int(input())
year = 0
while x < y:
    year += 1
    x += ((x/100)*p)
    x = (x*100)//1/100
print(year)
