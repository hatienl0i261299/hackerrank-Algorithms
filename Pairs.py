n,k = map(int,input().split())
arr = list(map(int,input().split()))
answer = 0
s = set(arr)
for v in s:
    if v + k in s:
        answer += 1
print(answer)