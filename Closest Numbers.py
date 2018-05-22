#!/usr/bin/py
from sys import maxsize


def closest(a):
    a.sort()
    smallest_difference = maxsize
    smallest_pairs = []

    for idx in range(len(a) - 1):
        diff = a[idx + 1] - a[idx]
        if diff < smallest_difference:
            smallest_difference = diff
            smallest_pairs = [(a[idx], a[idx + 1])]
        elif diff == smallest_difference:
            smallest_pairs.append((a[idx], a[idx + 1]))

    for pair in smallest_pairs:
        print(pair[0], pair[1],end=' ')


if __name__ == '__main__':
    n = input()
    vec = list(map(int, input().split()))
    closest(vec)