n,k = map(int,input().split())
s = list(map(int,input().split()))
b = int(input())
s.remove(s[k])
a = sum(s)/2
print(int(abs(a-b)) if a < b else "Bon Appetit")