def solve(n,arr):
    inv = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                inv += 1
    if inv % 2 == 0:
        return "YES"
    else:
        return "NO"
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        print(solve(n,arr))