def solve(n):
    count = 0
    r = int(n)
    for i in n:
        try:
            if r % int(i) == 0:
                count += 1
        except:
            pass
    return count

if __name__ == '__main__':
    for _ in range(int(input())):
        n = input()
        print(solve(n))
