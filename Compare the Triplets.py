a = list(map(int,input().split()))
b = list(map(int,input().split()))
alice = 0
bob = 0
if a[0] >b[0]:
    alice += 1
elif a[0] < b[0]:
    bob += 1
if a[1] > b[1]:
    alice += 1
elif a[1] < b[1]:
    bob += 1
if a[2] > b[2]:
    alice += 1
elif a[2] < b[2]:
    bob += 1
print(alice,bob)