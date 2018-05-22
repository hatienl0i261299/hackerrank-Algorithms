#!/bin/python
def insertionSort(ar):
    for i in range(1, len(ar)):
        temp = ar[i]
        j = i
        while j > 0 and temp < ar[j-1]:
            ar[j] = ar[j-1]
            j -= 1
        ar[j] = temp
        print(' '.join(str(j) for j in ar))

m = input()
ar = [int(i) for i in input().strip().split()]
insertionSort(ar)