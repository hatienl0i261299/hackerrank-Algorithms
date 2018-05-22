n = int(input())
arr = []
res = [[[0] for i in range(n)] for j in range(n)]
for i in range(n):
    arr.append(list(input().strip()))
for i in range(1,n-1):
    for j in range(1,n-1):
        t = arr[i][j]
        if t > arr[i-1][j] and t > arr[i][j-1]and t > arr[i+1][j] and t > arr[i][j+1]:
            res[i][j] = 'X'
for i in range(n):
    for j in range(n):
        if res[i][j] == 'X':
            arr[i][j] = 'X'
for i in arr:
    print(''.join(i))
