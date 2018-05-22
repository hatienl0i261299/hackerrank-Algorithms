#!/bin/python3

import sys

def solve(n, s, d, m):
    count = 0
    for i in range(len(s) - m+1):
        count += int(sum(s[i:i + m]) == d)
    return count
n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)