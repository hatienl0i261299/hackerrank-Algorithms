n = int(input())
arr = list(map(int,input().split()))
s = []
for i in range(n):
    for j in range(n):
        if arr[i] == arr[j] and i != j:
            x = abs(j-i)
            s.append(x)
try:
    print(min(s))
except:
    print(-1)