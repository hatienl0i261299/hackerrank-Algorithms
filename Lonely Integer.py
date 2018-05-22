if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int,input().split()))
    for i in numbers:
        if numbers.count(i) % 2 != 0:
            print(i)
            break