def solve(t,n,c,m):
    x = n/c
    curr = x
    count = 0
    while curr >= m:
        wrappers = int(curr/m)
        x += wrappers
        curr = wrappers + (curr % m)
    return int(x)
t = int(input())
for _ in range(t):
    n,c,m = map(int,input().split())
    print(solve(t,n,c,m))