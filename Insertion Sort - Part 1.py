#!/bin/python
def insertionSort(ar):
    num = ar[-1]
    for i in range(m-2, -1, -1):
        if ar[i] > num:
            ar[i+1] = ar[i]
            print(" ".join(str(j) for j in ar))
        else:
            ar[i+1] = num
            print(" ".join(str(j) for j in ar))
            return
    ar[0] = num
    print(" ".join(str(j) for j in ar))
    return

m = int(input())
ar = [int(i) for i in input().strip().split()]
insertionSort(ar)