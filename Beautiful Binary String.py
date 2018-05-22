if __name__ == '__main__':
    n = int(input())
    b = input().strip()
    binary = [int(c) for c in b]
    count = 0
    for i in range(2,n):
        if binary[i-2:i+1] == [0,1,0]:
            binary[i] = 1
            count += 1
    print(count)