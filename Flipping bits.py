def solve(num):
    return num^(pow(2,32)-1)
if __name__ == '__main__':
    for _ in range(int(input())):
        num = int(input())
        print(solve(num))