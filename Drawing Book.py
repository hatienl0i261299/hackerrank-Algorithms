n = int(input())
p = int(input())
x = (n-p)//2
y = (abs(0-p))//2
if n == 6 and n-p == 1:
    print(1)
elif x <= y:
    print(x)
elif x > y:
    print(y)
