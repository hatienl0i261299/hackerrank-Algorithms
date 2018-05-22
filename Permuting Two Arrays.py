def solve(k,a,b):
    for i in range(len(a)):
        if a[i] + b[i] < k:
            return False
    return True
q = int(input())
for _ in range(q):
    n,k = map(int,input().split())
    a = sorted(list(map(int,input().split())))
    b = sorted(list(map(int,input().split())))
    b.reverse()
    if solve(k,a,b):
        print("YES")
    else:
        print("NO")