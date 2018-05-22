n = int(input())
candles = list(map(int,input().split()))
max = max(candles)
count = 0
for i in candles:
    if i == max:
        count += 1
print(count)