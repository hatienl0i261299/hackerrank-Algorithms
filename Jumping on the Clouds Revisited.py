n,k = map(int,input().split())
arr = list(map(int,input().split()))
print(100 - sum(1+2*arr[i] for i in range(0,n,k)))