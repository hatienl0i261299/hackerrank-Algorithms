def solve(s):
    return True if list(s) == sorted(s) else False
if __name__ == '__main__':
    for _ in range(int(input())):
        arr = (sorted(input()) for _ in range(int(input())))
        zipp = (solve(z) for z in zip(*arr))
        print(["NO","YES"][all(zipp)])
