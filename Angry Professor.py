if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,k = map(int,input().split())
        times = list(map(int,input().split()))
        ontime = [int(temp) for temp in times if int(temp) <= 0]
        if len(ontime) < k:
            print("YES")
        else:
            print("NO")