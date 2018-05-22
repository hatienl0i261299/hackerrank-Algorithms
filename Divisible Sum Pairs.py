n,k = map(int,input().split())
a = list(map(int,input().strip().split()))
count = 0
for i in range(n):
    for j in range(i+1,len(a)):
        if (a[i] + a[j]) % k == 0:
            count += 1
print(count)