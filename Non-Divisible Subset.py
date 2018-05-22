def solve(s,k,n):
    r = [0]*k
    for v in s:
        r[v%k] += 1
    result = 0
    for a in range(1,(k+1)//2):
        result += max(r[a],r[k-a])
    if k % 2 == 0 and r[k//2]:
        result += 1
    if r[0]:
        result += 1
    return result
if __name__ == '__main__':
    n,k = map(int,input().split())
    s = list(map(int,input().split()))
    print(solve(s,k,n))