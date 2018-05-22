#!/bin/python3

import sys

def howManyGames(p, d, m, s):
    count=0
    a=0
    curr = p
    while s >= curr:
        count += 1
        s -= curr
        if curr - d >= m:
            curr -= d
        else:
            curr = m
    return count
if __name__ == "__main__":
    p, d, m, s = input().strip().split(' ')
    p, d, m, s = [int(p), int(d), int(m), int(s)]
    answer = howManyGames(p, d, m, s)
    print(answer)