#!/bin/python3

import os
import sys

def breakingRecords(score,n):
    minBroken = 0
    maxBriken = 0
    if len(score) > 1:
        minRecord = score[0]
        maxRecord = score[0]
        for i in range(n):
            if score[i] < minRecord:
                minRecord = score[i]
                minBroken += 1
            if score[i] > maxRecord:
                maxRecord = score[i]
                maxBriken += 1
    return (maxBriken,minBroken)

if __name__ == '__main__':
    n = int(input())
    score = list(map(int, input().rstrip().split()))
    print(*breakingRecords(score,n))
