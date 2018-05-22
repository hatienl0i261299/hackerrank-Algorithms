
#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    totalXs = 0
    maximumA = max(a)
    minimumB = max(b)
    counter = 1
    multipleofmaxA = maximumA
    while multipleofmaxA <= minimumB:
        factorOfAll = True
        for item in a:
            if multipleofmaxA % item != 0:
                factorOfAll = False
                break
        if factorOfAll:
            for item in b:
                if item % multipleofmaxA != 0:
                    factorOfAll = False
                    break
        if factorOfAll:
            totalXs += 1
        counter += 1
        multipleofmaxA = maximumA * counter
    return totalXs

if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    print(getTotalX(a,b))
