n = int(input())
sticks = list(map(int,input().split()))
sticks = sorted(sticks)
flag = False
for i in range(n-1,-1,-1):
    for j in range(i-1,-1,-1):
        for k in range(j-1,-1,-1):
            if sticks[j] + sticks[k] > sticks[i]:
                print(' '.join(str(e) for e in [sticks[k],sticks[j],sticks[i]]))
                flag = True
                break
        if flag:
            break
    if flag:
        break
if not flag:
    print(-1)