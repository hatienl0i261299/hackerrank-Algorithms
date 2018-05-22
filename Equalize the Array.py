import collections
n = int(input())
lst = list(map(int,input().split()))
lst = collections.Counter(lst)
print(n - max(lst.values()))