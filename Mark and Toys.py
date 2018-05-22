n,k = map(int,input().split())
cost = sorted(list(map(int,input().split())))
count = 0
prices = 0
for i in cost:
    if i + prices <= k:
        count += 1
        prices += i
    else:
        break
print(count)