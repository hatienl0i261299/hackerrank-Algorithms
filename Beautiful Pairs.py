from math import *
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
da = {}
db = {}
ask = []
cost = 0
for i in a:
    if i in da:
        da[i] +=1
    else:
        da[i] = 1
        ask.append(i)
for j in b:
    if j in db:
        db[j] += 1
    else:
        db[j] = 1
for k in da:
    if k in db:
        cost += min(da[k],db[k])
if cost == n:
    cost -= 1
else:
    cost += 1
print(cost)