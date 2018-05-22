import sys
import bisect

def findmedian(lst):
    l = len(lst)
    if l%2 == 0:
        med = int(round(float((lst[l/2] + lst[l/2-1])/float(2))))
    else:
        med = lst[l//2]
    return med



def notification(med_arr, arr1, arr):
    notify = 0
    j = 0
    for i in arr1:
        med = findmedian(med_arr)
        if i >= med*2:
            notify += 1
        med_arr.remove(arr[j])
        j += 1
        bisect.insort(med_arr,i)

    return notify


num, d = input().strip().split(' ')
num, d = [int(num), int(d)]
arr = list(map(int, input().strip().split(' ')))

med_arr = sorted(arr[0:d])
arr1 = arr[d:]

result = notification(med_arr, arr1, arr)
print(result)