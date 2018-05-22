def solve(n,arr):
    arr_sort = sorted(arr)
    diffcount = 0
    diff1 = -1
    diff2 = -1
    for i in range(n):
        if arr_sort[i] != arr[i]:
            diffcount += 1
            if diff1 == -1:
                diff1 = i
            elif diffcount > 1:
                diff2 = i
            lastdiff = i
    if diffcount == 2:
        arr[diff1],arr[diff2] = arr[diff2],arr[diff1]
        if arr == arr_sort:
            print('yes')
            print("swap {} {}".format(diff1+1,diff2+1))
        else:
            print("no")
    elif diffcount > 2:
        arr = arr[:diff1] + arr[diff1:diff2+1][::-1] + arr[diff2+1:]
        if arr == arr_sort:
            print("yes")
            print("reverse {} {}".format(diff1+1,diff2+1))
        else:
            print("no")
    elif arr == arr_sort:
        print("yes")

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    solve(n,arr)