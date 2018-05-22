def solve(arr,v):
    for i in range(len(arr)):
        if arr[i] == v:
            return i
    return -1
if __name__ == '__main__':
    v = int(input())
    n = int(input())
    arr = list(map(int,input().split()))
    print(solve(arr,v))