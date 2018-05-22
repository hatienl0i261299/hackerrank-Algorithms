#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    k1 = x1
    k2 = x2
    if x2 > x1 and v2 > v1:
        return "NO"
    else:
        while k1 != k2:
            k1 += v1
            k2 += v2
            if k1 == k2:
                return "YES"

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)