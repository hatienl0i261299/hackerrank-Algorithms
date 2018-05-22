b,n,m = map(int,input().split())
keyboard = list(map(int,input().split()))
drivers = list(map(int,input().split()))
tong = []
for i in keyboard:
    for j in drivers:
        if i + j <= b:
            tong.append(i+j)
print(max(tong) if tong != [] else -1)