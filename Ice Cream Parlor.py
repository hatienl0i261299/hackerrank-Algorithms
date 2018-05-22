def solve(m,n,cost):
    for idx in range(len(cost)-1):
        for idx2 in range(idx+1,len(cost)):
            if cost[idx] + cost[idx2] == m:
                return [idx+1,idx2+1]
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        m = int(input())
        n = int(input())
        cost = list(map(int,input().split()))
        print(*solve(m,n,cost))