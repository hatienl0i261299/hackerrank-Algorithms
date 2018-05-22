n = int(input())
arr = list(map(int,input().split()))
cnt = 0
for i in range(n-1):
    if arr[i] % 2 == 1:
        arr[i] += 1
        arr[i+1] += 1
        cnt += 2
if arr[-1] % 2 == 1:
    print("NO")
else:
    print(cnt)