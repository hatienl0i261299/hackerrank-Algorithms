#!/bin/python3

import os
import sys

#
# Complete the countApplesAndOranges function below.
#
def countApplesAndOranges(s, t, a, b, apples, oranges):
    avf = []
    ovf = []
    for v in apples:
        if (a+v)>=s and (a+v)<=t:
            avf.append(v)
    for g in oranges:
        if (b+g)<=t and (b+g)>=s:
            ovf.append(g)
    print (len(avf))
    print (len(ovf))

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apple = list(map(int, input().rstrip().split()))

    orange = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apple, orange)
