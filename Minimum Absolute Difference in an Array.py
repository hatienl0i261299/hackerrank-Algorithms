if __name__ == '__main__':
    n = int(input())
    numbers = sorted(list(map(int,input().split())))
    lst = []
    for x,y in zip(numbers,numbers[1:]):
        lst.append(abs(x-y))
    print(min(lst))