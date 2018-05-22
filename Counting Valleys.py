def solve(n,steps):
    num = 0
    level = 0
    for i in steps:
        if i == 'U':
            level += 1
        else:
            if level == 0:
                num += 1
            level -= 1
    return num
if __name__ == '__main__':
    n = int(input())
    steps = input().strip()
    print(solve(n,steps))