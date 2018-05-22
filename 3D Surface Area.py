def solve(arr,height,width):
    t = height*width*2
    for i in range(height):
        for j in range(width):
            if i == 0:
                t += arr[i][j]
            if j == 0:
                t += arr[i][j]
            if i == height - 1:
                t += arr[i][j]
            if j == width - 1:
                t += arr[i][j]
            if j != 0:
                t += abs(arr[i][j] - arr[i][j-1])
            if i != 0:
                t += abs(arr[i][j] - arr[i-1][j])
    return t
arr = []
height,width = map(int,input().split())
for i in range(height):
    arr.append(list(map(int,input().split())))
print(solve(arr,height,width))