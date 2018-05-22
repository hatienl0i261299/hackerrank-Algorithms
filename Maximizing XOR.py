def solve(l,r):
    max_xor = 0
    for low in range(l,r+1):
        for high in range(low,r+1):
            max_xor = max(max_xor,low^high)
    return max_xor
if __name__ == '__main__':
    l = int(input())
    r = int(input())
    print(solve(l,r))