if __name__ == '__main__':
    n = int(input())
    numbers = sorted(list(map(int,input().split())))
    numbers.reverse()
    sum = 0
    j = 0
    for i in numbers:
        sum += (i*(2**j))
        j+=1
    print(sum)