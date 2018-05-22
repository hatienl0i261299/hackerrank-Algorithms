if __name__ == '__main__':
    i,j,k = map(int,input().split())
    rev = []
    count = 0
    for a in range(i,j+1):
        if abs((a - int(str(a)[::-1]))) % k == 0:
            count += 1
    print(count)